@echo off
if not exist backups mkdir backups

copy db.sqlite3 backups\db_backup.sqlite3

echo Backup completed.
pause