# -*- coding: utf-8 -*-
"""Nielsen Ch13 High-Performance Liquid Chromatography (HPLC) — SOIL HTML deck.
Uses ../soil_deck_common.py. Run: python build_ch13.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
# 儀器流程：幫浦→注射器→管柱→偵測器→資料站（style 同 build_ch18 DUMAS_SVG flow boxes）
HPLC_FLOW_SVG = """
<svg viewBox="0 0 720 250">
 <g font-size="13">
  <rect x="14" y="92" width="104" height="64" rx="10" fill="#eaf2ff" stroke="#1f6feb" stroke-width="2"/>
  <text x="66" y="118" text-anchor="middle" class="lblb">溶劑槽</text>
  <text x="66" y="138" text-anchor="middle" class="lbl">移動相 (eluent)</text>
  <rect x="150" y="92" width="104" height="64" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="202" y="118" text-anchor="middle" class="lblb">幫浦</text>
  <text x="202" y="138" text-anchor="middle" class="lbl">0.2–2 mL/min</text>
  <rect x="286" y="92" width="104" height="64" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="338" y="118" text-anchor="middle" class="lblb">注射器</text>
  <text x="338" y="138" text-anchor="middle" class="lbl">定量環 10–100µL</text>
  <rect x="422" y="92" width="104" height="64" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="474" y="118" text-anchor="middle" class="lblb">管柱</text>
  <text x="474" y="138" text-anchor="middle" class="lbl">固定相·分離</text>
  <rect x="558" y="92" width="104" height="64" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="610" y="118" text-anchor="middle" class="lblb">偵測器</text>
  <text x="610" y="138" text-anchor="middle" class="lbl">訊號→波峰</text>
  <g stroke="#8493ad" stroke-width="2.5" fill="none" marker-end="url(#arh)">
   <path d="M118 124 h30"/><path d="M254 124 h30"/><path d="M390 124 h30"/><path d="M526 124 h30"/></g>
  <defs><marker id="arh" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#8493ad"/></marker></defs>
  <rect x="558" y="186" width="104" height="46" rx="10" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="610" y="206" text-anchor="middle" class="lblb">資料站</text>
  <text x="610" y="223" text-anchor="middle" class="lbl">層析圖·積分</text>
  <path d="M610 156 v30" stroke="#8493ad" stroke-width="2.5" fill="none" marker-end="url(#arh)"/>
  <text x="360" y="44" text-anchor="middle" class="lblb" font-size="15">HPLC 系統流程 (Fig. 13.1)</text>
  <text x="360" y="66" text-anchor="middle" class="lbl">高壓推送移動相，樣品隨之過管柱被分離</text>
 </g>
