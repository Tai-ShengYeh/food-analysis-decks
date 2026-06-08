# -*- coding: utf-8 -*-
"""Nielsen Ch12 Basic Principles of Chromatography — SOIL HTML deck.
Uses ../soil_deck_common.py.  Run: python build_ch12.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
COLUMN_SVG = """
<svg viewBox="0 0 300 400">
 <defs><linearGradient id="gc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eaf2ff"/><stop offset="1" stop-color="#cfe0f6"/></linearGradient></defs>
 <rect x="118" y="18" width="64" height="22" rx="6" fill="#48597a"/>
 <text x="150" y="33" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">注入樣品</text>
 <path d="M150 40 v18" stroke="#1f6feb" stroke-width="3"/>
 <rect x="110" y="58" width="80" height="270" rx="14" fill="url(#gc)" stroke="#1f6feb" stroke-width="3"/>
 <text x="150" y="78" text-anchor="middle" class="lblb">管柱 Column</text>
 <text x="150" y="96" text-anchor="middle" class="lbl">固定相</text>
 <circle cx="135" cy="125" r="7" fill="#d9822b"/><circle cx="160" cy="135" r="7" fill="#d9822b"/>
 <circle cx="148" cy="180" r="7" fill="#1f9d6b"/><circle cx="166" cy="195" r="7" fill="#1f9d6b"/>
 <circle cx="138" cy="250" r="7" fill="#8b5cf6"/>
 <text x="232" y="100" class="lbl">移動相</text><text x="232" y="118" class="lbl">↓ 流洗</text>
 <text x="232" y="190" class="lbl">分配快</text><text x="232" y="208" class="lbl">→ 先出</text>
 <path d="M150 328 v22" stroke="#1f6feb" stroke-width="3"/>
 <rect x="108" y="350" width="84" height="26" rx="7" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
 <text x="150" y="368" text-anchor="middle" class="lblb" font-size="12">偵測器 → 訊號</text>
 <text x="150" y="394" text-anchor="middle" class="lbl">管柱層析 Column chromatography</text>
</svg>"""

PEAK_SVG = """
<svg viewBox="0 0 560 250">
 <g font-size="13">
  <line x1="40" y1="200" x2="540" y2="200" stroke="#8493ad" stroke-width="2"/>
  <line x1="40" y1="200" x2="40" y2="30" stroke="#8493ad" stroke-width="2"/>
  <text x="20" y="120" text-anchor="middle" class="lbl" transform="rotate(-90 20 120)">偵測訊號</text>
  <text x="290" y="232" text-anchor="middle" class="lbl">時間 (或體積)</text>
  <path d="M40 200 L160 198 Q200 198 215 120 Q230 198 270 198" fill="none" stroke="#1f6feb" stroke-width="2.6"/>
  <path d="M270 198 Q330 198 350 70 Q372 198 460 198" fill="none" stroke="#d9822b" stroke-width="2.6"/>
  <line x1="215" y1="120" x2="215" y2="200" stroke="#1f6feb" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="350" y1="70" x2="350" y2="200" stroke="#d9822b" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="215" y1="48" x2="350" y2="48" stroke="#48597a" stroke-width="1.4" marker-start="url(#a2)" marker-end="url(#a2)"/>
  <text x="282" y="40" text-anchor="middle" class="lblb">Δt</text>
  <text x="215" y="216" text-anchor="middle" class="lbl" fill="#1f6feb">t_R1</text>
  <text x="350" y="216" text-anchor="middle" class="lbl" fill="#d9822b">t_R2</text>
  <text x="190" y="186" text-anchor="middle" class="lbl">w₁</text>
  <text x="405" y="186" text-anchor="middle" class="lbl">w₂</text>
  <defs><marker id="a2" markerWidth="9" markerHeight="9" refX="4" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#48597a"/></marker></defs>
  <text x="290" y="20" text-anchor="middle" class="lblb" font-size="15">層析峰與解析度 Rs = 2Δt / (w₁+w₂)</text>
 </g>
