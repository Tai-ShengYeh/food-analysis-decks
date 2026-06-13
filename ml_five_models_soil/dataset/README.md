# 五模型示範資料（ml_five_models_soil）

搭配 [../](../) 投影片「五種機器學習分類法 × 茶葉產地判別」。

| 檔案 | 說明 |
|------|------|
| `tea_five_models_demo.py` | LDA／Ridge／RF／Boosting／SVM 一次比較；標準化 + 留一法 LOO-CV（含 StandardScaler pipeline 防洩漏），輸出每個模型的 accuracy／precision／recall |
| `tea_origin_teaching.csv` | 20 茶樣 × 21 元素 + 二分標籤（Taiwan／Non-Taiwan）|
| `five_models_scores.json` | 實跑結果，投影片內嵌用 |

**執行**：
```bash
python tea_five_models_demo.py
```

**實跑結果（微量元素 T13，留一法 LOO-CV，可重現）**：

| 模型 | accuracy | precision | recall |
|------|:--------:|:---------:|:------:|
| LDA | 95.0% | 96.2% | 93.8% |
| Ridge | 100.0% | 100.0% | 100.0% |
| Random Forest | 95.0% | 96.2% | 93.8% |
| Boosting | 85.0% | 90.0% | 81.2% |
| SVM | 100.0% | 100.0% | 100.0% |

→ 小樣本(n=20)下，線性模型(LDA/Ridge/SVM)常與樹模型不相上下；Boosting 因資料太少而過擬合、反而最低。重點是「同一份資料、同一評估法」下的**公平比較**。

> ⚠️ 資料為**教學重建**（依蔡承祥等 2021 各國平均值與分布以亂數模擬，種子固定、非原始逐筆）。
> 與 `../../tea_multielement_soil/dataset/` 同源；該資料夾另附**真實可下載**的紅茶開放資料與蜂蜜 ICP-OES（CC0）。
