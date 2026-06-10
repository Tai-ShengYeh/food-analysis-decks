# -*- coding: utf-8 -*-
"""TFDA MOHWA0013.03 食品中二氧化硫之檢驗方法 (通氣蒸餾-鹼滴定) — SOIL HTML deck.
Source: 衛福部食藥署公告法 MOHWA0013.03. Run: python build_so2.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
APPARATUS_SVG = """
<svg viewBox="0 0 620 330">
 <text x="310" y="22" text-anchor="middle" class="lblb" font-size="15">通氣蒸餾裝置：把 SO₂ 從食品趕進吸收液</text>
 <!-- N2 source -->
 <rect x="20" y="200" width="60" height="80" rx="8" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
 <text x="50" y="245" text-anchor="middle" class="lbl">N₂</text><text x="50" y="298" text-anchor="middle" class="lbl">氮氣</text>
 <line x1="80" y1="235" x2="150" y2="235" stroke="#1f9d6b" stroke-width="3" marker-end="url(#sa)"/>
 <defs><marker id="sa" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#1f9d6b"/></marker></defs>
 <!-- round-bottom flask (sample+acid) -->
 <circle cx="190" cy="250" r="42" fill="#fbeede" stroke="#d9822b" stroke-width="2.4"/>
 <path d="M178 212 h24 v-18 h-24 Z" fill="#fbeede" stroke="#d9822b" stroke-width="2.4"/>
 <text x="190" y="250" text-anchor="middle" class="lblb" font-size="12">檢體</text>
 <text x="190" y="267" text-anchor="middle" class="lbl" font-size="11">+磷酸</text>
 <text x="190" y="312" text-anchor="middle" class="lbl">圓底燒瓶(加熱)</text>
 <path d="M170 300 q8 14 16 0 q8 -14 16 0" fill="none" stroke="#d94f4f" stroke-width="2.2"/>
 <text x="225" y="308" class="lbl">🔥本生燈</text>
 <!-- tube up to condenser -->
 <line x1="190" y1="194" x2="190" y2="150" stroke="#48597a" stroke-width="3"/>
 <line x1="190" y1="150" x2="330" y2="150" stroke="#48597a" stroke-width="3"/>
 <!-- condenser -->
 <rect x="330" y="120" width="120" height="40" rx="8" fill="#cfe0f6" stroke="#1f6feb" stroke-width="2.2"/>
 <text x="390" y="113" text-anchor="middle" class="lbl">雙層冷凝管(冷卻水)</text>
 <line x1="450" y1="150" x2="500" y2="150" stroke="#48597a" stroke-width="3"/>
 <line x1="500" y1="150" x2="500" y2="200" stroke="#48597a" stroke-width="3"/>
 <!-- pear flask (absorber H2O2) -->
 <path d="M470 205 q30 60 60 0 q-10 -25 -30 -25 q-20 0 -30 25 Z" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.4"/>
 <text x="500" y="232" text-anchor="middle" class="lblb" font-size="11">H₂O₂</text>
 <text x="500" y="290" text-anchor="middle" class="lbl">梨形燒瓶</text>
 <text x="500" y="306" text-anchor="middle" class="lbl">吸收液</text>
 <text x="560" y="160" class="lbl" fill="#1f6feb">SO₂→H₂SO₄</text>