</svg>"""

# 注射器 load / inject 兩態示意
INJECTOR_SVG = """
<svg viewBox="0 0 760 430">
<defs><marker id="av" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0 0 L6 3.5 L0 7 z" fill="#5b6b88"/></marker></defs>
<g font-size="12">
<text x="215" y="106" text-anchor="middle" class="lblb" font-size="14">(a) LOAD 載入</text>
<circle cx="215" cy="210" r="58" fill="#f6f9fd" stroke="#9fb3d1" stroke-width="2"/>
<path d="M215.0 152.0 C 119.0 162.0, 119.0 258.0, 215.0 268.0" fill="none" stroke="#475569" stroke-width="4"/>
<text x="115" y="206" text-anchor="middle" class="lblb" font-size="12" fill="#475569">定量環</text>
<text x="115" y="222" text-anchor="middle" class="lbl" font-size="10.5" fill="#475569">sample loop</text>
<path d="M265.2 181.0 Q 240.1 210.0 265.2 239.0" fill="none" stroke="#1f6feb" stroke-width="5" stroke-linecap="round"/>
<path d="M164.8 181.0 Q 202.4 188.2 215.0 152.0" fill="none" stroke="#d9822b" stroke-width="5" stroke-linecap="round"/>
<path d="M215.0 268.0 Q 202.4 231.8 164.8 239.0" fill="none" stroke="#d9822b" stroke-width="5" stroke-linecap="round"/>
<circle cx="215.0" cy="152.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="265.2" cy="181.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="265.2" cy="239.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="215.0" cy="268.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="164.8" cy="239.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="164.8" cy="181.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<path d="M282.5 171.0 L265.2 181.0" stroke="#1f6feb" stroke-width="2.4" marker-end="url(#av)"/>
<text x="287.7" y="172.0" text-anchor="start" class="lblb" font-size="12" fill="#15233f">幫浦</text>
<path d="M265.2 239.0 L282.5 249.0" stroke="#1f6feb" stroke-width="2.4" marker-end="url(#av)"/>
<text x="287.7" y="256.0" text-anchor="start" class="lblb" font-size="12" fill="#15233f">管柱</text>
<path d="M147.5 171.0 L164.8 181.0" stroke="#1f6feb" stroke-width="2.4" marker-end="url(#av)"/>
<text x="142.3" y="172.0" text-anchor="end" class="lblb" font-size="12" fill="#15233f">注射針</text>
<path d="M164.8 239.0 L147.5 249.0" stroke="#1f6feb" stroke-width="2.4" marker-end="url(#av)"/>
<text x="142.3" y="256.0" text-anchor="end" class="lblb" font-size="12" fill="#15233f">廢液</text>
<text x="215" y="320" text-anchor="middle" class="lbl" font-size="11.5">幫浦→管柱直通；注射針把樣品灌進定量環</text>
<text x="560" y="106" text-anchor="middle" class="lblb" font-size="14">(b) INJECT 注入</text>
<circle cx="560" cy="210" r="58" fill="#f6f9fd" stroke="#9fb3d1" stroke-width="2"/>
<path d="M560.0 152.0 C 464.0 162.0, 464.0 258.0, 560.0 268.0" fill="none" stroke="#475569" stroke-width="4"/>
<text x="460" y="206" text-anchor="middle" class="lblb" font-size="12" fill="#475569">定量環</text>
<text x="460" y="222" text-anchor="middle" class="lbl" font-size="10.5" fill="#475569">sample loop</text>
<path d="M610.2 181.0 Q 572.6 188.2 560.0 152.0" fill="none" stroke="#1f6feb" stroke-width="5" stroke-linecap="round"/>
<path d="M560.0 268.0 Q 572.6 231.8 610.2 239.0" fill="none" stroke="#1f6feb" stroke-width="5" stroke-linecap="round"/>
<path d="M509.8 181.0 Q 534.9 210.0 509.8 239.0" fill="none" stroke="#aab6cc" stroke-width="3.2" stroke-linecap="round"/>
<circle cx="560.0" cy="152.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="610.2" cy="181.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="610.2" cy="239.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="560.0" cy="268.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="509.8" cy="239.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<circle cx="509.8" cy="181.0" r="6" fill="#fff" stroke="#48597a" stroke-width="2"/>
<path d="M627.5 171.0 L610.2 181.0" stroke="#1f6feb" stroke-width="2.4" marker-end="url(#av)"/>
<text x="632.7" y="172.0" text-anchor="start" class="lblb" font-size="12" fill="#15233f">幫浦</text>
<path d="M610.2 239.0 L627.5 249.0" stroke="#1f6feb" stroke-width="2.4" marker-end="url(#av)"/>
<text x="632.7" y="256.0" text-anchor="start" class="lblb" font-size="12" fill="#15233f">管柱</text>
<path d="M492.5 171.0 L509.8 181.0" stroke="#aab6cc" stroke-width="2.4" marker-end="url(#av)"/>
<text x="487.3" y="172.0" text-anchor="end" class="lblb" font-size="12" fill="#aab6cc">注射針</text>
<path d="M509.8 239.0 L492.5 249.0" stroke="#aab6cc" stroke-width="2.4" marker-end="url(#av)"/>
<text x="487.3" y="256.0" text-anchor="end" class="lblb" font-size="12" fill="#aab6cc">廢液</text>
<text x="560" y="320" text-anchor="middle" class="lbl" font-size="11.5">閥旋轉：幫浦→定量環→管柱，把樣品帶上管柱</text>
</g>
</svg>
"""

# 決策樹：選分離模式 / 偵測器
DTREE_SVG = """
<svg viewBox="0 0 980 360">
 <rect x="380" y="14" width="220" height="56" rx="12" fill="#1f6feb"/>
 <text x="490" y="40" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">你的分析物是什麼？</text>
 <text x="490" y="60" text-anchor="middle" fill="#cfe0f6" font-size="12">選擇 HPLC 分離模式</text>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M420 70 C 200 110,130 120,120 150"/><path d="M470 70 C 400 120,380 120,375 150"/>
  <path d="M510 70 C 590 120,610 120,625 150"/><path d="M560 70 C 800 110,860 120,875 150"/></g>
 <g font-size="14" font-weight="800">
  <rect x="30" y="150" width="190" height="125" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="125" y="178" text-anchor="middle" fill="#15233f">非極性小分子?</text>
  <text x="125" y="206" text-anchor="middle" fill="#d9822b" font-size="16">逆相 RP</text>
  <text x="125" y="232" text-anchor="middle" fill="#48597a" font-size="12">C18 柱·水/甲醇</text>
  <text x="125" y="252" text-anchor="middle" fill="#48597a" font-size="12">最常用(&gt;70%)</text>
  <rect x="280" y="150" width="190" height="125" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="375" y="178" text-anchor="middle" fill="#15233f">帶電的離子?</text>
  <text x="375" y="206" text-anchor="middle" fill="#1f6feb" font-size="16">離子交換 IEC</text>
  <text x="375" y="232" text-anchor="middle" fill="#48597a" font-size="12">緩衝液·導電度偵測</text>
  <text x="375" y="252" text-anchor="middle" fill="#48597a" font-size="12">無機離子·有機酸</text>
  <rect x="530" y="150" width="190" height="125" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="625" y="178" text-anchor="middle" fill="#15233f">大分子分子量?</text>
  <text x="625" y="206" text-anchor="middle" fill="#1f9d6b" font-size="16">尺寸排阻 SEC</text>
  <text x="625" y="232" text-anchor="middle" fill="#48597a" font-size="12">大分子先出·不可梯度</text>
  <text x="625" y="252" text-anchor="middle" fill="#48597a" font-size="12">蛋白·多醣</text>
  <rect x="780" y="150" width="190" height="125" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="875" y="178" text-anchor="middle" fill="#15233f">專一純化?</text>
  <text x="875" y="206" text-anchor="middle" fill="#15233f" font-size="16">親和 Affinity</text>
  <text x="875" y="232" text-anchor="middle" fill="#48597a" font-size="12">固定化配體·可逆結合</text>
  <text x="875" y="252" text-anchor="middle" fill="#48597a" font-size="12">醣蛋白·葉酸</text>
 </g>
 <text x="490" y="320" text-anchor="middle" fill="#8493ad" font-size="12.5">偵測器同理：有發色團→UV-Vis；微量螢光物→螢光；無 UV 吸收(醣/脂)→RI 或 ELSD</text>
