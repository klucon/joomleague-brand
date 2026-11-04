#!/usr/bin/env sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
cd "$ROOT"
python3 developer/tools/validate_brand_kit.py . --report both --output-dir validation-reports
