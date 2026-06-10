# -*- coding: utf-8 -*-
"""TFDA MOHWA0030.00 食品中甜味劑之檢驗方法－多重分析 (LC-MS/MS) — SOIL HTML deck.
Source: 衛福部食藥署公告法 MOHWA0030.00. Run: python build_sweeteners.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
FLOW_SVG = """
<svg viewBox="0 0 1000 200">
 <defs><marker id="fa" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="500" y="34" text-anchor="middle" class="lblb" font-size="15">多重分析流程：一次驗 13 種甜味劑</text>
 <g font-size="13">
  <rect x="14" y="78" width="160" height="58" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="94" y="103" text-anchor="middle" class="lblb">檢體萃取</text><text x="94" y="122" text-anchor="middle" class="lbl">50%甲醇·超音波</text>
  <rect x="222" y="78" width="160" height="58" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="302" y="103" text-anchor="middle" class="lblb">LC 分離</text><text x="302" y="122" text-anchor="middle" class="lbl">Phenyl-Hexyl 管柱</text>
  <rect x="430" y="78" width="160" height="58" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="510" y="103" text-anchor="middle" class="lblb">ESI 游離</text><text x="510" y="122" text-anchor="middle" class="lbl">正/負離子切換</text>
  <rect x="638" y="78" width="160" height="58" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="718" y="103" text-anchor="middle" class="lblb">串聯質譜 MS/MS</text><text x="718" y="122" text-anchor="middle" class="lbl">MRM 離子對</text>
  <rect x="846" y="82" width="150" height="50" rx="9" fill="#15233f"/>
  <text x="921" y="106" text-anchor="middle" fill="#fff" font-weight="800">鑑別+定量</text>
  <text x="921" y="122" text-anchor="middle" fill="#cfe0f6" font-size="11">滯留時間+離子比</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#fa)">
  <line x1="176" y1="107" x2="218" y2="107"/><line x1="384" y1="107" x2="426" y2="107"/>
  <line x1="592" y1="107" x2="634" y2="107"/><line x1="800" y1="107" x2="842" y2="107"/></g>