</svg>"""

# ---------------- 引起動機 ----------------
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 13",
    "高效液相<span style='color:var(--accent-2)'>層析</span>", "High-Performance Liquid Chromatography",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>幫浦 · 注射器 · 管柱 · 偵測器 · 分離模式 · 檢量線定量",
    ["HPLC","逆相 RP","UV-Vis","梯度沖提","檢量線","UHPLC"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">一杯咖啡裡有幾百種成分，<span class="hi">怎麼把它們分開、量出來？</span></div>
  <p class="subtitle" style="max-width:800px;margin:22px auto 0">把樣品溶進液體「移動相」，用高壓推過裝滿固定相的管柱。<br>
  各成分與固定相的<strong>作用力不同</strong>，前後分批流出——這就是<strong>液相層析</strong>。</p>
  <div style="margin-top:24px"><span class="pill">糖類</span><span class="pill">維生素</span>
  <span class="pill">胺基酸</span><span class="pill">色素</span><span class="pill">農藥殘留</span><span class="pill">黴菌毒素</span></div></div>""")

add(MOT, dc.kt("13.1 為什麼用 HPLC", "比傳統管柱層析強在哪") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("📦","固定相多元","預裝管柱、各種固定相可選，分離模式比傳統更多") +
    dc.card("🔬","解析度高","小顆粒填料 + 高壓 → 波峰更窄、分得更開","a") +
    dc.card("⚡","速度快","多數分析 30 分鐘內完成，高通量","g") +
    dc.card("📈","靈敏多樣","多種偵測器可選、易回收、可接質譜 MS","b") + '</div>')

