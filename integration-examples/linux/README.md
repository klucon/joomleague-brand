# Example installation

Install the desktop file:
```bash
install -Dm644 JoomLeague.desktop ~/.local/share/applications/JoomLeague.desktop
```

Install PNG icons using the freedesktop.org hicolor layout:
```bash
install -Dm644 ../../developer/linux/joomleague-icon-64x64.png \
  ~/.local/share/icons/hicolor/64x64/apps/joomleague.png

install -Dm644 ../../developer/linux/joomleague-icon-128x128.png \
  ~/.local/share/icons/hicolor/128x128/apps/joomleague.png

install -Dm644 ../../developer/linux/joomleague-icon-256x256.png \
  ~/.local/share/icons/hicolor/256x256/apps/joomleague.png

install -Dm644 ../../developer/linux/joomleague-icon-512x512.png \
  ~/.local/share/icons/hicolor/512x512/apps/joomleague.png
```
