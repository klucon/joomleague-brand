# Validation workflow for Codex

Before committing any branding change, run:

```bash
./developer/tools/ci-validate.sh
```

A successful run ends with:

```text
Validation PASSED.
```

Reports:

- `validation-reports/validation-report.json`
- `validation-reports/validation-report.md`

GitHub runs the same check through:

`.github/workflows/validate-brand-kit.yml`

Codex should treat exit code `1` as a blocking error and fix the asset set before continuing.
