import json, base64, os
HERE = os.path.dirname(os.path.abspath(__file__))

WEEK = {
    "label": "Week of Oct 5–12, 2026",
    "sub": "NFL Week 5 · College Football Week 7 · MLB Division Series & LCS",
    "updated": "Mon Oct 5, 2026",
    "start": "2026-10-05", "end": "2026-10-12",
}

# ---------------- Teams: abbr, primary, secondary (text color auto) ----------------
T = {}
def t(key, name, abbr, c1, c2, league):
    T[key] = {"name": name, "abbr": abbr, "c1": c1, "c2": c2, "lg": league}

# NFL
t("ATL","Atlanta Falcons","ATL","#A71930","#000000","NFL")
t("NO","New Orleans Saints","NO","#D3BC8D","#101820","NFL")
t("TB","Tampa Bay Buccaneers","TB","#D50A0A","#34302B","NFL")
t("DAL","Dallas Cowboys","DAL","#041E42","#869397","NFL")
t("PHI","Philadelphia Eagles","PHI","#004C54","#A5ACAF","NFL")
t("JAX","Jacksonville Jaguars","JAX","#006778","#D7A22A","NFL")
t("CIN","Cincinnati Bengals","CIN","#FB4F14","#000000","NFL")
t("MIA","Miami Dolphins","MIA","#008E97","#FC4C02","NFL")
t("CHI","Chicago Bears","CHI","#0B162A","#C83803","NFL")
t("GB","Green Bay Packers","GB","#203731","#FFB612","NFL")
t("CLE","Cleveland Browns","CLE","#311D00","#FF3C00","NFL")
t("NYJ","New York Jets","NYJ","#125740","#FFFFFF","NFL")
t("HOU","Houston Texans","HOU","#03202F","#A71930","NFL")
t("TEN","Tennessee Titans","TEN","#0C2340","#4B92DB","NFL")
t("IND","Indianapolis Colts","IND","#002C5F","#A2AAAD","NFL")
t("PIT","Pittsburgh Steelers","PIT","#101820","#FFB612","NFL")
t("LV","Las Vegas Raiders","LV","#000000","#A5ACAF","NFL")
t("NE","New England Patriots","NE","#002244","#C60C30","NFL")
t("MIN","Minnesota Vikings","MIN","#4F2683","#FFC62F","NFL")
t("NYG","New York Giants","NYG","#0B2265","#A71930","NFL")
t("WAS","Washington Commanders","WAS","#5A1414","#FFB612","NFL")
t("DEN","Denver Broncos","DEN","#FB4F14","#002244","NFL")
t("LAC","Los Angeles Chargers","LAC","#0080C6","#FFC20E","NFL")
t("DET","Detroit Lions","DET","#0076B6","#B0B7BC","NFL")
t("ARI","Arizona Cardinals","ARI","#97233F","#FFB612","NFL")
t("SF","San Francisco 49ers","SF","#AA0000","#B3995D","NFL")
t("SEA","Seattle Seahawks","SEA","#002244","#69BE28","NFL")
t("BAL","Baltimore Ravens","BAL","#241773","#9E7C0C","NFL")
t("BUF","Buffalo Bills","BUF","#00338D","#C60C30","NFL")
t("LAR","Los Angeles Rams","LAR","#003594","#FFA300","NFL")
t("CAR","Carolina Panthers","CAR","#0085CA","#101820","NFL")
t("KC","Kansas City Chiefs","KC","#E31837","#FFB81C","NFL")
# MLB
t("CWS","Chicago White Sox","CWS","#27251F","#C4CED4","MLB"); T["CWS"]["short"]="White Sox"
t("CLEG","Cleveland Guardians","CLE","#00385D","#E31937","MLB")
t("NYY","New York Yankees","NYY","#0C2340","#C4CED3","MLB")
t("TBR","Tampa Bay Rays","TB","#092C5C","#8FBCE6","MLB"); T["NYJ"]["short"]="Jets"; T["NYG"]["short"]="Giants"
t("LAD","Los Angeles Dodgers","LAD","#005A9C","#EF3E42","MLB")
t("ATLB","Atlanta Braves","ATL","#CE1141","#13274F","MLB")
t("MIL","Milwaukee Brewers","MIL","#12284B","#FFC52F","MLB")
t("SD","San Diego Padres","SD","#2F241D","#FFC425","MLB")
t("TBD","To be determined","TBD","#6B7280","#9CA3AF","MLB")
# CFB
t("UGA","Georgia Bulldogs","UGA","#BA0C2F","#000000","CFB")
t("ALA","Alabama Crimson Tide","ALA","#9E1B32","#FFFFFF","CFB")
t("GT","Georgia Tech Yellow Jackets","GT","#B3A369","#003057","CFB"); T["GT"]["short"]="Georgia Tech"
t("DUKE","Duke Blue Devils","DUKE","#003087","#FFFFFF","CFB")
t("UNC","North Carolina Tar Heels","UNC","#7BAFD4","#13294B","CFB")
t("PITT","Pittsburgh Panthers","PITT","#003594","#FFB81C","CFB")
t("WAKE","Wake Forest Demon Deacons","WF","#9E7E38","#000000","CFB")
t("NCST","NC State Wolfpack","NCSU","#CC0000","#FFFFFF","CFB")
t("SCAR","South Carolina Gamecocks","SC","#73000A","#000000","CFB")
t("FLA","Florida Gators","UF","#0021A5","#FA4616","CFB")
t("TENN","Tennessee Volunteers","TENN","#FF8200","#FFFFFF","CFB")
t("ARK","Arkansas Razorbacks","ARK","#9D2235","#FFFFFF","CFB")
t("LSU","LSU Tigers","LSU","#461D7C","#FDD023","CFB")
t("UK","Kentucky Wildcats","UK","#0033A0","#FFFFFF","CFB")
t("MISS","Ole Miss Rebels","MISS","#CE1126","#14213D","CFB")
t("VAN","Vanderbilt Commodores","VAN","#866D4B","#000000","CFB")
t("TAMU","Texas A&M Aggies","A&M","#500000","#FFFFFF","CFB")
t("MIZ","Missouri Tigers","MIZ","#F1B82D","#000000","CFB")
t("TEX","Texas Longhorns","TEX","#BF5700","#FFFFFF","CFB")
t("OU","Oklahoma Sooners","OU","#841617","#FDF9D8","CFB")
t("OSU","Ohio State Buckeyes","OSU","#BB0000","#666666","CFB")
t("MD","Maryland Terrapins","MD","#E03A3E","#FFD520","CFB")
t("IU","Indiana Hoosiers","IU","#990000","#EEEDEB","CFB")
t("NEB","Nebraska Cornhuskers","NEB","#E41C38","#FDF2D9","CFB")
t("USC","USC Trojans","USC","#990000","#FFC72C","CFB")
t("PSU","Penn State Nittany Lions","PSU","#041E42","#FFFFFF","CFB")
t("UCLA","UCLA Bruins","UCLA","#2D68C4","#F2A900","CFB")
t("ORE","Oregon Ducks","ORE","#154733","#FEE123","CFB")
t("ND","Notre Dame Fighting Irish","ND","#0C2340","#C99700","CFB")
t("STAN","Stanford Cardinal","STAN","#8C1515","#FFFFFF","CFB")
t("VT","Virginia Tech Hokies","VT","#630031","#CF4420","CFB")
t("CAL","California Golden Bears","CAL","#003262","#FDB515","CFB")
t("SYR","Syracuse Orange","SYR","#F76900","#000E54","CFB")
t("UVA","Virginia Cavaliers","UVA","#232D4B","#F84C1E","CFB")
t("FSU","Florida State Seminoles","FSU","#782F40","#CEB888","CFB")
t("LOU","Louisville Cardinals","LOU","#AD0000","#000000","CFB")
t("HOUC","Houston Cougars","HOU","#C8102E","#FFFFFF","CFB")
t("KSU","Kansas State Wildcats","KSU","#512888","#D1D1D1","CFB")
t("UCF","UCF Knights","UCF","#000000","#BA9B37","CFB")
t("OKST","Oklahoma State Cowboys","OKST","#FF7300","#000000","CFB")
t("ARIZ","Arizona Wildcats","ARIZ","#CC0033","#003366","CFB")
t("WVU","West Virginia Mountaineers","WVU","#002855","#EAAA00","CFB")
t("KU","Kansas Jayhawks","KU","#0051BA","#E8000D","CFB")
t("UTAH","Utah Utes","UTAH","#CC0000","#FFFFFF","CFB")
t("ILL","Illinois Fighting Illini","ILL","#13294B","#E84A27","CFB")
t("MSU","Michigan State Spartans","MSU","#18453B","#FFFFFF","CFB")
t("MINN","Minnesota Golden Gophers","MINN","#7A0019","#FFCC33","CFB")
t("PUR","Purdue Boilermakers","PUR","#CEB888","#000000","CFB")
t("IOWA","Iowa Hawkeyes","IOWA","#000000","#FFCD00","CFB")
t("WASH","Washington Huskies","WASH","#4B2E83","#B7A57A","CFB")
t("ISU","Iowa State Cyclones","ISU","#C8102E","#F1BE48","CFB")
t("BYU","BYU Cougars","BYU","#002E5D","#FFFFFF","CFB")
t("BSU","Boise State Broncos","BSU","#0033A0","#D64309","CFB")
t("FRES","Fresno State Bulldogs","FRES","#DB0032","#002E6D","CFB")
t("CCU","Coastal Carolina Chanticleers","CCU","#006F71","#A27752","CFB")
t("MRSH","Marshall Thundering Herd","MRSH","#00B140","#000000","CFB")
t("CLT","Charlotte 49ers","CLT","#046A38","#B9975B","CFB")
t("UNT","North Texas Mean Green","UNT","#00853E","#000000","CFB")
t("UAB","UAB Blazers","UAB","#1E6B52","#F4C300","CFB")
t("MEM","Memphis Tigers","MEM","#003087","#898D8D","CFB")
t("GASO","Georgia Southern Eagles","GASO","#041E42","#A28D5B","CFB")
t("JMU","James Madison Dukes","JMU","#450084","#CBB677","CFB")
t("ODU","Old Dominion Monarchs","ODU","#003057","#7C878E","CFB")
t("APP","Appalachian State Mountaineers","APP","#222222","#FFCC00","CFB")
t("RICE","Rice Owls","RICE","#00205B","#C1C6C8","CFB")
t("ECU","East Carolina Pirates","ECU","#592A8A","#FDC82F","CFB")
t("KENN","Kennesaw State Owls","KSU","#231F20","#FDBB30","CFB")
t("JVST","Jacksonville State Gamecocks","JSU","#CC0000","#000000","CFB")
t("USM","Southern Miss Golden Eagles","USM","#FFAB00","#000000","CFB")
t("TROY","Troy Trojans","TROY","#8A2432","#B4B5B7","CFB")
t("USF","South Florida Bulls","USF","#006747","#CFC493","CFB")
t("UTSA","UTSA Roadrunners","UTSA","#0C2340","#F15A22","CFB")
t("USA","South Alabama Jaguars","USA","#00205B","#BF0D3E","CFB")
t("ARST","Arkansas State Red Wolves","ARST","#CC092F","#000000","CFB")
t("TUL","Tulane Green Wave","TUL","#006747","#418FDE","CFB")
t("ARMY","Army Black Knights","ARMY","#000000","#D4BF91","CFB")
t("TLSA","Tulsa Golden Hurricane","TLSA","#002D72","#C5B358","CFB")
t("NAVY","Navy Midshipmen","NAVY","#00205B","#C5B783","CFB")
t("WKU","Western Kentucky Hilltoppers","WKU","#C8102E","#000000","CFB")
t("MOST","Missouri State Bears","MOST","#5E0009","#000000","CFB")
t("SHSU","Sam Houston Bearkats","SHSU","#F56423","#002E5D","CFB")
t("LIB","Liberty Flames","LIB","#0A254E","#A61C2B","CFB")
t("NMSU","New Mexico State Aggies","NMSU","#8C0B42","#000000","CFB")
t("FIU","FIU Panthers","FIU","#081E3F","#B6862C","CFB")
t("SDSU","San Diego State Aztecs","SDSU","#A6192E","#000000","CFB")
t("ORST","Oregon State Beavers","ORST","#DC4405","#000000","CFB")
t("UNLV","UNLV Rebels","UNLV","#CF0A2C","#000000","CFB")
t("NDSU","North Dakota State Bison","NDSU","#0A5640","#FFC82E","CFB")
t("NEV","Nevada Wolf Pack","NEV","#003366","#807F84","CFB")
t("UTEP","UTEP Miners","UTEP","#FF8200","#041E42","CFB")
t("AF","Air Force Falcons","AF","#0033A0","#A7A8AA","CFB")
t("NIU","Northern Illinois Huskies","NIU","#C8102E","#000000","CFB")
t("HAW","Hawaii Rainbow Warriors","HAW","#024731","#C8C8C8","CFB")
t("ASU","Arizona State Sun Devils","ASU","#8C1D40","#FFC627","CFB")
t("ULL","Louisiana Ragin' Cajuns","ULL","#CE181E","#0A0203","CFB")
t("LT","Louisiana Tech Bulldogs","LT","#002F8B","#E31B23","CFB")
t("WYO","Wyoming Cowboys","WYO","#492F24","#FFC425","CFB")
t("SJSU","San Jose State Spartans","SJSU","#0055A2","#E5A823","CFB")
t("WSU","Washington State Cougars","WSU","#981E32","#5E6A71","CFB")
t("USU","Utah State Aggies","USU","#0F2439","#8A8D8F","CFB")
t("BALL","Ball State Cardinals","BALL","#BA0C2F","#000000","CFB")
t("NW","Northwestern Wildcats","NW","#4E2A84","#FFFFFF","CFB")
t("SAC","Sacramento State Hornets","SAC","#043927","#C4B581","CFB")
t("BGSU","Bowling Green Falcons","BGSU","#4F2C1D","#FF7300","CFB")
t("M-OH","Miami (OH) RedHawks","M-OH","#B61E2E","#000000","CFB")
t("UMASS","UMass Minutemen","UMASS","#881C1C","#000000","CFB")
t("EMU","Eastern Michigan Eagles","EMU","#006633","#FFFFFF","CFB")
t("AKR","Akron Zips","AKR","#041E42","#A89968","CFB")
t("CMU","Central Michigan Chippewas","CMU","#6A0032","#FFC82E","CFB")
t("OHIO","Ohio Bobcats","OHIO","#00694E","#CDA077","CFB")
t("BUFF","Buffalo Bulls","BUFF","#005BBB","#FFFFFF","CFB")
t("TOL","Toledo Rockets","TOL","#15397F","#FFD200","CFB")
t("KENT","Kent State Golden Flashes","KENT","#002664","#EAAB00","CFB")
t("WMU","Western Michigan Broncos","WMU","#6C4023","#B5A167","CFB")
t("CONN","UConn Huskies","CONN","#000E2F","#FFFFFF","CFB")
t("TEM","Temple Owls","TEM","#9D2235","#FFFFFF","CFB")

