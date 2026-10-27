---
tags: [systems, data]
---
# Telemetry, pins and CSV

- **Telemetry** (`TEL`): every lab reports rows (label, value, unit); tiles (`.tile`) show value plus a sparkline; `TEL.hist` keeps recent history. Updated every 125 ms ([[Frame loop]]).
- **Pins** (`PINS`, key `bitwistor-pins`): the pin button on a tile (`.tpin`) adds it to the floating dock (`.pdock`), which can be minimised (`bitwistor-pinmin`). On phones the dock is a 2-column grid at the bottom.
- **CSV** (`#telCsv`): exports the telemetry log `TLOG` (seconds + every column that has numbers) as `telemetry-<lab>-<time>.csv`. If nothing was recorded: toast "No telemetry recorded yet".
- Telemetry also feeds [[Sound]] and [[Compare A-B]].
