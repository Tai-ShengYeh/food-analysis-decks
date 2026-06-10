# -*- coding: utf-8 -*-
"""Nielsen Ch10 Nuclear Magnetic Resonance (NMR) — SOIL HTML deck.
Uses ../soil_deck_common.py.  Run: python build_ch10.py -> index.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---------------- SVGs ----------------
SPIN_SVG = """
<svg viewBox="0 0 680 300">
 <text x="340" y="20" text-anchor="middle" class="lblb" font-size="15">原子核像小磁鐵：放入磁場後沿 B₀ 排列</text>
 <!-- random cluster -->
 <g stroke="#48597a" stroke-width="2.2" fill="none">
  <g transform="translate(70,150) rotate(20)"><line x1="0" y1="-18" x2="0" y2="18"/><path d="M0 -18 l-5 7 M0 -18 l5 7"/></g>
  <g transform="translate(105,110) rotate(140)"><line x1="0" y1="-18" x2="0" y2="18"/><path d="M0 -18 l-5 7 M0 -18 l5 7"/></g>
  <g transform="translate(120,185) rotate(-70)"><line x1="0" y1="-18" x2="0" y2="18"/><path d="M0 -18 l-5 7 M0 -18 l5 7"/></g>
  <g transform="translate(75,215) rotate(255)"><line x1="0" y1="-18" x2="0" y2="18"/><path d="M0 -18 l-5 7 M0 -18 l5 7"/></g>
  <g transform="translate(140,135) rotate(95)"><line x1="0" y1="-18" x2="0" y2="18"/><path d="M0 -18 l-5 7 M0 -18 l5 7"/></g>
 </g>
 <text x="105" y="255" text-anchor="middle" class="lbl">無磁場：方向雜亂</text>
 <!-- arrow -->
 <line x1="185" y1="160" x2="255" y2="160" stroke="#15233f" stroke-width="3" marker-end="url(#nb)"/>
 <defs><marker id="nb" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#15233f"/></marker></defs>
 <text x="220" y="150" text-anchor="middle" class="lbl">放入 B₀</text>
 <!-- aligned column -->
 <text x="375" y="44" text-anchor="middle" class="lblb" fill="#1f6feb">↑ 平行(低能、稍多)</text>
 <g stroke="#1f6feb" stroke-width="2.4" fill="none">
  <g transform="translate(320,110)"><line x1="0" y1="-16" x2="0" y2="16"/><path d="M0 -16 l-5 7 M0 -16 l5 7"/></g>
  <g transform="translate(360,110)"><line x1="0" y1="-16" x2="0" y2="16"/><path d="M0 -16 l-5 7 M0 -16 l5 7"/></g>
  <g transform="translate(400,110)"><line x1="0" y1="-16" x2="0" y2="16"/><path d="M0 -16 l-5 7 M0 -16 l5 7"/></g>
  <g transform="translate(430,110)"><line x1="0" y1="-16" x2="0" y2="16"/><path d="M0 -16 l-5 7 M0 -16 l5 7"/></g>
 </g>
 <g stroke="#d9822b" stroke-width="2.4" fill="none">
  <g transform="translate(340,210)"><line x1="0" y1="-16" x2="0" y2="16"/><path d="M0 16 l-5 -7 M0 16 l5 -7"/></g>
  <g transform="translate(390,210)"><line x1="0" y1="-16" x2="0" y2="16"/><path d="M0 16 l-5 -7 M0 16 l5 -7"/></g>
 </g>
 <text x="375" y="250" text-anchor="middle" class="lblb" fill="#d9822b">↓ 反平行(高能、稍少)</text>
 <line x1="490" y1="60" x2="490" y2="250" stroke="#8493ad" stroke-width="1.4" stroke-dasharray="4 4"/>
 <!-- net M -->
 <line x1="600" y1="240" x2="600" y2="90" stroke="#1f9d6b" stroke-width="4" marker-end="url(#ng)"/>
 <defs><marker id="ng" markerWidth="10" markerHeight="10" refX="6" refY="8" orient="auto"><path d="M3 0 L6 8 L0 8 Z" fill="#1f9d6b"/></marker></defs>
 <ellipse cx="600" cy="86" rx="34" ry="12" fill="none" stroke="#8493ad" stroke-width="1.6"/>
 <text x="600" y="265" text-anchor="middle" class="lblb" fill="#1f9d6b">淨磁化 M</text>
 <text x="600" y="70" text-anchor="middle" class="lbl">進動(Larmor)</text>