AP = {"TEX":1,"UGA":2,"ND":3,"MIAMI":4,"OSU":5,"ALA":6,"IU":7,"BYU":8,"MISS":9,"LSU":10,"TTU":11,"UTAH":12,"ORE":13,"MIZ":14,"TENN":15,"FLA":16,"MSST":17,"OKST":18,"USC":19,"IOWA":20,"UCLA":21,"HOUC":22,"BSU":23,"SMU":24,"PITT":25}

# ---------------- Games ----------------
# fields: date, time (ET, "H:MM AM/PM"), sport, away, home, net, tier ('champ'|'marquee'|''), note, label
G = []
def g(date, time, sport, away, home, net, tier="", note="", label="", neutral=False):
    G.append({"date": date, "time": time, "sport": sport, "away": away, "home": home, "net": net,
              "tier": tier, "note": note, "label": label, "neutral": neutral})

# Monday Oct 5
g("2026-10-05","5:00 PM","MLB","CWS","CLEG","TBS","champ","ALDS Game 2 · White Sox lead 1-0","ALDS G2")
g("2026-10-05","8:00 PM","MLB","NYY","TBR","TBS","champ","ALDS Game 2 · Rays lead 1-0","ALDS G2")
g("2026-10-05","8:15 PM","NFL","ATL","NO","ESPN","marquee","Monday Night Football · NFL Week 4","MNF")
# Tuesday Oct 6
g("2026-10-06","6:00 PM","MLB","LAD","ATLB","FS1","champ","NLDS Game 3 at Truist Park · Series tied 1-1","NLDS G3")
g("2026-10-06","8:00 PM","CFB","USM","TROY","ESPN2","","Sun Belt")
g("2026-10-06","9:30 PM","MLB","MIL","SD","FS1","champ","NLDS Game 3 · Brewers lead 2-0","NLDS G3")
# Wednesday Oct 7
g("2026-10-07","4:00 PM","MLB","CLEG","CWS","TBS","champ","ALDS Game 3","ALDS G3")
g("2026-10-07","6:00 PM","MLB","LAD","ATLB","FS1","champ","NLDS Game 4 at Truist Park","NLDS G4")
g("2026-10-07","7:00 PM","CFB","JVST","KENN","CBSSN","","Conference USA")
g("2026-10-07","7:30 PM","CFB","NMSU","FIU","ESPN2","","Conference USA")
g("2026-10-07","8:00 PM","MLB","TBR","NYY","TBS","champ","ALDS Game 3","ALDS G3")
g("2026-10-07","10:00 PM","MLB","MIL","SD","FS1","champ","NLDS Game 4 · if necessary","NLDS G4")
# Thursday Oct 8
g("2026-10-08","5:00 PM","MLB","CLEG","CWS","TBS","champ","ALDS Game 4 · if necessary","ALDS G4")
g("2026-10-08","7:00 PM","CFB","MOST","WKU","CBSSN","","Conference USA")
g("2026-10-08","7:00 PM","CFB","SHSU","LIB","ESPNU","","Conference USA")
g("2026-10-08","7:30 PM","CFB","USF","UTSA","ESPN","","American")
g("2026-10-08","7:30 PM","CFB","USA","ARST","ESPN2","","Sun Belt")
g("2026-10-08","8:00 PM","MLB","TBR","NYY","TBS","champ","ALDS Game 4 · if necessary","ALDS G4")
g("2026-10-08","8:15 PM","NFL","TB","DAL","PRIME","marquee","Thursday Night Football · NFL Week 5","TNF")
# Friday Oct 9
g("2026-10-09","4:30 PM","MLB","SD","MIL","FS1","champ","NLDS Game 5 · if necessary","NLDS G5")
g("2026-10-09","7:00 PM","CFB","FSU","LOU","ESPN","","ACC")
g("2026-10-09","8:00 PM","MLB","ATLB","LAD","FOX","champ","NLDS Game 5 · if necessary","NLDS G5")
g("2026-10-09","9:00 PM","CFB","WYO","SJSU","CBSSN","","Mountain West")
g("2026-10-09","9:00 PM","CFB","WSU","USU","CW","","Pac-12")
g("2026-10-09","9:00 PM","CFB","IOWA","WASH","FOX","","Big Ten")
g("2026-10-09","10:15 PM","CFB","ISU","BYU","ESPN","","Big 12")
# Saturday Oct 10
g("2026-10-10","12:00 PM","CFB","UNC","PITT","ESPN","","ACC")
g("2026-10-10","12:00 PM","CFB","WAKE","NCST","CW","","ACC")
g("2026-10-10","12:00 PM","CFB","TUL","ARMY","CBSSN","","American")
g("2026-10-10","12:00 PM","CFB","ARIZ","WVU","TNT","","Big 12")
g("2026-10-10","12:00 PM","CFB","UCF","OKST","ESPN2","","Big 12")
g("2026-10-10","12:00 PM","CFB","IU","NEB","FOX","","Big Ten")
g("2026-10-10","12:00 PM","CFB","TAMU","MIZ","ABC","","SEC")
g("2026-10-10","12:30 PM","CFB","BALL","NW","BTN","","Big Ten")
g("2026-10-10","12:45 PM","CFB","SCAR","FLA","SECN","","SEC")
g("2026-10-10","1:00 PM","CFB","ODU","APP","ESPN+","","Sun Belt")
g("2026-10-10","3:30 PM","CFB","DUKE","GT","ESPN2","","ACC")
g("2026-10-10","3:30 PM","CFB","STAN","ND","NBC","","ACC/Independent")
g("2026-10-10","3:30 PM","CFB","VT","CAL","ACCN","","ACC")
g("2026-10-10","3:30 PM","CFB","CLT","UNT","ESPN+","","American")
g("2026-10-10","3:30 PM","CFB","TLSA","NAVY","CBSSN","","American")
g("2026-10-10","3:30 PM","CFB","UCLA","ORE","CBS","","Big Ten")
g("2026-10-10","3:30 PM","CFB","ILL","MSU","FS1","","Big Ten")
g("2026-10-10","3:30 PM","CFB","HOUC","KSU","FOX","","Big 12")
g("2026-10-10","3:30 PM","CFB","MISS","VAN","ESPN","","SEC")
g("2026-10-10","3:30 PM","CFB","TEX","OU","ABC","marquee","Red River Rivalry · Cotton Bowl, Dallas","RED RIVER", neutral=True)
g("2026-10-10","3:45 PM","CFB","CONN","TEM","ESPNU","","American")
g("2026-10-10","4:00 PM","CFB","RICE","ECU","ESPN+","","American")
g("2026-10-10","4:15 PM","CFB","MD","OSU","BTN","","Big Ten")
g("2026-10-10","4:15 PM","CFB","TENN","ARK","SECN","","SEC")
g("2026-10-10","5:00 PM","MLB","CWS","CLEG","TBS","champ","ALDS Game 5 · if necessary","ALDS G5")
g("2026-10-10","6:00 PM","CFB","SDSU","ORST","USA","","Pac-12")
g("2026-10-10","7:00 PM","CFB","UAB","MEM","ESPN2","","American")
g("2026-10-10","7:00 PM","CFB","LSU","UK","ESPN","","SEC")
g("2026-10-10","7:00 PM","CFB","CCU","MRSH","ESPN+","","Sun Belt")
g("2026-10-10","7:00 PM","CFB","NEV","UTEP","FS1","","Mountain West")
g("2026-10-10","7:00 PM","CFB","NDSU","UNLV","CW","","Mountain West")
g("2026-10-10","7:30 PM","CFB","UGA","ALA","ABC","marquee","#2 vs #6 · Bryant-Denny Stadium","GAME OF THE WEEK")
g("2026-10-10","7:30 PM","CFB","USC","PSU","NBC","","Big Ten")
g("2026-10-10","7:30 PM","CFB","SYR","UVA","ACCN","","ACC")
g("2026-10-10","7:30 PM","CFB","JMU","GASO","ESPNU","","Sun Belt")
g("2026-10-10","7:30 PM","CFB","AF","NIU","CBSSN","","Mountain West")
g("2026-10-10","7:30 PM","CFB","ULL","LT","ESPN+","","Sun Belt")
g("2026-10-10","8:00 PM","MLB","NYY","TBR","TBS","champ","ALDS Game 5 · if necessary","ALDS G5")
g("2026-10-10","8:00 PM","CFB","MINN","PUR","BTN","","Big Ten")
g("2026-10-10","10:15 PM","CFB","KU","UTAH","ESPN","","Big 12")
g("2026-10-10","10:30 PM","CFB","BSU","FRES","CW","","Mountain West")
g("2026-10-10","10:30 PM","CFB","HAW","ASU","FS1","","Big 12")
# Sunday Oct 11
g("2026-10-11","9:30 AM","NFL","PHI","JAX","ESPN","","International game · London","LONDON")
g("2026-10-11","1:00 PM","NFL","CIN","MIA","FOX","","Regional")
g("2026-10-11","1:00 PM","NFL","CHI","GB","FOX","","NFC North rivalry"); G[-1]["pop"]=2
g("2026-10-11","1:00 PM","NFL","CLE","NYJ","CBS","","Regional")
g("2026-10-11","1:00 PM","NFL","HOU","TEN","CBS","","Regional")
g("2026-10-11","1:00 PM","NFL","IND","PIT","CBS","","Regional"); G[-1]["pop"]=1
g("2026-10-11","1:00 PM","NFL","LV","NE","CBS","","Regional")
g("2026-10-11","1:00 PM","NFL","MIN","NO","FOX","","Regional"); G[-1]["pop"]=1
g("2026-10-11","1:00 PM","NFL","NYG","WAS","FOX","","Regional")
g("2026-10-11","4:05 PM","NFL","DEN","LAC","CBS","","Regional")
g("2026-10-11","4:25 PM","NFL","DET","ARI","FOX","","Regional"); G[-1]["pop"]=1
g("2026-10-11","4:25 PM","NFL","SF","SEA","FOX","","NFC West rivalry"); G[-1]["pop"]=2
g("2026-10-11","8:20 PM","NFL","BAL","ATL","NBC","marquee","Sunday Night Football · Mercedes-Benz Stadium","SNF")
g("2026-10-11","TBD","MLB","TBD","TBD","FOX","champ","NLCS Game 1 · matchup set after NLDS · FOX or FS1","NLCS G1")
# Monday Oct 12
g("2026-10-12","TBD","MLB","TBD","TBD","TBS","champ","ALCS Game 1","ALCS G1")
g("2026-10-12","TBD","MLB","TBD","TBD","FOX","champ","NLCS Game 2 · FOX or FS1","NLCS G2")
g("2026-10-12","8:15 PM","NFL","BUF","LAR","ABC","marquee","Monday Night Football","MNF")

