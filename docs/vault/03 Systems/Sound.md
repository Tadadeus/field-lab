---
tags: [systems, sound]
---
# Sound (`SND`)

- `sndInit`: WebAudio graph, two oscillators (sine 220 Hz, triangle 330 Hz) through a 2600 Hz low-pass into a gain at 0. Starts only after a user gesture; off unless `APP.snd`.
- `sndUpd`: a continuous tone whose pitch (196 Hz up 2.5 octaves) follows a chosen telemetry row (`sndRow`), or the engine's `sndv()`, or a slow sine. Sounds only while playing and the tab is visible.
- `sndTick(freq, dur, amp)`: short blips. Universe events (decay 1320 Hz, annihilation 520, reaction 880, hadronisation 660), Calc Lab crossings, UI clicks; `sndChime` = two notes.
- Toggle in the app popover ([[Settings and app popover]]); button `#sndB`.
