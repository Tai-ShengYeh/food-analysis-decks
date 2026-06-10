# -*- coding: utf-8 -*-
"""Nielsen Ch20 Vitamin Analysis — SOIL HTML deck (原理 + 食藥署官方法 TFDAA0025/0012).
Sources: Nielsen Ch20 + TFDA TFDAA0025.00 (脂溶) + TFDAA0012.04 (水溶).
Uses ../soil_deck_common.py.  Run: python build_ch20.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
MAP_SVG = """
<svg viewBox="0 0 960 320">
 <text x="480" y="22" text-anchor="middle" class="lblb" font-size="15">13 種維生素：4 種脂溶性 ＋ 9 種水溶性</text>
 <!-- fat-soluble panel -->
 <rect x="20" y="44" width="280" height="250" rx="14" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
 <text x="160" y="70" text-anchor="middle" class="lblb" fill="#d9822b" font-size="15">脂溶性 (4)</text>
 <text x="160" y="88" text-anchor="middle" class="lbl">溶於油脂 · 會儲存 · 過量易中毒</text>
 <g font-size="14" font-weight="800">
  <rect x="44" y="104" width="100" height="40" rx="8" fill="#fff" stroke="#d9822b"/><text x="94" y="129" text-anchor="middle" fill="#15233f">A 視黃醇</text>
  <rect x="176" y="104" width="100" height="40" rx="8" fill="#fff" stroke="#d9822b"/><text x="226" y="129" text-anchor="middle" fill="#15233f">D 鈣化醇</text>
  <rect x="44" y="158" width="100" height="40" rx="8" fill="#fff" stroke="#d9822b"/><text x="94" y="183" text-anchor="middle" fill="#15233f">E 生育醇</text>
  <rect x="176" y="158" width="100" height="40" rx="8" fill="#fff" stroke="#d9822b"/><text x="226" y="183" text-anchor="middle" fill="#15233f">K 葉醌</text>
 </g>
 <text x="160" y="232" text-anchor="middle" class="lbl">缺乏：D→佝僂、K→凝血障礙</text>
 <text x="160" y="252" text-anchor="middle" class="lbl">分析：先皂化去油脂，再 HPLC</text>
 <!-- water-soluble panel -->
 <rect x="320" y="44" width="620" height="250" rx="14" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
 <text x="630" y="70" text-anchor="middle" class="lblb" fill="#1f6feb" font-size="15">水溶性 (9)：B 群 ×8 ＋ C</text>
 <text x="630" y="88" text-anchor="middle" class="lbl">溶於水 · 不易儲存 · 過量隨尿排出</text>
 <g font-size="13" font-weight="800">
  <rect x="344" y="104" width="92" height="38" rx="8" fill="#fff" stroke="#1f6feb"/><text x="390" y="128" text-anchor="middle" fill="#15233f">B₁ 硫胺</text>
  <rect x="448" y="104" width="92" height="38" rx="8" fill="#fff" stroke="#1f6feb"/><text x="494" y="128" text-anchor="middle" fill="#15233f">B₂ 核黃素</text>
  <rect x="552" y="104" width="92" height="38" rx="8" fill="#fff" stroke="#1f6feb"/><text x="598" y="128" text-anchor="middle" fill="#15233f">B₃ 菸鹼酸</text>
  <rect x="656" y="104" width="92" height="38" rx="8" fill="#fff" stroke="#1f6feb"/><text x="702" y="128" text-anchor="middle" fill="#15233f">B₅ 泛酸</text>
  <rect x="760" y="104" width="92" height="38" rx="8" fill="#fff" stroke="#1f6feb"/><text x="806" y="128" text-anchor="middle" fill="#15233f">B₆ 吡哆醇</text>
  <rect x="344" y="150" width="92" height="38" rx="8" fill="#fff" stroke="#1f6feb"/><text x="390" y="174" text-anchor="middle" fill="#15233f">B₇ 生物素</text>
  <rect x="448" y="150" width="92" height="38" rx="8" fill="#fff" stroke="#1f6feb"/><text x="494" y="174" text-anchor="middle" fill="#15233f">B₉ 葉酸</text>
  <rect x="552" y="150" width="92" height="38" rx="8" fill="#fff" stroke="#1f6feb"/><text x="598" y="174" text-anchor="middle" fill="#15233f">B₁₂ 鈷胺</text>
  <rect x="656" y="150" width="196" height="38" rx="8" fill="#fff" stroke="#1f6feb"/><text x="754" y="174" text-anchor="middle" fill="#15233f">C 抗壞血酸</text>
 </g>
 <text x="630" y="218" text-anchor="middle" class="lbl">缺乏：C→壞血病、B₁→腳氣病、B₃→糙皮病、B₁₂→惡性貧血</text>
 <text x="630" y="242" text-anchor="middle" class="lbl">分析：易氧化怕熱怕光 → 加抗氧化劑、避光；HPLC／微生物檢定</text>
