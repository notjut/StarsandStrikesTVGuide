# Stars and Strikes Game Day Guide

Weekly sports TV programming guide for all 17 Stars and Strikes locations.
Live site: https://notjut.github.io/StarsandStrikesTVGuide/

- `index.html` — the published page (generated, do not edit by hand)
- `build/data.py` — this week's games, teams, channel lineups, and the 17 locations
- `build/template.html` — page layout and the sound-game picking rules
- `build/build.py` — rebuilds `index.html` (`python3 build/build.py`)

Weekly update: edit the games in `build/data.py`, run the build, commit and push.
