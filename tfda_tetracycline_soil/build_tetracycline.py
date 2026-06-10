# -*- coding: utf-8 -*-
"""TFDA MOHWV0036.06 食品中動物用藥殘留－四環黴素類抗生素 (LC-MS/MS) — SOIL HTML deck.
Source: 衛福部食藥署公告法 MOHWV0036.06. Run: python build_tetracycline.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
CHELATE_SVG = """
<svg viewBox="0 0 900 210">
 <defs><marker id="ta" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="450" y="24" text-anchor="middle" class="lblb" font-size="15">四環素會螯合金屬、黏住蛋白 → 加 EDTA 把它「釋放」出來</text>
 <!-- left: tetracycline bound to metal -->
 <g transform="translate(60,70)">
  <rect x="0" y="20" width="120" height="50" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2.4"/>
  <text x="60" y="42" text-anchor="middle" class="lblb" font-size="12">四環素</text>
  <text x="60" y="60" text-anchor="middle" class="lbl">(被困住)</text>
  <circle cx="140" cy="45" r="16" fill="#8493ad"/><text x="140" y="50" text-anchor="middle" fill="#fff" font-size="11">M²⁺</text>
  <text x="70" y="100" text-anchor="middle" class="lbl">Ca/Mg/Fe + 蛋白</text>
 </g>
 <line x1="300" y1="115" x2="400" y2="115" stroke="#48597a" stroke-width="2.6" marker-end="url(#ta)"/>
 <text x="350" y="105" text-anchor="middle" class="lbl">加 EDTA</text>
 <!-- middle: EDTA grabs metal -->
 <g transform="translate(420,70)">
  <rect x="0" y="20" width="120" height="50" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.4"/>
  <text x="60" y="42" text-anchor="middle" class="lblb" font-size="12">EDTA</text>
  <text x="60" y="60" text-anchor="middle" class="lbl">螯合金屬</text>
  <circle cx="140" cy="45" r="16" fill="#1f6feb"/><text x="140" y="50" text-anchor="middle" fill="#fff" font-size="11">M²⁺</text>
 </g>
 <line x1="660" y1="115" x2="740" y2="115" stroke="#48597a" stroke-width="2.6" marker-end="url(#ta)"/>
 <!-- right: free tetracycline -->
 <g transform="translate(760,70)">
  <rect x="0" y="20" width="120" height="50" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.4"/>
  <text x="60" y="42" text-anchor="middle" class="lblb" font-size="12">自由四環素</text>
  <text x="60" y="60" text-anchor="middle" class="lbl">回收率↑</text>
 </g>
