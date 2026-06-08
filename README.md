# 食品分析 · 互動教學投影片（Nielsen's Food Analysis）

9 章互動式 HTML 教學投影片，每章為 3 小時課程、淺色學術風、各含 6 個嵌入式形成性評量小遊戲。單一 HTML、可離線、跨裝置（手機／平板／桌機）。

🔗 **線上瀏覽（GitHub Pages）**：開啟本 repo 的 Pages 首頁即可進入九宮格入口。

## 章節

| 章 | 主題 | 連結 |
|---|---|---|
| 12 | 層析原理 Principles of Chromatography | `ch12_soil/` |
| 13 | 高效液相層析 HPLC | `ch13_hplc_soil/` |
| 14 | 氣相層析 Gas Chromatography | `ch14_gc_soil/` |
| 15 | 水分分析 Moisture Analysis | `ch15_moisture_soil/` |
| 16 | 灰分分析 Ash Analysis | `ch16_ash_soil/` |
| 17 | 油脂分析 Fat Analysis | `ch17_fat_soil/` |
| 18 | 蛋白質分析 Protein Analysis | `ch18_protein_soil/` |
| 19 | 碳水化合物分析 Carbohydrate Analysis | `ch19_carb_soil/` |
| 21 | 礦物質分析 Mineral Analysis | `ch21_mineral_soil/` |

共 9 章 · 約 283 頁 · 54 個小遊戲。

## 操作
← → / 空白鍵切頁　·　F 全螢幕　·　點畫面兩側翻頁。

## 開發
- 共用引擎：`soil_deck_common.py`（資料驅動：切頁／MCQ／拖放配對／排序／計算／可排序比較表／Chart.js）。
- 每章 `chXX_*/build_chXX.py` 為**唯一 source of truth**；改內容後執行 `python build_chXX.py` 重新產生該章 `index.html`。**請勿直接編輯 index.html**。
- 第 17 章使用獨立的 `build_fat_deck.py`（內嵌引擎）。

## 技術
純前端：HTML + CSS + 原生 JS，圖表用 Chart.js（CDN），字型用 Google Fonts（CDN）。小遊戲計分為前端即時（不蒐集任何資料）。

## 授權與聲明
投影片內容、程式、互動小遊戲為**原創教學素材**。內容參考 *Nielsen's Food Analysis*（B. P. Ismail, S. S. Nielsen 編，Springer）之章節架構；**本 repo 不包含任何課本 PDF 或受版權保護之原文**。供教學使用。
