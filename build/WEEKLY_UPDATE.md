# Weekly update procedure — Stars and Strikes Game Day Guide

This file is the standing instruction set for the automatic weekly refresh. Follow it top to bottom.

## 1. Window
- The guide covers **Monday through the following Monday** (8 days) so Monday Night Football appears at both ends.
- Set `WEEK` in `build/data.py`: `label` ("Week of Nov 9–16, 2026"), `sub` (e.g. "NFL Week 10 · College Football Nov 14 slate · NBA · NHL · College BB"), `updated` (today), `start`, `end` (YYYY-MM-DD).

## 2. Sources (live sports sites only — never Wikipedia for schedules)
- **NFL**: Yahoo Sports "how to watch every game this week", footballschedule.info, ESPN or NFL.com. Need kickoff ET, away @ home, network (note Prime Video / NFL Network / Peacock exclusives, international games).
- **College football**: fbschedules.com "College football schedule: TV selections for <date>" (complete list with TV). Confirm any game listed with two different times via the school's athletics site.
- **AP Top 25 football**: the current week's poll (Yahoo/CBS/AP). Put it in `AP` keyed by team key.
- **NBA**: NBA.com or ESPN schedule. Include every Hawks, Hornets and Grizzlies game plus all national TV games (ESPN/ABC/NBC/Peacock/Prime). Mark NBA Cup games in the note.
- **NHL**: NHL.com or ESPN. Include every Hurricanes, Predators and Lightning game plus national TV games (ESPN/ESPN2/ABC/TNT/truTV).
- **College basketball**: ESPN/team sites. Include every game for Georgia, Georgia Tech, Alabama, Auburn, Tennessee, Vanderbilt, Kentucky, South Carolina, Clemson, Duke, North Carolina, NC State, Wake Forest, Charlotte, Coastal Carolina, Georgia State, Georgia Southern, Kennesaw State, UAB, Middle Tennessee, Memphis, plus any ranked-vs-ranked or national-linear-TV game. Put the AP men's basketball poll in `APBB`.
- **Championships / postseason** (any big sport): MLB postseason (Oct), NBA Finals (June), Stanley Cup Final (June), NCAA Tournament (March–April), College Football Playoff (Dec–Jan), NFL playoffs (Jan–Feb), WNBA Finals (Oct), MLS Cup, major boxing/UFC title cards if nationally televised. Tag these `tier="champ"` — they are always main screens.

## 3. Editing `build/data.py`
- Every team referenced by a game must exist in `T` (key, full name, 2–5 letter abbreviation, primary color, secondary color, league). Add new teams with their real colors. Pro teams that share a city with a college team get a distinct key (e.g. `ATL` Falcons, `ATLH` Hawks, `ATLB` Braves).
- Game line: `g(date, "H:MM AM/PM" ET or "TBD", sport, AWAY, HOME, NET, tier, note, label, neutral=True/False)`.
  - `sport` ∈ NFL, CFB, NBA, NHL, NCAAB, MLB. `NET` must be a key in `NETS` (ABC/CBS/NBC/FOX/ESPN/ESPN2/ESPNU/FS1/CBSSN/SECN/ACCN/BTN/TBS/TNT/USA/NFLN/CW/ESPN+/PRIME/PEACOCK/FDSN-SE/FDSN-S…). Add a network to `NETS` if missing (DirecTV channel number, `inGuide: False` so it shows a verify mark).
  - `tier`: "champ" for playoff/title games, "marquee" for national primetime NFL windows (TNF/SNF/MNF), ranked rivalry games and the biggest national college game of the day, "" otherwise.
  - `label`: short tag shown on the card (MNF, SNF, TNF, GAME OF THE WEEK, NLDS G3, NBA CUP...).
  - NFL Sunday regional games: add `G[-1]["pop"]=1 or 2` for the games with the biggest national draw (rivalries, marquee QBs) so the 1:00/4:25 windows pick sensibly.
- Do not edit `MARKETS`, the location list, or local-team weights unless a store opens/closes or Justin asks. The page computes byes ("Off this week") automatically.

## 4. Build, verify, publish
1. `python3 build/build.py` → regenerates `index.html` (it prints "missing teams: set()" — fix any listed key before continuing).
2. Sanity-check with Playwright or by reading the generated page: every day has at least one sound game at an Atlanta store and a Carolina store; MNF is the only sound game on Monday; football days show no NBA/NHL/CBB sound games.
3. Commit with a message like `Weekly update — week of Nov 9–16, 2026` and push to `main`. The GitHub Actions workflow deploys to https://notjut.github.io/StarsandStrikesTVGuide/ within ~2 minutes.
4. Fetch the live URL and confirm the new week label appears. If the Actions run failed, inspect it (`gh api repos/notjut/StarsandStrikesTVGuide/actions/runs`) and fix.

## 5. Rules the page enforces (do not fight them in the data)
- One sound game at a time per store; higher priority owns the window; hand-offs allowed when the bigger game is in its last 45 minutes.
- Monday: MNF is the only sound game unless a local team is in a championship game.
- Football days (any NFL/CFB game that day): NBA, NHL, college basketball are side screens only, unless championship.
- Local team weights per store drive priority; Atlanta stores weight Georgia, Georgia Tech, Falcons, Hawks, Braves; the Carolinas weight Clemson, South Carolina, UNC, NC State, Duke, Panthers, Hornets, Hurricanes; Huntsville weights Alabama, Auburn; Smyrna weights Tennessee, Vanderbilt, Titans, Predators.
