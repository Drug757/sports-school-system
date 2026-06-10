@echo off
echo Checking project secrets...
git grep -n -i "password\|secret\|token\|api_key\|jwt"
pause