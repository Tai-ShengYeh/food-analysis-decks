# -*- coding: utf-8 -*-
"""Nielsen Ch15 Moisture & Total Solids Analysis — SOIL HTML deck. Uses ../soil_deck_common.py.
Run: python build_ch15.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
OVEN_SVG = """
<svg viewBox="0 0 320 300">
 <defs><linearGradient id="go" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eaf2ff"/><stop offset="1" stop-color="#cfe0f6"/></linearGradient></defs>
 <rect x="40" y="40" width="240" height="200" rx="14" fill="url(#go)" stroke="#1f6feb" stroke-width="3"/>
 <rect x="58" y="60" width="204" height="150" rx="8" fill="#ffffff" stroke="#1f6feb" stroke-width="2"/>
 <line x1="58" y1="118" x2="262" y2="118" stroke="#cfe0f6" stroke-width="2"/>
 <line x1="58" y1="160" x2="262" y2="160" stroke="#cfe0f6" stroke-width="2"/>
 <rect x="92" y="92" width="48" height="20" rx="4" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
 <rect x="178" y="92" width="48" height="20" rx="4" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
 <rect x="92" y="134" width="48" height="20" rx="4" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
 <text x="160" y="80" text-anchor="middle" class="lblb">乾燥皿 + 樣品</text>
 <path d="M150 178 q5 -14 10 0 M170 178 q5 -14 10 0" fill="none" stroke="#d9822b" stroke-width="2.4"/>
 <circle cx="252" cy="50" r="9" fill="#d9822b"/>
 <text x="252" y="36" text-anchor="middle" class="lbl">風扇</text>
 <rect x="120" y="240" width="80" height="16" rx="5" fill="#48597a"/>
 <text x="160" y="288" text-anchor="middle" class="lbl">強制對流烘箱 forced-draft oven</text>
</svg>"""

KF_SVG = """
<svg viewBox="0 0 480 340">
 <defs><marker id="arkf" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#1f9d6b"/></marker></defs>
 <text x="240" y="22" text-anchor="middle" class="lblb" font-size="15">Karl Fischer 滴定</text>
 <!-- 滴定管 burette -->
 <rect x="170" y="44" width="26" height="92" rx="3" fill="#eaf2ff" stroke="#1f6feb" stroke-width="2.5"/>
 <rect x="173" y="58" width="20" height="62" fill="#d9822b" opacity="0.5"/>
 <line x1="170" y1="72" x2="178" y2="72" stroke="#1f6feb" stroke-width="1.2"/>
 <line x1="170" y1="94" x2="178" y2="94" stroke="#1f6feb" stroke-width="1.2"/>
 <line x1="170" y1="116" x2="178" y2="116" stroke="#1f6feb" stroke-width="1.2"/>
 <text x="162" y="66" text-anchor="end" class="lblb">滴定管</text>
 <text x="162" y="84" text-anchor="end" class="lbl">KF 試劑 (I₂)</text>
 <!-- 加液管 + 滴 -->
 <path d="M183 136 v42" stroke="#1f6feb" stroke-width="3" fill="none"/>
 <circle cx="183" cy="170" r="3.4" fill="#d9822b"/>
 <!-- 密閉蓋 -->
 <rect x="120" y="178" width="126" height="12" rx="4" fill="#cfe0f6" stroke="#1f6feb" stroke-width="2"/>
 <text x="175" y="173" text-anchor="end" class="lbl">密閉蓋 · 隔絕大氣水分</text>
 <!-- 反應槽 beaker -->
 <path d="M126 190 L126 292 Q126 304 138 304 L228 304 Q240 304 240 292 L240 190" fill="none" stroke="#1f6feb" stroke-width="3"/>
 <path d="M129 216 L237 216 L237 292 Q237 301 228 301 L138 301 Q129 301 129 292 Z" fill="#f3d6b0"/>
 <text x="172" y="244" text-anchor="middle" class="lblb">密閉反應槽</text>
 <text x="172" y="264" text-anchor="middle" class="lbl">樣品 + 甲醇</text>
 <!-- 電極 electrode -->
 <rect x="212" y="180" width="9" height="86" rx="2" fill="#9fb3d1" stroke="#48597a" stroke-width="1.5"/>
 <!-- 攪拌子 + 攪拌器 -->
 <ellipse cx="183" cy="290" rx="17" ry="5" fill="#d9822b"/>
 <rect x="128" y="308" width="110" height="16" rx="5" fill="#48597a"/>
 <text x="183" y="320" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="'Noto Sans TC',sans-serif">磁攪拌器</text>
 <!-- 偵測器標籤 + 箭頭指電極 -->
 <rect x="306" y="118" width="164" height="62" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
 <text x="388" y="144" text-anchor="middle" class="lblb">電位偵測電極</text>
 <text x="388" y="164" text-anchor="middle" class="lbl">過量 I₂ → 偵測終點</text>
 <path d="M306 156 C 268 176, 245 184, 222 196" stroke="#1f9d6b" stroke-width="2.5" fill="none" marker-end="url(#arkf)"/>