for i,x in enumerate(G): x["id"] = i

# ---------------- Markets / channel lineups (from Justin's guide) ----------------
# Values: broadcast affiliates per market; cable numbers are DirecTV.
MARKETS = {
 "GA":   {"name":"Georgia (Atlanta DMA)", "ABC":"WSB 2",  "CBS":"WANF 46","NBC":"WXIA 11","FOX":"WAGA 5"},
 "MYR":  {"name":"Myrtle Beach",          "ABC":"WPDE 15","CBS":"WBTW 13","NBC":"WMBF 32","FOX":"WFXB 43"},
 "IRMO": {"name":"Columbia (Irmo)",       "ABC":"WOLO 25","CBS":"WLTX 19","NBC":"WIS 10", "FOX":"WACH 57"},
 "CLT":  {"name":"Charlotte",             "ABC":"WSOC 9", "CBS":"WBTV 3", "NBC":"WCNC 36","FOX":"WJZY 46"},
 "CHS":  {"name":"Charleston (Summerville)","ABC":"WCIV 36","CBS":"WCSC 5","NBC":"WCBD 2","FOX":"WTAT 24"},
 "RAL":  {"name":"Raleigh",               "ABC":"WTVD 11","CBS":"WNCN 17","NBC":"WRAL 5", "FOX":"WRAZ 50"},
 "HSV":  {"name":"Huntsville",            "ABC":"WAAY 31","CBS":"WHNT 19","NBC":"WAFF 48","FOX":"WZDX 54"},
 "NSH":  {"name":"Nashville (Smyrna)",    "ABC":"WKRN 2", "CBS":"WTVF 5", "NBC":"WSMV 4", "FOX":"WZTV 17"},
}
# Cable / streaming — inGuide = listed in Justin's channel lookup
NETS = {
 "ABC":  {"label":"ABC","kind":"local"},
 "CBS":  {"label":"CBS","kind":"local"},
 "NBC":  {"label":"NBC","kind":"local"},
 "FOX":  {"label":"FOX","kind":"local"},
 "ESPN": {"label":"ESPN","ch":"206","inGuide":True},
 "ESPN2":{"label":"ESPN2","ch":"206","inGuide":True},
 "ESPNU":{"label":"ESPNU","ch":"206","inGuide":True},
 "FS1":  {"label":"FS1","ch":"219","inGuide":True},
 "CBSSN":{"label":"CBS Sports Net","ch":"221","inGuide":True},
 "SECN": {"label":"SEC Network","ch":"611","inGuide":True},
 "ACCN": {"label":"ACC Network","ch":"612","inGuide":True},
 "BTN":  {"label":"Big Ten Network","ch":"610","inGuide":True},
 "TBS":  {"label":"TBS","ch":"247","inGuide":False},
 "TNT":  {"label":"TNT / truTV","ch":"245","inGuide":False},
 "USA":  {"label":"USA Network","ch":"242","inGuide":False},
 "CW":   {"label":"The CW","ch":"varies","inGuide":False},
 "ESPN+":{"label":"ESPN+ (app)","ch":"stream","inGuide":False},
 "PRIME":{"label":"Prime Video","ch":"stream","inGuide":False},
}

