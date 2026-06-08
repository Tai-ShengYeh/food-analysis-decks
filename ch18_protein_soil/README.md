# 蛋白質分析 Protein Analysis — SOIL HTML 投影片（Nielsen Ch18）

3 小時課程、淺色學術風、含 6 個嵌入式小遊戲。使用共用引擎 `../soil_deck_common.py`。

## 檔案
- `build_ch18.py` — **唯一 source of truth**（改內容改這裡，不要直接改 index.html）
- `index.html` — 產出（29 頁，單一檔、Chart.js 走 CDN）

## 重新產生
```bash
python build_ch18.py
```

## 開啟
瀏覽器直接開 `index.html`，或 `python -m http.server` 後瀏覽。
快捷鍵：← → / 空白鍵切頁、F 全螢幕、點兩側翻頁。

## 6 個嵌入式小遊戲
① 方法依「測什麼」分類（拖放）　② 凱氏定氮 MCQ　③ 方法依「應用」分類（拖放）
④ 凱氏定氮流程排序　⑤ 決策挑戰（選方法，含摻假題）　⑥ 計算闖關（火雞熱狗 %粗蛋白＝14.95%）

## 驗收（1280×720）
29 頁 0 溢出；6 遊戲 + 可排序比較表 + 2 張 Chart.js 圖全部正常。
