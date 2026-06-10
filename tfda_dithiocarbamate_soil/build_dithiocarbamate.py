# -*- coding: utf-8 -*-
"""TFDA MOHWP0054.04 食品中殘留農藥檢驗方法－殺菌劑二硫代胺基甲酸鹽類(二) — SOIL HTML deck.
Source: 衛福部食藥署 MOHWP0054.04 (頂空 GC-FPD, 共同產物 CS2). Run: python build_dithiocarbamate.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
CLEAVE_SVG = """
<svg viewBox="0 0 980 220">
 <defs><marker id="ca" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#48597a"/></marker></defs>
 <text x="490" y="24" text-anchor="middle" class="lblb" font-size="15">共同產物法：把各種二硫代胺基甲酸鹽『裂解』成共同的 CS₂ 來測</text>
 <g font-size="12.5">
  <rect x="14" y="78" width="190" height="62" rx="10" fill="#f6f9fd" stroke="#48597a" stroke-width="2.2"/>
  <text x="109" y="100" text-anchor="middle" class="lblb">二硫代胺基甲酸鹽</text><text x="109" y="118" text-anchor="middle" class="lbl">mancozeb/maneb…種類多</text>
  <rect x="254" y="78" width="170" height="62" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.2"/>
  <text x="339" y="100" text-anchor="middle" class="lblb">酸 + 氯化亞錫</text><text x="339" y="118" text-anchor="middle" class="lbl">加熱裂解</text>
  <rect x="474" y="78" width="150" height="62" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="549" y="100" text-anchor="middle" class="lblb">CS₂ 氣體</text><text x="549" y="118" text-anchor="middle" class="lbl">跑到頂空</text>
  <rect x="674" y="78" width="150" height="62" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.2"/>
  <text x="749" y="100" text-anchor="middle" class="lblb">GC 分離</text><text x="749" y="118" text-anchor="middle" class="lbl">Porpak Q 柱</text>
  <rect x="874" y="82" width="96" height="54" rx="9" fill="#15233f"/>
  <text x="922" y="104" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">FPD</text>
  <text x="922" y="122" text-anchor="middle" fill="#cfe0f6" font-size="10">硫選擇偵測</text>
 </g>
 <g stroke="#48597a" stroke-width="2.4" marker-end="url(#ca)">
  <line x1="204" y1="109" x2="250" y2="109"/><line x1="424" y1="109" x2="470" y2="109"/>
  <line x1="624" y1="109" x2="670" y2="109"/><line x1="824" y1="109" x2="870" y2="109"/></g>
 <text x="490" y="184" text-anchor="middle" class="lbl">一個共同產物 CS₂ → 一次測『總二硫代胺基甲酸鹽』，以 CS₂ 計</text>
