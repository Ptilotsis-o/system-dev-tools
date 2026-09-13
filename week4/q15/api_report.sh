#!/usr/bin/env bash
set -euo pipefail

URL="http://127.0.0.1:8000/packages.json"
OUT="summary.md"

curl -fsS "$URL" | jq -r '
  [ .[] | select(.status == "active" and .downloads >= 100) ]
  | sort_by([-.downloads, .name])
  | ["name", "version", "downloads"] as $header
  | "# Active Packages\n",
    "| " + ($header | join(" | ")) + " |",
    "| --- | --- | --- |",
    ( .[] | "| \(.name) | \(.version) | \(.downloads) |" )
' > "$OUT"