</svg>"""

PULSE_SVG = """
<svg viewBox="0 0 720 260">
 <text x="360" y="18" text-anchor="middle" class="lblb" font-size="15">90° RF 脈衝把磁化倒入 xy 平面，再弛豫放出訊號</text>
 <!-- panel a -->
 <g transform="translate(40,40)">
  <line x1="60" y1="160" x2="60" y2="30" stroke="#48597a" stroke-width="2"/><text x="60" y="22" text-anchor="middle" class="lbl">z</text>
  <line x1="60" y1="160" x2="150" y2="190" stroke="#48597a" stroke-width="2"/><line x1="60" y1="160" x2="0" y2="150" stroke="#48597a" stroke-width="2"/>
  <line x1="60" y1="160" x2="60" y2="60" stroke="#1f9d6b" stroke-width="4" marker-end="url(#pu)"/>
  <text x="60" y="215" text-anchor="middle" class="lblb">平衡：M 沿 B₀</text>
 </g>
 <defs><marker id="pu" markerWidth="10" markerHeight="10" refX="6" refY="8" orient="auto"><path d="M3 0 L6 8 L0 8 Z" fill="#1f9d6b"/></marker>
  <marker id="po" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="#d9822b"/></marker></defs>
 <text x="250" y="130" text-anchor="middle" class="lbl">90°脈衝</text>
 <line x1="215" y1="150" x2="285" y2="150" stroke="#d9822b" stroke-width="3" marker-end="url(#po)"/>
 <!-- panel b -->
 <g transform="translate(300,40)">
  <line x1="60" y1="160" x2="60" y2="30" stroke="#48597a" stroke-width="2"/><text x="60" y="22" text-anchor="middle" class="lbl">z</text>
  <line x1="60" y1="160" x2="150" y2="190" stroke="#48597a" stroke-width="2"/><line x1="60" y1="160" x2="0" y2="150" stroke="#48597a" stroke-width="2"/>
  <line x1="60" y1="160" x2="150" y2="172" stroke="#1f9d6b" stroke-width="4" marker-end="url(#pu)"/>
  <text x="60" y="215" text-anchor="middle" class="lblb">M 倒入 xy 平面(激發)</text>
 </g>
 <text x="540" y="130" text-anchor="middle" class="lbl">弛豫→FID</text>
 <line x1="505" y1="150" x2="575" y2="150" stroke="#d9822b" stroke-width="3" marker-end="url(#po)"/>
 <!-- panel c: receiver coil + signal -->
 <g transform="translate(590,40)">
  <line x1="20" y1="160" x2="20" y2="30" stroke="#48597a" stroke-width="2"/>
  <line x1="20" y1="160" x2="110" y2="190" stroke="#48597a" stroke-width="2"/>
  <path d="M15 95 q10 -10 20 0 q10 10 20 0 q10 -10 20 0" fill="none" stroke="#1f6feb" stroke-width="2.4"/>
  <text x="55" y="215" text-anchor="middle" class="lblb">接收線圈收訊號</text>
 </g>
</svg>"""

SHIFT_SVG = """
<svg viewBox="0 0 680 250">
 <text x="340" y="22" text-anchor="middle" class="lblb" font-size="15">化學位移：電子雲屏蔽程度決定訊號位置</text>
 <!-- spectrum baseline + peaks -->
 <line x1="60" y1="150" x2="620" y2="150" stroke="#15233f" stroke-width="2"/>
 <path d="M150 150 C160 70 180 70 190 150" fill="none" stroke="#1f6feb" stroke-width="2.6"/>
 <path d="M300 150 C308 100 322 100 330 150" fill="none" stroke="#1f6feb" stroke-width="2.6"/>
 <path d="M500 150 C508 60 522 60 530 150" fill="none" stroke="#d9822b" stroke-width="2.6"/>
 <text x="170" y="60" text-anchor="middle" class="lbl">端基質子</text>
 <text x="515" y="50" text-anchor="middle" class="lbl">甲基 CH₃</text>
 <!-- axis arrows -->
 <line x1="620" y1="185" x2="60" y2="185" stroke="#d94f4f" stroke-width="2.6" marker-end="url(#sl)"/>
 <defs><marker id="sl" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#d94f4f"/></marker></defs>
 <text x="120" y="208" class="lblb" fill="#d94f4f">← 去屏蔽 deshielded</text>
 <text x="560" y="208" text-anchor="end" class="lblb" fill="#1f6feb">屏蔽 shielded →</text>
 <text x="120" y="228" class="lbl">downfield · 高 ppm · 近電負性 O</text>
 <text x="560" y="228" text-anchor="end" class="lbl">upfield · 低 ppm · 電子雲厚</text>