</svg>"""

DIST_SVG = """
<svg viewBox="0 0 420 300">
 <defs><linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbeede"/><stop offset="1" stop-color="#f3d6b0"/></linearGradient></defs>
 <path d="M70 230 a58 58 0 1 0 -4 0 z" fill="url(#gd)" stroke="#1f6feb" stroke-width="3"/>
 <text x="68" y="200" text-anchor="middle" class="lblb">樣品</text>
 <text x="68" y="220" text-anchor="middle" class="lbl">+ 甲苯</text>
 <path d="M50 246 q4 -12 8 0 M70 246 q4 -12 8 0" fill="none" stroke="#d9822b" stroke-width="2.4"/>
 <text x="68" y="284" text-anchor="middle" class="lbl">加熱共沸</text>
 <path d="M68 116 v-44 h120" stroke="#1f6feb" stroke-width="3" fill="none"/>
 <rect x="188" y="56" width="34" height="120" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
 <text x="205" y="48" text-anchor="middle" class="lbl">水分收集管</text>
 <rect x="190" y="120" width="30" height="52" fill="#cfe0f6"/>
 <text x="205" y="150" text-anchor="middle" class="lblb" font-size="12">水</text>
 <path d="M222 80 h70" stroke="#1f6feb" stroke-width="3" fill="none"/>
 <rect x="292" y="50" width="110" height="60" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
 <text x="347" y="76" text-anchor="middle" class="lblb" font-size="13">冷凝管</text>
 <text x="347" y="96" text-anchor="middle" class="lbl" font-size="12">回流甲苯</text>
 <text x="210" y="28" text-anchor="middle" class="lblb" font-size="15">甲苯共沸蒸餾（Bidwell–Sterling）</text>
