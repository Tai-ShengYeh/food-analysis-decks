# -*- coding: utf-8 -*-
"""Nielsen Ch19 Carbohydrate Analysis — SOIL HTML deck. Uses ../soil_deck_common.py.
Run: python build_ch19.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
# 苯酚-硫酸法（總糖）顯色反應示意
PHENOL_SVG = """
<svg viewBox="0 0 560 240">
 <g font-size="13">
  <rect x="14" y="86" width="116" height="64" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="72" y="112" text-anchor="middle" class="lblb">醣類樣品</text>
  <text x="72" y="132" text-anchor="middle" class="lbl">清澈水溶液</text>
  <rect x="166" y="86" width="116" height="64" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="224" y="106" text-anchor="middle" class="lblb">加濃硫酸</text>
  <text x="224" y="126" text-anchor="middle" class="lbl">脫水→糠醛</text>
  <text x="224" y="144" text-anchor="middle" class="lbl">(furfural)</text>
  <rect x="318" y="86" width="116" height="64" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="376" y="112" text-anchor="middle" class="lblb">與苯酚縮合</text>
  <text x="376" y="132" text-anchor="middle" class="lbl">黃金色產物</text>
  <rect x="470" y="86" width="78" height="64" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="509" y="106" text-anchor="middle" class="lblb">比色</text>
  <text x="509" y="126" text-anchor="middle" class="lbl">490 nm</text>
  <text x="509" y="144" text-anchor="middle" class="lbl">測 A</text>
  <g stroke="#8493ad" stroke-width="2.5" fill="none" marker-end="url(#arp)">
   <path d="M130 118 h34"/><path d="M282 118 h34"/><path d="M434 118 h34"/></g>
  <defs><marker id="arp" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#8493ad"/></marker></defs>
  <text x="280" y="44" text-anchor="middle" class="lblb" font-size="15">苯酚-硫酸法 Phenol-Sulfuric Acid</text>
  <text x="280" y="64" text-anchor="middle" class="lbl">測幾乎所有單/寡/多醣（糖醇不顯色）·需標準曲線</text>
 </g>
</svg>"""

# 總澱粉酵素水解示意（α-amylase + glucoamylase → glucose → GOPOD）
STARCH_SVG = """
<svg viewBox="0 0 560 250">
 <g font-size="13">
  <rect x="20" y="92" width="104" height="62" rx="10" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="72" y="118" text-anchor="middle" class="lblb">澱粉</text>
  <text x="72" y="138" text-anchor="middle" class="lbl">DMSO 糊化</text>
  <rect x="156" y="92" width="104" height="62" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="208" y="112" text-anchor="middle" class="lblb">α-澱粉酶</text>
  <text x="208" y="132" text-anchor="middle" class="lbl">切成寡醣片段</text>
  <rect x="292" y="92" width="116" height="62" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="350" y="112" text-anchor="middle" class="lblb">葡萄糖澱粉酶</text>
  <text x="350" y="132" text-anchor="middle" class="lbl">完全水解→葡萄糖</text>
  <rect x="440" y="92" width="100" height="62" rx="10" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="490" y="112" text-anchor="middle" class="lblb">GOPOD</text>
  <text x="490" y="132" text-anchor="middle" class="lbl">顯色定量</text>
  <g stroke="#8493ad" stroke-width="2.5" fill="none" marker-end="url(#ars)">
   <path d="M124 123 h30"/><path d="M260 123 h30"/><path d="M408 123 h30"/></g>
  <defs><marker id="ars" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#8493ad"/></marker></defs>
  <text x="280" y="44" text-anchor="middle" class="lblb" font-size="15">總澱粉測定 Total Starch</text>
  <text x="280" y="64" text-anchor="middle" class="lbl">酵素專一水解成葡萄糖，再以葡萄糖氧化酶偶聯定量</text>
  <text x="280" y="180" text-anchor="middle" class="lbl">注意：抗性澱粉(RS)不易完全水解 → 多歸入膳食纖維</text>
 </g>