</svg>"""

FID_SVG = """
<svg viewBox="0 0 680 250">
 <text x="340" y="20" text-anchor="middle" class="lblb" font-size="15">自由感應衰減 FID（時域）→ 傅立葉轉換 → NMR 光譜（頻域）</text>
 <!-- FID time domain -->
 <line x1="40" y1="120" x2="270" y2="120" stroke="#8493ad" stroke-width="1.4"/>
 <path d="M50 120 Q60 70 70 120 Q80 165 90 120 Q100 80 110 120 Q120 152 130 120
   Q140 90 150 120 Q160 145 170 120 Q180 100 190 120 Q200 138 210 120 Q220 106 230 120 Q240 132 250 120"
   fill="none" stroke="#1f6feb" stroke-width="2.4"/>
 <text x="155" y="200" text-anchor="middle" class="lbl">時間(s) · FID 隨時間衰減</text>
 <!-- FT arrow -->
 <line x1="290" y1="120" x2="360" y2="120" stroke="#15233f" stroke-width="3" marker-end="url(#fb)"/>
 <defs><marker id="fb" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#15233f"/></marker></defs>
 <text x="325" y="108" text-anchor="middle" class="lbl">FT</text>
 <!-- frequency domain peaks -->
 <line x1="390" y1="150" x2="640" y2="150" stroke="#15233f" stroke-width="2"/>
 <path d="M470 150 C480 55 498 55 508 150" fill="none" stroke="#d9822b" stroke-width="2.6"/>
 <path d="M560 150 C568 85 582 85 590 150" fill="none" stroke="#d9822b" stroke-width="2.6"/>
 <text x="515" y="200" text-anchor="middle" class="lbl">頻率(Hz) · 不同質子族群的峰</text>
</svg>"""

SPECTRO_SVG = """
<svg viewBox="0 0 560 320">
 <text x="280" y="20" text-anchor="middle" class="lblb" font-size="15">NMR 光譜儀：超導冷磁鐵 + 探頭 + 控制台 + 工作站</text>
 <!-- magnet dewar -->
 <rect x="70" y="60" width="150" height="210" rx="16" fill="#eef6ff" stroke="#1f6feb" stroke-width="2.6"/>
 <rect x="95" y="60" width="100" height="210" rx="10" fill="#cfe0f6" stroke="#1f6feb" stroke-width="1.6"/>
 <rect x="132" y="44" width="26" height="226" fill="#f6f9fd" stroke="#48597a" stroke-width="1.6"/>
 <text x="145" y="40" text-anchor="middle" class="lbl">樣品入</text>
 <circle cx="145" cy="165" r="9" fill="#d9822b"/>
 <text x="145" y="292" text-anchor="middle" class="lblb">超導磁鐵(液氦 4.2 K)</text>
 <text x="145" y="200" text-anchor="middle" class="lbl">探頭 probe</text>
 <!-- console -->
 <rect x="300" y="120" width="150" height="120" rx="10" fill="#fbeede" stroke="#d9822b" stroke-width="2.4"/>
 <text x="375" y="148" text-anchor="middle" class="lblb">控制台 Console</text>
 <text x="375" y="172" text-anchor="middle" class="lbl">發射器 / 接收器</text>
 <text x="375" y="192" text-anchor="middle" class="lbl">勻場 shim / 控溫</text>
 <line x1="220" y1="170" x2="300" y2="170" stroke="#8493ad" stroke-width="2"/>
 <!-- data station -->
 <rect x="470" y="150" width="70" height="50" rx="6" fill="#15233f"/>
 <text x="505" y="180" text-anchor="middle" fill="#fff" font-size="12" font-weight="800">工作站</text>
 <line x1="450" y1="180" x2="470" y2="180" stroke="#8493ad" stroke-width="2"/>
 <text x="280" y="312" text-anchor="middle" class="lbl">500 MHz 機：¹H 發射器 500 MHz、¹³C 125 MHz(Fig 10.5)</text>
</svg>"""

# ================================================ 引起動機 ================================================
add(MOT, dc.cover("NIELSEN'S FOOD ANALYSIS · CHAPTER 10",
    "核磁<span style='color:var(--accent-2)'>共振</span> NMR", "Nuclear Magnetic Resonance",
    "食品分析　·　3 小時課程　·　含 6 個互動小遊戲<br>自旋 · Larmor · 化學位移 · FID/傅立葉 · T1/T2 · MRI · TD-NMR",
    ["原子核像小磁鐵","500 MHz=11.7 T","化學位移 ppm","FID→傅立葉","30 秒測油脂"]), ' data-cover="1"')

add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">同一種原理，<br>既能解出<span class="hi">完整分子結構</span>，又能 30 秒測出洋芋片的<span class="hi">油脂</span>？</div>
  <p class="subtitle" style="max-width:840px;margin:22px auto 0">答案是 <strong>核磁共振 (NMR)</strong>。<br>
  它「聆聽」原子核在磁場中像小磁鐵般的訊號——非破壞、只需微量樣品，<br>是唯一能給出<strong>完整分子結構</strong>的光譜技術。</p>
  <div style="margin-top:24px"><span class="pill">分子結構解析</span><span class="pill">油脂/水分品管</span>
  <span class="pill">摻假鑑別</span><span class="pill">MRI 成像</span></div></div>""")

