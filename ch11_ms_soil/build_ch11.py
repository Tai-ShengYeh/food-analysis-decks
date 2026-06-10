# -*- coding: utf-8 -*-
"""Nielsen Ch11 Mass Spectrometry — SOIL HTML deck. Uses ../soil_deck_common.py.
Run: python build_ch11.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
BLOCK_SVG = """
<svg viewBox="0 0 1000 200">
 <defs><marker id="mb" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <g font-size="13">
  <rect x="14" y="70" width="150" height="60" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="89" y="96" text-anchor="middle" class="lblb">樣品導入</text><text x="89" y="115" text-anchor="middle" class="lbl">GC/LC/直接</text>
  <rect x="210" y="70" width="150" height="60" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="285" y="96" text-anchor="middle" class="lblb">游離源</text><text x="285" y="115" text-anchor="middle" class="lbl">分子→離子</text>
  <rect x="406" y="70" width="160" height="60" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="486" y="96" text-anchor="middle" class="lblb">質量分析器</text><text x="486" y="115" text-anchor="middle" class="lbl">依 m/z 分離</text>
  <rect x="612" y="70" width="150" height="60" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="687" y="96" text-anchor="middle" class="lblb">偵測器</text><text x="687" y="115" text-anchor="middle" class="lbl">計數離子</text>
  <rect x="808" y="74" width="150" height="52" rx="9" fill="#15233f"/>
  <text x="883" y="104" text-anchor="middle" fill="#fff" font-weight="800">資料系統</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#mb)">
  <line x1="166" y1="100" x2="206" y2="100"/><line x1="362" y1="100" x2="402" y2="100"/>
  <line x1="568" y1="100" x2="608" y2="100"/><line x1="764" y1="100" x2="804" y2="100"/></g>
 <text x="486" y="40" text-anchor="middle" class="lblb" font-size="15">質譜儀三大功能：游離 → 依 m/z 分離 → 偵測 (Fig 11.1)</text>
 <text x="486" y="175" text-anchor="middle" class="lbl">全程高真空(10⁻⁶–10⁻⁸ torr)，避免離子與氣體分子碰撞</text>
</svg>"""

QUAD_SVG = """
<svg viewBox="0 0 560 260">
 <text x="280" y="22" text-anchor="middle" class="lblb" font-size="15">四極桿質量分析器：RF+DC 電場當「質量篩」</text>
 <!-- 4 rods (2 shown as ellipses pairs) -->
 <ellipse cx="200" cy="80" rx="120" ry="20" fill="#cfe0f6" stroke="#1f6feb" stroke-width="2"/>
 <ellipse cx="200" cy="180" rx="120" ry="20" fill="#cfe0f6" stroke="#1f6feb" stroke-width="2"/>
 <circle cx="90" cy="130" r="20" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
 <circle cx="320" cy="130" r="20" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
 <text x="200" y="70" text-anchor="middle" class="lbl">+ (DC+RF)</text>
 <text x="200" y="200" text-anchor="middle" class="lbl">−</text>
 <!-- ion path: stable sine -->
 <path d="M70 130 q30 -28 60 0 q30 28 60 0 q30 -28 60 0 q30 28 60 0" fill="none" stroke="#1f9d6b" stroke-width="3"/>
 <circle cx="70" cy="130" r="6" fill="#1f9d6b"/>
 <text x="40" y="135" text-anchor="end" class="lbl">離子</text>
 <line x1="350" y1="130" x2="420" y2="130" stroke="#1f9d6b" stroke-width="3" marker-end="url(#qm)"/>
 <defs><marker id="qm" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#1f9d6b"/></marker></defs>
 <text x="430" y="125" class="lblb">穩定路徑</text><text x="430" y="143" class="lbl">→ 偵測器</text>
 <!-- unstable -->
 <path d="M150 230 q20 -18 0 -36" fill="none" stroke="#d94f4f" stroke-width="2" stroke-dasharray="3 3"/>
 <text x="200" y="244" text-anchor="middle" class="lbl">不穩定離子撞上電極被抽走</text>
