# -*- coding: utf-8 -*-
"""Nielsen Ch18 Protein Analysis — SOIL HTML deck. Uses ../soil_deck_common.py.
Run: python build_ch18.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
KJELDAHL_SVG = """
<svg viewBox="0 0 300 380">
 <defs><linearGradient id="gk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eaf2ff"/><stop offset="1" stop-color="#cfe0f6"/></linearGradient></defs>
 <path d="M150 20 v90" stroke="#1f6feb" stroke-width="3"/>
 <path d="M135 24 h30" stroke="#1f6feb" stroke-width="3"/>
 <circle cx="150" cy="250" r="78" fill="url(#gk)" stroke="#1f6feb" stroke-width="3"/>
 <path d="M138 112 h24 v40 h-24 z" fill="url(#gk)" stroke="#1f6feb" stroke-width="3"/>
 <path d="M95 270 a58 58 0 0 0 110 0 z" fill="#fbeede"/>
 <text x="150" y="258" text-anchor="middle" class="lblb">樣品 + H₂SO₄</text>
 <text x="150" y="278" text-anchor="middle" class="lbl">+ 催化劑</text>
 <path d="M132 70 q6 -14 12 0 M150 60 q6 -14 12 0" fill="none" stroke="#d9822b" stroke-width="2.4"/>
 <text x="210" y="70" class="lbl">加熱消化</text>
 <rect x="104" y="336" width="92" height="18" rx="6" fill="#48597a"/>
 <text x="150" y="372" text-anchor="middle" class="lbl">凱氏瓶 Kjeldahl flask</text>
</svg>"""

DUMAS_SVG = """
<svg viewBox="0 0 560 230">
 <g font-size="13">
  <rect x="14" y="80" width="110" height="64" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="69" y="106" text-anchor="middle" class="lblb">燃燒爐</text>
  <text x="69" y="126" text-anchor="middle" class="lbl">700–1000°C / O₂</text>
  <rect x="160" y="80" width="110" height="64" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="215" y="106" text-anchor="middle" class="lblb">銅還原管</text>
  <text x="215" y="126" text-anchor="middle" class="lbl">600°C：NOx→N₂</text>
  <rect x="306" y="80" width="110" height="64" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="361" y="106" text-anchor="middle" class="lblb">GC 管柱</text>
  <text x="361" y="126" text-anchor="middle" class="lbl">He 載送分離</text>
  <rect x="452" y="80" width="96" height="64" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="500" y="106" text-anchor="middle" class="lblb">TCD 偵測</text>
  <text x="500" y="126" text-anchor="middle" class="lbl">熱導定量 N</text>
  <g stroke="#8493ad" stroke-width="2.5" fill="none" marker-end="url(#ar)">
   <path d="M124 112 h34"/><path d="M270 112 h34"/><path d="M416 112 h34"/></g>
  <defs><marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#8493ad"/></marker></defs>
  <text x="280" y="40" text-anchor="middle" class="lblb" font-size="15">Dumas 氮燃燒分析儀</text>
 </g>
