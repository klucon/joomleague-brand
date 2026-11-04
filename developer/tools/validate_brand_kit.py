#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow is required. Install with: python3 -m pip install Pillow", file=sys.stderr)
    sys.exit(2)

EXPECTED_RASTER_SIZES = {
    "favicons/favicon-16x16.png": (16, 16),
    "favicons/favicon-32x32.png": (32, 32),
    "favicons/favicon-48x48.png": (48, 48),

    "favicons/apple-touch-icon.png": (180, 180),
    "favicons/apple-touch-icon-120x120.png": (120, 120),
    "favicons/apple-touch-icon-152x152.png": (152, 152),
    "favicons/apple-touch-icon-167x167.png": (167, 167),
    "favicons/apple-touch-icon-180x180.png": (180, 180),

    "favicons/android-chrome-96x96.png": (96, 96),
    "favicons/android-chrome-144x144.png": (144, 144),
    "favicons/android-chrome-192x192.png": (192, 192),
    "favicons/android-chrome-512x512.png": (512, 512),
    "favicons/android-chrome-maskable-192x192.png": (192, 192),
    "favicons/android-chrome-maskable-512x512.png": (512, 512),

    "favicons/mstile-70x70.png": (70, 70),
    "favicons/mstile-150x150.png": (150, 150),
    "favicons/mstile-310x150.png": (310, 150),
    "favicons/mstile-310x310.png": (310, 310),

    "banners/joomleague-banner-1920x600.png": (1920, 600),
    "banners/joomleague-github-1280x640.png": (1280, 640),
    "social/joomleague-social-1200x630.png": (1200, 630),
    "icons/joomleague-avatar-1024x1024.png": (1024, 1024),
    "icons/joomleague-icon-simple-512x512.png": (512, 512),

    "developer/linux/joomleague-icon-64x64.png": (64, 64),
    "developer/linux/joomleague-icon-128x128.png": (128, 128),
    "developer/linux/joomleague-icon-256x256.png": (256, 256),
    "developer/linux/joomleague-icon-512x512.png": (512, 512),
    "developer/windows/joomleague-app-icon-256x256.png": (256, 256),
    "developer/macos/joomleague-app-icon-1024x1024.png": (1024, 1024),
}

REQUIRED_FILES = [
    "favicons/favicon.ico",
    "favicons/favicon.svg",
    "favicons/site.webmanifest",
    "favicons/browserconfig.xml",
    "favicons/safari-pinned-tab.svg",
    "developer/ai/assets.json",
    "developer/ai/ASSET_USAGE.md",
    "developer/ai/asset-inventory.json",
    "developer/svg/joomleague-symbol-flat.svg",
    "developer/svg/joomleague-symbol-outline.svg",
    "developer/svg/joomleague-symbol-monochrome.svg",
    "developer/svg/joomleague-symbol-currentcolor.svg",
    "developer/svg/joomleague-symbol-white.svg",
    "developer/svg/joomleague-symbol-blue.svg",
    "developer/windows/joomleague-app-icon.ico",
    "developer/macos/JoomLeague.icns",
]

SVG_FILES = [
    "favicons/favicon.svg",
    "favicons/safari-pinned-tab.svg",
    "developer/linux/icon.svg",
    "developer/svg/joomleague-symbol-flat.svg",
    "developer/svg/joomleague-symbol-outline.svg",
    "developer/svg/joomleague-symbol-monochrome.svg",
    "developer/svg/joomleague-symbol-currentcolor.svg",
    "developer/svg/joomleague-symbol-white.svg",
    "developer/svg/joomleague-symbol-blue.svg",
]

ASSET_EXTENSIONS = (
    ".png", ".svg", ".ico", ".icns", ".json", ".md", ".txt",
    ".xml", ".webmanifest", ".sh", ".py", ".yml", ".yaml", ".css", ".scss", ".docx", ".pdf"
)

class Reporter:
    def __init__(self) -> None:
        self.passed: list[str] = []
        self.warnings: list[str] = []
        self.errors: list[str] = []

    def ok(self, msg: str) -> None:
        self.passed.append(msg)
        print(f"[ OK ] {msg}")

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)
        print(f"[WARN] {msg}")

    def error(self, msg: str) -> None:
        self.errors.append(msg)
        print(f"[FAIL] {msg}")

def check_required(root: Path, r: Reporter) -> None:
    for rel in REQUIRED_FILES:
        if (root / rel).is_file():
            r.ok(f"Required file exists: {rel}")
        else:
            r.error(f"Missing required file: {rel}")

def check_raster_dimensions(root: Path, r: Reporter) -> None:
    for rel, expected in EXPECTED_RASTER_SIZES.items():
        p = root / rel
        if not p.is_file():
            r.error(f"Missing raster asset: {rel}")
            continue
        try:
            with Image.open(p) as im:
                actual = im.size
            if actual == expected:
                r.ok(f"Dimensions {rel}: {actual[0]}x{actual[1]}")
            else:
                r.error(
                    f"Wrong dimensions for {rel}: "
                    f"{actual[0]}x{actual[1]}, expected {expected[0]}x{expected[1]}"
                )
        except Exception as exc:
            r.error(f"Cannot read image {rel}: {exc}")

