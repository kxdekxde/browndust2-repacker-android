@echo off
echo Running Python Scripts...




REM Run 1_1__delete_unnecessary_files.py
python 1_1__delete_unnecessary_files.py
if %errorlevel% neq 0 (
    echo 1_1__delete_unnecessary_files.py failed
    pause
    exit /b %errorlevel%
)
echo 1_1__delete_unnecessary_files.py ran successfully



REM Run 1_2__copyfolders_backup_moddedbundles.py
python 1_2__copyfolders_backup_moddedbundles.py
if %errorlevel% neq 0 (
    echo 1_2__copyfolders_backup_moddedbundles.py failed
    pause
    exit /b %errorlevel%
)
echo 1_2__copyfolders_backup_moddedbundles.py ran successfully



REM Run 2___rename_subfolders.py
python 2___rename_subfolders.py
if %errorlevel% neq 0 (
    echo 2___rename_subfolders.py failed
    pause
    exit /b %errorlevel%
)
echo 2___rename_subfolders.py ran successfully



REM Run 3___add_bundle_extension.py
python 3___add_bundle_extension.py
if %errorlevel% neq 0 (
    echo 3___add_bundle_extension.py failed
    pause
    exit /b %errorlevel%
)
echo 3___add_bundle_extension.py ran successfully



REM Run 4___extract_assets.py
python 4___extract_assets.py
if %errorlevel% neq 0 (
    echo 4___extract_assets.py failed
    pause
    exit /b %errorlevel%
)
echo 4___extract_assets.py ran successfully



REM Run 5___repacker_LZ4_compressor__ASTC.py
python 5___repacker_LZ4_compressor__ASTC.py
if %errorlevel% neq 0 (
    echo 5___repacker_LZ4_compressor__ASTC.py failed
    pause
    exit /b %errorlevel%
)
echo 5___repacker_LZ4_compressor__ASTC.py ran successfully



REM Run 6___remove_bundle_extension.py
python 6___remove_bundle_extension.py
if %errorlevel% neq 0 (
    echo 6___remove_bundle_extension.py failed
    pause
    exit /b %errorlevel%
)
echo 6___remove_bundle_extension.py ran successfully



echo All scripts ran successfully.
pause
