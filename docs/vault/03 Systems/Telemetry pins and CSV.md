---
tags: [systems, data]
---
# Telemetry, pins and CSV

- `telemetry` runs every 125 ms ([[Frame loop]]) and collects the lab's readouts (`D.al`, energies, norms…).
- **Pins** (`PINS`, key `bitwistor-pins`, minimised state `bitwistor-pinmin`): pin a readout to a floating strip; each pin plots a rolling chart.
- **Download CSV** exports the pinned series (time + values).
- Readout text uses `.dtx` ([[Light theme and data colour]]).
