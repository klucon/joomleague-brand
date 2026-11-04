# JoomLeague Brand Kit validation

## Local validation

```bash
./developer/tools/validate-brand-kit.sh
```

This creates:

```text
validation-reports/
├── validation-report.json
└── validation-report.md
```

## Report modes

```bash
python3 developer/tools/validate_brand_kit.py --report json
python3 developer/tools/validate_brand_kit.py --report markdown
python3 developer/tools/validate_brand_kit.py --report both
```

Custom output directory:

```bash
python3 developer/tools/validate_brand_kit.py   --report both   --output-dir build/brand-validation
```

## CI-equivalent local run

```bash
./developer/tools/ci-validate.sh
```

## GitHub Actions

Workflow:

```text
.github/workflows/validate-brand-kit.yml
```

It validates the kit on relevant pushes and pull requests, writes both report formats,
adds the Markdown report to the Actions job summary, and uploads the reports as an artifact.

## Exit codes

- `0` validation passed
- `1` asset validation failed
- `2` environment/runtime failure

## Dependency

```bash
sudo apt install python3-pil
```

or:

```bash
python3 -m pip install Pillow
```
