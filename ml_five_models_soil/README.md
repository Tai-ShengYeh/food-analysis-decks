# 五種機器學習分類法 · 茶葉產地判別（教學 HTML）

接續 **茶葉多重元素檢驗 TFDAF0032.00**：14 元素指紋拿到後，電腦怎麼自動判「臺灣 vs 境外」？
本片把方法所列的 **5 種分類模型**一字排開，每一種都給「**一句話直覺 + Python (scikit-learn) 程式 + Orange Data Mining 積木**」兩條實作路線。

單一自含 `index.html`（深色「茶綠＋金」主題，與 tea deck 同家族），用瀏覽器打開即可。

## 五種模型（本片真實 LOO-CV 正確率，微量元素 T13）

| 模型 | 家族 | scikit-learn | Orange 積木 | 正確率 |
|------|------|--------------|-------------|:------:|
| LDA | 傳統·線性 | `LinearDiscriminantAnalysis` | （無原生→ Logistic Regression）| 95% |
| Ridge | 傳統·線性 | `RidgeClassifier` | Logistic Regression（Ridge L2）| 100% |
| Random Forest | ML·樹集成 | `RandomForestClassifier` | Random Forest ✓ | 95% |
| Boosting | ML·樹集成 | `GradientBoostingClassifier` | Gradient Boosting ✓ | 85% |
| SVM | ML·間隔/核 | `SVC` | SVM ✓ | 100% |

> **教學亮點（誠實的反直覺結果）**：在這份 n=20 的小資料上，最「高級」的 Boosting 反而最低（85%），
> 樸素的 Ridge／SVM 卻滿分——集成樹胃口大、小資料易過擬合；線性模型在小而乾淨的資料上又穩又準。
>
> **Orange 誠實標註**：Orange 的 Model 類別**沒有** LDA／Ridge 原生分類積木，需用
> **Logistic Regression**（可選 Ridge L2 正則化）代表「線性分界」這一家；RF／Gradient Boosting／SVM 則都是原生積木。

## 重新建置

```bash
python build_ml.py      # -> index.html（build_ml.py 是唯一 source of truth，勿直接改 index.html）
```
重用 `../soil_deck_common.py` 共用引擎（深色 skin + Python 高亮 + Orange 畫布 SVG）。

## 鍵盤操作

- `←` / `→` / 空白鍵：上一頁／下一頁
- 點畫面左右兩側：翻頁
- `F`：全螢幕

## dataset/（課堂實作）

| 檔案 | 說明 |
|------|------|
| `tea_five_models_demo.py` | 五模型一起跑 · 標準化 + 留一法 LOO-CV，輸出 accuracy／precision／recall（本片數字來源，可重現）|
| `tea_origin_teaching.csv` | 20 茶樣 × 21 元素 + 二分標籤（臺灣／境外）|
| `five_models_scores.json` | 上述結果（投影片內嵌用）|

執行：`python tea_five_models_demo.py`

> ⚠️ **資料性質**：`tea_origin_teaching.csv` 為**教學重建資料**——依蔡承祥等 (2021)
> 《以元素特徵區別台灣茶葉與國外茶葉之初步研究》各國平均值與分布以亂數模擬（固定種子、可重現），
> **非原始逐筆量測值**，僅供教學實跑、不可當真實數據引用。真實可下載的同構資料見
> `../tea_multielement_soil/dataset/README.md`（紅茶開放資料、蜂蜜 ICP-OES CC0）。

## 19 + 1 頁結構（SOIL 三段式）

- **引起動機**：封面 → 14 維太難用眼睛看 → 一份資料×五模型×兩條路
- **維持注意**：監督式分類 + LOO-CV → 標準化共同起點 → 五模型總覽 → LDA／Ridge／RF／Boosting／SVM 逐一詳解 → 真實正確率對比 → 互動①配對程式類別
- **喚起行動**：Orange 完整工作流 → Python 完整工作流 → 決策表（該用哪個）→ 互動②觀念速測 → 動手做兩條路 → 自我檢核 → 結語
