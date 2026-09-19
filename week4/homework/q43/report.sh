#!/usr/bin/env bash
set -euo pipefail
curl -fsS http://127.0.0.1:8080/inventory.json | \
jq -r '
  ["name","category","price","stock"],
  (.[] | select(.stock < 10) | [.name, .category, .price, .stock])
  | @csv
' | sort -t, -k3,3nr > inventory_low.csv
