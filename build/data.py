import json, base64, os
HERE = os.path.dirname(os.path.abspath(__file__))

WEEK = {
    "label": "Week of Nov 16–23, 2026",
    "sub": "NFL Week 11 · College Football Nov 21 · NBA Cup · NHL · College Basketball Feast Week tip-off",
    "updated": "Mon Nov 16, 2026",
    "start": "2026-11-16", "end": "2026-11-23",
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
# NBA
t("ATLH","Atlanta Hawks","ATL","#C8102E","#FDB927","NBA"); T["ATLH"]["short"]="Hawks"
t("CHA","Charlotte Hornets","CHA","#1D1160","#00788C","NBA"); T["CHA"]["short"]="Hornets"
t("MEMG","Memphis Grizzlies","MEM","#5D76A9","#12173F","NBA"); T["MEMG"]["short"]="Grizzlies"
t("BOS","Boston Celtics","BOS","#007A33","#BA9653","NBA")
t("NYK","New York Knicks","NYK","#006BB6","#F58426","NBA"); T["NYK"]["short"]="Knicks"
t("BKN","Brooklyn Nets","BKN","#000000","#FFFFFF","NBA")
t("PHI76","Philadelphia 76ers","PHI","#006BB6","#ED174C","NBA")
t("TOR","Toronto Raptors","TOR","#CE1141","#000000","NBA")
t("MIAH","Miami Heat","MIA","#98002E","#F9A01B","NBA")
t("ORL","Orlando Magic","ORL","#0077C0","#C4CED4","NBA")
t("WASW","Washington Wizards","WAS","#002B5C","#E31837","NBA")
t("CHIB","Chicago Bulls","CHI","#CE1141","#000000","NBA")
t("CLEC","Cleveland Cavaliers","CLE","#860038","#FDBB30","NBA")
t("DETP","Detroit Pistons","DET","#C8102E","#1D42BA","NBA")
t("INDP","Indiana Pacers","IND","#002D62","#FDBB30","NBA")
t("MILB","Milwaukee Bucks","MIL","#00471B","#EEE1C6","NBA")
t("DALM","Dallas Mavericks","DAL","#00538C","#002B5E","NBA")
t("HOUR","Houston Rockets","HOU","#CE1141","#000000","NBA")
t("NOP","New Orleans Pelicans","NOP","#0C2340","#C8102E","NBA")
t("SAS","San Antonio Spurs","SAS","#C4CED4","#000000","NBA")
t("DENN","Denver Nuggets","DEN","#0E2240","#FEC524","NBA")
t("MINT","Minnesota Timberwolves","MIN","#0C2340","#236192","NBA")
t("OKC","Oklahoma City Thunder","OKC","#007AC1","#EF6F1D","NBA")
t("POR","Portland Trail Blazers","POR","#E03A3E","#000000","NBA")
t("UTAJ","Utah Jazz","UTA","#002B5C","#F9A01B","NBA")
t("GSW","Golden State Warriors","GSW","#1D428A","#FFC72C","NBA")
t("LAC2","LA Clippers","LAC","#C8102E","#1D428A","NBA")
t("LAL","Los Angeles Lakers","LAL","#552583","#FDB927","NBA")
t("PHX","Phoenix Suns","PHX","#1D1160","#E56020","NBA")
t("SAC2","Sacramento Kings","SAC","#5A2D81","#63727A","NBA")
# NHL
t("CARH","Carolina Hurricanes","CAR","#CC0000","#000000","NHL"); T["CARH"]["short"]="Hurricanes"
t("NSH","Nashville Predators","NSH","#FFB81C","#041E42","NHL"); T["NSH"]["short"]="Predators"
t("TBL","Tampa Bay Lightning","TBL","#002868","#FFFFFF","NHL"); T["TBL"]["short"]="Lightning"
t("FLAP","Florida Panthers","FLA","#C8102E","#041E42","NHL")
t("BOSB","Boston Bruins","BOS","#FFB81C","#000000","NHL")
t("TORM","Toronto Maple Leafs","TOR","#00205B","#FFFFFF","NHL")
t("MTL","Montreal Canadiens","MTL","#AF1E2D","#192168","NHL")
t("OTT","Ottawa Senators","OTT","#000000","#C8102E","NHL")
t("BUFS","Buffalo Sabres","BUF","#002654","#FCB514","NHL")
t("DETR","Detroit Red Wings","DET","#CE1126","#FFFFFF","NHL")
t("NYR","New York Rangers","NYR","#0038A8","#CE1126","NHL")
t("NYI","New York Islanders","NYI","#00539B","#F47D30","NHL")
t("NJD","New Jersey Devils","NJD","#CE1126","#000000","NHL")
t("PHIF","Philadelphia Flyers","PHI","#F74902","#000000","NHL")
t("PITP","Pittsburgh Penguins","PIT","#000000","#FCB514","NHL")
t("WSH","Washington Capitals","WSH","#041E42","#C8102E","NHL")
t("CBJ","Columbus Blue Jackets","CBJ","#002654","#CE1126","NHL")
t("CHIH","Chicago Blackhawks","CHI","#CF0A2C","#000000","NHL")
t("STL","St. Louis Blues","STL","#002F87","#FCB514","NHL")
t("MINW","Minnesota Wild","MIN","#154734","#A6192E","NHL")
t("WPG","Winnipeg Jets","WPG","#041E42","#004C97","NHL")
t("COL","Colorado Avalanche","COL","#6F263D","#236192","NHL")
t("DALS","Dallas Stars","DAL","#006847","#8F8F8C","NHL")
t("UTAM","Utah Mammoth","UTA","#6CACE4","#010101","NHL")
t("VGK","Vegas Golden Knights","VGK","#B4975A","#333F42","NHL")
t("EDM","Edmonton Oilers","EDM","#041E42","#FF4C00","NHL")
t("CGY","Calgary Flames","CGY","#C8102E","#F1BE48","NHL")
t("VAN2","Vancouver Canucks","VAN","#00205B","#00843D","NHL")
t("SEAK","Seattle Kraken","SEA","#001628","#99D9D9","NHL")
t("SJS","San Jose Sharks","SJS","#006D75","#EA7200","NHL")
t("LAK","Los Angeles Kings","LAK","#111111","#A2AAAD","NHL")
t("ANA","Anaheim Ducks","ANA","#F47A38","#B9975B","NHL")
# College basketball opponents (Nov 2026)
t("PENN","Penn Quakers","PENN","#011F5B","#990000","CFB")
t("PRES","Presbyterian Blue Hose","PRES","#0A2240","#A6192E","CFB")
t("AMER","American Eagles","AU","#C41130","#00447C","CFB")
t("WOF","Wofford Terriers","WOF","#886E4C","#000000","CFB")
t("ETSU","East Tennessee State Buccaneers","ETSU","#041E42","#FFC72C","CFB")
t("APSU","Austin Peay Governors","APSU","#C8102E","#000000","CFB")
t("NICH","Nicholls Colonels","NICH","#C8102E","#8A8D8F","CFB")
t("VCU","VCU Rams","VCU","#000000","#F8B800","CFB")
t("RAD","Radford Highlanders","RAD","#CC0000","#002B5C","CFB")
t("FGCU","Florida Gulf Coast Eagles","FGCU","#00885A","#002D62","CFB")
t("UND","North Dakota Fighting Hawks","UND","#009A44","#000000","CFB")
t("USCU","USC Upstate Spartans","UPST","#006747","#000000","CFB")
t("OAK","Oakland Golden Grizzlies","OAK","#000000","#B59A57","CFB")
t("SHU","Seton Hall Pirates","SHU","#004488","#FFFFFF","CFB")
t("SEMO","Southeast Missouri State Redhawks","SEMO","#C8102E","#000000","CFB")
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

# added Nov 2026
t("SMU","SMU Mustangs","SMU","#0033A0","#C8102E","CFB")
t("BC","Boston College Eagles","BC","#98002E","#BC9B6A","CFB")
t("RUT","Rutgers Scarlet Knights","RUT","#CC0033","#5F6A72","CFB")
t("CINC","Cincinnati Bearcats","CIN","#E00122","#000000","CFB")
t("BAY","Baylor Bears","BAY","#154734","#FFB81C","CFB")
t("TXST","Texas State Bobcats","TXST","#501214","#8F8A81","CFB")
t("ULM","UL Monroe Warhawks","ULM","#800029","#CFB53B","CFB")
t("MERR","Merrimack Warriors","MERR","#002F6C","#F9A01B","CFB")
t("UNM","New Mexico Lobos","UNM","#BA0C2F","#A7A8AA","CFB")
t("FAU","Florida Atlantic Owls","FAU","#003366","#CC0000","CFB")
t("COLO","Colorado Buffaloes","COLO","#CFB87C","#000000","CFB")
t("TCU","TCU Horned Frogs","TCU","#4D1979","#A3A9AC","CFB")
t("DEL","Delaware Blue Hens","DEL","#00539F","#FFD200","CFB")
t("GAST","Georgia State Panthers","GSU","#0039A6","#C60C30","CFB")
t("TTU","Texas Tech Red Raiders","TTU","#CC0000","#000000","CFB")
t("MSST","Mississippi State Bulldogs","MSST","#660000","#FFFFFF","CFB")
t("MIAMI","Miami Hurricanes","MIA","#F47321","#005030","CFB")

t("CLEM","Clemson Tigers","CLEM","#F56600","#522D80","CFB")
t("AUB","Auburn Tigers","AUB","#0C2340","#E87722","CFB")
t("WIS","Wisconsin Badgers","WIS","#C5050C","#FFFFFF","CFB")
t("CSU","Colorado State Rams","CSU","#1E4D2B","#C8C372","CFB")
t("MICH","Michigan Wolverines","MICH","#00274C","#FFCB05","CFB")
t("MTSU","Middle Tennessee Blue Raiders","MTSU","#0066CC","#000000","CFB")
# College basketball opponents (added Nov 9, 2026)
t("FAMU","Florida A&M Rattlers","FAMU","#F47937","#00843D","CFB")
t("EKU","Eastern Kentucky Colonels","EKU","#861F41","#FFFFFF","CFB")
t("CHSO","Charleston Southern Buccaneers","CSU","#002855","#B9975B","CFB")
t("WIN","Winthrop Eagles","WIN","#872434","#D5A021","CFB")
t("MER","Mercer Bears","MER","#F76800","#000000","CFB")
t("EVAN","Evansville Purple Aces","EVAN","#4B2E83","#F58025","CFB")
t("SPU","Saint Peter's Peacocks","SPU","#003DA5","#FFFFFF","CFB")
t("VUL","Virginia-Lynchburg Dragons","VUL","#8B1A1A","#FFC72C","CFB")
t("LAGR","LaGrange Panthers","LAGR","#E51937","#000000","CFB")
t("GTWN","Georgetown Hoyas","GTWN","#041E42","#8D817B","CFB")
t("TNST","Tennessee State Tigers","TNST","#00539F","#FFFFFF","CFB")
t("NAU","Northern Arizona Lumberjacks","NAU","#003466","#FFC72C","CFB")
t("PVAM","Prairie View A&M Panthers","PVAM","#4F2D7F","#FFB81C","CFB")
t("SIUE","SIU Edwardsville Cougars","SIUE","#CC0000","#000000","CFB")
t("GWEB","Gardner-Webb Runnin' Bulldogs","GWU","#BB0000","#000000","CFB")
t("UNCA","UNC Asheville Bulldogs","UNCA","#003DA5","#FFFFFF","CFB")
t("SUU","Southern Utah Thunderbirds","SUU","#CC0000","#FFFFFF","CFB")
t("NORF","Norfolk State Spartans","NSU","#007A33","#F3D03E","CFB")
t("CIT","The Citadel Bulldogs","CIT","#3975B7","#FFFFFF","CFB")
t("JVU","Jacksonville Dolphins","JU","#00674A","#FFFFFF","CFB")
t("GRAM","Grambling State Tigers","GRAM","#000000","#ECAA00","CFB")
t("MARQ","Marquette Golden Eagles","MARQ","#003366","#FFCC00","CFB")
t("GONZ","Gonzaga Bulldogs","GONZ","#041E42","#C8102E","CFB")
t("SJU","St. John's Red Storm","SJU","#BA0C2F","#FFFFFF","CFB")
# added Nov 16, 2026
t("CHAT","Chattanooga Mocs","UTC","#00386B","#E0AA0F","CFB")
t("SAM","Samford Bulldogs","SAM","#002649","#CC0000","CFB")
t("TNTC","Tennessee Tech Golden Eagles","TNTC","#4F2984","#FFD100","CFB")
t("MONM","Monmouth Hawks","MONM","#041E42","#FFFFFF","CFB")
t("DAV","Davidson Wildcats","DAV","#000000","#AC1A2F","CFB")
t("EIU","Eastern Illinois Panthers","EIU","#004B83","#9C9A9A","CFB")
t("ELON","Elon Phoenix","ELON","#73000A","#B59A57","CFB")
t("MURR","Murray State Racers","MURR","#002144","#FFCB05","CFB")
t("HCU","Houston Christian Huskies","HCU","#00287A","#F58025","CFB")
t("GWASH","George Washington Revolutionaries","GW","#033C5A","#AA9868","CFB")
t("SELA","Southeastern Louisiana Lions","SELA","#006341","#FFC72C","CFB")
t("WCU","Western Carolina Catamounts","WCU","#592C88","#C5A900","CFB")
t("URI","Rhode Island Rams","URI","#75B2DD","#002147","CFB")
t("NKU","Northern Kentucky Norse","NKU","#000000","#FFC72C","CFB")
t("VILL","Villanova Wildcats","VILL","#003366","#FFFFFF","CFB")
# AP Top 25 football — poll released Sun Nov 8, 2026 (this week's poll was delayed to Mon Nov 16, 2 PM ET by the FAA ground stop that pushed Ole Miss–Oklahoma to Sunday)
AP = {"UGA":1,"UTAH":2,"ND":3,"UCLA":4,"MIAMI":5,"IU":6,"ALA":7,"TEX":8,"TENN":9,"TTU":10,"WAKE":11,"BYU":12,"UK":13,"HOUC":14,"USC":15,"IOWA":16,"BSU":17,"ORE":18,"MISS":19,"SCAR":20,"OSU":21,"ARIZ":22,"UNM":23,"LSU":24,"SMU":25}

# ---- short display names (team name without the mascot) for "Local:" chips and off-week notes
_MULTI = ["Crimson Tide","Blue Devils","Yellow Jackets","Fighting Irish","Demon Deacons","Wolf Pack","Red Raiders","Fighting Illini",
 "Golden Eagles","Golden Grizzlies","Golden Flashes","Golden Bears","Golden Gophers","Golden Hurricane","Golden Knights","Blue Raiders",
 "Red Wolves","Ragin' Cajuns","Sun Devils","Nittany Lions","Rainbow Warriors","Tar Heels","Mean Green","Scarlet Knights","Horned Frogs",
 "Blue Hens","Blue Hose","Fighting Hawks","Thundering Herd","Black Knights","Green Wave","White Sox","Blue Jays","Red Sox","Maple Leafs",
 "Red Wings","Blue Jackets","Trail Blazers","Purple Aces","Red Storm","Runnin' Bulldogs"]
for _k,_t in T.items():
    if _t.get("short"): continue
    n=_t["name"]
    m=next((x for x in _MULTI if n.endswith(" "+x)), None)
    base = n[:-len(m)-1] if m else n.rsplit(" ",1)[0]
    if _t["lg"] in ("NFL","NBA","NHL","MLB"):
        _t["short"] = (m or n.rsplit(" ",1)[1])          # pro: mascot ("Falcons", "White Sox")
    else:
        _t["short"] = base                                # college: school ("Alabama", "Georgia Tech")

# AP men's basketball poll — released Mon Nov 9, 2026 (Nov 16 poll not yet out at build time)
APBB = {"FLA":1,"DUKE":2,"ILL":3,"CONN":4,"MSU":5,"UVA":6,"TEX":7,"HOUC":8,"UCLA":9,"LOU":10,"TENN":11,"ARIZ":12,"SJU":13,"GONZ":14,"KU":15,"TTU":16,"MIAMI":17,"ALA":18,"ARK":19,"MICH":20,"USC":21,"VAN":22,"BYU":23,"UK":24,"NEB":25}

# ---------------- Games ----------------
# fields: date, time (ET, "H:MM AM/PM"), sport, away, home, net, tier ('champ'|'marquee'|''), note, label
G = []
def g(date, time, sport, away, home, net, tier="", note="", label="", neutral=False):
    G.append({"date": date, "time": time, "sport": sport, "away": away, "home": home, "net": net,
              "tier": tier, "note": note, "label": label, "neutral": neutral})

# ======== Monday Nov 16 ========
g("2026-11-16","8:15 PM","NFL","LAC","BAL","ESPN","marquee","Monday Night Football · M&T Bank Stadium · NFL Week 10","MNF")
g("2026-11-16","7:00 PM","NBA","ORL","BOS","PEACOCK","marquee","Peacock NBA Monday · TD Garden")
g("2026-11-16","7:00 PM","NBA","MEMG","WASW","DAZN","","Capital One Arena · also ABC24 (WATN) in Memphis")
g("2026-11-16","7:30 PM","NHL","MTL","NYR","TNT","marquee","NHL on TNT · Madison Square Garden · truTV/HBO Max simulcast")
g("2026-11-16","7:00 PM","NCAAB","CIT","CLEM","ACCN","","Littlejohn Coliseum")
g("2026-11-16","7:00 PM","NCAAB","JVU","UGA","SECN","","Stegeman Coliseum")
g("2026-11-16","7:00 PM","NCAAB","GRAM","UK","SECN+","","Rupp Arena")

# ======== Tuesday Nov 17 ========
g("2026-11-17","6:00 PM","CFB","EMU","WMU","ESPN2","","MAC · MACtion")
g("2026-11-17","7:00 PM","CFB","BALL","OHIO","CBSSN","","MAC · MACtion")
g("2026-11-17","7:00 PM","CFB","M-OH","KENT","ESPNU","","MAC · MACtion")
g("2026-11-17","8:00 PM","NBA","DETP","SAS","NBC","marquee","NBC Coast 2 Coast Tuesday · Peacock simulcast")
g("2026-11-17","11:00 PM","NBA","CHA","LAL","NBC","marquee","NBC Coast 2 Coast Tuesday · Hornets at Lakers · Peacock simulcast · moved to 11:00 ET for national TV")
g("2026-11-17","7:30 PM","NHL","WSH","TBL","HULU","","ESPN+/Hulu national exclusive (streaming only) · Benchmark International Arena")
g("2026-11-17","7:30 PM","NHL","TORM","CHIH","TNT","marquee","NHL on TNT doubleheader · truTV/HBO Max simulcast")
g("2026-11-17","8:00 PM","NHL","NSH","MINW","SPOT-NSH","","Grand Casino Arena, St. Paul")
g("2026-11-17","10:00 PM","NHL","DALS","VGK","TNT","marquee","NHL on TNT doubleheader · truTV/HBO Max simulcast")
g("2026-11-17","2:00 PM","NCAAB","HOUC","RUT","ESPN","","Players Era 8 · Las Vegas · #8 Houston", neutral=True)
g("2026-11-17","4:30 PM","NCAAB","FLA","ND","ESPN","","Players Era 8 · Las Vegas · #1 Florida", neutral=True)
g("2026-11-17","7:00 PM","NCAAB","ILL","DUKE","ESPN","marquee","#3 Illinois at #2 Duke · Cameron Indoor Stadium")
g("2026-11-17","7:00 PM","NCAAB","NORF","GT","ACCNX","","McCamish Pavilion")
g("2026-11-17","7:00 PM","NCAAB","MONM","WAKE","ACCNX","","LJVM Coliseum")
g("2026-11-17","7:00 PM","NCAAB","CLT","DAV","ESPN+","","Belk Arena, Davidson")
g("2026-11-17","7:30 PM","NCAAB","KENN","ALA","SECN+","","Coleman Coliseum · #18 Alabama")
g("2026-11-17","7:30 PM","NCAAB","FIU","UAB","ESPN+","","Bartow Arena")
g("2026-11-17","8:00 PM","NCAAB","EIU","VAN","SECN+","","Memorial Gym · #22 Vanderbilt")
g("2026-11-17","8:00 PM","NCAAB","MTSU","GASO","ESPN+","","Hill Convocation Center, Statesboro")
g("2026-11-17","9:00 PM","NCAAB","MSU","TENN","ESPN2","marquee","#5 Michigan State at #11 Tennessee · Food City Center")
g("2026-11-17","9:30 PM","NCAAB","KU","UNLV","ESPN","","Players Era 8 · Las Vegas · #15 Kansas", neutral=True)
g("2026-11-17","11:59 PM","NCAAB","WVU","AUB","ESPN","","Players Era 8 · Las Vegas · tips at midnight ET (11 PM CT)", neutral=True)

# ======== Wednesday Nov 18 ========
g("2026-11-18","7:00 PM","CFB","AKR","UMASS","CBSSN","","MAC · MACtion")
g("2026-11-18","7:30 PM","CFB","CMU","BUFF","ESPNU","","MAC · MACtion")
g("2026-11-18","7:00 PM","NBA","MILB","MIAH","ESPN","marquee","Kaseya Center")
g("2026-11-18","7:00 PM","NBA","MEMG","CLEC","DAZN","","Rocket Arena")
g("2026-11-18","8:00 PM","NBA","ATLH","OKC","HAWKS","","Paycom Center · Hawks at the defending champs")
g("2026-11-18","9:30 PM","NBA","GSW","DALM","ESPN","marquee","American Airlines Center")
g("2026-11-18","7:30 PM","NHL","BOSB","DETR","TNT","marquee","NHL on TNT · truTV/HBO Max simulcast")
g("2026-11-18","7:00 PM","NCAAB","ELON","SCAR","SECN","","Colonial Life Arena")
g("2026-11-18","9:00 PM","NCAAB","CONN","ARIZ","FS1","marquee","#4 UConn at #12 Arizona · McKale Center")
g("2026-11-18","TBD","NCAAB","AUB","TBD","ESPN2","","Players Era 8 · Las Vegas · semifinal 7:30 PM ESPN2 if Auburn beats WVU; consolation 2:00 PM ESPN or 10:00 PM ESPN2 if not", neutral=True)

# ======== Thursday Nov 19 ========
g("2026-11-19","7:30 PM","CFB","RICE","TEM","ESPN","","American · Lincoln Financial Field")
g("2026-11-19","8:15 PM","NFL","IND","HOU","PRIME","marquee","Thursday Night Football · Prime Video exclusive · NFL Week 11 · NRG Stadium","TNF")
g("2026-11-19","8:00 PM","NBA","GSW","MEMG","DAZN","","FedExForum")
g("2026-11-19","8:00 PM","NBA","NYK","MINT","NBATV","","Target Center")
g("2026-11-19","7:00 PM","NHL","MTL","CARH","HHN","","Lenovo Center · Hurricanes Hockey Network")
g("2026-11-19","7:30 PM","NHL","EDM","TBL","HULU","","ESPN+/Hulu national exclusive (streaming only) · McDavid in Tampa")
g("2026-11-19","10:00 PM","NHL","DALS","VGK","HULU","","ESPN+/Hulu national exclusive (streaming only)")
g("2026-11-19","6:00 PM","NCAAB","NCST","MURR","CBSSN","","Baha Mar Championship · Nassau · semifinal", neutral=True)
g("2026-11-19","8:00 PM","NCAAB","GASO","HCU","ESPN+","","Houston")
g("2026-11-19","TBD","NCAAB","AUB","TBD","ESPN","","Players Era 8 · Las Vegas · final 11:00 PM ESPN · 3rd 2:30 PM · 5th 5:00 PM ESPN · 7th 8:30 PM ESPN2 — depends on results", neutral=True)

# ======== Friday Nov 20 ========
g("2026-11-20","6:00 PM","CFB","ISU","UCF","FS1","","Big 12 · FBC Mortgage Stadium")
g("2026-11-20","7:30 PM","CFB","CLEM","DUKE","ESPN","marquee","ACC · Clemson at Duke · Wallace Wade Stadium · Friday night","CLEMSON–DUKE")
g("2026-11-20","7:30 PM","CFB","BGSU","TOL","ESPN2","","MAC · Battle of I-75")
g("2026-11-20","8:00 PM","CFB","ORE","MSU","FOX","","Big Ten · #18 Oregon · Spartan Stadium")
g("2026-11-20","8:00 PM","CFB","UTEP","AF","CW","","Mountain West")
g("2026-11-20","9:00 PM","CFB","UNM","WYO","FS1","","Mountain West · #23 New Mexico")
g("2026-11-20","7:00 PM","NBA","CHA","ATLH","HAWKS","","NBA Cup · East Group C · Hornets at Hawks · State Farm Arena · Hornets fans: WAXN 64 / DAZN","NBA CUP")
g("2026-11-20","7:30 PM","NBA","TOR","DETP","PRIME","marquee","NBA Cup group play · Prime Video exclusive","NBA CUP")
g("2026-11-20","10:00 PM","NBA","HOUR","DENN","PRIME","marquee","NBA Cup group play · Prime Video exclusive","NBA CUP")
g("2026-11-20","12:30 PM","NCAAB","MTSU","TEM","ESPN+","","Paradise Jam · St. Thomas, USVI · first round", neutral=True)
g("2026-11-20","2:00 PM","NCAAB","UAB","GWASH","CBSSN","","Greenbrier Tip-Off · White Sulphur Springs, WV", neutral=True)
g("2026-11-20","7:00 PM","NCAAB","CCU","TENN","SECN+","","Food City Center · #11 Tennessee")
g("2026-11-20","7:00 PM","NCAAB","SELA","KENN","ESPN+","","VyStar Arena")
g("2026-11-20","7:00 PM","NCAAB","GAST","JVST","ESPN+","","Pete Mathews Coliseum, Jacksonville AL")
g("2026-11-20","TBD","NCAAB","NCST","TBD","CBSSN","","Baha Mar Championship · Nassau · final 9:30 PM or 3rd-place 7:00 PM, both CBS Sports Network", neutral=True)
g("2026-11-20","8:00 PM","NCAAB","UGA","GT","ESPNU","","Georgia at Georgia Tech · McCamish Pavilion · in-state rivalry","UGA–GT")
g("2026-11-20","8:00 PM","NCAAB","UK","IU","CBS","","#24 Kentucky vs Indiana · Lucas Oil Stadium, Indianapolis", neutral=True)
g("2026-11-20","8:00 PM","NCAAB","UCF","VAN","SECN+","","Memorial Gym · #22 Vanderbilt")
g("2026-11-20","9:00 PM","NCAAB","MRSH","UNC","ACCN","","Dean Smith Center")

# ======== Saturday Nov 21 ========
g("2026-11-21","12:00 PM","CFB","SYR","BC","ACCN","","ACC · Alumni Stadium")
g("2026-11-21","12:00 PM","CFB","WAKE","GT","ESPN","marquee","ACC · #11 Wake Forest at Georgia Tech · Bobby Dodd Stadium, Atlanta","WAKE–GT")
g("2026-11-21","12:00 PM","CFB","ECU","ARMY","CBSSN","","American · Michie Stadium, West Point")
g("2026-11-21","12:00 PM","CFB","MEM","NAVY","ESPN2","","American · Navy-Marine Corps Memorial Stadium")
g("2026-11-21","12:00 PM","CFB","UNT","TUL","ESPNU","","American · Yulman Stadium")
g("2026-11-21","12:00 PM","CFB","BYU","KU","ABC","","Big 12 · #12 BYU · David Booth Kansas Memorial Stadium")
g("2026-11-21","12:00 PM","CFB","COLO","CINC","ESPN+","","Big 12 · Nippert Stadium")
g("2026-11-21","12:00 PM","CFB","NW","MINN","FS1","","Big Ten · Huntington Bank Stadium")
g("2026-11-21","12:00 PM","CFB","OSU","NEB","FOX","","Big Ten · #21 Ohio State · Memorial Stadium, Lincoln")
g("2026-11-21","12:00 PM","CFB","WIS","PUR","NBC","","Big Ten · Peacock simulcast")
g("2026-11-21","12:00 PM","CFB","VAN","FLA","SECN","","SEC · Vanderbilt at Florida · The Swamp")
g("2026-11-21","12:00 PM","CFB","WOF","MISS","SECN+","","SEC · #19 Ole Miss vs FCS Wofford · Vaught-Hemingway Stadium")
g("2026-11-21","12:30 PM","CFB","UNC","UVA","CW","","ACC · Scott Stadium, Charlottesville")
g("2026-11-21","1:00 PM","CFB","HOUC","WVU","TNT","","Big 12 · #14 Houston · TNT/truTV")
g("2026-11-21","1:00 PM","CFB","TNTC","MSST","SECN+","","SEC · FCS Tennessee Tech at Mississippi State")
g("2026-11-21","1:00 PM","CFB","WKU","LIB","ESPN+","","Conference USA · Williams Stadium")
g("2026-11-21","2:00 PM","CFB","CLT","TLSA","ESPN+","","American · H.A. Chapman Stadium")
g("2026-11-21","2:00 PM","CFB","CHAT","ALA","SECN+","","SEC · #7 Alabama vs FCS Chattanooga · Bryant-Denny Stadium")
g("2026-11-21","2:00 PM","CFB","MTSU","SHSU","ESPN+","","Conference USA · Bowers Stadium")
g("2026-11-21","2:00 PM","CFB","MOST","JVST","ESPN+","","Conference USA · Burgess-Snow Field")
g("2026-11-21","2:30 PM","CFB","USF","FAU","ESPN+","","American · Boca Raton")
g("2026-11-21","2:30 PM","CFB","IOWA","ILL","BTN","","Big Ten · #16 Iowa · Memorial Stadium, Champaign")
g("2026-11-21","2:30 PM","CFB","ULM","APP","ESPN+","","Sun Belt · Kidd Brewer Stadium")
g("2026-11-21","3:00 PM","CFB","CCU","ULL","ESPN+","","Sun Belt · Cajun Field")
g("2026-11-21","3:00 PM","CFB","DEL","NMSU","ESPN+","","Conference USA")
g("2026-11-21","3:00 PM","CFB","FIU","KENN","ESPN+","","Conference USA · Fifth Third Stadium, Kennesaw")
g("2026-11-21","3:30 PM","CFB","NCST","FSU","ACCN","","ACC · Doak Campbell Stadium")
g("2026-11-21","3:30 PM","CFB","TTU","BAY","FOX","","Big 12 · #10 Texas Tech · McLane Stadium")
g("2026-11-21","3:30 PM","CFB","SAM","AUB","SECN","","SEC · Auburn vs FCS Samford · Jordan-Hare Stadium")
g("2026-11-21","3:30 PM","CFB","ARK","TEX","ESPN","","SEC · #8 Texas · DKR-Texas Memorial Stadium")
g("2026-11-21","3:30 PM","CFB","LSU","TENN","ABC","marquee","SEC · #24 LSU at #9 Tennessee · Neyland Stadium","LSU–TENNESSEE")
g("2026-11-21","3:30 PM","CFB","ODU","CONN","CBSSN","","Non-conference · Rentschler Field")
g("2026-11-21","3:30 PM","CFB","IU","WASH","PEACOCK","","Big Ten · #6 Indiana · Peacock exclusive (streaming only) · Husky Stadium")
g("2026-11-21","3:30 PM","CFB","RUT","PSU","FS1","","Big Ten · Beaver Stadium")
g("2026-11-21","3:30 PM","CFB","UCLA","MICH","CBS","","Big Ten · #4 UCLA at Michigan · The Big House · Paramount+ simulcast")
g("2026-11-21","3:45 PM","CFB","TAMU","OU","ESPN2","","SEC · Gaylord Family Oklahoma Memorial Stadium")
g("2026-11-21","4:00 PM","CFB","NIU","NDSU","CW","","Non-conference · Fargodome")
g("2026-11-21","4:00 PM","CFB","GASO","TROY","ESPN+","","Sun Belt · Veterans Memorial Stadium, Troy")
g("2026-11-21","4:00 PM","CFB","GAST","MRSH","ESPN+","","Sun Belt · Joan C. Edwards Stadium, Huntington")
g("2026-11-21","4:00 PM","CFB","USA","USM","ESPN+","","Sun Belt · M.M. Roberts Stadium, Hattiesburg")
g("2026-11-21","6:00 PM","CFB","WSU","TXST","USA","","Pac-12 · San Marcos")
g("2026-11-21","6:15 PM","CFB","MD","USC","BTN","","Big Ten · #15 USC · LA Memorial Coliseum")
g("2026-11-21","7:00 PM","CFB","VT","MIAMI","ESPN","","ACC · #5 Miami · Hard Rock Stadium")
g("2026-11-21","7:00 PM","CFB","ARIZ","KSU","FS1","","Big 12 · #22 Arizona · Bill Snyder Family Stadium")
g("2026-11-21","7:00 PM","CFB","UNLV","SJSU","CBSSN","","Mountain West · CEFCU Stadium")
g("2026-11-21","7:00 PM","CFB","ARST","LT","ESPN+","","Non-conference · Joe Aillet Stadium")
g("2026-11-21","7:30 PM","CFB","PITT","LOU","ESPN2","","ACC · L&N Federal Credit Union Stadium")
g("2026-11-21","7:30 PM","CFB","STAN","CAL","ACCN","","ACC · Big Game · California Memorial Stadium")
g("2026-11-21","7:30 PM","CFB","SMU","ND","NBC","","#25 SMU at #3 Notre Dame · Notre Dame Stadium · Peacock simulcast")
g("2026-11-21","7:30 PM","CFB","CSU","FRES","CW","","Pac-12 · Valley Children's Stadium")
g("2026-11-21","7:30 PM","CFB","UGA","SCAR","ABC","marquee","SEC · #1 Georgia at #20 South Carolina · Williams-Brice Stadium, Columbia · ABC primetime","GAME OF THE WEEK")
g("2026-11-21","7:30 PM","CFB","UK","MIZ","SECN","","SEC · #13 Kentucky · Faurot Field")
g("2026-11-21","8:00 PM","CFB","UTSA","UAB","ESPNU","","American · Protective Stadium, Birmingham")
g("2026-11-21","9:00 PM","CFB","UTAH","TCU","FOX","","Big 12 · #2 Utah · Amon G. Carter Stadium")
g("2026-11-21","9:30 PM","CFB","SDSU","BSU","USA","","Pac-12 · #17 Boise State · Albertsons Stadium")
g("2026-11-21","10:15 PM","CFB","OKST","ASU","ESPN","","Big 12 · Mountain America Stadium")
g("2026-11-21","10:30 PM","CFB","USU","ORST","CBSSN","","Pac-12 · Reser Stadium")
g("2026-11-21","10:30 PM","CFB","HAW","NEV","FS1","","Mountain West · Mackay Stadium")
g("2026-11-21","7:30 PM","NBA","POR","NYK","NBATV","","Madison Square Garden")
g("2026-11-21","8:00 PM","NBA","MEMG","MINT","DAZN","","Target Center")
g("2026-11-21","10:00 PM","NBA","BOS","SAC2","NBATV","","Golden 1 Center")
g("2026-11-21","1:00 PM","NHL","EDM","CARH","HHN","","Lenovo Center · 1:00 PM matinee · McDavid and the Oilers in Raleigh · Hurricanes Hockey Network")
g("2026-11-21","6:00 PM","NHL","PITP","NSH","SPOT-NSH","","Bridgestone Arena · Crosby and the Penguins")
g("2026-11-21","7:00 PM","NCAAB","WCU","WAKE","ACCNX","","LJVM Coliseum · tip listed 7:00 or 2:00 — verify")
g("2026-11-21","7:00 PM","NCAAB","MICH","VILL","FOX","","#20 Michigan vs Villanova · Xfinity Mobile Arena, Philadelphia", neutral=True)
g("2026-11-21","11:00 PM","NCAAB","WSU","DUKE","ESPN2","","Acrisure Series · Palm Desert, CA · #2 Duke", neutral=True)
g("2026-11-21","TBD","NCAAB","MTSU","TBD","ESPN+","","Paradise Jam · St. Thomas · day 2 · opponent and time depend on Friday result", neutral=True)

# ======== Sunday Nov 22 ========
g("2026-11-22","1:00 PM","NFL","ARI","KC","CBS","","Chiefs at Arrowhead · Paramount+ simulcast"); G[-1]["pop"]=1
g("2026-11-22","1:00 PM","NFL","BAL","CAR","FOX","","Ravens at Panthers · Bank of America Stadium · Lamar Jackson in Charlotte")
g("2026-11-22","1:00 PM","NFL","MIA","BUF","FOX","","AFC East rivalry · Highmark Stadium · network listed FOX by NFL.com, CBS by some guides — verify"); G[-1]["pop"]=1
g("2026-11-22","1:00 PM","NFL","NO","CHI","FOX","","Regional · Soldier Field")
g("2026-11-22","1:00 PM","NFL","PIT","PHI","CBS","","Pennsylvania rivalry · Lincoln Financial Field · moved to 1:00 by the NFL · Paramount+ simulcast"); G[-1]["pop"]=2
g("2026-11-22","1:00 PM","NFL","TB","DET","CBS","","Bucs at Lions · Ford Field · network listed CBS by NFL.com, FOX by some guides — verify"); G[-1]["pop"]=2
g("2026-11-22","1:00 PM","NFL","TEN","DAL","FOX","","Titans at Cowboys · AT&T Stadium")
g("2026-11-22","4:05 PM","NFL","NYJ","LAC","FOX","","Regional · SoFi Stadium · lone 4:05 game")
g("2026-11-22","4:25 PM","NFL","JAX","NYG","CBS","","CBS late window · MetLife Stadium · moved to 4:25 by the NFL · Paramount+ simulcast")
g("2026-11-22","4:25 PM","NFL","LV","DEN","CBS","","CBS late national window · AFC West · Empower Field · Paramount+ simulcast"); G[-1]["pop"]=1
g("2026-11-22","8:20 PM","NFL","MIN","SF","NBC","marquee","Sunday Night Football · Mexico City · Estadio Banorte (49ers designated home) · Peacock simulcast","SNF · MEXICO CITY")
g("2026-11-22","3:30 PM","NBA","DETP","ATLH","HAWKS","","State Farm Arena · Sunday matinee")
g("2026-11-22","12:30 PM","NHL","CARH","NYR","HHN","","Madison Square Garden · 12:30 PM start (moved from 1:00) · Hurricanes Hockey Network")
g("2026-11-22","5:00 PM","NHL","BUFS","TBL","SPOT-TB","","Benchmark International Arena")
g("2026-11-22","2:00 PM","NCAAB","EVAN","MEM","ESPN+","","FedExForum · TV not posted — verify")
g("2026-11-22","7:00 PM","NCAAB","UAB","URI","CBSSN","","Greenbrier Tip-Off · River Division final/placement · TV not posted — verify", neutral=True)
g("2026-11-22","3:30 PM","NCAAB","VT","OKST","ESPN","","Charleston Classic · TD Arena, Charleston SC", neutral=True)

# ======== Monday Nov 23 ========
g("2026-11-23","8:15 PM","NFL","CIN","WAS","ESPN","marquee","Monday Night Football · Northwest Stadium, Landover · NFL Week 11","MNF")
g("2026-11-23","7:00 PM","NBA","MEMG","CHA","HORNETS","","Spectrum Center · Grizzlies at Hornets · Grizzlies fans: DAZN")
g("2026-11-23","7:30 PM","NBA","BKN","MINT","PEACOCK","marquee","Peacock NBA Monday · Target Center")
g("2026-11-23","1:30 PM","NCAAB","CLT","FGCU","ESPN+","","Fort Myers Tip-Off · Palms Division · TV not posted — verify", neutral=True)
g("2026-11-23","2:30 PM","NCAAB","CLEM","MISS","ESPN2","","Maui Invitational · Lahaina Civic Center · quarterfinal", neutral=True)
g("2026-11-23","4:00 PM","NCAAB","GAST","TUL","ESPN+","","Fort Myers Tip-Off · Palms Division · TV not posted — verify", neutral=True)
g("2026-11-23","5:00 PM","NCAAB","BYU","WASH","ESPN2","","Maui Invitational · #23 BYU · quarterfinal", neutral=True)
g("2026-11-23","7:00 PM","NCAAB","GASO","NKU","ESPN+","","Truist Arena, Highland Heights KY · time and TV not posted — verify")
g("2026-11-23","8:00 PM","NCAAB","MONM","UNC","ACCN","","Dean Smith Center · ACCN or ACCNX — verify")
g("2026-11-23","11:30 PM","NCAAB","ARIZ","CSU","ESPN2","","Maui Invitational · #12 Arizona · quarterfinal", neutral=True)
g("2026-11-23","TBD","NCAAB","MTSU","TBD","ESPN+","","Paradise Jam · St. Thomas · championship/placement game · time TBD", neutral=True)

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
 "NFLN": {"label":"NFL Network","ch":"212","inGuide":False},
 "HAWKS": {"label":"WANF 46 / Peachtree Sports Net · Prime Video in-market","ch":"46","inGuide":False},
 "HORNETS":{"label":"WSOC 9 / WAXN 64 · DAZN","ch":"9","inGuide":False},
 "DAZN": {"label":"DAZN (app)","ch":"stream","inGuide":False},
 "NBATV":{"label":"NBA TV","ch":"216","inGuide":False},
 "NHLN": {"label":"NHL Network","ch":"215","inGuide":False},
 "SPOT-NSH":{"label":"The Spot Nashville 28 (OTA) · NHL Network simulcast","ch":"28","inGuide":False},
 "HHN":  {"label":"Hurricanes Hockey Network (Prime Video / Spectrum / DirecTV)","ch":"HHN","inGuide":False},
 "SECN+":{"label":"SEC Network+ (app)","ch":"stream","inGuide":False},
 "ACCNX":{"label":"ACC Network Extra (app)","ch":"stream","inGuide":False},
 "HULU": {"label":"ESPN+ / Hulu (app)","ch":"stream","inGuide":False},
 "FDSN-SUN":{"label":"FanDuel Sports Sun (Tampa market) · out of market: ESPN+ (app)","ch":"stream","inGuide":False},
 "PEACOCK":{"label":"Peacock (app)","ch":"stream","inGuide":False},
 "SPOT-TB":{"label":"The Spot Tampa Bay 66 (OTA) · out of market: ESPN+ (app)","ch":"66","inGuide":False},
}

