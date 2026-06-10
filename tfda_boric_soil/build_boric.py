# -*- coding: utf-8 -*-
"""TFDA TFDAA0086 食品中硼酸之鑑別/檢驗 (薑黃素分光光度法) — SOIL HTML deck.
Source: 食藥署建議檢驗方法 TFDAA0086 + 食品藥物研究年報 13:50-57(2022). Run: python build_boric.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
COLOR_SVG = """
<svg viewBox="0 0 940 200">
 <defs><marker id="ba" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="470" y="26" text-anchor="middle" class="lblb" font-size="15">薑黃素呈色：硼酸 → 玫瑰紅(定量)，加氨 → 變綠(確認)</text>
 <circle cx="90" cy="110" r="40" fill="#fff" stroke="#d9822b" stroke-width="2.4"/>
 <text x="90" y="106" text-anchor="middle" class="lblb" font-size="12">薑黃素</text><text x="90" y="124" text-anchor="middle" class="lbl">curcumin(黃)</text>
 <text x="240" y="92" text-anchor="middle" class="lbl">+ 硼酸(酸性)</text>
 <line x1="134" y1="110" x2="300" y2="110" stroke="#48597a" stroke-width="2.4" marker-end="url(#ba)"/>
 <circle cx="350" cy="110" r="44" fill="#e23b5a" opacity=".85"/>
 <text x="350" y="106" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">玫瑰紅</text>
 <text x="350" y="124" text-anchor="middle" fill="#fff" font-size="11">rosocyanine</text>
 <text x="350" y="172" text-anchor="middle" class="lbl">550 nm 吸收 → 定量</text>
 <text x="520" y="92" text-anchor="middle" class="lbl">+ 氨水(鹼)</text>
 <line x1="396" y1="110" x2="560" y2="110" stroke="#48597a" stroke-width="2.4" marker-end="url(#ba)"/>
 <circle cx="610" cy="110" r="44" fill="#1f6b4a" opacity=".85"/>
 <text x="610" y="106" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">墨綠/藍</text>
 <text x="610" y="124" text-anchor="middle" fill="#fff" font-size="11">變色確認</text>
 <text x="610" y="172" text-anchor="middle" class="lbl">紅→綠 → 確認是硼</text>
 <text x="800" y="100" text-anchor="middle" class="lbl">紅越深</text>
 <text x="800" y="120" text-anchor="middle" class="lblb" fill="#e23b5a">硼酸越多</text>