</svg>"""

FAMILY_SVG = """
<svg viewBox="0 0 980 320">
 <rect x="400" y="14" width="180" height="48" rx="10" fill="#1f6feb"/>
 <text x="490" y="44" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">層析 Chromatography</text>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M460 62 C 300 90,210 95,200 120"/><path d="M490 62 v58"/>
  <path d="M520 62 C 680 90,770 95,780 120"/></g>
 <g font-size="14" font-weight="800">
  <rect x="110" y="120" width="180" height="56" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="200" y="146" text-anchor="middle" fill="#15233f">氣相層析 GC</text>
  <text x="200" y="166" text-anchor="middle" class="lbl">移動相＝氣體</text>
  <rect x="400" y="120" width="180" height="56" rx="10" fill="#eef4ec" stroke="#1f9d6b" stroke-width="2"/>
  <text x="490" y="146" text-anchor="middle" fill="#15233f">超臨界流體 SFC</text>
  <text x="490" y="166" text-anchor="middle" class="lbl">移動相＝超臨界流體</text>
  <rect x="690" y="120" width="180" height="56" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="780" y="146" text-anchor="middle" fill="#15233f">液相層析 LC</text>
  <text x="780" y="166" text-anchor="middle" class="lbl">移動相＝液體</text>
 </g>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M740 176 C 640 205,600 210,590 235"/><path d="M780 176 v59"/>
  <path d="M820 176 C 900 205,910 210,905 235"/></g>
 <g font-size="13" font-weight="700">
  <rect x="500" y="235" width="180" height="44" rx="9" fill="#f6f9fd" stroke="#48597a" stroke-width="1.6"/>
  <text x="590" y="262" text-anchor="middle" fill="#15233f">紙層析 Paper</text>
  <rect x="690" y="235" width="180" height="44" rx="9" fill="#f6f9fd" stroke="#48597a" stroke-width="1.6"/>
  <text x="780" y="262" text-anchor="middle" fill="#15233f">薄層 TLC</text>
  <rect x="816" y="235" width="150" height="44" rx="9" fill="#f6f9fd" stroke="#48597a" stroke-width="1.6"/>
  <text x="891" y="262" text-anchor="middle" fill="#15233f">管柱 Column</text>
 </g>
</svg>"""

DTREE_SVG = """
<svg viewBox="0 0 980 360">
 <rect x="380" y="14" width="220" height="56" rx="12" fill="#1f6feb"/>
 <text x="490" y="40" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">樣品有什麼特性？</text>
 <text x="490" y="60" text-anchor="middle" fill="#cfe0f6" font-size="12">依分子量與性質選分離模式</text>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M420 70 C 200 110,130 120,120 150"/><path d="M470 70 C 400 120,380 120,375 150"/>
  <path d="M510 70 C 590 120,610 120,625 150"/><path d="M560 70 C 800 110,860 120,875 150"/></g>
 <g font-size="14" font-weight="800">
  <rect x="30" y="150" width="190" height="120" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="125" y="178" text-anchor="middle" fill="#15233f">小分子·非極性?</text>
  <text x="125" y="206" text-anchor="middle" fill="#d9822b" font-size="15">正相 (silica)</text>
  <text x="125" y="232" text-anchor="middle" fill="#48597a" font-size="12">極性固定相</text>
  <text x="125" y="252" text-anchor="middle" fill="#48597a" font-size="12">非極性先出</text>
  <rect x="280" y="150" width="190" height="120" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="375" y="178" text-anchor="middle" fill="#15233f">小分子·水溶?</text>
  <text x="375" y="206" text-anchor="middle" fill="#1f6feb" font-size="15">逆相 RP</text>
  <text x="375" y="232" text-anchor="middle" fill="#48597a" font-size="12">非極性固定相</text>
  <text x="375" y="252" text-anchor="middle" fill="#48597a" font-size="12">食品分析最常用</text>
  <rect x="530" y="150" width="190" height="120" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="625" y="178" text-anchor="middle" fill="#15233f">帶電荷離子?</text>
  <text x="625" y="206" text-anchor="middle" fill="#1f9d6b" font-size="15">離子交換 IEC</text>
  <text x="625" y="232" text-anchor="middle" fill="#48597a" font-size="12">靜電作用</text>
  <text x="625" y="252" text-anchor="middle" fill="#48597a" font-size="12">調 pH / 鹽濃度溶離</text>
  <rect x="780" y="150" width="190" height="120" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="875" y="178" text-anchor="middle" fill="#15233f">大分子·測 MW?</text>
  <text x="875" y="206" text-anchor="middle" fill="#15233f" font-size="15">size 排阻 SEC</text>
  <text x="875" y="232" text-anchor="middle" fill="#48597a" font-size="12">依分子大小分離</text>
  <text x="875" y="252" text-anchor="middle" fill="#48597a" font-size="12">大分子先出</text>
 </g>
