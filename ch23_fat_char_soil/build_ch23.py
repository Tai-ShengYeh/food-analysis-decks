# -*- coding: utf-8 -*-
"""Nielsen Ch23 Fat Characterization — SOIL HTML deck. Uses ../soil_deck_common.py.
Run: python build_ch23.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
OXID_SVG = """
<svg viewBox="0 0 980 250">
 <defs><marker id="oa" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="490" y="24" text-anchor="middle" class="lblb" font-size="15">油脂氧化的路徑：初級(氫過氧化物) → 二級(醛酮) → 油耗味</text>
 <g font-size="12.5">
  <rect x="14" y="80" width="150" height="58" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="89" y="104" text-anchor="middle" class="lblb">不飽和油脂</text><text x="89" y="123" text-anchor="middle" class="lbl">+ O₂、光、金屬</text>
  <rect x="214" y="80" width="170" height="58" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="299" y="104" text-anchor="middle" class="lblb">氫過氧化物 LOOH</text><text x="299" y="123" text-anchor="middle" class="lbl">初級產物(無味)</text>
  <rect x="434" y="80" width="190" height="58" rx="10" fill="#fbe7e7" stroke="#d94f4f" stroke-width="2.2"/>
  <text x="529" y="104" text-anchor="middle" class="lblb">醛、酮、烴</text><text x="529" y="123" text-anchor="middle" class="lbl">二級產物(有味)</text>
  <rect x="674" y="84" width="150" height="50" rx="9" fill="#15233f"/>
  <text x="749" y="106" text-anchor="middle" fill="#fff" font-weight="800">油耗味 rancid</text>
  <text x="749" y="124" text-anchor="middle" fill="#cfe0f6" font-size="11">感官可察覺</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#oa)">
  <line x1="164" y1="109" x2="210" y2="109"/><line x1="384" y1="109" x2="430" y2="109"/><line x1="624" y1="109" x2="670" y2="109"/></g>
 <g font-size="11.5" fill="#1f9d6b">
  <text x="299" y="170" text-anchor="middle" class="lblb">↑ 過氧化價 PV、共軛雙烯 CD</text>
  <text x="529" y="170" text-anchor="middle" class="lblb">↑ p-茴香胺價、TBARS、揮發物</text></g>
 <text x="490" y="208" text-anchor="middle" class="lbl">過氧化價會『先升後降』(分解成二級產物)，所以要多種指標一起看</text>