add(MOT, dc.kt("10.1 介紹", "NMR 的<span class='hi'>四個</span>特點") +
    '<div class="grid2" style="margin-top:20px">' +
    dc.card("🧬","唯一能定完整結構","其他光譜只能看官能基；只有 NMR 能給出<strong>整個分子的結構</strong>資訊","b") +
    dc.card("🪶","非破壞·微量","毫克甚至微克即可，量完樣品不受損","g") +
    dc.card("💧","液態與固態皆可","可追蹤同一分子在系統中的變化(如水果熟成 固→液)","a") +
    dc.card("⚙️","品管主力","成本大降後，廣用於<strong>油脂、水分、蛋白</strong>例行分析","b") + '</div>')

add(MOT, dc.kt("10.2.1 原理", "原子核像<span class='hi'>小磁鐵</span>") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + SPIN_SVG + '</div><div><ul class="clean">' +
    "<li>有自旋的原子核帶電、自轉→產生磁場，像小磁鐵</li>" +
    "<li>常分析、自旋 <strong>I = 1/2</strong> 的核：<strong>¹H、¹³C、¹⁹F、³¹P</strong>(本章聚焦質子 ¹H)</li>" +
    "<li>放入強外加磁場 <strong>B₀</strong>：自旋只能<strong>平行</strong>或<strong>反平行</strong></li>" +
    "<li>平行能量低、族群稍多→產生可測的<strong>淨磁化 M</strong></li>" +
    '</ul></div></div>')

add(MOT, dc.kt("10.2.1 Larmor 頻率", "為什麼叫「<span class='hi'>500 MHz</span> 核磁儀」") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li>核在磁場中以特定頻率<strong>進動(precession)</strong>，即 <strong>Larmor 頻率</strong></li>" +
    "<li>Larmor 頻率<strong>正比於磁場強度 B₀</strong></li>" +
    "<li>質子 ¹H 在 <strong>11.7 T</strong> 的 Larmor 頻率 = <strong>500 MHz</strong></li>" +
    "<li>所以這台就稱為「500 MHz NMR」——磁場越強、頻率越高、解析越好</li>" +
    '</ul></div><div class="eq">f<sub>Larmor</sub> ∝ B₀<br>' +
    '<span style="font-size:.72em;color:var(--ink-2)">11.7 T → 500 MHz　·　14.1 T → 600 MHz</span></div></div>')

add(MOT, dc.chart_inner("field", "磁場越強，<span class='hi'>共振頻率</span>越高",
    "¹H 共振頻率與磁場強度成正比(示意對應)：常見機型 300/400/500/600/800/1000 MHz 對應磁場 7–23.5 T。",
    kicker="10.2.1 頻率 ∝ 磁場"), ' data-chart="field"')

add(MOT, dc.game_bucket_inner("g1","小遊戲 ①","自旋取向：平行 vs 反平行", 8,
    "把 8 個敘述分到「平行 B₀(低能態)」或「反平行 B₀(高能態)」。"), ' data-game="g1"')

# ================================================ 維持注意 ================================================
add(ATT, dc.kt("10.2.2 RF 脈衝", "用一個 <span class='hi'>90° 脈衝</span>敲一下") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + PULSE_SVG + '</div><div><ul class="clean">' +
    "<li>現代 NMR 用一個短 <strong>RF 脈衝</strong>同時激發一整段頻率(像敲鐘)</li>" +
    "<li><strong>90° 脈衝</strong>把淨磁化向量倒入 <strong>xy 平面</strong>，接收線圈就在那裡</li>" +
    "<li>脈衝後核相干進動、放出 RF 訊號被偵測</li>" +
    "<li>複雜的<strong>脈衝序列</strong>是 2-D NMR 解結構的關鍵</li>" +
    '</ul></div></div>')

add(ATT, dc.kt("10.2.2 弛豫", "脈衝後怎麼回到平衡：T1 與 T2") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("🔁","T1 自旋-晶格弛豫","激發態核與周圍「晶格」交換能量，磁化沿 z 軸<strong>回復</strong>","b") +
    dc.card("🌀","T2 自旋-自旋弛豫","鄰近核互相影響使<strong>相位散開</strong>、xy 訊號衰減","a") +
    '</div><div class="note" style="margin-top:16px">關鍵：<strong>不同型態(液態 vs 固態)弛豫速率不同</strong>。' +
    "這正是 NMR 能分辨水分活動度、固/液脂、玻璃轉化的物理基礎。</div>")

add(ATT, dc.game_mcq_inner("g2","小遊戲 ②","NMR 原理即時測驗", 5), ' data-game="g2"')