</svg>"""

METHOD_SVG = """
<svg viewBox="0 0 920 280">
 <text x="460" y="24" text-anchor="middle" class="lblb" font-size="15">三大類維生素分析法：準確度 ↑ 與 操作簡便 ↑ 互為反向</text>
 <g font-size="13.5">
  <rect x="120" y="56" width="680" height="50" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="150" y="86" class="lblb">生物檢定 Bioassay</text>
  <text x="640" y="86" text-anchor="end" class="lbl">人/動物餵食(大鼠骨鈣化)；僅 D、B₁₂</text>
  <rect x="120" y="116" width="680" height="50" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="150" y="146" class="lblb">微生物檢定 Microbiological</text>
  <text x="640" y="146" text-anchor="end" class="lbl">乳酸菌生長量；僅水溶性、專一靈敏但費時</text>
  <rect x="120" y="176" width="680" height="50" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="150" y="206" class="lblb">化學法 Chemical (HPLC 主流)</text>
  <text x="640" y="206" text-anchor="end" class="lbl">快速準確精密；脂溶+水溶；可配 MS 測 vitamers</text>
 </g>
 <defs><marker id="vu" markerWidth="10" markerHeight="10" refX="4" refY="8" orient="auto"><path d="M4 0 L8 8 L0 8 Z" fill="#15233f"/></marker>
  <marker id="vd" markerWidth="10" markerHeight="10" refX="4" refY="2" orient="auto"><path d="M4 10 L8 2 L0 2 Z" fill="#8493ad"/></marker></defs>
 <line x1="40" y1="226" x2="40" y2="56" stroke="#15233f" stroke-width="2.4" marker-end="url(#vu)"/>
 <text x="22" y="150" text-anchor="middle" class="lblb" transform="rotate(-90 22 150)">準確度／精密度 ↑</text>
 <line x1="880" y1="56" x2="880" y2="226" stroke="#8493ad" stroke-width="2.4" marker-end="url(#vd)"/>
 <text x="900" y="150" text-anchor="middle" class="lbl" transform="rotate(90 900 150)">操作簡便 ↑</text>
</svg>"""

HPLC_SVG = """
<svg viewBox="0 0 980 200">
 <defs><marker id="ha" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="490" y="28" text-anchor="middle" class="lblb" font-size="15">官方法骨幹：萃取 → C18 反相分離 → PDA 多波長偵測 → 比對定量</text>
 <g font-size="13">
  <rect x="14" y="74" width="170" height="56" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="99" y="98" text-anchor="middle" class="lblb">檢體萃取</text><text x="99" y="117" text-anchor="middle" class="lbl">避光·抗氧化</text>
  <rect x="232" y="74" width="180" height="56" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="322" y="98" text-anchor="middle" class="lblb">HPLC · C18 管柱</text><text x="322" y="117" text-anchor="middle" class="lbl">梯度分離各維生素</text>
  <rect x="460" y="74" width="200" height="56" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="560" y="98" text-anchor="middle" class="lblb">PDA 光二極體陣列</text><text x="560" y="117" text-anchor="middle" class="lbl">同時多波長偵測</text>
  <rect x="708" y="78" width="258" height="48" rx="9" fill="#15233f"/>
  <text x="837" y="100" text-anchor="middle" fill="#fff" font-weight="800">滯留時間+吸收圖譜→定量</text>
  <text x="837" y="117" text-anchor="middle" fill="#cfe0f6" font-size="11">含量 = C×V/(M×1000)</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#ha)">
  <line x1="184" y1="102" x2="228" y2="102"/><line x1="412" y1="102" x2="456" y2="102"/><line x1="660" y1="102" x2="704" y2="102"/></g>
 <text x="490" y="170" text-anchor="middle" class="lbl">脂溶(TFDAA0025)：D 264／E 280／A 325 nm　·　水溶(TFDAA0012)：泛酸210／C·B₁ 240／B₂·菸鹼260／葉酸280／B₆ 290 nm</text>
