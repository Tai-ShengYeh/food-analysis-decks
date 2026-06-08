# -*- coding: utf-8 -*-
"""Nielsen Ch16 Ash Analysis — SOIL HTML deck. Uses ../soil_deck_common.py.
Run: python build_ch16.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
FURNACE_SVG = """
<svg viewBox="0 0 320 300">
 <defs><linearGradient id="gf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbeede"/><stop offset="1" stop-color="#f3d6b0"/></linearGradient></defs>
 <rect x="40" y="60" width="240" height="170" rx="14" fill="#48597a"/>
 <rect x="58" y="84" width="204" height="118" rx="8" fill="url(#gf)" stroke="#d9822b" stroke-width="3"/>
 <rect x="58" y="84" width="204" height="118" rx="8" fill="none" stroke="#d9822b" stroke-width="3"/>
 <g stroke="#d9822b" stroke-width="2.4" fill="none" opacity="0.85">
  <path d="M74 100 h172"/><path d="M74 122 h172"/><path d="M74 144 h172"/><path d="M74 166 h172"/><path d="M74 188 h172"/></g>
 <rect x="120" y="150" width="80" height="34" rx="5" fill="#fff" stroke="#15233f" stroke-width="2"/>
 <text x="160" y="172" text-anchor="middle" class="lblb">坩堝+樣品</text>
 <rect x="118" y="232" width="84" height="20" rx="5" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
 <text x="160" y="247" text-anchor="middle" class="lbl">550°C</text>
 <path d="M158 60 q4 -16 8 0 M170 52 q4 -16 8 0" fill="none" stroke="#d94f4f" stroke-width="2.6"/>
 <text x="160" y="290" text-anchor="middle" class="lblb">馬弗爐 Muffle furnace</text>
</svg>"""

CRUCIBLE_SVG = """
<svg viewBox="0 0 560 230">
 <g font-size="13">
  <path d="M60 80 L100 170 L20 170 Z" fill="#f3eee7" stroke="#48597a" stroke-width="2.4"/>
  <ellipse cx="60" cy="80" rx="40" ry="12" fill="#fff" stroke="#48597a" stroke-width="2.4"/>
  <text x="60" y="200" text-anchor="middle" class="lblb">瓷坩堝</text>
  <text x="60" y="218" text-anchor="middle" class="lbl">便宜·常用</text>
  <path d="M200 80 L240 170 L160 170 Z" fill="#eef6ff" stroke="#1f6feb" stroke-width="2.4"/>
  <ellipse cx="200" cy="80" rx="40" ry="12" fill="#fff" stroke="#1f6feb" stroke-width="2.4"/>
  <text x="200" y="200" text-anchor="middle" class="lblb">石英坩堝</text>
  <text x="200" y="218" text-anchor="middle" class="lbl">耐酸·耐高溫</text>
  <path d="M340 80 L380 170 L300 170 Z" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.4"/>
  <ellipse cx="340" cy="80" rx="40" ry="12" fill="#fff" stroke="#1f9d6b" stroke-width="2.4"/>
  <text x="340" y="200" text-anchor="middle" class="lblb">鉑坩堝</text>
  <text x="340" y="218" text-anchor="middle" class="lbl">最惰性·最貴</text>
  <path d="M480 80 L520 170 L440 170 Z" fill="#fff6ea" stroke="#d9822b" stroke-width="2.4" stroke-dasharray="5 4"/>
  <ellipse cx="480" cy="80" rx="40" ry="12" fill="#fff" stroke="#d9822b" stroke-width="2.4"/>
  <text x="480" y="200" text-anchor="middle" class="lblb">石英纖維</text>
  <text x="480" y="218" text-anchor="middle" class="lbl">拋棄·快冷</text>
  <text x="280" y="34" text-anchor="middle" class="lblb" font-size="15">坩堝選擇：看耐溫與是否污染</text>
 </g>
