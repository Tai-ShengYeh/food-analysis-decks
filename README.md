# 食品分析 · 互動教學投影片（Nielsen's Food Analysis ＋ 食藥署公告檢驗方法）

16 份互動式 HTML 教學 deck —— **12 章 Nielsen《食品分析》** ＋ **4 項衛福部食藥署公告／建議檢驗方法**。每份為 3 小時課程、淺色學術風，各含 **6 個嵌入式形成性評量小遊戲**（拖放配對、選擇題、排序、計算、可排序比較表、互動圖表）。單一 HTML、可離線、跨裝置（手機／平板／桌機）。

🔗 **線上入口（九宮格）**：<https://tai-shengyeh.github.io/food-analysis-decks/>

---

## 一、Nielsen《食品分析》章節（12 章）

| 章 | 主題 | 線上連結 |
|---|---|---|
| 9  | 原子光譜：AAS／AES／ICP-MS | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch9_atomic_soil/) |
| 10 | 核磁共振 NMR | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch10_nmr_soil/) |
| 11 | 質譜 Mass Spectrometry | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch11_ms_soil/) |
| 12 | 層析原理 Principles of Chromatography | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch12_soil/) |
| 13 | 高效液相層析 HPLC | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch13_hplc_soil/) |
| 14 | 氣相層析 Gas Chromatography | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch14_gc_soil/) |
| 15 | 水分分析 Moisture Analysis | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch15_moisture_soil/) |
| 16 | 灰分分析 Ash Analysis | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch16_ash_soil/) |
| 17 | 油脂分析 Fat Analysis | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch17_fat_soil/) |
| 18 | 蛋白質分析 Protein Analysis | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch18_protein_soil/) |
| 19 | 碳水化合物分析 Carbohydrate Analysis | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch19_carb_soil/) |
| 21 | 礦物質分析 Mineral Analysis | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/ch21_mineral_soil/) |

## 二、食藥署公告檢驗方法 · 食品安全檢測（4 項）

| 方法代號 | 主題 | 核心技術 | 線上連結 |
|---|---|---|---|
| MOHWA0030 | 食品中甜味劑（13 品項） | LC-MS/MS · ESI · MRM | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/tfda_sweeteners_soil/) |
| MOHWA0013 | 食品中二氧化硫 | 通氣蒸餾 ＋ 鹼滴定（Monier-Williams） | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/tfda_so2_soil/) |
| TFDAA0086 | 食品中硼酸 | 薑黃素呈色 · 550 nm 分光光度 | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/tfda_boric_soil/) |
| MOHWV0036 | 四環素類動物用藥殘留（7 品項） | LC-MS/MS · ESI · MRM · EDTA 螯合萃取 | [開啟 →](https://tai-shengyeh.github.io/food-analysis-decks/tfda_tetracycline_soil/) |

> 依衛福部食藥署公告／建議檢驗方法之原理與流程編寫，為原創教學素材。

**合計：16 份 deck · 約 447 頁 · 96 個小遊戲。**

## 三、光譜系列 Ch6–8（附帶鏡像）

本 repo 另含光譜學基礎、UV-Vis／螢光、紅外光譜的靜態鏡像：`ch6_spectroscopy/`、`ch6_soil/`、`ch7_uvvis/`、`ch8_ir/`。
（部分頁面的 Firebase 即時互動功能——文字雲／測驗存檔——僅在原 Firebase 站台可用；GitHub 版供公開瀏覽。）

## 操作

← → / 空白鍵切頁　·　F 全螢幕　·　點畫面兩側翻頁。

## 開發

- 共用引擎：`soil_deck_common.py`（資料驅動：切頁／MCQ／拖放配對／排序／計算／可排序比較表／Chart.js）。
- 每份 deck 的 build 腳本為**唯一 source of truth**：Nielsen 章用 `chXX_*/build_chXX.py`、食藥署方法用 `tfda_*/build_<topic>.py`；改內容後執行該腳本重新產生該 deck 的 `index.html`。**請勿直接編輯 index.html。**
- 第 17 章使用獨立的 `build_fat_deck.py`（內嵌引擎）。

## 技術

純前端：HTML + CSS + 原生 JS，圖表用 Chart.js（CDN），字型用 Google Fonts（CDN）。小遊戲計分為前端即時，**不蒐集任何資料**。

## 授權與聲明

投影片內容、程式與互動小遊戲為**原創教學素材**，供教學使用。Nielsen 章節參考 *Nielsen's Food Analysis*（B. P. Ismail, S. S. Nielsen 編，Springer）之章節架構；食藥署方法 deck 依公告／建議檢驗方法之原理與流程編寫。**本 repo 不含任何課本 PDF、受版權保護之原文或官方文件原檔。**