add(MOT, dc.kt("13.1 HPLC 是什麼", "高壓推一管<span class='hi'>分配差異</span>") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li>1960 年代發展，原指<strong>高壓</strong>液相層析</li>" +
    "<li>1970 末改稱<strong>高效能</strong>，強調解析度與通量</li>" +
    "<li>凡能<strong>溶於移動相</strong>的化合物都可分析</li>" +
    "<li>分析為主，亦可<strong>半製備</strong>(收集純化分離出的成分)</li>" +
    '</ul></div><div class="note"><strong>核心：分離 = 各成分在固定相/移動相間「分配」程度不同。</strong><br>' +
    "作用力強者被拉住、晚出；作用力弱者先流出 → 在時間軸上分開。</div></div>")

add(MOT, dc.chart_inner("apps", "HPLC 在食品的<span class='hi'>應用</span>有多廣",
    "資料整理自 Table 13.1：各類食品成分常以 HPLC 分析（示意筆數）。",
    kicker="13.3 食品應用"), ' data-chart="apps"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">核心命題</div>
  <div class="hook" style="font-size:clamp(1.7rem,4vw,3rem)">先<span class="hi">分離</span>，再<span class="hi">偵測</span>，最後<span class="hi">定量</span></div>
  <p class="lead" style="max-width:840px;margin:20px auto 0">一套 HPLC 的工作邏輯：幫浦推移動相 → 注入樣品 → 管柱把成分分開 → 偵測器轉成訊號 → 用<strong>檢量線</strong>由波峰面積算濃度。</p>
  <div class="eq" style="max-width:560px;margin:24px auto 0">波峰面積 ∝ 濃度<br>
  <span style="font-size:.78em;color:var(--ink-2)">用標準品建檢量線：面積 → 濃度</span></div></div>""")

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","偵測器「測什麼」分類", 7,
    "每種偵測器靠什麼性質出訊號？把 7 個偵測器分到三類。"), ' data-game="g1"')

# ---------------- 維持注意 ----------------
add(ATT, dc.kt("13.2 系統元件", "HPLC 的五大元件") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("🫧","幫浦 Pump","精準推送移動相，0.2–2 mL/min","b") +
    dc.card("💉","注射器 Injector","把樣品送入流動的移動相","a") +
    dc.card("🧱","管柱 Column","裝固定相，分離的主舞台","g") +
    dc.card("📡","偵測器 Detector","濃度變化 → 電訊號","b") + '</div>' +
    '<div class="note" style="margin-top:16px">第五個是<strong>資料站</strong>：顯示層析圖、積分波峰、自動跑樣與報告。</div>')

add(ATT, dc.kt("13.2 儀器流程", "訊號怎麼一路傳下去") +
    '<div class="svgwrap" style="margin-top:8px">' + HPLC_FLOW_SVG + '</div>' +
    '<div class="note" style="margin-top:14px">記住順序：<strong>溶劑槽 → 幫浦 → 注射器 → 管柱 → 偵測器 → 資料站</strong>。管柱與偵測器常可恆溫。</div>')

add(ATT, dc.kt("13.2.1 幫浦", "Pump：穩定才準") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>流速 <strong>0.2–2 mL/min</strong>，準確度 ±1%、精密度 &lt;0.1% RSD</li>" +
    "<li>九成以上為<strong>往復式活塞幫浦</strong>(雙活塞最佳)</li>" +
    "<li>會產生脈動 → 需<strong>脈衝阻尼器</strong>(RI 偵測對脈動敏感)</li>" +
    "<li>材質 316 不鏽鋼；移動相需<strong>過濾(0.22/0.45µm)、脫氣</strong></li>" +
    '</ul></div><div class="note">流速穩定 → <strong>滯留時間</strong>與<strong>波峰面積</strong>才能重現。<br>' +
    "梯度沖提靠低死體積幫浦快速換溶劑。</div></div>")

add(ATT, dc.kt("13.2.2 注射器", "Injector：載入 vs 注入") +
    '<div class="svgwrap" style="margin-top:8px">' + INJECTOR_SVG + '</div>' +
    '<div class="note" style="margin-top:14px">閥式注射器用<strong>定量環</strong>：LOAD 灌樣、INJECT 旋轉讓環接入流路。' +
    "典型注入 10–100 µL；接<strong>自動進樣器</strong>可大量、可冷藏、提升精密度。</div>")

add(ATT, dc.kt("13.2.3 管柱", "Column：分離的舞台") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧱","硬體","不鏽鋼/玻璃/PEEK；分析柱常 10–25 cm × 4.6 mm","b") +
    dc.card("🛡️","保護柱","裝在分析柱前，擋強吸附物；每 50–200 針更換","a") +
    dc.card("⚪","填料","多孔矽膠或聚合物樹脂；小顆粒→高效率但高背壓","g") +
    dc.card("🚀","UHPLC","≤2µm 顆粒 + 超高壓(15000–20000 psi)，更快更省溶劑","b") + '</div>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","元件即時測驗", 4), ' data-game="g2"')

add(ATT, dc.kt("13.2.4 偵測器家族", "四種常見偵測器") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🔆","UV-Vis 吸收","測發色團；固定/可變波長/二極體陣列(200–700nm)。最常用","b") +
    dc.card("✨","螢光 Fluorescence","選擇性高、靈敏度可達 UV 的 1000 倍；適微量","a") +
    dc.card("💧","折射率 RI","近乎通用，但靈敏度低、<strong>不能用梯度</strong>；測醣/脂","g") +
    dc.card("⚡","電化學 EC","氧化還原/導電度；高選擇高靈敏；測兒茶酚胺、醣","b") + '</div>')

add(ATT, dc.chart_inner("sens", "偵測器<span class='hi'>靈敏度</span>差很多",
    "示意相對偵測極限（數字越大越靈敏，對數示意）。整合自 13.2.4。",
    kicker="13.2.4 靈敏度比較", height="52vh"), ' data-chart="sens"')

add(ATT, dc.kt("沖提方式", "等度 vs 梯度沖提") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("➖","等度 Isocratic","移動相組成<strong>全程不變</strong>；簡單、基線穩；適成分性質相近","b") +
    dc.card("📈","梯度 Gradient","運行中<strong>逐步改變</strong>移動相組成；分得開、波峰更銳","a") +
    '</div><div class="note" style="margin-top:18px">梯度幾乎用於所有模式，<strong>唯獨尺寸排阻(SEC)不用</strong>；' +
    "<strong>RI 偵測也不能搭梯度</strong>(組成一變、基線就漂)。</div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","元件「功能」配對", 6,
    "把每個元件配到它負責的工作。分到三大功能。"), ' data-game="g3"')

add(ATT, dc.kt("13.3 分離模式", "四種主要分離模式") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🟠","逆相 RP","非極性固定相(C18) + 極性移動相；<strong>最常用(&gt;70%)</strong>","a") +
    dc.card("🔵","正相 NP","極性固定相 + 非極性移動相(己烷)；分極性化合物","b") +
    dc.card("🟢","離子交換 IEC","帶電樹脂分離離子；緩衝液、導電度偵測","g") +
    dc.card("🟣","尺寸排阻 SEC","純依分子大小，<strong>大分子先出</strong>；測分子量","b") + '</div>')

add(ATT, dc.kt("最常用的兩兄弟", "逆相 RP vs 正相 NP") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🟠","逆相 Reversed-Phase","固定相<strong>非極性</strong>(C18)、移動相<strong>極性</strong>(水/甲醇/乙腈)。依疏水性遞增流出。<strong>水多→滯留久(k′大)</strong>","a") +
    dc.card("🔵","正相 Normal-Phase","固定相<strong>極性</strong>(矽膠/氰基/胺基)、移動相<strong>非極性</strong>(己烷)。分脂溶性維生素、類胡蘿蔔素","b") +
    '</div><div class="note" style="margin-top:18px">口訣：<strong>「逆相＝固定相不愛水」</strong>——非極性柱配水性溶劑，剛好和正相相反。</div>')

add(ATT, dc.kt("其餘模式", "離子交換 · 尺寸排阻 · 親和") +
    '<div class="grid3" style="margin-top:22px">' +
    dc.card("🟢","離子交換 IEC","帶電官能基樹脂；改變離子強度/pH 控滯留；測無機離子、有機酸、糖","g") +
    dc.card("🟣","尺寸排阻 SEC","依分子大小篩分，<strong>大分子先出</strong>；測蛋白/多醣分子量；不用梯度","b") +
    dc.card("🎯","親和 Affinity","固定化配體與目標<strong>可逆專一結合</strong>；純化醣蛋白、葉酸","a") + '</div>')

add(ATT, dc.chart_inner("chrom", "讀懂一張<span class='hi'>層析圖</span>",
    "訊號 vs 時間：先出的滯留時間短，波峰面積反映含量(示意)。",
    kicker="13.2.5 層析圖", height="54vh"), ' data-chart="chrom"')

add(ATT, dc.kt("關鍵參數", "滯留係數 k′ 看什麼") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">k′ = ' +
    '<span class="frac"><b>t<tspan style="font-size:.7em">R</tspan> − t<tspan style="font-size:.7em">0</tspan></b><span>t<sub>0</sub></span></span></div>' +
    '<div><ul class="clean"><li>t<sub>R</sub>＝滯留時間、t<sub>0</sub>＝死時間(不滯留物)</li>' +
    "<li>k′ 越大 → 被固定相拉得越久</li>" +
    "<li>RP：移動相<strong>水越多 k′ 越大</strong>；有機溶劑越多 k′ 越小</li>" +
    "<li>弱溶劑→大 k′；強溶劑→小 k′</li></ul></div></div>" +
    '<div class="note" style="margin-top:14px">調 k′ 是調分離的第一招——想多留住分析物，就降低溶劑強度。</div>')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","HPLC 分析流程排序", 7,
    "用 ▲▼ 把一次 HPLC 定量分析的 7 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選模式/偵測器", 5), ' data-game="g5"')

# ---------------- 喚起行動 ----------------
add(ACT, dc.cmp_inner("一張表選偵測器（點欄位排序）",
    [{"k":"d","t":"s","label":"偵測器"},{"k":"meas","t":"s","label":"偵測依據"},
     {"k":"sens","t":"n","label":"靈敏度","star":True},{"k":"grad","t":"s","label":"可梯度?"},
     {"k":"app","t":"s","label":"典型應用"}],
    "靈敏度：★ 越多越靈敏。整合自 13.2.4。", kicker="13.2.4 偵測器比較"), ' data-game="cmp"')

add(ACT, dc.kt("方法選擇", "跟著決策樹走") +
    '<div class="svgwrap" style="margin-top:8px">' + DTREE_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:12px">下一頁實戰：用檢量線由波峰面積算濃度 →</p>')

add(ACT, dc.kt("定性與定量", "標準品＋檢量線") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🏷️","定性","用<strong>滯留時間</strong>對照標準品；二極體陣列可比對光譜","b") +
    dc.card("📐","定量","<strong>波峰面積</strong>對標準品濃度建檢量線(A=mC+b)","a") +
    '</div><div class="note" style="margin-top:18px">資料站自動積分波峰面積、套檢量線、扣內標、出報告。' +
    "面積與濃度成正比，這是 HPLC 定量的根基。</div>")

add(ACT, dc.kt("13.3 計算", "用檢量線：面積 → 濃度") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">C = ' +
    '<span class="frac"><b>A − b</b><span>m</span></span></div>' +
    '<div><ul class="clean"><li>檢量線 <strong>A = m·C + b</strong>(面積對濃度)</li>' +
    "<li>m＝斜率、b＝截距，由標準品迴歸得到</li>" +
    "<li>測得樣品波峰面積 A → 反算濃度 C</li>" +
    "<li>必要時再乘<strong>稀釋倍數</strong>回推原樣品</li></ul></div></div>" +
    '<div class="note" style="margin-top:14px">下一題：已知檢量線與樣品面積，求咖啡因濃度。</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關",
    "咖啡因 UV 檢量線 <strong>A = 24.0·C + 5.0</strong>(C 單位 µg/mL，A 為波峰面積)。"
    "某飲料測得波峰面積 <strong>A = 605</strong>。求咖啡因濃度 <strong>C</strong>。", unit="µg/mL"),
    ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li><strong>HPLC＝高壓推移動相</strong>過管柱，靠分配差異分離成分</li>" +
    "<li>五大元件：<strong>幫浦→注射器→管柱→偵測器→資料站</strong></li>" +
    "<li>模式：<strong>逆相(最常用)</strong>、正相、離子交換、尺寸排阻、親和</li></ul>" +
    '<ul class="clean"><li>偵測器：UV-Vis(最常用)、螢光(最靈敏)、RI(通用但不可梯度)</li>' +
    "<li>定量靠<strong>檢量線</strong>：波峰面積 → 濃度(梯度除 SEC/RI 外皆可用)</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說出 HPLC 五大元件與正確流程順序",
     "解釋為什麼分離靠固定相/移動相的分配差異",
     "區分逆相與正相的固定相、移動相與適用對象",
     "為樣品選對分離模式(RP/IEC/SEC/親和)",
     "依分析物性質選對偵測器(UV/螢光/RI)",
     "說明等度與梯度的差別，及 SEC/RI 不可梯度",
     "用檢量線由波峰面積算出濃度"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把 HPLC<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions（保護柱、偵測器原理、k′、IEC/SEC 範例）<br>"
    "🔜 銜接章節：<strong>氣相層析 (Ch12/14)</strong>、<strong>質譜 (Ch11)</strong>、<strong>胺基酸/蛋白分離 (Ch24)</strong><br>"
    "🧪 思考：你的分析物極性如何？帶電嗎？有 UV 吸收嗎？該選哪種模式與偵測器？",
    ["逆相 RP","UV-Vis","螢光","梯度","檢量線","UHPLC-MS"]), ' data-cover="1"')

# ---------------- CFG ----------------
CFG = {
  "charts": {
    "apps": {"type":"bar","yTitle":"食品應用筆數(示意)",
      "labels":["逆相 RP","離子交換","正相 NP","尺寸排阻","親和","疏水交互","HILIC"],
      "datasets":[{"label":"應用情境數(示意)","data":[9,5,3,3,2,2,2],"color":"#1f6feb"}]},
    "sens": {"type":"bar","yTitle":"相對靈敏度(示意,越大越靈敏)",
      "labels":["螢光","電化學","UV-Vis","ELSD光散射","折射率 RI"],
      "datasets":[{"label":"相對偵測能力(示意)","data":[1000,500,100,30,10],"color":"#d9822b"}]},
    "chrom": {"type":"line","yTitle":"偵測訊號 (mAU)","zero":True,
      "labels":["0","1","2","3","4","5","6","7","8","9","10","11","12"],
      "datasets":[{"label":"層析圖(訊號 vs 時間, 分鐘)",
        "data":[2,3,30,8,4,5,55,18,4,3,40,9,3],"color":"#1f6feb"}]}
  },
  "bucket": {
    "g1": {"cats":["測光吸收/發光","測本體性質(整批移動相)","測電化學"],
      "items":[{"t":"UV-Vis 吸收","c":"測光吸收/發光"},{"t":"螢光 Fluorescence","c":"測光吸收/發光"},
        {"t":"二極體陣列 DAD","c":"測光吸收/發光"},
        {"t":"折射率 RI","c":"測本體性質(整批移動相)"},{"t":"蒸發光散射 ELSD","c":"測本體性質(整批移動相)"},
        {"t":"安培電流 (氧化還原)","c":"測電化學"},{"t":"導電度 Conductivity","c":"測電化學"}],
      "ok":"🎉 全對！UV/螢光/DAD 看光、RI/ELSD 測整批移動相性質、安培/導電度靠電化學。",
      "tip":"提示：RI 與 ELSD 測的是「整批移動相」的本體性質，不挑特定發色團。"},
    "g3": {"cats":["推送移動相","送入樣品","分離與偵測"],
      "items":[{"t":"幫浦 Pump","c":"推送移動相"},{"t":"脈衝阻尼器","c":"推送移動相"},
        {"t":"注射閥/定量環","c":"送入樣品"},{"t":"自動進樣器","c":"送入樣品"},
        {"t":"管柱(固定相)","c":"分離與偵測"},{"t":"UV 偵測器","c":"分離與偵測"}],
      "ok":"🎉 正確！幫浦/阻尼器推送、注射閥/自動進樣送樣、管柱分離、偵測器出訊號。",
      "tip":"提示：阻尼器是穩定幫浦脈動的；定量環屬於注射器。"}
  },
  "mcq": {
    "g2":[
      {"q":"HPLC 系統元件正確的流路順序是？","o":["注射器→幫浦→管柱→偵測器","幫浦→注射器→管柱→偵測器","管柱→幫浦→注射器→偵測器","偵測器→管柱→幫浦→注射器"],"a":1,
       "e":"幫浦推移動相、注射器送樣、管柱分離、偵測器出訊號，最後到資料站。"},
      {"q":"保護柱(guard column)的主要功能是？","o":["增加流速","保護分析柱免受強吸附物污染","提高溫度","產生梯度"],"a":1,
       "e":"保護柱裝在分析柱前、用相同填料，擋住雜質、定期更換以延長昂貴分析柱壽命。"},
      {"q":"關於 HPLC 幫浦，何者正確？","o":["流速越亂越好","流速穩定才能重現滯留時間與面積","幫浦不需過濾溶劑","活塞幫浦無脈動"],"a":1,
       "e":"流速準確穩定(±1%)是滯留時間與波峰面積重現的關鍵；往復活塞會脈動需阻尼器。"},
      {"q":"UHPLC 相較傳統 HPLC 的特點是？","o":["更大顆粒、更低壓","≤2µm 顆粒、更高壓、更快更省溶劑","只能用 RI 偵測","不能接質譜"],"a":1,
       "e":"UHPLC 用 ≤2µm 填料與超高壓，分離更快、更省溶劑，很適合接 MS。"}
    ],
    "g5":[
      {"q":"要分析非極性的酚類小分子，最常用的模式？","o":["正相 NP","逆相 RP","尺寸排阻 SEC","親和"],"a":1,
       "e":"逆相(C18)是最常用模式(>70%)，水/甲醇移動相，依疏水性分離。"},
      {"q":"要測沒有 UV 吸收的糖類(高濃度)，較適合的偵測器？","o":["UV-Vis","折射率 RI","螢光","二極體陣列"],"a":1,
       "e":"糖無發色團；RI 近乎通用，適合無 UV 吸收、濃度較高的分析物。"},
      {"q":"要測極微量、可生成螢光衍生物的維生素，最靈敏的偵測器？","o":["RI","UV 固定波長","螢光","導電度"],"a":2,
       "e":"螢光選擇性高、靈敏度可達 UV 的 1000 倍，最適微量分析。"},
      {"q":"要分離無機陰離子並用導電度偵測，最適合的模式？","o":["逆相","離子交換 IEC","尺寸排阻","正相"],"a":1,
       "e":"離子交換以帶電樹脂分離離子，常配導電度偵測。"},
      {"q":"用 RI 偵測器時，下列何者不能做？","o":["等度沖提","梯度沖提","測糖類","測脂質"],"a":1,
       "e":"移動相組成一改變 RI 就變、基線會漂，所以 RI 不能搭配梯度沖提。"}
    ]
  },
  "sort": {
    "g4":{"steps":["樣品前處理：萃取、過濾(0.22µm)","選定管柱與移動相、平衡系統",
       "注射器把樣品注入移動相","樣品隨移動相通過管柱被分離","偵測器把各波峰轉成訊號",
       "資料站積分波峰面積","套檢量線由面積算出濃度"],
       "shuffle":[3,0,6,1,4,2,5],
       "ok":"🎉 順序正確！前處理→平衡→注入→分離→偵測→積分→定量。",
       "tip":"提示：一定先做樣品前處理與系統平衡，最後才用檢量線換算濃度。"}
  },
  "calc": {
    "g6":{"answer":25.0,"tol":0.5,
      "ok":"🎉 正確！C=(A−b)/m=(605−5.0)/24.0 = 600/24 = <b>25.0 µg/mL</b>。",
      "bad":"再算算：檢量線 A=24.0·C+5.0，移項得 C=(605−5.0)/24.0。",
      "hint":"提示：先 605−5.0 = 600，再 ÷ 24.0 = 25.0 µg/mL。"}
  },
  "cmp": {
    "cols":[{"k":"d"},{"k":"meas"},{"k":"sens"},{"k":"grad"},{"k":"app"}],
    "rows":[
      {"d":"UV-Vis","meas":"發色團光吸收","sens":3,"grad":"可","app":"酚類·維生素·農藥(最常用)"},
      {"d":"螢光","meas":"放射螢光","sens":5,"grad":"可","app":"維生素·黴菌毒素(微量)"},
      {"d":"折射率 RI","meas":"移動相折射率","sens":1,"grad":"不可","app":"糖類·脂質(高濃度)"},
      {"d":"電化學","meas":"氧化還原/導電","sens":4,"grad":"可","app":"兒茶酚胺·醣·離子"},
      {"d":"ELSD 光散射","meas":"非揮發顆粒散射","sens":2,"grad":"可","app":"脂質·聚合物(通用)"},
      {"d":"質譜 MS","meas":"質荷比 m/z","sens":5,"grad":"可","app":"定性定量·污染物"}
    ]
  }
}

dc.build_html(
  {"title":"高效液相層析 HPLC · Nielsen Ch13","brand":"HPLC · CH13"},
  S, CFG, OUT)