</svg>"""

DTREE_SVG = """
<svg viewBox="0 0 980 360">
 <rect x="380" y="14" width="220" height="56" rx="12" fill="#1f6feb"/>
 <text x="490" y="40" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">你的樣品是什麼？</text>
 <text x="490" y="60" text-anchor="middle" fill="#cfe0f6" font-size="12">選擇水分分析方法</text>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M420 70 C 200 110,130 120,120 150"/><path d="M470 70 C 400 120,380 120,375 150"/>
  <path d="M510 70 C 590 120,610 120,625 150"/><path d="M560 70 C 800 110,860 120,875 150"/></g>
 <g font-size="14" font-weight="800">
  <rect x="30" y="150" width="190" height="120" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="125" y="178" text-anchor="middle" fill="#15233f">一般食品?</text>
  <text x="125" y="206" text-anchor="middle" fill="#d9822b" font-size="16">烘箱乾燥</text>
  <text x="125" y="232" text-anchor="middle" fill="#48597a" font-size="12">官方法、可多樣品</text>
  <text x="125" y="252" text-anchor="middle" fill="#48597a" font-size="12">高糖改真空 ≤70°C</text>
  <rect x="280" y="150" width="190" height="120" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="375" y="178" text-anchor="middle" fill="#15233f">低水分·高糖油?</text>
  <text x="375" y="206" text-anchor="middle" fill="#1f6feb" font-size="16">Karl Fischer</text>
  <text x="375" y="232" text-anchor="middle" fill="#48597a" font-size="12">不加熱、最準</text>
  <text x="375" y="252" text-anchor="middle" fill="#48597a" font-size="12">巧克力·油脂·乾果</text>
  <rect x="530" y="150" width="190" height="120" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="625" y="178" text-anchor="middle" fill="#15233f">香料·揮發物?</text>
  <text x="625" y="206" text-anchor="middle" fill="#1f9d6b" font-size="16">甲苯蒸餾</text>
  <text x="625" y="232" text-anchor="middle" fill="#48597a" font-size="12">熱分解少、直接測水</text>
  <text x="625" y="252" text-anchor="middle" fill="#48597a" font-size="12">香料官方法</text>
  <rect x="780" y="150" width="190" height="120" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="875" y="178" text-anchor="middle" fill="#15233f">線上快速品管?</text>
  <text x="875" y="206" text-anchor="middle" fill="#15233f" font-size="16">NIR / 微波</text>
  <text x="875" y="232" text-anchor="middle" fill="#48597a" font-size="12">快速、非破壞</text>
  <text x="875" y="252" text-anchor="middle" fill="#48597a" font-size="12">需先校正</text>
 </g>
</svg>"""

# ---------------- 引起動機 ----------------
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 15",
    "水分<span style='color:var(--accent-2)'>分析</span>", "Moisture & Total Solids Analysis",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>烘箱乾燥 · Karl Fischer · 蒸餾法 · NIR · 水活性",
    ["烘箱乾燥","Karl Fischer","甲苯蒸餾","NIR","折射率"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">一片洋芋片為何要<span class="hi">控制到 1.5% 水？</span></div>
  <p class="subtitle" style="max-width:780px;margin:22px auto 0">水分含量決定食品的<strong>保存性、口感、重量與合法性</strong>。<br>
  但水分子小又無所不在——是最重要、卻也最難測準的分析之一。</p>
  <div style="margin-top:24px"><span class="pill">保存性</span><span class="pill">品質</span>
  <span class="pill">包裝運輸</span><span class="pill">法規標準</span><span class="pill">營養計算</span></div></div>""")

add(MOT, dc.kt("15.1.1 為什麼重要", "為什麼要分析水分") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("🛡️","保存與穩定","脫水蔬果、奶粉、香料：水高易壞、結塊") +
    dc.card("⭐","品質因子","果醬抑制糖結晶、穀片 4–8% 水控制口感","a") +
    dc.card("📦","包裝運輸","濃縮乳汁、糖漿降水分以利包裝運送","g") +
    dc.card("⚖️","法規標準","切達起司 ≤39% 水、濃縮麵粉 ≤15% 水","b") + '</div>')

add(MOT, dc.kt("15.1.2 水的形式", "食品裡的<span class='hi'>水</span>") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li><strong>自由水</strong>：表面、毛細、可流動，最易蒸發</li>" +
    "<li><strong>結合水</strong>：以氫鍵、離子吸引依附在 −OH、=O、−NH₂</li>" +
    "<li><strong>包埋水</strong>：陷在膠體或緻密基質中，最難移除</li>" +
    "<li>幾乎<span class='em'>無法</span>把食品中所有水分完全去除</li>" +
    '</ul></div><div class="note"><strong>關鍵：水分子小、極性高、會跑。</strong><br>' +
    "取樣到秤重的每一步都可能得水或失水 → 控制溫度與時間最重要。</div></div>")

add(MOT, dc.chart_inner("moist", "食物裡的<span class='hi'>水分</span>含量", "資料：USDA (2023)，Table 15.3，% 水分（濕基）。",
    kicker="15.2.1 食物中的含量"), ' data-chart="moist"')