</svg>"""

# 決策樹：要測哪種碳水化合物？
DTREE_SVG = """
<svg viewBox="0 0 980 360">
 <rect x="378" y="14" width="224" height="56" rx="12" fill="#1f6feb"/>
 <text x="490" y="40" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">你要測的是什麼？</text>
 <text x="490" y="60" text-anchor="middle" fill="#cfe0f6" font-size="12">選擇碳水化合物分析方法</text>
 <g stroke="#8493ad" stroke-width="2" fill="none">
  <path d="M420 70 C 200 110,130 120,120 150"/><path d="M470 70 C 400 120,380 120,375 150"/>
  <path d="M510 70 C 590 120,610 120,625 150"/><path d="M560 70 C 800 110,860 120,875 150"/></g>
 <g font-size="14" font-weight="800">
  <rect x="30" y="150" width="190" height="124" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2"/>
  <text x="125" y="178" text-anchor="middle" fill="#15233f">總糖(混合醣)?</text>
  <text x="125" y="206" text-anchor="middle" fill="#d9822b" font-size="16">苯酚-硫酸法</text>
  <text x="125" y="232" text-anchor="middle" fill="#48597a" font-size="12">490nm 比色</text>
  <text x="125" y="252" text-anchor="middle" fill="#48597a" font-size="12">糖醇不顯色</text>
  <rect x="280" y="150" width="190" height="124" rx="12" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2"/>
  <text x="375" y="178" text-anchor="middle" fill="#15233f">還原糖?</text>
  <text x="375" y="206" text-anchor="middle" fill="#1f6feb" font-size="16">Somogyi-Nelson</text>
  <text x="375" y="232" text-anchor="middle" fill="#48597a" font-size="12">Cu²⁺→Cu⁺</text>
  <text x="375" y="252" text-anchor="middle" fill="#48597a" font-size="12">或 Lane-Eynon 滴定</text>
  <rect x="530" y="150" width="190" height="124" rx="12" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2"/>
  <text x="625" y="178" text-anchor="middle" fill="#15233f">個別糖/澱粉?</text>
  <text x="625" y="206" text-anchor="middle" fill="#1f9d6b" font-size="16">HPLC / 酵素法</text>
  <text x="625" y="232" text-anchor="middle" fill="#48597a" font-size="12">HPAEC-PAD 分離</text>
  <text x="625" y="252" text-anchor="middle" fill="#48597a" font-size="12">澱粉→葡萄糖 GOPOD</text>
  <rect x="780" y="150" width="190" height="124" rx="12" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
  <text x="875" y="178" text-anchor="middle" fill="#15233f">膳食纖維?</text>
  <text x="875" y="206" text-anchor="middle" fill="#15233f" font-size="16">AOAC 酵素重量法</text>
  <text x="875" y="232" text-anchor="middle" fill="#48597a" font-size="12">除澱粉/蛋白後秤殘渣</text>
  <text x="875" y="252" text-anchor="middle" fill="#48597a" font-size="12">991.43</text>
 </g>
</svg>"""

# ---------------- 引起動機 ----------------
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 19",
    "碳水化合物<span style='color:var(--accent-2)'>分析</span>", "Carbohydrate Analysis",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>分類 · 苯酚-硫酸法 · 還原糖 · HPLC · 酵素法 · 澱粉 · 膳食纖維",
    ["單/寡/多醣","總糖","還原糖","HPLC/PAD","膳食纖維"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">營養標示上的<span class="hi">總碳水化合物</span>，是「量」出來的嗎？</div>
  <p class="subtitle" style="max-width:800px;margin:22px auto 0">其實多數標示上的總碳水化合物是用<strong>差減法</strong>算的：<br>
  總重 −（水分＋蛋白質＋脂肪＋灰分）。它<strong>不是</strong>直接測量值。</p>
  <div style="margin-top:24px"><span class="pill">能量來源</span><span class="pill">質地</span>
  <span class="pill">膳食纖維</span><span class="pill">標示與定價</span><span class="pill">摻假鑑別</span></div></div>""")

add(MOT, dc.kt("19.1 為什麼重要", "為什麼要分析碳水化合物") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("⚡","能量主角","可消化醣類提供熱量；自然界 90% 醣以多醣形式存在") +
    dc.card("🏷️","標示法規","總碳水、總糖、添加糖、膳食纖維皆須正確標示","a") +
    dc.card("🍮","質地功能","增稠、穩定乳化泡沫、保水、抗凍融、褐變風味","g") +
    dc.card("🛡️","真偽品管","確認成分標示正確、偵測摻假與來源","b") + '</div>')

