import pandas as pd
import csv

data = pd.read_csv("Player Stats.csv")
df = data.head(100)

Name_List = df["Player"].tolist()
PPG_List = df["PPG"].tolist()
APG_List = df["APG"].tolist()
TOV_List = df["TOV"].tolist()
FGper_List = df["FG%"].tolist()
FGM_List = df["FGM"].tolist()
SPG_List = df["SPG"].tolist()
BPG_List = df["BPG"].tolist()
RPG_List = df["RPG"].tolist()

def MVP(ppg,apg,tov,fgper,fgm,spg,bpg,rpg):
    float(ppg)
    float(apg)
    float(tov)
    float(fgper)
    float(fgm)
    float(spg)
    float(bpg)
    float(rpg)
    mvp = (((ppg*1.2) + (apg) + (spg*1.2) + (bpg*5)))-(tov)
    return mvp

class Playerdata:
    def __init__(player, name, ppg, apg, tov, fgper, fgm, spg, bpg,rpg):
        player.name = name
        player.ppg = ppg
        player.apg = apg
        player.tov = tov
        player.fgper = fgper
        player.fgm = fgm
        player.spg = spg
        player.bpg = bpg
        player.rpg = rpg
        player.MVP = MVP(ppg,apg,tov,fgper,fgm,spg,bpg,rpg)
    def playerdata(player):
        print(str(player.name) + " averages " + str(player.ppg) + " pofloats per game " + " and " + str(player.apg) + " assists per game")

PlayerdataList = []

for x in range(100):
    PlayerdataList.append(Playerdata((Name_List[x]), (PPG_List[x]), (APG_List[x]),(TOV_List[x]),(FGper_List[x]),(FGM_List[x]),(SPG_List[x]),(BPG_List[x]),(RPG_List[x])))

for x in range(100):
     print(str(PlayerdataList[x].name) + " averages " + str(PlayerdataList[x].ppg) + " pofloats per game and " + str(PlayerdataList[x].apg) + " assists per game with a " + (str(PlayerdataList[x].MVP)) + " MVP score.")

