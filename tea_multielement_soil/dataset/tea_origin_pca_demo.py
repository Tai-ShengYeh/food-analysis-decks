# -*- coding: utf-8 -*-
"""
教學用「茶葉產地多重元素」資料集 + PCA / 分類示範
================================================================
⚠️ 資料性質（務必對學生講清楚）：
   這是「教學重建資料」——依據以下已發表論文中**各國的平均值與分布範圍**，
   以亂數模擬產生的逐筆樣本（非原始逐筆量測值，原始 raw data 並未公開）：

     蔡承祥、彭宗仁、劉滄棽、林毓雯、詹婉君. 2021.
     以元素特徵區別台灣茶葉與國外茶葉之初步研究. 台灣農業研究 70(4):231–242.
     DOI: 10.6156/JTAR.202112_70(4).0001

   用途：讓學生實際跑 標準化 → PCA → 分類，體會「多重元素指紋 + 機器學習」
   如何把台灣茶與國外茶分開，以及「特徵選擇」為什麼重要。
   想用**真正可下載的真實資料**練習，請見同資料夾 README 指向的蜂蜜 ICP-OES（CC0）資料集。

   元素分三群（呼應論文）：
     微量元素 trace      (mg/kg): Ti Se Cs Ga Sr Ba Cr Ni Co Cu Zn Rb Pb
     風化特徵 weathering (mg/kg): Fe Al Mn
     肥料特徵 fertilizer (%)    : P S K Ca Mg
"""
import csv, os, json, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "tea_origin_teaching.csv")
rng = np.random.default_rng(42)   # 固定種子 → 可重現

TRACE   = ["Ti","Se","Cs","Ga","Sr","Ba","Cr","Ni","Co","Cu","Zn","Rb","Pb"]
WEATHER = ["Fe","Al","Mn"]
FERT    = ["P","S","K","Ca","Mg"]
ELEMENTS = TRACE + WEATHER + FERT

# 各國平均值（讀自論文圖1–3與內文；台灣 vs 國外的判別重點：Ti/Se 台灣偏低、
# Cs 中國偏高、Ga/Sr/Ba 馬來西亞偏高、Cr/Ni/Co 印度偏高；Fe/Al/Mn 與 P/S/K/Ca/Mg 重疊）
MEAN = {  #            Ti    Se    Cs    Ga    Sr    Ba    Cr    Ni    Co    Cu   Zn   Rb   Pb    Fe    Al    Mn     P     S     K    Ca    Mg
  "TW": dict(zip(ELEMENTS,[0.627,0.028,0.05 ,0.52 ,10.0 , 8.0 ,0.23 ,2.7 ,0.20,16,38,30,0.8, 78.9, 569, 756,0.28,0.21,1.74,0.39,0.22])),
  "C" : dict(zip(ELEMENTS,[1.00 ,0.072,0.832,0.70 ,12.0 ,13.0 ,0.25 ,2.6 ,0.17,17,40,28,0.9, 92.0, 810,1120,0.27,0.22,1.55,0.37,0.19])),
  "M" : dict(zip(ELEMENTS,[0.37 ,0.019,0.18 ,2.99 ,28.7 ,50.8 ,0.27 ,3.5 ,0.20,15,35,22,0.7, 62.0,1225, 940,0.21,0.21,1.85,0.53,0.20])),
  "V" : dict(zip(ELEMENTS,[0.85 ,0.17 ,0.09 ,0.25 , 8.0 , 4.5 ,0.39 ,5.3 ,0.41,18,42,26,1.0, 78.0, 490,1210,0.31,0.24,1.80,0.39,0.19])),
  "S" : dict(zip(ELEMENTS,[1.25 ,0.089,0.19 ,1.08 ,16.5 ,15.5 ,0.13 ,3.4 ,0.12,16,37,33,0.8, 77.0, 640, 420,0.24,0.24,2.00,0.45,0.20])),
  "I" : dict(zip(ELEMENTS,[1.38 ,0.032,0.04 ,2.569,14.5 ,43.7 ,0.649,7.87,0.632,17,39,24,0.9,107.0, 880, 930,0.27,0.24,1.78,0.51,0.17])),
}
COUNTRY_NAME = {"TW":"Taiwan","C":"China","M":"Malaysia","V":"Vietnam","S":"SriLanka","I":"India"}
# 每國樣本數（與論文一致：台灣 12、中國 3、越南 1、馬來西亞 1、斯里蘭卡 2、印度 1）
NSAMP = {"TW":12,"C":3,"V":1,"M":1,"S":2,"I":1}
# 組內變異（變異係數 CV）。肥料元素給台灣較大 CV，模擬「各地施肥習性差異大」。
CV_TRACE, CV_WEATHER, CV_FERT, CV_FERT_TW = 0.12, 0.15, 0.10, 0.22

