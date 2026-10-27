---
tags: [systems, scenes]
---
# Scenes system

A **scene** is a saved set of parameters (lab, dimension, mode, sliders, camera) with a name, category and a one-line note.

- **504 scenes** in total; full generated list in [[Scene catalog]].
- Scenes are in `SC` (`k` key, `th` lab, `n` name, `cat`, `note`). Applying one switches to its lab context (`st`, keyed by lab+dim) and sets its parameters; `st.scene` remembers it. Undo covers it ([[Undo and redo]]).
- Scene search box (`.scfind`) searches names across all labs. Per lab: Calc 102, Universe 69, Lattice 64, Twistor 50, Law 48, Courant 43, Fluid 28, Sedenion 26, Qubits 21, Octonion 20, su3 17, Clifford 16.
- Calc scenes are `CXS` (102), see [[Lab Calc]].
- Favourites and recents are stored (`bitwistor-fav`, `bitwistor-recent`, see [[Storage keys]]).
- A scene can be turned into a share code ([[Share codes]]).