def check_svg_file(path: Path, rel: str, r: Reporter) -> None:
    if not path.is_file():
        r.error(f"Missing SVG: {rel}")
        return
    try:
        tree = ET.parse(path)
        el = tree.getroot()
        if el.tag.rsplit("}", 1)[-1].lower() != "svg":
            r.error(f"Not an SVG root element: {rel}")
            return
        if not el.attrib.get("viewBox"):
            r.warn(f"SVG has no viewBox: {rel}")
        else:
            r.ok(f"Valid SVG XML: {rel}")
    except ET.ParseError as exc:
        r.error(f"Invalid SVG XML {rel}: {exc}")

def check_svgs(root: Path, r: Reporter) -> None:
    for rel in SVG_FILES:
        check_svg_file(root / rel, rel, r)

def load_json(path: Path, rel: str, r: Reporter) -> Any | None:
    if not path.is_file():
        r.error(f"Missing JSON file: {rel}")
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        r.ok(f"Valid JSON: {rel}")
        return data
    except Exception as exc:
        r.error(f"Invalid JSON {rel}: {exc}")
        return None

def check_manifest(root: Path, r: Reporter) -> None:
    rel = "favicons/site.webmanifest"
    data = load_json(root / rel, rel, r)
    if not isinstance(data, dict):
        return

    for key in ["name", "short_name", "icons", "theme_color", "background_color", "display"]:
        if key not in data:
            r.error(f"{rel} missing key: {key}")

    icons = data.get("icons")
    if not isinstance(icons, list) or not icons:
        r.error(f"{rel}: icons must be a non-empty list")
        return

    has_maskable = False
    for i, item in enumerate(icons):
        if not isinstance(item, dict):
            r.error(f"{rel}: icons[{i}] is not an object")
            continue

        src = item.get("src")
        sizes = item.get("sizes")
        purpose = str(item.get("purpose", "any"))

        if "maskable" in purpose:
            has_maskable = True

        if not src or not sizes:
            r.error(f"{rel}: icons[{i}] must include src and sizes")
            continue

        target = root / "favicons" / str(src).lstrip("./")
        if not target.is_file():
            r.error(f"Manifest icon target missing: {src}")
            continue
        r.ok(f"Manifest icon exists: {src}")

        if isinstance(sizes, str) and "x" in sizes and " " not in sizes and target.suffix.lower() == ".png":
            try:
                w, h = map(int, sizes.lower().split("x", 1))
                with Image.open(target) as im:
                    actual = im.size
                if actual == (w, h):
                    r.ok(f"Manifest size matches: {src} -> {sizes}")
                else:
                    r.error(f"Manifest size mismatch for {src}: declared {sizes}, actual {actual[0]}x{actual[1]}")
            except Exception as exc:
                r.error(f"Could not validate manifest size for {src}: {exc}")

    if has_maskable:
        r.ok(f"{rel}: maskable icon present")
    else:
        r.warn(f"{rel}: no maskable icon purpose found")

def check_browserconfig(root: Path, r: Reporter) -> None:
    rel = "favicons/browserconfig.xml"
    path = root / rel
    if not path.is_file():
        r.error(f"Missing XML file: {rel}")
        return

    try:
        tree = ET.parse(path)
        r.ok(f"Valid XML: {rel}")
    except ET.ParseError as exc:
        r.error(f"Invalid XML {rel}: {exc}")
        return

    checks = {
        "square70x70logo": (70, 70),
        "square150x150logo": (150, 150),
        "wide310x150logo": (310, 150),
        "square310x310logo": (310, 310),
    }
    root_el = tree.getroot()

    for tag, expected in checks.items():
        found = root_el.find(f".//{tag}")
        if found is None:
            r.warn(f"{rel}: missing <{tag}> entry")
            continue

        src = found.attrib.get("src")
        if not src:
            r.error(f"{rel}: <{tag}> missing src")
            continue

        target = root / "favicons" / src.lstrip("./")
        if not target.is_file():
            r.error(f"{rel}: referenced file missing: {src}")
            continue

        with Image.open(target) as im:
            actual = im.size
        if actual == expected:
            r.ok(f"Windows tile reference valid: {src}")
        else:
            r.error(f"Windows tile {src} has {actual}, expected {expected}")

def iter_strings(obj: Any):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from iter_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from iter_strings(v)
    elif isinstance(obj, str):
        yield obj

def looks_like_file_reference(value: str) -> bool:
    prefixes = (
        "favicons/", "developer/", "social/", "banners/",
        "logos/", "icons/", "preview/", "integration-examples/",
        "brand-manual/", ".github/"
    )
    # Do not treat descriptive strings such as
    # "favicons/favicon.svg with favicon.ico fallback" as a path.
    return (
        value.startswith(prefixes)
        and " " not in value
        and value.lower().endswith(ASSET_EXTENSIONS)
    )

