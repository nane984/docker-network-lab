#!/bin/sh
set -e

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M")
BACKUP_DIR=/backups
LOG_FILE="$BACKUP_DIR/backup.log"

mkdir -p "$BACKUP_DIR"

export PGPASSWORD="$POSTGRES_PASSWORD"

echo "[$(date)] Starting Postgres backup" >> "$LOG_FILE"

pg_dump \
  -h "$POSTGRES_HOST" \
  -U "$POSTGRES_USER" \
  "$POSTGRES_DB" \
  > "$BACKUP_DIR/db_$TIMESTAMP.sql" 2>>"$LOG_FILE"

# obriši backup fajlove starije od 7 dana
find "$BACKUP_DIR" -type f -mtime +7 -name "db_*.sql" -delete

echo "[$(date)] Backup finished" >> "$LOG_FILE"