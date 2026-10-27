---
tags: [systems, state]
---
# History timeline (`HS`)

- Works for Lattice, Universe, Fluid, Law and the 4D field labs (`hsKind` = `la`, `un`, `fl`, `eq`, `fd`).
- `hsTick`: while playing, stores a snapshot every `HS.iv` ms (500 by default) with `hsPut`; `hsThin` thins old snapshots to fit a memory budget.
- `hsTake`: for `fd` stores field values, phases and entity positions; for engine labs copies the engine state (`LT`, `UN`, `FL`, `EQ`) minus excluded keys `HXL`.
- Scrubber bar `.hist` under the view: drag back in time, `#hsLive` returns to live. Moving the clock after scrubbing drops the future snapshots.
- RAM only. Different from [[Undo and redo]] (settings) and [[Camera bookmarks]] (view).
