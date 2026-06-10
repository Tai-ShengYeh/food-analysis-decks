# -*- coding: utf-8 -*-
"""Nielsen Ch22 pH and Titratable Acidity — SOIL HTML deck. Uses ../soil_deck_common.py.
Run: python build_ch22.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
PHMETER_SVG = """
<svg viewBox="0 0 560 300">
 <text x="280" y="22" text-anchor="middle" class="lblb" font-size="15">pH 計：玻璃指示電極 + 參考電極，量電位差換算 pH</text>
 <rect x="40" y="44" width="150" height="46" rx="8" fill="#15233f"/>
 <text x="115" y="73" text-anchor="middle" fill="#7ed957" font-family="JetBrains Mono" font-size="18">pH 3.59</text>
 <text x="115" y="104" text-anchor="middle" class="lbl">電壓計/放大器</text>
 <!-- electrodes -->
 <rect x="250" y="70" width="26" height="150" rx="5" fill="#cfe0f6" stroke="#1f6feb" stroke-width="2"/>
 <text x="263" y="244" text-anchor="middle" class="lbl">玻璃</text><text x="263" y="260" text-anchor="middle" class="lbl">指示電極</text>
 <circle cx="263" cy="226" r="8" fill="#1f6feb" opacity=".6"/>
 <rect x="320" y="70" width="26" height="150" rx="5" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
 <text x="333" y="244" text-anchor="middle" class="lbl">參考</text><text x="333" y="260" text-anchor="middle" class="lbl">電極(KCl)</text>
 <line x1="190" y1="60" x2="263" y2="70" stroke="#48597a" stroke-width="1.6"/>
 <line x1="190" y1="78" x2="333" y2="70" stroke="#48597a" stroke-width="1.6"/>
 <!-- beaker -->
 <path d="M225 210 h150 v50 a10 10 0 0 1 -10 10 h-130 a10 10 0 0 1 -10 -10 Z" fill="#e7f0fe" stroke="#48597a" stroke-width="2"/>
 <text x="300" y="290" text-anchor="middle" class="lbl">待測樣品</text>
 <!-- nernst -->
 <rect x="400" y="120" width="150" height="80" rx="10" fill="#f6f9fd" stroke="#1f9d6b" stroke-width="2"/>
 <text x="475" y="148" text-anchor="middle" class="lblb" fill="#1f9d6b" font-size="13">Nernst</text>
 <text x="475" y="172" text-anchor="middle" class="lbl">E = E₀ + 2.303·RT/zF·logA</text>
 <text x="475" y="192" text-anchor="middle" class="lbl">電位 ↔ H⁺ 活性</text>
 <text x="475" y="232" text-anchor="middle" class="lbl">用前先以 pH 4/7/10</text>
 <text x="475" y="248" text-anchor="middle" class="lbl">緩衝液兩點校正</text>