add(MOT, dc.kt("15.1.3 取樣與處理", "誤差，常常在<span class='hi'>秤之前</span>就發生") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li>暴露大氣的時間要<strong>越短越好</strong></li>" +
    "<li>研磨摩擦生熱會趕走水分，須避免</li>" +
    "<li>儲存容器<strong>頂空要小</strong>，水會在樣品與容器間移轉</li>" +
    "<li>控制溫度波動——水會往樣品的<strong>較冷處</strong>遷移</li>" +
    '</ul></div><div class="note"><strong>取樣與處理是任何分析中最大的潛在誤差來源。</strong><br>' +
    "整批取出、快速重新拌勻後再分取，才有代表性。</div></div>")

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">核心命題</div>
  <div class="hook" style="font-size:clamp(1.7rem,4vw,3rem)">秤水，<span class="hi">就是秤失重</span></div>
  <p class="lead" style="max-width:820px;margin:20px auto 0">多數<strong>直接法</strong>的根基：把水蒸乾，<strong>失去的重量</strong>就是水。剩下的固體＝<strong>總固形物</strong>。</p>
  <div class="eq" style="max-width:600px;margin:24px auto 0">% 水分 = <span class="frac"><b>濕重 − 乾重</b><span>濕重</span></span> × 100<br>
  <span style="font-size:.8em;color:var(--ink-2)">% 總固形物 = 100 − % 水分</span></div></div>""")

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","水的三種形式", 6,
    "把 6 個描述分到「自由水 / 結合水 / 包埋水」三類。"), ' data-game="g1"')

# ---------------- 維持注意 ----------------
add(ATT, dc.kt("方法全覽", "直接法 vs 間接法") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("🔥","直接法 · 去水","烘箱乾燥、蒸餾、Karl Fischer：把水移除或反應掉","b") +
    dc.card("📡","間接法 · 測性質","介電、密度、折射率、NIR、冰點：測與水有關的物性","a") +
    dc.card("⚖️","測量方式","直接法靠秤重 / 體積 / 滴定量化","g") +
    dc.card("🎯","校正需求","間接法快速非破壞，但須對直接法建檢量線","b") + '</div>')

add(ATT, dc.kt("15.2.2 烘箱乾燥", "烘箱乾燥：簡單可靠") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + OVEN_SVG + '</div><div><ul class="clean">' +
    "<li><strong>強制對流烘箱</strong>：風扇強制循環，溫差最小(≤1°C)</li>" +
    "<li><strong>真空烘箱</strong>：減壓(25–100 mmHg)下低溫(60–70°C)快乾</li>" +
    "<li><strong>對流(常壓)烘箱</strong>：無風扇、溫差可達 10°C，精度差</li>" +
    "<li>失重 = 水分；需控制<span class='em'>時間與溫度</span></li>" +
    '</ul><div class="note" style="margin-top:14px">高糖樣品改用真空烘箱 ≤70°C，避免梅納褐變與糖水解。</div></div></div>')

add(ATT, dc.chart_inner("dry", "不同烘箱的<span class='hi'>溫度差異</span>",
    "整合 Table 15.4／15.5：烘箱內最大溫差越小越精準。", kicker="15.2.2 溫度控制", height="52vh"),
    ' data-chart="dry"')

add(ATT, dc.kt("15.2.2 時間與溫度", "乾燥是一場<span class='hi'>取捨</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("⏱️","乾不夠","時間太短、溫度太低 → 水沒走完 → <strong>低估</strong>水分","b") +
    dc.card("🔥","過頭了","時間太長、溫度太高 → 成分分解生水或揮發物流失 → 誤差","a") +
    '</div><div class="note" style="margin-top:18px">技巧：液體(果汁/牛奶)先在<strong>蒸氣浴預乾</strong>避免噴濺；' +
    "黏結樣品用<strong>砂皿法</strong>(乾砂+玻棒)分散、防結殼。乾燥到<strong>恆重</strong>(兩次秤重相差 < 0.1–0.2 mg)。</div>")

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","烘箱乾燥即時測驗", 4), ' data-game="g2"')

add(ATT, dc.kt("15.2.4 Karl Fischer", "KF 滴定：微量水專家") +
    '<div class="svgwrap" style="margin-top:10px">' + KF_SVG + '</div>' +
    '<div class="note" style="margin-top:16px">每 1 mol 水耗 1 mol I₂：水把 SO₂ 還原碘 → 過量碘到達終點。' +
    "<strong>不加熱、快速、最準</strong>，是低水分高糖/高蛋白食品的首選。</div>")

add(ATT, dc.kt("15.2.3 蒸餾法", "甲苯共沸：直接量水") +
    '<div class="svgwrap" style="margin-top:10px">' + DIST_SVG + '</div>' +
    '<div class="note" style="margin-top:16px">樣品與<strong>甲苯</strong>共沸，水被帶出冷凝、在收集管<strong>直接讀體積</strong>。' +
    "熱分解比高溫烘箱少，是香料的官方法；須注意乳化與管壁殘水。</div>")

add(ATT, dc.game_sort_inner("g4","小遊戲 ③","烘箱乾燥流程排序", 6,
    "用 ▲▼ 把烘箱乾燥法的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("15.2.5 物理(間接)法", "不去水，也能測水") +
    '<div class="grid3" style="margin-top:22px">' +
    dc.card("⚡","介電/微波","水介電常數 80 ≫ 乾物 10；測電容變化。穀物、線上品管(≤35%水)","b") +
    dc.card("💧","密度/折射率","比重計、糖度計(°Brix)、折射儀；測液體糖漿/果汁的固形物","a") +
    dc.card("📡","NIR 近紅外","水的 −OH 在 1400／1920 nm 吸收；快速非破壞，穀物乾蔬官方法","g") + '</div>')

add(ATT, dc.kt("15.2.2 快速熱重法", "幾分鐘 vs 幾小時") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("📶","微波乾燥","微波能加熱蒸水，4–8 分鐘；起司/肉製品線上調整","b") +
    dc.card("🔦","紅外/鹵素乾燥","紅外燈或鹵素加熱穿透樣品，10–25 分鐘快速品管","a") +
    '</div><div class="note" style="margin-top:18px"><strong>熱重分析(TGA)</strong>：連續秤質量、控溫控氣氛，可定水分、水合物計量與分解——精準但設備貴。</div>')

add(ATT, dc.kt("15.2.6 取樣的陷阱", "為什麼水分<span class='hi'>最難測準</span>？") +
    '<div class="note" style="margin-top:14px">起司在天平上 50% RH 只要 <strong>5 秒就失 0.01% 水</strong>；' +
    "乾燥粉末則會從空氣<strong>吸水</strong>。取樣到秤重必須又快又密閉。</div>" +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("📉","會失水","高水分樣品暴露空氣 → 低估水分","b") +
    dc.card("📈","會吸水","低 a_w 的脆片/粉末吸收濕氣 → 高估水分","a") + '</div>')

add(ATT, dc.game_bucket_inner("g3","小遊戲 ④","各方法「測什麼」分類", 6,
    "同樣的方法，換個角度——它們實際量測的是什麼訊號？分到三類。"), ' data-game="g3"')

add(ATT, dc.kt("15.3 水活性 a_w", "水分量 ≠ 水的活性") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>a_w = 食品水蒸氣壓 p ÷ 純水蒸氣壓 p₀（0–1）</li>" +
    "<li>a_w = ERH/100，與平衡相對濕度相關</li>" +
    "<li>影響<strong>微生物生長、化學/酵素反應、質地</strong></li>" +
    "<li>同樣水分含量，a_w 不同 → 穩定性不同</li></ul></div>" +
    '<div class="note"><strong>a_w 0.85</strong> 是法規對病原菌生長的分界。' +
    "水分『遷移』是順著 a_w 由高到低，而非水分含量。</div></div>")

add(ATT, dc.kt("摻假與盲點", "水分造假怎麼<span class='hi'>抓</span>？") +
    '<div class="note" style="margin-top:14px">牛奶<strong>加水</strong>會抬高水分、稀釋固形物。因冰點是牛奶最穩定的物性，' +
    "AOAC 961.07 用<strong>冰點儀</strong>(正常乳 −0.527°C)偵測加水。</div>" +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("🧊","冰點法","加水使冰點上升 → 算出加水量；FDA 拒收 > −0.507°C 的乳","b") +
    dc.card("⚠️","分解陷阱","碳水高溫分解會『生水』→ 高估；蔗糖水解會『耗水』→ 低估","a") + '</div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對方法", 5), ' data-game="g5"')

# ---------------- 喚起行動 ----------------
add(ACT, dc.cmp_inner("一張表選方法（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"meas","t":"s","label":"量測對象"},
     {"k":"speed","t":"n","label":"速度","star":True},{"k":"app","t":"s","label":"主要應用"}],
    "速度：★ 越多越快。整合自 Table 15.5／15.6。", kicker="15.2.6 方法比較"), ' data-game="cmp"')

add(ACT, dc.kt("方法選擇", "跟著決策樹走") +
    '<div class="svgwrap" style="margin-top:10px">' + DTREE_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:14px">下一頁實戰：算一份液體樣品的水分與固形物 →</p>')

add(ACT, dc.kt("15.3 水活性應用", "為什麼要<span class='hi'>同時</span>量 a_w") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("🦠","控制微生物","各菌種有 a_w 生長下限；a_w 0.85 是低酸/酸化食品法規分界","b") +
    dc.card("🔄","防止水分遷移","派皮與內餡之間，水順 a_w 由高往低跑 → 影響質地保存","a") +
    dc.card("📊","穩定性地圖","Labuza 圖：脂質氧化、梅納反應、酵素速率隨 a_w 變化","g") +
    '</div><div class="note" style="margin-top:16px">水分含量 + 水活性 = 完整的水分分析。<strong>降 a_w 不是殺菌步驟</strong>，只是抑制生長。</div>')

add(ACT, dc.kt("15.2.2.1.7 計算", "從秤重到 % 水分與固形物") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">% 水分 = ' +
    '<span class="frac"><b>濕重 − 乾重</b><span>濕重</span></span> × 100</div>' +
    '<div><ul class="clean"><li>先扣除<strong>乾皿+玻纖蓋</strong>的重量</li>' +
    "<li>濕重 − 乾重 = 失去的水重</li><li>% 總固形物 = 乾重 ÷ 濕重 × 100</li>" +
    "<li>% 水分 + % 固形物 = 100</li></ul></div></div>")

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關",
    "液體樣品（Practice Problem 3）：乾皿+玻纖蓋 1.0376 g，皿+液體樣品 4.6274 g，"
    "皿+烘乾後 1.7321 g。求<strong>% 水分（濕基）</strong>。", unit="%"), ' data-game="g6"')

add(ACT, dc.kt("延伸應用", "濃縮：還要<span class='hi'>再蒸掉</span>多少水？") +
    '<div class="grid2-1" style="margin-top:14px"><div><ul class="clean">' +
    "<li>濃縮湯起始 1000 gal、8.67% 固形物</li>" +
    "<li>濃到 26.54% 固形物 → 體積 = (8.67/26.54)×1000 = <strong>326.7 gal</strong></li>" +
    "<li>標準要 28.63% → 體積 = (8.67/28.63)×1000 = <strong>302.8 gal</strong></li>" +
    "<li>還要蒸掉 326.7 − 302.8 = <span class='em'>23.9 gal</span> 水</li>" +
    '</ul></div><div class="note">關鍵觀念：濃縮過程<strong>固形物總量不變</strong>，' +
    "用『固形物守恆』反推體積，差值就是要再移除的水。(Practice Problem 1)</div></div>")

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li><strong>秤水＝秤失重</strong>；% 水分=(濕−乾)/濕×100，固形物=100−水分</li>" +
    "<li>水有<strong>自由/結合/包埋</strong>三形式，難完全去除</li>" +
    "<li>直接法：烘箱(官方·多樣品) vs <strong>Karl Fischer</strong>(微量·不加熱)</li></ul>" +
    '<ul class="clean"><li>間接法：NIR/介電/折射率快速，<strong>須先校正</strong></li>' +
    "<li><strong>a_w</strong> 比水分更能預測微生物與穩定性(0.85 分界)</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說出水的三種形式與其去除難易",
     "解釋『秤水就是秤失重』與總固形物的關係",
     "比較強制對流、真空、微波烘箱的差異",
     "說明 Karl Fischer 為何適合低水分高糖/油食品",
     "判斷該用哪種方法（一般/低水分/香料/線上品管）",
     "由秤重數據算出 % 水分與 % 固形物",
     "區分水分含量與水活性 a_w 的意義"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把水分分析<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions、Practice Problems<br>"
    "🔜 銜接章節：<strong>灰分分析 (Ch16)</strong>、<strong>蛋白質分析 (Ch18)</strong><br>"
    "🧪 思考：你的樣品水分高嗎？含糖油嗎？要官方法還是快速品管？該選哪種方法？",
    ["烘箱乾燥","Karl Fischer","甲苯蒸餾","NIR","水活性 a_w"]), ' data-cover="1"')

# ---------------- CFG ----------------
CFG = {
  "charts": {
    "moist": {"type":"bar","yTitle":"% 水分",
      "labels":["西瓜","柳橙","蘋果","牛奶(2%)","雞胸肉","切達起司","白麵包","葡萄乾","奶油","玉米片","花生"],
      "datasets":[{"label":"% 水分(濕基)","data":[91.5,86.3,85.6,89.3,68.6,36.8,13.4,15.3,15.9,3.5,1.6],"color":"#1f6feb"}]},
    "dry": {"type":"bar","yTitle":"烘箱最大溫差 (°C)",
      "labels":["對流(常壓)","強制對流","真空","微波","紅外"],
      "datasets":[{"label":"內部最大溫差","data":[10,1,4,2,3],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["自由水","結合水","包埋水"],
      "items":[{"t":"表面、毛細水可流動","c":"自由水"},{"t":"最易蒸發","c":"自由水"},
        {"t":"以氫鍵依附 −OH／=O","c":"結合水"},{"t":"形成有序水合殼層","c":"結合水"},
        {"t":"陷在膠體/緻密基質","c":"包埋水"},{"t":"最難移除","c":"包埋水"}],
      "ok":"🎉 全對！自由水最好蒸、結合水靠氫鍵、包埋水最難去。",
      "tip":"提示：氫鍵依附＝結合水；卡在凝膠/油炸緻密結構＝包埋水。"},
    "g3": {"cats":["測重量變化","測體積/滴定量","測物理性質(間接)"],
      "items":[{"t":"強制對流烘箱","c":"測重量變化"},{"t":"微波乾燥","c":"測重量變化"},
        {"t":"甲苯蒸餾","c":"測體積/滴定量"},{"t":"Karl Fischer","c":"測體積/滴定量"},
        {"t":"折射率(°Brix)","c":"測物理性質(間接)"},{"t":"NIR 近紅外","c":"測物理性質(間接)"}],
      "ok":"🎉 正確！烘箱/微波測失重、蒸餾讀體積、KF 看滴定量、折射率與 NIR 是間接物性。",
      "tip":"提示：蒸餾讀水的體積、KF 讀試劑用量；折射率/NIR 測的是與水相關的物性。"}
  },
  "mcq": {
    "g2":[
      {"q":"哪一種烘箱的內部溫差最小、最精準？","o":["對流(常壓)烘箱","強制對流烘箱","玻璃門真空烘箱","沒有差別"],"a":1,
       "e":"強制對流有風扇強制循環，溫差通常 ≤1°C。"},
      {"q":"% 水分（濕基）的正確算式是？","o":["(乾重−濕重)/乾重×100","(濕重−乾重)/濕重×100","乾重/濕重×100","濕重/乾重×100"],"a":1,
       "e":"水重=濕重−乾重，再除以濕重。"},
      {"q":"高糖食品為何改用真空烘箱、且溫度 ≤70°C？","o":["乾得比較慢","避免梅納褐變與糖水解","因為比較便宜","為了多放樣品"],"a":1,
       "e":"減壓可低溫蒸水，降低高糖產品的分解誤差。"},
      {"q":"碳水化合物在高溫『分解生水』，會使結果如何？","o":["低估水分","高估水分","不影響","只影響固形物"],"a":1,
       "e":"分解釋出的水被算進去 → 高估水分含量。"}
    ],
    "g5":[
      {"q":"巧克力、油脂等低水分高糖/油樣品，最準的選擇？","o":["強制對流烘箱","Karl Fischer","折射率","冰點法"],"a":1,
       "e":"KF 不加熱、快速、對低水分食品最準，是首選。"},
      {"q":"香料含揮發性成分，官方建議用哪種方法？","o":["甲苯共沸蒸餾","高溫對流烘箱","比重計","微波"],"a":0,
       "e":"蒸餾熱分解少、直接量水，是香料(986.21)官方法。"},
      {"q":"穀物工廠要快速、非破壞地監測水分，選？","o":["甲苯蒸餾","NIR 近紅外","Karl Fischer","真空烘箱"],"a":1,
       "e":"NIR 快速非破壞、適合線上品管，但須先校正。"},
      {"q":"純糖漿/果汁(單一溶質液體)測固形物，最簡便？","o":["折射率(°Brix)","凱氏定氮","TGA","蒸餾"],"a":0,
       "e":"折射率/比重計快速便宜，適合單一溶質的液體固形物。"},
      {"q":"懷疑牛奶被加水稀釋，最佳偵測法？","o":["烘箱乾燥","NIR","冰點(冰點儀)","折射率"],"a":2,
       "e":"冰點是牛奶最穩定物性；加水使冰點上升，冰點儀可偵測。"}
    ]
  },
  "sort": {
    "g4":{"steps":["乾燥皿+玻纖蓋先烘乾，置乾燥器冷卻後精秤","快速秤入樣品(濕重)、蓋好",
       "放入烘箱於規定溫度/時間乾燥","取出移入乾燥器冷卻","精秤乾燥後的皿+樣品(乾重)","由(濕重−乾重)/濕重×100 算 % 水分"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！先備皿→秤濕重→烘乾→冷卻→秤乾重→計算。","tip":"提示：一定先把空皿烘乾秤重，最後才計算 % 水分。"}
  },
  "calc": {
    "g6":{"answer":80.65,"tol":0.5,
      "ok":"🎉 正確！扣皿後濕重 3.5898 g、乾重 0.6945 g，水=2.8953 g；2.8953/3.5898×100 = <b>80.65%</b> 水分（固形物 19.35%）。",
      "bad":"再算算：先各扣 1.0376 g → 濕重 3.5898 g、乾重 0.6945 g，水重 2.8953 g，再 ÷ 濕重 ×100。",
      "hint":"提示：濕重=4.6274−1.0376=3.5898 g；乾重=1.7321−1.0376=0.6945 g；水/濕重×100≈80.65%。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"meas"},{"k":"speed"},{"k":"app"}],
    "rows":[
      {"m":"強制對流烘箱","meas":"重量變化","speed":2,"app":"多種食品·官方法"},
      {"m":"真空烘箱","meas":"重量變化","speed":2,"app":"高糖/熱敏食品·官方法"},
      {"m":"微波乾燥","meas":"重量變化","speed":4,"app":"液體/起司·快速品管"},
      {"m":"紅外/鹵素乾燥","meas":"重量變化","speed":4,"app":"快速品管(單樣品)"},
      {"m":"甲苯蒸餾","meas":"水的體積","speed":2,"app":"香料·乾果(官方法)"},
      {"m":"Karl Fischer","meas":"滴定量(I₂)","speed":3,"app":"低水分高糖/油(最準)"},
      {"m":"折射率","meas":"折射率(°Brix)","speed":5,"app":"糖漿·果汁·乳(固形物)"},
      {"m":"NIR 近紅外","meas":"−OH 吸收","speed":5,"app":"穀物·乳品線上品管"}
    ]
  }
}

dc.build_html(
  {"title":"水分分析 Moisture Analysis · Nielsen Ch15","brand":"MOISTURE · CH15"},
  S, CFG, OUT)