</svg>"""

DTREE_SVG = """
<svg viewBox="0 0 980 360">
 <rect x="380" y="14" width="220" height="56" rx="12" fill="#1f6feb"/>
 <text x="490" y="40" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">你的目標是什麼？</text>
 <text x="490" y="60" text-anchor="middle" fill="#cfe0f6" font-size="12">選擇灰化方法</text>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M420 70 C 200 110,130 120,120 150"/><path d="M470 70 C 400 120,380 120,375 150"/>
  <path d="M510 70 C 590 120,610 120,625 150"/><path d="M560 70 C 800 110,860 120,875 150"/></g>
 <g font-size="14" font-weight="800">
  <rect x="30" y="150" width="190" height="120" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="125" y="178" text-anchor="middle" fill="#15233f">只要總灰分?</text>
  <text x="125" y="206" text-anchor="middle" fill="#d9822b" font-size="16">乾式灰化</text>
  <text x="125" y="232" text-anchor="middle" fill="#48597a" font-size="12">安全·免酸·多樣品</text>
  <text x="125" y="252" text-anchor="middle" fill="#48597a" font-size="12">慢(12–18h)</text>
  <rect x="280" y="150" width="190" height="120" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="375" y="178" text-anchor="middle" fill="#15233f">要測揮發性礦物?</text>
  <text x="375" y="206" text-anchor="middle" fill="#1f6feb" font-size="16">濕式灰化</text>
  <text x="375" y="232" text-anchor="middle" fill="#48597a" font-size="12">低溫·礦物不揮發</text>
  <text x="375" y="252" text-anchor="middle" fill="#48597a" font-size="12">留在溶液好分析</text>
  <rect x="530" y="150" width="190" height="120" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="625" y="178" text-anchor="middle" fill="#15233f">要快速·高通量?</text>
  <text x="625" y="206" text-anchor="middle" fill="#1f9d6b" font-size="16">微波灰化</text>
  <text x="625" y="232" text-anchor="middle" fill="#48597a" font-size="12">數十分鐘完成</text>
  <text x="625" y="252" text-anchor="middle" fill="#48597a" font-size="12">設備貴·單次量少</text>
  <rect x="780" y="150" width="190" height="120" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="875" y="178" text-anchor="middle" fill="#15233f">果醬·糖漿摻假?</text>
  <text x="875" y="206" text-anchor="middle" fill="#15233f" font-size="16">特殊灰分</text>
  <text x="875" y="232" text-anchor="middle" fill="#48597a" font-size="12">水溶/酸不溶灰分</text>
  <text x="875" y="252" text-anchor="middle" fill="#48597a" font-size="12">硫酸化灰分</text>
 </g>
</svg>"""

# ---------------- 引起動機 ----------------
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 16",
    "灰分<span style='color:var(--accent-2)'>分析</span>", "Ash Analysis",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>乾式灰化 · 濕式灰化 · 微波灰化 · 坩堝 · 礦物前處理",
    ["馬弗爐 550°C","酸消化","微波","水溶/酸不溶","% 灰分"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">把食物<span class="hi">完全燒光</span>，剩下的是什麼？</div>
  <p class="subtitle" style="max-width:780px;margin:22px auto 0">有機物會化成 CO₂ 與水蒸氣飛走，<br>
  留下來的白色殘渣——就是<strong>礦物質 (無機物)</strong>，我們稱為<strong>灰分 (ash)</strong>。</p>
  <div style="margin-top:24px"><span class="pill">總礦物量</span><span class="pill">營養品質</span>
  <span class="pill">毒性重金屬</span><span class="pill">摻假檢測</span><span class="pill">礦物前處理</span></div></div>""")

add(MOT, dc.kt("16.1.1 定義", "灰分是<span class='hi'>什麼</span>") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li><strong>灰分 (ash)</strong>：食品中有機物完全燃燒或酸氧化後，剩下的<strong>無機(礦物)殘渣</strong></li>" +
    "<li>本質是<span class='em'>重量分析 (gravimetric)</span>：比較<strong>灰重</strong>與<strong>原樣品重</strong></li>" +
    "<li>礦物會轉成氧化物、硫酸鹽、磷酸鹽、氯化物、矽酸鹽</li>" +
    "<li>可用<strong>濕基</strong>或<strong>乾基</strong>表示</li>" +
    '</ul></div><div class="note"><strong>核心：灰分 ≈ 食品的「總礦物質」估計值。</strong><br>' +
    "兩大灰化法：<strong>乾式</strong>(高溫燃燒) 與 <strong>濕式</strong>(酸氧化)。</div></div>")

