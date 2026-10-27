---
tags: [systems, compare]
---
# Compare A-B (`CMP`)

- Panel `#cmpP` with buttons: capture A, capture B, **B live** (B keeps showing the running view), swap, close.
- `cmpSnap` stores an image of the view, the scene name, the time, the telemetry values (minus frame-rate rows) and the full state.
- `cmpDiff` lists settings that differ (labels from `CMPL`, ignoring view keys `CMPX`); the telemetry table marks values that went up or down.
- `cmpLoad` restores a captured state.
