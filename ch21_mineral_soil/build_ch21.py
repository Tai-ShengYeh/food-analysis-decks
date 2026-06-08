# -*- coding: utf-8 -*-
"""Nielsen Ch21 Traditional Methods for Mineral Analysis — SOIL HTML deck.
Uses ../soil_deck_common.py.  Run: python build_ch21.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
# 滴定示意：滴定管 + 錐形瓶（EDTA 變色 pink→blue）
TITRATE_SVG = """
<svg viewBox="0 0 320 380">
 <defs><linearGradient id="gt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eaf2ff"/><stop offset="1" stop-color="#cfe0f6"/></linearGradient></defs>
 <rect x="150" y="20" width="20" height="150" rx="4" fill="#fff" stroke="#1f6feb" stroke-width="2.4"/>
 <rect x="150" y="60" width="20" height="110" rx="0" fill="url(#gt)"/>
 <path d="M150 170 h20 l-7 20 h-6 z" fill="#1f6feb"/>
 <text x="232" y="64" class="lbl">滴定管</text>
 <text x="232" y="82" class="lbl">標準 EDTA / AgNO₃</text>
 <path d="M160 198 l-2 14 m2 -6 l-2 14" stroke="#1f6feb" stroke-width="2" fill="none"/>
 <path d="M110 250 h100 l-22 90 a30 30 0 0 1 -56 0 z" fill="url(#gt)" stroke="#1f6feb" stroke-width="2.4"/>
 <path d="M126 318 a30 30 0 0 0 68 0 z" fill="#fbeede"/>
 <text x="160" y="312" text-anchor="middle" class="lblb">樣品 + 指示劑</text>
 <text x="160" y="372" text-anchor="middle" class="lbl">終點：顏色改變</text>
</svg>"""

# 乾式灰化 → 溶解 → 分析（前處理流程示意）
ASH_SVG = """
<svg viewBox="0 0 560 230">
 <g font-size="13">
  <rect x="14" y="80" width="116" height="64" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="72" y="106" text-anchor="middle" class="lblb">高溫灰化</text>
  <text x="72" y="126" text-anchor="middle" class="lbl">550°C 燒掉有機質</text>
  <rect x="166" y="80" width="116" height="64" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="224" y="106" text-anchor="middle" class="lblb">強酸溶解</text>
  <text x="224" y="126" text-anchor="middle" class="lbl">灰分 → 礦物離子</text>
  <rect x="318" y="80" width="116" height="64" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="376" y="106" text-anchor="middle" class="lblb">調整/遮蔽</text>
  <text x="376" y="126" text-anchor="middle" class="lbl">控 pH·除干擾</text>
  <rect x="470" y="80" width="78" height="64" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="509" y="106" text-anchor="middle" class="lblb">測定</text>
  <text x="509" y="126" text-anchor="middle" class="lbl">滴定/比色</text>
  <g stroke="#8493ad" stroke-width="2.5" fill="none" marker-end="url(#arA)">
   <path d="M130 112 h34"/><path d="M282 112 h34"/><path d="M434 112 h34"/></g>
  <defs><marker id="arA" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#8493ad"/></marker></defs>
  <text x="280" y="40" text-anchor="middle" class="lblb" font-size="15">前處理：灰化 → 溶解 → 測定</text>
 </g>
