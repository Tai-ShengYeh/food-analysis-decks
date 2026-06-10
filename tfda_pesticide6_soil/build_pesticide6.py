# -*- coding: utf-8 -*-
"""TFDA TFDAP0007.05 食品中殘留農藥檢驗方法－多重殘留分析方法(六) — SOIL HTML deck.
Source: 衛福部食藥署 TFDAP0007.05 (QuEChERS + LC-MS/MS, 32 農藥). Run: python build_pesticide6.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
QUECHERS_SVG = """
<svg viewBox="0 0 980 220">
 <defs><marker id="qa" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="490" y="24" text-anchor="middle" class="lblb" font-size="15">QuEChERS：乙腈萃取 → 加鹽分層 → dSPE 淨化 → LC-MS/MS</text>
 <g font-size="12.5">
  <rect x="14" y="80" width="180" height="58" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="104" y="104" text-anchor="middle" class="lblb">乙腈萃取</text><text x="104" y="122" text-anchor="middle" class="lbl">1%甲酸乙腈+內標</text>
  <rect x="244" y="80" width="180" height="58" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="334" y="104" text-anchor="middle" class="lblb">加鹽分層</text><text x="334" y="122" text-anchor="middle" class="lbl">MgSO₄/NaCl/檸檬酸鹽·離心</text>
  <rect x="474" y="80" width="180" height="58" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="564" y="104" text-anchor="middle" class="lblb">dSPE 淨化</text><text x="564" y="122" text-anchor="middle" class="lbl">PSA/C18/GCB 依基質</text>
  <rect x="704" y="80" width="180" height="58" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="794" y="104" text-anchor="middle" class="lblb">LC-MS/MS</text><text x="794" y="122" text-anchor="middle" class="lbl">ESI±·MRM·32 農藥</text>
  <rect x="906" y="84" width="64" height="50" rx="9" fill="#15233f"/>
  <text x="938" y="113" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">定量</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#qa)">
  <line x1="194" y1="109" x2="240" y2="109"/><line x1="424" y1="109" x2="470" y2="109"/>
  <line x1="654" y1="109" x2="700" y2="109"/><line x1="884" y1="109" x2="902" y2="109"/></g>
 <text x="490" y="184" text-anchor="middle" class="lbl">QuEChERS = Quick · Easy · Cheap · Effective · Rugged · Safe(快速、簡單、便宜、有效、耐用、安全)</text>