add(MOT, dc.kt("16.1.2 為什麼重要", "為什麼要測灰分") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("📊","概略分析","測食品<strong>總礦物量</strong>，是 proximate analysis 的一環") +
    dc.card("🧫","礦物前處理","為特定礦物(鈣、鐵…)或重金屬分析<strong>先除去有機物</strong>","a") +
    dc.card("🥛","營養品質","乳品富鈣、牛肉富鐵；植物礦物量隨<strong>土壤</strong>變化","g") +
    dc.card("⚠️","毒性與保存","砷會在土壤累積進稻米；高過渡金屬加速油脂酸敗","b") + '</div>')

add(MOT, dc.kt("16.1.2 應用面", "灰分透露的<span class='hi'>三件事</span>") +
    '<div class="grid3" style="margin-top:22px">' +
    dc.card("🌱","土壤的指紋","植物礦物量隨<strong>土壤</strong>變化大；砷土種的稻米會濃縮砷","g") +
    dc.card("🏷️","規格與標示","雖不直接標於人食，但常是<strong>麵粉/全穀的規格</strong>，也標於寵物食品","b") +
    dc.card("🛢️","保存期","脂質食品中高量<strong>過渡金屬</strong>會加速酸敗、縮短保存","a") + '</div>' +
    '<p class="subtitle" style="margin-top:18px">所以灰分既是「營養」指標，也是「品質、毒性、保存」的線索。</p>')

