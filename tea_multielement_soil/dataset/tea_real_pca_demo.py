# -*- coding: utf-8 -*-
"""
茶葉產地判別 — 用「真實、已發表」的紅茶元素資料跑 PCA + 多類 PLS-DA(LOO-CV)。

兩個來源（皆為 open-access，數值逐欄抄自論文內嵌表格，非臆造）：
  [A] Brzezicha-Cirocka et al. 2016, Biol Trace Elem Res — 紅茶 4 產地 × 14 元素（FAAS）
      表 Table 4 給「各產地 mean ± SD」(mg/100 g)。PMC5344953。
      原始逐筆值未公開 → 用各產地 mean±SD「重建」逐筆（同 tea_origin_pca_demo.py 手法），
      樣本數採論文實際數：China 12 / India 17 / Ceylon 10 / Kenya 4。
  [B] "Bioelements in black teas" 2021 — 紅茶 7 國 20 個「真實茶樣」× 8 元素（FAAS, mg/kg）
      表 Table 1 直接列出 20 個產品的逐樣平均值 → 直接當 20 個真實資料點，無需重建。PMC8512582。
      論文自報 PCA：PC1 29.96% / PC2 22.52% / PC3 17.12%（前 3 個 69.61%）。

⚠️ 技術為 FAAS（非 ICP-MS）、且 [A] 為重建。但「標準化→PCA→PLS-DA→LOO」流程與 ICP-MS 完全相同。
輸出：blacktea_4origin_reconstructed.csv、blacktea_7country_products.csv，並印出實跑結果。
"""
import os, json, numpy as np, pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import LeaveOneOut

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(2026)

# ---------- [A] Brzezicha-Cirocka 2016, Table 4 (mg/100 g) ----------
# 丟掉 Cd（India/Ceylon/Kenya 皆 <LOD，只有 China 有 → 會讓 China 變得太好認；當作 <LOD 教學註記）
ELEMS_A = ["Ca","K","Mg","Na","P","Mn","Fe","Zn","Cu","Co","Cr","Ni","Pb"]
# 每個產地：(n 樣本, {element:(mean, sd)})
ORIGIN_A = {
 "China":  (12, {"Ca":(161,101),"K":(2666,223),"Mg":(764,77),"Na":(67.3,61.4),"P":(408,58.0),
                 "Mn":(30.9,11.8),"Fe":(0.90,0.26),"Zn":(4.25,0.63),"Cu":(2.25,0.42),
                 "Co":(0.03,0.01),"Cr":(0.08,0.02),"Ni":(0.50,0.21),"Pb":(0.05,0.04)}),
 "India":  (17, {"Ca":(153,35),"K":(2803,161),"Mg":(822,103),"Na":(30.7,11.5),"P":(359,40),
                 "Mn":(30.4,10.5),"Fe":(0.57,0.29),"Zn":(3.70,0.60),"Cu":(2.39,0.50),
                 "Co":(0.02,0.01),"Cr":(0.07,0.03),"Ni":(0.58,0.13),"Pb":(0.02,0.01)}),
 "Ceylon": (10, {"Ca":(168,51),"K":(2981,153),"Mg":(769,42),"Na":(55.5,31.0),"P":(305,53),
                 "Mn":(27.7,10.3),"Fe":(0.43,0.09),"Zn":(2.70,0.52),"Cu":(1.83,0.14),
                 "Co":(0.02,0.01),"Cr":(0.05,0.01),"Ni":(0.35,0.10),"Pb":(0.02,0.01)}),
 "Kenya":  (4,  {"Ca":(155,33),"K":(2738,119),"Mg":(774,63),"Na":(21.8,6.06),"P":(344,25),
                 "Mn":(53.2,12.6),"Fe":(0.53,0.01),"Zn":(2.74,0.22),"Cu":(1.85,0.17),
                 "Co":(0.02,0.01),"Cr":(0.11,0.06),"Ni":(0.36,0.05),"Pb":(0.013,0.003)}),
}

rowsA = []
for origin, (n, stats) in ORIGIN_A.items():
    for i in range(n):
        row = {"sample_id": f"{origin[:2].upper()}{i+1:02d}", "origin": origin}
        for e in ELEMS_A:
            m, s = stats[e]
            row[e] = round(float(max(rng.normal(m, s), m*0.02)), 4)  # 不允許負值
        rowsA.append(row)
dfA = pd.DataFrame(rowsA)
dfA.to_csv(os.path.join(HERE, "blacktea_4origin_reconstructed.csv"), index=False, encoding="utf-8")