</svg>"""

FLOW_SVG = """
<svg viewBox="0 0 1000 180">
 <defs><marker id="fb" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="500" y="30" text-anchor="middle" class="lblb" font-size="15">新法 TFDAA0086：免灰化、可客觀定量</text>
 <g font-size="13">
  <rect x="14" y="70" width="175" height="58" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="101" y="95" text-anchor="middle" class="lblb">檢體萃取</text><text x="101" y="114" text-anchor="middle" class="lbl">己烷/乙酸乙酯</text>
  <rect x="237" y="70" width="175" height="58" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="324" y="95" text-anchor="middle" class="lblb">加薑黃素試劑</text><text x="324" y="114" text-anchor="middle" class="lbl">酸性下衍生</text>
  <rect x="460" y="70" width="175" height="58" rx="10" fill="#fbe7e7" stroke="#e23b5a" stroke-width="2.2"/>
  <text x="547" y="95" text-anchor="middle" class="lblb">呈玫瑰紅</text><text x="547" y="114" text-anchor="middle" class="lbl">rosocyanine</text>
  <rect x="683" y="70" width="175" height="58" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="770" y="95" text-anchor="middle" class="lblb">550 nm 測吸光</text><text x="770" y="114" text-anchor="middle" class="lbl">分光光度計</text>
  <rect x="900" y="74" width="96" height="50" rx="9" fill="#15233f"/>
  <text x="948" y="103" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">定量</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#fb)">
  <line x1="189" y1="99" x2="233" y2="99"/><line x1="412" y1="99" x2="456" y2="99"/>
  <line x1="635" y1="99" x2="679" y2="99"/><line x1="858" y1="99" x2="896" y2="99"/></g>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("食藥署建議檢驗方法 · TFDAA0086",
    "食品中<span style='color:var(--accent-2)'>硼酸</span>檢驗", "Boric Acid in Foods",
    "食品安全檢測　·　3 小時課程　·　含 6 個互動小遊戲<br>硼砂(禁用) · 薑黃素呈色 · 玫瑰紅 rosocyanine · 550 nm 分光光度",
    ["違法添加硼砂","薑黃素呈色","玫瑰紅 550nm","免灰化定量","累積性中毒"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">為什麼有些<span class="hi">油麵、年糕、魚丸</span><br>特別 Q 彈、又特別耐放？</div>
  <p class="subtitle" style="max-width:840px;margin:22px auto 0">可能違法加了<strong>硼砂(硼酸鈉)</strong>——增加脆度、Q 彈與保存性。<br>
  但硼酸/硼砂在台灣是<strong>禁用的非法添加物</strong>，會在體內累積中毒。食藥署 <strong>TFDAA0086</strong> 教你怎麼驗。</p>
  <div style="margin-top:24px"><span class="pill">增加Q彈脆度</span><span class="pill">非法添加</span>
  <span class="pill">累積中毒</span><span class="pill">薑黃素呈色</span></div></div>""")

add(MOT, dc.kt("背景", "硼砂為什麼<span class='hi'>危險</span>") +
    '<div class="grid2" style="margin-top:20px">' +
    dc.card("🍜","為何被加","增加 Q 彈、脆度與彈性，延長保存——口感與賣相變好","b") +
    dc.card("🚫","台灣禁用","硼酸及硼砂屬<strong>非法食品添加物</strong>，不得用於食品","a") +
    dc.card("☠️","累積中毒","在體內不易代謝、會累積；急性會噁心嘔吐腹瀉，高劑量影響生殖甚至致死","b") +
    dc.card("🍙","常見食品","油麵、年糕、紅龜粿、粽子、魚丸、蝦等講求口感的製品","g") + '</div>')

add(MOT, dc.kt("呈色原理", "薑黃素遇硼酸<span class='hi'>變玫瑰紅</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + COLOR_SVG + '</div>' +
    '<div class="note" style="margin-top:10px">硼酸在酸性下與<strong>薑黃素(curcumin)</strong>結合，生成紅色的 <strong>rosocyanine</strong>(玫瑰紅)，' +
    "在 <strong>550 nm</strong> 有最大吸收→可定量；紅斑再<strong>加氨變墨綠</strong>，可確認確實是硼。</div>")

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","薑黃試紙(舊) vs 分光光度(新)", 8,
    "把 8 個特徵分到「舊法：薑黃試紙(定性)」或「新法 TFDAA0086：分光光度(定量)」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("為什麼要改良", "舊薑黃試紙法的<span class='hi'>痛點</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>舊公告法(MOHWA0014)屬<strong>定性鑑別</strong>，只能說『有/沒有』</li>" +
    "<li>樣品要先<strong>灰化</strong>，前處理<strong>耗時</strong></li>" +
    "<li>看<strong>試紙顏色</strong>判讀，容易受<strong>主觀</strong>影響</li>" +
    "<li>紅色食品(紅麴米、紫米、湯圓)的天然色素會干擾判讀</li>" +
    '</ul></div><div class="note"><strong>新法 TFDAA0086 的解方：</strong><br>' +
    "免灰化、直接萃取衍生呈色，用<strong>分光光度計讀數值</strong>客觀定量；以正己烷/乙酸乙酯取代有毒的氯仿，紅色食品也不干擾。</div></div>")

add(ATT, dc.kt("新法流程", "萃取 → 呈色 → 550 nm") +
    '<div class="svgwrap" style="margin-top:6px">' + FLOW_SVG + '</div>' +
    '<div style="margin-top:8px"><span class="pill">萃取溶劑：n-己烷/乙酸乙酯(1:1)</span><span class="pill">薑黃素 + EHD 衍生</span>'
    '<span class="pill">玫瑰紅 rosocyanine</span><span class="pill">550 nm 讀吸光度</span><span class="pill">LOQ 300 mg/kg</span></div>')

add(ATT, dc.kt("試劑與儀器", "呈色與定量的<span class='hi'>關鍵角色</span>") +
    '<div class="grid3" style="margin-top:16px">' +
    dc.card("🌕","薑黃素 curcumin","與硼酸結合呈玫瑰紅(rosocyanine)的顯色劑","a") +
    dc.card("🧴","EHD / 己烷-乙酸乙酯","2-乙基-1,3-己二醇與萃取溶劑；取代有毒氯仿","b") +
    dc.card("📟","分光光度計","在 550 nm 讀吸光度，依檢量線定量","g") + '</div>' +
    '<p class="subtitle" style="margin-top:12px">另用亞鐵氰化鉀、醋酸鋅澄清/除蛋白；呈色後在 550 nm 量測。</p>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","硼酸方法即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("定性 vs 定量", "兩種思路<span class='hi'>互補</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🟥→🟩","薑黃試紙(定性)","試紙呈紅棕色 → 加氨變墨綠即確認有硼；現場、快速、但主觀、不能給數值","a") +
    dc.card("📈","分光光度(定量)","薑黃素衍生呈玫瑰紅，550 nm 讀吸光度，對照<strong>檢量線</strong>得濃度→客觀數值","b") +
    '</div><div class="note" style="margin-top:14px"><strong>互補：</strong>試紙適合現場初步鑑別；分光光度法(TFDAA0086)給可追溯的<strong>定量結果</strong>。</div>')

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","為何添加 vs 健康危害", 6,
    "把 6 個敘述分到「為何被違法添加」或「對健康的危害」。"), ' data-game="g3"')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","硼酸分光光度法流程排序", 6,
    "用 ▲▼ 把 TFDAA0086 分光光度法的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：硼酸判斷", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("硼酸的幾種檢驗法（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"quant","t":"n","label":"定量能力","star":True},
     {"k":"eq","t":"s","label":"設備"},{"k":"use","t":"s","label":"特點"}],
    "★ 越多越能定量。TFDAA0086 為薑黃素分光光度法。", kicker="方法比較"), ' data-game="cmp"')

add(ACT, dc.chart_inner("calib", "薑黃素法的<span class='hi'>檢量線</span>",
    "硼酸濃度(µg/mL) 對 550 nm 吸光度，呈良好線性(示意，y≈0.095x，r≈0.99995)，符合比爾定律。",
    kicker="定量基礎", height="50vh"), ' data-chart="calib"')

add(ACT, dc.kt("健康與法規", "為什麼<span class='hi'>絕不能</span>加") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧬","會累積","硼在體內排除慢、會累積，反覆攝取風險升高","b") +
    dc.card("🤢","急性中毒","噁心、嘔吐、腹瀉、紅斑；嚴重影響肝腎與生殖","a") +
    dc.card("⚖️","法規","硼酸/硼砂為<strong>非法添加物</strong>，食品中<strong>不得檢出</strong>(非『限量』)","g") +
    dc.card("🍢","稽查重點","Q 彈魚丸、脆貢丸、油麵、年糕、粽子等是抽驗常見對象","b") + '</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：由吸光度求濃度",
    "薑黃素法檢量線為 <b>Abs = 0.095 × C</b>(C 單位 µg/mL)。某檢體呈色液測得 <b>Abs = 0.570</b>。"
    "求硼酸濃度 C。", unit="µg/mL"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>硼酸/硼砂是<strong>非法添加物</strong>，加在 Q 彈/脆度食品，會累積中毒</li>" +
    "<li>呈色原理：硼酸 + <strong>薑黃素</strong>(酸性)→ 玫瑰紅 rosocyanine</li>" +
    "<li>定量：<strong>550 nm</strong> 分光光度，對照檢量線(比爾定律)</li></ul>" +
    '<ul class="clean"><li>定性確認：紅斑<strong>加氨變墨綠</strong>(紅→綠)</li>' +
    "<li>TFDAA0086 比舊薑黃試紙法<strong>免灰化、可定量、紅色食品不干擾</strong></li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明硼砂為何被違法添加、有哪些健康危害",
     "寫出硼酸與薑黃素呈色(玫瑰紅 rosocyanine)的原理",
     "說明為何在 550 nm 測定吸光度",
     "比較舊薑黃試紙法與新分光光度法(TFDAA0086)的差異",
     "解釋『加氨變墨綠』作為確認反應的意義",
     "由檢量線吸光度推算硼酸濃度(比爾定律)",
     "說明新法為何用己烷/乙酸乙酯取代氯仿",
     "指出硼酸在食品中是『不得檢出』而非『限量』"]))

add(ACT, dc.cover("延伸 · CONNECT",
    "從一顆魚丸<br><span style='color:var(--accent-2)'>看懂硼砂</span>", "",
    "🔗 對照：本法是<strong>呈色/分光光度</strong>路線，與滴定(SO₂)、LC-MS/MS(甜味劑/四環素)互補<br>"
    "🔬 銜接：<strong>紫外可見光譜 (Ch7)</strong>、比爾定律、食品添加物管理<br>"
    "🧪 思考：紅色食品為何會干擾舊法？分光光度法如何避免？『不得檢出』與『限量』有何不同？",
    ["硼砂(禁用)","薑黃素","玫瑰紅 550nm","分光光度","食安檢測"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "calib": {"type":"line","yTitle":"吸光度 Abs (550 nm)",
      "labels":["3","5","7","9","10"],
      "datasets":[{"label":"Abs = 0.095 × C","data":[0.285,0.475,0.665,0.855,0.95],"color":"#e23b5a"}]}
  },
  "bucket": {
    "g1": {"cats":["舊法：薑黃試紙(定性)","新法 TFDAA0086：分光光度(定量)"],
      "items":[{"t":"屬定性鑑別(只能說有/沒有)","c":"舊法：薑黃試紙(定性)"},
        {"t":"樣品需先灰化、較耗時","c":"舊法：薑黃試紙(定性)"},
        {"t":"以試紙顏色判讀(紅棕→加氨變墨綠)","c":"舊法：薑黃試紙(定性)"},
        {"t":"結果易受主觀判讀影響","c":"舊法：薑黃試紙(定性)"},
        {"t":"可定量(讀吸光度給數值)","c":"新法 TFDAA0086：分光光度(定量)"},
        {"t":"免灰化、直接萃取衍生呈色","c":"新法 TFDAA0086：分光光度(定量)"},
        {"t":"以 550 nm 分光光度測定","c":"新法 TFDAA0086：分光光度(定量)"},
        {"t":"用 n-己烷/乙酸乙酯取代有毒氯仿","c":"新法 TFDAA0086：分光光度(定量)"}],
      "ok":"🎉 全對！舊法定性、需灰化、主觀；新法免灰化、550 nm 客觀定量。",
      "tip":"提示：跟『試紙、灰化、定性、主觀』有關→舊法；跟『吸光度、550nm、定量、客觀』有關→新法。"},
    "g3": {"cats":["為何被違法添加","對健康的危害"],
      "items":[{"t":"讓油麵、年糕更 Q 彈有嚼勁","c":"為何被違法添加"},
        {"t":"讓魚丸、貢丸更脆、外觀更好","c":"為何被違法添加"},
        {"t":"延長保存、防止腐敗","c":"為何被違法添加"},
        {"t":"在體內不易代謝、會累積","c":"對健康的危害"},
        {"t":"急性中毒會噁心、嘔吐、腹瀉","c":"對健康的危害"},
        {"t":"高劑量影響生殖、甚至致死","c":"對健康的危害"}],
      "ok":"🎉 正確！口感/保存→被加的理由；累積/中毒/生殖毒性→危害。",
      "tip":"提示：跟『口感、賣相、保存』有關→添加理由；跟『中毒、累積、器官』有關→危害。"}
  },
  "mcq": {
    "g2":[
      {"q":"TFDAA0086 用什麼顯色劑與硼酸呈色？","o":["茚三酮","薑黃素(curcumin)","酚酞","碘","茴香醛"],"a":1,
       "e":"硼酸在酸性下與薑黃素結合成玫瑰紅(rosocyanine)。"},
      {"q":"呈色後在哪個波長測定吸光度？","o":["280 nm","410 nm","550 nm","700 nm"],"a":2,
       "e":"rosocyanine 在 550 nm 有最大吸收，故於 550 nm 定量。"},
      {"q":"紅棕色斑『加氨變墨綠』的用途是？","o":["增加靈敏度","確認確實是硼(定性確認)","稀釋","加快反應"],"a":1,
       "e":"加氨(鹼)使紅色轉墨綠，是確認反應、排除其他紅色干擾。"},
      {"q":"新法相較舊薑黃試紙法的主要優點是？","o":["更便宜","免灰化、可客觀定量、紅色食品不干擾","不需試劑","可現場目視"],"a":1,
       "e":"新法免灰化、用分光光度客觀定量，並改善紅色食品干擾。"},
      {"q":"硼酸/硼砂在台灣食品的法規定位是？","o":["合法添加物","限量使用","非法添加物(不得檢出)","僅限外銷"],"a":2,
       "e":"硼酸與硼砂為非法食品添加物，食品中不得檢出。"}
    ],
    "g5":[
      {"q":"想對 Q 彈魚丸做現場快速初步鑑別，較適合？","o":["ICP-MS","薑黃試紙法","離子層析","凱氏定氮"],"a":1,
       "e":"薑黃試紙法可現場快速定性鑑別；確認與定量再送分光光度法。"},
      {"q":"檢驗紅麴米製品的硼酸，為何優先選新法？","o":["比較便宜","紅色色素會干擾舊法的目視判讀","紅麴不含硼","新法不需儀器"],"a":1,
       "e":"紅色食品天然色素干擾舊法目視；新法經萃取衍生、550nm 定量較不受干擾。"},
      {"q":"TFDAA0086 以什麼取代有毒的氯仿作萃取/衍生溶劑？","o":["苯","n-己烷/乙酸乙酯","汽油","濃硫酸"],"a":1,
       "e":"以 n-己烷/乙酸乙酯(1:1)取代氯仿，較安全且回收率良好。"},
      {"q":"要測『總硼元素』而非僅硼酸鹽，最適合？","o":["薑黃試紙","薑黃素分光光度","ICP-MS","酸鹼滴定"],"a":2,
       "e":"ICP-MS 可超痕量測定總硼元素含量。"},
      {"q":"分光光度定量為何要做檢量線？","o":["美觀","由吸光度依比爾定律換算濃度","當空白","增加顏色"],"a":1,
       "e":"檢量線建立吸光度與濃度的線性關係(比爾定律)，據以定量。"}
    ]
  },
  "sort": {
    "g4":{"steps":["取檢體，以 n-己烷/乙酸乙酯萃取硼酸","加入薑黃素試劑，在酸性下衍生呈色",
       "生成玫瑰紅色 rosocyanine","以分光光度計在 550 nm 測定吸光度",
       "對照檢量線(Abs vs 濃度)換算硼酸濃度","以含量公式換算成檢體中硼酸含量(mg/kg)"],
       "shuffle":[2,0,4,1,5,3],
       "ok":"🎉 順序正確！萃取→加薑黃素衍生→呈玫瑰紅→550nm測吸光→對檢量線→算含量。",
       "tip":"提示：先萃取再加顯色劑呈色，呈色後才量吸光度、再對檢量線定量。"}
  },
  "calc": {
    "g6":{"answer":6.0,"tol":0.2,
      "ok":"🎉 正確！C = Abs/0.095 = 0.570/0.095 = <b>6.0 µg/mL</b>。",
      "bad":"再算算：由 Abs = 0.095×C，反解 C = Abs/0.095。",
      "hint":"提示：C = 0.570 / 0.095 = 6.0 µg/mL。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"quant","t":"n","star":True},{"k":"eq"},{"k":"use"}],
    "rows":[
      {"m":"薑黃試紙法(舊·定性)","quant":1,"eq":"薑黃試紙","use":"現場定性·需灰化·主觀"},
      {"m":"薑黃素分光光度(TFDAA0086)","quant":4,"eq":"分光光度計","use":"免灰化·客觀定量·LOQ 300mg/kg"},
      {"m":"ICP-MS","quant":5,"eq":"ICP-MS","use":"超痕量·測總硼元素"},
      {"m":"離子層析 IC","quant":4,"eq":"離子層析儀","use":"測硼酸鹽陰離子"}
    ]
  }
}

dc.build_html(
  {"title":"食品中硼酸檢驗 薑黃素分光光度法 · TFDAA0086","brand":"硼酸 · 分光光度"},
  S, CFG, OUT)