</svg>"""

# AAS 火焰原子吸收示意
AAS_SVG = """
<svg viewBox="0 0 560 230">
 <g font-size="13">
  <rect x="14" y="86" width="86" height="54" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="57" y="108" text-anchor="middle" class="lblb">空心陰極燈</text>
  <text x="57" y="126" text-anchor="middle" class="lbl">HCL 特定波長</text>
  <path d="M150 110 q24 -22 48 0 q24 22 48 0" fill="none" stroke="#d9822b" stroke-width="2.6"/>
  <text x="198" y="86" text-anchor="middle" class="lbl">火焰：原子化</text>
  <rect x="150" y="118" width="96" height="22" rx="6" fill="#fbeede" stroke="#d9822b" stroke-width="1.6"/>
  <text x="198" y="134" text-anchor="middle" class="lbl">樣品霧化</text>
  <rect x="300" y="86" width="86" height="54" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="343" y="108" text-anchor="middle" class="lblb">單光器</text>
  <text x="343" y="126" text-anchor="middle" class="lbl">選波長</text>
  <rect x="436" y="86" width="110" height="54" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="491" y="108" text-anchor="middle" class="lblb">偵測器</text>
  <text x="491" y="126" text-anchor="middle" class="lbl">吸收 ∝ 濃度</text>
  <g stroke="#8493ad" stroke-width="2.5" fill="none" marker-end="url(#arB)">
   <path d="M100 113 h44"/><path d="M246 113 h48"/><path d="M386 113 h44"/></g>
  <defs><marker id="arB" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#8493ad"/></marker></defs>
  <text x="280" y="40" text-anchor="middle" class="lblb" font-size="15">原子吸收光譜 AAS（火焰法）</text>
 </g>
</svg>"""

# 決策樹：選礦物質分析法
DTREE_SVG = """
<svg viewBox="0 0 980 360">
 <rect x="380" y="14" width="220" height="56" rx="12" fill="#1f6feb"/>
 <text x="490" y="40" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">你要測什麼？</text>
 <text x="490" y="60" text-anchor="middle" fill="#cfe0f6" font-size="12">選擇礦物質分析方法</text>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M420 70 C 200 110,130 120,120 150"/><path d="M470 70 C 400 120,380 120,375 150"/>
  <path d="M510 70 C 590 120,610 120,625 150"/><path d="M560 70 C 800 110,860 120,875 150"/></g>
 <g font-size="14" font-weight="800">
  <rect x="30" y="150" width="190" height="124" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="125" y="178" text-anchor="middle" fill="#15233f">水的硬度?</text>
  <text x="125" y="206" text-anchor="middle" fill="#d9822b" font-size="16">EDTA 滴定</text>
  <text x="125" y="232" text-anchor="middle" fill="#48597a" font-size="12">測 Ca+Mg·pH 10</text>
  <text x="125" y="252" text-anchor="middle" fill="#48597a" font-size="12">以 CaCO₃ mg/L 表示</text>
  <rect x="280" y="150" width="190" height="124" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="375" y="178" text-anchor="middle" fill="#15233f">鹽/氯化物?</text>
  <text x="375" y="206" text-anchor="middle" fill="#1f6feb" font-size="16">Mohr / Volhard</text>
  <text x="375" y="232" text-anchor="middle" fill="#48597a" font-size="12">AgNO₃ 沉澱滴定</text>
  <text x="375" y="252" text-anchor="middle" fill="#48597a" font-size="12">高氯食品·乳酪</text>
  <rect x="530" y="150" width="190" height="124" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="625" y="178" text-anchor="middle" fill="#15233f">磷/微量元素?</text>
  <text x="625" y="206" text-anchor="middle" fill="#1f9d6b" font-size="16">比色法</text>
  <text x="625" y="232" text-anchor="middle" fill="#48597a" font-size="12">磷-鉬藍·專一</text>
  <text x="625" y="252" text-anchor="middle" fill="#48597a" font-size="12">需標準曲線</text>
  <rect x="780" y="150" width="190" height="124" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="875" y="178" text-anchor="middle" fill="#15233f">多元素·痕量?</text>
  <text x="875" y="206" text-anchor="middle" fill="#15233f" font-size="16">AAS / ICP</text>
  <text x="875" y="232" text-anchor="middle" fill="#48597a" font-size="12">ppb 級·靈敏</text>
  <text x="875" y="252" text-anchor="middle" fill="#48597a" font-size="12">儀器貴·需灰化</text>
 </g>
