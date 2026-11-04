# JoomLeague Asset Usage Guide

This pack is designed so humans and coding agents can choose a correct asset without guessing.

## Core rule

JoomLeague is **sport-neutral**.

Never use imagery tied to a single sport:
- footballs
- players
- stadiums
- jerseys
- racquets
- hockey sticks
- balls specific to one sport

Use abstract brand graphics, the trophy/shield emblem, or the official wordmark.

## Which asset should I use?

| Context | Recommended asset |
|---|---|
| Browser favicon | `favicons/favicon.svg` |
| Legacy favicon fallback | `favicons/favicon.ico` |
| Apple home screen | `favicons/apple-touch-icon.png` |
| Android launcher | `favicons/android-chrome-192x192.png` |
| Android high resolution | `favicons/android-chrome-512x512.png` |
| Android adaptive / maskable | `favicons/android-chrome-maskable-512x512.png` |
| Windows app icon | `developer/windows/joomleague-app-icon.ico` |
| Linux desktop icon | `developer/linux/joomleague-icon-256x256.png` |
| macOS app icon | `developer/macos/joomleague-app-icon-1024x1024.png` |
| Joomla menu icon | `developer/svg/joomleague-symbol-currentcolor.svg` |
| Joomla toolbar icon | `developer/svg/joomleague-symbol-outline.svg` |
| Tiny UI icon | `developer/svg/joomleague-symbol-flat.svg` |
| Dark background | `developer/svg/joomleague-symbol-white.svg` |
| Light background | `developer/svg/joomleague-symbol-blue.svg` |
| Social preview | `social/joomleague-social-1200x630.png` |
| GitHub banner | `banners/joomleague-github-1280x640.png` |
| Website banner | `banners/joomleague-banner-1920x600.png` |

## Size guidance

- 16–24 px: outline SVG
- 24–48 px: flat SVG
- 48 px and larger: full emblem PNG or color SVG
- logos with text: use only when the wordmark remains readable

## CSS-colored icon

Use:

`developer/svg/joomleague-symbol-currentcolor.svg`

The icon follows CSS `color`.

Example:

```css
.joomleague-icon {
  color: #0062A9;
  width: 1.5rem;
  height: 1.5rem;
}
```

## Brand colors

- Blue: `#0062A9`
- Green: `#46B450`
- Orange: `#F39C12`
- Red: `#E74C3C`

Wordmark:
- `Joom` → blue
- `Le` → green
- `ag` → orange
- `ue` → red

## AI / Codex

Read `developer/ai/assets.json` first.

Prefer its `recommended_assets` and `selection_rules` over filename guessing.
