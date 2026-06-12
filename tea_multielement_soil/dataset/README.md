# 茶葉產地判別 — ML 教學資料集

用來示範 TFDAF0032.00 方法裡「多重元素指紋 + 機器學習判別產地」的教學素材。
搭配 [tea_multielement_soil](../) 投影片的「PCA 真實示範 / 特徵選擇」段落。

---

## 1. 教學重建資料（本資料夾）

| 檔案 | 說明 |
|------|------|
| `tea_origin_teaching.csv` | 20 筆茶樣 × 21 元素 + 二分標籤（Taiwan / Non-Taiwan） |
| `tea_origin_pca_demo.py` | 產生 CSV + 跑 標準化→PCA→LDA 留一法交叉驗證 + 匯出 `pca_scores.json` |
| `pca_scores.json` | 四種元素子集的 PC1×PC2 得分（投影片「互動切換」頁直接內嵌使用） |

> ⚠️ **資料性質**：逐筆數值是依下列論文的**各國平均值與分布範圍以亂數模擬**而成，
> **非原始逐筆量測值**（原始 raw data 並未公開）。固定亂數種子(42)，可重現。
> 用途是讓學生「實際跑一遍、看見分群」，不可當作真實實驗數據引用。
>
> 來源統計量：**蔡承祥、彭宗仁、劉滄棽、林毓雯、詹婉君. 2021. 以元素特徵區別台灣茶葉與國外茶葉之初步研究. 台灣農業研究 70(4):231–242.** DOI:10.6156/JTAR.202112_70(4).0001

**欄位**：`sample_id, country, origin` + 21 元素
- 微量 (mg/kg)：Ti Se Cs Ga Sr Ba Cr Ni Co Cu Zn Rb Pb
- 風化 (mg/kg)：Fe Al Mn
- 肥料 (%)：P S K Ca Mg

**執行**：
```bash
python tea_origin_pca_demo.py
```

**實跑結果（已驗證，標準化後）—— 重現論文「特徵選擇」結論**：

| 元素子集 | PC1% | PC2% | LDA 留一法正確率 |
|----------|:----:|:----:|:----:|
| T 微量 (13) | 37.1 | 24.7 | **95.0%** |
| TW 微量+風化 (16) | 33.9 | 23.2 | 95.0% |
| TF 微量+肥料 (18) | 30.6 | 19.0 | 90.0% |
| A 全部 (21) | 29.2 | 18.6 | 85.0% |

→ 微量元素就能把台灣茶與國外茶分開；**加入肥料元素反而變差**（呼應論文：肥料受各地施肥習慣影響、變異大，是干擾因子）。這就是機器學習的 **特徵選擇 (feature selection)**。

---

## 2. 真實、可引用的替代資料集（紅茶產地，本資料夾已附 CSV）

茶葉產地的**逐筆**開放資料幾乎不存在（多為 "data on request"），但有 open-access 論文**內嵌了完整、有國別標籤的元素表**。本資料夾已把其中兩份整理成可直接讀的 CSV：

| 檔案 | 來源 | 內容 | 主要用途 |
|------|------|------|----------|
| `blacktea_7country_products.csv` | [B] 2021 | **20 個真實茶樣** × 8 元素，7 國（日/尼泊爾/肯亞/伊朗/斯里蘭卡/中國/印度）| **PCA**（真實點、無重建）|
| `blacktea_4origin_reconstructed.csv` | [A] 2016 | 43 筆 × 13 元素，4 產地（中/印/錫蘭/肯亞）| **多類 PLS-DA**（重建自各產地 mean±SD）|
| `tea_real_pca_demo.py` | — | 產生上兩個 CSV + 跑 PCA + 多類 PLS-DA(LOO-CV) | 一鍵重現 |

**執行**：`python tea_real_pca_demo.py`

**實跑結果（已驗證）**：
- **[B] 20 個真實茶樣 PCA**：PC1 **31.5%** / PC2 **24.8%**（PC1+2＝56.3%）→ **幾乎重現論文自報的 PC1 29.96% / PC2 22.52%**，證明是真資料、流程正確（很好的可信度教學點）。
- **[A] 4 國多類 PLS-DA（3 成分, LOO-CV）＝ 88.4%**：Ceylon 100%、India 94%、China 75%、Kenya 75%（China↔India/Kenya 互混 → 真實的「分類不總是滿分」）。

**來源（皆 open-access，數值逐欄抄自論文內嵌表格，非臆造）**：
- [A] Brzezicha-Cirocka et al. 2016, *Biol Trace Elem Res* — 紅茶 4 產地 14 元素（FAAS）。Table 4 各產地 mean±SD。**PMC5344953**。
- [B] "Bioelements in black teas" 2021 — 紅茶 7 國 20 產品 8 元素（FAAS）。Table 1 逐產品值；論文自報 PCA。**PMC8512582**。

**蜂蜜 CC0**（唯一「免抄、直接下載」的逐筆集）— Mendeley `tt6pp6pbpk`（**CC0 公眾領域**），429×12，pure/syrup/adulterated；原論文 Liu et al. 2021 *Food Chemistry* 343:128455。化學計量同構，教「機制」一流。

> ⚠️ **誠實標註**：
> - 技術是 **FAAS（非 ICP-MS）**；但「標準化→PCA→PLS-DA→LOO」流程與 ICP-MS 完全相同。
> - `blacktea_4origin_reconstructed.csv` 是**重建**（依各產地 mean±SD 模擬逐筆，種子 2026 可重現）、非原始逐筆；`blacktea_7country_products.csv` 是 **20 個真實產品的逐樣平均值（無重建）**。
> - 茶種為紅茶（非台灣烏龍）；講台灣案例時要說明。
> - 台灣專屬的開放茶葉元素資料集**確認不存在**（Tsai 2021 只摘要開放、無可下載資料）。

> 教學設計建議（hybrid）：用 **[B] 20 真實紅茶** 教 PCA「真實手感」、**[A] 4 國重建** 教多類 PLS-DA、**Tsai 2021 重建＋互動切換**講台灣產地與特徵選擇、**蜂蜜 CC0** 當免抄即跑的後備。