</svg>"""

# ---------------- 引起動機 ----------------
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 12",
    "層析<span style='color:var(--accent-2)'>原理</span>", "Basic Principles of Chromatography",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>萃取 · 移動相/固定相 · 分配係數 · 七大分離模式 · 解析度",
    ["Extraction","Partition K","GC/LC/SFC","7 modes","Resolution"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">一杯混合液裡的成分，<span class="hi">怎麼一個一個分開？</span></div>
  <p class="subtitle" style="max-width:780px;margin:22px auto 0">食品裡常是數十種成分的混合物。要定性、定量，<br>
  第一步往往是——把它們<strong>分離 (separation)</strong> 出來。</p>
  <div style="margin-top:24px"><span class="pill">色素分離</span><span class="pill">胺基酸</span>
  <span class="pill">脂溶性維生素</span><span class="pill">多酚</span><span class="pill">糖類</span></div></div>""")

add(MOT, dc.kt("12.1 為什麼重要", "層析：分析科學的基石") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("🌈","分離混合物","把複雜樣品中的各成分逐一分開，是定性/定量的前提") +
    dc.card("🔬","應用極廣","胺基酸、蛋白、脂質、醣類、酚類、摻假物皆可分析","a") +
    dc.card("⚙️","技術多元","材料、設備、方法種類繁多，可彈性搭配","g") +
    dc.card("🚀","品質控制","食品成分與產品的特性分析與品管","b") + '</div>')

add(MOT, dc.kt("12.2 先談萃取", "萃取：分離的起點") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li><strong>批次萃取</strong>：與第二種不互溶溶劑搖盪，溶質依分配分布</li>" +
    "<li><strong>連續萃取</strong>：如 Soxhlet，溶劑循環反覆萃取</li>" +
    "<li><strong>逆流萃取</strong>：多管串聯，分離分配係數相近的溶質</li>" +
    "<li>每一管的平衡 ≈ 層析的一個<span class='em'>理論板</span></li>" +
    '</ul></div><div class="note"><strong>分配係數 K：溶質在兩相濃度之比 (式 12.1)。</strong><br>' +
    "K = 相 1 濃度 ÷ 相 2 濃度。逆流萃取正是層析的概念前身。</div></div>")