</svg>"""

ACID_SVG = """
<svg viewBox="0 0 620 230">
 <text x="310" y="22" text-anchor="middle" class="lblb" font-size="15">pH（強度）vs 可滴定酸度（總量）——量的是不同東西</text>
 <rect x="30" y="50" width="270" height="150" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
 <text x="165" y="78" text-anchor="middle" class="lblb" fill="#1f6feb" font-size="15">pH</text>
 <text x="165" y="100" text-anchor="middle" class="lbl">= −log[H⁺]</text>
 <text x="165" y="126" text-anchor="middle" class="lbl">只看『已解離』的游離 H⁺</text>
 <text x="165" y="148" text-anchor="middle" class="lbl">反映『酸的強度』</text>
 <text x="165" y="174" text-anchor="middle" class="lbl">用 pH 計量</text>
 <rect x="320" y="50" width="270" height="150" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
 <text x="455" y="78" text-anchor="middle" class="lblb" fill="#d9822b" font-size="15">可滴定酸度 TA</text>
 <text x="455" y="100" text-anchor="middle" class="lbl">= 用鹼中和的『總酸量』</text>
 <text x="455" y="126" text-anchor="middle" class="lbl">含未解離 + 已解離的酸</text>
 <text x="455" y="148" text-anchor="middle" class="lbl">比 pH 更能預測『風味酸度』</text>
 <text x="455" y="174" text-anchor="middle" class="lbl">用滴定量</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 22",
    "pH 與<span style='color:var(--accent-2)'>可滴定酸度</span>", "pH and Titratable Acidity",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>pH 計 · 滴定曲線 · 酚酞終點 · KHP 標定 · 主要酸 · Brix/酸比",
    ["pH=−log[H⁺]","可滴定酸度 TA","0.1N NaOH 滴定","酚酞 pH 8.2","果汁熟度"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">檸檬很酸、黑咖啡也酸——<br>但「酸」指的是 <span class="hi">pH</span> 還是<span class="hi">總酸量</span>？</div>
  <p class="subtitle" style="max-width:840px;margin:22px auto 0">這是兩個<strong>不一樣</strong>的概念：pH 看『游離 H⁺ 的強度』，可滴定酸度看『能被中和的總酸量』。<br>
  它們各自影響<strong>風味、微生物安定性、水果熟度</strong>，分析方法也不同。</p>
  <div style="margin-top:24px"><span class="pill">風味酸度</span><span class="pill">發酵監控</span>
  <span class="pill">水果熟度</span><span class="pill">保存安定性</span></div></div>""")

add(MOT, dc.kt("22.1 兩個概念", "pH vs 可滴定酸度") +
    '<div class="svgwrap" style="margin-top:6px">' + ACID_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:8px">食品中的有機酸大多<strong>只部分解離</strong>；可滴定酸度把『未解離的酸』也算進去，' +
    "所以常是比 pH 更好的風味酸度指標。</p>")

add(MOT, dc.kt("22.3 pH 基礎", "pH 計怎麼量") +
    '<div class="svgwrap" style="margin-top:4px">' + PHMETER_SVG + '</div>' +
    '<div class="note" style="margin-top:8px"><strong>pH = −log[H⁺]</strong>；pH 計是<strong>電位計</strong>，' +
    "玻璃電極對 H⁺ 活性產生電位(Nernst)、與參考電極比較。用前以 <strong>pH 4/7/10 緩衝液兩點校正</strong>並做溫度補償。</div>")

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","pH vs 可滴定酸度", 8,
    "把 8 個敘述分到「pH」或「可滴定酸度 TA」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("22.4 可滴定酸度", "用<span class='hi'>鹼</span>把酸中和、數滴定量") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>取定量樣品(常 10 mL)，以 <strong>0.1 N NaOH</strong> 滴定</li>" +
    "<li>終點：<strong>酚酞</strong>由無色變粉紅(pH ≈ 8.2)，或用 pH 計測<strong>電位終點</strong></li>" +
    "<li>由滴定量、鹼濃度、樣品量算出總酸，以<strong>主要酸</strong>表示</li>" +
    "<li>深色樣品看不出酚酞變色 → 改用<strong>電位滴定</strong></li>" +
    '</ul></div><div class="note"><strong>為什麼到 pH 8.2？</strong><br>' +
    "弱酸滴定的當量點落在鹼性側；酚酞在 pH 8.0–9.6 變色，剛好標示終點。CO₂ 干擾可先煮沸去除。</div></div>")

add(ATT, dc.chart_inner("titration", "滴定曲線：<span class='hi'>強酸</span>與<span class='hi'>弱酸</span>",
    "0.1 N 酸以 0.1 N NaOH 滴定(示意)。弱酸在 pKa 附近有緩衝平台、當量點在鹼性側；強酸在當量點(pH 7)急升。",
    kicker="22.4.2 滴定曲線", height="50vh"), ' data-chart="titration"')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","pH 與酸度即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("22.4.3 試劑準備", "NaOH 與<span class='hi'>標準酸</span>的眉角") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("⚠️","NaOH 不是好基準","強吸濕、含 Na₂CO₃、會吸收空氣 CO₂ → 濃度不準，每批要『標定』","a") +
    dc.card("🧪","用 KHP 標定","鄰苯二甲酸氫鉀(KHP)純、不吸濕、可乾燥、分子量大 → 當『標準酸』標定 NaOH","b") +
    '</div><div class="note" style="margin-top:14px"><strong>去 CO₂：</strong>配 NaOH 用無 CO₂ 水(煮沸或通氮)；儲存用 ' +
    "<strong>ascarite 阱</strong>(鹼性吸收劑)擋空氣 CO₂；工作液每週重新標定。</div>")

add(ATT, dc.kt("22.4.5 計算", "從滴定量到 <span class='hi'>% 酸</span>") +
    '<div class="grid2" style="margin-top:12px"><div class="eq">% 酸 = ' +
    '<span class="frac"><b>N × V × 當量重</b><span>W × 1000</span></span> × 100</div>' +
    '<div><ul class="clean"><li><strong>N</strong>：NaOH 濃度(N)　<strong>V</strong>：滴定量(mL)</li>' +
    "<li><strong>當量重</strong>：主要酸的當量重(檸檬酸 64、蘋果酸 67、酒石酸 75)</li>" +
    "<li><strong>W</strong>：樣品重(g)；以<strong>主要酸</strong>表示結果</li>" +
    "<li>柑橘→檸檬酸、葡萄→酒石酸、乳品→乳酸</li></ul></div></div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","食物的主要酸", 6,
    "把 6 種食物分到它的「主要有機酸」(檸檬酸 / 蘋果酸 / 其他)。"), ' data-game="g3"')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","可滴定酸度滴定流程排序", 6,
    "用 ▲▼ 把可滴定酸度的 6 個操作步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("22.4.6 食物中的酸", "酸度、糖度與<span class='hi'>熟度</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🍊","主要酸","柑橘/莓果→檸檬酸；蘋果→蘋果酸；葡萄→酒石酸；乳品→乳酸","b") +
    dc.card("🍬","Brix/酸比","糖度(Brix) ÷ 酸度；隨水果成熟『糖升酸降』→ 比值升，是常用熟度指標","a") +
    dc.card("🍷","揮發酸度","醋酸發酵中先測總酸，再煮掉醋酸測固定酸；差值=揮發酸度","g") +
    dc.card("🧀","發酵監控","以可滴定酸度追蹤起司/優格的乳酸發酵進程","b") + '</div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：酸度分析判斷", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("常見食品酸的當量重（點欄位排序）",
    [{"k":"a","t":"s","label":"酸"},{"k":"mw","t":"n","label":"分子量"},{"k":"eq","t":"n","label":"當量重"},
     {"k":"n","t":"n","label":"可解離 H⁺"},{"k":"food","t":"s","label":"常見於"}],
    "整合自 Table 22.1。當量重 = 分子量 ÷ 可解離 H⁺ 數。", kicker="Table 22.1"), ' data-game="cmp"')

add(ACT, dc.chart_inner("brix", "水果的<span class='hi'>典型 °Brix</span>",
    "整合自 Table 22.5：成熟水果的糖度(°Brix)代表值。Brix 配合可滴定酸度算 Brix/酸比，可指示熟度。",
    kicker="22.4.6 數據", height="50vh"), ' data-chart="brix"')

add(ACT, dc.kt("應用", "pH 與酸度<span class='hi'>守護</span>什麼") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🦠","微生物安定","pH 影響微生物生長；低 pH(酸化)是重要保存手段","b") +
    dc.card("👅","風味","可滴定酸度比 pH 更能預測『嚐起來多酸』(糖會掩蓋酸味)","a") +
    dc.card("🍓","熟度與品質","Brix/酸比追蹤水果成熟、決定採收與分級","g") +
    dc.card("🧪","製程監控","發酵、醃漬、飲料配方都靠 pH/酸度把關","b") + '</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：% 酸",
    "取柑橘汁 <b>W = 15 g</b>，以 <b>0.085 N NaOH</b> 滴定用去 <b>V = 17.5 mL</b>；以檸檬酸(當量重 <b>64</b>)表示。"
    "求 % 酸。公式：N×V×當量重/(W×1000)×100。", unit="%"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li><strong>pH</strong>＝游離 H⁺ 強度(−log[H⁺])；<strong>可滴定酸度</strong>＝可中和的總酸量</li>" +
    "<li>pH 計是電位計(Nernst)，用前以 4/7/10 緩衝液<strong>兩點校正</strong></li>" +
    "<li>可滴定酸度：0.1N NaOH 滴定到<strong>酚酞(pH 8.2)</strong>或電位終點</li></ul>" +
    '<ul class="clean"><li>NaOH 不純須以 <strong>KHP 標定</strong>、防 CO₂</li>' +
    "<li>% 酸 = N×V×當量重/(W×1000)×100；以<strong>主要酸</strong>表示</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明 pH 與可滴定酸度的差別與各自意義",
     "解釋 pH 計的原理(玻璃電極/Nernst)與兩點校正",
     "描述可滴定酸度的滴定步驟與酚酞終點(pH 8.2)",
     "說明為何 NaOH 要用 KHP 標定、為何要防 CO₂",
     "讀懂強酸與弱酸的滴定曲線與當量點差異",
     "說出常見食物的主要酸與其當量重",
     "用 N×V×當量重/(W×1000)×100 計算 % 酸",
     "解釋 Brix/酸比為何能指示水果熟度"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把酸度分析<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions(終點選擇、KHP、Brix/酸比、揮發酸度、% 酸計算)<br>"
    "🔜 銜接：<strong>HPLC (Ch13)</strong> 分個別有機酸、發酵與醃漬製程、<strong>水分/糖度</strong>量測<br>"
    "🧪 思考：你要的是『酸的強度(pH)』還是『總酸量(TA)』？樣品深色嗎？主要酸是哪一種？",
    ["pH","可滴定酸度","酚酞終點","KHP 標定","Brix/酸比"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "titration": {"type":"line","yTitle":"pH","zero":True,
      "labels":["0","20","40","60","80","100","110","120","140"],
      "datasets":[
        {"label":"強酸(鹽酸)","data":[1.0,1.2,1.5,1.9,2.8,7.0,11.5,12.2,12.6],"color":"#1f6feb"},
        {"label":"弱酸(醋酸,pKa 4.8)","data":[2.9,4.1,4.6,5.1,5.7,8.7,11.4,12.1,12.5],"color":"#d9822b"}]},
    "brix": {"type":"bar","yTitle":"典型 °Brix",
      "labels":["番茄","葡萄柚","檸檬","柳橙","蘋果","葡萄","鳳梨","香蕉"],
      "datasets":[{"label":"°Brix(代表值)","data":[4,8.5,9,11.5,11.3,13.8,14.5,18],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["pH","可滴定酸度 TA"],
      "items":[{"t":"= −log[H⁺]","c":"pH"},{"t":"只反映已解離的游離 H⁺","c":"pH"},
        {"t":"代表『酸的強度』","c":"pH"},{"t":"用玻璃電極/電位計量測","c":"pH"},
        {"t":"= 能被鹼中和的『總酸量』","c":"可滴定酸度 TA"},{"t":"含未解離 + 已解離的酸","c":"可滴定酸度 TA"},
        {"t":"以 0.1 N NaOH 滴定到酚酞終點","c":"可滴定酸度 TA"},{"t":"比 pH 更能預測風味酸度","c":"可滴定酸度 TA"}],
      "ok":"🎉 全對！pH 看游離 H⁺ 的強度；可滴定酸度看可中和的總酸量。",
      "tip":"提示：跟『−log[H⁺]、電極、強度』有關→pH；跟『滴定、總酸量、中和』有關→TA。"},
    "g3": {"cats":["檸檬酸","蘋果酸","其他酸"],
      "items":[{"t":"柳橙、檸檬、莓果","c":"檸檬酸"},{"t":"番茄","c":"檸檬酸"},
        {"t":"蘋果","c":"蘋果酸"},{"t":"香蕉(蘋果酸為主)","c":"蘋果酸"},
        {"t":"葡萄(酒石酸)","c":"其他酸"},{"t":"優格、起司(乳酸)","c":"其他酸"}],
      "ok":"🎉 正確！柑橘莓果番茄→檸檬酸；蘋果香蕉→蘋果酸；葡萄→酒石酸、乳品→乳酸。",
      "tip":"提示：柑橘類與番茄是檸檬酸；蘋果是蘋果酸；葡萄酒石酸、發酵乳品乳酸歸『其他』。"}
  },
  "mcq": {
    "g2":[
      {"q":"pH 的定義是？","o":["總酸量","−log[H⁺]","滴定量","糖度"],"a":1,
       "e":"pH = −log[H⁺]，反映游離氫離子濃度(強度)。"},
      {"q":"為什麼可滴定酸度常比 pH 更能預測風味酸度？","o":["比較貴","它計入未解離的酸(總酸量)","它只看強酸","它不受糖影響"],"a":1,
       "e":"食品有機酸多只部分解離；TA 把未解離的酸也算進去，較貼近嚐到的酸。"},
      {"q":"可滴定酸度滴定常用的終點指示劑與 pH 是？","o":["甲基紅 pH 5","酚酞 pH 8.2","澱粉 pH 7","溴瑞香草藍 pH 6"],"a":1,
       "e":"弱酸當量點在鹼性側，用酚酞(變色約 pH 8.2)指示終點。"},
      {"q":"為什麼 NaOH 滴定液每批都要用 KHP 標定？","o":["KHP 較便宜","NaOH 吸濕、含碳酸鈉、濃度不準","KHP 顏色漂亮","為了加快"],"a":1,
       "e":"NaOH 強吸濕又吸 CO₂，濃度不可靠；用純淨的 KHP 標定其真實濃度。"},
      {"q":"pH 計使用前的標準作業是？","o":["加熱","以 pH 4/7/10 緩衝液兩點校正","加鹽","稀釋樣品"],"a":1,
       "e":"用涵蓋樣品 pH 的兩個緩衝液做兩點校正，並做溫度補償。"}
    ],
    "g5":[
      {"q":"番茄汁顏色深，滴定看不出酚酞變色，怎麼辦？","o":["多加指示劑","改用 pH 計做電位滴定","稀釋到無色","用更濃的鹼"],"a":1,
       "e":"深色樣品用電位滴定(pH 計)判斷終點，較客觀。"},
      {"q":"要判斷柳橙是否成熟可採收，最常用？","o":["只看 pH","Brix/酸比","只看顏色","測水分"],"a":1,
       "e":"成熟時糖升酸降，Brix/酸比上升，是常用熟度指標。"},
      {"q":"醋發酵想知道有多少酸來自醋酸，做法是？","o":["只測 pH","先測總酸,煮掉醋酸測固定酸,相減得揮發酸度","測糖度","測顏色"],"a":1,
       "e":"總酸 − 固定酸(煮掉揮發酸後)= 揮發酸度(主要為醋酸)。"},
      {"q":"報告葡萄汁的可滴定酸度時，應以哪種酸表示？","o":["檸檬酸","蘋果酸","酒石酸","乳酸"],"a":2,
       "e":"以該食品的主要酸表示;葡萄的主要酸是酒石酸。"},
      {"q":"配製 NaOH 標準鹼為何要用無 CO₂ 水？","o":["比較純","CO₂ 會生成碳酸鹽緩衝、模糊終點","加快反應","降低成本"],"a":1,
       "e":"CO₂ 溶入會形成碳酸/碳酸鹽,造成緩衝並使終點不明確。"}
    ]
  },
  "sort": {
    "g4":{"steps":["以 KHP 標定 0.1 N NaOH 的真實濃度","精確量取定量樣品(如 10 mL/g)置於錐形瓶",
       "加入 2–3 滴酚酞指示劑(深色樣品改用 pH 計)","以 0.1 N NaOH 緩慢滴定並搖盪",
       "滴到酚酞變粉紅且不退色(或到 pH 8.2)為終點","以 N×V×當量重/(W×1000)×100 算出 % 酸"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！標定鹼→取樣→加指示劑→滴定→判讀終點→計算。",
       "tip":"提示：先標定鹼濃度,取樣加指示劑後才滴定;到終點才計算。"}
  },
  "calc": {
    "g6":{"answer":0.635,"tol":0.03,
      "ok":"🎉 正確！% 酸 = 0.085×17.5×64/(15×1000)×100 = 95.2/15000×100 ≈ <b>0.635%</b>(以檸檬酸計)。",
      "bad":"再算算：% 酸 = N×V×當量重/(W×1000)×100 = 0.085×17.5×64/(15×1000)×100。",
      "hint":"提示：0.085×17.5×64 = 95.2；95.2/(15×1000)×100 = 0.635%。"}
  },
  "cmp": {
    "cols":[{"k":"a"},{"k":"mw","t":"n"},{"k":"eq","t":"n"},{"k":"n","t":"n"},{"k":"food"}],
    "rows":[
      {"a":"檸檬酸 Citric","mw":192,"eq":64,"n":3,"food":"柑橘·莓果·番茄"},
      {"a":"蘋果酸 Malic","mw":134,"eq":67,"n":2,"food":"蘋果·香蕉"},
      {"a":"酒石酸 Tartaric","mw":150,"eq":75,"n":2,"food":"葡萄"},
      {"a":"乳酸 Lactic","mw":90,"eq":90,"n":1,"food":"優格·起司"},
      {"a":"醋酸 Acetic","mw":60,"eq":60,"n":1,"food":"醋·發酵品"},
      {"a":"草酸 Oxalic","mw":90,"eq":45,"n":2,"food":"菠菜等葉菜"}
    ]
  }
}

dc.build_html(
  {"title":"pH 與可滴定酸度 · Nielsen Ch22","brand":"pH/酸度 · CH22"},
  S, CFG, OUT)