def cv_of(el, country):
    if el in FERT:
        return CV_FERT_TW if country == "TW" else CV_FERT
    if el in WEATHER:
        return CV_WEATHER
    return CV_TRACE

# ---- 產生逐筆資料 ----
rows = []
sid = 1
for c in ["TW","C","V","M","S","I"]:
    for _ in range(NSAMP[c]):
        rec = {"sample_id": "T%02d" % sid, "country": COUNTRY_NAME[c],
               "origin": ("Taiwan" if c == "TW" else "Non-Taiwan")}
        for el in ELEMENTS:
            mu = MEAN[c][el]
            val = rng.normal(mu, mu * cv_of(el, c))
            val = max(val, mu * 0.05)                       # 不為負
            rec[el] = round(float(val), 4 if el in FERT or mu < 1 else 2)
        rows.append(rec); sid += 1

with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    f.write("# 教學重建資料（非原始逐筆量測）。來源統計量：蔡承祥等 2021, 台灣農業研究 70(4):231-242.\n")
    f.write("# 單位：Ti..Pb,Fe,Al,Mn = mg/kg；P,S,K,Ca,Mg = %（重量百分比）。origin 為二分標籤。\n")
    w = csv.DictWriter(f, fieldnames=["sample_id","country","origin"] + ELEMENTS)
    w.writeheader()
    for r in rows:
        w.writerow(r)
print("CSV ->", CSV_PATH, "| rows:", len(rows),
      "| Taiwan:", sum(r["origin"]=="Taiwan" for r in rows),
      "Non-Taiwan:", sum(r["origin"]=="Non-Taiwan" for r in rows))

# ================================================================
# PCA + 分類示範（標準化後）
# ================================================================
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import LeaveOneOut, cross_val_score

X = np.array([[r[e] for e in ELEMENTS] for r in rows], float)
y = np.array([1 if r["origin"]=="Taiwan" else 0 for r in rows])

SETS = {"T (trace 13)":TRACE, "TW (trace+weather 16)":TRACE+WEATHER,
        "TF (trace+fert 18)":TRACE+FERT, "A (all 21)":ELEMENTS}
idx = {e:i for i,e in enumerate(ELEMENTS)}

SHORT = {"T (trace 13)":"T","TW (trace+weather 16)":"TW","TF (trace+fert 18)":"TF","A (all 21)":"A"}
CC = {"Taiwan":"TW","China":"C","Malaysia":"M","Vietnam":"V","SriLanka":"S","India":"I"}
SCORES = {}

print("\n=== PCA 解釋變異 + 留一法(LOO-CV) LDA 分類正確率 ===")
print("%-26s %8s %8s %10s" % ("element set","PC1%","PC2%","LDA LOO-CV"))
results = {}
for name, els in SETS.items():
    cols = [idx[e] for e in els]
    Xs = StandardScaler().fit_transform(X[:, cols])
    pcs = PCA(n_components=min(5, Xs.shape[1])).fit(Xs)
    pc1, pc2 = pcs.explained_variance_ratio_[:2] * 100
    acc = cross_val_score(LinearDiscriminantAnalysis(), Xs, y, cv=LeaveOneOut()).mean() * 100
    results[name] = (pc1, pc2, acc)
    print("%-26s %7.1f%% %7.1f%% %9.1f%%" % (name, pc1, pc2, acc))
    # 匯出 PC1xPC2 得分供互動投影片（定向：台灣在左上，與真實 Fig 4 一致）
    sc = pcs.transform(Xs)[:, :2].astype(float)
    if sc[y==1, 0].mean() > sc[y==0, 0].mean(): sc[:, 0] *= -1
    if sc[y==1, 1].mean() < sc[y==0, 1].mean(): sc[:, 1] *= -1
    pts = [[round(float(sc[i,0]),3), round(float(sc[i,1]),3),
            ("TW" if rows[i]["origin"]=="Taiwan" else CC[rows[i]["country"]])] for i in range(len(rows))]
    SCORES[SHORT[name]] = {"pc1":round(float(pc1),1), "pc2":round(float(pc2),1),
                           "acc":round(float(acc),1), "pts":pts}

with open(os.path.join(HERE, "pca_scores.json"), "w", encoding="utf-8") as f:
    json.dump(SCORES, f, ensure_ascii=False)
print("scores -> pca_scores.json  (供互動切換投影片內嵌)")

print("\n重點：微量元素(trace)就能把台灣茶與國外茶分開；這就是 TFDAF0032.00")
print("用 LDA/Ridge/RF/Boosting/SVM 等模型自動判別產地的資料基礎。")
print("（論文另發現：只加『肥料元素』會因各地施肥差異大而降低 PCA 區分力 → 特徵選擇很重要）")