add(MOT, dc.chart_inner("polar", "<span class='hi'>極性</span>決定洗脫順序", "資料：Table 12.4 化合物極性序（相對等級，數字越大越極性）。",
    kicker="12.4.1 極性序"), ' data-chart="polar"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">核心命題</div>
  <div class="hook" style="font-size:clamp(1.7rem,4vw,3rem)">兩相之間，<span class="hi">不斷分配</span></div>
  <p class="lead" style="max-width:820px;margin:20px auto 0">層析的本質：溶質在<strong>移動相</strong>與<strong>固定相</strong>之間反覆達成平衡。</p>
  <div class="eq" style="max-width:560px;margin:24px auto 0">分配係數 K = <span class="frac"><b>移動相中溶質濃度</b><span>固定相中溶質濃度</span></span><br>
  <span style="font-size:.8em;color:var(--ink-2)">與固定相作用越強 → 走得越慢 → 越晚洗出</span></div></div>""")

add(MOT, dc.kt("12.3.1 歷史", "從色素到<span class='hi'>層析學</span>") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("🌿","1903 Tsvet","俄國植物學家用碳酸鈣管柱分離葉片色素，命名 chromatography","g") +
    dc.card("🧪","1941 Martin & Synge","發展液–液分配層析，奠定理論板概念","b") +
    dc.card("⛽","1960s GC","氣相層析商品化，先用於石油工業","a") +
    dc.card("🚀","HPLC / SFC","由 GC 理論推進液相；SFC 1962 起應用於食品","b") + '</div>')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","三種層析依「移動相」分類", 6,
    "移動相是什麼狀態？把 6 個關鍵字分到三類。"), ' data-game="g1"')

# ---------------- 維持注意 ----------------
add(ATT, dc.kt("12.3.2 一般術語", "層析家族<span class='hi'>樹</span>") +
    '<div class="svgwrap" style="margin-top:10px">' + FAMILY_SVG + '</div>' +
    '<div class="note" style="margin-top:14px">依<strong>移動相</strong>分為 GC / LC / SFC；液相層析再分為平面式（紙、薄層 TLC）與管柱式。</div>')

add(ATT, dc.kt("12.3 管柱層析", "管柱裡發生了什麼") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + COLUMN_SVG + '</div><div><ul class="clean">' +
    "<li><strong>移動相</strong>帶著樣品流過<strong>固定相</strong></li>" +
    "<li>各成分與固定相作用<span class='em'>強弱不同</span></li>" +
    "<li>作用弱者走得快 → <strong>先洗出</strong>；作用強者後出</li>" +
    "<li>出柱後經<strong>偵測器</strong>產生峰 (peak)</li>" +
    '</ul><div class="note" style="margin-top:14px">1903 年 Tsvet 用碳酸鈣管柱分離葉片色素，命名「chromatography」。</div></div></div>')

add(ATT, dc.kt("12.4 七大分離模式", "依物理化學原理區分") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧲","吸附 / 分配","正相·逆相：靠極性差異 (van der Waals / 溶解度)","b") +
    dc.card("💧","HILIC / HIC","親水交互作用 / 疏水交互作用","a") +
    dc.card("⚡","離子交換","靜電作用，依電荷分離","g") +
    dc.card("🔑","親和 / 排阻","專一結合 (affinity) / 依分子大小 (SEC)","b") + '</div>' +
    '<div class="note" style="margin-top:14px">同一分離常牽涉<strong>不只一種機制</strong>；整理自 Table 12.3。</div>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","層析原理即時測驗", 4), ' data-game="g2"')

add(ATT, dc.kt("12.4.1 / 12.4.2", "正相 vs 逆相") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🟠","正相 Normal-phase","固定相<strong>極性</strong>(silica)、移動相非極性；<strong>非極性先出、極性後出</strong>","a") +
    dc.card("🔵","逆相 Reversed-phase","固定相<strong>非極性</strong>(C8/C18)、移動相極性(水/乙腈)；<strong>極性先出</strong>","b") +
    '</div><div class="note" style="margin-top:18px">逆相 HPLC 是食品分析<strong>最常用</strong>：維生素、多酚、類胡蘿蔔素、類黃酮。</div>')

add(ATT, dc.kt("12.3.5 超臨界流體", "SFC：介於 GC 與 LC") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🌫️","移動相","超臨界 CO₂（介於氣/液之間），可調壓力、溫度與組成","g") +
    dc.card("🧴","強項","分析<strong>非揮發·熱不安定</strong>物；脂質、脂溶性維生素、Sudan 染料","b") +
    '</div><div class="note" style="margin-top:18px">分析時間短、溶劑用量少；可用填充或毛細管柱，並可接質譜 (MS)。</div>')

add(ATT, dc.kt("12.4.5 離子交換", "靠電荷分離") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("➖","陽離子交換","固定相帶<strong>負電</strong>(RSO₃⁻/RCO₂⁻)，抓陽離子","b") +
    dc.card("➕","陰離子交換","固定相帶<strong>正電</strong>(R-NHR'₂⁺)，抓陰離子","a") +
    '</div><div class="note" style="margin-top:18px">溶離策略：改變<strong>pH</strong> 或提高<strong>離子強度</strong>(如加 NaCl) 以削弱靜電作用。</div>')

add(ATT, dc.kt("12.4.6 親和層析", "Affinity：專一鎖定") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>固定相接上<strong>專一配基</strong>(抗體、酵素抑制劑、凝集素)</li>" +
    "<li>只有目標分子被<span class='em'>專一結合</span>，其餘直接洗掉</li>" +
    "<li>改 pH / 離子強度，或加競爭配基即可溶離</li>" +
    "<li>純化單一蛋白的<strong>高選擇性</strong>利器</li></ul></div>" +
    '<div class="note">「鑰匙–鎖」式的辨識：靠生物專一性而非極性或電荷，' +
    "純化倍率極高，常一步到位。</div></div>")

add(ATT, dc.game_sort_inner("g4","小遊戲 ③","層析分析流程排序", 7,
    "用 ▲▼ 把一次完整層析分析的 7 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("12.4.7 排阻層析", "SEC：依大小篩分") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>固定相為<strong>多孔膠體</strong>(如 Sephadex 葡聚醣)</li>" +
    "<li>大分子<span class='em'>進不了</span>孔洞 → 走孔隙體積 → <strong>先洗出</strong></li>" +
    "<li>小分子鑽進孔洞 → 路徑長 → 後出</li>" +
    "<li>可估蛋白質<strong>分子量</strong>(Kav vs log MW 檢量線)</li></ul></div>" +
    '<div class="note">與其他模式相反：<strong>大分子先出、小分子後出</strong>。' +
    "溫和條件少變性，常作為純化的早期步驟，也可替代透析脫鹽。</div></div>")

add(ATT, dc.chart_inner("hetp", "找出最佳<span class='hi'>流速</span>", "Van Deemter：HETP=A+B/u+Cu。HETP 越小、效率越高（代表性示意數據）。",
    kicker="12.5.1.2.2 Van Deemter", height="52vh"), ' data-chart="hetp"')

add(ATT, dc.kt("12.5.1.2.1 滯留時間", "讀懂層析圖") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("⏱️","滯留時間 t_R","成分從進樣到出峰所需時間（或滯留體積 V_R）","b") +
    dc.card("💨","空容時間 t₀","不被滯留的成分(溶劑前緣)通過管柱的時間","a") +
    dc.card("✂️","校正滯留 t'_R","t'_R = t_R − t₀，扣掉系統死體積後的真實滯留","g") +
    dc.card("📐","峰寬 w","基線寬度 w = 4σ；半高寬 w½ 更準確","b") + '</div>' +
    '<div class="note" style="margin-top:14px">跨系統比較時用<strong>校正滯留時間 t\'_R</strong> 較可靠。</div>')

add(ATT, dc.kt("12.5.1 解析度", "把峰<span class='hi'>分得開</span>") +
    '<div class="svgwrap" style="margin-top:8px">' + PEAK_SVG + '</div>' +
    '<div class="note" style="margin-top:14px">解析度 Rs 越大，兩峰分得越開。<strong>Rs = 2Δt / (w₁+w₂)</strong>（式 12.4），通常 Rs ≥ 1.5 視為基線分離。</div>')

add(ATT, dc.kt("12.5.1.2 三要素", "效率 · 選擇性 · 容量") +
    '<div class="grid3" style="margin-top:22px">' +
    dc.card("📊","效率 N","理論板數 N=16(t_R/w)²；板越多、峰越窄。HETP=L/N","b") +
    dc.card("🎯","選擇性 α","分離因子 α=t'_R2/t'_R1；峰間相對距離","a") +
    dc.card("⏱️","容量因子 k'","k'=(t_R−t₀)/t₀；停留在固定相的程度，常取 1–15","g") + '</div>' +
    '<div class="note" style="margin-top:14px">Rs 與選擇性<strong>線性</strong>相關，但與效率僅<strong>平方根</strong>相關——N 要 4 倍才讓 Rs 加倍。</div>')

add(ATT, dc.game_bucket_inner("g3","小遊戲 ④","固定相依「化學本質」分類", 6,
    "換個角度——這些分離模式的固定相本質是什麼？分到三類。"), ' data-game="g3"')

add(ATT, dc.kt("12.5.3 定量分析", "內標 vs 外標") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧮","外標法","另外配標準品分開進樣，建<strong>峰面積–濃度</strong>檢量線；需偵測器穩定","b") +
    dc.card("🎯","內標法","加入已知量內標物，用<strong>峰面積比</strong>校正；補償前處理損失與進樣誤差","a") +
    '</div><div class="note" style="margin-top:18px">內標物須與分析物<strong>性質相似但分得開</strong>、且樣品中本不存在（Table 12.7）。</div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對模式", 5), ' data-game="g5"')

# ---------------- 喚起行動 ----------------
add(ACT, dc.cmp_inner("一張表選分離模式（點欄位排序）",
    [{"k":"m","t":"s","label":"模式"},{"k":"sp","t":"s","label":"固定相"},
     {"k":"mp","t":"s","label":"移動相"},{"k":"by","t":"s","label":"依何分離"}],
    "整合自 Table 12.3。點欄位標題可排序。", kicker="12.4 模式比較"), ' data-game="cmp"')

add(ACT, dc.kt("方法選擇", "跟著決策樹走") +
    '<div class="svgwrap" style="margin-top:10px">' + DTREE_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:14px">下一頁實戰：算兩個峰的解析度 Rs →</p>')

add(ACT, dc.kt("12.5.1 計算", "解析度：從滯留時間到 Rs") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">R<sub>s</sub> = ' +
    '<span class="frac"><b>2 · Δt</b><span>w₁ + w₂</span></span></div>' +
    '<div><ul class="clean"><li>Δt = 兩峰滯留時間差 (t_R2 − t_R1)</li>' +
    "<li>w₁、w₂ = 兩峰基線寬度</li><li>Rs 越大、分得越開</li>" +
    "<li>Rs ≥ 1.5 ≈ 基線分離</li></ul></div></div>")

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關",
    "兩個層析峰：t_R1 = 10.0 min、t_R2 = 12.0 min，基線寬 w₁ = w₂ = 1.0 min。"
    "求<strong>解析度 Rs</strong>（無單位）。", unit=""), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>層析＝溶質在<strong>移動相與固定相</strong>間反覆分配</li>" +
    "<li>依移動相分 <strong>GC / LC / SFC</strong>；液相再分平面與管柱</li>" +
    "<li>七大模式：吸附·分配·HILIC·HIC·離子交換·親和·排阻</li></ul>" +
    '<ul class="clean"><li>峰的好壞看 <strong>Rs、N、α、k\'</strong>；Van Deemter 找最佳流速</li>' +
    "<li>定量靠峰面積＋標準品：<strong>內標</strong>補損失、<strong>外標</strong>建檢量線</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["用「兩相分配」解釋層析的基本原理",
     "畫出層析家族樹並說明 GC/LC/SFC 的差別",
     "說出七大分離模式各自靠什麼分離",
     "比較正相與逆相、陽離子與陰離子交換",
     "判斷該用哪種模式（小分子/離子/大分子）",
     "由滯留時間與峰寬算出解析度 Rs",
     "區分內標法與外標法的用途"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把層析原理<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions、Practice Problems<br>"
    "🔜 銜接章節：<strong>HPLC (Ch13)</strong>、<strong>氣相層析 GC (Ch14)</strong><br>"
    "🧪 思考：你的樣品是小分子還是大分子？帶電荷嗎？該選哪種分離模式？",
    ["GC","LC/HPLC","SFC","IEC","SEC"]), ' data-cover="1"')

# ---------------- CFG ----------------
CFG = {
  "charts": {
    "polar": {"type":"bar","yTitle":"相對極性 (等級)",
      "labels":["碳氟化物","飽和烴","烯類","芳香族","鹵化物","醚類","酯/酮/醛","醇/胺","醯胺","羧酸"],
      "datasets":[{"label":"相對極性（Table 12.4，越大越極性）","data":[1,2,3,4,5,6,7,8,9,10],"color":"#1f6feb"}]},
    "hetp": {"type":"line","yTitle":"HETP (任意單位)","zero":False,
      "labels":["0.4","0.6","0.8","1.0","1.2","1.5","2.0","2.5","3.0"],
      "datasets":[{"label":"HETP = A + B/u + Cu","data":[5.5,4.3,3.7,3.4,3.3,3.4,3.9,4.6,5.4],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["氣相 GC","液相 LC","超臨界流體 SFC"],
      "items":[{"t":"載送氣體 (He)","c":"氣相 GC"},{"t":"揮發性成分","c":"氣相 GC"},
        {"t":"水 / 乙腈","c":"液相 LC"},{"t":"逆相 HPLC","c":"液相 LC"},
        {"t":"超臨界 CO₂","c":"超臨界流體 SFC"},{"t":"非揮發·熱不安定物","c":"超臨界流體 SFC"}],
      "ok":"🎉 全對！GC 用氣體移動相、LC 用液體、SFC 用超臨界流體（如 CO₂）。",
      "tip":"提示：移動相是氣體→GC；液體→LC；超臨界流體→SFC。"},
    "g3": {"cats":["極性固定相","非極性固定相","帶電/孔洞固定相"],
      "items":[{"t":"正相 silica","c":"極性固定相"},{"t":"HILIC","c":"極性固定相"},
        {"t":"逆相 C18","c":"非極性固定相"},{"t":"HIC butyl-Sepharose","c":"非極性固定相"},
        {"t":"離子交換樹脂","c":"帶電/孔洞固定相"},{"t":"排阻 Sephadex","c":"帶電/孔洞固定相"}],
      "ok":"🎉 正確！silica/HILIC 極性、C18/HIC 非極性、離子交換帶電、排阻靠孔洞。",
      "tip":"提示：silica 與 HILIC 是極性；C18 與 HIC 是非極性；IEC 帶電、SEC 多孔。"}
  },
  "mcq": {
    "g2":[
      {"q":"層析分離的最根本原理是？","o":["重量差異","溶質在兩相間反覆分配","顏色差異","沸點唯一"],"a":1,
       "e":"層析＝溶質在移動相與固定相之間反覆達成平衡分配。"},
      {"q":"依「移動相」分類，下列何者正確？","o":["GC 用液體","LC 用氣體","SFC 用超臨界流體","GC 用超臨界流體"],"a":2,
       "e":"GC 氣體、LC 液體、SFC 超臨界流體。"},
      {"q":"正相層析中，洗脫順序為？","o":["極性先出","非極性先出","同時出","隨機"],"a":1,
       "e":"正相固定相為極性，非極性溶質作用弱→先洗出，極性後出。"},
      {"q":"分配係數 K 的定義是？","o":["兩相中溶質濃度之比","溫度比","體積比","峰高比"],"a":0,
       "e":"K = 溶質在相 1 與相 2 的濃度之比（式 12.1）。"}
    ],
    "g5":[
      {"q":"要依分子大小分離蛋白質、並估其分子量，選？","o":["離子交換","排阻層析 SEC","正相","氣相 GC"],"a":1,
       "e":"SEC 依分子大小篩分，可由 Kav-logMW 檢量線估分子量。"},
      {"q":"分離帶電荷的離子化合物，最適合？","o":["排阻 SEC","離子交換 IEC","親和層析","正相"],"a":1,
       "e":"離子交換靠靜電作用，專門分離帶電荷物種。"},
      {"q":"食品中極性偏低的多酚、脂溶性維生素，最常用？","o":["逆相 RP","正相 silica","離子交換","SEC"],"a":0,
       "e":"逆相 HPLC 是食品分析最常用，廣泛分析多酚、類胡蘿蔔素等。"},
      {"q":"想提高兩個相鄰峰的解析度 Rs，最有效的是？","o":["只增加管柱長度(提升N)","改善選擇性α","降低溫度","加大進樣量"],"a":1,
       "e":"Rs 與選擇性α線性相關、與效率N僅平方根相關，故改善α最有效。"},
      {"q":"要校正前處理損失與進樣體積誤差，定量宜用？","o":["外標法","內標法","只看峰高","不校正"],"a":1,
       "e":"內標法加入已知內標物、用峰面積比校正，可補償損失與進樣誤差。"}
    ]
  },
  "sort": {
    "g4":{"steps":["評估樣品特性，選擇分離模式","選固定相、移動相與溶離條件(等度/梯度)",
       "注入樣品到管柱","成分依與固定相作用強弱分離","偵測器記錄各峰(滯留時間/峰面積)",
       "優化解析度(調 N / α / k')","以標準品定性與定量"],
       "shuffle":[3,0,6,1,4,2,5],
       "ok":"🎉 順序正確！選模式→定條件→進樣→分離→偵測→優化→定量。",
       "tip":"提示：先選模式與條件，最後才用標準品定量。"}
  },
  "calc": {
    "g6":{"answer":2.0,"tol":0.05,
      "ok":"🎉 正確！Rs = 2×(12.0−10.0) ÷ (1.0+1.0) = 4.0 ÷ 2.0 = <b>2.0</b>（> 1.5，基線分離）。",
      "bad":"再算算：Rs = 2·Δt ÷ (w₁+w₂)；Δt = 12.0−10.0 = 2.0，分母 = 1.0+1.0 = 2.0。",
      "hint":"提示：Δt = 2.0，w₁+w₂ = 2.0；Rs = 2×2.0 ÷ 2.0。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"sp"},{"k":"mp"},{"k":"by"}],
    "rows":[
      {"m":"正相 (吸附/分配)","sp":"極性 (silica)","mp":"非極性溶劑","by":"極性 (非極性先出)"},
      {"m":"逆相 RP","sp":"非極性 (C8/C18)","mp":"極性 (水/乙腈)","by":"極性 (極性先出)"},
      {"m":"HILIC","sp":"極性改質 silica","mp":"高比例有機+水","by":"極性 (親水)"},
      {"m":"疏水 HIC","sp":"弱疏水配基","mp":"高鹽→低鹽","by":"表面疏水性"},
      {"m":"陽離子交換","sp":"負電基 (RSO₃⁻)","mp":"緩衝/離子強度","by":"正電荷密度"},
      {"m":"陰離子交換","sp":"正電基 (R-NHR'₂⁺)","mp":"緩衝/離子強度","by":"負電荷密度"},
      {"m":"親和 Affinity","sp":"專一配基/抗體","mp":"緩衝","by":"專一結合力"},
      {"m":"排阻 SEC","sp":"多孔膠 (Sephadex)","mp":"水/緩衝","by":"分子大小 (大先出)"}
    ]
  }
}

dc.build_html(
  {"title":"層析原理 Basic Principles of Chromatography · Nielsen Ch12","brand":"CHROMATOGRAPHY · CH12"},
  S, CFG, OUT)