</svg>"""

# ---------------- 引起動機 ----------------
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 21",
    "礦物質<span style='color:var(--accent-2)'>分析</span>", "Mineral Analysis",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>EDTA 滴定 · Mohr/Volhard · 比色法 · 離子選擇電極 · AAS/ICP",
    ["EDTA","Mohr/Volhard","磷-鉬藍","ISE","AAS/ICP"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">一瓶礦泉水裡的鈣，<span class="hi">是怎麼量出來的？</span></div>
  <p class="subtitle" style="max-width:800px;margin:22px auto 0">礦物質是<strong>無機元素</strong>，不像蛋白脂肪可以「燒掉測差」。<br>
  關鍵在於——先把礦物質從食物基質中<strong>分離</strong>，再用合適方法<strong>測定</strong>。</p>
  <div style="margin-top:24px"><span class="pill">營養標示</span><span class="pill">水質硬度</span>
  <span class="pill">加工功能</span><span class="pill">重金屬安全</span><span class="pill">摻假</span></div></div>""")

add(MOT, dc.kt("21.1.1 飲食中的重要性", "為什麼要分析礦物質") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("🏷️","營養標示","NLEA 強制標示 Na、Fe、Ca，新規再加 K") +
    dc.card("🦴","健康角色","鈣防骨鬆、鐵防貧血、鈉控血壓","a") +
    dc.card("🏭","加工功能","鹽調味/防腐、磷增保水、鈣促膠凝","g") +
    dc.card("☠️","毒性安全","重金屬(鉛汞鎘砷)需低於限量","b") + '</div>')

add(MOT, dc.kt("21.1 分離 + 測定", "礦物質分析的<span class='hi'>骨架</span>") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li><strong>巨量礦物</strong>：Ca、P、Na、K、Mg、Cl、S（每日 >100 mg）</li>" +
    "<li><strong>微量礦物</strong>：Fe、I、Zn、Cu、Mn… (mg/µg 級)</li>" +
    "<li>分析 = <strong>分離</strong>(專一/非專一) + <strong>測定</strong></li>" +
    "<li>體積、吸光值等都是<span class='em'>替代量(surrogate)</span>，再換算成質量</li>" +
    '</ul></div><div class="note"><strong>關鍵：最終目標是礦物質的「質量」。</strong><br>' +
    "滴定體積、吸光度需透過<strong>化學計量或標準曲線</strong>換算回礦物質量。</div></div>")

