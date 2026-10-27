---
tags: [systems, sandbox]
---
# Sandbox objects and probes

Entity types `ETYPES` (8): point · tracer · ray · fline (Field line) · link · sphere · twistor (Twistor ring) · spinor (Spinor flag).

- Added from the sandbox panel (`.addrow` chips), listed as rows (`.erow`) with a colour swatch, name, type and delete button; the selected entity is edited in the inspector (`#insLive`).
- Entities live in `st.ents` and are saved with the state, [[Share codes]] and [[History timeline]] snapshots (positions).
- Probes (`.prb`) read field values at a point; placing a probe is disabled in [[Lab Calc]].
- Available in the 4D field labs ([[Shared 4D field engine]]); hidden in engine labs.