</svg>"""

DTREE_SVG = """
<svg viewBox="0 0 980 360">
 <rect x="380" y="14" width="220" height="56" rx="12" fill="#1f6feb"/>
 <text x="490" y="40" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">你的目標是什麼？</text>
 <text x="490" y="60" text-anchor="middle" fill="#cfe0f6" font-size="12">選擇蛋白質分析方法</text>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M420 70 C 200 110,130 120,120 150"/><path d="M470 70 C 400 120,380 120,375 150"/>
  <path d="M510 70 C 590 120,610 120,625 150"/><path d="M560 70 C 800 110,860 120,875 150"/></g>
 <g font-size="14" font-weight="800">
  <rect x="30" y="150" width="190" height="120" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="125" y="178" text-anchor="middle" fill="#15233f">高脂樣品?</text>
  <text x="125" y="206" text-anchor="middle" fill="#d9822b" font-size="16">Kjeldahl</text>
  <text x="125" y="232" text-anchor="middle" fill="#48597a" font-size="12">Dumas 燃燒怕起火</text>
  <text x="125" y="252" text-anchor="middle" fill="#48597a" font-size="12">高脂改用凱氏法</text>
  <rect x="280" y="150" width="190" height="120" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="375" y="178" text-anchor="middle" fill="#15233f">營養標示?</text>
  <text x="375" y="206" text-anchor="middle" fill="#1f6feb" font-size="16">Dumas</text>
  <text x="375" y="232" text-anchor="middle" fill="#48597a" font-size="12">快速、安全、自動</text>
  <text x="375" y="252" text-anchor="middle" fill="#48597a" font-size="12">已大量取代凱氏</text>
  <rect x="530" y="150" width="190" height="120" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="625" y="178" text-anchor="middle" fill="#15233f">純化蛋白定量?</text>
  <text x="625" y="206" text-anchor="middle" fill="#1f9d6b" font-size="16">BCA / Lowry</text>
  <text x="625" y="232" text-anchor="middle" fill="#48597a" font-size="12">高靈敏、微量</text>
  <text x="625" y="252" text-anchor="middle" fill="#48597a" font-size="12">BCA 容忍洗滌劑</text>
  <rect x="780" y="150" width="190" height="120" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="875" y="178" text-anchor="middle" fill="#15233f">穀物快速品管?</text>
  <text x="875" y="206" text-anchor="middle" fill="#15233f" font-size="16">NIR 紅外</text>
  <text x="875" y="232" text-anchor="middle" fill="#48597a" font-size="12">快速、非破壞</text>
  <text x="875" y="252" text-anchor="middle" fill="#48597a" font-size="12">需先校正</text>
 </g>
</svg>"""

# ---------------- 引起動機 ----------------
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 18",
    "蛋白質<span style='color:var(--accent-2)'>分析</span>", "Protein Analysis",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>凱氏定氮 · Dumas 燃燒 · 比色法 · UV 吸收 · 非蛋白氮",
    ["Kjeldahl","Dumas","Biuret/BCA","染料結合","UV 280nm"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">一杯牛奶的蛋白質，<span class="hi">是怎麼量出來的？</span></div>
  <p class="subtitle" style="max-width:780px;margin:22px auto 0">蛋白質種類繁多、結構複雜，無法直接「秤」出來。<br>
  關鍵在於——蛋白質含有一個獨特的元素：<strong>氮 (N)</strong>。</p>
  <div style="margin-top:24px"><span class="pill">營養標示</span><span class="pill">定價</span>
  <span class="pill">功能性</span><span class="pill">生物活性</span><span class="pill">摻假檢測</span></div></div>""")

add(MOT, dc.kt("18.1.2 為什麼重要", "為什麼要分析蛋白質") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("🏷️","營養標示","法規要求標示蛋白質含量") +
    dc.card("💰","定價","穀物、乳品常以蛋白(氮)含量計價","a") +
    dc.card("🍞","功能性","麵筋、酪蛋白、蛋白決定加工特性","g") +
    dc.card("🧫","生物活性","酵素、抑制劑活性以每 mg 蛋白表示","b") + '</div>')

add(MOT, dc.kt("18.1.1 分類與組成", "蛋白質與<span class='hi'>氮</span>") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li><strong>簡單蛋白</strong>：水解後只有胺基酸</li>" +
    "<li><strong>共軛蛋白</strong>：另含非胺基酸成分</li>" +
    "<li>20 種 α-胺基酸以<strong>胜肽鍵</strong>相連</li>" +
    "<li>蛋白質含氮量 <span class='em'>13.4–19.1%</span>，因胺基酸組成而異</li>" +
    '</ul></div><div class="note"><strong>關鍵：氮是蛋白質最具辨識性的元素。</strong><br>' +
    "非蛋白氮 (NPN) 也含氮——所以氮法測到的是<strong>粗蛋白</strong>。</div></div>")

