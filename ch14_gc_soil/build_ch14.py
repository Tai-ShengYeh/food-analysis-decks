# -*- coding: utf-8 -*-
"""Nielsen Ch14 Gas Chromatography (GC) — SOIL HTML deck. Uses ../soil_deck_common.py.
Run: python build_ch14.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
# GC 儀器流程示意：載氣→注射口→管柱/烘箱→偵測器→數據（仿 build_ch18 DUMAS_SVG 流程方塊）
GC_FLOW_SVG = """
<svg viewBox="0 0 620 240">
 <g font-size="13">
  <rect x="12" y="92" width="104" height="62" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="64" y="116" text-anchor="middle" class="lblb">載氣鋼瓶</text>
  <text x="64" y="136" text-anchor="middle" class="lbl">He / H₂ / N₂</text>
  <rect x="152" y="92" width="104" height="62" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="204" y="112" text-anchor="middle" class="lblb">注射口</text>
  <text x="204" y="130" text-anchor="middle" class="lbl">汽化·分流</text>
  <text x="204" y="146" text-anchor="middle" class="lbl">250°C</text>
  <rect x="292" y="80" width="120" height="86" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="352" y="104" text-anchor="middle" class="lblb">烘箱 + 管柱</text>
  <text x="352" y="124" text-anchor="middle" class="lbl">毛細管柱</text>
  <text x="352" y="142" text-anchor="middle" class="lbl">溫度程式</text>
  <path d="M312 150 q12 -10 24 0 t24 0 t24 0" fill="none" stroke="#1f6feb" stroke-width="2"/>
  <rect x="448" y="92" width="104" height="62" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="500" y="116" text-anchor="middle" class="lblb">偵測器</text>
  <text x="500" y="136" text-anchor="middle" class="lbl">FID/TCD/MS</text>
  <rect x="556" y="100" width="52" height="46" rx="8" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="582" y="120" text-anchor="middle" class="lbl">數據</text>
  <text x="582" y="136" text-anchor="middle" class="lbl">層析圖</text>
  <g stroke="#8493ad" stroke-width="2.5" fill="none" marker-end="url(#arg)">
   <path d="M116 123 h34"/><path d="M256 123 h34"/><path d="M412 123 h34"/><path d="M552 123 h2"/></g>
  <defs><marker id="arg" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#8493ad"/></marker></defs>
  <text x="310" y="40" text-anchor="middle" class="lblb" font-size="15">氣相層析儀 (GC) 五大組件</text>
  <text x="310" y="58" text-anchor="middle" class="lbl">載氣 → 注射 → 分離 → 偵測 → 數據</text>
 </g>
</svg>"""

# 分流 / 不分流 注射示意
SPLIT_SVG = """
<svg viewBox="0 0 560 240">
 <g font-size="13">
  <rect x="220" y="14" width="120" height="34" rx="8" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="280" y="36" text-anchor="middle" class="lblb">注射口 250°C</text>
  <path d="M280 48 v34" stroke="#8493ad" stroke-width="2.5" marker-end="url(#ars)"/>
  <rect x="40" y="96" width="220" height="120" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="150" y="120" text-anchor="middle" class="lblb">分流 Split</text>
  <text x="150" y="142" text-anchor="middle" class="lbl">分流閥開，1:50~1:100</text>
  <text x="150" y="162" text-anchor="middle" class="lbl">僅少量上管柱→尖峰</text>
  <text x="150" y="184" text-anchor="middle" class="lbl">適高濃度樣品</text>
  <text x="150" y="204" text-anchor="middle" class="lbl">多數樣品排出分流口</text>
  <rect x="300" y="96" width="220" height="120" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="410" y="120" text-anchor="middle" class="lblb">不分流 Splitless</text>
  <text x="410" y="142" text-anchor="middle" class="lbl">分流閥關，全量上管柱</text>
  <text x="410" y="162" text-anchor="middle" class="lbl">靈敏度高→微量分析</text>
  <text x="410" y="184" text-anchor="middle" class="lbl">起始柱溫低於溶劑沸點</text>
  <text x="410" y="204" text-anchor="middle" class="lbl">利用溶劑效應聚焦</text>
  <defs><marker id="ars" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#8493ad"/></marker></defs>
 </g>