</svg>"""

DSPE_SVG = """
<svg viewBox="0 0 920 220">
 <text x="460" y="22" text-anchor="middle" class="lblb" font-size="15">分散式固相萃取(dSPE)：依基質選不同淨化劑</text>
 <rect x="20" y="48" width="280" height="150" rx="12" fill="#eef6ff" stroke="#1f6feb" stroke-width="2"/>
 <text x="160" y="74" text-anchor="middle" class="lblb" fill="#1f6feb" font-size="14">I 類</text>
 <text x="160" y="96" text-anchor="middle" class="lbl">新鮮蔬果·香辛(高水分)</text>
 <text x="160" y="124" text-anchor="middle" class="lblb">PSA + MgSO₄</text>
 <text x="160" y="148" text-anchor="middle" class="lbl">去有機酸、糖、極性雜質</text>
 <text x="160" y="170" text-anchor="middle" class="lbl">與殘留水分</text>
 <rect x="320" y="48" width="280" height="150" rx="12" fill="#fff6ea" stroke="#d9822b" stroke-width="2"/>
 <text x="460" y="74" text-anchor="middle" class="lblb" fill="#d9822b" font-size="14">II 類</text>
 <text x="460" y="96" text-anchor="middle" class="lbl">穀類·乾豆(蠟/油脂/醣高)</text>
 <text x="460" y="124" text-anchor="middle" class="lblb">PSA + MgSO₄ + C18</text>
 <text x="460" y="148" text-anchor="middle" class="lbl">多加 C18 去『油脂、蠟』</text>
 <rect x="620" y="48" width="280" height="150" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
 <text x="760" y="74" text-anchor="middle" class="lblb" fill="#1f9d6b" font-size="14">III 類</text>
 <text x="760" y="96" text-anchor="middle" class="lbl">乾燥茶葉·香辛(色素高)</text>
 <text x="760" y="124" text-anchor="middle" class="lblb">PSA + MgSO₄ + GCB</text>
 <text x="760" y="148" text-anchor="middle" class="lbl">多加 GCB 石墨化碳</text>
 <text x="760" y="170" text-anchor="middle" class="lbl">去『色素』</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("食藥署公告檢驗方法 · TFDAP0007.05",
    "農藥<span style='color:var(--accent-2)'>多重殘留</span>分析(六)", "Pesticide Multiresidue Analysis (6)",
    "食品安全檢測　·　3 小時課程　·　含 6 個互動小遊戲<br>QuEChERS · LC-MS/MS · MRM · 32 項農藥 · 三類 dSPE 淨化",
    ["一次驗 32 種","QuEChERS","LC-MS/MS","ESI 正/負","三類淨化"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">蔬果上殘留的<span class="hi">32 種農藥</span>(像克美素、二、四地…)，<br>有些極性又不揮發,怎麼一次驗？</div>
  <p class="subtitle" style="max-width:850px;margin:22px auto 0">這些<strong>極性/酸性農藥</strong>難用 GC 做;用 <strong>QuEChERS 前處理 + LC-MS/MS</strong> 一次搞定。<br>
  QuEChERS 是席捲全球的『快速、簡單、便宜』多重殘留前處理法。</p>
  <div style="margin-top:24px"><span class="pill">極性農藥</span><span class="pill">多重殘留</span>
  <span class="pill">ppb 級</span><span class="pill">高通量</span></div></div>""")

add(MOT, dc.kt("背景", "多重殘留分析的<span class='hi'>挑戰與解方</span>") +
    '<div class="grid2" style="margin-top:20px">' +
    dc.card("🧩","挑戰","農藥種類多、基質複雜、殘留 ppb 級;逐一檢驗太慢","b") +
    dc.card("⚡","QuEChERS","Quick·Easy·Cheap·Effective·Rugged·Safe——一套快速前處理一次處理多種農藥","a") +
    dc.card("💧","為何用 LC-MS/MS","本法(六)專攻<strong>極性/酸性農藥</strong>(克美素、2,4-D…),GC 不適合","g") +
    dc.card("🎯","一次 32 項","20 項走 ESI 正離子 + 12 項走 ESI 負離子,合計 32 項","b") + '</div>')

add(MOT, dc.kt("方法核心", "QuEChERS → <span class='hi'>LC-MS/MS</span>") +
    '<div class="svgwrap" style="margin-top:4px">' + QUECHERS_SVG + '</div>')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","萃取階段 vs 淨化階段", 8,
    "把 8 個試劑/步驟分到「乙腈萃取階段」或「dSPE 淨化階段」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("萃取", "乙腈 + 鹽析<span class='hi'>分層</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>檢體均質,加<strong>含 1%甲酸的乙腈</strong>與內標</li>" +
    "<li>加<strong>萃取鹽</strong>(無水硫酸鎂 + 氯化鈉 + 檸檬酸鈉/檸檬酸氫二鈉,檸檬酸鹽緩衝)</li>" +
    "<li>高速分散裝置(GenoGrinder)激烈振盪 → 鹽析使<strong>乙腈與水相分層</strong>,農藥進乙腈層</li>" +
    "<li>低溫離心,取<strong>乙腈上清液</strong>供淨化</li>" +
    '</ul></div><div class="note"><strong>為何加鹽？</strong><br>' +
    "鹽析降低農藥在水相的溶解度、促進分層;檸檬酸鹽緩衝保護對 pH 敏感的農藥。</div></div>")

add(ATT, dc.kt("淨化", "dSPE 依<span class='hi'>基質</span>選淨化劑") +
    '<div class="svgwrap" style="margin-top:4px">' + DSPE_SVG + '</div>' +
    '<div class="note" style="margin-top:8px"><strong>PSA</strong>去有機酸與極性雜質;高油脂基質多加 <strong>C18</strong> 去油脂蠟;' +
    "高色素(茶葉)多加 <strong>GCB 石墨化碳</strong>去色素。淨化越乾淨,基質效應越小、訊號越穩。</div>")

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","QuEChERS 即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("LC-MS/MS 偵測", "ESI 正負切換 + <span class='hi'>MRM</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>管柱 <strong>CORTECS C18</strong>(1.6 µm),醋酸銨/甲酸-甲醇梯度,0.3 mL/min</li>" +
    "<li>游離:<strong>ESI 正離子(4 kV)/負離子(3 kV)切換</strong>——20 項走正、12 項走負</li>" +
    "<li>偵測:<strong>MRM</strong>,每農藥監測母離子→子離子(定量+定性離子對)</li>" +
    "<li>內標 <strong>磷酸三苯酯(TPP)</strong>當品管參考;以<strong>基質匹配檢量線</strong>定量</li>" +
    '</ul></div><div class="note"><strong>基質匹配檢量線:</strong><br>' +
    "用空白基質配檢量線,抵銷食品成分造成的離子化增強/抑制(基質效應)。</div></div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","三類 dSPE 配基質", 6,
    "把 6 個項目分到「I 類(蔬果)」「II 類(穀類乾豆)」或「III 類(茶葉)」。"), ' data-game="g3"')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","QuEChERS 多重殘留流程排序", 6,
    "用 ▲▼ 把多重殘留分析(六)的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("鑑別與計算", "離子比確認 + 面積定量") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">含量(ppm) = ' +
    '<span class="frac"><b>C × V</b><span>M</span></span></div>' +
    '<div><ul class="clean"><li><strong>C</strong>:由基質匹配檢量線求得濃度(µg/mL)</li>' +
    "<li><strong>V</strong>:萃取乙腈體積(10 mL)　<strong>M</strong>:取樣重(g)</li>" +
    "<li>鑑別:滯留時間 + 定性/定量<strong>離子比</strong>落在容許範圍</li>" +
    "<li>LOQ 依品項與基質約 <strong>0.01–0.05 ppm</strong></li></ul></div></div>")

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對策略", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("三類 dSPE 淨化（點欄位排序）",
    [{"k":"c","t":"s","label":"類別"},{"k":"mx","t":"s","label":"適用基質"},
     {"k":"s","t":"s","label":"淨化劑"},{"k":"r","t":"s","label":"主要去除"}],
    "整合自 TFDAP0007.05。依基質選淨化劑是 QuEChERS 的精髓。", kicker="2.8 淨化"), ' data-game="cmp"')

add(ACT, dc.chart_inner("rt", "部分農藥的<span class='hi'>滯留時間</span>",
    "整合自 TFDAP0007.05 參考層析圖譜(分):從克美素(0.82)到 bioresmethrin(14.87),CORTECS C18 把 32 種農藥逐一分開。",
    kicker="層析分離", height="52vh"), ' data-chart="rt"')

add(ACT, dc.kt("方法定位", "三種農藥檢驗法<span class='hi'>各司其職</span>") +
    '<div class="grid3" style="margin-top:18px">' +
    dc.card("💧","本法 · 多重殘留(六)","QuEChERS+LC-MS/MS,測極性/酸性農藥『個別』品項(32 項)","b") +
    dc.card("🌫️","GC-MS/MS","測揮發、熱穩定的農藥(如有機磷、有機氯)","a") +
    dc.card("🧅","二硫代胺基甲酸鹽法","裂解成共同產物 CS₂、GC-FPD 測『總量』","g") + '</div>' +
    '<p class="subtitle" style="margin-top:14px">極性/不揮發→LC-MS/MS;揮發→GC-MS;特定族群(如 dithiocarbamate)→共同產物法。</p>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：農藥含量",
    "QuEChERS-LC-MS/MS：取樣 <b>M = 10 g</b>、萃取乙腈 <b>V = 10 mL</b>;由檢量線得濃度 "
    "<b>C = 0.05 µg/mL</b>。求含量(ppm)。公式:C×V/M。", unit="ppm"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>本法(六)以 <strong>QuEChERS + LC-MS/MS</strong> 驗 <strong>32 項極性/酸性農藥</strong></li>" +
    "<li>QuEChERS:乙腈萃取 → 加鹽分層 → dSPE 淨化</li>" +
    "<li>三類 dSPE:I 類 PSA、II 類加 <strong>C18(去油脂)</strong>、III 類加 <strong>GCB(去色素)</strong></li></ul>" +
    '<ul class="clean"><li>LC-MS/MS:<strong>ESI 正/負切換</strong>、MRM、TPP 內標、基質匹配檢量線</li>' +
    "<li>含量 = C×V/M;鑑別靠滯留時間+離子比;LOQ 0.01–0.05 ppm</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明為何極性/酸性農藥要用 LC-MS/MS 而非 GC",
     "說出 QuEChERS 的三大步驟與名稱由來",
     "解釋加鹽(鹽析)與檸檬酸鹽緩衝的作用",
     "依基質選對 dSPE 淨化劑(PSA/C18/GCB)",
     "說明 ESI 正/負切換、MRM 與基質匹配檢量線",
     "依序排出 QuEChERS 多重殘留流程",
     "用 C×V/M 計算農藥殘留含量",
     "比較本法與 GC-MS、二硫代胺基甲酸鹽法的定位"]))

add(ACT, dc.cover("延伸 · CONNECT",
    "從一籃蔬果<br><span style='color:var(--accent-2)'>看懂多重殘留</span>", "",
    "🔗 同骨幹:<strong>LC-MS/MS + MRM</strong> 也用於甜味劑、四環素;本法多了 QuEChERS 與三類 dSPE<br>"
    "🔬 銜接:<strong>質譜 (Ch11)</strong>、<strong>HPLC (Ch13)</strong>、固相萃取、食品安全衛生管理<br>"
    "🧪 思考:你的農藥揮發嗎、極性如何?基質是蔬果、穀類還是茶葉?該用哪一種淨化劑?",
    ["QuEChERS","LC-MS/MS","dSPE","基質匹配","食安檢測"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "rt": {"type":"bar","yTitle":"滯留時間 (分)",
      "labels":["克美素","賽滅淨","依滅草","二四地","MCPA","三氯比","美速隆","多寧","Bioresmethrin"],
      "datasets":[{"label":"滯留時間 (min)","data":[0.82,2.52,3.53,5.83,6.27,6.75,7.32,11.34,14.87],"color":"#1f6feb"}]}
  },
  "bucket": {
    "g1": {"cats":["乙腈萃取階段","dSPE 淨化階段"],
      "items":[{"t":"含 1%甲酸的乙腈","c":"乙腈萃取階段"},{"t":"萃取鹽(MgSO₄/NaCl/檸檬酸鹽)","c":"乙腈萃取階段"},
        {"t":"高速分散裝置激烈振盪","c":"乙腈萃取階段"},{"t":"離心後取乙腈上清液","c":"乙腈萃取階段"},
        {"t":"PSA(去有機酸/極性雜質)","c":"dSPE 淨化階段"},{"t":"C18(去油脂蠟)","c":"dSPE 淨化階段"},
        {"t":"GCB(去色素)","c":"dSPE 淨化階段"},{"t":"再離心取上清、氮吹復溶","c":"dSPE 淨化階段"}],
      "ok":"🎉 全對！乙腈+鹽萃取分層;PSA/C18/GCB 屬 dSPE 淨化。",
      "tip":"提示:跟『乙腈、加鹽、振盪、分層』有關→萃取;跟『PSA/C18/GCB、復溶』→淨化。"},
    "g3": {"cats":["I 類(蔬果)","II 類(穀類乾豆)","III 類(茶葉)"],
      "items":[{"t":"新鮮蔬菜/水果(高水分)","c":"I 類(蔬果)"},{"t":"用 PSA + MgSO₄","c":"I 類(蔬果)"},
        {"t":"穀類/乾豆(蠟·油脂·醣高)","c":"II 類(穀類乾豆)"},{"t":"多加 C18 去油脂","c":"II 類(穀類乾豆)"},
        {"t":"乾燥茶葉/香辛(色素高)","c":"III 類(茶葉)"},{"t":"多加 GCB 去色素","c":"III 類(茶葉)"}],
      "ok":"🎉 正確！蔬果用 PSA;穀類乾豆加 C18 去油脂;茶葉加 GCB 去色素。",
      "tip":"提示:高水分蔬果→I 類;高油脂穀豆→II 類(C18);高色素茶葉→III 類(GCB)。"}
  },
  "mcq": {
    "g2":[
      {"q":"本法(六)為何用 LC-MS/MS 而非 GC？","o":["比較便宜","針對極性/酸性、不揮發的農藥","速度快","不需標準品"],"a":1,
       "e":"克美素、2,4-D 等極性/不揮發農藥不適合 GC,用 LC-MS/MS。"},
      {"q":"QuEChERS 名稱代表的特性不包含？","o":["Quick 快速","Cheap 便宜","Coloured 有色","Safe 安全"],"a":2,
       "e":"QuEChERS = Quick/Easy/Cheap/Effective/Rugged/Safe。"},
      {"q":"萃取時加大量鹽的主要目的是？","o":["調色","鹽析促進乙腈與水相分層","當內標","殺菌"],"a":1,
       "e":"加鹽降低農藥在水相溶解度、促進乙腈分層;檸檬酸鹽兼緩衝。"},
      {"q":"高色素的乾燥茶葉,dSPE 要多加什麼淨化劑？","o":["C18","GCB 石墨化碳","PSA only","NaCl"],"a":1,
       "e":"茶葉色素多,加 GCB(石墨化碳)去除色素。"},
      {"q":"本法以什麼配製檢量線抵銷基質效應？","o":["純水","純甲醇","空白基質(基質匹配檢量線)","乙腈"],"a":2,
       "e":"用空白基質配檢量線,抵銷食品成分造成的離子化增強/抑制。"}
    ],
    "g5":[
      {"q":"要一次篩檢蔬果上多種極性農藥,最有效率的是？","o":["逐一單測","QuEChERS+LC-MS/MS 多重殘留","只測顏色","只看外觀"],"a":1,
       "e":"QuEChERS+LC-MS/MS 一次處理並偵測多種農藥,高通量。"},
      {"q":"高油脂的穀類/乾豆檢體,淨化要多加？","o":["GCB","C18","NaCl","水"],"a":1,
       "e":"高油脂基質加 C18 去油脂蠟,屬 II 類淨化。"},
      {"q":"某農藥訊號在純溶劑與基質中差很多,代表？","o":["儀器壞","有基質效應,需用基質匹配檢量線","農藥揮發","要加熱"],"a":1,
       "e":"基質效應使訊號增強/抑制;用基質匹配檢量線校正。"},
      {"q":"要分辨檢出的是哪一種農藥,本法靠什麼鑑別？","o":["顏色","滯留時間 + 定性/定量離子比","氣味","密度"],"a":1,
       "e":"以滯留時間與 MRM 離子比(落在容許範圍)鑑別品項。"},
      {"q":"揮發、熱穩定的農藥(如有機磷),較適合用？","o":["本法 LC-MS/MS","GC-MS/MS","二硫代胺基甲酸鹽法","滴定"],"a":1,
       "e":"揮發、熱穩定的農藥用 GC-MS/MS;本法針對極性農藥。"}
    ]
  },
  "sort": {
    "g4":{"steps":["檢體均質、精秤,加含 1%甲酸乙腈與內標","加入萃取鹽(MgSO₄/NaCl/檸檬酸鹽),激烈振盪",
       "離心使乙腈與水相分層,取乙腈上清液","上清液移入對應的 dSPE 淨化離心管(I/II/III 類)",
       "振盪離心、取上清,氮氣吹乾後以甲醇復溶過濾","LC-MS/MS 以 ESI± MRM 分析,比對離子比與滯留時間定量"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！乙腈萃取→加鹽分層→取上清→dSPE 淨化→復溶→LC-MS/MS。",
       "tip":"提示:先乙腈+鹽萃取分層、取上清,再依基質 dSPE 淨化、復溶後才上 LC-MS/MS。"}
  },
  "calc": {
    "g6":{"answer":0.05,"tol":0.005,
      "ok":"🎉 正確！含量 = C×V/M = 0.05×10/10 = <b>0.05 ppm</b>。",
      "bad":"再算算：含量 = C×V/M = 0.05×10/10。",
      "hint":"提示:0.05×10 = 0.5;0.5/10 = 0.05 ppm。"}
  },
  "cmp": {
    "cols":[{"k":"c"},{"k":"mx"},{"k":"s"},{"k":"r"}],
    "rows":[
      {"c":"I 類","mx":"新鮮蔬果·香辛(高水分)","s":"PSA + MgSO₄","r":"有機酸·糖·極性雜質·水分"},
      {"c":"II 類","mx":"穀類·乾豆(蠟/油脂/醣高)","s":"PSA + MgSO₄ + C18","r":"多去油脂、蠟"},
      {"c":"III 類","mx":"乾燥茶葉·香辛(色素高)","s":"PSA + MgSO₄ + GCB","r":"多去色素"}
    ]
  }
}

dc.build_html(
  {"title":"農藥多重殘留分析(六) QuEChERS LC-MS/MS · TFDAP0007.05","brand":"農藥(六) · LC-MS/MS"},
  S, CFG, OUT)
