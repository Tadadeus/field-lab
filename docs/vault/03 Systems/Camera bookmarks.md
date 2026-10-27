---
tags: [systems, camera]
---
# Camera bookmarks (`CAMS`)

- `camGet()` captures yaw, pitch, distance, FOV, pan, 3D rotation `M3`, orbit flag and the 4D view.
- Named bookmarks in the popover `.bmpop` (button `#apBm` on the view); saved in `bitwistor-cams`.
- `camFly(c)` flies to a bookmark over 700 ms with ease-in-out (`bmTick`) and stops auto-orbit.
- `bitwistor-cz`, `bitwistor-cz2` and `bitwistor-spcz` hold zoom levels of other views ([[Storage keys]]).