</svg>"""

TAG_SVG = """
<svg viewBox="0 0 620 250">
 <text x="310" y="22" text-anchor="middle" class="lblb" font-size="15">一個三酸甘油酯，三種『值』各看一處</text>
 <!-- glycerol backbone -->
 <line x1="120" y1="70" x2="120" y2="190" stroke="#48597a" stroke-width="3"/>
 <g font-size="13">
  <line x1="120" y1="80" x2="200" y2="80" stroke="#48597a" stroke-width="2.4"/>
  <text x="150" y="74" class="lbl">酯鍵</text>
  <line x1="200" y1="80" x2="430" y2="80" stroke="#d9822b" stroke-width="3"/>
  <!-- one C=C double bond: two parallel lines along the chain, highlighted (what 碘價 counts) -->
  <line x1="290" y1="80" x2="332" y2="80" stroke="#1f6feb" stroke-width="2.8"/>
  <line x1="290" y1="86" x2="332" y2="86" stroke="#1f6feb" stroke-width="2.8"/>
  <text x="360" y="74" text-anchor="middle" class="lbl">脂肪酸鏈(含 C=C 雙鍵)</text>
  <line x1="120" y1="130" x2="430" y2="130" stroke="#d9822b" stroke-width="3"/>
  <line x1="120" y1="180" x2="430" y2="180" stroke="#d9822b" stroke-width="3"/>
 </g>
 <!-- callouts -->
 <rect x="440" y="56" width="170" height="44" rx="8" fill="#eef6ff" stroke="#1f6feb" stroke-width="1.8"/>
 <text x="525" y="74" text-anchor="middle" class="lblb" fill="#1f6feb" font-size="12">碘價 IV</text>
 <text x="525" y="92" text-anchor="middle" class="lbl">數 C=C 雙鍵→不飽和度</text>
 <rect x="440" y="108" width="170" height="44" rx="8" fill="#fff6ea" stroke="#d9822b" stroke-width="1.8"/>
 <text x="525" y="126" text-anchor="middle" class="lblb" fill="#d9822b" font-size="12">皂化價 SV</text>
 <text x="525" y="144" text-anchor="middle" class="lbl">皂化酯鍵→平均鏈長</text>
 <rect x="440" y="160" width="170" height="44" rx="8" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="1.8"/>
 <text x="525" y="178" text-anchor="middle" class="lblb" fill="#1f9d6b" font-size="12">酸價 AV / FFA</text>
 <text x="525" y="196" text-anchor="middle" class="lbl">水解游離的脂肪酸</text>
 <text x="120" y="214" text-anchor="middle" class="lbl">甘油</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 23",
    "油脂<span style='color:var(--accent-2)'>特性</span>分析", "Fat Characterization",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>碘價 · 皂化價 · 酸價 · 過氧化價 · 氧化安定性 · 脂肪酸組成",
    ["碘價=不飽和度","皂化價=鏈長","過氧化價=氧化","發煙點","OSI/Rancimat"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">一瓶油<span class="hi">壞了沒</span>？是橄欖油還是混了便宜油？<br>飽和還是不飽和？——怎麼用幾個<span class="hi">數字</span>說清楚？</div>
  <p class="subtitle" style="max-width:850px;margin:22px auto 0">油脂的『特性分析』就是一組數字：<strong>碘價、皂化價、酸價、過氧化價</strong>…<br>
  分別告訴你它的<strong>不飽和度、鏈長、水解與氧化劣化</strong>，攸關品質、保存與營養標示。</p>
  <div style="margin-top:24px"><span class="pill">鑑別與摻假</span><span class="pill">新鮮度/油耗</span>
  <span class="pill">飽和/trans 標示</span><span class="pill">保存期</span></div></div>""")

add(MOT, dc.kt("23.2.2 劣化三路", "油脂會怎麼<span class='hi'>變壞</span>") +
    '<div class="grid3" style="margin-top:18px">' +
    dc.card("💧","水解 Lipolysis","酯鍵被水解 → 游離脂肪酸(FFA)；短鏈 FFA 造成『水解酸敗』(乳品奶味)","b") +
    dc.card("🔥","氧化 Oxidation","O₂ 攻擊不飽和鍵 → 氫過氧化物 → 醛酮 → <strong>油耗味</strong>(最主要的劣化)","a") +
    dc.card("🍳","聚合 Polymerization","高溫油炸使分子聚合 → 黏度上升、總極性物增加","g") + '</div>' +
    '<p class="subtitle" style="margin-top:14px">不同劣化用不同『值』來測：FFA/酸價測水解、過氧化價等測氧化。</p>')

add(MOT, dc.kt("23.2.2.2 氧化路徑", "從<span class='hi'>無味</span>到<span class='hi'>油耗</span>") +
    '<div class="svgwrap" style="margin-top:4px">' + OXID_SVG + '</div>')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","物理特性 vs 化學特性", 8,
    "把 8 個檢驗項目分到「物理特性」或「化學特性」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("一圖看四值", "每個『值』各看<span class='hi'>一處</span>") +
    '<div class="svgwrap" style="margin-top:4px">' + TAG_SVG + '</div>' +
    '<div class="note" style="margin-top:8px"><strong>碘價</strong>數雙鍵(不飽和度)、<strong>皂化價</strong>皂化酯鍵(平均鏈長)、' +
    "<strong>酸價/FFA</strong>看水解出的游離脂肪酸、<strong>過氧化價</strong>看氧化生成的氫過氧化物。</div>")

add(ATT, dc.kt("23.4.1 / 23.4.2", "碘價與皂化價") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🟣","碘價 IV","每 100 g 油吸收的碘克數 → <strong>不飽和度</strong>。ICl 加成雙鍵，剩餘碘以硫代硫酸鈉/澱粉滴定。越不飽和、碘價越高","a") +
    dc.card("🧼","皂化價 SV","皂化 1 g 油所需 KOH 的毫克數 → <strong>平均分子量/鏈長</strong>。KOH 皂化後回滴。皂化價越小、鏈越長","b") +
    '</div><div class="note" style="margin-top:14px">兩者都可由<strong>脂肪酸組成計算</strong>(計算碘價/計算皂化價)，一次分析得兩個結果。</div>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","油脂特性即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("23.4.3 / 23.4.5", "酸價與過氧化價") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧪","酸價 AV / FFA","中和 1 g 油中游離脂肪酸所需 KOH mg → <strong>水解酸敗</strong>程度。油炸油常設 AV ≤ 2 mg KOH/g","b") +
    dc.card("🫧","過氧化價 PV","每 kg 油的氫過氧化物毫當量 → <strong>初級氧化</strong>。KI 還原 ROOH 生碘,以硫代硫酸鈉滴定。PV>20 品質很差","a") +
    '</div><div class="note" style="margin-top:14px"><strong>二級氧化</strong>指標：p-茴香胺價(醛,350nm)、TBARS(丙二醛,530nm)、共軛雙烯(232nm)、揮發物(hexanal)。' +
    "<strong>Totox = p-茴香胺價 + 2×過氧化價</strong>。</div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","各『值』測什麼", 6,
    "把 6 個檢驗值分到「測不飽和度」「測鏈長/水解」或「測氧化」。"), ' data-game="g3"')

add(ATT, dc.kt("23.3 物理特性", "不用試劑也能<span class='hi'>看出</span>很多") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🔬","折射率 RI","隨不飽和度上升;可鑑別與測純度","b") +
    dc.card("🌡️","熔點","毛細管/滑動/滴落熔點;反映固體脂與組成","a") +
    dc.card("💨","發煙點","開始冒煙的溫度;<strong>FFA 越高、發煙點越低</strong>","g") +
    dc.card("🧈","固體脂含量 SFC","以脈衝 NMR 測固/液脂比例(連回 Ch10);決定塗抹性與口感","b") + '</div>')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","碘價滴定流程排序", 6,
    "用 ▲▼ 把碘價測定的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("23.5 氧化安定性", "預測油『撐得多久』") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>誘導期</strong>：抗氧化劑耗盡前氧化緩慢的時間,越長越安定</li>" +
    "<li><strong>OSI(油脂安定指數)</strong>：在 110/130°C 通空氣,測揮發酸使導電度急升的時間(<strong>Rancimat</strong>)</li>" +
    "<li><strong>氧消耗試驗</strong>(Oxipres/Oxitest):密閉測壓力下降,可用整顆食品</li>" +
    "<li>加速試驗快,但高溫路徑未必等於常溫,須對照真實貨架</li>" +
    '</ul></div><div class="note"><strong>用途：</strong>比較配方、抗氧化劑效果、包裝與儲存對保存期的影響。</div></div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對檢驗", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("油脂檢驗『值』一覽（點欄位排序）",
    [{"k":"v","t":"s","label":"檢驗值"},{"k":"t","t":"s","label":"測量目標"},
     {"k":"p","t":"s","label":"原理"},{"k":"m","t":"s","label":"數值意義"}],
    "整合自 Table 23.3。", kicker="Table 23.3"), ' data-game="cmp"')

add(ACT, dc.chart_inner("iodine", "不同油脂的<span class='hi'>碘價</span>",
    "整合自 Table 23.2:碘價反映不飽和度。椰子油最飽和(碘價低)、魚油最不飽和(碘價高)。",
    kicker="23.4.1 數據", height="52vh"), ' data-chart="iodine"')

add(ACT, dc.kt("23.6 脂肪酸組成", "標示與健康的<span class='hi'>核心</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧬","脂肪酸 FAMEs","油脂轉成脂肪酸甲酯,以 <strong>GC</strong> 分離定量 → 飽和/不飽和/各脂肪酸%","b") +
    dc.card("↩️","反式脂肪 trans","以 <strong>IR 966 cm⁻¹</strong> 或 GC 測;營養標示必填","a") +
    dc.card("🧀","膽固醇/植物固醇","皂化後 TMS 衍生,以 GC 定量(營養標示)","g") +
    dc.card("📊","發煙點 vs FFA","FFA 上升使發煙點下降,油炸油劣化的指標(見下頁圖)","b") + '</div>')

add(ACT, dc.chart_inner("smoke", "FFA 越高，<span class='hi'>發煙點</span>越低",
    "整合自 Fig 23.4(橄欖油):游離脂肪酸含量上升,發煙點明顯下降 → 油炸油劣化的警訊。",
    kicker="23.3.3 數據", height="46vh"), ' data-chart="smoke"')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：過氧化價",
    "過氧化價滴定：檢液用 <b>S = 2.0 mL</b>、空白 <b>B = 0.1 mL</b> 之 <b>0.01 N</b> 硫代硫酸鈉；取樣 <b>W = 5 g</b>。"
    "求過氧化價(meq/kg)。公式：(S−B)×N/W×1000。", unit="meq/kg"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>油脂劣化三路：<strong>水解、氧化、聚合</strong>;氧化最關鍵</li>" +
    "<li><strong>碘價</strong>=不飽和度、<strong>皂化價</strong>=平均鏈長</li>" +
    "<li><strong>酸價/FFA</strong>=水解、<strong>過氧化價</strong>=初級氧化(會先升後降)</li></ul>" +
    '<ul class="clean"><li>二級氧化:p-茴香胺價、TBARS;<strong>Totox=p-AV+2PV</strong></li>' +
    "<li>安定性用 <strong>OSI(Rancimat)</strong>;脂肪酸/trans 用 GC、IR</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說出油脂劣化的三條路徑與各自的檢驗",
     "解釋碘價測不飽和度、皂化價測平均鏈長的原理",
     "區分酸價(水解)與過氧化價(初級氧化)",
     "說明為何過氧化價會先升後降、要搭配二級指標",
     "舉出物理特性(折射率/熔點/發煙點/SFC)各反映什麼",
     "說明 OSI/Rancimat 如何評估氧化安定性",
     "用 (S−B)×N/W×1000 計算過氧化價",
     "說出脂肪酸組成、trans、膽固醇的分析方法"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把油脂特性<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions(碘價/皂化價/過氧化價計算、Totox、OSI)<br>"
    "🔜 銜接：<strong>油脂分析 (Ch17)</strong>、<strong>NMR/SFC (Ch10)</strong>、<strong>GC (Ch14)</strong>、<strong>紅外 (Ch8)</strong><br>"
    "🧪 思考：你要知道油的『不飽和度、鏈長、還是新鮮度』?該選哪個值?要不要看二級氧化?",
    ["碘價","皂化價","過氧化價","OSI","脂肪酸/trans"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "iodine": {"type":"bar","yTitle":"碘價 (g I₂ / 100 g)",
      "labels":["椰子油","棕櫚油","豬脂","橄欖油","玉米油","大豆油","紅花油","魚油"],
      "datasets":[{"label":"碘價","data":[9,50,60,85,121,128,145,175],"color":"#d9822b"}]},
    "smoke": {"type":"line","yTitle":"發煙點 (°C)","zero":False,
      "labels":["0.05","0.1","0.2","0.4","0.6","0.8","1.0"],
      "datasets":[{"label":"發煙點(橄欖油)","data":[218,205,195,177,170,165,160],"color":"#1f6feb"}]}
  },
  "bucket": {
    "g1": {"cats":["物理特性","化學特性"],
      "items":[{"t":"折射率 (RI)","c":"物理特性"},{"t":"熔點","c":"物理特性"},
        {"t":"發煙點","c":"物理特性"},{"t":"固體脂含量 (SFC)","c":"物理特性"},
        {"t":"碘價 (IV)","c":"化學特性"},{"t":"皂化價 (SV)","c":"化學特性"},
        {"t":"過氧化價 (PV)","c":"化學特性"},{"t":"TBARS (丙二醛)","c":"化學特性"}],
      "ok":"🎉 全對！折射率/熔點/發煙點/SFC 是物理量;碘價/皂化價/過氧化價/TBARS 是化學量。",
      "tip":"提示：用儀器量『物理量』(溫度、折射、固液比)→物理;用反應/滴定/呈色→化學。"},
    "g3": {"cats":["測不飽和度","測鏈長/水解","測氧化"],
      "items":[{"t":"碘價(碘加成雙鍵)","c":"測不飽和度"},{"t":"共軛雙烯(UV 232 nm)","c":"測不飽和度"},
        {"t":"皂化價(平均分子量/鏈長)","c":"測鏈長/水解"},{"t":"酸價/FFA(水解出的游離脂肪酸)","c":"測鏈長/水解"},
        {"t":"過氧化價(初級·氫過氧化物)","c":"測氧化"},{"t":"TBARS(二級·丙二醛)","c":"測氧化"}],
      "ok":"🎉 正確！碘價/CD 看雙鍵;皂化價/酸價看鏈長與水解;過氧化價/TBARS 看氧化。",
      "tip":"提示：跟『雙鍵』有關→不飽和度;跟『酯鍵/水解』→鏈長水解;跟『氫過氧化物/醛』→氧化。"}
  },
  "mcq": {
    "g2":[
      {"q":"碘價(IV)反映油脂的什麼？","o":["鏈長","不飽和度(雙鍵多寡)","酸度","水分"],"a":1,
       "e":"碘加成到 C=C 雙鍵;碘價越高代表越不飽和。"},
      {"q":"皂化價(SV)越小，代表脂肪酸鏈？","o":["越短","越長","越多雙鍵","越氧化"],"a":1,
       "e":"皂化價反映平均分子量;值越小代表平均鏈越長。"},
      {"q":"酸價(AV)/游離脂肪酸(FFA)主要反映哪種劣化？","o":["氧化","水解酸敗","聚合","結晶"],"a":1,
       "e":"FFA 由酯鍵水解而來,酸價反映水解酸敗程度。"},
      {"q":"過氧化價(PV)測的是？","o":["二級醛類","初級氫過氧化物","雙鍵","游離脂肪酸"],"a":1,
       "e":"PV 以碘滴定測氫過氧化物,是初級氧化指標。"},
      {"q":"為什麼不能只靠過氧化價判斷油有沒有壞？","o":["太貴","氫過氧化物會分解,PV 先升後降","不準","太慢"],"a":1,
       "e":"PV 先升後降;須搭配 p-茴香胺價、TBARS 等二級指標。"}
    ],
    "g5":[
      {"q":"想知道一瓶油『有多不飽和』(會不會易氧化)，測？","o":["酸價","碘價","水分","顏色"],"a":1,
       "e":"碘價反映不飽和度;越不飽和越易氧化。"},
      {"q":"油炸油用久了想評估新鮮度，最常測？","o":["碘價","酸價/FFA 與總極性物","折射率","熔點"],"a":1,
       "e":"油炸劣化主要看 FFA/酸價、總極性物與聚合物。"},
      {"q":"要比較兩種抗氧化劑哪個讓油更耐放，用？","o":["皂化價","OSI/Rancimat 測誘導期","碘價","顏色"],"a":1,
       "e":"OSI(Rancimat)測誘導期,誘導期越長越安定。"},
      {"q":"要算油脂的總氧化程度(初級+二級)，用？","o":["只看 PV","Totox = p-茴香胺價 + 2×過氧化價","只看碘價","只看酸價"],"a":1,
       "e":"Totox 結合初級(PV)與二級(p-AV)指標反映總氧化。"},
      {"q":"要做反式脂肪營養標示,常用的快速光譜法是？","o":["UV 280","紅外 966 cm⁻¹","螢光","折射率"],"a":1,
       "e":"反式雙鍵在 IR 966 cm⁻¹ 有吸收,可定 trans 含量。"}
    ]
  },
  "sort": {
    "g4":{"steps":["精秤油樣,溶於適當溶劑","加入過量 ICl,於暗處靜置使加成到雙鍵",
       "加碘化鉀,使剩餘 ICl 轉成游離碘","以標準硫代硫酸鈉滴定游離碘(黃色將褪時加澱粉)",
       "繼續滴定至藍色消失為終點(另做空白)","以 (B−S)×N×126.9/(W×1000)×100 算碘價"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！秤樣溶解→加 ICl 暗反應→加 KI 釋碘→硫代硫酸鈉滴定→終點→計算。",
       "tip":"提示：先讓碘加成雙鍵,再把剩餘 ICl 變游離碘來滴定;藍色消失為終點。"}
  },
  "calc": {
    "g6":{"answer":3.8,"tol":0.2,
      "ok":"🎉 正確！PV = (S−B)×N/W×1000 = (2.0−0.1)×0.01/5×1000 = 0.019/5×1000 = <b>3.8 meq/kg</b>。",
      "bad":"再算算：PV = (S−B)×N/W×1000 = (2.0−0.1)×0.01/5×1000。",
      "hint":"提示：(2.0−0.1)=1.9;1.9×0.01=0.019;0.019/5×1000 = 3.8 meq/kg。"}
  },
  "cmp": {
    "cols":[{"k":"v"},{"k":"t"},{"k":"p"},{"k":"m"}],
    "rows":[
      {"v":"碘價 IV","t":"不飽和度","p":"碘加成雙鍵","m":"越高越不飽和"},
      {"v":"皂化價 SV","t":"平均鏈長","p":"皂化所需 KOH","m":"越小鏈越長"},
      {"v":"酸價 AV/FFA","t":"水解程度","p":"中和游離脂肪酸","m":"越高水解酸敗越多"},
      {"v":"過氧化價 PV","t":"初級氧化","p":"碘滴定氫過氧化物","m":"越高初級氧化越多(會先升後降)"},
      {"v":"p-茴香胺價","t":"二級氧化","p":"醛類呈色 350 nm","m":"與 PV 合算 Totox"},
      {"v":"TBARS","t":"二級氧化","p":"丙二醛呈色 530 nm","m":"越高油耗越嚴重"}
    ]
  }
}

dc.build_html(
  {"title":"油脂特性分析 Fat Characterization · Nielsen Ch23","brand":"油脂特性 · CH23"},
  S, CFG, OUT)