add(MOT, dc.chart_inner("ca", "食物裡的<span class='hi'>鈣</span>含量", "資料：USDA SR-28，Ca（mg / 100 g 濕基）。",
    kicker="21.1 食物中的含量"), ' data-chart="ca"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">核心命題</div>
  <div class="hook" style="font-size:clamp(1.7rem,4vw,3rem)">先<span class="hi">分離</span>，再<span class="hi">測定</span></div>
  <p class="lead" style="max-width:840px;margin:20px auto 0">傳統法多需先<strong>灰化</strong>把礦物質從有機基質游離出來，水樣則常可<strong>直接測</strong>。</p>
  <div class="eq" style="max-width:560px;margin:24px auto 0">替代量(體積/吸光) → 礦物質量<br>
  <span style="font-size:.8em;color:var(--ink-2)">經化學計量或標準曲線換算</span></div></div>""")

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","方法依「原理」分類", 7,
    "每個方法的偵測原理是什麼？把 7 個方法分到三類。"), ' data-game="g1"')

# ---------------- 維持注意 ----------------
add(ATT, dc.kt("方法全覽", "傳統法 + 儀器法") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("💧","滴定法","EDTA 錯合(測鈣/硬度)、Mohr/Volhard 沉澱(測氯)","b") +
    dc.card("🎨","比色法","顯色劑 + Beer 定律(如磷-鉬藍)","a") +
    dc.card("🔌","電極法","離子選擇電極 ISE（Nernst 方程）","g") +
    dc.card("📡","光譜儀器","AAS、ICP-OES（多元素、痕量）","b") + '</div>')

add(ATT, dc.kt("21.2.2 樣品前處理", "灰化：游離礦物質") +
    '<div class="svgwrap" style="margin-top:6px">' + ASH_SVG + '</div>' +
    '<div class="note" style="margin-top:14px">傳統法多需把礦物質從<strong>有機基質</strong>游離 → 多先<strong>灰化</strong>(Ch16)。' +
    "最大隱憂是<strong>污染</strong>：用非金屬器具、酸洗玻璃、純水，必要時跑<strong>試劑空白</strong>。水樣常可直接測。</div>")

add(ATT, dc.kt("21.3.1 EDTA 錯合滴定", "EDTA：測鈣與硬度") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + TITRATE_SVG + '</div><div><ul class="clean">' +
    "<li>EDTA 與金屬離子形成 <strong>1:1</strong> 穩定錯合物</li>" +
    "<li>須在 <span class='em'>pH 10</span>(氨緩衝)；指示劑 Calmagite/EBT</li>" +
    "<li>終點：<strong>粉紅 → 藍</strong>（金屬被 EDTA 奪走）</li>" +
    "<li>mol EDTA = mol (Ca + Mg) → 算硬度</li>" +
    '</ul><div class="note" style="margin-top:14px">主要應用：水的<strong>總硬度</strong>(Ca+Mg)，以 CaCO₃ mg/L 表示。</div></div></div>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","EDTA 與前處理即時測驗", 4), ' data-game="g2"')

add(ATT, dc.kt("21.3.2 沉澱滴定", "Mohr vs Volhard：測氯化物") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("➡️","Mohr 正滴定","AgNO₃ 直接滴 Cl⁻；K₂CrO₄ 為指示劑。過量 Ag⁺ 與鉻酸根生成<strong>磚紅色 Ag₂CrO₄</strong>為終點","b") +
    dc.card("⬅️","Volhard 反滴定","先加<strong>過量</strong>AgNO₃，再用 KSCN 回滴；Fe³⁺ 指示劑遇過量 SCN⁻ 變<strong>紅色</strong>","a") +
    '</div><div class="note" style="margin-top:18px">兩法都用 Ag⁺ 沉澱 Cl⁻；測得氯後 ×1.648 換算成<strong>食鹽 (NaCl)</strong>。配藥須用<strong>煮沸水</strong>除碳酸鹽干擾。</div>')

add(ATT, dc.kt("沉澱滴定的化學", "Mohr 的兩步反應") +
    '<div class="grid2" style="margin-top:8px"><div class="eq" style="font-size:1.05rem">' +
    "Ag⁺ + Cl⁻ → AgCl↓<br><span style='font-size:.8em;color:var(--ink-2)'>白色混濁（先反應）</span></div>" +
    '<div class="eq" style="font-size:1.05rem">2Ag⁺ + CrO₄²⁻ → Ag₂CrO₄↓<br>' +
    "<span style='font-size:.8em;color:var(--ink-2)'>磚紅（Cl⁻ 用盡後才出現＝終點）</span></div></div>" +
    '<div class="note" style="margin-top:16px">關鍵：AgCl 的溶解度比 Ag₂CrO₄ 低 → Cl⁻<strong>先</strong>被沉澱完，多餘 Ag⁺ 才去找鉻酸根顯色。</div>')

add(ATT, dc.game_sort_inner("g4","小遊戲 ③","灰化→鈣分析流程排序", 7,
    "用 ▲▼ 把「灰化後以 EDTA 測鈣」的 7 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("21.3.3 比色法", "顏色 = 礦物質的訊號") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🎨","原理","顯色劑(chromogen)與礦物反應生成<strong>有色錯合物</strong>，依 Beer 定律 A=εbc 定量","b") +
    dc.card("🔵","磷-鉬藍","磷 + 鉬酸銨 → 磷鉬酸，抗壞血酸還原成<strong>藍色</strong>，讀 700/880 nm","a") +
    '</div><div class="note" style="margin-top:18px">很<strong>專一</strong>、其他礦物多不干擾，常先<strong>灰化溶解</strong>；多用<strong>標準曲線</strong>定量。</div>')

add(ATT, dc.kt("21.3.4 離子選擇電極", "ISE：直接讀離子") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>原理同 pH 電極，依 <strong>Nernst 方程</strong>產生電位</li>" +
    "<li>改變感應玻璃組成 → 對特定離子(Na⁺、Cl⁻、Ca²⁺…)專一</li>" +
    "<li>電位(mV) ∝ 離子<strong>活度</strong>；用 ISA 緩衝固定離子強度</li>" +
    "<li>以 <strong>mV vs log 濃度</strong> 標準曲線定量</li></ul></div>" +
    '<div class="note">優點：可直接測陰陽離子、不受濁度/顏色影響、設備便宜。<br>' +
    "缺點：<strong>低濃度測不準</strong>、反應慢、電極須專一。</div></div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ④","方法配對「測哪種礦物」", 7,
    "同樣這些方法，換個角度——它們最常拿來測哪種礦物？分到三類。"), ' data-game="g3"')

add(ATT, dc.kt("21.4 快速鹽分析儀", "現場測鹽：又快又準") +
    '<div class="grid3" style="margin-top:22px">' +
    dc.card("⚗️","自動滴定","自動加 AgNO₃ + ISE 判終點；少主觀誤差","b") +
    dc.card("⚡","庫侖法","電流由銀絲原位產生 Ag⁺，無需標定滴定液","a") +
    dc.card("🔋","電導法","鹽解離成離子→電導 ∝ 濃度，並校正溫度","g") + '</div>' +
    '<div class="note" style="margin-top:16px">Quantab® 試紙、鹽度計/折射計也常用——多源自沉澱滴定或物理量原理。</div>')

add(ATT, dc.kt("21.5 vs 現代儀器", "傳統法 vs AAS / ICP") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧪","傳統法","試劑器材常備、技術門檻低、單一元素便宜；但較耗人力、偵測限較高","b") +
    dc.card("📡","AAS / ICP","多元素、痕量(ppb)、線性廣；但儀器貴、需訓練、多需灰化","a") +
    '</div><div class="note" style="margin-top:18px">小型實驗室、樣品少時 → <strong>傳統法</strong>合適；大量樣品/痕量/多元素 → <strong>AAS/ICP</strong>。</div>')

add(ATT, dc.kt("21.2.3 干擾與校正", "讓數據可信的三招") +
    '<div class="grid3" style="margin-top:22px">' +
    dc.card("🧫","試劑空白","扣掉試劑本身帶入的礦物污染","b") +
    dc.card("💉","加標(spike)","加已知量礦物，整合萃取損失與基質效應","a") +
    dc.card("📈","基質標準曲線","在含干擾離子的背景下配標準，貼近真實樣品","g") + '</div>' +
    '<div class="note" style="margin-top:16px">水須<strong>煮沸除碳酸鹽</strong>；可用選擇性沉澱/離子交換移除干擾離子。</div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對方法", 5), ' data-game="g5"')

# ---------------- 喚起行動 ----------------
add(ACT, dc.cmp_inner("一張表選方法（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"meas","t":"s","label":"原理/測什麼"},
     {"k":"sens","t":"n","label":"靈敏度","star":True},{"k":"app","t":"s","label":"主要應用"}],
    "靈敏度：★ 越多越靈敏(偵測限越低)。整合自 Table 21.3。", kicker="21.5 方法比較"), ' data-game="cmp"')

add(ACT, dc.chart_inner("range", "各法的<span class='hi'>偵測範圍</span>差很多",
    "概念示意：ISE 約 1–10⁻⁶ M；ICP/AAS 可達 ppb。數值為數量級概念，非單一定值。",
    kicker="21.5 偵測限概念", height="52vh"), ' data-chart="range"')

add(ACT, dc.kt("方法選擇", "跟著決策樹走") +
    '<div class="svgwrap" style="margin-top:10px">' + DTREE_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:14px">下一頁實戰：用 EDTA 滴定算水的硬度 →</p>')

add(ACT, dc.kt("光譜法概念", "AAS：火焰原子吸收") +
    '<div class="svgwrap" style="margin-top:6px">' + AAS_SVG + '</div>' +
    '<div class="note" style="margin-top:14px">火焰把樣品<strong>原子化</strong>，空心陰極燈發特定波長，原子吸收量<strong>正比於濃度</strong>。' +
    "ICP-OES 則以電漿激發、測<strong>發射</strong>光，可多元素同時、線性更廣。</div>")

add(ACT, dc.kt("21.8 計算", "EDTA 滴定：算水的硬度") +
    '<div class="grid2" style="margin-top:14px"><div class="eq" style="font-size:1.05rem">硬度(mg/L) = ' +
    '<span class="frac"><b>V<sub>EDTA</sub> · M<sub>EDTA</sub> · 100090</b><span>樣品體積 (L)</span></span></div>' +
    '<div><ul class="clean"><li>mol EDTA = mol (Ca+Mg)（1:1）</li>' +
    "<li>以 <strong>CaCO₃</strong> 表示，MW = 100.09 g/mol</li>" +
    "<li>×1000 把 mol 換成 mg、×(1/L) 變濃度</li>" +
    "<li>對照硬度等級：>120 ppm 為硬水</li></ul></div></div>")

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關",
    "取 <strong>50.0 mL</strong> 水樣，以 <strong>0.0100 M</strong> EDTA 滴定 Ca+Mg，"
    "滴定至終點共用 <strong>8.00 mL</strong>。求水的硬度（以 CaCO₃ 計，<strong>mg/L</strong>）。", unit="mg/L"),
    ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li><strong>分析＝分離＋測定</strong>，傳統法多需先<strong>灰化</strong></li>" +
    "<li><strong>EDTA</strong> 滴定測 Ca/硬度（pH 10、粉紅→藍）</li>" +
    "<li><strong>Mohr/Volhard</strong> 用 Ag⁺ 沉澱測氯 → 換算食鹽</li></ul>" +
    '<ul class="clean"><li><strong>比色法</strong>(磷-鉬藍) 與 <strong>ISE</strong> 各有專長</li>' +
    "<li>痕量/多元素用 <strong>AAS/ICP</strong>；防污染靠空白/加標/基質校正</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明礦物質分析「分離 + 測定」的骨架",
     "解釋為什麼傳統法常需先灰化、如何防污染",
     "描述 EDTA 滴定測鈣/硬度的原理與終點變色",
     "比較 Mohr 與 Volhard 兩種測氯方法",
     "說明比色法(磷-鉬藍)與 ISE 的原理",
     "判斷該用傳統法還是 AAS/ICP",
     "由 EDTA 滴定數據算出水的硬度"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把礦物質分析<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions、Practice Problems<br>"
    "🔜 銜接章節：<strong>灰分分析 (Ch16)</strong>、<strong>原子光譜法 (Ch9)</strong>、<strong>離子層析 (Ch13)</strong><br>"
    "🧪 思考：你要測硬度、測鹽、測磷、還是痕量多元素？該選哪種方法？",
    ["EDTA","Mohr/Volhard","磷-鉬藍","ISE","AAS/ICP"]), ' data-cover="1"')

# ---------------- CFG ----------------
CFG = {
  "charts": {
    "ca": {"type":"bar","yTitle":"Ca (mg/100 g)",
      "labels":["牛奶","茅屋乳酪","雞肉腸","蛋","葡萄乾","馬鈴薯","全麥麵粉","糙米","蘋果","香蕉"],
      "datasets":[{"label":"鈣 (mg/100 g)","data":[113,111,92,56,50,30,34,9,8,5],"color":"#1f6feb"}]},
    "range": {"type":"bar","yTitle":"log₁₀(偵測下限, M) 概念",
      "labels":["EDTA 滴定","Mohr/Volhard","比色法","ISE","AAS","ICP-OES"],
      "datasets":[{"label":"偵測下限數量級 (越負越靈敏)","data":[-3,-3,-5,-6,-7,-9],"color":"#d9822b"}],
      "zero":False}
  },
  "bucket": {
    "g1": {"cats":["滴定(體積)","比色(吸光)","電位/光譜(儀器)"],
      "items":[{"t":"EDTA 錯合滴定","c":"滴定(體積)"},{"t":"Mohr 沉澱滴定","c":"滴定(體積)"},
        {"t":"Volhard 反滴定","c":"滴定(體積)"},
        {"t":"磷-鉬藍比色","c":"比色(吸光)"},{"t":"鐵顯色比色","c":"比色(吸光)"},
        {"t":"離子選擇電極 ISE","c":"電位/光譜(儀器)"},{"t":"AAS / ICP","c":"電位/光譜(儀器)"}],
      "ok":"🎉 全對！滴定看體積、比色看吸光、ISE/光譜靠儀器訊號。",
      "tip":"提示：EDTA/Mohr/Volhard 都是滴定；鉬藍與鐵顯色是比色；ISE 與 AAS/ICP 是儀器。"},
    "g3": {"cats":["測鈣/硬度","測氯/鹽","測磷或多元素"],
      "items":[{"t":"EDTA 滴定","c":"測鈣/硬度"},{"t":"AquaChek 試紙","c":"測鈣/硬度"},
        {"t":"Mohr 滴定","c":"測氯/鹽"},{"t":"Volhard 滴定","c":"測氯/鹽"},{"t":"Quantab 試紙","c":"測氯/鹽"},
        {"t":"磷-鉬藍比色","c":"測磷或多元素"},{"t":"ICP-OES","c":"測磷或多元素"}],
      "ok":"🎉 正確！EDTA 測硬度、Ag⁺ 法測氯鹽、鉬藍測磷、ICP 測多元素。",
      "tip":"提示：AquaChek＝硬度試紙；Quantab＝鹽試紙；鉬藍專測磷；ICP 一次多元素。"}
  },
  "mcq": {
    "g2":[
      {"q":"礦物質分析最大的隱憂是什麼？","o":["顏色干擾","樣品污染","溫度太低","體積太大"],"a":1,
       "e":"研磨器具、玻璃、試劑都可能帶入礦物 → 污染是首要隱憂。"},
      {"q":"EDTA 滴定鈣/鎂時為何要控制在 pH 10？","o":["怕變色太快","低 pH 下 EDTA 螯合位被質子化、錯合不穩","高 pH 比較便宜","與溫度無關"],"a":1,
       "e":"pH 太低 EDTA 被質子化失效；太高(>12)金屬會沉澱成氫氧化物，故定在 pH 10。"},
      {"q":"用 Calmagite/EBT 指示劑，EDTA 滴定的終點顏色變化是？","o":["藍→粉紅","粉紅→藍","無色→紅","綠→黃"],"a":1,
       "e":"金屬被 EDTA 奪走後，指示劑由粉紅(錯合)轉為藍(游離)。"},
      {"q":"為何傳統法常要先「灰化」樣品？","o":["增加重量","把礦物質從有機基質游離出來","產生顏色","降低 pH"],"a":1,
       "e":"有機基質會妨礙礦物與試劑反應，灰化把礦物游離出來；水樣常可直接測。"}
    ],
    "g5":[
      {"q":"要測自來水的「總硬度」，最合適的傳統法是？","o":["Mohr 滴定","EDTA 錯合滴定","磷-鉬藍比色","UV 280"],"a":1,
       "e":"硬度＝Ca+Mg，EDTA 在 pH 10 一次滴定總量，以 CaCO₃ 表示。"},
      {"q":"測奶油的鹽(NaCl)含量，常用哪種滴定？","o":["EDTA","Mohr(AgNO₃+鉻酸)","Volhard 必須","Karl Fischer"],"a":1,
       "e":"Mohr 正滴定直接用 AgNO₃ 滴氯，磚紅 Ag₂CrO₄ 為終點(AOAC 960.29)。"},
      {"q":"乳酪在硝酸中溶解後測氯，較適合哪種法？","o":["Mohr","Volhard 反滴定","比色","ISE 不可用"],"a":1,
       "e":"酸性、需先過量沉澱再回滴的情況用 Volhard(AOAC 935.43)。"},
      {"q":"要快速、非破壞且多元素同時測痕量礦物，選？","o":["EDTA 滴定","Mohr","ICP-OES","Quantab 試紙"],"a":2,
       "e":"ICP-OES 多元素同時、痕量(ppb)、線性廣，但儀器貴需訓練。"},
      {"q":"想直接測牛奶中的鈣或低鈉冰淇淋的鈉，方便的選擇？","o":["離子選擇電極 ISE","Mohr","Volhard","重量法"],"a":0,
       "e":"ISE 可直接測特定離子、不受濁度顏色影響，適合 Na/K/Ca 等品管。"}
    ]
  },
  "sort": {
    "g4":{"steps":["樣品以非金屬器具磨碎、精秤","550°C 高溫灰化燒掉有機質",
       "灰分以強酸溶解成礦物離子","加氨緩衝調至 pH 10、加 Calmagite 指示劑",
       "用標準 EDTA 滴定至粉紅變藍","記錄 EDTA 體積，扣除試劑空白","由 mol EDTA 換算鈣含量"],
       "shuffle":[2,4,0,6,1,5,3],
       "ok":"🎉 順序正確！灰化→溶解→調 pH→滴定→扣空白→換算。",
       "tip":"提示：一定先灰化溶解、調好 pH 才滴定，最後才換算成鈣。"}
  },
  "calc": {
    "g6":{"answer":160.0,"tol":3.0,
      "ok":"🎉 正確！n(EDTA)=0.00800 L×0.0100 M=8.0×10⁻⁵ mol＝mol(Ca+Mg)；"
           "×100090 mg/mol÷0.0500 L = <b>160 mg/L</b>（以 CaCO₃ 計，屬硬水）。",
      "bad":"再算算：mol=V×M=0.00800×0.0100；mg CaCO₃=mol×100090；再÷0.0500 L 得 mg/L。",
      "hint":"提示：mol=8.0×10⁻⁵；×100090≈8.0 mg CaCO₃；÷0.050 L ≈ 160 mg/L。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"meas"},{"k":"sens"},{"k":"app"}],
    "rows":[
      {"m":"EDTA 滴定","meas":"Ca+Mg 錯合(體積)","sens":2,"app":"水硬度·灰中鈣·試紙"},
      {"m":"Mohr 滴定","meas":"Cl⁻ 沉澱(正滴定)","sens":2,"app":"奶油/食品鹽分"},
      {"m":"Volhard 滴定","meas":"Cl⁻ 沉澱(反滴定)","sens":2,"app":"乳酪等高氯食品"},
      {"m":"比色法","meas":"顯色+Beer 吸光","sens":4,"app":"磷·鐵等單一元素"},
      {"m":"ISE","meas":"離子活度→mV","sens":3,"app":"Na/K/Cl/Ca 品管"},
      {"m":"AAS","meas":"原子吸收","sens":5,"app":"單元素·痕量"},
      {"m":"ICP-OES","meas":"原子發射","sens":5,"app":"多元素·痕量·標示"}
    ]
  }
}

dc.build_html(
  {"title":"礦物質分析 Mineral Analysis · Nielsen Ch21","brand":"MINERAL · CH21"},
  S, CFG, OUT)
