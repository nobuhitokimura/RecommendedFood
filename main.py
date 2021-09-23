import pprint
import math
import sys
from dimod import *
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import csv


###
### 変数
###
foodData = []   # 料理名
Amount = []     # 金額
Calorie = []    # カロリー
Protein = []    # プロテイン
Lipid = []      # 脂質
Carbs = []      # 炭水化物


###
### CSV読み込み
### 料理データ取得
###
foodData = open("./foodData.csv")
#print(foodData)
for c in foodData:
    if c == 0:
        continue
    else:
        l = c.split(',')
        foodData.append(l[1]);
        Amount = []
        Calorie = []
        Protein = []
        Lipid = []
        Carbs = []
