#!/usr/bin/env bash
set -euo pipefail
jq -r '
  group_by(.region)
  | map({region: .[0].region, total: (map(.amount) | add)})
  | sort_by(-.total)
  | .[] | "- \(.region): \(.total)"
' sales.json > sales_summary.md
