#!/usr/bin/env sh
set -eu
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
KIT_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)
exec python3 "$SCRIPT_DIR/validate_brand_kit.py" "$KIT_ROOT" --report both --output-dir validation-reports