add(MOT, dc.chart_inner("ashfood", "食物裡的<span class='hi'>灰分</span>含量", "資料：USDA FoodData Central，% 灰分（濕基）。乾燥食品最高，新鮮食品多 < 5%。",
    kicker="16.1.3 食物中的含量"), ' data-chart="ashfood"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">核心命題</div>
  <div class="hook" style="font-size:clamp(1.7rem,4vw,3rem)">灰分 = <span class="hi">秤</span>燒完的殘渣</div>
  <p class="lead" style="max-width:820px;margin:20px auto 0">灰化是一種<strong>重量分析</strong>：把樣品燒到只剩礦物，<strong>秤重</strong>再算百分比。</p>
  <div class="eq" style="max-width:560px;margin:24px auto 0">% 灰分 = <span class="frac"><b>灰重</b><span>樣品重</span></span> × 100<br>
  <span style="font-size:.78em;color:var(--ink-2)">分母用濕重→濕基；用乾重→乾基</span></div></div>""")

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","乾式 vs 濕式：分特徵", 8,
    "把 8 個特徵分到「乾式灰化」或「濕式灰化」。"), ' data-game="g1"')

# ---------------- 維持注意 ----------------
add(ATT, dc.kt("方法全覽", "四大灰化方法") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("🔥","乾式灰化","馬弗爐 500–600°C 高溫燃燒；安全、免試劑","a") +
    dc.card("🧪","濕式灰化","強酸 + 氧化劑、100–120°C 氧化；礦物留溶液","b") +
    dc.card("📡","微波灰化","微波加熱(乾或濕)；數十分鐘、高通量","g") +
    dc.card("🔬","特殊灰分","水溶/不溶、酸不溶、鹼度、硫酸化灰分","b") + '</div>')

add(ATT, dc.kt("16.2.1 取樣前處理", "灰化前要<span class='hi'>準備</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>樣品量小：一般 <strong>2–10 g</strong>(新機種可低至 250 mg)，需均勻代表性</li>" +
    "<li>高水分蔬果先<strong>烘乾</strong>(≤100°C)，避免沸騰噴濺損失</li>" +
    "<li>高脂肉品先<strong>乾燥+脫脂</strong>，避免冒煙起火</li>" +
    "<li>易燃揮發物(乙醇)須先除去</li></ul></div>" +
    '<div class="note"><strong>污染是大敵：</strong>磨樣的鋼製器具會帶入<strong>鐵</strong>；坩堝、玻璃器皿要酸洗。<br>' +
    "用<strong>空白 (blank)</strong> 校正環境與器具污染。</div></div>")

add(ATT, dc.kt("16.2.2 乾式灰化", "Dry：高溫燒成灰") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + FURNACE_SVG + '</div><div><ul class="clean">' +
    "<li><strong>原理</strong>：馬弗爐 <span class='em'>525°C 以上</span>，有機物在氧氣下燃燒成 CO₂ 與氮氧化物</li>" +
    "<li><strong>時間</strong>：約 12–18 小時(或過夜)</li>" +
    "<li>剩下礦物 → 氧化物、硫酸鹽、磷酸鹽等</li>" +
    "<li><strong>優點</strong>：安全、免酸、可同時跑很多樣品</li>" +
    '</ul><div class="note" style="margin-top:12px">缺點：慢；As、Cd、Pb、Hg、P、Zn 等<strong>揮發性元素會流失</strong>。</div></div></div>')

add(ATT, dc.kt("坩堝怎麼選", "看耐溫與會不會污染") +
    '<div class="svgwrap" style="margin-top:6px">' + CRUCIBLE_SVG + '</div>' +
    '<div class="note" style="margin-top:14px"><strong>瓷</strong>便宜常用但驟冷會裂；<strong>石英纖維</strong>可拋棄、耐 1000°C、秒冷；' +
    "<strong>鋼</strong>含 Fe/Cr/Ni 會虛增灰分；<strong>鉑</strong>最惰性但太貴。</div>")

add(ATT, dc.kt("坩堝的細節", "標記與<span class='hi'>預灰化</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>麥克筆寫的記號會在灰化時<strong>燒掉</strong> → 用鋼針刻、或鑽石筆刻痕</li>" +
    "<li>可用 <strong>FeCl₃/HCl</strong>(鐵釘溶於濃 HCl)的棕色顏料做永久標記</li>" +
    "<li>坩堝使用前要先<strong>灼燒並清潔</strong>(預灰化)，去除有機污染</li>" +
    "<li>酸洗 + 去離子水反覆沖洗，消除礦物污染</li></ul></div>" +
    '<div class="note"><strong>為什麼這麼講究？</strong>灰分是微量重量分析，<br>' +
    "任何來自器具的礦物(尤其<strong>鐵</strong>)或殘碳都會直接造成誤差。</div></div>")

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","乾式灰化即時測驗", 4), ' data-game="g2"')

add(ATT, dc.kt("16.2.3 濕式灰化", "Wet：用酸把有機物氧化掉") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>又稱<strong>濕氧化 / 濕消化</strong></li>" +
    "<li>常用<strong>濃 HNO₃ + 濃 H₂SO₄</strong>(有時加 H₂O₂)，100–120°C</li>" +
    "<li>低溫且可用密閉壓力瓶 → <strong>礦物不揮發、留在溶液</strong></li>" +
    "<li>過氯酸(HClO₄)會生爆炸性過氧化物，已停用</li></ul></div>" +
    '<div class="note"><strong>用途：</strong>為特定礦物分析(如 ICP)做前處理時的<strong>首選</strong>。<br>' +
    "缺點：需<strong>全程顧爐</strong>、腐蝕性試劑、單次量少。</div></div>")

add(ATT, dc.chart_inner("temp", "三種灰化的<span class='hi'>溫度與時間</span>",
    "整合自 Table 16.2：典型溫度(°C)與所需時間(小時)。微波大幅縮短時間。", kicker="16.3 方法比較", height="52vh"),
    ' data-chart="temp"')

add(ATT, dc.game_sort_inner("g4","小遊戲 ③","乾式灰化流程排序", 6,
    "用 ▲▼ 把乾式灰化(AOAC 通用程序)的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("操作陷阱", "別把<span class='hi'>熱坩堝</span>直接丟進乾燥器") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("💨","為什麼不行","熱樣品產生壓力可能<strong>頂開</strong>乾燥器蓋；冷卻時又形成<strong>真空</strong>很難打開","a") +
    dc.card("✅","正確做法","先讓坩堝在爐內降到 250°C 以下，鉗入乾燥器；蓋子<strong>側推</strong>緩慢進氣","b") +
    '</div><div class="note" style="margin-top:18px">常見錯誤示範：用<strong>全鋼鉗</strong>夾(污染鐵)、<strong>800°C/48 h</strong>過度灼燒、' +
    "在開放空間冷卻(吸濕)。每一步都會讓灰分數值失真。</div>")

add(ATT, dc.kt("16.2.4 微波灰化", "Microwave：分鐘級的灰化") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("💧","微波濕式","酸消化於開放或密閉瓶；密閉可達 1500 psi、酸超過沸點，30 分內完成","b") +
    dc.card("🔥","微波乾式","微波馬弗爐可達 1200°C，數分鐘灰化，最多省 97% 時間，常免抽氣櫃","a") +
    '</div><div class="note" style="margin-top:18px">速度快 → <strong>通量大</strong>(5–24 樣/時)；但設備貴、單次裝載量較少。已廣用於品管。</div>')

add(ATT, dc.kt("16.2.5 特殊灰分", "四種「特殊灰分」") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🍓","水溶/水不溶灰分","灰溶於沸水過濾分兩部分；<strong>水溶灰分低 → 果肉含量高</strong>(果醬品質)","b") +
    dc.card("🪨","酸不溶灰分","灰溶於 10% HCl，不溶者多為<strong>矽酸鹽</strong> → 測蔬果表面砂土污染","a") +
    dc.card("⚖️","灰分鹼度","以 NaOH 滴定；蔬果灰呈<strong>鹼性</strong>、肉與穀類偏酸","g") +
    dc.card("🍬","硫酸化灰分","加 H₂SO₄ 灼燒至恆重；多用於<strong>糖、糖漿、色素</strong>","b") + '</div>')

add(ATT, dc.game_bucket_inner("g3","小遊戲 ④","特殊灰分：對應用途", 6,
    "把 6 個情境分給最合適的「特殊灰分」測定。"), ' data-game="g3"')

add(ATT, dc.kt("樣品的麻煩", "高脂·高糖·高水分怎麼辦") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>高脂/高蛋白</strong>(起司、香料、花生)：易冒煙起火 → 微開爐門慢燒，或先脫脂</li>" +
    "<li><strong>高糖</strong>：易結焦成<strong>焦油</strong>(高估灰分) → 混棉絮、加幾滴橄欖油助蒸氣逸出</li>" +
    "<li><strong>高水分</strong>(肉、糖漿)：先在蒸氣浴/紅外燈蒸乾</li></ul></div>" +
    '<div class="note">殘碳(黑色焦油)未燒完時：加幾滴水或硝酸<strong>再灰化</strong>；' +
    "仍不行就用<strong>無灰濾紙</strong>過濾後重灰化(扣濾紙重)。</div></div>")

add(ATT, dc.kt("揮發流失", "為什麼乾式會<span class='hi'>少算</span>某些礦物？") +
    '<div class="note" style="margin-top:14px">乾式灰化溫度高(550°C+)，部分元素會<strong>揮發流失</strong>：' +
    "As、B、Cd、Cr、Cu、Fe、Pb、Hg、Ni、P、V、Zn。要測這些礦物時，改用<strong>低溫濕式灰化</strong>。</div>" +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("🔥","乾式的盲點","高溫把揮發性元素趕跑 → 這些礦物會被低估","a") +
    dc.card("🧪","濕式的補位","低溫 + 密閉 → 礦物不揮發、留在溶液，適合後續元素分析","b") + '</div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對方法", 5), ' data-game="g5"')

# ---------------- 喚起行動 ----------------
add(ACT, dc.cmp_inner("一張表選方法（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"temp","t":"n","label":"溫度°C"},
     {"k":"time","t":"s","label":"時間"},{"k":"safe","t":"n","label":"安全度","star":True},{"k":"app","t":"s","label":"主要應用"}],
    "安全度：★ 越多越安全。整合自 Table 16.2。", kicker="16.3 方法比較"), ' data-game="cmp"')

add(ACT, dc.kt("方法選擇", "跟著決策樹走") +
    '<div class="svgwrap" style="margin-top:10px">' + DTREE_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:14px">下一頁實戰：算一杯生咖啡的灰分 →</p>')

add(ACT, dc.kt("16.6 計算", "從坩堝秤重到 % 灰分") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">% 灰分 = ' +
    '<span class="frac"><b>灰化後 − 坩堝空重</b><span>原樣品重</span></span> × 100</div>' +
    '<div><ul class="clean"><li>灰重 = (坩堝+灰) − 空坩堝</li>' +
    "<li>分母用<strong>原(濕)樣品重</strong> → 濕基</li>" +
    "<li>除以乾物係數(DMC) → 乾基</li>" +
    "<li>例：DMC = 1 − 水分%/100</li></ul></div></div>")

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關",
    "生咖啡(水分 11.5%)：取樣 5.2146 g，空坩堝 28.5053 g，灰化後坩堝+灰 28.5939 g。"
    "求<strong>濕基 % 灰分</strong>。", unit="%"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li><strong>灰分＝燒完剩下的礦物</strong>，是重量分析(秤灰重)</li>" +
    "<li>乾式：<strong>馬弗爐 550°C</strong>、安全免酸、但慢且揮發流失</li>" +
    "<li>濕式：<strong>酸氧化 100–120°C</strong>、礦物留溶液、適合礦物前處理</li></ul>" +
    '<ul class="clean"><li>微波(乾或濕)：分鐘級、高通量、設備貴</li>' +
    "<li>特殊灰分：水溶/酸不溶/鹼度/硫酸化 → 品質與摻假</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["解釋灰分的定義與它是「重量分析」",
     "說出乾式灰化的溫度、時間與優缺點",
     "比較乾式與濕式灰化的差異與適用時機",
     "說明微波灰化的最大優勢(速度/通量)",
     "舉出至少兩種特殊灰分及其用途",
     "由坩堝秤重算出濕基與乾基 % 灰分",
     "解釋為何某些礦物在乾式灰化會流失"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把灰分分析<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions、Practice Problems<br>"
    "🔜 銜接章節：<strong>礦物質分析 (Ch9/21)</strong>、<strong>水分分析 (Ch15)</strong><br>"
    "🧪 思考：你的樣品要測總灰分還是特定礦物？高脂高糖嗎？該選乾式還是濕式？",
    ["乾式灰化","濕式灰化","微波灰化","特殊灰分","% 灰分"]), ' data-cover="1"')

# ---------------- CFG ----------------
CFG = {
  "charts": {
    "ashfood": {"type":"bar","yTitle":"% 灰分（濕基）",
      "labels":["牛肉乾","裸麥麵包","炸魚排","葡萄乾","漢堡肉","煉乳","全麥麵粉","糙米","優格","蘋果"],
      "datasets":[{"label":"% 灰分","data":[6.8,2.5,2.5,1.9,1.9,1.6,1.6,1.5,1.1,0.2],"color":"#1f6feb"}]},
    "temp": {"type":"bar","yTitle":"數值",
      "labels":["乾式","濕式","微波乾式","微波濕式"],
      "datasets":[
        {"label":"溫度 °C","data":[550,110,1000,200],"color":"#d9822b"},
        {"label":"時間 小時","data":[15,2,0.5,0.5],"color":"#1f6feb"}]}
  },
  "bucket": {
    "g1": {"cats":["乾式灰化","濕式灰化"],
      "items":[{"t":"馬弗爐 500–600°C","c":"乾式灰化"},{"t":"用強酸氧化","c":"濕式灰化"},
        {"t":"礦物留在溶液","c":"濕式灰化"},{"t":"可同時跑多樣品","c":"乾式灰化"},
        {"t":"100–120°C 低溫","c":"濕式灰化"},{"t":"揮發性元素易流失","c":"乾式灰化"},
        {"t":"需全程顧爐","c":"濕式灰化"},{"t":"安全·免試劑","c":"乾式灰化"}],
      "ok":"🎉 全對！乾式靠高溫燃燒、濕式靠酸氧化；濕式礦物不流失但要顧爐。",
      "tip":"提示：高溫、免酸、可多樣品 → 乾式；強酸、低溫、礦物留溶液 → 濕式。"},
    "g3": {"cats":["水溶/不溶灰分","酸不溶灰分","硫酸化灰分"],
      "items":[{"t":"判斷果醬的果肉含量","c":"水溶/不溶灰分"},{"t":"果肉多→水溶灰分低","c":"水溶/不溶灰分"},
        {"t":"測蔬果表面砂土污染","c":"酸不溶灰分"},{"t":"不溶物多為矽酸鹽","c":"酸不溶灰分"},
        {"t":"糖與糖漿的殘留","c":"硫酸化灰分"},{"t":"加 H₂SO₄ 灼燒至恆重","c":"硫酸化灰分"}],
      "ok":"🎉 正確！水溶/不溶看果肉、酸不溶看砂土矽酸鹽、硫酸化用於糖類。",
      "tip":"提示：果醬→水溶/不溶；表面砂土(矽酸鹽)→酸不溶；糖/色素→硫酸化。"}
  },
  "mcq": {
    "g2":[
      {"q":"乾式灰化用的設備是？","o":["熱盤 + 酸","馬弗爐","離心機","分光光度計"],"a":1,
       "e":"乾式灰化在馬弗爐 (muffle furnace) 中高溫燃燒。"},
      {"q":"典型乾式灰化的溫度約為？","o":["100–120°C","250°C","500–600°C","1500°C"],"a":2,
       "e":"乾式灰化約 525°C 以上，常用 550°C。"},
      {"q":"乾式灰化的主要缺點是？","o":["需用強酸","耗時長且揮發性元素流失","無法跑多樣品","不安全"],"a":1,
       "e":"乾式需 12–18 小時，且 As、Pb、Zn 等揮發性元素會流失。"},
      {"q":"哪種坩堝最惰性但最昂貴？","o":["瓷","鋼","鉑","石英纖維"],"a":2,
       "e":"鉑坩堝最惰性、最佳，但太貴不適合大量例行使用。"}
    ],
    "g5":[
      {"q":"只要測食品的總灰分(概略分析)，最省事的選擇？","o":["濕式灰化","乾式灰化","逐元素 ICP","層析"],"a":1,
       "e":"乾式安全、免酸、可多樣品，適合測總灰分。"},
      {"q":"要測會揮發的礦物(如 As、Pb)，較不會流失的方法？","o":["乾式灰化","濕式灰化","更高溫乾式","延長乾式時間"],"a":1,
       "e":"濕式低溫且可密閉，礦物不揮發、留在溶液中。"},
      {"q":"工廠要快速、高通量做大量樣品的灰分，選？","o":["傳統乾式","傳統濕式","微波灰化","靜置乾燥"],"a":2,
       "e":"微波灰化數十分鐘完成，通量高(5–24 樣/時)。"},
      {"q":"要判斷果醬的果肉含量，該測哪種灰分？","o":["硫酸化灰分","水溶/水不溶灰分","灰分鹼度","總灰分"],"a":1,
       "e":"水溶灰分越低代表果肉含量越高。"},
      {"q":"高脂花生乾式灰化時冒煙起火，最佳處理？","o":["直接關爐門快燒","微開爐門慢燒或先脫脂","加更多樣品","升到 1000°C"],"a":1,
       "e":"高脂高蛋白先脫脂，或微開爐門讓它慢慢燒完再關門。"}
    ]
  },
  "sort": {
    "g4":{"steps":["精秤 5–10 g 樣品入已知重坩堝(高水分先預乾)","用坩堝鉗把坩堝放入冷的馬弗爐",
       "約 550°C 加熱 12–18 小時(或過夜)","關爐，待降到 250°C 以下再緩緩開門",
       "用鉗夾入乾燥器，蓋好冷卻至室溫","秤重，算灰重 → % 灰分"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！秤樣→入冷爐→高溫燒→降溫開門→乾燥器冷卻→秤重算。","tip":"提示：一定先放冷爐再升溫；燒完要降到 250°C 以下才開門，避免吹散灰。"}
  },
  "calc": {
    "g6":{"answer":1.70,"tol":0.05,
      "ok":"🎉 正確！灰重 = 28.5939 − 28.5053 = 0.0886 g；0.0886 ÷ 5.2146 × 100 = <b>1.70%</b>(濕基)。",
      "bad":"再算算：先求灰重 = 28.5939 − 28.5053 = 0.0886 g，再 ÷ 5.2146 × 100。",
      "hint":"提示：灰重 0.0886 g；濕基 = 0.0886 ÷ 5.2146 × 100 ≈ 1.70%(乾基需再 ÷0.885 ≈ 1.92%)。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"temp","t":"n"},{"k":"time"},{"k":"safe","t":"n"},{"k":"app"}],
    "rows":[
      {"m":"乾式灰化","temp":550,"time":"12–18 h","safe":4,"app":"總灰分·概略分析·礦物前處理"},
      {"m":"濕式灰化","temp":110,"time":"~2 h","safe":2,"app":"礦物前處理(官方法)·防揮發"},
      {"m":"微波乾式","temp":1000,"time":"~30 min","safe":3,"app":"總灰分·品管(快速)"},
      {"m":"微波濕式","temp":200,"time":"~30 min","safe":3,"app":"礦物前處理(快速·ICP)"}
    ]
  }
}

dc.build_html(
  {"title":"灰分分析 Ash Analysis · Nielsen Ch16","brand":"ASH · CH16"},
  S, CFG, OUT)
