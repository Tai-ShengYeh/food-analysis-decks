# -*- coding: utf-8 -*-
"""
茶葉產地判別 — 五種機器學習分類法一次比較（搭配教學投影片 ml_five_models/）
================================================================
同一份資料、同一套前處理（標準化）、同一個評估法（留一法 LOO-CV），
把 TFDAF0032.00 方法所列的 5 種模型放在一起比，輸出每個模型的：
  正確率 accuracy、精確率 precision、召回率 recall（macro 平均）
並把結果寫成 five_models_scores.json 供投影片內嵌。

5 種模型（對應 scikit-learn 類別）：
  LDA            -> LinearDiscriminantAnalysis   線性判別分析（傳統統計）
  Ridge          -> RidgeClassifier              脊（嶺）迴歸分類（L2 正則化線性）
  Random Forest  -> RandomForestClassifier       隨機森林（多棵樹投票）
  Boosting       -> GradientBoostingClassifier   梯度提升（一棵接一棵補錯）
  SVM            -> SVC(kernel="rbf")            支援向量機（最大間隔 + 核函數）

⚠️ 資料為「教學重建資料」（依 蔡承祥等 2021 各國平均值與分布以亂數模擬，非原始逐筆）。
   用途是讓學生實跑、看見「不同模型在同一資料上的表現差異」。
執行：python tea_five_models_demo.py
"""
import csv, os, json
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "tea_origin_teaching.csv")

# 與投影片一致：用「微量元素 T（13 個）」這組正確特徵來比模型
TRACE = ["Ti", "Se", "Cs", "Ga", "Sr", "Ba", "Cr", "Ni", "Co", "Cu", "Zn", "Rb", "Pb"]

# ---- 讀資料（跳過 # 註解列）----
rows = []
with open(CSV_PATH, encoding="utf-8") as f:
    for line in f:
        if line.startswith("#"):
            continue
        rows.append(line)
reader = csv.DictReader(rows)
data = list(reader)

X = np.array([[float(r[e]) for e in TRACE] for r in data], float)
y = np.array([1 if r["origin"] == "Taiwan" else 0 for r in data])
print("樣本數 n =", len(y), "| 台灣 =", int(y.sum()), "境外 =", int((1 - y).sum()),
      "| 特徵數 =", X.shape[1])

# ---- 五種模型 ----
MODELS = {
    "LDA":           LinearDiscriminantAnalysis(),
    "Ridge":         RidgeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=300, random_state=0),
    "Boosting":      GradientBoostingClassifier(random_state=0),
    "SVM":           SVC(kernel="rbf", C=1.0, gamma="scale"),
}

# ---- 留一法交叉驗證：每個模型都把標準化包進 pipeline（避免資訊洩漏）----
loo = LeaveOneOut()
out = {}
print("\n=== 五模型 · 留一法(LOO-CV) · 微量元素 T(13) ===")
print("%-15s %8s %10s %8s" % ("model", "accuracy", "precision", "recall"))
for name, clf in MODELS.items():
    pipe = make_pipeline(StandardScaler(), clf)
    pred = cross_val_predict(pipe, X, y, cv=loo)
    acc = accuracy_score(y, pred) * 100
    pre = precision_score(y, pred, average="macro", zero_division=0) * 100
    rec = recall_score(y, pred, average="macro", zero_division=0) * 100
    out[name] = {"acc": round(acc, 1), "precision": round(pre, 1), "recall": round(rec, 1)}
    print("%-15s %7.1f%% %9.1f%% %7.1f%%" % (name, acc, pre, rec))

with open(os.path.join(HERE, "five_models_scores.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False)
print("\nscores -> five_models_scores.json （供投影片內嵌）")
print("提醒：小樣本(n=20)下，線性模型(LDA/Ridge/SVM)常與樹模型不相上下，")
print("      重點是『同一份資料、同一評估法』下的公平比較，而非追求單一最高分。")
