---
tags: [systems, scenes]
---
# Scenes system

A **scene** is a saved set of parameters (lab, dimension, mode, sliders, camera) with a name, category and a one-line note.

- **504 scenes** in total; full generated list in [[Scene catalog]].
- Applying a scene sets the context (`st`, keyed by lab+dim) and then the parameters; it pushes an undo step ([[Undo and redo]]).
- Calc scenes are `CXS` (102), see [[Lab Calc]].
- Favourites and recents are stored (`bitwistor-fav`, `bitwistor-recent`, see [[Storage keys]]).
- A scene can be turned into a share code ([[Share codes]]).
