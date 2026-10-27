---
tags: [systems, share]
---
# Share codes

- State → JSON → deflate-raw → base64, prefixed `B1.`.
- Pasting a code validates it (`deepMerge` + `validP`, see [[State and persistence]]) and restores the lab, dimension, parameters and sandbox.
- Uses the browser `CompressionStream`; if unavailable, sharing is hidden.
- Related: [[Scenes system]].
