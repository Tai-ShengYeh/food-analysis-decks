# -*- coding: utf-8 -*-
"""Nielsen Ch9 Atomic Absorption / Emission Spectroscopy & ICP-MS — SOIL HTML deck.
Uses ../soil_deck_common.py.  Run: python build_ch9.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
EMISSION_SVG = """
<svg viewBox="0 0 660 318">
 <text x="330" y="20" text-anchor="middle" class="lblb" font-size="15">每個元素都有獨特的發射譜線「指紋」</text>
 <g>
  <!-- Na -->
  <text x="118" y="62" text-anchor="end" class="lblb">鈉 Na</text>
  <rect x="132" y="42" width="450" height="30" fill="#111"/>
  <rect x="498" y="42" width="6" height="30" fill="#ffd23f"/><rect x="506" y="42" width="4" height="30" fill="#ffd23f"/>
  <rect x="300" y="42" width="2" height="30" fill="#5a6cff" opacity=".7"/>
  <!-- Ca -->
  <text x="118" y="112" text-anchor="end" class="lblb">鈣 Ca</text>
  <rect x="132" y="92" width="450" height="30" fill="#111"/>
  <rect x="520" y="92" width="5" height="30" fill="#ff7a3c"/><rect x="250" y="92" width="3" height="30" fill="#4aa3ff"/>
  <rect x="232" y="92" width="3" height="30" fill="#7e57ff"/>
  <!-- Cu -->
  <text x="118" y="162" text-anchor="end" class="lblb">銅 Cu</text>
  <rect x="132" y="142" width="450" height="30" fill="#111"/>
  <rect x="360" y="142" width="4" height="30" fill="#46c46a"/><rect x="330" y="142" width="3" height="30" fill="#46c46a"/>
  <rect x="300" y="142" width="3" height="30" fill="#4aa3ff"/>
  <!-- Sr -->
  <text x="118" y="212" text-anchor="end" class="lblb">鍶 Sr</text>
  <rect x="132" y="192" width="450" height="30" fill="#111"/>
  <rect x="540" y="192" width="6" height="30" fill="#ff5a5a"/><rect x="512" y="192" width="4" height="30" fill="#ff5a5a"/>
  <rect x="470" y="192" width="3" height="30" fill="#ff8a3c"/>
  <!-- Ba -->
  <text x="118" y="262" text-anchor="end" class="lblb">鋇 Ba</text>
  <rect x="132" y="242" width="450" height="30" fill="#111"/>
  <rect x="340" y="242" width="4" height="30" fill="#46c46a"/><rect x="312" y="242" width="3" height="30" fill="#7ed957"/>
  <rect x="380" y="242" width="3" height="30" fill="#ffd23f"/><rect x="430" y="242" width="3" height="30" fill="#ff8a3c"/>
 </g>
 <text x="132" y="300" class="lbl">← 短波長 (藍/紫)</text>
 <text x="582" y="300" text-anchor="end" class="lbl">長波長 (紅) →</text>
</svg>"""

AAS_SVG = """
<svg viewBox="0 0 980 240">
 <defs><marker id="ah" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
   <path d="M0 0 L7 3 L0 6 Z" fill="#d9822b"/></marker></defs>
 <!-- light beam -->
 <line x1="120" y1="96" x2="880" y2="96" stroke="#d9822b" stroke-width="3" marker-end="url(#ah)" opacity=".85"/>
 <!-- HCL source -->
 <rect x="20" y="68" width="110" height="56" rx="9" fill="#e7f0fe" stroke="#1f6feb" stroke-width="2.4"/>
 <text x="75" y="92" text-anchor="middle" class="lblb">空心陰極燈</text>
 <text x="75" y="111" text-anchor="middle" class="lbl">HCL 光源</text>
 <!-- chopper -->
 <circle cx="178" cy="96" r="20" fill="#fff" stroke="#48597a" stroke-width="2.2"/>
 <path d="M178 96 L178 76 A20 20 0 0 1 195 106 Z" fill="#48597a"/>
 <text x="178" y="140" text-anchor="middle" class="lbl">斬光器</text>
 <!-- atomizer/flame -->
 <rect x="250" y="70" width="130" height="52" rx="9" fill="#fbeede" stroke="#d9822b" stroke-width="2.4"/>
 <path d="M300 70 q6 -22 12 0 M318 70 q6 -22 12 0" fill="none" stroke="#d94f4f" stroke-width="2.6"/>
 <text x="315" y="96" text-anchor="middle" class="lblb">火焰 / 石墨爐</text>
 <text x="315" y="113" text-anchor="middle" class="lbl">原子化器</text>
 <!-- monochromator -->
 <rect x="470" y="70" width="130" height="52" rx="9" fill="#eef6ff" stroke="#1f6feb" stroke-width="2.4"/>
 <text x="535" y="92" text-anchor="middle" class="lblb">單色器</text>
 <text x="535" y="111" text-anchor="middle" class="lbl">選定波長</text>
 <!-- detector -->
 <rect x="690" y="70" width="120" height="52" rx="9" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.4"/>
 <text x="750" y="92" text-anchor="middle" class="lblb">偵測器</text>
 <text x="750" y="111" text-anchor="middle" class="lbl">PMT</text>
 <!-- readout -->
 <rect x="858" y="74" width="104" height="44" rx="8" fill="#15233f"/>
 <text x="910" y="101" text-anchor="middle" fill="#fff" font-weight="800" font-size="13">讀出</text>
 <!-- zone labels -->
 <g font-size="13">
  <line x1="20" y1="170" x2="215" y2="170" stroke="#8493ad" stroke-width="1.5"/>
  <text x="118" y="190" text-anchor="middle" class="lblb" fill="#1f6feb">光源</text>
  <line x1="240" y1="170" x2="395" y2="170" stroke="#8493ad" stroke-width="1.5"/>
  <text x="318" y="190" text-anchor="middle" class="lblb" fill="#d9822b">樣品池</text>
  <line x1="460" y1="170" x2="962" y2="170" stroke="#8493ad" stroke-width="1.5"/>
  <text x="711" y="190" text-anchor="middle" class="lblb" fill="#1f9d6b">光的測量</text>
 </g>
 <text x="490" y="222" text-anchor="middle" class="lbl">雙光束原子吸收光譜儀 (Fig 9.3)：光源放出元素專屬波長 → 被原子化的樣品吸收 → 測剩餘光強</text>