</svg>"""

TQ_SVG = """
<svg viewBox="0 0 980 230">
 <defs><marker id="tm" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#1f9d6b"/></marker></defs>
 <text x="490" y="22" text-anchor="middle" class="lblb" font-size="15">三重四極桿 MS/MS：選母離子 → 碰撞碎裂 → 選子離子 (Fig 11.14)</text>
 <line x1="40" y1="120" x2="930" y2="120" stroke="#1f9d6b" stroke-width="3" marker-end="url(#tm)"/>
 <rect x="70" y="92" width="150" height="56" rx="9" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
 <text x="145" y="116" text-anchor="middle" class="lblb">Q1</text><text x="145" y="135" text-anchor="middle" class="lbl">選母離子</text>
 <rect x="300" y="92" width="180" height="56" rx="9" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
 <text x="390" y="116" text-anchor="middle" class="lblb">Q2 碰撞室</text><text x="390" y="135" text-anchor="middle" class="lbl">CID 與 Ar/N₂ 碰撞碎裂</text>
 <rect x="560" y="92" width="150" height="56" rx="9" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
 <text x="635" y="116" text-anchor="middle" class="lblb">Q3</text><text x="635" y="135" text-anchor="middle" class="lbl">選子離子</text>
 <rect x="800" y="96" width="120" height="48" rx="8" fill="#15233f"/>
 <text x="860" y="125" text-anchor="middle" fill="#fff" font-weight="800">偵測器</text>
 <text x="145" y="76" text-anchor="middle" class="lbl">precursor</text>
 <text x="635" y="76" text-anchor="middle" class="lbl">product</text>
 <text x="490" y="200" text-anchor="middle" class="lbl">SRM/MRM：只看特定「離子對」→ 雜訊大降、靈敏度↑100–1000 倍，痕量定量首選</text>