</svg>"""

# 決策樹：選偵測器 / 管柱
DTREE_SVG = """
<svg viewBox="0 0 980 360">
 <rect x="380" y="14" width="220" height="56" rx="12" fill="#1f6feb"/>
 <text x="490" y="40" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">你要測什麼？</text>
 <text x="490" y="60" text-anchor="middle" fill="#cfe0f6" font-size="12">選 GC 偵測器 / 管柱</text>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M420 70 C 200 110,130 120,120 150"/><path d="M470 70 C 400 120,380 120,375 150"/>
  <path d="M510 70 C 590 120,610 120,625 150"/><path d="M560 70 C 800 110,860 120,875 150"/></g>
 <g font-size="14" font-weight="800">
  <rect x="30" y="150" width="190" height="120" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="125" y="178" text-anchor="middle" fill="#15233f">一般有機物?</text>
  <text x="125" y="206" text-anchor="middle" fill="#d9822b" font-size="16">FID</text>
  <text x="125" y="232" text-anchor="middle" fill="#48597a" font-size="12">靈敏、線性廣</text>
  <text x="125" y="252" text-anchor="middle" fill="#48597a" font-size="12">脂肪酸·風味通用</text>
  <rect x="280" y="150" width="190" height="120" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="375" y="178" text-anchor="middle" fill="#15233f">永久氣體/水?</text>
  <text x="375" y="206" text-anchor="middle" fill="#1f6feb" font-size="16">TCD</text>
  <text x="375" y="232" text-anchor="middle" fill="#48597a" font-size="12">通用、非破壞</text>
  <text x="375" y="252" text-anchor="middle" fill="#48597a" font-size="12">CO₂·O₂·N₂ 包裝氣體</text>
  <rect x="530" y="150" width="190" height="120" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="625" y="178" text-anchor="middle" fill="#15233f">農藥/含鹵?</text>
  <text x="625" y="206" text-anchor="middle" fill="#1f9d6b" font-size="16">ECD</text>
  <text x="625" y="232" text-anchor="middle" fill="#48597a" font-size="12">極靈敏(pg)</text>
  <text x="625" y="252" text-anchor="middle" fill="#48597a" font-size="12">PCB·殘留農藥</text>
  <rect x="780" y="150" width="190" height="120" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="875" y="178" text-anchor="middle" fill="#15233f">未知物鑑定?</text>
  <text x="875" y="206" text-anchor="middle" fill="#15233f" font-size="16">MS</text>
  <text x="875" y="232" text-anchor="middle" fill="#48597a" font-size="12">質譜=指紋</text>
  <text x="875" y="252" text-anchor="middle" fill="#48597a" font-size="12">配 LRI 確認身分</text>
 </g>
</svg>"""

# ---------------- 引起動機 ----------------
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 14",
    "氣相<span style='color:var(--accent-2)'>層析</span>", "Gas Chromatography (GC)",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>樣品前處理 · 管柱 · 載氣 · 注射 · 偵測器 · 定性定量",
    ["FID","TCD","ECD","MS","SPME","毛細管柱"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">咖啡的香氣有上百種分子，<span class="hi">怎麼一一分開？</span></div>
  <p class="subtitle" style="max-width:800px;margin:22px auto 0">食品香氣、脂肪酸、殘留溶劑都是<strong>揮發性</strong>小分子的混合物。<br>
  氣相層析 (GC) 能把它們<strong>逐一分離</strong>，再用偵測器一個個量出來。</p>
  <div style="margin-top:24px"><span class="pill">香氣分析</span><span class="pill">脂肪酸組成</span>
  <span class="pill">殘留農藥</span><span class="pill">包裝溶劑</span><span class="pill">攙假檢測</span></div></div>""")

add(MOT, dc.kt("14.1 為什麼用 GC", "GC 適合分析什麼") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("💨","揮發性","樣品要能氣化——常溫或加熱下成為氣體") +
    dc.card("🔥","熱穩定","在高溫注射口/管柱中不會分解","a") +
    dc.card("🍳","食品應用","脂肪酸、膽固醇、風味、溶劑、農藥、PCB","g") +
    dc.card("🧪","不合適的","糖、胺基酸、維生素 → 需先衍生化或改用 HPLC","b") + '</div>')

