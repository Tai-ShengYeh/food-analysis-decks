# -*- coding: utf-8 -*-
"""TFDA TFDAA0063.00 食品中二氧化硫之檢驗方法 (氣相層析質譜法 / 頂空 GC-MS) — SOIL HTML deck.
Source: 衛福部食藥署 TFDAA0063.00. Run: python build_so2_gcms.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
HEADSPACE_SVG = """
<svg viewBox="0 0 640 320">
 <text x="320" y="24" text-anchor="middle" class="lblb" font-size="15">頂空(Headspace)進樣：只取上部揮發出的 SO₂ 氣體</text>
 <!-- vial -->
 <rect x="120" y="70" width="150" height="190" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2.4"/>
 <rect x="150" y="54" width="90" height="20" rx="4" fill="#48597a"/>
 <text x="195" y="48" text-anchor="middle" class="lbl">鋁蓋封瓶</text>
 <!-- liquid -->
 <rect x="122" y="195" width="146" height="63" rx="0" fill="#cfe0f6"/>
 <path d="M122 195 h146" stroke="#1f6feb" stroke-width="1.5"/>
 <text x="195" y="232" text-anchor="middle" class="lbl">檢體 + 磷酸 + NaCl</text>
 <!-- headspace SO2 dots -->
 <g fill="#d9822b"><circle cx="160" cy="110" r="4"/><circle cx="200" cy="130" r="4"/><circle cx="235" cy="105" r="4"/>
  <circle cx="180" cy="155" r="4"/><circle cx="220" cy="170" r="4"/><circle cx="150" cy="135" r="4"/></g>
 <text x="195" y="95" text-anchor="middle" class="lblb" fill="#d9822b" font-size="12">頂空：SO₂ 氣體</text>
 <!-- heat -->
 <path d="M150 270 q8 14 16 0 q8 -14 16 0 q8 14 16 0" fill="none" stroke="#d94f4f" stroke-width="2.4"/>
 <text x="195" y="292" text-anchor="middle" class="lbl">加熱 80°C · 15 分 · 攪拌</text>
 <!-- needle -->
 <line x1="195" y1="54" x2="195" y2="30" stroke="#15233f" stroke-width="2"/>
 <line x1="320" y1="30" x2="195" y2="30" stroke="#15233f" stroke-width="2"/>
 <!-- arrow to GC-MS -->
 <defs><marker id="ha" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#1f9d6b"/></marker></defs>
 <line x1="340" y1="150" x2="430" y2="150" stroke="#1f9d6b" stroke-width="3" marker-end="url(#ha)"/>
 <text x="385" y="140" text-anchor="middle" class="lbl">取 1 mL 氣體</text>
 <rect x="440" y="110" width="180" height="80" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.4"/>
 <text x="530" y="145" text-anchor="middle" class="lblb">GC-MS</text>
 <text x="530" y="168" text-anchor="middle" class="lbl">分離 + 質譜偵測</text>
 <text x="320" y="312" text-anchor="middle" class="lbl">只取氣相 → 不揮發的基質留在瓶裡，不汙染管柱與離子源</text>
</svg>"""

GCMS_SVG = """
<svg viewBox="0 0 980 210">
 <defs><marker id="ga" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="490" y="26" text-anchor="middle" class="lblb" font-size="15">頂空 GC-MS / SIM：先分離、再以特定 m/z 專一偵測</text>
 <g font-size="13">
  <rect x="14" y="72" width="160" height="58" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="94" y="96" text-anchor="middle" class="lblb">頂空進樣</text><text x="94" y="115" text-anchor="middle" class="lbl">85°C · 1 mL</text>
  <rect x="222" y="72" width="190" height="58" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="317" y="96" text-anchor="middle" class="lblb">GC 分離</text><text x="317" y="115" text-anchor="middle" class="lbl">DB-624 · 45→240°C</text>
  <rect x="460" y="72" width="190" height="58" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="555" y="96" text-anchor="middle" class="lblb">MS · EI 70 eV</text><text x="555" y="115" text-anchor="middle" class="lbl">SIM 選擇性離子</text>
  <rect x="698" y="76" width="268" height="50" rx="9" fill="#15233f"/>
  <text x="832" y="98" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">SO₂ m/z 64(定量)·48(定性)</text>
  <text x="832" y="116" text-anchor="middle" fill="#cfe0f6" font-size="11">內標 2-氯甲苯 m/z 126</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#ga)">
  <line x1="174" y1="101" x2="218" y2="101"/><line x1="412" y1="101" x2="456" y2="101"/><line x1="650" y1="101" x2="694" y2="101"/></g>
 <text x="490" y="186" text-anchor="middle" class="lbl">SIM 只盯特定 m/z → 雜訊低、專一性高，能在複雜基質中確認 SO₂</text>