</svg>"""

CHEM_SVG = """
<svg viewBox="0 0 980 200">
 <defs><marker id="ca" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="490" y="26" text-anchor="middle" class="lblb" font-size="15">四步化學：酸化釋出 → 載氣帶出 → 吸收氧化 → 鹼滴定</text>
 <g font-size="13">
  <rect x="14" y="70" width="180" height="64" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="104" y="96" text-anchor="middle" class="lblb">亞硫酸鹽</text><text x="104" y="116" text-anchor="middle" class="lbl">SO₃²⁻ / HSO₃⁻</text>
  <rect x="270" y="70" width="180" height="64" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="360" y="96" text-anchor="middle" class="lblb">SO₂ 氣體</text><text x="360" y="116" text-anchor="middle" class="lbl">加磷酸→釋出↑</text>
  <rect x="526" y="70" width="180" height="64" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="616" y="96" text-anchor="middle" class="lblb">硫酸 H₂SO₄</text><text x="616" y="116" text-anchor="middle" class="lbl">H₂O₂ 吸收氧化</text>
  <rect x="782" y="70" width="184" height="64" rx="10" fill="#fbe7e7" stroke="#d94f4f" stroke-width="2.2"/>
  <text x="874" y="96" text-anchor="middle" class="lblb">NaOH 滴定</text><text x="874" y="116" text-anchor="middle" class="lbl">至橄欖綠終點</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#ca)">
  <line x1="194" y1="102" x2="266" y2="102"/><line x1="450" y1="102" x2="522" y2="102"/><line x1="706" y1="102" x2="778" y2="102"/></g>
 <text x="232" y="92" text-anchor="middle" class="lbl">+磷酸</text>
 <text x="488" y="92" text-anchor="middle" class="lbl">N₂帶出</text>
 <text x="744" y="92" text-anchor="middle" class="lbl">氧化</text>
 <text x="490" y="172" text-anchor="middle" class="lbl">SO₂ + H₂O₂ → H₂SO₄；H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O　(1 mL 0.01N NaOH ≙ 0.32 mg SO₂)</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("食藥署公告檢驗方法 · MOHWA0013.03",
    "食品中<span style='color:var(--accent-2)'>二氧化硫</span>檢驗", "Sulfur Dioxide in Foods",
    "食品安全檢測　·　3 小時課程　·　含 6 個互動小遊戲<br>亞硫酸鹽 · 通氣蒸餾 · H₂O₂ 吸收 · 鹼滴定 (Monier-Williams)",
    ["金針/筍乾/蜜餞","通氣蒸餾","H₂O₂氧化","NaOH滴定","氣喘風險"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">金針、筍乾、蜜餞為什麼<br>那麼<span class="hi">鮮黃漂亮、又不發霉</span>？</div>
  <p class="subtitle" style="max-width:840px;margin:22px auto 0">很可能加了<strong>二氧化硫(亞硫酸鹽)</strong>——它能漂白、防腐、抗氧化、防褐變。<br>
  適量合法，但<strong>過量會誘發氣喘</strong>。食藥署 <strong>MOHWA0013.03</strong> 用通氣蒸餾＋鹼滴定來定量。</p>
  <div style="margin-top:24px"><span class="pill">漂白增色</span><span class="pill">防腐保鮮</span>
  <span class="pill">過敏原</span><span class="pill">氣喘誘發</span></div></div>""")

add(MOT, dc.kt("背景", "亞硫酸鹽為什麼<span class='hi'>無所不在</span>") +
    '<div class="grid2" style="margin-top:20px">' +
    dc.card("🌼","漂白防褐變","保持金針、蝦、脫水蔬果的色澤，防止酵素性褐變","b") +
    dc.card("🦠","防腐抗菌","抑制葡萄酒、蜜餞中的雜菌與酵母","a") +
    dc.card("🍋","抗氧化","保護維生素 C、延緩氧化變色","g") +
    dc.card("😮‍💨","健康風險","過量殘留可誘發<strong>氣喘</strong>與過敏，須限量並標示","b") + '</div>')

add(MOT, dc.kt("方法原理", "四步驟把 SO₂<span class='hi'>抓出來秤</span>") +
    '<div class="svgwrap" style="margin-top:8px">' + CHEM_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:8px">酸化讓亞硫酸鹽釋出 SO₂ 氣體 → 氮氣帶著它蒸餾出來 → 過氧化氫吸收並氧化成硫酸 → 用氫氧化鈉滴定。</p>')

add(MOT, dc.kt("裝置", "通氣蒸餾裝置長這樣") +
    '<div class="svgwrap" style="margin-top:6px">' + APPARATUS_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:8px">圓底燒瓶(檢體+磷酸，加熱) → 雙層冷凝管 → 梨形燒瓶(H₂O₂ 吸收液)；全程通氮氣帶出 SO₂。</p>')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","趕出 SO₂ vs 吸收滴定", 8,
    "把 8 個試劑/裝置分到「釋放並帶出 SO₂」或「吸收並滴定 SO₂」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("為什麼要通氮蒸餾", "把 SO₂ 與食品<span class='hi'>分離</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>食品基質複雜，直接測會被干擾 → 先把 SO₂ 變成<strong>氣體分離出來</strong></li>" +
    "<li>加 <strong>25%磷酸</strong>酸化，使結合態亞硫酸鹽釋出 SO₂</li>" +
    "<li>通<strong>氮氣(0.5–0.6 L/min)</strong>當載氣，把 SO₂ 持續帶向冷凝管</li>" +
    "<li>加<strong>矽油防起泡、沸石防暴沸</strong>，微細火焰加熱約 10 分鐘</li>" +
    '</ul></div><div class="note"><strong>為何通『氮』不通空氣？</strong><br>' +
    "避免空氣中的氧在高溫下把 SO₂ 提前氧化、或讓檢體成分氧化造成誤差。</div></div>")

add(ATT, dc.kt("吸收與氧化", "H₂O₂ 把 SO₂ 變成<span class='hi'>硫酸</span>") +
    '<div class="grid2" style="margin-top:16px"><div class="eq">SO₂ + H₂O₂ → H₂SO₄</div>' +
    '<div><ul class="clean"><li>梨形燒瓶內裝 <strong>0.3% 過氧化氫</strong>吸收液</li>' +
    "<li>SO₂ 被氧化成<strong>硫酸</strong>，固定在吸收液中</li>" +
    "<li>原本不易直接滴定的 SO₂，轉成可用<strong>酸鹼滴定</strong>定量的 H₂SO₄</li></ul></div></div>" +
    '<div class="note" style="margin-top:14px">這是 <strong>Monier-Williams</strong> 法的精髓：用化學反應把氣體「固定」成可滴定的強酸。</div>')

add(ATT, dc.kt("滴定與指示劑", "滴到<span class='hi'>橄欖綠</span>就是終點") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>混合指示劑</strong>：甲基紅 0.2 g + 亞甲藍 0.1 g(溶於乙醇)</li>" +
    "<li>吸收液先調成<strong>橄欖綠</strong>(加指示劑變紫，再以 NaOH 微調)</li>" +
    "<li>蒸餾後生成的硫酸使溶液變色，再以 <strong>0.01 N NaOH</strong> 滴回橄欖綠</li>" +
    "<li>同時做<strong>空白</strong>(不含檢體)校正試劑與環境</li>" +
    '</ul></div><div class="note"><strong>混合指示劑</strong>比單一指示劑變色更銳利，' +
    "在這個 pH 範圍的終點(橄欖綠)更好判讀。</div></div>")

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","二氧化硫方法即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("計算", "從滴定量到<span class='hi'>SO₂ 含量</span>") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">SO₂ (g/kg) = ' +
    '<span class="frac"><b>(C − B) × f × 0.32</b><span>W</span></span></div>' +
    '<div><ul class="clean"><li><strong>C</strong>：檢液之 0.01 N NaOH 滴定量(mL)</li>' +
    "<li><strong>B</strong>：空白之滴定量(mL)</li>" +
    "<li><strong>f</strong>：0.01 N NaOH 力價</li>" +
    "<li><strong>0.32</strong>：1 mL 0.01 N NaOH ≙ 0.32 mg SO₂</li>" +
    "<li><strong>W</strong>：取樣重量(g)</li></ul></div></div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","亞硫酸鹽的三大功能配實例", 6,
    "把 6 個情境分到「漂白/防褐變」「防腐抗菌」或「抗氧化保鮮」。"), ' data-game="g3"')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","二氧化硫檢驗流程排序", 6,
    "用 ▲▼ 把通氣蒸餾-鹼滴定法的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：二氧化硫判斷", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("二氧化硫的幾種檢驗法（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"acc","t":"n","label":"準確度","star":True},
     {"k":"eq","t":"s","label":"設備"},{"k":"use","t":"s","label":"特點/用途"}],
    "★ 越多越準確。公告法為通氣蒸餾-鹼滴定。", kicker="方法比較"), ' data-game="cmp"')

add(ACT, dc.chart_inner("so2food", "哪些食品<span class='hi'>常驗出</span>二氧化硫",
    "示意常見範圍(mg/kg)，非特定產品；不同食品有各自法規限量。乾金針、脫水蔬果通常較高。",
    kicker="背景數據", height="52vh"), ' data-chart="so2food"')

add(ACT, dc.kt("健康與法規", "適量合法、過量<span class='hi'>有風險</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("📏","限量管理","各類食品有最大殘留限量(以 SO₂ 計)，超量即違規","b") +
    dc.card("😮‍💨","氣喘與過敏","亞硫酸鹽是常見過敏原，敏感者(尤其氣喘患者)可能誘發症狀","a") +
    dc.card("🏷️","須標示","含一定量亞硫酸鹽須在成分標示，保護過敏族群","g") +
    dc.card("💧","會流失","水煮、浸泡可降低部分殘留；但檢驗看的是『產品當下』含量","b") + '</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：SO₂ 含量",
    "某乾筍檢體取樣 <b>W = 20 g</b>；檢液滴定量 <b>C = 12.5 mL</b>、空白 <b>B = 0.5 mL</b>、力價 <b>f = 1.00</b>。"
    "求 SO₂ 含量(g/kg)。公式：(C−B)×f×0.32/W。", unit="g/kg"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>SO₂(亞硫酸鹽)用於<strong>漂白、防腐、抗氧化、防褐變</strong></li>" +
    "<li>方法四步：<strong>酸化釋出→通氮蒸餾→H₂O₂吸收氧化→NaOH滴定</strong></li>" +
    "<li>H₂O₂ 把 SO₂ 氧化成 <strong>H₂SO₄</strong>，再用 0.01 N NaOH 滴定</li></ul>" +
    '<ul class="clean"><li>終點＝<strong>橄欖綠</strong>(甲基紅+亞甲藍混合指示劑)，須做空白</li>' +
    "<li>含量 = (C−B)×f×0.32/W；1 mL 0.01N NaOH ≙ 0.32 mg SO₂；LOQ 0.01 g/kg</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說出二氧化硫在食品的用途與健康風險",
     "解釋為什麼要『酸化＋通氮蒸餾』把 SO₂ 分離出來",
     "寫出 H₂O₂ 吸收氧化 SO₂ 的反應與目的",
     "說明混合指示劑與橄欖綠終點、為何要做空白",
     "用 (C−B)×f×0.32/W 計算 SO₂ 含量",
     "解釋 0.32 這個換算因子的由來",
     "比較蒸餾滴定法與比色法/GC-MS/快篩的差異",
     "舉出至少三種常含亞硫酸鹽的食品"]))

add(ACT, dc.cover("延伸 · CONNECT",
    "從一把金針<br><span style='color:var(--accent-2)'>看懂亞硫酸鹽</span>", "",
    "🔗 對照學習：本法是<strong>古典濕式滴定</strong>，與甜味劑/四環素的 LC-MS/MS 形成互補<br>"
    "🔬 銜接：<strong>灰分/礦物前處理 (Ch16)</strong>、滴定分析、食品添加物管理<br>"
    "🧪 思考：同一塊乾筍，為何取樣量不同檢出值要相關？通氮為何不能改通空氣？",
    ["亞硫酸鹽","通氣蒸餾","H₂O₂氧化","酸鹼滴定","食安檢測"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "so2food": {"type":"bar","yTitle":"SO₂ 示意含量 (mg/kg)",
      "labels":["乾金針","脫水蔬果","筍乾","蜜餞","白葡萄酒","冷凍蝦","澱粉"],
      "datasets":[{"label":"SO₂ (mg/kg, 示意)","data":[2000,800,500,400,200,100,50],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["釋放並帶出 SO₂","吸收並滴定 SO₂"],
      "items":[{"t":"25%磷酸(酸化使釋出 SO₂)","c":"釋放並帶出 SO₂"},
        {"t":"氮氣(載氣帶出 SO₂)","c":"釋放並帶出 SO₂"},
        {"t":"本生燈微細火焰加熱蒸餾","c":"釋放並帶出 SO₂"},
        {"t":"沸石(防止暴沸)","c":"釋放並帶出 SO₂"},
        {"t":"0.3%過氧化氫(吸收並氧化成硫酸)","c":"吸收並滴定 SO₂"},
        {"t":"甲基紅+亞甲藍混合指示劑","c":"吸收並滴定 SO₂"},
        {"t":"0.01 N 氫氧化鈉(滴定)","c":"吸收並滴定 SO₂"},
        {"t":"梨形燒瓶(裝吸收液)","c":"吸收並滴定 SO₂"}],
      "ok":"🎉 全對！前段把 SO₂ 酸化釋出並用氮氣蒸餾帶出；後段用 H₂O₂ 吸收氧化再滴定。",
      "tip":"提示：跟『酸化、加熱、載氣』有關→釋放帶出；跟『吸收液、指示劑、滴定』有關→吸收滴定。"},
    "g3": {"cats":["漂白/防褐變","防腐抗菌","抗氧化保鮮"],
      "items":[{"t":"保持乾金針鮮黃、不褐變","c":"漂白/防褐變"},
        {"t":"防止蝦類產生黑斑(黑變)","c":"漂白/防褐變"},
        {"t":"抑制葡萄酒中的雜菌與酵母","c":"防腐抗菌"},
        {"t":"延長蜜餞的保存期限","c":"防腐抗菌"},
        {"t":"防止脫水蔬果氧化變色","c":"抗氧化保鮮"},
        {"t":"保護果汁中的維生素 C","c":"抗氧化保鮮"}],
      "ok":"🎉 正確！亞硫酸鹽同時具漂白/防褐變、防腐抗菌、抗氧化三大功能。",
      "tip":"提示：顏色相關→漂白/防褐變；抑菌相關→防腐；防氧化變質相關→抗氧化。"}
  },
  "mcq": {
    "g2":[
      {"q":"本方法 MOHWA0013.03 的定量原理是？","o":["紫外光吸收","通氣蒸餾後以鹼滴定","原子吸收","層析"],"a":1,
       "e":"檢體經酸化、通氮蒸餾，SO₂ 被 H₂O₂ 吸收氧化成硫酸，再以 NaOH 滴定。"},
      {"q":"加入 25% 磷酸的目的是？","o":["中和","酸化使亞硫酸鹽釋出 SO₂ 氣體","當吸收液","當指示劑"],"a":1,
       "e":"酸化把結合態亞硫酸鹽轉為 SO₂ 氣體，便於蒸餾帶出。"},
      {"q":"梨形燒瓶中的 0.3% 過氧化氫扮演什麼角色？","o":["指示劑","吸收並把 SO₂ 氧化成硫酸","催化劑","載氣"],"a":1,
       "e":"H₂O₂ 吸收 SO₂ 並氧化成 H₂SO₄，固定後才能用酸鹼滴定。"},
      {"q":"滴定終點的顏色判斷是？","o":["無色→粉紅","橄欖綠","藍→黃","紅→橙"],"a":1,
       "e":"以甲基紅+亞甲藍混合指示劑，滴定至溶液呈橄欖綠為終點。"},
      {"q":"換算因子 0.32 代表？","o":["每克樣品 0.32 mL","1 mL 0.01N NaOH 相當 0.32 mg SO₂","0.32% 過氧化氫","pH 0.32"],"a":1,
       "e":"1 mL 0.01 N NaOH 中和的硫酸相當於 0.32 mg SO₂。"}
    ],
    "g5":[
      {"q":"蒸餾時若把通『氮氣』改成通『空氣』，主要風險是？","o":["沒差","氧會造成額外氧化、結果失真","SO₂ 不會釋出","溫度太低"],"a":1,
       "e":"空氣中的氧在高溫下會額外氧化，造成檢驗結果偏差，故用惰性氮氣。"},
      {"q":"為什麼一定要同時做『空白』？","o":["增加樣品數","校正試劑與環境帶來的滴定量","加快速度","當對照甜度"],"a":1,
       "e":"空白可扣除試劑/環境本身消耗的 NaOH，使結果準確。"},
      {"q":"檢出值接近法規限值時，方法建議？","o":["直接判定","適度調整取樣量並比較相關性以確認轉化完全","只測一次","改測甜度"],"a":1,
       "e":"接近限值時調整取樣量、比較檢出值與取樣量相關性，確保 SO₂ 完全轉化吸收。"},
      {"q":"現場想快速初篩大量乾貨是否含亞硫酸鹽，較適合？","o":["通氣蒸餾滴定","快篩試劑組","GC-MS","凱氏定氮"],"a":1,
       "e":"快篩試劑組適合現場半定量初篩；確認與定量再用公告法。"},
      {"q":"加入矽油與沸石的目的分別是？","o":["增色與防腐","防起泡與防暴沸","吸收與氧化","指示與滴定"],"a":1,
       "e":"矽油消泡、沸石防止暴沸，使蒸餾平穩。"}
    ]
  },
  "sort": {
    "g4":{"steps":["梨形燒瓶加 0.3% H₂O₂ 與混合指示劑，調成橄欖綠吸收液","檢體切細稱重置於圓底燒瓶，加乙醇、25%磷酸、矽油、沸石",
       "接上裝置，通氮氣(0.5–0.6 L/min)當載氣","以微細火焰加熱蒸餾約 10 分鐘，SO₂ 被 H₂O₂ 吸收氧化成硫酸",
       "以 0.01 N NaOH 滴定吸收液至橄欖綠終點(另做空白)","以 (C−B)×f×0.32/W 計算 SO₂ 含量"],
       "shuffle":[2,4,0,5,1,3],
       "ok":"🎉 順序正確！備吸收液→裝樣加酸→通氮→加熱蒸餾→滴定→計算。",
       "tip":"提示：先備好吸收液與檢體，通氮後才加熱蒸餾；蒸餾完成才滴定計算。"}
  },
  "calc": {
    "g6":{"answer":0.192,"tol":0.01,
      "ok":"🎉 正確！(12.5−0.5)×1.00×0.32/20 = 12×0.32/20 = 3.84/20 = <b>0.192 g/kg</b>。",
      "bad":"再算算：先 (C−B)=12.5−0.5=12，再 ×f×0.32÷W。",
      "hint":"提示：(12.5−0.5)=12；12×1.00×0.32=3.84；3.84/20=0.192 g/kg。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"acc","t":"n","star":True},{"k":"eq"},{"k":"use"}],
    "rows":[
      {"m":"通氣蒸餾-鹼滴定(公告法)","acc":5,"eq":"通氣蒸餾裝置","use":"官方定量法·準確·需熟練"},
      {"m":"比色法(副玫瑰苯胺)","acc":4,"eq":"分光光度計","use":"靈敏·適低含量"},
      {"m":"GC-MS","acc":5,"eq":"GC-MS","use":"高專一·可確認"},
      {"m":"快篩試劑組","acc":2,"eq":"試劑組","use":"現場初篩·半定量"}
    ]
  }
}

dc.build_html(
  {"title":"食品中二氧化硫檢驗 · MOHWA0013.03","brand":"二氧化硫 · 滴定"},
  S, CFG, OUT)
