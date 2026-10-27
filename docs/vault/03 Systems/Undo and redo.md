---
tags: [systems, state]
---
# Undo and redo (`UNDO`)

- `UNDO = {st, rd, last, key, down}`: undo and redo stacks of JSON snapshots.
- `usnap()` snapshots `st` except fast-changing keys `UVOL` (`fv, v, mph, yaw, pitch, play, rev, sel`) and the camera distance; `uApply` restores one.
- So undo covers settings, scenes and sandbox edits, not the running simulation or the camera.
- Shortcuts in [[Keyboard shortcuts]]. See also [[History timeline]].