</svg>"""

HCL_SVG = """
<svg viewBox="0 0 440 240">
 <!-- glass envelope -->
 <rect x="40" y="60" width="300" height="120" rx="60" fill="#eef6ff" stroke="#1f6feb" stroke-width="2.6"/>
 <!-- cathode cup -->
 <path d="M120 95 q-26 25 0 50 l26 -8 q-14 -17 0 -34 Z" fill="#d9822b" opacity=".85"/>
 <text x="118" y="200" text-anchor="middle" class="lblb">陰極 (待測元素)</text>
 <!-- anode -->
 <line x1="210" y1="80" x2="210" y2="120" stroke="#48597a" stroke-width="4"/>
 <circle cx="210" cy="120" r="5" fill="#48597a"/>
 <text x="232" y="80" class="lbl">陽極(鎢)</text>
 <!-- Ar gas dots -->
 <g fill="#7e57ff" opacity=".6">
  <circle cx="175" cy="110" r="3"/><circle cx="195" cy="140" r="3"/><circle cx="240" cy="100" r="3"/>
  <circle cx="265" cy="150" r="3"/><circle cx="225" cy="160" r="3"/><circle cx="285" cy="115" r="3"/></g>
 <text x="300" y="170" text-anchor="middle" class="lbl">Ar / Ne 填充氣</text>
 <!-- window + beam -->
 <rect x="338" y="108" width="16" height="24" fill="#cfe0f6" stroke="#1f6feb" stroke-width="2"/>
 <line x1="354" y1="120" x2="420" y2="120" stroke="#d9822b" stroke-width="3.4" marker-end="url(#ah2)"/>
 <defs><marker id="ah2" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
   <path d="M0 0 L7 3 L0 6 Z" fill="#d9822b"/></marker></defs>
 <text x="388" y="110" text-anchor="middle" class="lbl">專屬譜線</text>
 <text x="220" y="36" text-anchor="middle" class="lblb" font-size="15">空心陰極燈 HCL：陰極用哪種元素，就放出哪種元素的光</text>
</svg>"""

ICP_SVG = """
<svg viewBox="0 0 380 340">
 <text x="190" y="22" text-anchor="middle" class="lblb" font-size="15">感應耦合電漿 (ICP) 焰炬</text>
 <!-- quartz tubes -->
 <rect x="150" y="90" width="80" height="190" rx="10" fill="#f6f9fd" stroke="#48597a" stroke-width="2"/>
 <rect x="166" y="90" width="48" height="190" rx="8" fill="#eef6ff" stroke="#1f6feb" stroke-width="1.6"/>
 <!-- plasma -->
 <path d="M190 60 C 150 110, 158 170, 190 210 C 222 170, 230 110, 190 60 Z"
   fill="url(#pg)" stroke="#d9822b" stroke-width="2"/>
 <ellipse cx="190" cy="150" rx="16" ry="40" fill="#d94f4f" opacity=".75"/>
 <defs><linearGradient id="pg" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#cfe0f6"/><stop offset="1" stop-color="#7eb6ff"/></linearGradient></defs>
 <!-- load coil -->
 <g stroke="#d9822b" stroke-width="5" fill="none">
  <path d="M150 240 q40 -14 80 0"/><path d="M150 256 q40 -14 80 0"/><path d="M150 272 q40 -14 80 0"/></g>
 <text x="262" y="262" class="lbl">RF 負載線圈</text>
 <text x="262" y="278" class="lbl">(27/40 MHz)</text>
 <!-- argon arrows -->
 <line x1="190" y1="320" x2="190" y2="282" stroke="#1f9d6b" stroke-width="3" marker-end="url(#ah3)"/>
 <defs><marker id="ah3" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
   <path d="M0 0 L7 3 L0 6 Z" fill="#1f9d6b"/></marker></defs>
 <text x="190" y="335" text-anchor="middle" class="lbl">氬氣 + 樣品氣溶膠</text>
 <!-- temps -->
 <text x="118" y="96" text-anchor="end" class="lblb" fill="#d94f4f">~10000 K</text>
 <text x="280" y="150" class="lblb" fill="#1f6feb">6000–7000 K</text>
 <text x="280" y="168" class="lbl">(分析激發區)</text>
