from PIL import Image
import os, gc
import UnityPy
import subprocess
import tempfile

# Configure UnityPy fallback version
UnityPy.config.FALLBACK_UNITY_VERSION = '2022.3.22f1'
ADD_PADDING = False

# Change the working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Paths for various folders
modded_assets_base_folder = os.path.join(script_dir, "Extracted Assets")
original_bundles_folder = os.path.join(script_dir, "Original Bundles")
repacked_base_folder = os.path.join(script_dir, "Repacked")

def find_modded_asset(filename):
    """Search for modded PNG assets in Extracted Assets subfolders"""
    for root, dirs, files in os.walk(modded_assets_base_folder):
        if filename in files:
            return os.path.join(root, filename)
    return None

def free_system_resources():
    print("Freeing up system resources...")
    gc.collect()
    try:
        with open("/proc/self/statm") as f:
            mem_usage = int(f.readline().split()[1]) * 4096 / (1024 * 1024)
            print(f"Memory usage reduced to: {mem_usage:.2f} MB")
    except FileNotFoundError:
        pass
    print("System resources have been freed.")

def compress_astc(image: Image.Image, block: str, quality="-medium"):
    """Compress image to ASTC format using SSE2 version"""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.png")
        output_path = os.path.join(tmpdir, "output.astc")

        image.save(input_path)

        cmd = [
            "astcenc-sse2",
            "-cs", input_path, output_path,
            block,
            quality,
            "-yflip",
            "-decode_unorm8",
            "-silent"
        ]

        subprocess.run(cmd, check=True)

        with open(output_path, "rb") as f:
            astc_data = f.read()[16:]

        return astc_data

# Main processing loop
for root, dirs, files in os.walk(original_bundles_folder):
    for bundle_file in files:
        bundle_path = os.path.join(root, bundle_file)

        if "__data" not in bundle_file:
            continue

        try:
            env = UnityPy.load(bundle_path)
            edited = False

            for obj in env.objects:
                try:
                    if obj.type.name == "Texture2D":
                        data = obj.read()
                        file_name = data.m_Name + ".png"
                        modded_file_path = find_modded_asset(file_name)

                        if modded_file_path and os.path.exists(modded_file_path):
                            print(f"Replacing {file_name} in {bundle_path}")

                            pil_img = Image.open(modded_file_path).convert("RGBA")
                            astc_data = compress_astc(pil_img, block="4x4")

                            data.m_Width, data.m_Height = pil_img.size
                            data.m_TextureFormat = 48  # ASTC_RGB_4x4
                            data.image_data = astc_data
                            data.m_CompleteImageSize = len(astc_data)
                            data.m_MipCount = 1
                            data.m_StreamData.offset = 0
                            data.m_StreamData.size = 0
                            data.m_StreamData.path = ""

                            data.save()
                            edited = True

                    elif obj.type.name == "TextAsset":
                        data = obj.read()
                        file_name = data.m_Name
                        modded_file_path = find_modded_asset(file_name)

                        if modded_file_path and os.path.exists(modded_file_path):
                            print(f"Replacing {file_name} in {bundle_path}")
                            with open(modded_file_path, "rb") as f:
                                data.m_Script = f.read().decode("utf-8", "surrogateescape")
                            data.save()
                            edited = True

                except Exception as e:
                    print(f"Error processing asset in {bundle_file}: {e}")

            if edited:
                relative_path = os.path.relpath(bundle_path, original_bundles_folder)
                repacked_path = os.path.join(repacked_base_folder, relative_path)
                os.makedirs(os.path.dirname(repacked_path), exist_ok=True)

                try:
                    with open(repacked_path, "wb") as f:
                        bundle_data = env.file.save(packer="lz4")
                        f.write(bundle_data)

                        if ADD_PADDING:
                            current_size = f.tell()
                            padding_needed = (0x10 - (current_size % 0x10)) % 0x10
                            if padding_needed:
                                f.write(b'\x00' * padding_needed)

                    print(f"Saved modified bundle to {repacked_path}")

                except Exception as e:
                    print(f"Error saving bundle: {e}")

        except Exception as e:
            print(f"Error processing bundle {bundle_file}: {e}")

free_system_resources()