</svg>"""

ESI_SVG = """
<svg viewBox="0 0 600 220">
 <text x="300" y="20" text-anchor="middle" class="lblb" font-size="15">電灑游離 ESI：液相分子變氣相離子(軟游離)</text>
 <!-- capillary -->
 <rect x="20" y="95" width="150" height="22" rx="4" fill="#cfe0f6" stroke="#1f6feb" stroke-width="2"/>
 <text x="95" y="88" text-anchor="middle" class="lbl">LC 流出液 + 高電壓</text>
 <!-- Taylor cone -->
 <path d="M170 95 L210 106 L170 117 Z" fill="#d9822b" opacity=".7"/>
 <text x="200" y="138" text-anchor="middle" class="lbl">Taylor cone</text>
 <!-- droplets shrinking -->
 <g fill="#1f6feb">
  <circle cx="245" cy="106" r="12" opacity=".5"/><circle cx="300" cy="100" r="8" opacity=".55"/>
  <circle cx="345" cy="112" r="6" opacity=".6"/><circle cx="385" cy="103" r="4" opacity=".7"/></g>
 <text x="300" y="150" text-anchor="middle" class="lbl">帶電液滴蒸發、庫侖爆炸越變越小</text>
 <!-- ions -->
 <g fill="#1f9d6b" font-size="12">
  <text x="440" y="98">＋</text><text x="465" y="112">＋</text><text x="490" y="100">＋</text></g>
 <rect x="520" y="92" width="60" height="30" rx="5" fill="#15233f"/>
 <text x="550" y="112" text-anchor="middle" fill="#fff" font-size="11">進質譜</text>
 <text x="455" y="140" text-anchor="middle" class="lbl">氣相離子(可帶多電荷)</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 11",
    "質譜<span style='color:var(--accent-2)'>分析</span> MS", "Mass Spectrometry",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>游離源 · 質量分析器 · GC-MS · LC-MS · 串聯質譜 · 高解析 HRMS",
    ["m/z 質荷比","ESI/EI/MALDI","三重四極桿","ppb–ppt","三聚氰胺/農藥"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">怎麼從一團複雜食品裡，<br>精準「秤」出一個分子、抓出 <span class="hi">ppb 級</span>的農藥或三聚氰胺？</div>
  <p class="subtitle" style="max-width:840px;margin:22px auto 0">答案是<strong>質譜 (MS)</strong>。<br>
  它先把分子變成<strong>帶電的離子</strong>，再依<strong>質荷比 m/z</strong> 把它們一一分開、秤重，<br>靈敏到單一兆分之一(ppt)、還能算出分子式。</p>
  <div style="margin-top:24px"><span class="pill">農藥殘留篩檢</span><span class="pill">三聚氰胺/獸藥</span>
  <span class="pill">真偽與溯源</span><span class="pill">foodomics</span></div></div>""")

add(MOT, dc.kt("11.1 介紹", "質譜能做什麼") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("⚖️","秤分子的質量","小到咖啡因(194 Da)、大到免疫球蛋白(144,000 Da)都能測","b") +
    dc.card("🔗","聯用威力","與 GC、LC 聯用(GC-MS、LC-MS)→大幅降低偵測極限、提高專一性","a") +
    dc.card("🧩","得到分子資訊","由碎片與精確質量推出分子量與結構/組成","g") +
    dc.card("🛡️","食安守門","農藥、獸藥、黴菌毒素、三聚氰胺…官方法多用 LC-MS/MS","b") + '</div>')

add(MOT, dc.kt("11.2.1 三大功能", "質譜儀的<span class='hi'>骨架</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + BLOCK_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:8px">不論氣態、液態或固態，樣品都要先變成<strong>氣相離子</strong>，' +
    "才能在高真空中被電磁場依 m/z 分離。</p>")

add(MOT, dc.kt("11.3 判讀基礎", "質譜圖怎麼看：<span class='hi'>基峰</span>與<span class='hi'>分子離子</span>") +
    '<div class="grid2-1" style="margin-top:8px"><div>' +
    dc.chart_inner("spectrum", "", "丁烷的 EI 質譜(示意)：x 軸 m/z、y 軸相對強度。基峰 m/z 43=100%，分子離子 m/z 58。",
        kicker="", height="44vh") + '</div><div><ul class="clean">' +
    "<li><strong>基峰(base peak)</strong>：強度最高的峰，設為 100%</li>" +
    "<li><strong>分子(前驅)離子 M⁺•</strong>：完整分子失去一個電子，質量＝分子量</li>" +
    "<li><strong>子離子(碎片)</strong>：M⁺• 進一步裂解的產物</li>" +
    "<li>丁烷(58)：基峰 43、另有 29、15；甲醇(32)：基峰 31</li>" +
    '</ul></div></div>', ' data-chart="spectrum"')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","軟游離 vs 硬游離", 8,
    "把 8 個敘述分到「硬游離(多碎片)」或「軟游離(少碎片)」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("11.2.2 樣品導入", "靜態 vs 動態") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("💉","靜態(static)","純物或萃取液<strong>直接注入</strong>、直接插入探針、DART 即時分析","b") +
    dc.card("🔀","動態(dynamic)","混合物先用 <strong>GC 或 LC 分離</strong>，經介面去除載氣/溶劑後進質譜","a") +
    '</div><div class="note" style="margin-top:16px">所有質譜都在高真空運作，<strong>介面(interface)</strong>的關鍵任務' +
    "就是把大量 GC 載氣或 LC 溶劑移除，只讓分析物離子進入。</div>")

add(ATT, dc.kt("11.2.3 游離源", "把分子變離子的<span class='hi'>四種</span>常見方式") +
    '<div class="grid2" style="margin-top:14px">' +
    dc.card("⚡","EI 電子撞擊","70 eV 電子撞出離子；<strong>硬游離</strong>、碎片豐富，GC-MS 主力、可比對圖庫","a") +
    dc.card("💧","ESI 電灑","最常用 LC-MS；<strong>軟游離</strong>、可多電荷，適合極性/大分子","b") +
    dc.card("🔥","APCI/APPI","常壓化學/光游離；適合低極性、揮發性分子","g") +
    dc.card("🔬","MALDI","基質輔助雷射；軟游離大生物分子(蛋白、核酸)，常配 TOF","b") + '</div>')

add(ATT, dc.kt("11.2.3.2 ESI 細看", "電灑：液滴→離子") +
    '<div class="svgwrap" style="margin-top:6px">' + ESI_SVG + '</div>' +
    '<div class="note" style="margin-top:12px">高電壓在毛細管尖端拉出 <strong>Taylor cone</strong>，噴出帶電液滴；溶劑蒸發使液滴縮小、' +
    "電荷密度升高到<strong>庫侖爆炸</strong>，最終釋出氣相離子。ESI 可帶<strong>多電荷</strong>，故能測 m/z 上限內的大蛋白。</div>")

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","游離與判讀即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("11.2.4 質量分析器", "四種「秤離子」的<span class='hi'>引擎</span>") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + QUAD_SVG + '</div><div><ul class="clean">' +
    "<li><strong>四極桿(Q)</strong>：RF+DC 當質量篩，便宜堅固、定量主力</li>" +
    "<li><strong>離子阱(IT)</strong>：先困住離子，可做多階 <strong>MSⁿ</strong></li>" +
    "<li><strong>飛行時間(TOF)</strong>：依飛行時間分離，掃描快、質量範圍大</li>" +
    "<li><strong>傅立葉(Orbitrap/FT-ICR)</strong>：測離子振盪頻率，<strong>超高解析</strong></li>" +
    '</ul></div></div>')

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","GC-MS vs LC-MS：誰適合？", 6,
    "把 6 個情境分到「適合 GC-MS」或「適合 LC-MS」。"), ' data-game="g3"')

add(ATT, dc.kt("11.6 串聯質譜 MS/MS", "三重四極桿：痕量定量的<span class='hi'>主力</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + TQ_SVG + '</div>' +
    '<div class="note" style="margin-top:10px"><strong>SRM/MRM</strong>(選擇/多重反應偵測)：Q1 選母離子、Q2 碰撞碎裂(CID)、Q3 選子離子，' +
    "只盯特定「離子對」→ 雜訊大降、靈敏度提升 <strong>100–1000 倍</strong>。這就是農藥、獸藥、甜味劑官方法都用它的原因。</div>")

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","三重四極桿 MRM 流程排序", 6,
    "用 ▲▼ 把 LC-MS/MS 做 MRM 定量的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("11.7 高解析質譜 HRMS", "用<span class='hi'>準確質量</span>算出分子式") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>解析度以 <strong>FWHM</strong>(半高寬)定義；四極桿~500、Orbitrap~30,000、FT-ICR~3,000,000</li>" +
    "<li><strong>準確質量</strong>＋同位素細結構 → 推出<strong>元素組成</strong></li>" +
    "<li>質量誤差 <strong>&lt; 5 ppm</strong> 即可可靠定出分子式</li></ul>" +
    '<div class="note">咖啡因 C₈H₁₀N₄O₂ 的三種質量：<br><strong>標稱 194</strong>(整數和)、' +
    "<strong>單一同位素 194.0804</strong>(最豐同位素精確和)、<strong>平均 194.1906</strong>(考慮同位素豐度)。" +
    "<br>質量量得越準，越能唯一決定分子式。</div></div>")

add(ATT, dc.chart_inner("resolution", "各質量分析器的<span class='hi'>解析度</span>",
    "解析度取以 10 為底對數：四極桿~500 到 FT-ICR~3,000,000，跨 4 個數量級——解析度越高，越能分辨質量相近的離子。",
    kicker="11.7 解析度"), ' data-chart="resolution"')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對質譜技術", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("一張表選質量分析器（點欄位排序）",
    [{"k":"m","t":"s","label":"分析器"},{"k":"res","t":"n","label":"解析度","star":True},
     {"k":"acc","t":"s","label":"質量準確度"},{"k":"cost","t":"n","label":"成本","star":True},{"k":"app","t":"s","label":"代表用途"}],
    "解析度／成本 ★ 越多越高。整合自 Table 11.1 與 11.7。", kicker="11.2.4 / 11.7 比較"), ' data-game="cmp"')

add(ACT, dc.kt("11.8 應用", "質譜在食品的<span class='hi'>實戰</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("☕","咖啡因/可可鹼","逆相 LC-MS/MS，以 SIM/MRM 分離定量(同質量異構物也能分)","b") +
    dc.card("🥛","三聚氰胺(2008)","極性、不揮發→須 LC-MS/MS；母離子 127.1 → 子離子 85.1","a") +
    dc.card("🍵","綠茶兒茶素","ESI-MS 全掃描＋MS/MS，鑑定 epicatechin 等多酚","g") +
    dc.card("🦠","MALDI-TOF 微生物","以蛋白質指紋 24 小時內快速鑑定細菌、酵母菌","b") + '</div>')

add(ACT, dc.kt("11.8 焦點案例", "三聚氰胺：質譜如何<span class='hi'>破案</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>三聚氰胺含氮量高(67%)，被非法加入乳品/麵筋<strong>假造蛋白質</strong>(Ch18 凱氏法只測氮)</li>" +
    "<li>分子極性、不揮發 → GC 不行，<strong>LC-MS/MS</strong> 成首選</li>" +
    "<li>ESI⁺ 產生 <strong>m/z 127.1</strong> 母離子 → CID → <strong>m/z 85.1</strong> 子離子</li>" +
    "<li>同時監測多組離子對 → 高專一性、低偽陽性</li>" +
    '</ul></div><div class="note"><strong>啟示：</strong>單測「總氮」會被鑽漏洞；<br>' +
    "質譜直接看<strong>分子身分(m/z)</strong>，才能識破摻假。這正是後面食藥署各項 LC-MS/MS 公告法的基礎。</div></div>")

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：質量準確度(ppm)",
    "高解析質譜測得咖啡因分子離子為 <b>194.0811</b>，理論單一同位素質量為 <b>194.0804</b>。"
    "求質量準確度。公式：(測得−理論)/理論 × 10⁶。", unit="ppm"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>MS＝<strong>游離 → 依 m/z 分離 → 偵測</strong>；全程高真空</li>" +
    "<li>游離：<strong>EI 硬</strong>(GC-MS、碎片多)、<strong>ESI 軟</strong>(LC-MS、多電荷)</li>" +
    "<li>分析器：四極桿/離子阱/TOF/Orbitrap，解析度差距大</li></ul>" +
    '<ul class="clean"><li><strong>三重四極桿 MRM</strong>：痕量定量主力(靈敏度×100–1000)</li>' +
    "<li><strong>HRMS</strong> 準確質量(&lt;5 ppm)→ 定分子式；應用遍及農藥、獸藥、摻假</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說出質譜的三大功能與五大組件",
     "區分靜態與動態樣品導入、GC-MS 與 LC-MS 的適用對象",
     "比較 EI 與 ESI(硬/軟游離)及其代表應用",
     "說明四極桿、離子阱、TOF、Orbitrap 的差異",
     "畫出三重四極桿 MRM 的流程並說明為何靈敏",
     "解讀質譜圖的基峰、分子離子與子離子",
     "用準確質量算出質量準確度(ppm)並說明其用途",
     "舉出至少兩個質譜在食品安全的應用案例"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把質譜<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions(乙醇 EI 質譜、標稱 vs 單一同位素質量、CAD vs CID)<br>"
    "🔜 銜接：<strong>HPLC (Ch13)</strong>、<strong>GC (Ch14)</strong>、<strong>蛋白質/凱氏法 (Ch18)</strong>、食藥署 LC-MS/MS 公告法<br>"
    "🧪 思考：你的分析物揮發嗎？極性如何？要定量還是鑑定結構？該選 GC-MS、LC-MS/MS 還是 HRMS？",
    ["m/z","EI/ESI","MRM 定量","HRMS","食安應用"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "spectrum": {"type":"bar","yTitle":"相對強度 (%)","zero":True,
      "labels":["15","29","43","57","58"],
      "datasets":[{"label":"丁烷 EI 質譜","data":[10,32,100,5,30],"color":"#d9822b"}]},
    "resolution": {"type":"bar","yTitle":"解析度 log₁₀(R)",
      "labels":["四極桿","離子阱","TOF","Orbitrap","FT-ICR"],
      "datasets":[{"label":"log₁₀(解析度)","data":[2.7,3.0,4.5,5.5,6.5],"color":"#1f6feb"}]}
  },
  "bucket": {
    "g1": {"cats":["硬游離(多碎片)","軟游離(少碎片)"],
      "items":[{"t":"EI 電子撞擊(70 eV)","c":"硬游離(多碎片)"},
        {"t":"打出豐富碎片、可比對質譜圖庫","c":"硬游離(多碎片)"},
        {"t":"GC-MS 揮發性分子常用","c":"硬游離(多碎片)"},
        {"t":"分子離子常因裂解而不明顯","c":"硬游離(多碎片)"},
        {"t":"ESI 電灑游離","c":"軟游離(少碎片)"},
        {"t":"MALDI 雷射游離大分子","c":"軟游離(少碎片)"},
        {"t":"主要產生 (M+H)⁺、碎片少","c":"軟游離(少碎片)"},
        {"t":"LC-MS 分析極性/熱不穩定分子","c":"軟游離(少碎片)"}],
      "ok":"🎉 全對！硬游離(EI)碎片多可比對圖庫；軟游離(ESI/MALDI/CI)保留分子離子。",
      "tip":"提示：碎片多、能比對圖庫→硬(EI)；保留完整分子離子、碎片少→軟(ESI/MALDI)。"},
    "g3": {"cats":["適合 GC-MS","適合 LC-MS"],
      "items":[{"t":"揮發、熱穩定的小分子(精油、脂肪酸甲酯)","c":"適合 GC-MS"},
        {"t":"常用 EI 硬游離、比對質譜圖庫","c":"適合 GC-MS"},
        {"t":"需先衍生化才夠揮發(如 FAME)","c":"適合 GC-MS"},
        {"t":"極性、不揮發或熱不穩定(三聚氰胺、農藥、抗生素)","c":"適合 LC-MS"},
        {"t":"常用 ESI/APCI 軟游離","c":"適合 LC-MS"},
        {"t":"大分子量、多電荷的蛋白質","c":"適合 LC-MS"}],
      "ok":"🎉 正確！揮發/熱穩定→GC-MS；極性/不揮發/大分子→LC-MS。",
      "tip":"提示：能變成氣相又耐熱→GC-MS；極性、怕熱、不揮發、大分子→LC-MS。"}
  },
  "mcq": {
    "g2":[
      {"q":"質譜依什麼把離子分開？","o":["沸點","質荷比 m/z","極性","顏色"],"a":1,
       "e":"質量分析器依離子的質荷比(m/z)分離；多數離子帶 +1，m/z≈質量。"},
      {"q":"質譜圖中強度設為 100% 的峰稱為？","o":["分子離子","基峰(base peak)","同位素峰","雜訊"],"a":1,
       "e":"基峰是強度最高的峰，設為 100%，其餘峰相對於它。"},
      {"q":"代表完整分子、質量最大的離子稱為？","o":["子離子","基峰","分子(前驅)離子 M⁺•","加合物"],"a":2,
       "e":"分子(前驅)離子由完整分子失去一個電子形成，質量等於分子量。"},
      {"q":"最常用於 LC-MS、可產生多電荷的軟游離法是？","o":["EI","ESI 電灑","FAB","場游離"],"a":1,
       "e":"ESI 是最普遍的 LC-MS 軟游離法，可帶多電荷，能測大蛋白。"},
      {"q":"EI 的電子能量通常設定在？","o":["7 eV","70 eV","700 eV","7 keV"],"a":1,
       "e":"EI 標準用 70 eV，使不同儀器得到的質譜相近、便於比對圖庫。"}
    ],
    "g5":[
      {"q":"要鑑定未知物、需要超高解析的準確質量，選？","o":["四極桿","Orbitrap/FT-ICR(HRMS)","單一四極桿","離子阱"],"a":1,
       "e":"高解析(Orbitrap/FT-ICR)提供準確質量與同位素細結構，利於定分子式。"},
      {"q":"要定量食品中 ppb 級農藥殘留(高選擇、高靈敏)，選？","o":["單一四極桿全掃描","三重四極桿 MRM","TOF 全掃描","紅外光譜"],"a":1,
       "e":"三重四極桿 SRM/MRM 雜訊低、靈敏度高，是痕量定量首選。"},
      {"q":"要分析揮發性精油成分並比對質譜圖庫，選？","o":["LC-MS ESI","GC-MS(EI)","MALDI-TOF","ICP-MS"],"a":1,
       "e":"揮發、熱穩定分子用 GC-MS(EI)，碎片可比對標準質譜圖庫。"},
      {"q":"要在 24 小時內快速鑑定細菌種類，選？","o":["GC-MS","MALDI-TOF","凱氏定氮","UV-Vis"],"a":1,
       "e":"MALDI-TOF 以微生物蛋白質指紋比對資料庫，快速鑑定菌種。"},
      {"q":"三聚氰胺(極性、不揮發)殘留分析，最適合？","o":["GC-MS","LC-MS/MS","火焰光度計","折射計"],"a":1,
       "e":"三聚氰胺不揮發、極性，須 LC-MS/MS；MRM 127.1→85.1 高專一。"}
    ]
  },
  "sort": {
    "g4":{"steps":["樣品經 LC 分離後進入 ESI，分子被游離成離子","Q1：選出特定『母離子(precursor)』，擋掉其他離子",
       "Q2 碰撞室：與 Ar/N₂ 碰撞(CID)使母離子碎裂","Q3：從碎片中選出特定『子離子(product)』",
       "偵測器記錄該『母→子離子對』的訊號","多重反應偵測(MRM)：同時監測多組離子對進行定量"],
       "shuffle":[2,0,4,1,5,3],
       "ok":"🎉 順序正確！LC分離→游離→Q1選母→Q2碰撞→Q3選子→偵測/MRM。",
       "tip":"提示：先選母離子(Q1)，才碰撞碎裂(Q2)，再選子離子(Q3)；離子對訊號最後被偵測。"}
  },
  "calc": {
    "g6":{"answer":3.6,"tol":0.6,
      "ok":"🎉 正確！(194.0811−194.0804)/194.0804 × 10⁶ = 0.0007/194.08 × 10⁶ ≈ <b>3.6 ppm</b>(＜5 ppm，可定分子式)。",
      "bad":"再算算：誤差 = 測得−理論 = 0.0007，再除以理論值乘以 10⁶。",
      "hint":"提示：ppm = (194.0811−194.0804)/194.0804 × 10⁶ = 0.0007/194.0804 × 10⁶ ≈ 3.6。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"res","t":"n","star":True},{"k":"acc"},{"k":"cost","t":"n","star":True},{"k":"app"}],
    "rows":[
      {"m":"四極桿 Q","res":2,"acc":"單位質量","cost":2,"app":"例行定量·SIM"},
      {"m":"離子阱 IT","res":2,"acc":"單位質量","cost":2,"app":"多階 MSⁿ·結構解析"},
      {"m":"飛行時間 TOF","res":4,"acc":"高","cost":3,"app":"大分子·全掃描篩檢"},
      {"m":"Orbitrap","res":5,"acc":"極高(<5 ppm)","cost":4,"app":"未知物鑑定·農藥篩檢"},
      {"m":"FT-ICR","res":5,"acc":"最高","cost":5,"app":"同位素細結構"}
    ]
  }
}

dc.build_html(
  {"title":"質譜分析 Mass Spectrometry · Nielsen Ch11","brand":"MS · CH11"},
  S, CFG, OUT)