</svg>"""

CHROM_SVG = """
<svg viewBox="0 0 640 230">
 <text x="320" y="22" text-anchor="middle" class="lblb" font-size="15">內標法：比較 SO₂ 與內標(2-氯甲苯)的波峰面積</text>
 <line x1="60" y1="180" x2="600" y2="180" stroke="#48597a" stroke-width="1.6"/>
 <line x1="60" y1="180" x2="60" y2="44" stroke="#48597a" stroke-width="1.6"/>
 <!-- SO2 peak (thin) at ~3.87 min -->
 <path d="M150 180 C158 70 168 70 176 180" fill="none" stroke="#1f9d6b" stroke-width="2.6"/>
 <text x="163" y="60" text-anchor="middle" class="lblb" fill="#1f9d6b" font-size="12">SO₂</text>
 <text x="163" y="198" text-anchor="middle" class="lbl">3.87 min · m/z 64</text>
 <!-- I.S. peak (thin) at ~9.995 min -->
 <path d="M470 180 C478 90 488 90 496 180" fill="none" stroke="#d9822b" stroke-width="2.6"/>
 <text x="483" y="80" text-anchor="middle" class="lblb" fill="#d9822b" font-size="12">2-氯甲苯 (I.S.)</text>
 <text x="483" y="198" text-anchor="middle" class="lbl">9.995 min · m/z 126</text>
 <text x="330" y="216" text-anchor="middle" class="lbl">滯留時間 (分) →　以 SO₂/內標 面積比定量，校正進樣與基質變異</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("食藥署公告檢驗方法 · TFDAA0063.00",
    "食品中<span style='color:var(--accent-2)'>二氧化硫</span> · GC-MS 法", "Sulfur Dioxide in Foods · GC/MS",
    "食品安全檢測　·　3 小時課程　·　含 6 個互動小遊戲<br>頂空進樣 · 氣相層析質譜 · SIM · 內標法 · 干擾確認",
    ["頂空 Headspace","GC-MS","SIM m/z 64","2-氯甲苯內標","干擾時改用"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">同樣是驗二氧化硫，<br>為什麼除了滴定法，還要一個 <span class="hi">GC-MS 法</span>？</div>
  <p class="subtitle" style="max-width:850px;margin:22px auto 0">滴定法測「總量」很好用，但遇到<strong>會干擾的食品基質</strong>就可能失準。<br>
  這時改用 <strong>頂空氣相層析質譜法 (TFDAA0063)</strong>——靠特定 <strong>m/z</strong> 專一確認，干擾物再多也能認出 SO₂。</p>
  <div style="margin-top:24px"><span class="pill">更專一</span><span class="pill">避基質干擾</span>
  <span class="pill">確認/仲裁</span><span class="pill">與滴定互補</span></div></div>""")

add(MOT, dc.kt("背景", "二氧化硫的<span class='hi'>兩種</span>官方檢驗法") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("⚗️","通氣蒸餾-鹼滴定 (MOHWA0013)","酸化釋出 SO₂→H₂O₂ 吸收→NaOH 滴定；<strong>公告法、結果以此為準</strong>，設備簡單、測總量","b") +
    dc.card("🔬","頂空 GC-MS (TFDAA0063)","加熱讓 SO₂ 揮發到頂空→GC 分離→MS 以 m/z 偵測；<strong>高專一</strong>，食品有<strong>干擾時改用</strong>","a") +
    '</div><div class="note" style="margin-top:14px">兩法互補：滴定法快速測總量；GC-MS 法在複雜或干擾基質中，提供<strong>更專一的確認</strong>。</div>')

add(MOT, dc.kt("方法核心", "頂空：只取<span class='hi'>揮發出來</span>的 SO₂") +
    '<div class="svgwrap" style="margin-top:4px">' + HEADSPACE_SVG + '</div>')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","滴定法 vs GC-MS 法", 8,
    "把 8 個特徵分到「通氣蒸餾滴定法 (MOHWA0013)」或「頂空 GC-MS 法 (TFDAA0063)」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("為什麼用頂空", "把樣品的麻煩<span class='hi'>留在瓶裡</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>SO₂ 容易<strong>揮發</strong>：加熱後它會跑到瓶子<strong>上部空間(頂空)</strong></li>" +
    "<li>只抽取<strong>頂空氣體</strong>進 GC-MS → 不揮發的糖、色素、蛋白等<strong>留在瓶裡</strong></li>" +
    "<li>避免基質<strong>汙染管柱與離子源</strong>、降低干擾</li>" +
    "<li>加<strong>氯化鈉鹽析</strong>、加熱 80°C，把更多 SO₂ 趕到頂空</li>" +
    '</ul></div><div class="note"><strong>頂空 = 乾淨的氣相取樣。</strong><br>' +
    "這正是它能在『會干擾滴定法』的食品中，仍精準測 SO₂ 的關鍵。</div></div>")

add(ATT, dc.kt("前處理試劑", "釋出、保護、再<span class='hi'>校正</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧪","釋出 SO₂","<strong>磷酸</strong>酸化使亞硫酸鹽釋出 SO₂；<strong>氯化鈉</strong>鹽析降低其溶解度","b") +
    dc.card("🛡️","保護 SO₂","<strong>甘露醇</strong>抗氧化、<strong>EDTA-2Na</strong> 螯合金屬離子——防 SO₂ 在前處理被氧化流失","a") +
    '</div><div class="note" style="margin-top:14px"><strong>內標：</strong>加入 <strong>2-氯甲苯</strong>當內部標準品(I.S.)，' +
    "用來校正進樣量與基質造成的訊號變異。</div>")

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","GC-MS 法即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("GC-MS / SIM", "先分離，再用 <span class='hi'>m/z</span> 專一偵測") +
    '<div class="svgwrap" style="margin-top:4px">' + GCMS_SVG + '</div>' +
    '<div class="note" style="margin-top:8px">GC 用 <strong>DB-624 毛細管柱</strong>(45→240°C 升溫)把成分分開；MS 以 <strong>EI 70 eV</strong> 游離、' +
    "<strong>SIM 選擇性離子偵測</strong>：SO₂ 看 <strong>m/z 64(定量)、48(定性)</strong>，內標 2-氯甲苯看 <strong>m/z 126</strong>。</div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","試劑功能：釋出 / 保護 / 偵測", 6,
    "把 6 個試劑/角色分到「釋出 SO₂」「保護 SO₂ 不流失」或「偵測與校正」。"), ' data-game="g3"')

add(ATT, dc.kt("內標法定量", "為什麼要加<span class='hi'>內部標準</span>") +
    '<div class="svgwrap" style="margin-top:4px">' + CHROM_SVG + '</div>' +
    '<div class="note" style="margin-top:8px">頂空進樣的氣體量、基質效應都會讓訊號浮動；以已知量的 <strong>2-氯甲苯</strong>當內標，' +
    "用 <strong>SO₂/內標的波峰面積比</strong>對標準曲線定量，可抵銷這些變異、提高準確度。</div>")

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","頂空 GC-MS 檢驗流程排序", 6,
    "用 ▲▼ 把頂空 GC-MS 法(TFDAA0063)的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("鑑別與計算", "離子比確認 + 面積比定量") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">SO₂ (g/kg) = ' +
    '<span class="frac"><b>C</b><span>W</span></span> × 10⁻³</div>' +
    '<div><ul class="clean"><li><strong>C</strong>：由標準曲線求得的 SO₂ 量(µg)</li>' +
    "<li><strong>W</strong>：取樣分析檢體重量(g)</li>" +
    "<li>鑑別：滯留時間 + <strong>定性/定量離子比(48/64)</strong>落在容許範圍</li>" +
    "<li>定量極限 LOQ = <strong>0.01 g/kg</strong></li></ul></div></div>")

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：何時用 GC-MS", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("二氧化硫的幾種檢驗法（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"spec","t":"n","label":"專一性","star":True},
     {"k":"eq","t":"s","label":"設備"},{"k":"use","t":"s","label":"特點"}],
    "★ 越多越專一。GC-MS 法(TFDAA0063)為干擾時的確認法。", kicker="方法比較"), ' data-game="cmp"')

add(ACT, dc.chart_inner("oven", "GC 的<span class='hi'>升溫程式</span>",
    "DB-624 管柱：初溫 45°C 恆溫 4.5 分 → 60°C/min 升至 240°C → 恆溫。升溫讓不同成分依序沖出、分離。",
    kicker="層析條件", height="48vh"), ' data-chart="oven"')

add(ACT, dc.chart_inner("rt", "SIM 圖譜的<span class='hi'>滯留時間</span>",
    "整合自 TFDAA0063 參考層析圖譜(分)：SO₂ 早沖出、內標 2-氯甲苯晚沖出，兩峰分得很開。",
    kicker="層析分離", height="48vh"), ' data-chart="rt"')

add(ACT, dc.kt("意義與應用", "確認法的<span class='hi'>價值</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🎯","高專一確認","看特定 m/z，不受外觀顏色或其他物質干擾，適合『確認/仲裁』","b") +
    dc.card("🧩","與滴定互補","公告滴定法測總量；干擾或爭議樣品改用 GC-MS 確認","a") +
    dc.card("🍷","適用難測基質","深色、複雜、含干擾物的食品(如某些酒類、加工品)","g") +
    dc.card("⚖️","食安把關","亞硫酸鹽過量會誘發氣喘，精準定量才能落實限量管理","b") + '</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：SO₂ 含量",
    "頂空 GC-MS 法：取樣 <b>W = 0.25 g</b>；由標準曲線得 SO₂ 量 <b>C = 250 µg</b>。"
    "求含量(g/kg)。公式：C/W × 10⁻³。", unit="g/kg"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>TFDAA0063 是 SO₂ 的<strong>第二種官方法</strong>(GC-MS)，干擾時改用</li>" +
    "<li><strong>頂空進樣</strong>：只取揮發的 SO₂ 氣體，避基質干擾</li>" +
    "<li>前處理：磷酸釋出、NaCl 鹽析、<strong>甘露醇/EDTA 抗氧化保護</strong></li></ul>" +
    '<ul class="clean"><li>GC(DB-624)分離 → MS <strong>SIM</strong>：SO₂ m/z 64/48、內標 126</li>' +
    "<li><strong>內標法</strong>(2-氯甲苯)以面積比定量；含量 = C/W×10⁻³，LOQ 0.01 g/kg</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明為何 SO₂ 除了滴定法還要 GC-MS 法、兩者如何互補",
     "解釋頂空進樣的原理與『把基質留在瓶裡』的好處",
     "說出磷酸、氯化鈉、甘露醇、EDTA 各自的作用",
     "說明 SIM 偵測與 SO₂ 的定量(64)/定性(48)離子",
     "解釋 2-氯甲苯內標法為何能提高準確度",
     "依序排出頂空 GC-MS 的檢驗流程",
     "用離子比鑑別、用 C/W×10⁻³ 計算 SO₂ 含量",
     "判斷什麼情況下該選 GC-MS 而非滴定法"]))

add(ACT, dc.cover("延伸 · CONNECT",
    "從一種分析物<br><span style='color:var(--accent-2)'>兩種方法</span>", "",
    "🔗 同一 SO₂、兩種官方法：<strong>滴定(MOHWA0013)</strong> 測總量、<strong>GC-MS(TFDAA0063)</strong> 專一確認<br>"
    "🔬 銜接：<strong>氣相層析 (Ch14)</strong>、<strong>質譜 (Ch11)</strong>、頂空進樣、內標定量<br>"
    "🧪 思考：你的樣品基質會干擾嗎？要測總量還是要專一確認？為何頂空能避開不揮發干擾物？",
    ["頂空 GC-MS","SIM","內標法","確認法","食安檢測"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "oven": {"type":"line","yTitle":"管柱溫度 (°C)",
      "labels":["0","4.5","7.75","16"],
      "datasets":[{"label":"DB-624 升溫程式","data":[45,45,240,240],"color":"#d9822b"}]},
    "rt": {"type":"bar","yTitle":"滯留時間 (分)",
      "labels":["二氧化硫 (m/z 64)","2-氯甲苯 I.S. (m/z 126)"],
      "datasets":[{"label":"滯留時間 (min)","data":[3.87,9.995],"color":"#1f6feb"}]}
  },
  "bucket": {
    "g1": {"cats":["通氣蒸餾滴定法 (MOHWA0013)","頂空 GC-MS 法 (TFDAA0063)"],
      "items":[{"t":"通氣蒸餾→H₂O₂ 吸收→NaOH 滴定","c":"通氣蒸餾滴定法 (MOHWA0013)"},
        {"t":"以橄欖綠終點判斷","c":"通氣蒸餾滴定法 (MOHWA0013)"},
        {"t":"公告法、檢驗結果以此為準","c":"通氣蒸餾滴定法 (MOHWA0013)"},
        {"t":"設備相對簡單、不需質譜","c":"通氣蒸餾滴定法 (MOHWA0013)"},
        {"t":"頂空進樣器取上部氣體","c":"頂空 GC-MS 法 (TFDAA0063)"},
        {"t":"以 GC 分離後 MS 偵測","c":"頂空 GC-MS 法 (TFDAA0063)"},
        {"t":"看 m/z 離子、專一性高","c":"頂空 GC-MS 法 (TFDAA0063)"},
        {"t":"食品基質有干擾時改用","c":"頂空 GC-MS 法 (TFDAA0063)"}],
      "ok":"🎉 全對！滴定法是公告法、測總量；GC-MS 看 m/z、專一性高，干擾時改用。",
      "tip":"提示：跟『蒸餾、滴定、橄欖綠、公告法』有關→滴定；跟『頂空、GC、m/z、質譜』有關→GC-MS。"},
    "g3": {"cats":["釋出 SO₂","保護 SO₂ 不流失","偵測與校正"],
      "items":[{"t":"磷酸酸化","c":"釋出 SO₂"},
        {"t":"氯化鈉鹽析(降低 SO₂ 溶解度)","c":"釋出 SO₂"},
        {"t":"甘露醇抗氧化","c":"保護 SO₂ 不流失"},
        {"t":"EDTA-2Na 螯合金屬離子","c":"保護 SO₂ 不流失"},
        {"t":"MS 以 m/z 64 定量 SO₂","c":"偵測與校正"},
        {"t":"2-氯甲苯內部標準校正","c":"偵測與校正"}],
      "ok":"🎉 正確！磷酸/NaCl 釋出、甘露醇/EDTA 保護、MS+內標 偵測校正。",
      "tip":"提示：把 SO₂『趕出來』→釋出；防它『被氧化流失』→保護；『看訊號、校正』→偵測校正。"}
  },
  "mcq": {
    "g2":[
      {"q":"TFDAA0063 法使用的核心儀器是？","o":["分光光度計","頂空進樣氣相層析質譜儀(GC-MS)","原子吸收儀","滴定管"],"a":1,
       "e":"本法以頂空進樣器配 GC-MS 分析揮發出的 SO₂。"},
      {"q":"為什麼取『頂空(上部空間)』氣體分析？","o":["比較快","SO₂ 易揮發、取氣相可避開不揮發基質干擾","顏色好看","省試劑"],"a":1,
       "e":"SO₂ 揮發到頂空，只取氣體可把糖、色素等基質留在瓶裡，降低干擾。"},
      {"q":"加入磷酸的作用是？","o":["中和","酸化使亞硫酸鹽釋出 SO₂","當內標","當吸收液"],"a":1,
       "e":"磷酸酸化使結合態亞硫酸鹽釋出 SO₂ 氣體。"},
      {"q":"SIM 模式中 SO₂ 的『定量離子』m/z 為？","o":["48","64","126","240"],"a":1,
       "e":"SO₂ 定量離子 m/z 64、定性離子 m/z 48；內標 2-氯甲苯 m/z 126。"},
      {"q":"2-氯甲苯在本法中扮演什麼角色？","o":["氧化劑","內部標準品(I.S.)","顯色劑","載氣"],"a":1,
       "e":"2-氯甲苯當內部標準，用於校正進樣與基質造成的訊號變異。"}
    ],
    "g5":[
      {"q":"某深色加工食品會干擾滴定法的 SO₂ 測定，較佳做法？","o":["直接報滴定值","改用頂空 GC-MS 確認(TFDAA0063)","加水稀釋","忽略干擾"],"a":1,
       "e":"基質干擾時，改用專一性高的頂空 GC-MS 法確認。"},
      {"q":"GC-MS 法為何比滴定法更『專一』？","o":["更貴","只盯特定 m/z 離子，不受其他物質干擾","速度快","不需標準品"],"a":1,
       "e":"SIM 只偵測 SO₂ 專屬 m/z，複雜基質中也能專一辨識。"},
      {"q":"頂空進樣相較直接進樣的主要好處？","o":["訊號更強","只取氣相、避免不揮發基質汙染管柱與離子源","不需加熱","可省內標"],"a":1,
       "e":"頂空只引入揮發物，保護儀器並降低基質干擾。"},
      {"q":"加入內標 2-氯甲苯主要校正什麼？","o":["pH","進樣量與基質造成的訊號變異","溫度","顏色"],"a":1,
       "e":"以 SO₂/內標面積比定量，抵銷進樣量與基質效應的波動。"},
      {"q":"SO₂ 的定性/定量離子比(48/64)超出容許範圍，代表？","o":["濃度過高","鑑別不符，需排除干擾再確認","儀器壞了","SO₂ 不存在"],"a":1,
       "e":"離子比超出容許範圍代表可能有干擾或非目標物，須再確認。"}
    ]
  },
  "sort": {
    "g4":{"steps":["檢體切細(液態先脫氣)、精確稱重，置於頂空分析瓶","加入 2-氯甲苯內標、氯化鈉與 25%磷酸，迅速封瓶混勻",
       "頂空進樣器加熱 80°C 15 分鐘,SO₂ 揮發到上部空間","取 1 mL 頂空氣體注入 GC,DB-624 管柱升溫分離",
       "MS 以 EI/SIM 偵測(SO₂ m/z 64/48、內標 m/z 126)","以 SO₂/內標波峰面積比對標準曲線,鑑別並定量"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！秤樣裝瓶→加試劑封瓶→加熱頂空→取氣進 GC→MS SIM 偵測→面積比定量。",
       "tip":"提示：先裝瓶加試劑封好，加熱讓 SO₂ 進頂空後才取氣進樣；最後用面積比定量。"}
  },
  "calc": {
    "g6":{"answer":1.0,"tol":0.05,
      "ok":"🎉 正確！含量 = C/W ×10⁻³ = 250/0.25 ×10⁻³ = 1000×10⁻³ = <b>1.0 g/kg</b>。",
      "bad":"再算算：含量 = C/W ×10⁻³ = 250/0.25 ×10⁻³。",
      "hint":"提示：250/0.25 = 1000；1000 × 10⁻³ = 1.0 g/kg。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"spec","t":"n","star":True},{"k":"eq"},{"k":"use"}],
    "rows":[
      {"m":"通氣蒸餾-鹼滴定(MOHWA0013)","spec":3,"eq":"通氣蒸餾裝置","use":"公告法為準·測總 SO₂·設備簡單"},
      {"m":"頂空 GC-MS(TFDAA0063)","spec":5,"eq":"GC-MS+頂空進樣","use":"高專一(看 m/z)·干擾時改用·內標校正"},
      {"m":"比色法(副玫瑰苯胺)","spec":3,"eq":"分光光度計","use":"靈敏·適低含量"},
      {"m":"快篩試劑組","spec":1,"eq":"試劑組","use":"現場初篩·半定量"}
    ]
  }
}

dc.build_html(
  {"title":"食品中二氧化硫檢驗 GC-MS法 · TFDAA0063","brand":"二氧化硫 · GC-MS"},
  S, CFG, OUT)