# ---------------- 17 Locations ----------------
# local: team key -> weight (how much that team matters at this location)
L = []
def loc(id, name, state, market, tz, local, note=""):
    L.append({"id":id,"name":name,"state":state,"market":market,"tz":tz,"local":local,"note":note})

GA_CORE = {"UGA":10,"GT":8,"ATL":10,"ATLB":10,"ATLH":7,"GASO":3,"KENN":3,"GAST":3}
loc("augusta","Augusta","GA","GA","ET", {**GA_CORE,"SCAR":6,"CLT":0}, "Augusta is its own TV market (WJBF 6 ABC · WRDW 12 CBS · WAGT 26 NBC · WFXG 54 FOX). Your guide lists Atlanta affiliates for all Georgia stores — verify locals on the box before game time.")
loc("buford","Buford","GA","GA","ET", GA_CORE)
loc("columbus","Columbus","GA","GA","ET", {**GA_CORE,"AUB":7,"ALA":5}, "Columbus is its own TV market (WTVM 9 ABC · WRBL 3 CBS · WLTZ 38 NBC · WXTX 54 FOX). Your guide lists Atlanta affiliates — verify locals on the box.")
loc("cumming","Cumming","GA","GA","ET", GA_CORE)
loc("dacula","Dacula","GA","GA","ET", GA_CORE)
loc("dallas","Dallas","GA","GA","ET", GA_CORE)
loc("loganville","Loganville","GA","GA","ET", GA_CORE)
loc("stone-mountain","Stone Mountain","GA","GA","ET", GA_CORE)
loc("woodstock","Woodstock","GA","GA","ET", GA_CORE)
loc("myrtle-beach","Myrtle Beach","SC","MYR","ET", {"SCAR":9,"CLEM":9,"CCU":9,"CAR":8,"CHA":5,"CARH":4,"ATLB":6,"UNC":4,"NCST":4})
loc("irmo","Irmo","SC","IRMO","ET", {"SCAR":10,"CLEM":8,"CAR":7,"CHA":5,"CARH":4,"ATLB":6,"UGA":3})
loc("rock-hill","Rock Hill","SC","CLT","ET", {"SCAR":9,"CLEM":9,"CAR":9,"CHA":7,"CARH":5,"CLT":5,"UNC":5,"NCST":5,"ATLB":6})
loc("summerville","Summerville","SC","CHS","ET", {"SCAR":9,"CLEM":9,"CAR":7,"CHA":5,"CARH":4,"ATLB":6,"CCU":3})
loc("concord","Concord","NC","CLT","ET", {"CAR":10,"CHA":8,"CARH":7,"UNC":8,"NCST":8,"CLT":6,"DUKE":6,"WAKE":5,"APP":4,"ATLB":5})
loc("raleigh","Raleigh","NC","RAL","ET", {"NCST":10,"UNC":9,"DUKE":8,"CAR":9,"CARH":9,"CHA":5,"WAKE":6,"ECU":5,"ATLB":5})
loc("huntsville","Huntsville","AL","HSV","CT", {"ALA":10,"AUB":9,"TEN":7,"ATL":6,"ATLB":7,"ATLH":4,"MEMG":4,"NSH":4,"UAB":4,"JVST":4,"USA":2}, "Times shown in Central.")
loc("smyrna","Smyrna","TN","NSH","CT", {"TENN":10,"VAN":8,"TEN":10,"NSH":9,"MEMG":6,"ATLH":3,"ATLB":6,"MTSU":5,"MEM":3}, "Times shown in Central.")

logo = base64.b64encode(open(os.path.join(HERE,"logo.webp"),"rb").read()).decode()

DATA = {"week":WEEK,"teams":T,"ap":AP,"apbb":APBB,"games":G,"markets":MARKETS,"nets":NETS,"locations":L}
json.dump(DATA, open(os.path.join(HERE,"data.json"),"w"))
open(os.path.join(HERE,"logo.b64"),"w").write(logo)
# sanity: every team referenced exists
missing = {k for x in G for k in (x["away"],x["home"]) if k not in T}
print("missing teams:", missing, "| games:", len(G), "| locations:", len(L))