add(MOT, dc.kt("14.1 核心原理", "兩種力量<span class='hi'>共同</span>分離") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li><strong>移動相</strong>：載氣 (He/H₂/N₂) 帶著樣品前進</li>" +
    "<li><strong>固定相</strong>：管柱內壁的液膜，與分析物作用</li>" +
    "<li>與固定相作用越強 → 滯留越久、越晚出峰</li>" +
    "<li>GC 還額外靠<span class='em'>沸點</span>分離 → 解析力極強</li>" +
    '</ul></div><div class="note"><strong>關鍵：分配 (partition) 是 GC 的主力。</strong><br>' +
    "依「與固定相親和力 + 沸點」差異，讓各成分在不同時間流出 → 得到層析圖。</div></div>")

add(MOT, dc.chart_inner("chrom", "層析圖長<span class='hi'>什麼樣子</span>？",
    "示意層析圖：x = 滯留時間 (min)，y = 訊號。峰位 = 定性，峰面積 = 定量。",
    kicker="14.4 層析圖"), ' data-chart="chrom"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">核心命題</div>
  <div class="hook" style="font-size:clamp(1.7rem,4vw,3rem)">先<span class="hi">分離</span>，再<span class="hi">偵測</span></div>
  <p class="lead" style="max-width:820px;margin:20px auto 0">一台 GC = 管柱負責<strong>分離</strong>、偵測器負責<strong>感應</strong>。<br>
  五大組件：<strong>載氣 → 注射口 → 烘箱/管柱 → 偵測器 → 數據</strong>。</p>
  <div class="eq" style="max-width:620px;margin:24px auto 0">峰位置 → 定性 (是什麼)<br>
  <span style="font-size:.8em;color:var(--ink-2)">峰面積 → 定量 (有多少)</span></div></div>""")

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","偵測器測什麼", 6,
    "把 6 個分析物丟給最合適的偵測器。分到三類。"), ' data-game="g1"')

# ---------------- 維持注意 ----------------
add(ATT, dc.kt("儀器全覽", "GC 五大組件") +
    '<div class="svgwrap" style="margin-top:10px">' + GC_FLOW_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:12px">記錄必備：注射方式、管柱規格、各區溫度、載氣種類與流速、偵測器。</p>')

add(ATT, dc.kt("14.2 樣品前處理", "為什麼不能直接打進去") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li>注射口高溫會把<strong>非揮發物分解</strong> → 產生假峰</li>" +
    "<li>目標物常需先<strong>分離濃縮</strong>到可偵測濃度</li>" +
    "<li>研磨/均質可能讓酵素或微生物改變組成</li>" +
    "<li>要先<strong>滅活、冷凍、乾燥</strong>保存樣品</li></ul></div>" +
    '<div class="note"><strong>前處理決定成敗。</strong><br>' +
    "分離方法選錯或操作不當，後面再好的 GC 也救不回來。</div></div>")

add(ATT, dc.kt("14.2.2 揮發物分離", "把香氣從食物裡<span class='hi'>抓出來</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🫧","頂空 Headspace","靜態(直接取上方氣體)/動態(吹掃捕集 Purge&Trap)，低沸點物快速","b") +
    dc.card("💧","蒸餾","水蒸氣蒸餾、同步蒸餾萃取 (SDE/Likens–Nickerson)；高溫易生假峰","a") +
    dc.card("🧴","溶劑萃取","二氯甲烷/乙醚萃取；不可含脂肪；SAFE 真空低溫去非揮發物","g") +
    dc.card("🧵","固相萃取","SPE / SPME 纖維 / SBSE 攪拌子；少溶劑、可自動化","b") + '</div>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","前處理與注射即時測驗", 4), ' data-game="g2"')

add(ATT, dc.kt("14.2.3 衍生化", "讓「不揮發」變「揮發」") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧬","為何要做","糖、胺基酸太不揮發或熱不穩；酚、酸太極性 → 出峰差","b") +
    dc.card("🔧","三大常用","矽烷化(糖/膽固醇)、酯化(脂肪酸→FAME)、肟化(醛酮)","a") +
    '</div><div class="note" style="margin-top:18px">脂肪酸常用 <strong>BF₃/甲醇酯化</strong>成脂肪酸甲酯 (FAME) 再上 GC；' +
    "農藥、香氣、PCB 本身夠揮發穩定，<strong>不必</strong>衍生化。</div>")

add(ATT, dc.kt("14.3.2 注射模式", "分流 vs 不分流") +
    '<div class="svgwrap" style="margin-top:10px">' + SPLIT_SVG + '</div>' +
    '<div class="note" style="margin-top:14px">注射口溫度約比柱溫上限高 <strong>20°C</strong>(常 250°C)。' +
    "高濃度用<strong>分流</strong>(尖峰)；微量用<strong>不分流</strong>(高靈敏)。另有 PTV、管柱內注射、熱脫附。</div>")

add(ATT, dc.kt("14.3.4 管柱", "填充柱 vs 毛細管柱") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧱","填充柱 Packed","不鏽鋼/玻璃，2–3 m；矽藻土載體塗液相 1–10%；效率低，幾乎被淘汰","b") +
    dc.card("🧵","毛細管柱 Capillary","熔融石英中空管 5–100 m；內徑 0.1–0.53 mm；液膜鍵結交聯，高解析","a") +
    '</div><div class="note" style="margin-top:18px">最通用：<strong>5% 苯基-95% 甲基聚矽氧烷</strong>(DB-5)，' +
    "−60~325°C 範圍廣；極性物用 WAX(聚乙二醇)；trans 脂肪酸用氰丙基柱 (SP-2560)。</div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","元件功能配對", 6,
    "每個 GC 元件負責什麼？把 6 個元件配到三大功能。"), ' data-game="g3"')

add(ATT, dc.kt("14.3.1 載氣", "三種載氣怎麼選") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🎈","N₂ 氮氣","HETP 最低(最有效率)，但最佳流速很慢 → 分析太久","b") +
    dc.card("🟢","He 氦氣","流速 40 cm/s 仍維持好解析；最常用、安全","a") +
    dc.card("⚡","H₂ 氫氣","曲線最平坦、分析最快；可燃但實務少出事","g") +
    '</div><div class="note" style="margin-top:18px">載氣須高純度，並加<strong>水分/氧氣/碳氫捕集器</strong>。' +
    "權衡速度與安全，He/H₂ 常勝過理論最佳的 N₂。</div>")

add(ATT, dc.chart_inner("vand", "載氣與流速：<span class='hi'>van Deemter</span>",
    "示意 van Deemter 曲線：HETP 越低分離越好。N₂ 谷底最低但落在低流速；He/H₂ 較平坦適合快速分析。",
    kicker="14.4.2 分離效率", height="52vh"), ' data-chart="vand"')

add(ATT, dc.kt("14.3.5 偵測器", "四大常用偵測器") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🔥","FID 火焰離子化","燒有機物產生離子；靈敏、線性最廣；食品最常用主力","b") +
    dc.card("🌡️","TCD 熱導","測熱導差異；通用(含水/氣體)、非破壞；靈敏度低","a") +
    dc.card("⚛️","ECD 電子捕獲","放射源；對含鹵/農藥極靈敏(pg)；線性窄、易飽和","g") +
    dc.card("🔬","MS 質譜","碎片離子=指紋；可鑑定未知物，亦作選擇性偵測","b") + '</div>')

add(ATT, dc.kt("偵測器專長", "選擇性 vs 靈敏度") +
    '<div class="grid3" style="margin-top:22px">' +
    dc.card("🟣","FPD / PFPD","燒後測特定波長光，專測<strong>硫 S / 磷 P</strong>；風味硫化物、有機磷農藥","b") +
    dc.card("🔆","PID 光離子化","UV 光游離，靈敏、非破壞、可調選擇性；風味嗅聞","a") +
    dc.card("🟢","NPD 熱離子","改良 FID，專測<strong>氮 N / 磷 P</strong>；亞硝胺、胺、農藥","g") + '</div>')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","GC 分析流程排序", 7,
    "用 ▲▼ 把一次完整的 GC 分析排成正確順序（7 步）。"), ' data-game="g4"')

add(ATT, dc.chart_inner("sens", "偵測器<span class='hi'>靈敏度</span>大不同",
    "資料：Table 14.5 偵測下限 (pg，數值越小越靈敏)。ECD/FPD 屬痕量等級。",
    kicker="14.3.5 偵測下限", height="52vh"), ' data-chart="sens"')

add(ATT, dc.kt("14.4.2 分離效率", "Van Deemter 三項") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">HETP = A + B/u + C·u</div>' +
    '<div><ul class="clean"><li><strong>A 渦流擴散</strong>：流路不均(毛細管很小)</li>' +
    "<li><strong>B/u 縱向擴散</strong>：流速太慢時變大</li>" +
    "<li><strong>C·u 質傳阻抗</strong>：流速太快來不及平衡</li>" +
    "<li>HETP 越小越好；存在<span class='em'>最佳流速</span></li></ul></div></div>" +
    '<div class="note" style="margin-top:16px">毛細管柱每公尺約 3000–4000 塔板，總數可達 10⁵~5×10⁵；解析力遠勝填充柱。</div>')

add(ATT, dc.kt("14.4 取捨金字塔", "四個性質<span class='hi'>不可兼得</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🎯","解析 Resolution","細內徑、薄膜、長柱、最佳流速 → 分得開","b") +
    dc.card("📦","容量 Capacity","大內徑、厚膜 → 載量大但解析差","a") +
    dc.card("⚡","速度 Speed","薄膜、高流速、短柱 → 快但犧牲解析","g") +
    dc.card("🔍","靈敏度 Sensitivity","偵測器與注射方式決定","b") +
    '</div><div class="note" style="margin-top:16px">優化其一必犧牲其他——依分析需求折衷選柱與條件。</div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選偵測器/管柱", 5), ' data-game="g5"')

# ---------------- 喚起行動 ----------------
add(ACT, dc.cmp_inner("一張表選偵測器（點欄位排序）",
    [{"k":"d","t":"s","label":"偵測器"},{"k":"meas","t":"s","label":"專測對象"},
     {"k":"sens","t":"n","label":"靈敏度","star":True},{"k":"app","t":"s","label":"主要應用"}],
    "靈敏度：★ 越多越靈敏（偵測下限越低）。整合自 Table 14.5。", kicker="14.3.5 偵測器比較"), ' data-game="cmp"')

add(ACT, dc.kt("方法選擇", "跟著決策樹選偵測器") +
    '<div class="svgwrap" style="margin-top:10px">' + DTREE_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:14px">下一頁實戰：用滯留時間算未知物的線性滯留指標 →</p>')

add(ACT, dc.kt("14.5.2 定性", "用滯留指標<span class='hi'>確認身分</span>") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">LRI = 100·n + 100 × ' +
    '<span class="frac"><b>t<sub>未知</sub> − t<sub>n</sub></b><span>t<sub>n+1</sub> − t<sub>n</sub></span></span></div>' +
    '<div><ul class="clean"><li>加入一系列正<strong>烷類 (C5–C25)</strong>當標尺</li>' +
    "<li>n = 較早出峰那支烷類的碳數</li>" +
    "<li>LRI 與柱相有關，但<strong>不受溫度程式影響</strong></li>" +
    "<li>配合 MS，LRI 差 ±10 內即可確認</li></ul></div></div>" +
    '<div class="note" style="margin-top:14px">例：恰在 C7、C8 正中間出峰的化合物 → LRI = 750。</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關",
    "某香氣化合物在 C8 與 C9 之間出峰：t(C8)=8.00 min、t(C9)=10.00 min、t(未知)=8.50 min。"
    "求其<strong>線性滯留指標 LRI</strong>。", unit="LRI"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>GC 專測<strong>揮發、熱穩定</strong>的小分子；不合適者先衍生化</li>" +
    "<li>前處理(頂空/蒸餾/萃取/SPME)<strong>決定成敗</strong></li>" +
    "<li>毛細管柱解析遠勝填充柱；DB-5 最通用</li></ul>" +
    '<ul class="clean"><li>載氣 He/H₂ 比理論最佳的 N₂ 更實用(快)</li>' +
    "<li>偵測器：FID 通用、TCD 測氣體、ECD 測農藥、MS 鑑定；定性靠 LRI、定量靠內標</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說出 GC 適合分析哪類化合物(揮發、熱穩定)",
     "說出 GC 五大組件與訊號流向",
     "比較頂空、蒸餾、溶劑萃取、SPME 的適用時機",
     "解釋為何糖/脂肪酸要衍生化",
     "區分分流與不分流注射、填充柱與毛細管柱",
     "依需求選對偵測器(FID/TCD/ECD/MS)",
     "由滯留時間算出線性滯留指標 LRI"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把氣相層析<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions、Practice Problems<br>"
    "🔜 銜接章節：<strong>液相層析 HPLC (Ch13)</strong>、<strong>質譜法 (Ch11)</strong><br>"
    "🧪 思考：你的樣品揮發嗎？需要衍生化嗎？該選哪種偵測器？",
    ["FID","TCD","ECD","MS","SPME","LRI"]), ' data-cover="1"')

# ---------------- CFG ----------------
CFG = {
  "charts": {
    "chrom": {"type":"line","yTitle":"訊號 (a.u.)","zero":True,
      "labels":["0","1","2","3","4","5","6","7","8","9","10","11","12"],
      "datasets":[{"label":"層析訊號","data":[2,3,28,6,4,15,5,3,40,7,4,22,3],"color":"#1f6feb"}]},
    "vand": {"type":"line","yTitle":"HETP (mm)","zero":True,
      "labels":["10","20","30","40","50","60","70"],
      "datasets":[
        {"label":"N₂ 氮","data":[0.25,0.40,0.58,0.78,1.00,1.24,1.50],"color":"#1f6feb"},
        {"label":"He 氦","data":[0.50,0.40,0.36,0.35,0.38,0.43,0.50],"color":"#d9822b"},
        {"label":"H₂ 氫","data":[0.48,0.38,0.34,0.33,0.34,0.36,0.39],"color":"#1f9d6b"}]},
    "sens": {"type":"bar","yTitle":"偵測下限 (pg，越小越靈敏)",
      "labels":["TCD","FID","PID","FPD(P)","FPD(S)","ECD"],
      "datasets":[{"label":"偵測下限 (pg)","data":[400,50,5,0.9,2,0.5],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["FID(一般有機物)","TCD(永久氣體/水)","ECD(含鹵/農藥)"],
      "items":[{"t":"脂肪酸甲酯 FAME","c":"FID(一般有機物)"},{"t":"風味醛酮","c":"FID(一般有機物)"},
        {"t":"包裝頂空 O₂/CO₂","c":"TCD(永久氣體/水)"},{"t":"水分","c":"TCD(永久氣體/水)"},
        {"t":"殘留農藥","c":"ECD(含鹵/農藥)"},{"t":"PCB 多氯聯苯","c":"ECD(含鹵/農藥)"}],
      "ok":"🎉 全對！FID 測一般有機物、TCD 測氣體/水、ECD 對含鹵農藥極靈敏。",
      "tip":"提示：含鹵或農藥殘留→ECD；永久氣體與水→TCD；其餘有機物→FID。"},
    "g3": {"cats":["移動相/輸送","樣品導入","分離/偵測"],
      "items":[{"t":"載氣鋼瓶","c":"移動相/輸送"},{"t":"壓力調節器/捕集器","c":"移動相/輸送"},
        {"t":"注射口(汽化分流)","c":"樣品導入"},{"t":"自動進樣器","c":"樣品導入"},
        {"t":"毛細管柱+烘箱","c":"分離/偵測"},{"t":"FID/TCD 偵測器","c":"分離/偵測"}],
      "ok":"🎉 正確！載氣與調節器負責輸送、注射口/進樣器負責導入、管柱與偵測器負責分離與感應。",
      "tip":"提示：先想這個元件在『載氣→注射→分離→偵測』哪一段。"}
  },
  "mcq": {
    "g2":[
      {"q":"為什麼食品通常不能直接打進 GC？","o":["太便宜","非揮發物在注射口分解產生假峰","顏色太深","太冷"],"a":1,
       "e":"高溫注射口會裂解非揮發成分，形成假峰並污染管柱。"},
      {"q":"動態頂空(Purge & Trap)用吸附阱的主要優點？","o":["產生大量水","得到不含水的揮發物且可自動化","需要強酸","破壞樣品"],"a":1,
       "e":"吸附阱(如 Tenax)對水親和力低，得無水揮發物且易自動化。"},
      {"q":"分流(split)注射相較不分流，特性是？","o":["靈敏度最高","僅少量上管柱、峰較尖、適高濃度","全量上管柱","只能測氣體"],"a":1,
       "e":"分流閥開、多數樣品排出，少量上柱得尖峰，適高濃度樣品。"},
      {"q":"脂肪酸為何常要先衍生化才上 GC？","o":["增加顏色","太極性/揮發性差，酯化成 FAME 改善層析","降低成本","讓它變紅"],"a":1,
       "e":"游離脂肪酸極性高、出峰差，酯化成脂肪酸甲酯後揮發性與分離大幅改善。"}
    ],
    "g5":[
      {"q":"要分析食品包裝頂空的 O₂、CO₂、N₂，選哪個偵測器？","o":["FID","TCD","ECD","FPD"],"a":1,
       "e":"永久氣體與水 FID 沒反應，TCD 通用且非破壞，最合適。"},
      {"q":"分析蔬果中痕量含氯殘留農藥，最佳偵測器？","o":["TCD","FID","ECD","PID"],"a":2,
       "e":"ECD 對含鹵化合物極靈敏(0.05–1 pg)，是農藥/PCB 首選。"},
      {"q":"要鑑定未知香氣化合物的身分，最該用？","o":["TCD","ECD","MS 質譜","FPD"],"a":2,
       "e":"MS 提供碎片指紋，配合 LRI 可確認未知物身分。"},
      {"q":"分離極性的游離脂肪酸與醇類，該選哪種管柱？","o":["100% 甲基聚矽氧烷","WAX(聚乙二醇)極性柱","非極性 DB-1","填充柱"],"a":1,
       "e":"極性分析物需極性柱(如 WAX/FFAP)才有好分離。"},
      {"q":"想縮短分析時間又維持解析，載氣多選？","o":["N₂(谷底在低流速)","He 或 H₂","空氣","CO₂"],"a":1,
       "e":"He/H₂ 在高流速仍維持低 HETP，分析快；N₂ 最佳流速太慢。"}
    ]
  },
  "sort": {
    "g4":{"steps":["樣品前處理：研磨/均質並滅活","分離濃縮揮發物(頂空/萃取/SPME)",
       "(必要時)衍生化使分析物揮發穩定","注射口汽化、分流/不分流導入管柱",
       "烘箱溫度程式，毛細管柱分離","偵測器(FID/MS)產生訊號","由峰位定性、峰面積定量"],
       "shuffle":[3,0,6,1,4,2,5],
       "ok":"🎉 順序正確！前處理→分離→(衍生化)→注射→分離→偵測→定性定量。",
       "tip":"提示：一定先把揮發物從食物中分離出來，最後才讀峰做定性定量。"}
  },
  "calc": {
    "g6":{"answer":825,"tol":1,
      "ok":"🎉 正確！LRI = 100×8 + 100×(8.50−8.00)/(10.00−8.00) = 800 + 100×0.25 = <b>825</b>。",
      "bad":"再算算：LRI = 100·n + 100×(t未知−t_n)/(t_{n+1}−t_n)，n=8(C8)，分數=(8.50−8.00)/(10.00−8.00)=0.25。",
      "hint":"提示：n=8；分數 = 0.50/2.00 = 0.25；LRI = 800 + 25 = 825。"}
  },
  "cmp": {
    "cols":[{"k":"d"},{"k":"meas"},{"k":"sens"},{"k":"app"}],
    "rows":[
      {"d":"TCD 熱導","meas":"幾乎全部(含水/氣體)","sens":2,"app":"永久氣體·包裝氣體·非破壞"},
      {"d":"FID 火焰離子","meas":"多數有機物","sens":4,"app":"脂肪酸·風味·通用主力"},
      {"d":"ECD 電子捕獲","meas":"含鹵/硝基/雙鍵","sens":5,"app":"殘留農藥·PCB"},
      {"d":"FPD 火焰光度","meas":"硫 S / 磷 P","sens":4,"app":"有機磷農藥·硫化物風味"},
      {"d":"PID 光離子化","meas":"視游離能","sens":4,"app":"風味·嗅聞·非破壞"},
      {"d":"NPD 熱離子","meas":"氮 N / 磷 P","sens":4,"app":"亞硝胺·胺·農藥"},
      {"d":"MS 質譜","meas":"碎片離子指紋","sens":4,"app":"未知物鑑定·選擇性偵測"}
    ]
  }
}

dc.build_html(
  {"title":"氣相層析 GC · Nielsen Ch14","brand":"GC · CH14"},
  S, CFG, OUT)
