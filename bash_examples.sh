# Remove excel files older than 30 days
find . -type f -name "*.xlsx" -mtime +30 -exec rm -f {} \;