add(ATT, dc.kt("10.2.3 化學位移與屏蔽", "電子雲決定訊號<span class='hi'>落在哪</span>") +
    '<div class="grid2-1" style="margin-top:8px"><div class="svgwrap">' + SHIFT_SVG + '</div><div><ul class="clean">' +
    "<li>核周圍<strong>電子雲</strong>會產生反向小磁場，把核<strong>屏蔽</strong>起來</li>" +
    "<li>屏蔽多→訊號在<strong>右側(upfield)、低 ppm</strong></li>" +
    "<li>靠近電負性原子(如 O)→電子被拉走→<strong>去屏蔽→左側(downfield)、高 ppm</strong></li>" +
    "<li>化學位移以 <strong>ppm</strong> 表示，反映該質子的化學環境</li>" +
    '</ul></div></div>')

add(ATT, dc.game_bucket_inner("g3","小遊戲 ③","屏蔽 vs 去屏蔽", 8,
    "把 8 個敘述分到「屏蔽 shielded」或「去屏蔽 deshielded」。"), ' data-game="g3"')

add(ATT, dc.kt("10.2.4 一維 NMR 實驗", "從脈衝到光譜：FID → 傅立葉") +
    '<div class="svgwrap" style="margin-top:6px">' + FID_SVG + '</div>' +
    '<div class="note" style="margin-top:12px">樣品溶於<strong>氘化溶劑(D₂O)</strong>避免被溶劑質子蓋過；90° 脈衝後收到隨時間衰減的 ' +
    "<strong>FID(時域)</strong>，再做<strong>傅立葉轉換</strong>變成頻域光譜。各峰<strong>積分面積</strong>正比於質子數→可定量。</div>")

add(ATT, dc.chart_inner("scans", "多掃幾次：<span class='hi'>訊雜比</span>的代價",
    "訊雜比 S/N 與掃描次數的平方根成正比(S/N ∝ √n)。掃描×4 才能讓 S/N×2——解析度換來的是時間。",
    kicker="10.2.4 訊號平均", height="50vh"), ' data-chart="scans"')

add(ATT, dc.game_sort_inner("g4","小遊戲 ④","一維 NMR 流程排序", 6,
    "用 ▲▼ 把一維 ¹H-NMR 實驗的 6 個步驟排成正確順序。"), ' data-game="g4"')

add(ATT, dc.kt("10.2.5 耦合與 2-D NMR", "鄰近核會<span class='hi'>互相分裂</span>訊號") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>耦合(coupling)</strong>：鄰近核透過共價鍵電子互相影響，使峰<strong>分裂</strong>(以 Hz 計)</li>" +
    "<li>分裂程度與核的<strong>距離與幾何</strong>有關(trans 耦合 > cis)→透露分子幾何</li>" +
    "<li><strong>2-D NMR</strong>＝一系列一維實驗，圖上的<strong>交叉峰(cross peaks)</strong>顯示耦合關聯</li>" +
    '</ul></div><div class="note"><strong>為什麼要 2-D？</strong><br>' +
    "複雜分子的一維峰會重疊；2-D 把 ¹H、¹³C 的關聯攤開，才能逐一指認原子、定出完整結構。</div></div>")

