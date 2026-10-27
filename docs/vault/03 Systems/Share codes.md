---
tags: [systems, share]
---
# Share codes

- `shareCode()`: copy of `st` (minus selection) wrapped as `{v:5, th, dim, c}` → JSON → `b64deflate`.
- `b64deflate`: `CompressionStream('deflate-raw')` + base64 with tag `B1`; without CompressionStream it stores raw bytes with tag `B0`.
- `shareOpen(code)`: accepts a bare code or a URL with `#s=`; checks `v === 5` and the lab id, else toast "That is not a share code". Builds a default context (`defCtx`) and merges the code into it (`deepMerge`), so missing or bad fields fall back to defaults ([[State and persistence]]).
- UI: "Share this view" in the Memory tab ([[Settings and app popover]]).