def check_assets_json(root: Path, r: Reporter) -> None:
    rel = "developer/ai/assets.json"
    data = load_json(root / rel, rel, r)
    if not isinstance(data, dict):
        return

    refs = sorted({s for s in iter_strings(data) if looks_like_file_reference(s)})
    if not refs:
        r.error(f"{rel}: no asset references found")
        return

    for ref in refs:
        if (root / ref).is_file():
            r.ok(f"assets.json reference exists: {ref}")
        else:
            r.error(f"assets.json broken reference: {ref}")

    brand = data.get("brand", {})
    if isinstance(brand, dict) and brand.get("sport_neutral") is True:
        r.ok(f"{rel}: sport_neutral=true")
    else:
        r.warn(f"{rel}: brand.sport_neutral is not true")

def check_optional_integrations(root: Path, r: Reporter) -> None:
    ex = root / "integration-examples"
    if not ex.is_dir():
        r.warn("integration-examples/ not present; skipping integration checks")
        return

    required = [
        "README.md",
        "CODEX_INTEGRATION.md",
        "joomla/README.md",
        "html/index.html",
        "pwa/site.webmanifest.example",
        "windows/browserconfig.xml.example",
        "linux/JoomLeague.desktop",
        "github/README.example.md",
    ]
    for rel in required:
        if (ex / rel).is_file():
            r.ok(f"Integration example exists: integration-examples/{rel}")
        else:
            r.warn(f"Missing integration example: integration-examples/{rel}")

def payload(root: Path, r: Reporter) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "tool": "JoomLeague Brand Kit Validator",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "status": "passed" if not r.errors else "failed",
        "summary": {
            "passed": len(r.passed),
            "warnings": len(r.warnings),
            "errors": len(r.errors),
        },
        "passed_checks": r.passed,
        "warnings": r.warnings,
        "errors": r.errors,
    }

def write_json_report(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def write_markdown_report(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    s = data["summary"]

    lines = [
        "# JoomLeague Brand Kit Validation Report",
        "",
        f"**Status:** {data['status'].upper()}",
        "",
        f"- Passed checks: **{s['passed']}**",
        f"- Warnings: **{s['warnings']}**",
        f"- Errors: **{s['errors']}**",
        f"- Generated: `{data['generated_at']}`",
        "",
    ]

    if data["errors"]:
        lines += ["## Errors", ""]
        lines += [f"- {x}" for x in data["errors"]]
        lines += [""]

    if data["warnings"]:
        lines += ["## Warnings", ""]
        lines += [f"- {x}" for x in data["warnings"]]
        lines += [""]

    lines += ["## Passed checks", ""]
    lines += [f"- {x}" for x in data["passed_checks"]]
    lines += [""]

    path.write_text("\n".join(lines), encoding="utf-8")

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate JoomLeague Brand Kit assets.")
    p.add_argument("root", nargs="?", help="Brand-kit root")
    p.add_argument(
        "--report",
        choices=["none", "json", "markdown", "both"],
        default="none",
        help="Create report files",
    )
    p.add_argument(
        "--output-dir",
        default="validation-reports",
        help="Report output directory; relative paths are resolved from the kit root",
    )
    return p.parse_args()

def main() -> int:
    args = parse_args()

    root = (
        Path(args.root).expanduser().resolve()
        if args.root
        else Path(__file__).resolve().parents[2]
    )

    if not root.is_dir():
        print(f"ERROR: Brand kit root does not exist: {root}", file=sys.stderr)
        return 2

    print("JoomLeague Brand Kit validator")
    print(f"Root: {root}")
    print("=" * 72)

    r = Reporter()
    check_required(root, r)
    check_raster_dimensions(root, r)
    check_svgs(root, r)
    check_manifest(root, r)
    check_browserconfig(root, r)
    check_assets_json(root, r)
    check_optional_integrations(root, r)

    report = payload(root, r)

    print("=" * 72)
    print(f"Passed checks : {len(r.passed)}")
    print(f"Warnings      : {len(r.warnings)}")
    print(f"Errors        : {len(r.errors)}")

    if args.report != "none":
        report_dir = Path(args.output_dir)
        if not report_dir.is_absolute():
            report_dir = root / report_dir

        if args.report in ("json", "both"):
            jp = report_dir / "validation-report.json"
            write_json_report(jp, report)
            print(f"JSON report   : {jp}")

        if args.report in ("markdown", "both"):
            mp = report_dir / "validation-report.md"
            write_markdown_report(mp, report)
            print(f"Markdown report: {mp}")

    if r.errors:
        print("\nValidation FAILED.")
        return 1

    print("\nValidation PASSED.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(2)
    except Exception as exc:
        print(f"Validator runtime error: {exc}", file=sys.stderr)
        sys.exit(2)
