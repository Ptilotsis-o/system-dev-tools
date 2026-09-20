#!/usr/bin/env bash
set -euo pipefail
jq 'map(.version += 1)' config.json > config_new.json
diff -u config.json config_new.json > config.diff || true