</svg>"""

ATOM_SVG = """
<svg viewBox="0 0 380 360">
 <defs><marker id="au" markerWidth="10" markerHeight="10" refX="4" refY="8" orient="auto">
   <path d="M4 0 L8 8 L0 8 Z" fill="#1f6feb"/></marker></defs>
 <line x1="70" y1="330" x2="70" y2="40" stroke="#1f6feb" stroke-width="3" marker-end="url(#au)"/>
 <g font-size="13">
  <rect x="92" y="300" width="220" height="40" rx="8" fill="#f6f9fd" stroke="#48597a" stroke-width="1.8"/>
  <text x="202" y="318" text-anchor="middle" class="lblb">溶液 M(H₂O)ₘⁿ⁺ , X⁻</text>
  <text x="202" y="334" text-anchor="middle" class="lbl">霧化進入火焰/電漿</text>
  <rect x="92" y="244" width="220" height="40" rx="8" fill="#eef6ff" stroke="#1f6feb" stroke-width="1.8"/>
  <text x="202" y="262" text-anchor="middle" class="lblb">固態鹽 (MX)ₙ</text>
  <text x="202" y="278" text-anchor="middle" class="lbl">去溶劑 desolvation</text>
  <rect x="92" y="188" width="220" height="40" rx="8" fill="#fbeede" stroke="#d9822b" stroke-width="1.8"/>
  <text x="202" y="206" text-anchor="middle" class="lblb">氣態分子 MX</text>
  <text x="202" y="222" text-anchor="middle" class="lbl">汽化 vaporization</text>
  <rect x="92" y="132" width="220" height="40" rx="8" fill="#e3f6ee" stroke="#1f9d6b" stroke-width="2.2"/>
  <text x="202" y="150" text-anchor="middle" class="lblb">自由原子 M ⭐</text>
  <text x="202" y="166" text-anchor="middle" class="lbl">原子化 → 在此測 AAS/AES</text>
  <rect x="92" y="60" width="220" height="40" rx="8" fill="#fbe7e7" stroke="#d94f4f" stroke-width="1.8"/>
  <text x="202" y="78" text-anchor="middle" class="lblb">離子 M⁺</text>
  <text x="202" y="94" text-anchor="middle" class="lbl">游離 ionization (過熱→干擾)</text>
 </g>
 <text x="40" y="36" class="lbl">能量↑</text>
</svg>"""

POLY_TABLE = """
<table class="cmp" style="margin-top:8px">
 <thead><tr><th>多原子離子</th><th>m/z</th><th>受干擾的元素</th></tr></thead>
 <tbody>
  <tr><td class="c">³⁸Ar¹H⁺</td><td>39</td><td>³⁹K⁺ (鉀)</td></tr>
  <tr><td class="c">⁴⁰Ar¹²C⁺</td><td>52</td><td>⁵²Cr⁺ (鉻)</td></tr>
  <tr><td class="c">⁴⁰Ar¹⁶O⁺</td><td>56</td><td>⁵⁶Fe⁺ (鐵)</td></tr>
  <tr><td class="c">⁴⁰Ar³⁵Cl⁺</td><td>75</td><td>⁷⁵As⁺ (砷)</td></tr>
  <tr><td class="c">⁴⁰Ar⁴⁰Ar⁺</td><td>80</td><td>⁸⁰Se⁺ (硒)</td></tr>
 </tbody>