</svg>"""

DCIP_SVG = """
<svg viewBox="0 0 940 200">
 <defs><marker id="da" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="470" y="24" text-anchor="middle" class="lblb" font-size="15">維生素 C 的 DCIP 滴定：抗壞血酸把藍/紅色 DCIP 還原成無色，終點轉玫瑰紅</text>
 <circle cx="100" cy="112" r="40" fill="#fff" stroke="#1f6feb" stroke-width="2.4"/>
 <text x="100" y="108" text-anchor="middle" class="lblb" font-size="12">抗壞血酸</text><text x="100" y="126" text-anchor="middle" class="lbl">(維生素C)</text>
 <text x="250" y="92" text-anchor="middle" class="lbl">滴入 DCIP 染料</text>
 <line x1="144" y1="112" x2="300" y2="112" stroke="#48597a" stroke-width="2.4" marker-end="url(#da)"/>
 <circle cx="350" cy="112" r="42" fill="#f6f9fd" stroke="#8493ad" stroke-width="2.4"/>
 <text x="350" y="108" text-anchor="middle" class="lblb" font-size="12">仍無色</text><text x="350" y="126" text-anchor="middle" class="lbl">DCIP 被還原</text>
 <text x="350" y="170" text-anchor="middle" class="lbl">還有 C → 染料持續褪色</text>
 <text x="540" y="92" text-anchor="middle" class="lbl">C 耗盡，再一滴</text>
 <line x1="396" y1="112" x2="552" y2="112" stroke="#48597a" stroke-width="2.4" marker-end="url(#da)"/>
 <circle cx="602" cy="112" r="42" fill="#e8417a" opacity=".85"/>
 <text x="602" y="108" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">玫瑰紅</text><text x="602" y="126" text-anchor="middle" fill="#fff" font-size="11">終點!</text>
 <text x="602" y="170" text-anchor="middle" class="lbl">過量 DCIP 在酸性呈玫瑰紅</text>
 <text x="800" y="100" text-anchor="middle" class="lbl">滴定量越多</text>
 <text x="800" y="120" text-anchor="middle" class="lblb" fill="#1f6feb">維生素C越多</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 20",
    "維他命<span style='color:var(--accent-2)'>分析</span>", "Vitamin Analysis",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>13 種維生素 · 脂溶 vs 水溶 · HPLC · 食藥署官方法 TFDAA0025／0012",
    ["4 脂溶 + 9 水溶","IU / %DV","皂化 · 三酶法","HPLC-PDA","營養標示查核"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">這顆綜合維他命錠標示<br><span class="hi">維生素C 500 mg、維生素D 800 IU</span>——是真的足量嗎？</div>
  <p class="subtitle" style="max-width:850px;margin:22px auto 0">維生素加太少達不到標示、加太多(脂溶性)可能中毒；<strong>營養標示要準</strong>。<br>
  維生素種類多、又怕光怕氧怕熱——怎麼把它們一一<strong>準確定量</strong>？這一章告訴你。</p>
  <div style="margin-top:24px"><span class="pill">營養標示查核</span><span class="pill">強化食品</span>
  <span class="pill">膳食評估</span><span class="pill">保健食品品管</span></div></div>""")

add(MOT, dc.kt("20.1 定義", "13 種維生素，分<span class='hi'>兩大家族</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + MAP_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:8px">維生素是微量就能維持代謝的有機物，人體多半不能自行合成，須從食物攝取。</p>')

add(MOT, dc.kt("關鍵差異", "脂溶 vs 水溶：<span class='hi'>性質決定方法</span>") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("🧈","脂溶性 A·D·E·K","溶於油脂、會在體內<strong>儲存</strong>(過量易中毒)；分析時先<strong>皂化</strong>去油脂、<strong>全程避光</strong>、加抗氧化劑","a") +
    dc.card("💧","水溶性 B 群·C","溶於水、不易儲存(過量隨尿排出)；<strong>易氧化、怕熱怕光</strong>，分析要加抗氧化劑、低 pH 保護","b") +
    '</div><div class="note" style="margin-top:14px">同樣是「維生素」，溶解性不同 → <strong>萃取、保存、偵測波長、甚至毒性</strong>都不一樣。</div>')

add(MOT, dc.kt("20.1.3 單位", "mg、IU、%DV 別<span class='hi'>搞混</span>") +
    '<div class="grid3" style="margin-top:18px">' +
    dc.card("⚖️","mg / µg","直接的<strong>質量</strong>單位，最直觀","b") +
    dc.card("💪","IU 國際單位","量的是<strong>生物活性(效力)</strong>，不是質量；每種維生素換算率不同","a") +
    dc.card("🏷️","%DV 每日值","佔每日建議攝取量的百分比，用於營養標示","g") + '</div>' +
    '<p class="subtitle" style="margin-top:14px">標示與品管常要在不同基準間換算——例如維生素 D「800 IU」要對應到質量才能用 HPLC 查核。</p>')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","脂溶性 vs 水溶性維生素", 8,
    "把 8 種維生素分到「脂溶性」或「水溶性」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("20.1.4 萃取", "每種維生素的萃取法<span class='hi'>都不同</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>脂溶 A·D·E</strong>：有機溶劑萃取 + <strong>皂化(saponification)</strong>——KOH 把三酸甘油酯水解成皂去除，維生素留下；加抗氧化劑防氧化</li>" +
    "<li><strong>維生素C</strong>：<strong>偏磷酸/醋酸冷萃</strong>，低 pH + 螯合劑防氧化</li>" +
    "<li><strong>B₁、B₂</strong>：酸中煮沸/高壓滅菌 + <strong>酶處理</strong></li>" +
    "<li><strong>葉酸</strong>：<strong>三酶法</strong>(α-澱粉酶、蛋白酶、γ-麩胺醯水解酶)</li>" +
    '</ul></div><div class="note"><strong>為什麼這麼講究？</strong><br>' +
    "維生素對<strong>光、氧、pH、熱</strong>都敏感；萃取要『放得出來又不破壞』，所以每種維生素有專屬配方。</div></div>")

add(ATT, dc.kt("20.1.5 三大方法類", "從生物到化學，<span class='hi'>各有取捨</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + METHOD_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:8px">越往化學法：越準確精密、但儀器與技術門檻越高；越往生物法：越接近生理活性、但慢又粗略。</p>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","維生素分析原理測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("20.4 化學法主流", "為什麼<span class='hi'>HPLC</span> 成為首選") +
    '<div class="svgwrap" style="margin-top:4px">' + HPLC_SVG + '</div>' +
    '<div class="note" style="margin-top:8px"><strong>HPLC/UHPLC</strong>相對簡單、準確、精密，可同時分析多種維生素；接上<strong>質譜(LC-MS/MS)</strong>還能分辨' +
    "同一維生素的不同形式(<strong>vitamers</strong>)、提高靈敏與專一。但層析是『分離』不是『鑑定』，須先確認峰的身分與純度。</div>")

add(ATT, dc.kt("20.4.2 維生素C經典法", "DCIP 滴定：<span class='hi'>顏色</span>告訴你終點") +
    '<div class="svgwrap" style="margin-top:6px">' + DCIP_SVG + '</div>' +
    '<div class="note" style="margin-top:8px">抗壞血酸把氧化還原指示染料 <strong>2,6-二氯靛酚(DCIP)</strong> 還原成無色；當維生素C耗盡，過量 DCIP 在酸性下呈' +
    "<strong>玫瑰紅</strong>為終點。深色樣品看不出顏色時，改用分光光度計於 <strong>545 nm</strong> 判讀。</div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","三大方法類配特徵", 6,
    "把 6 個敘述分到「生物檢定」「微生物檢定」或「化學法 HPLC」。"), ' data-game="g3"')

add(ATT, dc.kt("官方法實戰 ①", "脂溶性維生素 · <span class='hi'>TFDAA0025</span>") +
    '<div class="grid2" style="margin-top:14px"><div><ul class="clean">' +
    "<li>適用<strong>膠囊/錠狀</strong>食品中 <strong>7 品項</strong>：A、A 醋酸酯、A 棕櫚酸酯、D₂、D₃、E、E 醋酸酯</li>" +
    "<li><strong>HPLC + 光二極體陣列(PDA)</strong>、C18 反相管柱、甲醇/水梯度</li>" +
    "<li>三段定量波長：<strong>D 264 / E 280 / A 325 nm</strong></li>" +
    "<li>加 <strong>BHT 抗氧化</strong>、<strong>全程避光</strong>；DMSO + 正己烷萃取</li>" +
    '</ul></div><div class="note"><strong>為何避光加 BHT？</strong><br>' +
    "A、D、E 對光與氧極敏感，會降解失準；BHT 與避光是脂溶維生素分析的鐵律。</div></div>")

add(ATT, dc.kt("官方法實戰 ②", "水溶性維生素 · <span class='hi'>TFDAA0012</span>") +
    '<div class="grid2" style="margin-top:14px"><div><ul class="clean">' +
    "<li>適用膠囊/錠狀食品中 <strong>9 品項</strong>：B₁、B₂、菸鹼酸、菸鹼醯胺、泛酸、B₆、葉酸、L-5-甲基四氫葉酸鈣、C</li>" +
    "<li><strong>HPLC-PDA</strong>、C18 管柱、磷酸鉀緩衝/乙腈梯度</li>" +
    "<li>多段波長：泛酸 210／C·B₁ 240／B₂·菸鹼 260／葉酸 280／B₆ 290 nm</li>" +
    "<li>加 <strong>L-半胱胺酸</strong>抗氧化(保護維生素C)；維生素C 標準液臨用配製</li>" +
    '</ul></div><div class="note"><strong>關鍵：</strong>維生素C最容易消失，' +
    "所以水溶法用 <strong>L-半胱胺酸</strong>當還原保護劑、標準液現配現用。</div></div>")

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","脂溶維生素 HPLC 檢驗流程排序", 6,
    "用 ▲▼ 把脂溶性維生素(TFDAA0025)的 6 個檢驗步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.chart_inner("wavelength", "為什麼要用<span class='hi'>PDA 多波長</span>",
    "各維生素的定量波長不同(nm)，光二極體陣列(PDA)可一次同時偵測多個波長。整合自 TFDAA0025／0012。",
    kicker="偵測設計", height="50vh"), ' data-chart="wavelength"')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對維生素分析法", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("四種分析路線一覽（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"acc","t":"n","label":"準確度","star":True},
     {"k":"v","t":"s","label":"適用維生素"},{"k":"feat","t":"s","label":"特點"}],
    "★ 越多越準確。整合自 20.2–20.4。", kicker="20.5 方法比較"), ' data-game="cmp"')

add(ACT, dc.chart_inner("rt", "水溶性維生素的<span class='hi'>HPLC 滯留時間</span>",
    "整合自 TFDAA0012.04 參考層析圖譜(分)。C18 反相管柱可把 9 種水溶性維生素逐一分開。",
    kicker="層析分離", height="52vh"), ' data-chart="rt"')

add(ACT, dc.kt("應用與品管", "維生素分析在<span class='hi'>守護</span>什麼") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🏷️","營養標示查核","確認『維生素C 500mg』『維生素D 800IU』屬實、無誇大或不足","b") +
    dc.card("➕","強化食品","麵粉、奶粉、機能飲料的維生素強化是否達標、有無過量","a") +
    dc.card("💊","保健食品","綜合維他命膠囊/錠的含量與安定性(脂溶性過量有風險)","g") +
    dc.card("🎯","品質保證","以標準參考物質(SRM)查核準確度、做方法確效","b") + '</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：維生素含量",
    "脂溶官方法：取樣 <b>M = 0.5 g</b>、最後定容 <b>V = 2 mL</b>；由標準曲線得維生素A濃度 "
    "<b>C = 10 µg/mL</b>。求含量(mg/g)。公式：C×V/(M×1000)。", unit="mg/g"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>13 種維生素＝<strong>4 脂溶(A·D·E·K)＋9 水溶(B 群·C)</strong>；溶解性決定方法</li>" +
    "<li>單位：mg／<strong>IU(活性)</strong>／%DV(每日值)要會換算</li>" +
    "<li>萃取因維生素而異：脂溶<strong>皂化</strong>、葉酸<strong>三酶</strong>、C<strong>冷萃低pH</strong></li></ul>" +
    '<ul class="clean"><li>三大方法類：生物＜微生物＜<strong>化學(HPLC)</strong>(準確度遞增)</li>' +
    "<li>官方法：脂溶 TFDAA0025(避光+BHT)、水溶 TFDAA0012(L-半胱胺酸)，皆 <strong>HPLC-PDA</strong></li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說出 13 種維生素與脂溶／水溶的分類及差異",
     "解釋 mg、IU、%DV 的不同(IU 量的是活性)",
     "說明為何各維生素萃取法不同、皂化與三酶法的用途",
     "比較生物檢定、微生物檢定與化學法(HPLC)的取捨",
     "描述維生素C的 DCIP 滴定原理與終點顏色",
     "說出脂溶(TFDAA0025)與水溶(TFDAA0012)官方法的儀器、波長與抗氧化策略",
     "依序排出脂溶維生素 HPLC 檢驗流程",
     "用 C×V/(M×1000) 計算維生素含量"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把維生素分析<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions(萃取步驟、為何避光、DCIP 是否低/高估、HPLC 優缺)<br>"
    "🔜 銜接：<strong>紫外可見光譜 (Ch7)</strong>、<strong>HPLC (Ch13)</strong>、<strong>質譜 (Ch11)</strong>、食藥署 HPLC 公告法<br>"
    "🧪 思考：你的樣品是脂溶還水溶維生素？怕光怕氧嗎？要 HPLC、微生物還是滴定法？標示是 mg 還 IU？",
    ["脂溶/水溶","HPLC-PDA","皂化","DCIP 滴定","營養標示"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "wavelength": {"type":"bar","yTitle":"定量波長 (nm)",
      "labels":["泛酸B₅","維生素C","B₂/菸鹼","D₂/D₃","E","B₆","維生素A"],
      "datasets":[{"label":"定量波長 (nm)","data":[210,240,260,264,280,290,325],"color":"#1f6feb"}]},
    "rt": {"type":"bar","yTitle":"滯留時間 (分)",
      "labels":["維生素C","菸鹼酸","B₁","B₆","菸鹼醯胺","泛酸","L-5-MTHF","葉酸","B₂"],
      "datasets":[{"label":"滯留時間 (min)","data":[3.43,5.38,6.61,9.61,11.33,14.45,17.30,20.19,22.50],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["脂溶性維生素","水溶性維生素"],
      "items":[{"t":"維生素 A (視黃醇)","c":"脂溶性維生素"},{"t":"維生素 D","c":"脂溶性維生素"},
        {"t":"維生素 E (生育醇)","c":"脂溶性維生素"},{"t":"維生素 K","c":"脂溶性維生素"},
        {"t":"維生素 C (抗壞血酸)","c":"水溶性維生素"},{"t":"維生素 B₁ (硫胺)","c":"水溶性維生素"},
        {"t":"葉酸 (B₉)","c":"水溶性維生素"},{"t":"維生素 B₁₂ (鈷胺)","c":"水溶性維生素"}],
      "ok":"🎉 全對！A·D·E·K 脂溶(會儲存)、B 群與 C 水溶(易排出、易氧化)。",
      "tip":"提示：只有 A、D、E、K 是脂溶；B 群與 C 都是水溶。"},
    "g3": {"cats":["生物檢定","微生物檢定","化學法 HPLC"],
      "items":[{"t":"以大鼠骨鈣化(line test)測維生素D","c":"生物檢定"},
        {"t":"主要僅用於維生素 D 與 B₁₂","c":"生物檢定"},
        {"t":"以乳酸菌生長量測定","c":"微生物檢定"},
        {"t":"僅限水溶性維生素、專一但費時","c":"微生物檢定"},
        {"t":"簡單、準確、精密，現今主流","c":"化學法 HPLC"},
        {"t":"可同時分析多種、配 MS 測 vitamers","c":"化學法 HPLC"}],
      "ok":"🎉 正確！生物檢定接近生理活性、微生物檢定專一靈敏、HPLC 快速準確為主流。",
      "tip":"提示：動物餵食→生物；乳酸菌生長→微生物；管柱+波長→化學 HPLC。"}
  },
  "mcq": {
    "g2":[
      {"q":"13 種維生素中，脂溶性有幾種？","o":["2","4","9","13"],"a":1,
       "e":"脂溶性 4 種(A、D、E、K)，其餘 9 種(B 群 8 + C)為水溶性。"},
      {"q":"國際單位(IU)量的是維生素的什麼？","o":["質量","生物活性(效力)","體積","熔點"],"a":1,
       "e":"IU 衡量生物活性/效力而非質量，各維生素換算率不同。"},
      {"q":"分析脂溶性維生素時，去除油脂常用的步驟是？","o":["皂化(saponification)","發酵","蒸餾","滴定"],"a":0,
       "e":"以 KOH 皂化把三酸甘油酯水解成皂去除，留下脂溶維生素。"},
      {"q":"葉酸萃取常用的特殊處理是？","o":["皂化","三酶法(trienzyme)","通氮蒸餾","灰化"],"a":1,
       "e":"葉酸用 α-澱粉酶、蛋白酶、γ-麩胺醯水解酶的三酶法釋出。"},
      {"q":"就『準確度與精密度』而言，三大方法類的高低順序是？","o":["生物 > 微生物 > 化學","化學 > 微生物 > 生物","三者相同","微生物最高"],"a":1,
       "e":"準確度：化學(HPLC) > 微生物 > 生物；操作簡便則相反。"}
    ],
    "g5":[
      {"q":"要測膠囊中的脂溶性維生素 A／D／E，最適合的官方法是？","o":["微生物檢定","HPLC-PDA(TFDAA0025)","DCIP 滴定","大鼠生物檢定"],"a":1,
       "e":"脂溶性維生素以 HPLC-PDA(TFDAA0025)分析，三波長定量。"},
      {"q":"水溶官方法為了保護最易氧化的維生素C，加入什麼？","o":["BHT","L-半胱胺酸","氯化鈉","蔗糖"],"a":1,
       "e":"水溶法加 L-半胱胺酸當還原保護劑，並現配維生素C標準液。"},
      {"q":"脂溶性維生素檢驗為何要全程避光並加 BHT？","o":["增色","A·D·E 對光與氧敏感、易降解","加快流速","降低成本"],"a":1,
       "e":"脂溶維生素怕光怕氧，避光+BHT 抗氧化可防降解失準。"},
      {"q":"要分辨同一維生素的不同形式(vitamers)並提高靈敏，宜用？","o":["DCIP 滴定","HPLC-UV","LC-MS/MS","折射計"],"a":2,
       "e":"LC-MS/MS 可辨識 vitamers、提高靈敏與專一。"},
      {"q":"深色果汁用 DCIP 滴定看不出玫瑰紅終點，怎麼辦？","o":["放棄","改用分光光度計於 545 nm 判讀","加更多染料","加熱"],"a":1,
       "e":"有色樣品改測 545 nm 透光率變化判斷終點。"}
    ]
  },
  "sort": {
    "g4":{"steps":["取膠囊/錠狀檢體均質、精確稱重(避光)","加 75% DMSO 溶液，超音波振盪",
       "加正己烷振盪萃取，4300×g 離心取上層(重複)","氮氣吹乾，以含 BHT 乙醇復溶定容、過濾",
       "注入 HPLC，C18 管柱以甲醇/水梯度分離","PDA 於 D264／E280／A325 nm 測定，比對滯留時間與圖譜定量"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！秤樣→DMSO超音波→正己烷萃取離心→吹乾復溶→HPLC分離→PDA定量。",
       "tip":"提示：先萃取(DMSO+正己烷)、離心取上層，吹乾復溶後才上 HPLC；偵測在最後一步。"}
  },
  "calc": {
    "g6":{"answer":0.04,"tol":0.004,
      "ok":"🎉 正確！含量 = C×V/(M×1000) = 10×2/(0.5×1000) = 20/500 = <b>0.04 mg/g</b>(＞LOQ 0.002)。",
      "bad":"再算算：含量 = C×V/(M×1000) = 10×2/(0.5×1000)。",
      "hint":"提示：分子 10×2=20；分母 0.5×1000=500；20/500 = 0.04 mg/g。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"acc","t":"n","star":True},{"k":"v"},{"k":"feat"}],
    "rows":[
      {"m":"生物檢定 Bioassay","acc":2,"v":"主要 D、B₁₂","feat":"接近生理活性·慢且粗略·現少用"},
      {"m":"微生物檢定","acc":4,"v":"水溶性維生素","feat":"專一靈敏·費時·需嚴格操作"},
      {"m":"化學-滴定/螢光","acc":3,"v":"C(DCIP)·B₁(硫胺色素)·B₂","feat":"古典·設備簡單·專屬"},
      {"m":"化學-HPLC/UHPLC","acc":5,"v":"脂溶+水溶大多數","feat":"快速準確精密·主流·配MS測vitamers"}
    ]
  }
}

dc.build_html(
  {"title":"維他命分析 Vitamin Analysis · Nielsen Ch20 + TFDA","brand":"VITAMIN · CH20"},
  S, CFG, OUT)
