@echo off

if not exist release mkdir release

echo Sports School Release > release\release-info.txt
echo Version: 0.1.1 >> release\release-info.txt

echo Release package created.
pause