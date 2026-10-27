---
tags: [systems, storage, reference]
---
# Storage keys (localStorage)

| key | holds |
|---|---|
| `bitwistor-lab-v5` (`SKEY`) | main saved state, written every 1.5 s when dirty |
| `bitwistor-app` | app settings (theme, sound, quality) |
| `bitwistor-tour` | tour done flag |
| `bitwistor-spcz` | sphere view zoom |
| `bitwistor-pinmin` | pins panel minimised |
| `bitwistor-cz`, `bitwistor-cz2` | camera zoom values |
| `bitwistor-cams` | camera bookmarks ([[Camera bookmarks]]) |
| `bitwistor-fav` | favourite scenes |
| `bitwistor-pins` | pinned readouts ([[Telemetry pins and CSV]]) |
| `bitwistor-recent` | recent scenes |
| `bitwistor-engine` (`ENGK`) | WebGL / WebGPU choice |

All reads and writes are wrapped in try/catch. Load path: [[State and persistence]].