add(ATT, dc.kt("10.3 儀器", "NMR 光譜儀的<span class='hi'>四大部分</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + SPECTRO_SVG + '</div>' +
    '<div style="margin-top:8px"><span class="pill">超導冷磁鐵(液氦4.2K/液氮)</span><span class="pill">磁鐵孔 + 探頭(勻場線圈)</span>'
    '<span class="pill">控制台(發射/接收/控溫)</span><span class="pill">資料工作站</span></div>')

add(ATT, dc.game_mcq_inner("g5","小遊戲 ⑤","決策挑戰：選對 NMR 技術", 5), ' data-game="g5"')

# ================================================ 喚起行動 ================================================
add(ACT, dc.cmp_inner("一張表看 NMR 的各種型態（點欄位排序）",
    [{"k":"m","t":"s","label":"技術"},{"k":"depth","t":"n","label":"資訊深度","star":True},
     {"k":"sample","t":"s","label":"樣品型態"},{"k":"cost","t":"n","label":"成本","star":True},{"k":"app","t":"s","label":"代表應用"}],
    "資訊深度／成本 ★ 越多越高。整合自 10.3–10.4。", kicker="10.4 技術比較"), ' data-game="cmp"')

add(ACT, dc.kt("10.4 應用總覽", "NMR 在食品的<span class='hi'>用途地圖</span>") +
    '<div class="grid2" style="margin-top:18px">' +
    dc.card("🧪","結構與純度","碳水化合物結構、β-葡聚醣 1,3/1,4 鍵結比、增稠劑鑑定(2-D)","b") +
    dc.card("🛢️","油脂","脂肪酸組成(¹H 積分)、油品真偽、氧化追蹤、固體脂含量 SFC","a") +
    dc.card("💧","水分與狀態","水分活動度 T2、玻璃轉化 Tg(NMR 狀態圖)","g") +
    dc.card("🍊","成像 MRI","完整水果/包裝成像：凍傷、種子、水分遷移、結凍過程","b") + '</div>')

add(ACT, dc.kt("10.4.1 液態 vs 固態 vs MRI", "同一原理，三種玩法") +
    '<div class="grid3" style="margin-top:18px">' +
    dc.card("💧","液態 NMR","溶於氘溶劑、訊號窄、解析高；純度與結構分析","b") +
    dc.card("🧱","固態 NMR","訊號寬→用<strong>魔角旋轉 MAS / CP-MAS</strong>變窄；測澱粉、細胞壁、產地","a") +
    dc.card("🍊","MRI","原樣成像、2-D/3-D；柑橘凍傷與種子偵測(Fig 10.7)","g") + '</div>' +
    '<p class="subtitle" style="margin-top:16px">液態看「溶得開的純樣」、固態看「粉末與組織」、MRI 看「完整樣品的空間影像」。</p>')

add(ACT, dc.kt("10.4.1.5 TD-NMR", "30 秒測出<span class='hi'>油脂與水分</span>") +
    '<div class="grid2" style="margin-top:16px"><div><ul class="clean">' +
    "<li><strong>時域(TD)/低解析 NMR</strong>：桌上型、無需冷媒、便宜易用</li>" +
    "<li>對應 <strong>AOAC 2008.06</strong>(肉品水分與脂肪)</li>" +
    "<li>結合微波快乾的 <strong>ORACLE™</strong>：脂肪 0.05–100%，約 <strong>30 秒</strong>完成</li>" +
    "<li>用於冰淇淋、雞肉香腸、牛肉、油凝膠等品管</li>" +
    '</ul></div><div class="note"><strong>高解析 vs 低解析：</strong><br>' +
    "高解析(超導磁鐵)給<strong>結構</strong>；低解析 TD-NMR 不給結構，但<strong>快、穩、便宜</strong>，" +
    "靠 T1/T2 弛豫差異算<strong>含量</strong>(固/液脂、水分)。</div></div>")

add(ACT, dc.kt("10.4.2 摻假與品質", "NMR 指紋＋化學計量學") +
    '<div class="grid3" style="margin-top:18px">' +
    dc.card("🫒","橄欖油真偽","以 ¹³C/¹H NMR 結合多變量分析，揪出榛果油摻假、辨品種與產地","a") +
    dc.card("🧃","果汁摻假","¹H NMR + PCA 區分葡萄柚汁摻入、鮮榨 vs 果渣回洗柳橙汁","b") +
    dc.card("🍺","啤酒批次","以乳酸、丙酮酸、酪胺酸等分辨不同生產地的品質一致性","g") + '</div>')

add(ACT, dc.game_calc_inner("g6","小遊戲 ⑥","計算闖關：Larmor 頻率",
    "Larmor(共振)頻率與磁場強度<b>成正比</b>。已知 ¹H 在 <b>11.7 T</b> 為 <b>500 MHz</b>。"
    "求 ¹H 在 <b>14.1 T</b> 超導磁鐵中的共振頻率。", unit="MHz"), ' data-game="g6"')

add(ACT, dc.kt("重點整理", "今天的五個關鍵") +
    '<div class="grid2" style="margin-top:18px"><ul class="clean">' +
    "<li>NMR 聽<strong>原子核(¹H 等 I=1/2)</strong>在磁場中的訊號；唯一能定完整結構</li>" +
    "<li>Larmor 頻率<strong>正比於磁場</strong>(11.7 T→500 MHz)</li>" +
    "<li><strong>90° 脈衝</strong>→ FID(時域)→<strong>傅立葉</strong>→光譜；積分可定量</li></ul>" +
    '<ul class="clean"><li><strong>化學位移</strong>：屏蔽=低 ppm(右)、去屏蔽=高 ppm(左)</li>' +
    "<li>應用：油脂/水分(<strong>TD-NMR 30 秒</strong>)、摻假鑑別、<strong>MRI</strong> 成像</li></ul></div>")

add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明 NMR 為何能定出完整分子結構、有哪些常用核",
     "解釋原子核在 B₀ 中的平行/反平行與淨磁化 M",
     "說明 Larmor 頻率與磁場的關係(為何叫 500 MHz 機)",
     "描述 90° 脈衝、FID 與傅立葉轉換的角色",
     "區分屏蔽與去屏蔽、upfield 與 downfield、ppm 高低",
     "比較 T1 與 T2 弛豫，並說明對食品分析的意義",
     "說出高解析 NMR、TD-NMR、MRI、固態 NMR 各自的用途",
     "用『頻率∝磁場』換算不同磁場下的共振頻率"]))