</svg>"""

FPD_SVG = """
<svg viewBox="0 0 560 230">
 <text x="280" y="22" text-anchor="middle" class="lblb" font-size="15">火焰光度檢出器 FPD：只對『含硫』化合物發亮</text>
 <!-- flame -->
 <path d="M150 170 C120 120, 180 110, 150 60 C175 110, 200 130, 150 170 Z" fill="#9ad0ff" opacity=".7" stroke="#1f6feb" stroke-width="1.5"/>
 <text x="150" y="195" text-anchor="middle" class="lbl">氫火焰</text>
 <line x1="150" y1="200" x2="150" y2="180" stroke="#1f9d6b" stroke-width="3"/>
 <text x="150" y="216" text-anchor="middle" class="lbl">含 S 樣品進入</text>
 <!-- emission -->
 <g stroke="#7c3aed" stroke-width="2" opacity=".8">
  <line x1="165" y1="90" x2="230" y2="80"/><line x1="165" y1="100" x2="230" y2="100"/><line x1="165" y1="110" x2="230" y2="120"/></g>
 <text x="195" y="54" text-anchor="middle" class="lbl">硫受激發、放出特定波長光</text>
 <!-- filter -->
 <rect x="300" y="72" width="40" height="56" rx="4" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
 <text x="320" y="150" text-anchor="middle" class="lblb" fill="#d9822b" font-size="12">325 nm</text>
 <text x="320" y="166" text-anchor="middle" class="lbl">硫濾光鏡</text>
 <!-- detector -->
 <line x1="340" y1="100" x2="420" y2="100" stroke="#48597a" stroke-width="2" marker-end="url(#ca)"/>
 <rect x="430" y="76" width="110" height="48" rx="8" fill="#15233f"/>
 <text x="485" y="98" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">光電倍增管</text>
 <text x="485" y="116" text-anchor="middle" fill="#cfe0f6" font-size="11">只記錄硫的訊號</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("食藥署公告檢驗方法 · MOHWP0054.04",
    "二硫代胺基甲酸鹽<span style='color:var(--accent-2)'>殺菌劑</span>", "Dithiocarbamates (Fungicide)",
    "食品安全檢測　·　3 小時課程　·　含 6 個互動小遊戲<br>共同產物 CS₂ · 頂空進樣 · GC-FPD · 硫選擇偵測 · 假陽性確認",
    ["蔬果常見殺菌劑","裂解成 CS₂","頂空 GC-FPD","硫選擇 325nm","十字花科假陽性"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">高麗菜、葡萄上的<span class="hi">殺菌劑殘留</span>，<br>種類那麼多、結構又不穩，怎麼一次驗？</div>
  <p class="subtitle" style="max-width:850px;margin:22px auto 0">二硫代胺基甲酸鹽類(mancozeb、maneb…)是廣用殺菌劑,個別分子難測。<br>
  巧招是:把它們<strong>全部裂解成共同產物『二硫化碳 CS₂』</strong>,再用<strong>頂空 GC-FPD</strong>一次測總量。</p>
  <div style="margin-top:24px"><span class="pill">廣用殺菌劑</span><span class="pill">共同產物法</span>
  <span class="pill">CS₂</span><span class="pill">硫選擇偵測</span></div></div>""")

add(MOT, dc.kt("背景", "為什麼用<span class='hi'>共同產物</span>法") +
    '<div class="grid2" style="margin-top:20px">' +
    dc.card("🍇","廣用殺菌劑","二硫代胺基甲酸鹽(mancozeb 等)用於蔬果防黴;非系統性、多留在表面","b") +
    dc.card("🧩","種類多又不穩","各種結構不同、難個別定量;但都含相同官能基","a") +
    dc.card("🔑","共同點 = CS₂","酸性下加熱會『裂解』放出共同產物<strong>二硫化碳(CS₂)</strong>","g") +
    dc.card("🎯","策略","測 CS₂ 就等於測『總二硫代胺基甲酸鹽』,以 CS₂ 計","b") + '</div>')

add(MOT, dc.kt("方法核心", "裂解 → 頂空 → <span class='hi'>GC-FPD</span>") +
    '<div class="svgwrap" style="margin-top:4px">' + CLEAVE_SVG + '</div>')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","共同產物法 vs 個別分析法", 8,
    "把 8 個敘述分到「共同產物法(本法)」或「個別分析法(如 LC-MS/MS)」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("裂解設計", "酸 + <span class='hi'>氯化亞錫</span>放出 CS₂") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>反應試劑</strong>:鹽酸 + 氯化亞錫(SnCl₂)——酸化裂解,SnCl₂ 當還原劑減少干擾</li>" +
    "<li>切碎檢體加反應試劑、封入<strong>頂空分析瓶</strong></li>" +
    "<li><strong>加熱 80°C、120 分鐘</strong>,讓 CS₂ 充分釋出到上部空間</li>" +
    "<li>取樣針 85°C、取 <strong>1 mL 頂空氣體</strong>注入 GC</li>" +
    '</ul></div><div class="note"><strong>為何用頂空？</strong><br>' +
    "CS₂ 易揮發,只取上部氣體即可,把不揮發的蔬果基質留在瓶裡、不汙染管柱。</div></div>")

add(ATT, dc.kt("FPD 偵測", "只對<span class='hi'>含硫</span>化合物發亮") +
    '<div class="svgwrap" style="margin-top:4px">' + FPD_SVG + '</div>' +
    '<div class="note" style="margin-top:8px"><strong>高選擇性</strong>讓 FPD 在複雜基質中專挑含硫的 CS₂;但 FPD 對硫的反應<strong>非線性</strong>，標準曲線須取波峰面積的<strong>『根號值』</strong>才線性。</div>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","CS₂ 法即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("標準曲線的玄機", "面積取<span class='hi'>根號</span>才線性") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>FPD 對硫的反應是非線性</strong>(約與含硫量平方相關)</li>" +
    "<li>所以標準曲線用<strong>波峰面積的『根號值』</strong>對 CS₂ 量作圖,才呈線性</li>" +
    "<li>以 CS₂ 標準品配 <strong>0.2–5 µg</strong> 製作標準曲線</li>" +
    "<li>層析:Porpak Q 柱、140°C、注入器 180°C、檢出器 300°C</li>" +
    '</ul></div><div class="note"><strong>記住:</strong>FPD 高選擇但『非線性』;<br>' +
    "用面積『根號值』線性化是這個方法的招牌細節。</div></div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","試劑/裝置角色", 8,
    "把 8 個項目分到「釋出 CS₂」或「偵測 CS₂」。"), ' data-game="g3"')

add(ATT, dc.kt("假陽性陷阱", "十字花科與<span class='hi'>蔥蒜</span>的麻煩") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>蒜、洋蔥、韭菜、青蔥、青椒、十字花科等含<strong>內生性硫化物</strong></li>" +
    "<li>這些天然硫化物在裂解條件下也會<strong>產生 CS₂</strong> → 假陽性</li>" +
    "<li>檢出時須做<strong>清洗試驗</strong>確認:1 份以自來水流洗 10 分鐘瀝乾、另 1 份不洗</li>" +
    "<li>比較兩者 CS₂:清洗前後<strong>無明顯差異</strong>→視為未檢出(因農藥可被洗掉、內生硫化物洗不掉)</li>" +
    '</ul></div><div class="note"><strong>原理:</strong>二硫代胺基甲酸鹽是非系統性、留表面,易被水洗除;<br>' +
    "內生性硫化物在組織內,洗不掉。用『洗得掉與否』來區分。</div></div>")

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","CS₂ 頂空 GC-FPD 流程排序", 6,
    "用 ▲▼ 把二硫代胺基甲酸鹽檢驗的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：判讀與確認", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("二硫代胺基甲酸鹽的幾種檢驗法（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"spec","t":"n","label":"專一性","star":True},
     {"k":"d","t":"s","label":"偵測對象"},{"k":"f","t":"s","label":"特點"}],
    "★ 越多越能分辨個別農藥。本法為頂空 GC-FPD 共同產物法。", kicker="方法比較"), ' data-game="cmp"')

add(ACT, dc.chart_inner("curve", "FPD 標準曲線：面積<span class='hi'>根號值</span>線性",
    "示意:CS₂ 量(µg)對波峰面積的『根號值』呈良好線性(FPD 對硫非線性,取根號才線性化)。",
    kicker="定量基礎", height="50vh"), ' data-chart="curve"')

add(ACT, dc.kt("意義與限制", "共同產物法的<span class='hi'>得與失</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("✅","優點","一次測『總量』、快速、FPD 硫選擇性高、適合大量篩檢","b") +
    dc.card("⚠️","限制","無法分辨是哪一種二硫代胺基甲酸鹽;含硫蔬菜有假陽性","a") +
    dc.card("🚿","確認","可疑樣品做清洗試驗,或結合源頭稽查綜合判定","g") +
    dc.card("🥗","食安","殺菌劑殘留攸關健康;此法是蔬果殘留監測的實用工具","b") + '</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：殘留含量",
    "頂空 GC-FPD：取樣 <b>M = 2 g</b>;由標準曲線得檢液中 CS₂ 量 <b>C = 3.0 µg</b>。"
    "求殘留含量(ppm,以 CS₂ 計)。公式:C/M。", unit="ppm"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>二硫代胺基甲酸鹽種類多 → <strong>共同產物法</strong>:全部裂解成 CS₂</li>" +
    "<li>裂解:<strong>鹽酸 + 氯化亞錫</strong>、加熱 80°C 釋出 CS₂ 到頂空</li>" +
    "<li>偵測:<strong>GC-FPD</strong>(火焰光度+325nm 硫濾光鏡),硫選擇性高</li></ul>" +
    '<ul class="clean"><li>FPD 非線性 → 標準曲線取面積<strong>根號值</strong></li>' +
    "<li>含硫蔬菜<strong>假陽性</strong> → 清洗試驗確認;含量 = C/M,以 CS₂ 計,LOQ 0.1 ppm</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明為何用『共同產物 CS₂』法測二硫代胺基甲酸鹽",
     "說出鹽酸與氯化亞錫在裂解中的角色",
     "解釋頂空進樣與 FPD 硫選擇偵測的原理",
     "說明為何 FPD 標準曲線要取面積的根號值",
     "解釋十字花科/蔥蒜為何造成假陽性、如何做清洗試驗確認",
     "依序排出 CS₂ 頂空 GC-FPD 的檢驗流程",
     "用 C/M 計算殘留含量(以 CS₂ 計)",
     "說出共同產物法的優點與限制"]))

add(ACT, dc.cover("延伸 · CONNECT",
    "從一顆高麗菜<br><span style='color:var(--accent-2)'>看懂共同產物法</span>", "",
    "🔗 對照:本法測『共同產物』、多重殘留法(六)用 LC-MS/MS 測『個別農藥』<br>"
    "🔬 銜接:<strong>氣相層析 (Ch14)</strong>、頂空進樣、選擇性檢出器(FPD)、食品安全管理<br>"
    "🧪 思考:為何含硫蔬菜會假陽性?清洗試驗的邏輯是什麼?FPD 為何要取根號?",
    ["共同產物 CS₂","頂空 GC-FPD","硫選擇","假陽性確認","食安檢測"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "curve": {"type":"line","yTitle":"波峰面積之根號值 (示意)",
      "labels":["0.2","1","2","3","5"],
      "datasets":[{"label":"√面積","data":[20,100,200,300,500],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["共同產物法(本法)","個別分析法(如 LC-MS/MS)"],
      "items":[{"t":"把全部裂解成 CS₂ 再測","c":"共同產物法(本法)"},
        {"t":"測『總二硫代胺基甲酸鹽』(以 CS₂ 計)","c":"共同產物法(本法)"},
        {"t":"用 GC-FPD 硫選擇偵測","c":"共同產物法(本法)"},
        {"t":"快速、適合大量篩檢但無法分辨品項","c":"共同產物法(本法)"},
        {"t":"直接測每一種農藥分子","c":"個別分析法(如 LC-MS/MS)"},
        {"t":"可分辨是哪一種農藥","c":"個別分析法(如 LC-MS/MS)"},
        {"t":"以質譜 m/z 專一鑑別","c":"個別分析法(如 LC-MS/MS)"},
        {"t":"前處理與分析較複雜","c":"個別分析法(如 LC-MS/MS)"}],
      "ok":"🎉 全對！共同產物法測總量(CS₂)、快但不分品項;個別法測每種分子、可分辨但較複雜。",
      "tip":"提示:跟『裂解成CS₂、總量、GC-FPD』有關→共同產物法;跟『個別分子、m/z、可分品項』→個別法。"},
    "g3": {"cats":["釋出 CS₂","偵測 CS₂"],
      "items":[{"t":"鹽酸(酸化裂解)","c":"釋出 CS₂"},{"t":"氯化亞錫(還原)","c":"釋出 CS₂"},
        {"t":"加熱 80°C 120 分鐘","c":"釋出 CS₂"},{"t":"頂空進樣取上部氣體","c":"釋出 CS₂"},
        {"t":"FPD 火焰光度檢出器","c":"偵測 CS₂"},{"t":"325 nm 硫選擇濾光鏡","c":"偵測 CS₂"},
        {"t":"Porpak Q 毛細管柱分離","c":"偵測 CS₂"},{"t":"CS₂ 對照標準品","c":"偵測 CS₂"}],
      "ok":"🎉 正確！酸/氯化亞錫/加熱/頂空把 CS₂ 放出來;FPD/濾光鏡/柱/標準品負責偵測定量。",
      "tip":"提示:跟『酸、還原、加熱、頂空』有關→釋出;跟『FPD、濾光鏡、柱、標準品』→偵測。"}
  },
  "mcq": {
    "g2":[
      {"q":"本法(MOHWP0054)測二硫代胺基甲酸鹽的策略是？","o":["直接測每種農藥","裂解成共同產物 CS₂ 再測","測顏色","測 pH"],"a":1,
       "e":"各種二硫代胺基甲酸鹽裂解後都產生 CS₂,測 CS₂ 即測總量。"},
      {"q":"裂解反應試劑是鹽酸加上什麼？","o":["氫氧化鈉","氯化亞錫(SnCl₂)","過氧化氫","乙醇"],"a":1,
       "e":"以鹽酸酸化裂解、氯化亞錫當還原劑減少干擾。"},
      {"q":"FPD(火焰光度檢出器)的特點是？","o":["測所有有機物","只對含硫(或磷)化合物高選擇","測顏色","測質量"],"a":1,
       "e":"FPD 搭配 325 nm 硫濾光鏡,對含硫化合物高選擇。"},
      {"q":"為什麼標準曲線要用波峰面積的『根號值』？","o":["比較快","FPD 對硫的反應呈非線性,取根號才線性","省試劑","增加靈敏"],"a":1,
       "e":"FPD 硫反應約與含量平方相關,面積取根號可線性化。"},
      {"q":"本法的定量極限(LOQ)為？","o":["0.001 ppm","0.1 ppm","1 ppm","10 ppm"],"a":1,
       "e":"本檢驗方法之定量極限為 0.1 ppm(以 CS₂ 計)。"}
    ],
    "g5":[
      {"q":"高麗菜檢出 CS₂,但它是十字花科,該怎麼辦？","o":["直接判陽性","做清洗試驗確認(可能是內生硫化物)","重測一次","加更多試劑"],"a":1,
       "e":"含硫蔬菜會假陽性,須做清洗試驗區分農藥與內生硫化物。"},
      {"q":"清洗試驗:清洗前後 CS₂ 無明顯差異,代表？","o":["農藥很多","視為未檢出(內生硫化物洗不掉)","儀器壞了","要加倍取樣"],"a":1,
       "e":"農藥在表面可洗除;若洗前後無差異,訊號多來自洗不掉的內生硫化物。"},
      {"q":"想知道檢出的是哪一種二硫代胺基甲酸鹽,本法可以嗎？","o":["可以,看 CS₂ 就知道","不行,本法只測總量,需個別分析法","可以,看顏色","可以,看 pH"],"a":1,
       "e":"共同產物法只能測總量;要分辨品項須用個別分析(如 LC-MS/MS)。"},
      {"q":"為何用頂空只取上部氣體？","o":["比較香","CS₂ 易揮發、取氣相可避免基質汙染管柱","省時間","增加顏色"],"a":1,
       "e":"頂空只引入揮發的 CS₂,把蔬果基質留在瓶裡保護儀器。"},
      {"q":"二硫代胺基甲酸鹽屬非系統性殺菌劑,代表它？","o":["會進入植物全身","多留在表面、較易被水洗除","不能用","只在根部"],"a":1,
       "e":"非系統性=留在表面,故易水洗;這正是清洗試驗的依據。"}
    ]
  },
  "sort": {
    "g4":{"steps":["切碎檢體精秤,置於頂空分析瓶","加入鹽酸+氯化亞錫反應試劑,迅速封瓶混勻",
       "於 80°C 加熱 120 分鐘,使二硫代胺基甲酸鹽裂解放出 CS₂","取 1 mL 頂空氣體注入 GC,Porpak Q 柱分離",
       "以 FPD(325 nm 硫濾光鏡)偵測 CS₂","以波峰面積根號值對標準曲線,算含量(C/M,以 CS₂ 計)"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！秤樣裝瓶→加試劑封瓶→加熱裂解→取頂空進 GC→FPD 偵測→根號面積定量。",
       "tip":"提示:先封瓶加熱讓 CS₂ 釋出,再取頂空氣體進樣;FPD 偵測後用根號面積定量。"}
  },
  "calc": {
    "g6":{"answer":1.5,"tol":0.1,
      "ok":"🎉 正確！含量 = C/M = 3.0/2 = <b>1.5 ppm</b>(以 CS₂ 計)。",
      "bad":"再算算：含量 = C/M = 3.0/2。",
      "hint":"提示:3.0 µg ÷ 2 g = 1.5 µg/g = 1.5 ppm。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"spec","t":"n","star":True},{"k":"d"},{"k":"f"}],
    "rows":[
      {"m":"頂空 GC-FPD(本法 MOHWP0054)","spec":3,"d":"共同產物 CS₂","f":"快·測總量·硫選擇·有假陽性需確認"},
      {"m":"比色法(CS₂ 顯色)","spec":2,"d":"CS₂ 顯色","f":"古典·較不專一"},
      {"m":"LC-MS/MS(個別農藥)","spec":5,"d":"各 dithiocarbamate 分子","f":"可分品項·專一·較複雜"}
    ]
  }
}

dc.build_html(
  {"title":"二硫代胺基甲酸鹽殺菌劑檢驗 GC-FPD · MOHWP0054.04","brand":"殺菌劑 · GC-FPD"},
  S, CFG, OUT)