</svg>"""

MRM_SVG = """
<svg viewBox="0 0 640 250">
 <text x="320" y="22" text-anchor="middle" class="lblb" font-size="15">MRM：一個母離子 → 定量+定性兩個子離子</text>
 <circle cx="90" cy="120" r="34" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.4"/>
 <text x="90" y="116" text-anchor="middle" class="lblb">母離子</text><text x="90" y="134" text-anchor="middle" class="lbl">precursor</text>
 <rect x="200" y="96" width="120" height="48" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
 <text x="260" y="116" text-anchor="middle" class="lblb">碰撞碎裂</text><text x="260" y="133" text-anchor="middle" class="lbl">CID</text>
 <line x1="124" y1="120" x2="196" y2="120" stroke="#48597a" stroke-width="2.4"/>
 <g>
  <circle cx="470" cy="70" r="28" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.4"/>
  <text x="470" y="66" text-anchor="middle" class="lblb" font-size="12">定量離子</text><text x="470" y="82" text-anchor="middle" class="lbl">quantifier</text>
  <circle cx="470" cy="172" r="28" fill="#fbe7e7" stroke="#d94f4f" stroke-width="2.4"/>
  <text x="470" y="168" text-anchor="middle" class="lblb" font-size="12">定性離子</text><text x="470" y="184" text-anchor="middle" class="lbl">qualifier</text>
  <line x1="322" y1="112" x2="442" y2="80" stroke="#48597a" stroke-width="2"/>
  <line x1="322" y1="128" x2="442" y2="164" stroke="#48597a" stroke-width="2"/></g>
 <text x="560" y="120" text-anchor="middle" class="lbl">兩者波峰面積比</text>
 <text x="560" y="138" text-anchor="middle" class="lbl">落在容許範圍</text>
 <text x="560" y="156" text-anchor="middle" class="lblb" fill="#1f9d6b">→ 確認身分</text>
 <text x="320" y="232" text-anchor="middle" class="lbl">例：醋磺內酯鉀 162＞82(定量)、162＞78(定性)；蔗糖素 414＞199、414＞216</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("食藥署公告檢驗方法 · MOHWA0030.00",
    "食品中<span style='color:var(--accent-2)'>甜味劑</span>檢驗", "Sweeteners in Foods · Multiple Analysis",
    "食品安全檢測　·　3 小時課程　·　含 6 個互動小遊戲<br>LC-MS/MS · ESI · MRM · 13 品項甜味劑 · 基質匹配檢量線",
    ["13 品項一次驗","LC-MS/MS","ESI 正/負","MRM 離子對","LOQ 0.01 g/kg"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">這瓶「無糖」飲料，<br>是真的無糖，還是偷加了<span class="hi">代糖</span>而且超標？</div>
  <p class="subtitle" style="max-width:840px;margin:22px auto 0">高倍甜味劑(代糖)用量極微就很甜，有<strong>使用範圍與限量</strong>，有的甚至<strong>禁用</strong>(如甘精)。<br>
  食藥署 <strong>MOHWA0030.00</strong> 用 <strong>LC-MS/MS</strong> 一次把 <strong>13 種</strong>甜味劑驗個清楚。</p>
  <div style="margin-top:24px"><span class="pill">合法但限量</span><span class="pill">違法添加</span>
  <span class="pill">禁用甘精</span><span class="pill">標示不實</span></div></div>""")

add(MOT, dc.kt("背景", "甜味劑為什麼要<span class='hi'>檢驗</span>") +
    '<div class="grid2" style="margin-top:20px">' +
    dc.card("🍬","高倍甜味劑","甜度為蔗糖數十至數千倍，微量就夠甜、熱量低","b") +
    dc.card("📏","有使用限量","各品項有可用食品範圍與最大限量，超量即違規","a") +
    dc.card("🚫","部分禁用","如對位乙氧苯脲(甘精, dulcin)在台灣禁用","b") +
    dc.card("🏷️","標示要誠實","『無糖/減糖』是否屬實、有無未標示之代糖","g") + '</div>')

add(MOT, dc.kt("方法總覽", "一次驗 13 種的<span class='hi'>流程</span>") +
    '<div class="svgwrap" style="margin-top:8px">' + FLOW_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:10px">檢體萃取 → 液相層析分離 → 電灑游離(ESI) → 串聯質譜 MRM → 以滯留時間與離子比鑑別並定量。</p>')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","天然 vs 人工甜味劑", 8,
    "把 8 種甜味劑分到「天然來源」或「人工合成」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("13 品項", "這次方法涵蓋的<span class='hi'>甜味劑</span>") +
    '<div class="grid3" style="margin-top:16px">' +
    dc.card("🧪","人工合成","醋磺內酯鉀、阿斯巴甜、糖精鈉、環己基磺醯胺酸鈉(甜精)、蔗糖素、紐甜、alitame、對位乙氧苯脲(甘精,禁用)","b") +
    dc.card("🌿","天然來源","甜菊糖(stevioside)、rebaudioside A、rebaudioside B、甘草素、新橘皮苷二氫查爾酮(NHDC)","g") +
    dc.card("🎯","定量極限","13 品項 LOQ 均為 <strong>0.01 g/kg</strong>","a") + '</div>' +
    '<p class="subtitle" style="margin-top:14px">同時涵蓋人工與天然代糖，一張方法、一次進樣全包。</p>')

add(ATT, dc.kt("為什麼用 LC-MS/MS", "極性、不揮發、要高專一") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>甜味劑多為<strong>極性、不揮發</strong>分子 → GC 不適合，用 <strong>液相層析(LC)</strong></li>" +
    "<li><strong>ESI</strong> 軟游離；本法<strong>正/負離子切換</strong>：阿斯巴甜等走 ESI⁺、糖精等走 ESI⁻</li>" +
    "<li>食品基質複雜 → 用<strong>串聯質譜 MS/MS</strong>提高選擇性、壓低雜訊</li>" +
    "<li>管柱 Eclipse Plus <strong>Phenyl-Hexyl</strong>，甲酸銨/甲醇梯度，流速 0.35 mL/min</li>" +
    '</ul></div><div class="note"><strong>關鍵字：</strong>LC 分離 + ESI 游離 + MRM 偵測。<br>' +
    "極性化合物的痕量混合分析，這是國際公認的最佳組合。</div></div>")

add(ATT, dc.kt("MRM 鑑別", "定量離子＋定性離子，<span class='hi'>雙保險</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + MRM_SVG + '</div>' +
    '<div class="note" style="margin-top:10px">每個甜味劑都監測<strong>兩組離子對</strong>：定量離子對算濃度、定性離子對確認身分。' +
    "兩者波峰面積比(相對離子強度)須落在<strong>容許範圍</strong>，才算驗出該物。</div>")

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","甜味劑方法即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("檢體前處理", "液體 · 固體 · 高油脂各有<span class='hi'>對策</span>") +
    '<div class="grid3" style="margin-top:16px">' +
    dc.card("🥤","液體檢體","混勻取 1 g，以 50%甲醇定容、過 0.22 µm 濾膜","b") +
    dc.card("🍰","固體檢體","切碎取 1 g，加 50%甲醇<strong>超音波 15 分</strong>、2200×g 離心，重複萃取","a") +
    dc.card("🧈","高油脂檢體","萃取液再加<strong>正己烷脫脂</strong>，取下層水相分析","g") + '</div>' +
    '<p class="subtitle" style="margin-top:12px">原則：把甜味劑萃進 50%甲醇水相、去除油脂與顆粒，再上機。</p>')

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","ESI 正離子 vs 負離子", 6,
    "依本法附表，把 6 種甜味劑分到「ESI⁺ 正離子」或「ESI⁻ 負離子」。"), ' data-game="g3"')

add(ATT, dc.kt("層析與定量", "基質匹配檢量線") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>以<strong>空白基質</strong>配製 10–150 ng/mL <strong>基質匹配檢量線</strong>，抵銷基質效應</li>" +
    "<li>注入 5 µL；ESI 正離子毛細管 4 kV、負離子 3.5 kV</li>" +
    "<li>各品項有專屬<strong>滯留時間</strong>：醋磺內酯鉀最早(~1.8 min)、rebaudioside B 最晚(~18.8 min)</li>" +
    "<li>鑑別＝滯留時間 + 定性/定量離子比落在容許範圍</li>" +
    '</ul></div><div class="note"><strong>基質效應：</strong>食品成分會增強或抑制離子化訊號；<br>' +
    "用「同基質」配檢量線是 LC-MS/MS 定量的關鍵紀律。</div></div>")

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","甜味劑檢驗流程排序", 6,
    "用 ▲▼ 把甜味劑多重分析的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：甜味劑判斷", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("甜味劑一覽（點欄位排序）",
    [{"k":"n","t":"s","label":"中文名"},{"k":"en","t":"s","label":"英文名"},{"k":"src","t":"s","label":"來源"},
     {"k":"esi","t":"s","label":"ESI"},{"k":"q","t":"s","label":"定量離子對"}],
    "列舉代表品項(全方法共 13 項)；離子對與來源整合自 MOHWA0030.00 附表。", kicker="附表"), ' data-game="cmp"')

add(ACT, dc.chart_inner("sweetness", "代糖有多甜？<span class='hi'>蔗糖的幾倍</span>",
    "相對甜度(蔗糖=1)取以 10 為底對數，數值為代表值。紐甜可達數千倍，故都比糖甜數十～數千倍。",
    kicker="背景數據", height="52vh"), ' data-chart="sweetness"')

add(ACT, dc.kt("法規與健康", "合法、限量、與<span class='hi'>違規</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("✅","合法但限量","多數甜味劑在規定食品與限量內可用；每日容許攝取量 ADI 有上限","b") +
    dc.card("🚫","禁用品項","對位乙氧苯脲(甘精, dulcin)具毒性疑慮，在台灣<strong>禁止使用</strong>","a") +
    dc.card("🔎","稽查重點","『無糖』飲料是否暗藏代糖、是否超量、是否標示不實","g") +
    dc.card("🧾","為何要多重分析","業者可能混用多種代糖→一次驗 13 種最有效率","b") + '</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：甜味劑含量",
    "某固體檢體取樣 <b>M = 1 g</b>、定容 <b>V = 100 mL</b>、稀釋倍數 <b>F = 10</b>；由檢量線得濃度 "
    "<b>C = 50 ng/mL</b>。求含量(g/kg)。公式：含量 = C×V×F/M × 10⁻⁶。", unit="g/kg"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>MOHWA0030.00：一次驗 <strong>13 種</strong>甜味劑(人工＋天然)</li>" +
    "<li>原理：萃取 → LC 分離 → <strong>ESI</strong> → <strong>MS/MS MRM</strong></li>" +
    "<li>ESI <strong>正/負離子切換</strong>；用<strong>基質匹配檢量線</strong>抵銷基質效應</li></ul>" +
    '<ul class="clean"><li>鑑別＝<strong>滯留時間＋定量/定性離子比</strong>(容許範圍)</li>' +
    "<li>LOQ 0.01 g/kg；甘精(dulcin)在台灣<strong>禁用</strong></li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明為什麼甜味劑要用 LC-MS/MS 多重分析",
     "舉出至少 4 種人工與 3 種天然甜味劑",
     "解釋 ESI 正/負離子切換與 MRM 離子對的意義",
     "說出液體/固體/高油脂檢體的前處理重點",
     "解釋基質匹配檢量線為何能抵銷基質效應",
     "說明如何用滯留時間與離子比鑑別甜味劑",
     "用公式由濃度算出檢體中甜味劑含量",
     "指出哪一種甜味劑在台灣禁用"]))

add(ACT, dc.cover("延伸 · CONNECT",
    "從一瓶飲料<br><span style='color:var(--accent-2)'>看懂代糖</span>", "",
    "🔗 方法骨幹同源：<strong>LC-MS/MS + MRM</strong> 也用於農藥、獸藥(四環素)、真偽鑑別<br>"
    "🔬 銜接：<strong>HPLC (Ch13)</strong>、<strong>質譜 (Ch11)</strong>、食藥署其他公告法<br>"
    "🧪 思考：看到『無糖』標示，你會想驗哪幾種代糖？為何要同時看定量與定性離子？",
    ["LC-MS/MS","MRM","13 品項","基質匹配","食安檢測"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "sweetness": {"type":"bar","yTitle":"甜度 log₁₀(蔗糖倍數)",
      "labels":["環己基磺醯胺酸鈉","甘草素","醋磺內酯鉀","阿斯巴甜","甜菊糖","糖精","蔗糖素","紐甜"],
      "datasets":[{"label":"log₁₀(相對甜度)","data":[1.6,1.7,2.3,2.3,2.4,2.6,2.8,3.9],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["天然來源","人工合成"],
      "items":[{"t":"甜菊糖 stevioside","c":"天然來源"},{"t":"rebaudioside A","c":"天然來源"},
        {"t":"甘草素 glycyrrhizin","c":"天然來源"},{"t":"新橘皮苷二氫查爾酮 NHDC","c":"天然來源"},
        {"t":"阿斯巴甜 aspartame","c":"人工合成"},{"t":"醋磺內酯鉀 acesulfame K","c":"人工合成"},
        {"t":"蔗糖素 sucralose","c":"人工合成"},{"t":"對位乙氧苯脲(甘精,禁用)","c":"人工合成"}],
      "ok":"🎉 全對！甜菊糖/rebaudioside/甘草素/NHDC 屬天然；其餘為人工合成代糖。",
      "tip":"提示：來自甜菊、甘草、柑橘的屬天然；化學合成的(阿斯巴甜、糖精類)屬人工。"},
    "g3": {"cats":["ESI⁺ 正離子","ESI⁻ 負離子"],
      "items":[{"t":"阿斯巴甜 aspartame","c":"ESI⁺ 正離子"},{"t":"紐甜 neotame","c":"ESI⁺ 正離子"},
        {"t":"蔗糖素 sucralose","c":"ESI⁺ 正離子"},
        {"t":"醋磺內酯鉀 acesulfame K","c":"ESI⁻ 負離子"},{"t":"糖精鈉 saccharin","c":"ESI⁻ 負離子"},
        {"t":"環己基磺醯胺酸鈉(甜精)","c":"ESI⁻ 負離子"}],
      "ok":"🎉 正確！依本法附表：阿斯巴甜/紐甜/蔗糖素走 ESI⁺；醋磺內酯鉀/糖精/甜精走 ESI⁻。",
      "tip":"提示：帶磺酸基(酸性、易帶負電)的多用 ESI⁻；其餘多用 ESI⁺。"}
  },
  "mcq": {
    "g2":[
      {"q":"本方法 MOHWA0030.00 採用的核心分析儀器是？","o":["氣相層析 GC","液相層析串聯質譜 LC-MS/MS","紫外光分光光度計","原子吸收 AAS"],"a":1,
       "e":"甜味劑極性不揮發，採 LC-MS/MS；以 ESI 游離、MRM 偵測。"},
      {"q":"為什麼甜味劑不適合用 GC？","o":["太便宜","極性、不揮發、易裂解","沒有標準品","顏色太深"],"a":1,
       "e":"甜味劑多為極性、不揮發或熱不穩定分子，故用液相層析。"},
      {"q":"MRM 監測『定量離子對＋定性離子對』的目的是？","o":["省時間","同時定量並確認身分","增加甜度","降低成本"],"a":1,
       "e":"定量離子算濃度、定性離子確認身分，離子比須落在容許範圍。"},
      {"q":"本法以什麼配製檢量線以抵銷基質效應？","o":["純水","純甲醇","空白基質(基質匹配檢量線)","蔗糖溶液"],"a":2,
       "e":"用同類空白基質配檢量線，抵銷食品成分造成的離子化增強/抑制。"},
      {"q":"下列何者在台灣『禁止』作為甜味劑使用？","o":["蔗糖素","對位乙氧苯脲(甘精)","醋磺內酯鉀","甜菊糖"],"a":1,
       "e":"對位乙氧苯脲(dulcin, 甘精)具毒性疑慮，台灣禁用。"}
    ],
    "g5":[
      {"q":"飲料標示『無糖』，要確認是否偷加多種代糖，最有效率的做法？","o":["逐一單獨檢驗","用多重分析一次驗13種","只測蔗糖","看顏色"],"a":1,
       "e":"MOHWA0030.00 多重分析一次涵蓋 13 品項，最有效率。"},
      {"q":"高油脂的甜點檢體，前處理要多做哪一步？","o":["加酸水解","以正己烷脫脂取下層","高溫灰化","通氮蒸餾"],"a":1,
       "e":"高油脂檢體萃取後加正己烷脫脂、取下層水相，避免干擾。"},
      {"q":"某帶磺酸基的甜味劑訊號弱，較可能該用哪個離子模式？","o":["ESI 正離子","ESI 負離子","EI","MALDI"],"a":1,
       "e":"磺酸基酸性、易帶負電，常用 ESI 負離子模式偵測。"},
      {"q":"驗出疑似甜味劑，但定性/定量離子比超出容許範圍，應？","o":["直接判定陽性","視為不符、再確認(可能基質干擾)","忽略","換成 GC"],"a":1,
       "e":"離子比超出容許範圍代表鑑別不符，須排除干擾再確認。"},
      {"q":"想知道代糖『有多甜』以理解微量即超標，應參考？","o":["沸點","相對甜度(蔗糖倍數)","顏色","密度"],"a":1,
       "e":"高倍甜味劑甜度為蔗糖數十至數千倍，微量即達效果，故限量很低。"}
    ]
  },
  "sort": {
    "g4":{"steps":["取檢體(液/固/高油脂)，以 50%甲醇萃取","固體超音波 15 分後 2200×g 離心，取上清液",
       "(高油脂)加正己烷脫脂、取下層；過 0.22 µm 濾膜","注入 LC，以 Phenyl-Hexyl 管柱梯度分離",
       "ESI 正/負離子切換游離，串聯質譜以 MRM 偵測","比對滯留時間與離子比鑑別，並以基質匹配檢量線定量"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！萃取→離心→脫脂過濾→LC分離→ESI/MRM→鑑別定量。",
       "tip":"提示：先萃取再離心、過濾後才上機；游離偵測之後才做鑑別與定量。"}
  },
  "calc": {
    "g6":{"answer":0.05,"tol":0.005,
      "ok":"🎉 正確！含量 = C×V×F/M ×10⁻⁶ = 50×100×10/1 ×10⁻⁶ = <b>0.05 g/kg</b>(＞LOQ 0.01，可定量)。",
      "bad":"再算算：含量 = C×V×F/M ×10⁻⁶ = 50×100×10/1 ×10⁻⁶。",
      "hint":"提示：50×100×10 = 50000；50000/1 ×10⁻⁶ = 0.05 g/kg。"}
  },
  "cmp": {
    "cols":[{"k":"n"},{"k":"en"},{"k":"src"},{"k":"esi"},{"k":"q"}],
    "rows":[
      {"n":"醋磺內酯鉀","en":"Acesulfame K","src":"人工","esi":"ESI⁻","q":"162>82"},
      {"n":"阿斯巴甜","en":"Aspartame","src":"人工","esi":"ESI⁺","q":"295>120"},
      {"n":"糖精鈉","en":"Saccharin","src":"人工","esi":"ESI⁻","q":"182>42"},
      {"n":"環己磺醯胺酸鈉","en":"Cyclamate","src":"人工","esi":"ESI⁻","q":"178>80"},
      {"n":"蔗糖素","en":"Sucralose","src":"人工","esi":"ESI⁺","q":"414>199"},
      {"n":"紐甜","en":"Neotame","src":"人工","esi":"ESI⁺","q":"379>172"},
      {"n":"甘精(禁用)","en":"Dulcin","src":"人工","esi":"ESI⁺","q":"181>108"},
      {"n":"甜菊糖","en":"Stevioside","src":"天然","esi":"ESI⁻","q":"641.4>479"},
      {"n":"新橘皮苷二氫查爾酮","en":"NHDC","src":"天然","esi":"ESI⁻","q":"611>303"}
    ]
  }
}

dc.build_html(
  {"title":"食品中甜味劑檢驗 LC-MS/MS · MOHWA0030.00","brand":"甜味劑 · MS/MS"},
  S, CFG, OUT)