add(ACT, dc.cover("下一步 · NEXT",
    "把核磁共振<br><span style='color:var(--accent-2)'>用起來</span>", "",
    "📌 課後練習：Study Questions(自旋、化學位移、FID、儀器組件、應用)<br>"
    "🔜 銜接章節：<strong>油脂 (Ch17)</strong>、<strong>水分 (Ch15)</strong>、<strong>質譜 (Ch11)</strong>、<strong>玻璃轉化 (Ch30)</strong><br>"
    "🧪 思考：你要的是『分子結構』還是『含量』？需要成像嗎？該選高解析 NMR、TD-NMR 還是 MRI？",
    ["NMR","化學位移","FID/傅立葉","TD-NMR","MRI"]), ' data-cover="1"')

# ================================================ CFG ================================================
CFG = {
  "charts": {
    "field": {"type":"line","yTitle":"¹H 共振頻率 (MHz)",
      "labels":["7.05 T","9.4 T","11.7 T","14.1 T","18.8 T","23.5 T"],
      "datasets":[{"label":"¹H 頻率","data":[300,400,500,600,800,1000],"color":"#1f6feb"}]},
    "scans": {"type":"line","yTitle":"相對訊雜比 S/N (∝√n)",
      "labels":["16 次","64 次","256 次","1024 次"],
      "datasets":[{"label":"相對 S/N","data":[4,8,16,32],"color":"#d9822b"}]}
  },
  "bucket": {
    "g1": {"cats":["平行 B₀ (低能態)","反平行 B₀ (高能態)"],
      "items":[{"t":"能量較低、較穩定","c":"平行 B₀ (低能態)"},
        {"t":"兩取向中族群數目『稍多』","c":"平行 B₀ (低能態)"},
        {"t":"自旋方向與外加磁場 B₀ 相同","c":"平行 B₀ (低能態)"},
        {"t":"淨磁化 M 的來源(過剩的這群)","c":"平行 B₀ (低能態)"},
        {"t":"能量較高","c":"反平行 B₀ (高能態)"},
        {"t":"族群數目稍少","c":"反平行 B₀ (高能態)"},
        {"t":"自旋方向與 B₀ 相反","c":"反平行 B₀ (高能態)"},
        {"t":"受 RF 脈衝激發後部分核躍遷到此態","c":"反平行 B₀ (高能態)"}],
      "ok":"🎉 全對！平行＝低能、族群稍多、產生淨磁化 M；反平行＝高能、稍少。",
      "tip":"提示：與 B₀ 同向→低能、稍多→平行；反向→高能、稍少→反平行。"},
    "g3": {"cats":["屏蔽 shielded","去屏蔽 deshielded"],
      "items":[{"t":"電子雲密度高、把核遮住","c":"屏蔽 shielded"},
        {"t":"訊號出現在右側 (upfield)","c":"屏蔽 shielded"},
        {"t":"化學位移較小(低 ppm)","c":"屏蔽 shielded"},
        {"t":"如 6-去氧糖的甲基 CH₃ 質子","c":"屏蔽 shielded"},
        {"t":"靠近電負性原子(如 O)","c":"去屏蔽 deshielded"},
        {"t":"訊號出現在左側 (downfield)","c":"去屏蔽 deshielded"},
        {"t":"化學位移較大(高 ppm)","c":"去屏蔽 deshielded"},
        {"t":"如糖的端基異構(anomeric)質子","c":"去屏蔽 deshielded"}],
      "ok":"🎉 正確！屏蔽=電子雲厚、右側、低 ppm；去屏蔽=近電負性原子、左側、高 ppm。",
      "tip":"提示：電子雲厚、遠離 O→屏蔽(右/低 ppm)；靠近 O→去屏蔽(左/高 ppm)。"}
  },
  "mcq": {
    "g2":[
      {"q":"NMR 光譜法研究的對象是？","o":["分子的振動","原子核(在磁場中的自旋)","價電子躍遷","離子的質荷比"],"a":1,
       "e":"NMR 量測的是原子核在外加磁場中的自旋行為，這點與多數光譜法不同。"},
      {"q":"下列何者是最常分析、自旋 I=1/2 的核？","o":["¹²C","¹⁶O","¹H(質子)","³²S"],"a":2,
       "e":"¹H、¹³C、¹⁹F、³¹P 自旋皆為 1/2；本章聚焦最常見的質子 ¹H。"},
      {"q":"「500 MHz NMR」指的是？","o":["磁場為 500 特斯拉","¹H 在該磁場的共振頻率為 500 MHz","每秒掃描 500 次","解析度 500 ppm"],"a":1,
       "e":"¹H 在 11.7 T 的 Larmor 頻率為 500 MHz，故稱 500 MHz 核磁儀。"},
      {"q":"90° RF 脈衝的主要作用是？","o":["把樣品加熱","把淨磁化向量倒入 xy 平面","讓核游離","降低磁場"],"a":1,
       "e":"90° 脈衝把磁化從 z 軸倒入 xy 平面(接收線圈所在)，訊號最大。"},
      {"q":"T1 與 T2 分別稱為？","o":["縱向與橫向頻率","自旋-晶格 與 自旋-自旋 弛豫","屏蔽與去屏蔽","耦合與分裂"],"a":1,
       "e":"T1＝自旋-晶格弛豫(沿 z 回復)；T2＝自旋-自旋弛豫(相位散開)。"}
    ],
    "g5":[
      {"q":"要快速(約 30 秒)測肉品的油脂與水分含量做品管，選？","o":["高解析 2-D NMR","TD-NMR(低解析時域)","MRI","固態 CP-MAS"],"a":1,
       "e":"TD-NMR 桌上型、便宜快速，靠 T1/T2 弛豫算含量(對應 AOAC 2008.06)。"},
      {"q":"要解析複雜分子、指認每個原子得到完整結構，選？","o":["TD-NMR","低場弛豫儀","高解析 2-D NMR","MRI"],"a":2,
       "e":"高解析 2-D NMR 把 ¹H/¹³C 關聯攤開，才能定出完整分子結構。"},
      {"q":"要對完整水果成像、看內部凍傷或種子，選？","o":["MRI","液態 NMR","TD-NMR","火焰光度計"],"a":0,
       "e":"MRI 可對原樣做空間成像，例如柑橘凍傷與種子偵測。"},
      {"q":"固態粉末樣品訊號太寬，怎麼讓譜線變窄？","o":["稀釋","魔角旋轉 MAS","升高溫度","換氘溶劑"],"a":1,
       "e":"固態各向異性使訊號寬；以魔角旋轉(MAS，常配 CP)大幅變窄。"},
      {"q":"要追蹤食品中水分子的活動度與玻璃轉化，較適合？","o":["MRI 影像","弛豫(T2)/NMR 狀態圖","高解析 2-D NMR","氫化物生成法"],"a":1,
       "e":"T2 弛豫反映質子活動度；NMR 狀態圖可關聯水分與玻璃轉化 Tg。"}
    ]
  },
  "sort": {
    "g4":{"steps":["樣品溶於氘化溶劑(D₂O)、裝入 NMR 管放進磁鐵","核在 B₀ 中沿 z 軸對齊(平衡態)",
       "施加 90° RF 脈衝，把磁化倒入 xy 平面","接收線圈收到衰減訊號→自由感應衰減 FID(時域)",
       "對 FID 做傅立葉轉換→得到頻域 NMR 光譜","多次掃描相加、積分各峰→改善訊雜比並定量"],
       "shuffle":[2,4,0,5,1,3],
       "ok":"🎉 順序正確！溶樣放磁鐵→平衡→90°脈衝→收 FID→傅立葉→相加積分。",
       "tip":"提示：先有平衡態才打脈衝；先得時域 FID 才能傅立葉成頻域光譜。"}
  },
  "calc": {
    "g6":{"answer":602.6,"tol":12,
      "ok":"🎉 正確！f ∝ B₀：500 × (14.1 / 11.7) ≈ <b>603 MHz</b>(即俗稱的 600 MHz 機)。",
      "bad":"再算算：頻率與磁場成正比，f₂ = 500 × (14.1 / 11.7)。",
      "hint":"提示：f₂ = 500 × (14.1 / 11.7) = 500 × 1.205 ≈ 603 MHz。"}
  },
  "cmp": {
    "cols":[{"k":"m"},{"k":"depth","t":"n","star":True},{"k":"sample"},{"k":"cost","t":"n","star":True},{"k":"app"}],
    "rows":[
      {"m":"高解析 1D/2D NMR","depth":5,"sample":"溶液(氘溶劑)","cost":5,"app":"完整分子結構·摻假鑑別"},
      {"m":"TD-NMR(低解析)","depth":1,"sample":"原樣(液/固)","cost":1,"app":"30 秒測油脂/水分·SFC"},
      {"m":"MRI","depth":3,"sample":"完整樣品","cost":5,"app":"成像凍傷/種子/水分遷移"},
      {"m":"固態 CP-MAS","depth":4,"sample":"粉末/組織","cost":4,"app":"澱粉/細胞壁結構·產地"},
      {"m":"弛豫 relaxometry","depth":2,"sample":"原樣","cost":2,"app":"水分活動度 T2·玻璃轉化"}
    ]
  }
}

dc.build_html(
  {"title":"核磁共振 NMR · Nielsen Ch10","brand":"NMR · CH10"},
  S, CFG, OUT)