# ---------------- 17 Locations ----------------
# local: team key -> weight (how much that team matters at this location)
L = []
def loc(id, name, state, market, tz, local, note=""):
    L.append({"id":id,"name":name,"state":state,"market":market,"tz":tz,"local":local,"note":note})

GA_CORE = {"UGA":10,"GT":8,"ATL":10,"ATLB":10,"GASO":3,"KENN":3}
loc("augusta","Augusta","GA","GA","ET", {**GA_CORE,"SCAR":6,"CLT":0}, "Augusta is its own TV market (WJBF 6 ABC · WRDW 12 CBS · WAGT 26 NBC · WFXG 54 FOX). Your guide lists Atlanta affiliates for all Georgia stores — verify locals on the box before game time.")
loc("buford","Buford","GA","GA","ET", GA_CORE)
loc("columbus","Columbus","GA","GA","ET", {**GA_CORE,"ALA":6}, "Columbus is its own TV market (WTVM 9 ABC · WRBL 3 CBS · WLTZ 38 NBC · WXTX 54 FOX). Your guide lists Atlanta affiliates — verify locals on the box. Auburn is on a bye this week.")
loc("cumming","Cumming","GA","GA","ET", GA_CORE)
loc("dacula","Dacula","GA","GA","ET", GA_CORE)
loc("dallas","Dallas","GA","GA","ET", GA_CORE)
loc("loganville","Loganville","GA","GA","ET", GA_CORE)
loc("stone-mountain","Stone Mountain","GA","GA","ET", GA_CORE)
loc("woodstock","Woodstock","GA","GA","ET", GA_CORE)
loc("myrtle-beach","Myrtle Beach","SC","MYR","ET", {"SCAR":9,"CCU":9,"CAR":8,"ATLB":6,"UNC":4,"NCST":4}, "Panthers are on a bye this week.")
loc("irmo","Irmo","SC","IRMO","ET", {"SCAR":10,"CAR":7,"ATLB":6,"UGA":3}, "Panthers are on a bye this week. Clemson is on a bye.")
loc("rock-hill","Rock Hill","SC","CLT","ET", {"SCAR":9,"CAR":9,"CLT":5,"UNC":5,"NCST":5,"ATLB":6}, "Panthers are on a bye this week. Clemson is on a bye.")
loc("summerville","Summerville","SC","CHS","ET", {"SCAR":9,"CAR":7,"ATLB":6,"CCU":3}, "Panthers are on a bye this week. Clemson is on a bye.")
loc("concord","Concord","NC","CLT","ET", {"CAR":10,"UNC":8,"NCST":8,"CLT":6,"DUKE":5,"WAKE":5,"APP":4,"ATLB":5}, "Panthers are on a bye this week.")
loc("raleigh","Raleigh","NC","RAL","ET", {"NCST":10,"UNC":9,"DUKE":8,"CAR":9,"WAKE":6,"ECU":5,"ATLB":5}, "Panthers are on a bye this week.")
loc("huntsville","Huntsville","AL","HSV","CT", {"ALA":10,"TEN":7,"ATL":6,"ATLB":7,"UAB":4,"JVST":4,"USA":2}, "Auburn is on a bye this week. Times shown in Central.")
loc("smyrna","Smyrna","TN","NSH","CT", {"TENN":10,"VAN":8,"TEN":10,"ATLB":6,"MEM":3}, "Times shown in Central.")

logo = base64.b64encode(open(os.path.join(HERE,"logo.webp"),"rb").read()).decode()

DATA = {"week":WEEK,"teams":T,"ap":AP,"games":G,"markets":MARKETS,"nets":NETS,"locations":L}
json.dump(DATA, open(os.path.join(HERE,"data.json"),"w"))
open(os.path.join(HERE,"logo.b64"),"w").write(logo)
# sanity: every team referenced exists
missing = {k for x in G for k in (x["away"],x["home"]) if k not in T}
print("missing teams:", missing, "| games:", len(G), "| locations:", len(L))
