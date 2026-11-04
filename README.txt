JoomLeague Brand Kit — Final

Brand rules used
================
- Sport-neutral visual identity only.
- No football, balls, players, jerseys, stadiums, or any other sport-specific imagery.
- Joomla-inspired palette:
  Blue   #0062A9
  Green  #46B450
  Orange #F39C12
  Red    #E74C3C
- Final wordmark color split:
  Joom = blue
  Le   = green
  ag   = orange
  ue   = red

Contents
========
banners/
  joomleague-banner-1920x600.png
  joomleague-github-1280x640.png

social/
  joomleague-social-1200x630.png

icons/
  joomleague-avatar-1024x1024.png
  joomleague-icon-simple-512x512.png

favicons/
  favicon-180x180.png
  favicon-48x48.png
  favicon-32x32.png
  favicon-16x16.png

logos/
  joomleague-logo-standard-transparent.png
  joomleague-logo-compact-horizontal.png
  joomleague-logo-monochrome-white.png
  joomleague-logo-monochrome-black.png
  joomleague-logo-on-light.png
  joomleague-logo-on-dark.png

preview/
  joomleague-brand-preview-final.png


Update in v3
============
- Icons and favicons were rebuilt from a clean standalone emblem source
  (shield + trophy + multicolor ring only).
- No part of the 'JoomLeague' wordmark is present in icon or favicon assets.


Additional file
===============
- favicons/favicon.ico
  Classic multi-size ICO file for browsers and Windows.


Update in v5
============
Added complete mobile/PWA icon support:
- apple-touch-icon.png (180x180)
- android-chrome-192x192.png
- android-chrome-512x512.png
- android-chrome-maskable-192x192.png
- android-chrome-maskable-512x512.png
- mstile-150x150.png
- site.webmanifest
- browserconfig.xml
- html-head-snippet.txt

All mobile/PWA icons use the clean standalone JoomLeague emblem only.


Update in v6
============
Added Apple and Android background variants:

Apple:
- white
- blue
- transparent

Android:
- white
- blue
- transparent

Also added manifest variants:
- site-white.webmanifest
- site-blue.webmanifest
- site-transparent.webmanifest

Recommended:
- Apple: blue or white
- Android standard: transparent or blue
- Android maskable: blue or white


Update in v7
============
Complete Device Support added:

Apple:
- apple-touch-icon-120x120.png
- apple-touch-icon-152x152.png
- apple-touch-icon-167x167.png
- apple-touch-icon-180x180.png
- apple-touch-icon.png

Android / PWA:
- android-chrome-96x96.png
- android-chrome-144x144.png
- android-chrome-192x192.png
- android-chrome-512x512.png
- android-chrome-maskable-192x192.png
- android-chrome-maskable-512x512.png
- site.webmanifest

Windows:
- mstile-70x70.png
- mstile-150x150.png
- mstile-310x150.png
- mstile-310x310.png
- browserconfig.xml

SVG:
- favicon.svg
- safari-pinned-tab.svg

Documentation:
- html-head-snippet.txt
- usage-overview.txt


Update in v8 — Developer & AI Asset Pack
=========================================
Added:
- Linux desktop icons: 64, 128, 256, 512 px + icon.svg
- Windows multi-size app ICO + 256px PNG
- macOS 1024px app icon + ICNS
- True-vector simplified UI SVG variants:
  - flat
  - outline
  - monochrome
  - currentColor
  - white
  - blue
- developer/ai/assets.json
- developer/ai/ASSET_USAGE.md
- developer/ai/asset-inventory.json
- Linux .desktop example

The simplified SVG symbols are intentionally optimized for small UI use.
The full glossy emblem remains the preferred asset for larger presentation sizes.


Integration examples added
==========================
See:
  integration-examples/

Included examples:
- Joomla
- HTML
- PWA
- Windows
- Linux
- GitHub
- Codex-specific integration rules


Validator added
===============
Run:

  ./developer/tools/validate-brand-kit.sh

Checks required files, icon dimensions, SVG validity, site.webmanifest,
browserconfig.xml and all asset paths referenced by developer/ai/assets.json.


FINAL v8 Complete additions
===========================
Design tokens:
  developer/tokens/joomleague-tokens.css
  developer/tokens/_joomleague-tokens.scss
  developer/tokens/joomleague-tokens.json

Brand manual:
  brand-manual/JoomLeague-Brand-Manual-FINAL-v8.docx
  brand-manual/JoomLeague-Brand-Manual-FINAL-v8.pdf


FINAL v9 - Print & Source additions
====================================
Print:
  print/JoomLeague-Print-Reference.pdf
  print/JoomLeague-Print-Colors.csv
  print/JoomLeague-Print-Colors.json
  print/cmyk/*.tif
  print/monochrome/*.tif
  print/pantone-reference/PANTONE-REFERENCE.md

Source files:
  sources/master/
  sources/figma/
  sources/adobe/

Native Figma .fig and Adobe Illustrator .ai files are proprietary.
The pack provides editable SVG/EPS/PDF interchange sources instead.