</svg>"""

FLOW_SVG = """
<svg viewBox="0 0 1000 180">
 <defs><marker id="fc" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="500" y="30" text-anchor="middle" class="lblb" font-size="15">四環素殘留檢驗流程</text>
 <g font-size="12.5">
  <rect x="10" y="70" width="170" height="58" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="95" y="94" text-anchor="middle" class="lblb">萃取</text><text x="95" y="113" text-anchor="middle" class="lbl">McIlvaine+EDTA</text>
  <rect x="222" y="70" width="170" height="58" rx="10" fill="#fbe7e7" stroke="#d94f4f" stroke-width="2.2"/>
  <text x="307" y="94" text-anchor="middle" class="lblb">沉澱蛋白</text><text x="307" y="113" text-anchor="middle" class="lbl">三氯醋酸·離心</text>
  <rect x="434" y="70" width="170" height="58" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="519" y="94" text-anchor="middle" class="lblb">SPE 淨化</text><text x="519" y="113" text-anchor="middle" class="lbl">Oasis HLB</text>
  <rect x="646" y="70" width="180" height="58" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="736" y="94" text-anchor="middle" class="lblb">LC-MS/MS</text><text x="736" y="113" text-anchor="middle" class="lbl">CSH C18·ESI⁺·MRM</text>
  <rect x="868" y="74" width="124" height="50" rx="9" fill="#15233f"/>
  <text x="930" y="98" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">鑑別定量</text>
  <text x="930" y="115" text-anchor="middle" fill="#cfe0f6" font-size="10">離子對+RT</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#fc)">
  <line x1="180" y1="99" x2="218" y2="99"/><line x1="392" y1="99" x2="430" y2="99"/>
  <line x1="604" y1="99" x2="642" y2="99"/><line x1="826" y1="99" x2="864" y2="99"/></g>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("食藥署公告檢驗方法 · MOHWV0036.06",
    "食品中<span style='color:var(--accent-2)'>四環素</span>殘留檢驗", "Tetracyclines in Foods",
    "食品安全檢測　·　3 小時課程　·　含 6 個互動小遊戲<br>動物用藥殘留 · LC-MS/MS · McIlvaine-EDTA · SPE · 7 品項",
    ["畜禽水產/蛋/奶/蜜","LC-MS/MS","EDTA 螯合","SPE 淨化","抗藥性風險"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">你吃的雞肉、雞蛋、蜂蜜裡，<br>會不會殘留<span class="hi">抗生素</span>？</div>
  <p class="subtitle" style="max-width:850px;margin:22px auto 0">畜禽水產若用了<strong>四環黴素類抗生素</strong>又沒遵守停藥期就上市，藥物會殘留。<br>
  吃進殘留抗生素恐引發過敏、並助長<strong>抗藥性細菌</strong>。食藥署 <strong>MOHWV0036.06</strong> 用 LC-MS/MS 一次驗 7 種。</p>
  <div style="margin-top:24px"><span class="pill">停藥期</span><span class="pill">最大殘留限量 MRL</span>
  <span class="pill">抗藥性 AMR</span><span class="pill">過敏</span></div></div>""")

add(MOT, dc.kt("背景", "四環黴素類抗生素為什麼要<span class='hi'>管</span>") +
    '<div class="grid2" style="margin-top:20px">' +
    dc.card("💊","廣效抗生素","四環素、土黴素、金黴素…用於畜禽水產治療與防病","b") +
    dc.card("⏳","停藥期","用藥後須等藥物代謝到安全值才能上市；違規即超標","a") +
    dc.card("🦠","抗藥性 AMR","殘留抗生素會篩選出抗藥性細菌，威脅公共衛生","b") +
    dc.card("🍯","涵蓋食品廣","肌肉、內臟、脂肪、蛋類、乳汁、蜂蜜都要監測","g") + '</div>')

add(MOT, dc.kt("7 品項", "這次方法涵蓋的<span class='hi'>四環黴素類</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧬","四種母體藥物","四環黴素(TC)、羥四環黴素/<strong>土黴素</strong>(OTC)、氯四環黴素/<strong>金黴素</strong>(CTC)、脫氧羥四環黴素/<strong>多西環素</strong>(DC)","b") +
    dc.card("🔄","三種差向異構物","4-epimer-TC、4-epimer-OTC、4-epimer-CTC——母體在酸性下會差向異構化的產物，也須監測","a") +
    '</div><p class="subtitle" style="margin-top:14px">共 <strong>7 品項</strong>：4 個母體 + 3 個差向異構物(epimer)。</p>')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","母體藥物 vs 差向異構物", 7,
    "把 7 個分析物分到「母體抗生素」或「差向異構物(4-epimer)」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("方法總覽", "四環素殘留檢驗的<span class='hi'>流程</span>") +
    '<div class="svgwrap" style="margin-top:8px">' + FLOW_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:10px">萃取(McIlvaine+EDTA) → 三氯醋酸沉澱蛋白 → 固相萃取(SPE)淨化 → LC-MS/MS 以 MRM 鑑別定量。</p>')

add(ATT, dc.kt("關鍵難題", "四環素為何<span class='hi'>難萃取</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + CHELATE_SVG + '</div>' +
    '<div class="note" style="margin-top:10px">四環素結構會<strong>螯合金屬離子(Ca、Mg、Fe)</strong>並結合蛋白質，被「困」在基質裡 → 回收率差。' +
    "加入 <strong>EDTA</strong> 競爭螯合金屬，把四環素<strong>釋放出來</strong>，是本法成敗的關鍵。</div>")

add(ATT, dc.kt("萃取設計", "McIlvaine 緩衝液 + <span class='hi'>EDTA</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>McIlvaine 緩衝液</strong>(檸檬酸 + 磷酸氫二鈉)調到 <strong>pH 4</strong>：酸性下四環素穩定、好萃取</li>" +
    "<li>萃取液含 <strong>EDTA-Na₂</strong>：螯合金屬、解開四環素與基質的鍵結</li>" +
    "<li>加<strong>三氯醋酸</strong>沉澱蛋白質，離心去除</li>" +
    "<li>低溫(4°C)離心、12000×g，取上清液</li>" +
    '</ul></div><div class="note"><strong>為什麼 pH 4？</strong><br>' +
    "四環素在中性/鹼性易降解、在強酸易差向異構化；<strong>弱酸(pH 4)</strong>是穩定與萃取的甜蜜點。</div></div>")

add(ATT, dc.kt("淨化", "固相萃取 SPE 去<span class='hi'>基質干擾</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧪","SPE Oasis HLB","萃取液過固相萃取匣，分析物吸附、雜質先洗掉","b") +
    dc.card("💧","沖提與濃縮","以甲醇沖提四環素，加 DMSO 後氮氣吹乾、再復溶","a") +
    dc.card("🎯","為何要淨化","食品基質會抑制/增強離子化(基質效應)，淨化後訊號更乾淨","g") + '</div>' +
    '<p class="subtitle" style="margin-top:12px">萃取(放出來) → 沉澱蛋白(去大分子) → SPE(去小分子雜質) → 乾淨檢液上機。</p>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","四環素方法即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("LC-MS/MS 偵測", "CSH C18 + ESI⁺ + MRM") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>管柱 ACQUITY <strong>CSH C18</strong>(1.7 µm)，管柱溫 40°C；移動相 0.1%甲酸水/乙腈梯度</li>" +
    "<li>游離：<strong>ESI 正離子</strong>(四環素易質子化帶正電)</li>" +
    "<li>偵測：<strong>MRM</strong>，每物監測母離子→子離子(如 TC 445>410、OTC 461>426)</li>" +
    "<li>以<strong>基質匹配檢量線</strong>定量；鑑別靠滯留時間 + 離子比</li>" +
    '</ul></div><div class="note"><strong>為何又是 LC-MS/MS？</strong><br>' +
    "殘留是 <strong>ppb 級痕量</strong>、又是多殘留混合 → 需要 MRM 的高選擇性與靈敏度。</div></div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③", "萃取階段 vs 淨化階段", 6,
    "把 6 個試劑/步驟分到「萃取階段」或「淨化(SPE)階段」。"), ' data-game="g3"')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","四環素殘留檢驗流程排序", 6,
    "用 ▲▼ 把四環素殘留檢驗的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：四環素判斷", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("7 品項四環黴素一覽（點欄位排序）",
    [{"k":"n","t":"s","label":"中文名"},{"k":"en","t":"s","label":"英文名"},{"k":"cls","t":"s","label":"類別"},
     {"k":"q","t":"s","label":"定量離子對"}],
    "離子對整合自 MOHWV0036.06 附表(母離子>定量子離子)。", kicker="附表"), ' data-game="cmp"')

add(ACT, dc.chart_inner("rt", "7 品項的<span class='hi'>滯留時間</span>",
    "LC-MS/MS 參考層析的滯留時間(分)。差向異構物通常比母體更早沖出，CSH C18 可逐一分開。",
    kicker="層析分離", height="52vh"), ' data-chart="rt"')

add(ACT, dc.kt("殘留與抗藥性", "為什麼<span class='hi'>非管不可</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("⏳","停藥期是關鍵","遵守停藥期讓藥代謝到 MRL 以下，是合法上市的前提","b") +
    dc.card("🦠","抗藥性 AMR","長期暴露低劑量抗生素會篩選出超級細菌，難以治療","a") +
    dc.card("🤧","過敏與菌叢","殘留可能引起過敏、擾亂腸道菌叢","g") +
    dc.card("📏","MRL 與 LOQ","各食品有最大殘留限量；本法 LOQ 0.005 ppm(內臟 0.05 ppm)","b") + '</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：殘留含量",
    "某內臟檢體取樣 <b>M = 2 g</b>、最後定容 <b>V = 2 mL</b>；由檢量線得濃度 <b>C = 0.05 µg/mL</b>。"
    "求殘留含量(ppm)。公式：含量 = C×V/M。", unit="ppm"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>MOHWV0036.06：LC-MS/MS 驗畜禽水產/蛋/奶/蜜中 <strong>7 種</strong>四環黴素</li>" +
    "<li>四環素會<strong>螯合金屬、黏蛋白</strong> → 必加 <strong>EDTA</strong> 釋放</li>" +
    "<li>萃取用 <strong>McIlvaine 緩衝液 pH 4</strong> + EDTA + 三氯醋酸沉澱蛋白</li></ul>" +
    '<ul class="clean"><li>SPE(Oasis HLB)淨化 → <strong>CSH C18 / ESI⁺ / MRM</strong></li>' +
    "<li>含量 = C×V/M；LOQ 0.005 ppm(內臟 0.05)；含 3 個差向異構物</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明為什麼要管制食品中四環黴素殘留(停藥期、抗藥性)",
     "說出 7 品項：4 個母體 + 3 個差向異構物",
     "解釋四環素為何難測、EDTA 扮演什麼角色",
     "說明 McIlvaine 緩衝液 pH 4 與三氯醋酸的用途",
     "描述 SPE 淨化的目的(去基質干擾)",
     "說出 LC-MS/MS 用 ESI⁺ 與 MRM 的原因",
     "用 C×V/M 計算殘留含量並對照 MRL/LOQ",
     "解釋什麼是差向異構物、為何也要監測"]))

add(ACT, dc.cover("延伸 · CONNECT",
    "從一顆雞蛋<br><span style='color:var(--accent-2)'>看懂藥物殘留</span>", "",
    "🔗 方法骨幹：<strong>LC-MS/MS + MRM</strong> 同樣用於甜味劑、農藥；本法多了 EDTA 螯合的巧思<br>"
    "🔬 銜接：<strong>質譜 (Ch11)</strong>、<strong>HPLC (Ch13)</strong>、固相萃取、食品安全衛生管理<br>"
    "🧪 思考：為何四環素一定要加 EDTA？差向異構物代表什麼？停藥期沒到就上市會怎樣？",
    ["動物用藥殘留","LC-MS/MS","EDTA 螯合","SPE","抗藥性"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "rt": {"type":"bar","yTitle":"滯留時間 (分)",
      "labels":["4-epi-TC","4-epi-OTC","OTC","TC","4-epi-CTC","CTC","DC"],
      "datasets":[{"label":"滯留時間 (min)","data":[4.59,4.90,5.83,6.12,6.70,8.42,8.88],"color":"#1f6feb"}]}
  },
  "bucket": {
    "g1": {"cats":["母體抗生素","差向異構物 (4-epimer)"],
      "items":[{"t":"四環黴素 Tetracycline (TC)","c":"母體抗生素"},
        {"t":"羥四環黴素/土黴素 Oxytetracycline (OTC)","c":"母體抗生素"},
        {"t":"氯四環黴素/金黴素 Chlortetracycline (CTC)","c":"母體抗生素"},
        {"t":"脫氧羥四環黴素/多西環素 Doxycycline (DC)","c":"母體抗生素"},
        {"t":"4-epimer-tetracycline","c":"差向異構物 (4-epimer)"},
        {"t":"4-epimer-oxytetracycline","c":"差向異構物 (4-epimer)"},
        {"t":"4-epimer-chlortetracycline","c":"差向異構物 (4-epimer)"}],
      "ok":"🎉 全對！TC/OTC/CTC/DC 是母體藥物；3 個 4-epimer 是它們的差向異構物。",
      "tip":"提示：名稱有『4-epimer』的就是差向異構物；其餘四個是母體抗生素。"},
    "g3": {"cats":["萃取階段","淨化(SPE)階段"],
      "items":[{"t":"McIlvaine 緩衝液(pH 4)","c":"萃取階段"},
        {"t":"EDTA-Na₂(螯合金屬、釋放四環素)","c":"萃取階段"},
        {"t":"三氯醋酸(沉澱蛋白質)","c":"萃取階段"},
        {"t":"Oasis HLB 固相萃取匣","c":"淨化(SPE)階段"},
        {"t":"以甲醇沖提分析物","c":"淨化(SPE)階段"},
        {"t":"氮氣吹乾後以 20%甲醇復溶","c":"淨化(SPE)階段"}],
      "ok":"🎉 正確！McIlvaine/EDTA/三氯醋酸屬萃取；HLB匣/沖提/復溶屬 SPE 淨化。",
      "tip":"提示：把藥『放出來』的(緩衝液、EDTA、沉澱蛋白)是萃取；把雜質『去掉』的(HLB、沖提、復溶)是淨化。"}
  },
  "mcq": {
    "g2":[
      {"q":"本方法 MOHWV0036.06 採用的分析儀器是？","o":["氣相層析 GC","液相層析串聯質譜 LC-MS/MS","紫外分光光度計","酸鹼滴定"],"a":1,
       "e":"四環素極性、不揮發、屬痕量多殘留，採 LC-MS/MS、ESI⁺、MRM。"},
      {"q":"萃取時加入 EDTA 的主要目的是？","o":["調色","螯合金屬離子、把四環素從基質釋放出來","當移動相","沉澱蛋白"],"a":1,
       "e":"四環素會螯合 Ca/Mg/Fe 並黏蛋白；EDTA 競爭金屬，提升回收率。"},
      {"q":"萃取用 McIlvaine 緩衝液調到 pH 4 的原因是？","o":["殺菌","弱酸下四環素穩定且好萃取","增加甜味","降低成本"],"a":1,
       "e":"中性/鹼性易降解、強酸易差向異構化；pH 4 是穩定與萃取的折衷。"},
      {"q":"固相萃取(SPE)在此方法的角色是？","o":["游離","淨化去除基質干擾","滴定","加熱"],"a":1,
       "e":"SPE(Oasis HLB)去除基質雜質，降低基質效應、讓訊號乾淨。"},
      {"q":"本法共監測幾個品項？","o":["3","5","7","13"],"a":2,
       "e":"7 品項：四環素/土黴素/金黴素/多西環素 4 母體 + 3 個 4-epimer。"}
    ],
    "g5":[
      {"q":"養殖戶用藥後『沒到停藥期就上市』，最直接的後果是？","o":["沒影響","藥物殘留可能超過 MRL","顏色變深","重量變輕"],"a":1,
       "e":"停藥期是讓藥代謝到 MRL 以下；未到期上市易殘留超標。"},
      {"q":"為什麼四環素殘留分析特別需要 EDTA？","o":["增色","四環素會螯合金屬、黏蛋白，EDTA 幫助釋放","當內標","當緩衝"],"a":1,
       "e":"沒有 EDTA 競爭金屬，四環素被困在基質中，回收率會很差。"},
      {"q":"要同時驗肌肉、內臟、蛋、蜂蜜中多種四環素，最有效率的是？","o":["逐一定性試劑","LC-MS/MS 多殘留 MRM","薄層層析","折射計"],"a":1,
       "e":"LC-MS/MS 以 MRM 一次測多基質、多品項，靈敏且專一。"},
      {"q":"層析圖上比母體更早沖出的小峰，常是？","o":["雜訊","差向異構物(4-epimer)","溶劑","內標"],"a":1,
       "e":"四環素的 4-epimer 極性略不同，通常較母體早沖出，須一併監測。"},
      {"q":"長期食用抗生素殘留食品，公共衛生上最受關注的風險是？","o":["蛀牙","抗藥性(AMR)細菌增加","近視","骨折"],"a":1,
       "e":"低劑量長期暴露會篩選抗藥性細菌，使感染更難治療。"}
    ]
  },
  "sort": {
    "g4":{"steps":["檢體(肌肉/內臟/蛋/乳/蜂蜜)切細均質、精確稱重","加 McIlvaine 緩衝液+EDTA 與三氯醋酸萃取，渦旋振盪",
       "低溫離心,沉澱蛋白、取上清液","上清液過 Oasis HLB 固相萃取匣淨化",
       "甲醇沖提、氮氣吹乾後復溶，過濾供上機","LC-MS/MS 以 ESI⁺ MRM 分析,比對離子對與滯留時間定量"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！均質→McIlvaine-EDTA萃取→離心去蛋白→SPE淨化→沖提復溶→LC-MS/MS。",
       "tip":"提示：先萃取(放出來)、離心去蛋白，再 SPE 淨化、復溶，最後才上 LC-MS/MS。"}
  },
  "calc": {
    "g6":{"answer":0.05,"tol":0.005,
      "ok":"🎉 正確！含量 = C×V/M = 0.05×2/2 = <b>0.05 ppm</b>(恰為內臟 LOQ)。",
      "bad":"再算算：含量 = C×V/M = 0.05×2/2。",
      "hint":"提示：0.05×2 = 0.1；0.1/2 = 0.05 ppm。"}
  },
  "cmp": {
    "cols":[{"k":"n"},{"k":"en"},{"k":"cls"},{"k":"q"}],
    "rows":[
      {"n":"四環黴素","en":"Tetracycline (TC)","cls":"母體","q":"445>410"},
      {"n":"羥四環黴素(土黴素)","en":"Oxytetracycline (OTC)","cls":"母體","q":"461>426"},
      {"n":"氯四環黴素(金黴素)","en":"Chlortetracycline (CTC)","cls":"母體","q":"479>444"},
      {"n":"脫氧羥四環黴素(多西環素)","en":"Doxycycline (DC)","cls":"母體","q":"445>428"},
      {"n":"4-差向四環黴素","en":"4-Epimer-tetracycline","cls":"差向異構物","q":"445>410"},
      {"n":"4-差向土黴素","en":"4-Epimer-oxytetracycline","cls":"差向異構物","q":"461>426"},
      {"n":"4-差向金黴素","en":"4-Epimer-chlortetracycline","cls":"差向異構物","q":"479>462"}
    ]
  }
}

dc.build_html(
  {"title":"食品中四環素殘留檢驗 LC-MS/MS · MOHWV0036.06","brand":"四環素 · MS/MS"},
  S, CFG, OUT)
