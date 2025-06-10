# Brown Dust 2 Repacker (Android version)
A simple tool useful to mod [Brown Dust 2](https://www.browndust2.com/en-us/) bundles. Thanks to Bingle and Seggss&AN for the help with this repacker.


#### NOTE: This tool only works with .skel files, not with .json files. And it uses an external [ASTC encoder](https://github.com/ARM-software/astc-encoder) developed by ARM-software.

## Before to use this tool:

  - Double-click on `0_INSTALL_REQUIREMENTS.bat` to install the required dependencies and Python 3.13.
  - Download and install [Microsoft C++ Build Tools](https://aka.ms/vs/17/release/vs_BuildTools.exe), and after that install the necessary dependencies following [this video guide](https://files.catbox.moe/vqsuix.mp4).



## Usage for repack:

1. Check out [this list](https://kxdekxde.github.io/bd2-parentfolders/characters.html) to know which folders you need to copy from your Android device to your PC. 
2. Copy those folders from your Android device to the repacker **`Backup`** folder.
3. Update your game.
4. After you finished to update your game, copy the folders once again but this time from your Android device to the repacker **`Original Bundles`** folder.
5. Double-click on _0___REPACKER.bat_ to start the repacking process. And now just wait, the Terminal window will display when the repacking process is done.
6. If everything worked with no issues you will see your repacked mods saved with their respective folders in the folder **`Repacked`**.
7. Move those folders from **`Repacked`** back to your Android device in `Android/data/com.neowizgames.game.browndust2/files/UnityCache/Shared/`.
8. Replace and that's it.

NOTE: The script _Z___clean_folders.py_ is just to clean the folders used by the tool when you finished to repack your mods, so you can just ignore this script and delete the files or folders you don't need anymore manually. This script doesn't clean the folders **`Repacked`** and **`Backup`**.


## Usage to install mods:

1. Check out [this list](https://kxdekxde.github.io/bd2-parentfolders/characters.html) to know which folders you need to copy from your Android device to your PC. 
2. Copy those folders from your Android device to the repacker folders **`Original Bundles`** and **`Modded Bundles`**.
3. Run _1_1__delete_unnecessary_files.py_ to remove any not necessary file inside these folders.
4. Run _3___add_bundle_extension.py_.
5. Run _4___extract_assets.py_ and wait until the process finishes.
6. Here I got [some modded assets](https://mega.nz/folder/kDsGiCDC#aTgZj_2lQJ4Qxj4NI-duYg) to use as sample. Or you can download any other mod where the creator provided the .atlas + .skel + .png assets.
7. Go to the repacker folder **`Extracted Assets`** and you will see some folders that contain the raw assets We extracted previously on step 5 (various files .atlas, .skel and .png).
8. Copy the modded assets you downloaded and paste them in their corresponding locations replacing the raw assets.
9. Run _5___repacker_LZ4_compressor__ASTC.py_ and the tool will start to repack the files using the modded assets you replaced in **`Extracted Assets`**. The Terminal window will close when the repacking process is completed.
10. Run _6___remove_bundle_extension.py_.
11. If everything worked with no issues you will see your repacked files saved in the folder **`Repacked`**.
12. Move those folders from **`Repacked`** back to your Android device in `Android/data/com.neowizgames.game.browndust2/files/UnityCache/Shared/`.
13. Replace and that's it.


## Usage to install your own mods (for modders):

If you make your own mods you can use this tool to save some time too. You can use this tool to extract/export the assets to **`Extracted Assets`** and then you can start to work with the assets from there, save the changes to the assets and when you're ready to import the assets back to the bundles you can run _5___repacker_LZ4_compressor__ASTC.py_ and _6___remove_bundle_extension.py_ and your modified files will be saved to **`Repacked`**. Then just move them back to your Android device replacing the raw ones and that's it.


Happy modding! ^‿^