# ---------- [B] Bioelements in black teas 2021, Table 1 (mg/kg) — 20 個真實產品 ----------
ELEMS_B = ["Na","K","Ca","Mg","Cu","Zn","Mn","Fe"]
PRODUCTS_B = [
 # tea_id, country, region, Na,K,Ca,Mg,Cu,Zn,Mn,Fe
 ("JO","Japan","Organic",49.11,11158.11,842.56,877.12,5.30,24.42,443.46,26.91),
 ("JS","Japan","Shizuoka",18.74,10577.44,503.44,821.64,8.94,21.94,302.52,32.92),
 ("NI1","Nepal","Ilam",53.24,15323.11,1150.33,1068.08,12.46,35.81,395.22,94.94),
 ("NI2","Nepal","Ilam",21.31,12195.33,994.20,1041.76,11.97,25.73,224.11,36.08),
 ("NI3","Nepal","Ilam",27.42,11199.44,838.77,842.08,11.10,25.28,359.41,79.42),
 ("NI4","Nepal","Ilam",53.44,12752.67,1532.00,1022.39,11.78,22.42,301.14,103.86),
 ("K1","Kenya","Marinyn",30.14,12192.78,857.28,996.16,22.08,23.38,824.72,99.52),
 ("K2","Kenya","Mount Kenya",45.19,10969.11,1556.11,932.21,12.57,20.31,459.44,64.39),
 ("Ir","Iran","Lahijan",41.20,8344.56,1417.33,1017.43,23.87,24.10,730.14,179.53),
 ("SLC","Sri Lanka","Central",109.72,10222.33,1478.56,1097.82,21.57,23.51,285.81,131.06),
 ("SLU","Sri Lanka","Uva",50.57,13794.22,1856.11,1229.56,12.26,27.64,453.46,37.93),
 ("SLR","Sri Lanka","Ruhuna",29.97,11289.67,1380.33,997.88,10.91,12.54,224.78,28.97),
 ("BChI","Blend","China/India",44.83,10576.78,1027.32,901.47,16.56,31.08,525.49,80.86),
 ("CHY1","China","Yunnan",14.47,12705.11,1232.67,905.68,12.39,31.19,846.29,61.27),
 ("CHY2","China","Yunnan",54.00,11693.56,1518.78,1040.59,10.11,22.11,465.11,109.81),
 ("CHY3","China","Yunnan",11.24,11905.33,1115.00,951.72,10.08,21.73,513.97,29.24),
 ("CHF","China","Fujian",113.97,9635.33,1588.00,990.81,13.67,22.98,711.44,108.82),
 ("IA1","India","Assam",19.22,12805.33,1602.67,1233.44,19.48,23.61,202.77,33.56),
 ("IA2","India","Assam",17.87,12146.67,1465.00,1035.66,15.34,35.03,434.61,42.42),
 ("ID","India","Darjeeling",49.00,11498.67,1482.67,961.62,14.88,27.48,250.64,34.32),
]
dfB = pd.DataFrame(PRODUCTS_B, columns=["tea_id","country","region"]+ELEMS_B)
dfB.to_csv(os.path.join(HERE, "blacktea_7country_products.csv"), index=False, encoding="utf-8")

def pca_report(X, label):
    Z = StandardScaler().fit_transform(X)
    p = PCA().fit(Z)
    evr = (p.explained_variance_ratio_*100).round(2)
    print(f"  [{label}] PCA EVR%: PC1={evr[0]} PC2={evr[1]} PC3={evr[2] if len(evr)>2 else '-'}  (PC1+2={round(evr[0]+evr[1],1)})")
    return Z, evr

def plsda_loo(Z, y_labels, max_nc=5):
    labels = sorted(set(y_labels))
    yidx = np.array([labels.index(l) for l in y_labels])
    Y = np.zeros((len(yidx), len(labels))); Y[np.arange(len(yidx)), yidx] = 1
    best = None
    for nc in range(2, min(max_nc, Z.shape[1], len(labels)+2)+1):
        pred = np.empty(len(yidx), dtype=int)
        for tr, te in LeaveOneOut().split(Z):
            pls = PLSRegression(n_components=nc).fit(Z[tr], Y[tr])
            pred[te] = pls.predict(Z[te]).argmax(1)
        acc = float((pred == yidx).mean())
        if best is None or acc > best["acc"]:
            best = {"nc": nc, "acc": acc, "pred": pred}
    K = len(labels)
    cm = [[int(((yidx==r)&(best["pred"]==c)).sum()) for c in range(K)] for r in range(K)]
    return labels, best, cm

print("="*64)
print("[A] 紅茶 4 產地（重建自 Brzezicha 2016 各產地 mean±SD；13 元素）")
print(f"    樣本數 {len(dfA)}：" + " ".join(f"{k}={v[0]}" for k,v in ORIGIN_A.items()))
Za, _ = pca_report(dfA[ELEMS_A].values, "4-origin recon")
labels, best, cm = plsda_loo(Za, dfA["origin"].tolist())
print(f"  多類 PLS-DA（{best['nc']} 成分, LOO-CV）整體正確率 = {best['acc']*100:.1f}%")
print(f"  類別順序 {labels}")
for r,l in enumerate(labels):
    print(f"    真實 {l:7s} -> {cm[r]}  (sens {cm[r][r]/sum(cm[r])*100:.0f}%)")

print("="*64)
print("[B] 紅茶 7 國 20 個真實產品（Bioelements 2021；8 元素，無重建）")
Zb, evrb = pca_report(dfB[ELEMS_B].values, "20 real products")
print("    論文自報 PCA：PC1 29.96% / PC2 22.52% / PC3 17.12%（對照上面實算）")
# 分類：類別太小的併入，做有意義的多類
grp = dfB["country"].replace({"Iran":"Other","Japan":"EastAsia","China":"EastAsia",
                              "Nepal":"SouthAsia","India":"SouthAsia","Sri Lanka":"SouthAsia",
                              "Kenya":"Africa","Blend":"Other"})
dfB2 = dfB[grp!="Other"].copy(); g2 = grp[grp!="Other"]
labels2, best2, cm2 = plsda_loo(StandardScaler().fit_transform(dfB2[ELEMS_B].values), g2.tolist(), max_nc=4)
print(f"  分區多類 PLS-DA（{best2['nc']} 成分, LOO-CV, 併小類 EastAsia/SouthAsia/Africa, n={len(dfB2)}）= {best2['acc']*100:.1f}%  {labels2}")

print("="*64); print("已輸出 blacktea_4origin_reconstructed.csv、blacktea_7country_products.csv 到", HERE)