add(MOT, dc.chart_inner("prot", "食物裡的<span class='hi'>蛋白質</span>含量", "資料：USDA FoodData Central (2023)，% 蛋白質（濕基）。",
    kicker="18.1.3 食物中的含量"), ' data-chart="prot"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">核心命題</div>
  <div class="hook" style="font-size:clamp(1.7rem,4vw,3rem)">測蛋白，先<span class="hi">測氮</span></div>
  <p class="lead" style="max-width:820px;margin:20px auto 0">大多數方法的根基：先測<strong>氮含量</strong>，再乘上<strong>換算因子</strong>得到蛋白質。</p>
  <div class="eq" style="max-width:520px;margin:24px auto 0">% 蛋白質 = % N × 換算因子<br>
  <span style="font-size:.8em;color:var(--ink-2)">蛋白多含 16% N → 因子 = 100/16 = 6.25</span></div></div>""")

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","方法依「測什麼」分類", 7,
    "每個方法的化學基礎是什麼？把 7 個方法分到三類。"), ' data-game="g1"')

# ---------------- 維持注意 ----------------
add(ATT, dc.kt("方法全覽", "四大方法家族") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("🧪","氮法","Kjeldahl 凱氏定氮、Dumas 燃燒法","b") +
    dc.card("📡","光譜法","紅外 IR / NIR（胜肽鍵）","a") +
    dc.card("🎨","比色法","Biuret、Lowry、BCA、染料結合","g") +
    dc.card("🔆","UV 吸收","280nm(Trp/Tyr)、220nm(胜肽鍵)","b") + '</div>')

add(ATT, dc.kt("18.2.1 凱氏定氮", "Kjeldahl：百年經典") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + KJELDAHL_SVG + '</div><div><ul class="clean">' +
    "<li><strong>消化</strong>：H₂SO₄ + 催化劑把有機氮轉成硫酸銨</li>" +
    "<li><strong>中和蒸餾</strong>：加鹼釋出氨，蒸餾入硼酸液</li>" +
    "<li><strong>滴定</strong>：標準 HCl 滴定硼酸根 → 算出 N</li>" +
    "<li>測到的是<span class='em'>粗蛋白</span>（含非蛋白氮）</li>" +
    '</ul><div class="note" style="margin-top:14px">1883 年 Johann Kjeldahl 發明；三步驟沿用至今。</div></div></div>')

add(ATT, dc.chart_inner("fac", "為什麼換算因子<span class='hi'>不一樣</span>？",
    "Table 18.3：不同食物蛋白的含氮量不同 → 換算因子不同。", kicker="18.2.1 換算因子", height="52vh"),
    ' data-chart="fac"')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","凱氏定氮即時測驗", 4), ' data-game="g2"')

add(ATT, dc.kt("18.2.2 Dumas 燃燒法", "Dumas：快速、安全、自動") +
    '<div class="svgwrap" style="margin-top:10px">' + DUMAS_SVG + '</div>' +
    '<div class="note" style="margin-top:16px">高溫燃燒釋出 N₂，以 GC-TCD 定量<strong>總氮</strong>（含無機氮）。' +
    "免危險試劑、數分鐘完成、可自動化——已大量取代凱氏法。</div>")

add(ATT, dc.kt("兩種氮法比較", "Kjeldahl vs Dumas") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧪","Kjeldahl","測<strong>有機氮+氨</strong>；便宜、用腐蝕性試劑；<strong>高脂樣品首選</strong>（不怕燃燒起火）","b") +
    dc.card("🔥","Dumas","測<strong>總氮</strong>（含硝酸鹽）；快速安全、設備貴；營養標示/品管廣用","a") +
    '</div><div class="note" style="margin-top:18px">三聚氰胺等<strong>含氮摻假物</strong>會被兩種氮法一起算進去 → 虛報蛋白。</div>')

add(ATT, dc.game_sort_inner("g4","小遊戲 ③","凱氏定氮流程排序", 6,
    "用 ▲▼ 把凱氏定氮的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("18.3 紅外光譜", "IR / NIR：測胜肽鍵") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("📡","原理","蛋白的<strong>胜肽鍵</strong>在特定波長吸收（中紅外 6.47 µm；NIR 多個波段）","b") +
    dc.card("⚡","應用","乳品蛋白分析儀（中紅外）；穀物、肉、乳品（NIR）。快速品管，需先校正","a") +
    '</div><div class="note" style="margin-top:18px">間接法——只是<strong>估計值</strong>，必須對官方法建立檢量線。</div>')

add(ATT, dc.kt("18.4 比色法", "顏色 = 蛋白質的訊號") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🟣","銅離子系","Biuret(胜肽鍵·540nm)、Lowry(+酚試劑·750nm)、BCA(562nm)","b") +
    dc.card("🔵","染料結合","Bradford 用 Coomassie 藍(595nm)；陰離子染料結合鹼性胺基酸","a") +
    '</div><div class="note" style="margin-top:18px">需用標準蛋白(如 BSA)建檢量線——報的是<strong>相對</strong>含量，靈敏度高、用量少。</div>')

add(ATT, dc.kt("銅離子三兄弟", "Biuret → Lowry → BCA") +
    '<div class="grid3" style="margin-top:22px">' +
    dc.card("🟣","Biuret","胜肽鍵 + Cu²⁺ → 紫色 540nm。簡單、干擾少、靈敏度低","b") +
    dc.card("🔬","Lowry","Biuret + 酚試劑(Trp/Tyr) → 750/500nm。靈敏但試劑不穩","a") +
    dc.card("🟢","BCA","Cu⁺ 螯合 BCA → 562nm。靈敏、容忍洗滌劑，純化常用","g") + '</div>')

add(ATT, dc.game_bucket_inner("g3","小遊戲 ④","方法依「應用場景」分類", 7,
    "同樣這些方法，換個角度——它們最常用在哪裡？分到三類。"), ' data-game="g3"')

add(ATT, dc.kt("18.5 UV 吸收法", "紫外光下的蛋白質") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🔆","280 nm","<strong>Trp / Tyr</strong> 芳香胺基酸吸收；非破壞、快速；適純化蛋白(Beer 定律 A=abc)","b") +
    dc.card("〰️","205–220 nm","<strong>胜肽鍵</strong>吸收；可測少 Trp/Tyr 的胜肽；需純、清澈樣品","a") +
    '</div><div class="note" style="margin-top:18px">核酸也在 280nm 吸收 → 需相對純的樣品；不同蛋白 E₂₈₀ 不同。</div>')

add(ATT, dc.kt("18.6 非蛋白氮 NPN", "抓出「假蛋白」摻假") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>用 <strong>三氯醋酸 (TCA)</strong> 沉澱蛋白質</li>" +
    "<li>過濾/離心，分離上清液中的非蛋白氮</li>" +
    "<li>對上清液做凱氏/Dumas 測 N → 換算</li></ul></div>" +
    '<div class="note">用途：檢測以<strong>尿素、氨、三聚氰胺</strong>等含氮物造假。' +
    "因為氮法分不出真蛋白與假氮，NPN 能補位。</div></div>")

add(ATT, dc.kt("摻假的破口", "為什麼三聚氰胺<span class='hi'>騙得過</span>氮法？") +
    '<div class="note" style="margin-top:14px">三聚氰胺含氮量極高(66%)。凱氏/Dumas 只測「氮」，' +
    "把它當成蛋白質 → <strong>虛報高蛋白</strong>。2007 寵物食品、2008 奶粉事件皆然。</div>" +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("🚫","氮法的盲點","只看氮原子，分不出來源是真蛋白還是含氮化合物","b") +
    dc.card("🛡️","破解策略","用<strong>不靠氮</strong>的方法(染料結合/胺基酸)與氮法<strong>比對</strong>，數值兜不攏就有問題","a") + '</div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對方法", 5), ' data-game="g5"')

# ---------------- 喚起行動 ----------------
add(ACT, dc.cmp_inner("一張表選方法（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"meas","t":"s","label":"化學基礎"},
     {"k":"speed","t":"n","label":"速度","star":True},{"k":"app","t":"s","label":"主要應用"}],
    "速度：★ 越多越快。整合自 Table 18.2。", kicker="18.7 方法比較"), ' data-game="cmp"')

add(ACT, dc.kt("方法選擇", "跟著決策樹走") +
    '<div class="svgwrap" style="margin-top:10px">' + DTREE_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:14px">下一頁實戰：算一條火雞熱狗的粗蛋白 →</p>')

add(ACT, dc.kt("18.11 計算", "凱氏定氮：從 mL HCl 到 % 蛋白") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">% N = ' +
    '<span class="frac"><b>N · (V樣品−V空白) · 14.007</b><span>樣品克數</span></span> × 100</div>' +
    '<div><ul class="clean"><li>滴定的 mol HCl = mol NH₃ = mol N</li>' +
    "<li>扣除試劑空白</li><li>% N × 換算因子 = % 粗蛋白</li>" +
    "<li>肉類因子 6.25（16% N）</li></ul></div></div>")

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關",
    "火雞熱狗：樣品 0.5172 g，HCl 為 0.1027 N，滴定樣品用 8.8 mL、空白 0.2 mL。"
    "求<strong>粗蛋白 %</strong>（肉類因子 6.25）。", unit="%"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li><strong>測蛋白＝先測氮</strong>，再乘換算因子（粗蛋白）</li>" +
    "<li>氮法：<strong>Kjeldahl</strong>(高脂首選) vs <strong>Dumas</strong>(快速取代)</li>" +
    "<li>換算因子因含氮量而異（肉 6.25、奶 6.38、小麥 5.33）</li></ul>" +
    '<ul class="clean"><li>比色/UV：靈敏、需標準蛋白校正</li>' +
    "<li>含氮摻假(三聚氰胺)會騙過氮法 → 用 NPN/非氮法比對</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["解釋為什麼「測蛋白」要先「測氮」",
     "說出凱氏定氮的三大步驟與順序",
     "比較 Kjeldahl 與 Dumas 的差異與適用時機",
     "解釋換算因子為何隨食物不同",
     "判斷該用哪種方法（高脂/標示/純化/品管）",
     "由滴定數據算出 % 粗蛋白",
     "說明含氮摻假為何能騙過氮法"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把蛋白質分析<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions、Practice Problems<br>"
    "🔜 銜接章節：<strong>碳水化合物分析 (Ch19)</strong>、<strong>水分分析 (Ch15)</strong><br>"
    "🧪 思考：你的樣品含脂高嗎？要測標示還是純化？該選哪種方法？",
    ["Kjeldahl","Dumas","Biuret/BCA","Bradford","UV 280"]), ' data-cover="1"')

# ---------------- CFG ----------------
CFG = {
  "charts": {
    "prot": {"type":"bar","yTitle":"% 蛋白質",
      "labels":["黃豆","脫脂奶粉","牛肉乾","鮪魚罐","切達起司","雞胸","全麥麵粉","蛋","優格","蘋果"],
      "datasets":[{"label":"% 蛋白質","data":[36.5,36.2,31.1,26.5,24.2,22.5,13.2,12.6,5.25,0.26],"color":"#1f6feb"}]},
    "fac": {"type":"bar","yTitle":"換算因子",
      "labels":["蛋/肉","牛奶","小麥","玉米","燕麥","黃豆","米"],
      "datasets":[{"label":"N→蛋白 換算因子","data":[6.25,6.38,5.33,5.65,5.36,5.52,5.17],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["測氮","測胜肽鍵","測芳香胺基酸/染料"],
      "items":[{"t":"Kjeldahl 凱氏","c":"測氮"},{"t":"Dumas 燃燒","c":"測氮"},
        {"t":"Biuret","c":"測胜肽鍵"},{"t":"紅外光譜 IR","c":"測胜肽鍵"},{"t":"UV 220nm","c":"測胜肽鍵"},
        {"t":"UV 280nm","c":"測芳香胺基酸/染料"},{"t":"Bradford 染料","c":"測芳香胺基酸/染料"}],
      "ok":"🎉 全對！氮法測 N、Biuret/IR/220nm 測胜肽鍵、280nm/染料測芳香胺基酸。",
      "tip":"提示：紅外與 220nm 都是看「胜肽鍵」；280nm 看 Trp/Tyr。"},
    "g3": {"cats":["營養標示/法定","蛋白純化研究","快速品管"],
      "items":[{"t":"Kjeldahl","c":"營養標示/法定"},{"t":"Dumas","c":"營養標示/法定"},
        {"t":"BCA","c":"蛋白純化研究"},{"t":"Lowry","c":"蛋白純化研究"},{"t":"UV 280nm","c":"蛋白純化研究"},
        {"t":"NIR 紅外","c":"快速品管"},{"t":"染料結合(Sprint)","c":"快速品管"}],
      "ok":"🎉 正確！氮法做法定標示、比色/UV 做純化、紅外與染料做快速品管。",
      "tip":"提示：BCA/Lowry/UV280 多用於蛋白純化；NIR 與 Sprint 染料是現場快速品管。"}
  },
  "mcq": {
    "g2":[
      {"q":"凱氏定氮測到的是「粗蛋白」，原因是？","o":["只測純蛋白","也測到非蛋白氮(NPN)","只測脂肪","只測碳"],"a":1,
       "e":"氮法把所有含氮物都算進去，故稱粗蛋白。"},
      {"q":"蛋白質的換算因子 6.25 是怎麼來的？","o":["100÷16","16÷100","6.25×N","隨機"],"a":0,
       "e":"多數蛋白含 16% N，100/16 = 6.25。"},
      {"q":"凱氏定氮的正確三步驟是？","o":["蒸餾→消化→滴定","消化→中和蒸餾→滴定","滴定→消化→蒸餾","萃取→燃燒→滴定"],"a":1,
       "e":"先消化成硫酸銨，再中和蒸餾出氨，最後滴定。"},
      {"q":"為什麼不同食物的換算因子不同？","o":["蛋白含氮量不同","秤重不同","溫度不同","顏色不同"],"a":0,
       "e":"各食物蛋白的胺基酸組成不同 → 含氮量不同 → 因子不同。"}
    ],
    "g5":[
      {"q":"高脂肪樣品(如香腸)測蛋白，較安全的選擇？","o":["Dumas 燃燒","Kjeldahl 凱氏","NIR","UV280"],"a":1,
       "e":"高脂在 Dumas 燃燒可能起火，高脂樣品首選凱氏法。"},
      {"q":"要做大量樣品的營養標示蛋白，現多用？","o":["Kjeldahl","Dumas 燃燒","Lowry","Bradford"],"a":1,
       "e":"Dumas 快速、安全、可自動化，已大量取代凱氏。"},
      {"q":"純化中的蛋白質定量、樣品含洗滌劑，最適合？","o":["BCA","UV280","Kjeldahl","Dumas"],"a":0,
       "e":"BCA 容忍洗滌劑、靈敏度好，純化常用。"},
      {"q":"穀物工廠要快速、非破壞地監測蛋白，選？","o":["Kjeldahl","NIR 紅外","Biuret","NPN"],"a":1,
       "e":"NIR 快速非破壞，適合線上/品管，但需先校正。"},
      {"q":"懷疑小麥麩質摻三聚氰胺(含氮假蛋白)，最佳策略？","o":["只用 Kjeldahl","只用 Dumas","染料結合法與氮法比對","只看顏色"],"a":2,
       "e":"含氮摻假騙得過氮法；用不靠氮的染料法與氮法比對才抓得出。"}
    ]
  },
  "sort": {
    "g4":{"steps":["樣品磨碎、精秤放入凱氏瓶","加 H₂SO₄ + 催化劑消化（→硫酸銨）",
       "加鹼中和硫酸","蒸餾出氨，導入硼酸溶液","用標準 HCl 滴定硼酸根","由 N 量 × 換算因子 = 粗蛋白"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！消化→中和→蒸餾→滴定→換算。","tip":"提示：一定先消化成硫酸銨，最後才換算成蛋白。"}
  },
  "calc": {
    "g6":{"answer":14.95,"tol":0.3,
      "ok":"🎉 正確！%N=(8.8−0.2)×0.1027×14.007÷517.2mg×100 = 2.39%；×6.25 = <b>14.95%</b> 粗蛋白。",
      "bad":"再算算：先算 %N =(8.8−0.2)×0.1027×14.007÷(0.5172×1000)×100 ≈ 2.39%，再 ×6.25。",
      "hint":"提示：校正體積 8.6 mL；%N≈2.39%；×6.25 ≈ 14.9~15.0%。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"meas"},{"k":"speed"},{"k":"app"}],
    "rows":[
      {"m":"Kjeldahl","meas":"總有機氮","speed":2,"app":"全部食品·高脂首選·法定"},
      {"m":"Dumas","meas":"總氮","speed":4,"app":"營養標示·品管(廣用)"},
      {"m":"紅外 IR/NIR","meas":"胜肽鍵","speed":5,"app":"穀物·乳品快速品管"},
      {"m":"染料結合","meas":"鹼性胺基酸","speed":4,"app":"品管·摻假比對"},
      {"m":"Biuret","meas":"胜肽鍵","speed":3,"app":"蛋白定量(基礎)"},
      {"m":"Lowry","meas":"胜肽鍵+胺基酸","speed":2,"app":"研究·高靈敏"},
      {"m":"BCA","meas":"胜肽鍵+胺基酸","speed":3,"app":"蛋白純化(容忍洗滌劑)"},
      {"m":"UV 280nm","meas":"Trp/Tyr","speed":4,"app":"純化蛋白·管柱偵測"}
    ]
  }
}

dc.build_html(
  {"title":"蛋白質分析 Protein Analysis · Nielsen Ch18","brand":"PROTEIN · CH18"},
  S, CFG, OUT)