</table>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 9",
    "原子<span style='color:var(--accent-2)'>光譜</span>分析", "Atomic Absorption · Emission · ICP-MS",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>AAS · AES · 火焰 / 石墨爐 · ICP-OES · ICP-MS · 礦物元素",
    ["空心陰極燈","氬電漿 10000K","ppt 偵測","同位素","礦物分析"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">食物燒成灰之後，<br>怎麼知道裡面有多少<span class="hi">鈣、鐵、鉛</span>？</div>
  <p class="subtitle" style="max-width:820px;margin:22px auto 0">灰分(Ch16)只告訴你「總礦物量」。<br>
  要分出<strong>單一元素</strong>的含量，得靠每個元素獨一無二的<strong>「光指紋」</strong>——原子光譜法。</p>
  <div style="margin-top:24px"><span class="pill">營養礦物 Ca·Fe·Zn</span><span class="pill">毒性重金屬 Pb·Cd·As·Hg</span>
  <span class="pill">產地溯源</span><span class="pill">品質與標示</span></div></div>""")

add(MOT, dc.kt("9.1 介紹", "兩種互補的原子光譜：<span class='hi'>吸收</span>與<span class='hi'>發射</span>") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("⬇️","原子吸收 AAS","自由中性原子<strong>吸收</strong>元素專屬波長的光；測吸收量。需要外部光源(空心陰極燈)。","b") +
    dc.card("⬆️","原子發射 AES","受激發的原子落回基態時<strong>放出</strong>專屬波長的光；測發射量。光源就是原子本身。","a") +
    '</div><div class="note" style="margin-top:16px"><strong>共同關鍵：</strong>每個元素的吸收/發射譜線都<strong>獨一無二</strong>，' +
    "所以即使在複雜食品基質中，也能專一辨識特定元素。</div>")

add(MOT, dc.kt("9.1 元素的指紋", "為什麼能「認出」每個元素") +
    '<div class="svgwrap" style="margin-top:6px">' + EMISSION_SVG + '</div>' +
    '<p class="subtitle" style="text-align:center;margin-top:10px">不同元素的電子能階不同 → 吸收/發射的波長組合各異，' +
    "如同條碼般可逐一辨識(Fig 9.1)。</p>")

add(MOT, dc.kt("9.1 為什麼重要", "原子光譜在食品上的<span class='hi'>四個任務</span>") +
    '<div class="grid2" style="margin-top:20px">' +
    dc.card("🥛","營養礦物","定量 Ca、Fe、Zn、K、Mg…——營養標示與品質的核心","g") +
    dc.card("☠️","毒性重金屬","Pb、Cd、As、Hg 常需 ppb–ppt 級偵測，攸關食安","a") +
    dc.card("🌍","產地溯源","以元素/同位素指紋追蹤食品的地理來源","b") +
    dc.card("🏷️","規格與品質","強化食品(如鐵強化麵粉)是否達標、是否摻假","b") + '</div>')

add(MOT, dc.kt("9.1 核心概念", "原子化：把樣品變成<span class='hi'>自由原子</span>") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + ATOM_SVG + '</div><div><ul class="clean">' +
    "<li>食品中元素多以<strong>化合物</strong>存在，必須先變成<strong>自由中性原子</strong>才能做原子光譜</li>" +
    "<li>溶液 → <strong>去溶劑</strong> → <strong>汽化</strong> → <strong>原子化</strong>(自由原子)</li>" +
    "<li>原子吸收測<strong>原子</strong>不測離子；溫度過高造成<strong>游離</strong>反而是干擾</li>" +
    '</ul><div class="note" style="margin-top:12px">能量來源決定溫度：火焰、石墨爐(電熱)、氬電漿。' +
    "溫度越高，原子化越完全(但也更易游離)。</div></div></div>")

add(MOT, dc.chart_inner("temp", "不同原子化方式的<span class='hi'>溫度</span>",
    "整合自 Table 9.1：火焰 2000–3400 K、電熱 1500–3300 K、ICP 6000–7000 K。電漿溫度遠高於火焰，原子化更完全、干擾更少。",
    kicker="9.1 原子化溫度"), ' data-chart="temp"')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","吸收 vs 發射：分特徵", 8,
    "把 8 個敘述分到「原子吸收 AAS」或「原子發射 AES」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("9.2 原子吸收光譜 AAS", "Alan Walsh 1952：用<span class='hi'>吸收</span>定量") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>原理：氣態<strong>自由中性原子</strong>吸收 UV-Vis(200–800 nm)的<strong>專屬波長</strong></li>" +
    "<li>吸光度由<strong>比爾定律</strong>與原子濃度成正比 → 配標準曲線定量</li>" +
    "<li>火焰式一次只能測<strong>一個元素</strong>，且每元素要換一支燈</li>" +
    "<li>測不到磷(P)等<strong>非金屬</strong>(吸收落在真空紫外，需真空)</li>" +
    '</ul></div><div class="note"><strong>兩種原子化：</strong>火焰原子化(穩定易用) 與 ' +
    "電熱(石墨爐)原子化(偵測極限更低、樣品更少)。雖被 ICP 取代於商業，仍是大學教學主力。</div></div>")

add(ATT, dc.kt("9.2.1 / 9.2.2 原子化", "火焰 vs 石墨爐") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("🔥","火焰原子化","樣品<strong>霧化</strong>進火焰(空氣-乙炔/笑氣-乙炔)；穩定、易用，但靈敏度較低、樣品停留短","a") +
    dc.card("🧯","石墨爐(電熱)","樣品(0.5–100 µL)注入石墨管，分階段加熱→蒸乾→灰化→2000–3000 K 原子化","b") +
    '</div><div class="grid2" style="margin-top:14px">' +
    dc.card("✅","石墨爐優點","偵測極限更低、所需樣品更少","g") +
    dc.card("⚠️","石墨爐代價","設備貴、通量低、基質干擾大、精密度較差","a") + '</div>')

add(ATT, dc.kt("9.2.3 儀器", "原子吸收光譜儀的<span class='hi'>五大組件</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + AAS_SVG + '</div>' +
    '<div style="margin-top:10px"><span class="pill">① 光源 HCL/EDL</span><span class="pill">② 原子化器</span>' +
    '<span class="pill">③ 單色器 200–800 nm</span><span class="pill">④ 偵測器 PMT</span><span class="pill">⑤ 讀出裝置</span></div>')

add(ATT, dc.kt("9.2.3.1 光源", "空心陰極燈 HCL：元素專屬的光") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + HCL_SVG + '</div><div><ul class="clean">' +
    "<li>陰極由<strong>待測元素</strong>製成，通電後放出該元素的<strong>專屬譜線</strong></li>" +
    "<li>所以每種元素需要<strong>一支對應的燈</strong>(約 60 種元素有商用 HCL)</li>" +
    "<li><strong>斬光器</strong>把燈光調變成交流訊號，扣掉火焰自身的連續發射</li>" +
    "<li>揮發性元素(As、Hg、Cd)可用<strong>無電極放電燈 EDL</strong></li>" +
    '</ul></div></div>')

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","AAS 原理即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("9.2.3.2 原子化器細節", "火焰類型與兩種增敏技術") +
    '<div class="grid3" style="margin-top:18px">' +
    dc.card("🔵","氧化焰","貧燃(過氧)、最熱、藍色清晰","b") +
    dc.card("🟡","還原焰","富燃(過燃料)、較冷、黃色","a") +
    dc.card("⚪","化學計量焰","燃料與助燃恰好完全燃燒","g") + '</div>' +
    '<div class="grid2" style="margin-top:14px">' +
    dc.card("💧","冷蒸氣法 (Hg)","汞可在室溫以自由原子存在；用 SnCl₂ 還原成元素汞，直接送入吸收池——汞分析首選","b") +
    dc.card("🫧","氫化物生成法","As、Pb、Sn、Sb、Se… 生成揮發性氫化物後導入，靈敏度大增","a") + '</div>')

add(ATT, dc.kt("9.2.4 安全", "乙炔是<span class='hi'>爆炸性</span>氣體") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("💥","為什麼危險","空氣-乙炔、笑氣-乙炔是最常用燃料；乙炔可爆，需良好通風","a") +
    dc.card("🚫","鐵律","火焰 AAS <strong>運轉中絕不可無人看管</strong>；排氣口應在燃燒頭正上方","b") +
    '</div><div class="note" style="margin-top:18px">操作前務必詳閱儀器商 SOP；避免未燃燃料堆積與有毒煙霧。</div>')

add(ATT, dc.kt("9.2.5 干擾", "兩大類：<span class='hi'>光譜性</span>與<span class='hi'>非光譜性</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🌈","光譜性干擾","其他元素/分子在待測波長附近<strong>吸收或放光</strong>。例：Fe 213.856 與 Zn 213.859 nm 重疊；鹼土氧化物背景吸收。用氘燈、Zeeman 校正","b") +
    dc.card("⚗️","非光譜性干擾","影響<strong>原子化效率或游離</strong>。含輸送、溶質揮發(磷酸鈣)、化學(難熔氧化物)、游離干擾","a") +
    '</div><div class="note" style="margin-top:14px"><strong>實例：</strong>牛奶測鈣時，磷酸鹽與鈣生成焦磷酸鈣壓低訊號→加<strong>鑭(La)</strong>當釋放劑；' +
    "鹼金屬易游離→加 K/Cs 當<strong>游離抑制劑</strong>。</div>")

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","干擾分類：光譜 vs 非光譜", 6,
    "把 6 種干擾現象分到「光譜性干擾」或「非光譜性干擾」。"), ' data-game="g3"')

add(ATT, dc.kt("9.3 原子發射 AES / ICP-OES", "氬電漿：又熱又穩的多元素利器") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + ICP_SVG + '</div><div><ul class="clean">' +
    "<li>AES 不需外部光源——<strong>被激發的原子本身發光</strong>(火焰光度計即屬此類)</li>" +
    "<li><strong>ICP-OES</strong>：氬電漿由 RF 線圈感應加熱，溫度可達 ~10000 K，分析激發 6000–7000 K</li>" +
    "<li>低氧環境→<strong>氧化物少、化學干擾少</strong>；可<strong>同時測多元素</strong>(可達 70 種)</li>" +
    "<li>線性範圍寬達 <strong>6 個數量級</strong></li>" +
    '</ul></div></div>')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","原子化流程排序", 6,
    "用 ▲▼ 把樣品「從溶液到離子」的 6 個階段排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("9.5 ICP-MS", "不測光，改測<span class='hi'>離子的質荷比</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>Houk 等(1980)：把氬電漿當成<strong>離子源</strong>接上質譜儀</li>" +
    "<li>依離子的<strong>質荷比 m/z</strong> 分離、計數——偵測極限可達 <strong>ppt</strong></li>" +
    "<li>能分辨<strong>同位素</strong>(同元素不同質量)，可做產地溯源</li>" +
    "<li>取樣錐 + 截取錐 + 離子透鏡把離子導入四極桿</li>" +
    '</ul></div><div class="note"><strong>三技術的定位：</strong><br>AAS 便宜、單元素、教學；<br>' +
    "ICP-OES 多元素、高通量、商業例行；<br>ICP-MS 超痕量、同位素、最佳偵測極限(也最貴)。</div></div>")

add(ATT, dc.kt("9.5.2 ICP-MS 干擾", "同質量重疊：<span class='hi'>多原子</span>干擾") +
    '<div class="grid2-1" style="margin-top:12px"><div>' + POLY_TABLE +
    '<p class="cap" style="text-align:left">Table 9.2：氬與酸中元素結合成多原子離子，質量恰與待測元素相同。</p></div>' +
    '<div><ul class="clean">' +
    "<li><strong>同質異位素干擾</strong>：⁵⁸Fe 與 ⁵⁸Ni 重疊→改選 ⁵⁶Fe、⁶⁰Ni</li>" +
    "<li><strong>雙電荷干擾</strong>：¹³⁸Ba²⁺ 出現在 m/z 69，干擾 ⁶⁹Ga</li>" +
    "<li><strong>多原子干擾</strong>：如 ⁴⁰Ar¹⁶O⁺ 干擾 ⁵⁶Fe⁺</li>" +
    "<li>對策：<strong>碰撞/反應池(CRC)</strong>、高解析磁場式 ICP-MS</li>" +
    '</ul></div></div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對技術", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("一張表選技術（點欄位排序）",
    [{"k":"m","t":"s","label":"技術"},{"k":"power","t":"n","label":"偵測力","star":True},
     {"k":"multi","t":"s","label":"多元素"},{"k":"range","t":"n","label":"工作範圍(數量級)"},
     {"k":"cost","t":"s","label":"成本"},{"k":"iso","t":"s","label":"同位素"}],
    "偵測力 ★ 越多越靈敏；工作範圍為線性數量級。整合自 Table 9.3。", kicker="9.6 方法比較"), ' data-game="cmp"')

add(ACT, dc.chart_inner("range", "四技術的<span class='hi'>線性工作範圍</span>",
    "整合自 Table 9.3：數量級越大，可量測的濃度跨距越廣。ICP-MS 最寬(9–10)，火焰 AAS 最窄。",
    kicker="9.6 工作範圍", height="52vh"), ' data-chart="range"')

add(ACT, dc.kt("9.6 偵測極限", "差距可達<span class='hi'>百萬倍</span>") +
    '<div class="grid2" style="margin-top:16px">' +
    dc.card("🪙","鉛 Pb (µg/L)","火焰AAS <b>15</b> → 石墨爐 <b>0.05</b> → ICP-OES <b>1.3</b> → ICP-MS <b>0.00001</b>","b") +
    dc.card("🔬","鎘 Cd (µg/L)","火焰AAS <b>0.8</b> → 石墨爐 <b>0.002</b> → ICP-OES <b>0.1</b> → ICP-MS <b>0.00009</b>","a") +
    '</div><div class="note" style="margin-top:16px">整合自 Table 9.4。測<strong>超痕量毒性重金屬</strong>時，' +
    "ICP-MS 的偵測極限比火焰 AAS 好上數個數量級——這正是它最大的價值。</div>")

add(ACT, dc.kt("9.4 應用與實務", "從樣品到可靠數字") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>多數食品須先<strong>灰化(乾式/濕式)</strong>破壞有機物，再溶於稀酸(連回 Ch16)</li>" +
    "<li>液態油品可直接溶於有機溶劑後吸入火焰，免灰化</li>" +
    "<li>定量靠<strong>標準品做校正曲線</strong>；以<strong>標準參考物質(SRM)</strong>查核準確度</li>" +
    '</ul></div><div class="note"><strong>痕量分析的紀律：</strong><br>' +
    "用高純度試劑與去離子水；每批帶<strong>試劑空白</strong>；玻璃器皿酸洗(1 N HCl 浸泡)再以去離子水沖洗。</div></div>")

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：標準曲線回推",
    "鐵的標準曲線為 <b>A = 0.1006 × C + 0.0005</b>(C 單位 mg/L)。某強化麵粉消化液的校正吸光度 "
    "<b>A = 0.270</b>。求鐵濃度 <b>C</b>。", unit="mg/L"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li><strong>AAS 測吸收、AES 測發射</strong>；每元素譜線獨一無二</li>" +
    "<li>AAS 需<strong>元素專屬 HCL</strong>，火焰式一次一元素</li>" +
    "<li>原子化序：溶液→去溶劑→汽化→<strong>原子化</strong>→(過熱)游離</li></ul>" +
    '<ul class="clean"><li><strong>ICP-OES</strong> 氬電漿、多元素、寬線性、高通量</li>' +
    "<li><strong>ICP-MS</strong> 測 m/z、ppt 偵測、可分同位素(最貴)</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明 AAS 與 AES 的差別(吸收 vs 發射)",
     "解釋空心陰極燈為何要用待測元素、為何一元素一支燈",
     "依序說出原子化的各階段，並指出哪一步測訊號",
     "比較火焰與石墨爐原子化的優缺點",
     "區分光譜性與非光譜性干擾，並各舉一例",
     "說明 ICP-OES 與 ICP-MS 的原理與各自定位",
     "依需求(預算/元素數/偵測極限/同位素)選對技術",
     "用標準曲線從吸光度回推元素濃度"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把原子光譜<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions、Practice Problems(鐵強化麵粉、嬰兒配方 Ca/K/Na)<br>"
    "🔜 銜接章節：<strong>灰分前處理 (Ch16)</strong>、<strong>礦物質分析 (Ch21)</strong>、<strong>質譜 (Ch11)</strong><br>"
    "🧪 思考：你的樣品要測哪些元素？需要多痕量？要不要同位素？該選 AAS、ICP-OES 還是 ICP-MS？",
    ["AAS","ICP-OES","ICP-MS","偵測極限","礦物分析"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "temp": {"type":"bar","yTitle":"原子化溫度 (K)",
      "labels":["火焰","石墨爐(電熱)","ICP 電漿"],
      "datasets":[{"label":"典型溫度 K","data":[2700,2400,6500],"color":"#d9822b"}]},
    "range": {"type":"bar","yTitle":"線性工作範圍(數量級)",
      "labels":["火焰 AAS","石墨爐 AAS","ICP-OES","ICP-MS"],
      "datasets":[{"label":"數量級","data":[3.5,2,6.5,9.5],"color":"#1f6feb"}]}
  },
  "bucket": {
    "g1": {"cats":["原子吸收 AAS","原子發射 AES"],
      "items":[{"t":"用空心陰極燈(HCL)當外部光源","c":"原子吸收 AAS"},
        {"t":"測量光被吸收而減少的量","c":"原子吸收 AAS"},
        {"t":"Alan Walsh 於 1952 年提出","c":"原子吸收 AAS"},
        {"t":"每種元素需換一支專屬燈","c":"原子吸收 AAS"},
        {"t":"光源就是被激發的樣品原子本身","c":"原子發射 AES"},
        {"t":"測量原子落回基態放出的光","c":"原子發射 AES"},
        {"t":"火焰或氬電漿就是輻射來源","c":"原子發射 AES"},
        {"t":"ICP-OES、火焰光度計屬於此類","c":"原子發射 AES"}],
      "ok":"🎉 全對！AAS 靠外部 HCL 測吸收、一元素一支燈；AES 由原子自身發光、可多元素。",
      "tip":"提示：要外部光源、測『吸收』→ AAS；原子自己發光、測『發射』→ AES。"},
    "g3": {"cats":["光譜性干擾","非光譜性干擾"],
      "items":[{"t":"Fe 213.856 與 Zn 213.859 nm 譜線重疊","c":"光譜性干擾"},
        {"t":"氧化鈣等鹼土分子譜帶造成背景吸收","c":"光譜性干擾"},
        {"t":"<250 nm 有機分子未燒盡造成背景吸收","c":"光譜性干擾"},
        {"t":"樣品黏度/表面張力改變霧化輸送速率","c":"非光譜性干擾"},
        {"t":"磷酸鹽與鈣形成難分解的焦磷酸鈣","c":"非光譜性干擾"},
        {"t":"高溫火焰使分析原子游離 M⇌M⁺+e⁻","c":"非光譜性干擾"}],
      "ok":"🎉 正確！光譜性＝波長重疊/背景吸收；非光譜性＝影響原子化或游離。",
      "tip":"提示：跟『波長/背景光』有關→光譜性；跟『霧化、化學反應、游離』有關→非光譜性。"}
  },
  "mcq": {
    "g2":[
      {"q":"AAS 測量的物理量是？","o":["激發態原子放出的光","自由中性原子對專屬波長的吸收","離子的質荷比","分子的振動"],"a":1,
       "e":"AAS 測氣態自由中性原子吸收元素專屬波長(200–800 nm)的光。"},
      {"q":"空心陰極燈(HCL)的陰極為何要用『待測元素』製成？","o":["降低成本","才能放出該元素專屬的譜線","提高火焰溫度","防止游離"],"a":1,
       "e":"陰極用待測元素，放出的正是該元素能吸收的專屬波長；故每元素需各自的燈。"},
      {"q":"為什麼火焰 AAS 通常測不到磷(P)等非金屬？","o":["濃度太低","其吸收落在真空紫外、需真空","會立刻游離","沒有對應的燈"],"a":1,
       "e":"P 等非金屬吸收在真空紫外區，一般 AAS 無真空環境，故做不到。"},
      {"q":"石墨爐(電熱式)相較火焰式 AAS 的主要優點是？","o":["更便宜","偵測極限更低、所需樣品更少","通量更高","可測同位素"],"a":1,
       "e":"石墨爐偵測極限更低、樣品量更少；代價是較貴、通量低、基質干擾大。"},
      {"q":"火焰 AAS 常用且具爆炸性、操作中不可離人的氣體是？","o":["氬氣","乙炔(acetylene)","氮氣","二氧化碳"],"a":1,
       "e":"乙炔是常用燃料且具爆炸性；火焰 AAS 運轉中絕不可無人看管。"}
    ],
    "g5":[
      {"q":"要追溯橄欖油的地理來源、需要同位素比值資訊，選哪種？","o":["火焰 AAS","ICP-OES","ICP-MS","石墨爐 AAS"],"a":2,
       "e":"只有 ICP-MS 能提供同位素資訊，最適合產地溯源。"},
      {"q":"商業實驗室要對大量樣品一次測定多種礦物、追求高通量，最划算？","o":["火焰 AAS","ICP-OES","逐元素石墨爐 AAS","逐元素換 HCL"],"a":1,
       "e":"ICP-OES 一次可測多元素(可達 70)、線性寬，適合高通量例行分析。"},
      {"q":"大學教學實驗室、預算有限，只要測鈉鉀鈣，較適合？","o":["ICP-MS","火焰 AAS / 火焰光度計","高解析 ICP-MS","磁場式 ICP-MS"],"a":1,
       "e":"火焰 AAS / 火焰光度計便宜、易用，最適合教學與鹼/鹼土金屬。"},
      {"q":"要分析超痕量重金屬鎘(ppt 級)，偵測極限最佳的是？","o":["火焰 AAS","ICP-OES","ICP-MS","火焰光度計"],"a":2,
       "e":"ICP-MS 偵測極限可達 ppt，最適合超痕量毒性重金屬。"},
      {"q":"用 AAS 測牛奶中的鈣，磷酸鹽造成干擾，最佳對策？","o":["升高火焰溫度","加入鑭(La)當釋放劑","稀釋十倍","換更亮的燈"],"a":1,
       "e":"磷酸鹽與鈣生成焦磷酸鈣造成化學干擾；加鑭(La)優先結合磷酸鹽，釋放出鈣。"}
    ]
  },
  "sort": {
    "g4":{"steps":["樣品溶液被霧化成細霧，進入火焰/電漿","去溶劑：溶劑蒸發，留下乾的固態鹽粒",
       "汽化：固態鹽受熱變成氣態分子","原子化：氣態分子解離成自由中性原子",
       "激發/吸收：原子吸收(AAS)或被激發後發射(AES)專屬波長","游離：過熱時原子失去電子成為離子(干擾)"],
       "shuffle":[3,0,5,1,4,2],
       "ok":"🎉 順序正確！霧化→去溶劑→汽化→原子化→測訊號→(過熱)游離。",
       "tip":"提示：先變乾(去溶劑)、再變氣(汽化)、才拆成原子(原子化)；訊號在『自由原子』階段測得。"}
  },
  "calc": {
    "g6":{"answer":2.68,"tol":0.06,
      "ok":"🎉 正確！C = (0.270 − 0.0005) / 0.1006 = 0.2695 / 0.1006 ≈ <b>2.68 mg/L</b>。",
      "bad":"再算算：把 A=0.270 代入 A = 0.1006C + 0.0005，解出 C。",
      "hint":"提示：C = (A − 0.0005) / 0.1006 = (0.270 − 0.0005) / 0.1006 ≈ 2.68 mg/L。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"power","t":"n","star":True},{"k":"multi"},{"k":"range","t":"n"},{"k":"cost"},{"k":"iso"}],
    "rows":[
      {"m":"火焰 AAS","power":2,"multi":"單一","range":3.5,"cost":"低","iso":"✗"},
      {"m":"石墨爐 AAS","power":3,"multi":"單一","range":2,"cost":"低–中","iso":"✗"},
      {"m":"ICP-OES","power":3,"multi":"多(可達70)","range":6.5,"cost":"中","iso":"✗"},
      {"m":"ICP-MS","power":5,"multi":"多","range":9.5,"cost":"高","iso":"✓"}
    ]
  }
}

dc.build_html(
  {"title":"原子光譜分析 AAS·AES·ICP-MS · Nielsen Ch9","brand":"ATOMIC · CH9"},
  S, CFG, OUT)
