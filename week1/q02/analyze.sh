#!/usr/bin/env bash

csv_file="$1"

if [ ! -f "$csv_file" ]; then
    echo "Error: File '$csv_file' not found." >&2
    exit 1
fi

echo "=== Top 2 5xx Paths ==="
awk -F',' 'NR>1 && $4 >= 500 {print $3}' "$csv_file" \
    | sort \
    | uniq -c \
    | sort -k1,1rn -k2,2 \
    | head -n 2

echo ""
echo "=== Average Latency ==="

awk -F',' 'NR>1 {sum += $5; count++} END {printf "%.2f\n", sum/count}' "$csv_file"