add(MOT, dc.kt("19.1 分類", "依分子大小<span class='hi'>分類</span>") +
    '<div class="grid2" style="margin-top:18px"><div><ul class="clean">' +
    "<li><strong>單醣 (DP 1)</strong>：葡萄糖、果糖——唯一能直接吸收</li>" +
    "<li><strong>雙醣 (DP 2)</strong>：蔗糖、乳糖、麥芽糖</li>" +
    "<li><strong>寡醣 (DP 3–9)</strong>：棉子糖、水蘇糖、麥芽糊精</li>" +
    "<li><strong>多醣 (DP &gt;9)</strong>：澱粉、纖維素、果膠、植物膠</li>" +
    '</ul></div><div class="note"><strong>FAO/WHO 依分子大小分：</strong>糖(DP1–2)、寡醣(DP3–9)、多醣(DP&gt;9)。<br>' +
    "人類只能消化<strong>蔗糖、乳糖、麥芽糊精與澱粉</strong>；其餘多醣皆不可消化。</div></div>")

add(MOT, dc.chart_inner("carb", "食物裡的<span class='hi'>碳水化合物</span>含量", "資料：USDA FoodData Central，% 總碳水化合物（濕基，概值）。",
    kicker="19.1 食物中的含量"), ' data-chart="carb"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">核心命題</div>
  <div class="hook" style="font-size:clamp(1.7rem,4vw,3rem)">先<span class="hi">分類</span>，再<span class="hi">選方法</span></div>
  <p class="lead" style="max-width:840px;margin:20px auto 0">沒有單一方法能測「全部」碳水化合物。<br>
  策略是：依<strong>結構類型</strong>（單/寡/多醣、可否消化）選擇對應的分析法。</p>
  <div class="note" style="max-width:640px;margin:24px auto 0">關鍵前處理：先<strong>乾燥→脫脂</strong>，再用<strong>熱 80% 乙醇</strong>萃取低分子醣，把多醣與蛋白留在殘渣。</div></div>""")

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","依分子大小分類", 7,
    "把 7 個碳水化合物依分子大小分到三類（單醣 / 寡醣 / 多醣）。"), ' data-game="g1"')

# ---------------- 維持注意 ----------------
add(ATT, dc.kt("方法全覽", "醣分析方法地圖") +
    '<div class="grid2" style="margin-top:22px">' +
    dc.card("🟡","總糖","苯酚-硫酸法(490nm)——幾乎測所有醣","b") +
    dc.card("🔵","還原糖","Somogyi-Nelson、Lane-Eynon(Cu²⁺還原)","a") +
    dc.card("🧬","個別糖","HPLC / HPAEC-PAD、GC、酵素法(GOPOD)","g") +
    dc.card("🌾","多醣/纖維","澱粉酵素法、膳食纖維 AOAC 重量法、果膠","b") + '</div>')

add(ATT, dc.kt("19.2 樣品前處理", "萃取與淨化") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>乾燥</strong>：真空烤箱乾至恆重（可同時測水分）</li>" +
    "<li><strong>磨碎＋脫脂</strong>：不先除脂，水溶性醣萃取會不完全</li>" +
    "<li><strong>熱 80% 乙醇萃取</strong>：溶出單/寡醣；加碳酸鈣中和防蔗糖水解</li>" +
    "<li><strong>離子交換淨化</strong>：除去帶電的灰分、有機酸、色素</li></ul></div>" +
    '<div class="note">為何用 80% 乙醇而非水？<br>低分子醣<strong>可溶</strong>於熱 80% 乙醇，而<strong>多醣與蛋白不溶</strong>——萃取相當專一。' +
    "（不能用 Soxhlet：含水乙醇會共沸成 95%。）</div></div>")

add(ATT, dc.kt("19.3 總糖", "苯酚-硫酸法") +
    '<div class="svgwrap" style="margin-top:10px">' + PHENOL_SVG + '</div>' +
    '<div class="note" style="margin-top:14px">濃硫酸使醣脫水成糠醛衍生物，與苯酚縮合成<strong>黃金色</strong>，於 <strong>490 nm</strong> 比色。' +
    "簡單、快速、便宜；但<strong>糖醇不顯色</strong>，且反應非計量 → 必須用<strong>標準曲線</strong>。</div>")

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","醣類分析即時測驗", 4), ' data-game="g2"')

add(ATT, dc.kt("19.4.1 還原糖", "Somogyi-Nelson 法") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' +
    """<svg viewBox="0 0 300 300">
     <circle cx="150" cy="120" r="64" fill="#e7f0fe" stroke="#1f6feb" stroke-width="3"/>
     <text x="150" y="112" text-anchor="middle" class="lblb">還原糖</text>
     <text x="150" y="134" text-anchor="middle" class="lbl">游離醛基</text>
     <path d="M150 188 v34" stroke="#d9822b" stroke-width="3" marker-end="url(#a2)"/>
     <defs><marker id="a2" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10 z" fill="#d9822b"/></marker></defs>
     <rect x="70" y="226" width="160" height="56" rx="12" fill="#fbeede" stroke="#d9822b" stroke-width="2.4"/>
     <text x="150" y="250" text-anchor="middle" class="lblb">Cu²⁺ → Cu⁺</text>
     <text x="150" y="270" text-anchor="middle" class="lbl">還原砷鉬酸→藍色 520nm</text>
     <text x="150" y="40" text-anchor="middle" class="lblb" font-size="15">氧化還原顯色</text>
    </svg>""" +
    '</div><div><ul class="clean">' +
    "<li>還原糖的<strong>醛基</strong>把 Cu(II) 還原成 Cu(I)</li>" +
    "<li>Cu(I) 再還原<strong>砷鉬酸</strong>錯合物 → 強烈藍色</li>" +
    "<li>於 <strong>520 nm</strong> 比色定量（葡萄糖當量）</li>" +
    "<li>酮糖會異構成醛糖被一起測到——需標準曲線</li>" +
    '</ul><div class="note" style="margin-top:12px">反應非計量、各糖反應不同 → 必須建標準曲線。</div></div></div>')

add(ATT, dc.kt("19.4.1.2 另一還原糖法", "Lane-Eynon 滴定") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧪","原理","樣品滴入沸騰鹼性硫酸銅(含酒石酸鉀鈉、甲基藍指示劑)；還原糖把 Cu²⁺ 還原，當 Cu²⁺ 耗盡，指示劑藍色消失","b") +
    dc.card("📏","判讀","以達終點所需<strong>體積</strong>計算還原糖量；AOAC 945.66。反應非計量 → 仍需標準曲線","a") +
    '</div><div class="note" style="margin-top:16px">與 Somogyi-Nelson 同樣基於<strong>Cu(II)→Cu(I)</strong>，差別在「滴定到指示劑變色」而非比色。</div>')

add(ATT, dc.game_sort_inner("g4","小遊戲 ③","膳食纖維流程排序", 6,
    "用 ▲▼ 把 AOAC 991.43 酵素-重量法測膳食纖維的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("19.4.2 個別糖", "HPLC 與 HPAEC-PAD") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧬","HPLC 首選","同時定性(滯留時間)＋定量(峰面積)；快速、精準；除還原糖外也能測糖醇","b") +
    dc.card("⚡","HPAEC-PAD","高 pH 下醣羥基解離，陰離子交換管柱分離；脈衝電化學偵測器(PAD)專一靈敏","a") +
    '</div><div class="note" style="margin-top:16px">HPAEC-PAD 偵測下限約 1.5 ng（單醣）；響應因子逐日變動，需每天跑標準品校正。</div>')

add(ATT, dc.kt("19.4.2.3 酵素法", "專一又靈敏") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧫","GOPOD 測葡萄糖","葡萄糖氧化酶將葡萄糖氧化生成 H₂O₂；過氧化酶＋無色染料 → 顯色定量","b") +
    dc.card("🎯","高度專一","酵素對特定醣高度專一、靈敏、不需高純度樣品、易自動化（套組販售）","g") +
    '</div><div class="note" style="margin-top:16px">應用延伸：澱粉先酵素水解成葡萄糖，再用 GOPOD 測 → 得<strong>總澱粉</strong>。</div>')

add(ATT, dc.kt("19.5.1 澱粉", "總澱粉酵素測定") +
    '<div class="svgwrap" style="margin-top:10px">' + STARCH_SVG + '</div>' +
    '<div class="note" style="margin-top:14px">唯一可靠的總澱粉法：以純化澱粉酶完全水解成<strong>葡萄糖</strong>再定量(GOPOD)。' +
    "酵素須純化以免雜酶釋出非澱粉葡萄糖。<strong>抗性澱粉(RS)</strong>不易完全水解，多歸入膳食纖維。</div>")

add(ATT, dc.kt("19.5.2 植物膠與果膠", "多醣最難測") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🌿","植物膠(hydrocolloids)","結構、溶解度、分子量差異大，<strong>無單一通用法</strong>；多需萃取→去蛋白→乙醇沉澱→水解測組成糖","b") +
    dc.card("🍓","果膠(pectin)","主成分為聚半乳糖醛酸，無官方法；常以<strong>間羥基聯苯-硫酸法</strong>測<strong>糖醛酸</strong>含量間接定量","a") +
    '</div><div class="note" style="margin-top:16px">添加量常僅 0.01–1%，且常為混摻——分離回收必有損失，定量格外困難。</div>')

add(ATT, dc.game_bucket_inner("g3","小遊戲 ④","方法「測什麼」分類", 7,
    "換個角度——這些方法各自測的是哪一類目標？分到三類。"), ' data-game="g3"')

add(ATT, dc.kt("19.6 膳食纖維", "定義決定方法") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>膳食纖維＝小腸<strong>不可消化</strong>的醣類＋木質素等</li>" +
    "<li>除非抗性澱粉外，<strong>所有非澱粉多醣</strong>皆屬纖維</li>" +
    "<li>分<strong>可溶(SDF)</strong>與<strong>不可溶(IDF)</strong>；TDF＝SDF＋IDF</li>" +
    "<li>定義須先取得共識，方法才能照定義測量</li></ul></div>" +
    '<div class="note">難處：纖維除了化學定義，還牽涉<strong>生理效應</strong>（不同來源效果不同）。' +
    "AACC、IOM、Codex、FDA 四套定義略有差異，正持續調和。</div></div>")

add(ATT, dc.kt("19.6.2 纖維方法", "酵素-重量法") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🧪","為何叫「酵素-重量」","用<strong>酵素</strong>(α-澱粉酶、蛋白酶、葡萄糖澱粉酶)移除可消化澱粉與蛋白，再以<strong>重量</strong>秤殘渣","b") +
    dc.card("⚖️","關鍵校正","殘渣須扣除<strong>蛋白(凱氏/Dumas)、灰分(灰化)、空白</strong>，才是真正纖維","a") +
    '</div><div class="note" style="margin-top:16px">最棘手的干擾是<strong>澱粉</strong>：未除盡的可消化澱粉會增加殘渣重，<strong>高估</strong>纖維。</div>')

add(ATT, dc.kt("19.7 物理與光譜法", "快速但只適純樣品") +
    '<div class="grid3" style="margin-top:20px">' +
    dc.card("💧","比重/折射率","以比重計(°Brix)或折射計測糖漿濃度；僅適<strong>單一純物質</strong>(如純蔗糖)","b") +
    dc.card("🔄","旋光度","偏光儀測旋光；可由蔗糖水解前後('轉化')測蔗糖","a") +
    dc.card("📡","FTIR / NIR","快速、非破壞；乳品分析儀測乳糖；NIR 估纖維與糖，需先校正","g") + '</div>' +
    '<div class="note" style="margin-top:16px">物理法快速便宜，但只對<strong>純溶液</strong>準確；光譜法為間接估計值，須建檢量線。</div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對方法", 5), ' data-game="g5"')

# ---------------- 喚起行動 ----------------
add(ACT, dc.cmp_inner("一張表選方法（點欄位排序）",
    [{"k":"m","t":"s","label":"方法"},{"k":"meas","t":"s","label":"測什麼"},
     {"k":"speed","t":"n","label":"速度","star":True},{"k":"app","t":"s","label":"主要應用"}],
    "速度：★ 越多越快。整合自 Table 19.2。", kicker="19.7 方法比較"), ' data-game="cmp"')

add(ACT, dc.chart_inner("fiber", "各食物的<span class='hi'>總膳食纖維</span>", "資料：Table 19.8（AOAC 991.43），g 纖維 / 100 g 食物（濕基）。",
    kicker="19.6 膳食纖維含量", height="52vh"), ' data-chart="fiber"')

add(ACT, dc.kt("方法選擇", "跟著決策樹走") +
    '<div class="svgwrap" style="margin-top:10px">' + DTREE_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:14px">下一頁實戰：算一份早餐穀片的總膳食纖維 →</p>')

add(ACT, dc.kt("19.8 方法演進", "為何<span class='hi'>層析法</span>勝出") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("📉","舊法的痛","顯色/還原糖法：不同糖反應不同，混合醣時尤其麻煩；物理法只適純物質","b") +
    dc.card("📈","層析法的強","HPLC/GC 把混合醣<strong>分離</strong>、以滯留時間<strong>辨識</strong>、再<strong>定量</strong>每一成分","a") +
    '</div><div class="note" style="margin-top:16px">趨勢：舊法漸被層析取代；但因簡單、品管、標準化需求，部分舊法仍續用。澱粉是例外——可用酵素專一測定。</div>')

add(ACT, dc.kt("19.10 計算", "膳食纖維 %：扣空白、蛋白、灰分") +
    '<div class="grid2" style="margin-top:14px"><div class="eq">纖維% = ' +
    '<span class="frac"><b>殘渣 − 蛋白 − 灰分 − 空白</b><span>樣品重</span></span> × 100</div>' +
    '<div><ul class="clean"><li>殘渣含少量殘留蛋白與灰分 → 須扣除</li>' +
    "<li>另扣<strong>試劑空白</strong>(blank)</li>" +
    "<li>結果以<strong>乾基</strong>表示（若樣品已乾燥）</li>" +
    "<li>TDF ＝ IDF ＋ SDF</li></ul></div></div>")

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關",
    "擠壓早餐穀片以 AOAC 991.43 測總纖維：樣品重 1002.8 mg，殘渣 151.9 mg，"
    "殘留蛋白 13.1 mg、灰分 21.1 mg、空白 6.1 mg。求<strong>總膳食纖維 %</strong>。", unit="%"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li><strong>沒有萬用法</strong>——依結構類型(單/寡/多醣)選方法</li>" +
    "<li>前處理：乾燥→脫脂→<strong>熱 80% 乙醇</strong>萃取低分子醣</li>" +
    "<li>總糖<strong>苯酚-硫酸法</strong>；還原糖<strong>Somogyi-Nelson/Lane-Eynon</strong></li></ul>" +
    '<ul class="clean"><li>個別糖看<strong>HPLC/HPAEC-PAD</strong>；澱粉用<strong>酵素→葡萄糖</strong></li>' +
    "<li>膳食纖維<strong>酵素-重量法</strong>：除澱粉/蛋白，秤殘渣扣蛋白灰分空白</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["依分子大小分辨單醣、寡醣、多醣",
     "說明為何用熱 80% 乙醇萃取低分子醣",
     "解釋苯酚-硫酸法測總糖的原理與限制",
     "說明還原糖法 (Somogyi-Nelson) 的化學基礎",
     "說出總澱粉酵素測定的兩種酵素與順序",
     "判斷該用哪種方法（總糖/還原糖/個別糖/纖維）",
     "由殘渣數據算出 % 總膳食纖維"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把碳水化合物分析<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions、Practice Problems<br>"
    "🔜 銜接章節：<strong>蛋白質分析 (Ch18)</strong>、<strong>水分分析 (Ch15)</strong><br>"
    "🧪 思考：你要測總糖、還原糖、個別糖，還是膳食纖維？該選哪種方法？",
    ["苯酚-硫酸法","Somogyi-Nelson","HPLC/PAD","酵素法","膳食纖維"]), ' data-cover="1"')

# ---------------- CFG ----------------
CFG = {
  "charts": {
    "carb": {"type":"bar","yTitle":"% 總碳水化合物",
      "labels":["白糖","蜂蜜","白米(生)","玉米片","白吐司","葡萄乾","馬鈴薯(生)","蘋果","牛奶","雞胸"],
      "datasets":[{"label":"% 總碳水化合物","data":[100,82,79,84,49,79,17,14,4.8,0],"color":"#1f6feb"}]},
    "fiber": {"type":"bar","yTitle":"g 總膳食纖維 / 100 g",
      "labels":["大豆麩","高纖穀片","燕麥麩","大麥","西梅乾","胡蘿蔔","四季豆","葡萄乾","巴西利","杏桃"],
      "datasets":[{"label":"總膳食纖維 (TDF)","data":[67.14,33.73,16.92,12.25,9.29,3.93,2.89,3.13,2.66,1.12],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["單醣 (DP 1)","寡醣 (DP 3–9)","多醣 (DP >9)"],
      "items":[{"t":"葡萄糖","c":"單醣 (DP 1)"},{"t":"果糖","c":"單醣 (DP 1)"},
        {"t":"棉子糖(三醣)","c":"寡醣 (DP 3–9)"},{"t":"水蘇糖(四醣)","c":"寡醣 (DP 3–9)"},
        {"t":"麥芽糊精","c":"寡醣 (DP 3–9)"},
        {"t":"澱粉","c":"多醣 (DP >9)"},{"t":"纖維素","c":"多醣 (DP >9)"}],
      "ok":"🎉 全對！單醣 DP1、寡醣 DP3–9、多醣 DP>9。",
      "tip":"提示：棉子糖/水蘇糖/麥芽糊精是寡醣；澱粉與纖維素是多醣。"},
    "g3": {"cats":["總糖/還原糖","個別糖(專一)","多醣/纖維"],
      "items":[{"t":"苯酚-硫酸法","c":"總糖/還原糖"},{"t":"Somogyi-Nelson","c":"總糖/還原糖"},
        {"t":"Lane-Eynon","c":"總糖/還原糖"},
        {"t":"HPLC/HPAEC-PAD","c":"個別糖(專一)"},{"t":"GOPOD 酵素","c":"個別糖(專一)"},
        {"t":"澱粉酵素法","c":"多醣/纖維"},{"t":"AOAC 纖維重量法","c":"多醣/纖維"}],
      "ok":"🎉 正確！苯酚-硫酸/還原糖法測總量，HPLC/酵素測個別糖，酵素重量法測多醣纖維。",
      "tip":"提示：苯酚-硫酸/Somogyi/Lane-Eynon 測「總量」；HPLC 與 GOPOD 測「特定糖」。"}
  },
  "mcq": {
    "g2":[
      {"q":"營養標示上的「總碳水化合物」通常如何取得？","o":["苯酚-硫酸法直接測","差減法計算","HPLC 測","滴定"],"a":1,
       "e":"總碳水＝總重−(水分+蛋白+脂肪+灰分)，是差減法，非直接測量。"},
      {"q":"前處理為何用熱 80% 乙醇而非水萃取單/寡醣？","o":["乙醇較便宜","低分子醣可溶、多醣與蛋白不溶","水會破壞糖","乙醇可滅菌"],"a":1,
       "e":"低分子醣溶於熱 80% 乙醇，而多醣與蛋白不溶——萃取相當專一。"},
      {"q":"苯酚-硫酸法測總糖時，哪一類醣『不會』顯色？","o":["單醣","糖醇(如山梨醇)","雙醣","多醣"],"a":1,
       "e":"糖醇(alditol)不給陽性反應；幾乎所有單/寡/多醣會顯色。"},
      {"q":"還原糖法(Somogyi-Nelson)的化學基礎是？","o":["蛋白質沉澱","Cu(II)被還原成Cu(I)","脂肪皂化","胜肽鍵吸收"],"a":1,
       "e":"還原糖的醛基把 Cu²⁺ 還原成 Cu⁺，再還原砷鉬酸顯藍色。"}
    ],
    "g5":[
      {"q":"想一次測出混合樣品中「全部醣」的總量，最簡便？","o":["苯酚-硫酸法","HPLC","GC","DSC"],"a":0,
       "e":"苯酚-硫酸法簡單快速，幾乎測所有醣的總糖(需標準曲線)。"},
      {"q":"要同時分離並定量混合物中各個別糖，首選？","o":["苯酚-硫酸法","HPLC/HPAEC-PAD","Lane-Eynon","比重計"],"a":1,
       "e":"HPLC 能分離、定性(滯留時間)又定量(峰面積)，是個別糖首選。"},
      {"q":"要測食品中的『總澱粉』，正確做法是？","o":["苯酚-硫酸法直接測","酵素水解成葡萄糖再測","測比重","測折射率"],"a":1,
       "e":"以 α-澱粉酶+葡萄糖澱粉酶完全水解成葡萄糖，再 GOPOD 定量。"},
      {"q":"測膳食纖維時，最關鍵要先去除哪種干擾物？","o":["可消化澱粉","水分","色素","礦物質"],"a":0,
       "e":"未除盡的可消化澱粉會增加殘渣重、高估纖維，故須酵素水解去除。"},
      {"q":"純糖漿濃度快速現場估計，最簡單的物理法？","o":["折射率(折射計)","HPLC","酵素法","苯酚-硫酸法"],"a":0,
       "e":"折射率/比重對單純純糖溶液可快速估濃度(如°Brix)。"}
    ]
  },
  "sort": {
    "g4":{"steps":["脫脂後加緩衝液，以耐熱 α-澱粉酶糊化並分解澱粉","冷卻至 60°C，加鹼性蛋白酶分解蛋白質",
       "調 pH 4.1–4.8，加葡萄糖澱粉酶完成澱粉水解","加 4 倍體積 95% 乙醇(使乙醇達 78%)沉澱可溶纖維",
       "過濾收集殘渣，依序以 78%/95% 乙醇、丙酮清洗，烘乾秤重","扣除殘留蛋白、灰分與空白 → 得膳食纖維"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！α-澱粉酶→蛋白酶→葡萄糖澱粉酶→乙醇沉澱→過濾烘乾→扣除校正。","tip":"提示：先酵素消化(澱粉酶→蛋白酶→葡萄糖澱粉酶)，再加乙醇沉澱、過濾，最後扣蛋白灰分空白。"}
  },
  "calc": {
    "g6":{"answer":11.13,"tol":0.3,
      "ok":"🎉 正確！(151.9−13.1−21.1−6.1)÷1002.8×100 = 111.6÷1002.8×100 = <b>11.13%</b>（取 2 位有效數字 ≈ 11%）。",
      "bad":"再算算：纖維% =(殘渣−蛋白−灰分−空白)÷樣品重×100 =(151.9−13.1−21.1−6.1)÷1002.8×100。",
      "hint":"提示：分子 = 151.9−13.1−21.1−6.1 = 111.6 mg；÷1002.8 mg ×100 ≈ 11.1%。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"meas"},{"k":"speed"},{"k":"app"}],
    "rows":[
      {"m":"差減法","meas":"總碳水(扣除其他)","speed":5,"app":"營養標示(法定·非實測)"},
      {"m":"苯酚-硫酸法","meas":"總糖(不含糖醇)","speed":4,"app":"總碳水·研究品管"},
      {"m":"Somogyi-Nelson","meas":"還原糖","speed":3,"app":"葡萄糖/麥芽糖/糖漿"},
      {"m":"Lane-Eynon","meas":"還原糖(滴定)","speed":3,"app":"還原糖·產品標準化"},
      {"m":"HPLC/HPAEC-PAD","meas":"個別單/寡醣","speed":3,"app":"個別糖定性定量(首選)"},
      {"m":"酵素法 GOPOD","meas":"特定糖(如葡萄糖)","speed":3,"app":"葡萄糖·蔗糖·乳糖·澱粉"},
      {"m":"澱粉酵素法","meas":"總澱粉","speed":2,"app":"澱粉(水解成葡萄糖)"},
      {"m":"AOAC 纖維重量法","meas":"膳食纖維(IDF/SDF/TDF)","speed":1,"app":"膳食纖維標示(法定)"},
      {"m":"折射率/比重","meas":"溶液固形物濃度","speed":5,"app":"純糖漿快速估濃度"}
    ]
  }
}

dc.build_html(
  {"title":"碳水化合物分析 Carbohydrate Analysis · Nielsen Ch19","brand":"CARBOHYDRATE · CH19"},
  S, CFG, OUT)
