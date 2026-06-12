# -*- coding: utf-8 -*-
"""茶葉中多重元素檢驗方法 (TFDAF0032.00) — SOIL HTML teaching deck.
Reuses ../soil_deck_common.py engine, re-skinned to a dark "tea-green + gold" theme.
AI hero images (FLUX) are base64-embedded; technical diagrams are inline dark SVG.
Run:  python build_tea.py   ->   index.html
"""
import os, sys, io, base64
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "generated")
OUT = os.path.join(HERE, "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"

# 互動 PCA 切換用：讀 dataset/ 由 tea_origin_pca_demo.py 匯出的真實計算得分（PC1×PC2，四種元素子集）
try:
    with open(os.path.join(HERE, "dataset", "pca_scores.json"), encoding="utf-8") as _f:
        PCA_SCORES_JSON = _f.read().strip() or "{}"
except Exception:
    PCA_SCORES_JSON = "{}"

# ============================================================ DARK TEA-GREEN SKIN
# Appended AFTER the light CSS so later :root wins (DRY: same class names reused).
DARK = r"""
/* ===== DARK TEA-GREEN SKIN (overrides light academic) ===== */
:root{
  --bg:#0e1512;--surface:#1a241e;--surface-2:#13201a;
  --ink:#ecf4ea;--ink-2:#b6c8b4;--ink-3:#83977f;--line:#2b3c32;
  --accent:#5fd07f;--accent-soft:rgba(95,208,127,.13);
  --accent-2:#e7ad4d;--accent-2-soft:rgba(231,173,77,.15);
  --ok:#5fd07f;--ok-soft:rgba(95,208,127,.14);--bad:#ef7373;--bad-soft:rgba(239,115,115,.16);--warn:#e7ad4d;
  --shadow:0 16px 44px rgba(0,0,0,.5);--shadow-sm:0 5px 18px rgba(0,0,0,.4)}
body{background:
  radial-gradient(900px 600px at 88% -10%,rgba(231,173,77,.07),transparent 60%),
  radial-gradient(900px 620px at 4% 110%,rgba(95,208,127,.07),transparent 60%),
  var(--bg)}
.cover{background:
  radial-gradient(1100px 560px at 82% 16%,rgba(231,173,77,.17),transparent 60%),
  radial-gradient(880px 520px at 8% 94%,rgba(95,208,127,.16),transparent 55%),
  linear-gradient(135deg,#0f1714,#13211a 55%,#0c1310)}
.note{color:var(--ink)}
.lbl{fill:var(--ink-2)}.lblb{fill:var(--ink)}
table.cmp tbody tr:hover{background:rgba(95,208,127,.07)}
table.cmp thead th{color:var(--accent)}
/* full-bleed image slides */
.slide[data-full]{padding:0}
.slide[data-full] .slide-inner{max-width:none;width:100%;height:100%;position:relative}
.fullimg{position:absolute;inset:0;overflow:hidden}
.fullimg>img{width:100%;height:100%;object-fit:cover;display:block}
.fullimg .scrim{position:absolute;inset:0}
.fullimg .ovl{position:absolute;z-index:3;left:8%;right:8%;max-width:880px}
/* image cards used inside grid2 */
.imgcard{border-radius:18px;overflow:hidden;border:1px solid var(--line);box-shadow:var(--shadow);
  position:relative;background:var(--surface-2)}
.imgcard>img{width:100%;display:block;object-fit:cover;aspect-ratio:1/1}
.imgcard .cn{position:absolute;left:12px;top:12px;z-index:2}
.imgph{display:flex;align-items:center;justify-content:center;aspect-ratio:1/1;color:var(--ink-3);
  font-size:.9rem;border:1px dashed var(--line);border-radius:18px}
/* misc */
.grid5{display:grid;grid-template-columns:repeat(5,1fr);gap:13px}
.dnums{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}
.dnum{background:var(--surface);border:1px solid var(--line);border-top:3px solid var(--accent-2);
  border-radius:14px;padding:14px 16px;box-shadow:var(--shadow-sm)}
.dnum .v{font-family:"JetBrains Mono",monospace;font-weight:800;color:var(--accent);font-size:clamp(1.05rem,1.9vw,1.45rem)}
.dnum .k{color:var(--ink-2);font-size:.84rem;margin-top:5px;line-height:1.4}
.tbl{width:100%;border-collapse:collapse;font-size:clamp(.84rem,1.25vw,1.05rem)}
.tbl th,.tbl td{padding:11px 14px;border-bottom:1px solid var(--line);text-align:center}
.tbl thead th{color:var(--accent-2);font-weight:800;border-bottom:2px solid var(--accent-2)}
.tbl td.c{color:var(--accent);font-weight:800;font-family:"JetBrains Mono",monospace}
.minicard{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:13px 15px}
.minicard .mt{font-weight:800;color:var(--ink);font-size:clamp(.92rem,1.4vw,1.08rem);margin-bottom:4px}
.minicard .mb{color:var(--ink-2);font-size:clamp(.8rem,1.15vw,.95rem);line-height:1.5}
.minicard.b{border-top:3px solid var(--accent)}.minicard.a{border-top:3px solid var(--accent-2)}
/* two-line table header (term + small unit); keeps columns narrow so grid2 stays balanced */
.tbl th .u{display:block;font-weight:600;color:var(--ink-3);font-size:.8em;margin-top:3px;font-family:"JetBrains Mono",monospace}
/* compact sortable element table (slide 5) */
table.cmp{font-size:clamp(.8rem,1.12vw,.96rem)}
table.cmp th,table.cmp td{padding:6px 14px}
.slide[data-game="cmp"]{padding-top:44px;padding-bottom:40px}
"""
dc.CSS = dc.CSS + DARK
# Safe single-substring patch: make Chart.js axis/label/grid colors readable on dark.
dc.JS = dc.JS.replace(
    "Chart.defaults.color='#48597a';",
    "Chart.defaults.color='#b6c8b4';Chart.defaults.borderColor='rgba(255,255,255,.12)';")

# ============================================================ image embedding
def img_uri(key, full=False):
    p = os.path.join(GEN, key + ".jpg")
    if not os.path.exists(p):
        return None
    try:
        from PIL import Image
        im = Image.open(p).convert("RGB")
        w, h = im.size
        tw = 1280 if full else 920
        if w > tw:
            im = im.resize((tw, int(h * tw / w)), Image.LANCZOS)
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=80, optimize=True)
        raw = buf.getvalue()
    except Exception:
        with open(p, "rb") as f:
            raw = f.read()
    return "data:image/jpeg;base64," + base64.b64encode(raw).decode()

IMG_COVER = img_uri("cover", full=True)
IMG_FINGER = img_uri("fingerprint")
IMG_ICPMS = img_uri("icpms")
IMG_CLOSE = img_uri("closing", full=True)

def imgcard(uri, badge, alt):
    if not uri:
        return '<div class="imgcard"><div class="imgph">（AI 圖生成中，重跑 build 即內嵌）</div></div>'
    return '<div class="imgcard"><span class="tag cn">%s</span><img alt="%s" src="%s"></div>' % (badge, alt, uri)

def fullbleed(uri, ovl_html, scrim, ovl_pos):
    if uri:
        return ('<div class="fullimg"><img alt="" src="%s">'
                '<div class="scrim" style="%s"></div>'
                '<div class="ovl" style="%s">%s</div></div>') % (uri, scrim, ovl_pos, ovl_html)
    return '<div class="cover">%s</div>' % ovl_html

# ============================================================ dark SVG diagrams
SVG_PREP = r"""
<svg viewBox="0 0 680 226">
 <defs><marker id="apa" markerWidth="10" markerHeight="10" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#6f8472"/></marker></defs>
 <!-- 1 quartering -->
 <rect x="24" y="50" width="100" height="100" rx="6" fill="#13201a" stroke="#5fd07f" stroke-width="2"/>
 <rect x="24" y="50" width="50" height="50" fill="rgba(95,208,127,.34)"/>
 <rect x="74" y="100" width="50" height="50" fill="rgba(95,208,127,.34)"/>
 <line x1="74" y1="50" x2="74" y2="150" stroke="#2b3c32" stroke-width="1.4"/>
 <line x1="24" y1="100" x2="124" y2="100" stroke="#2b3c32" stroke-width="1.4"/>
 <text x="74" y="174" text-anchor="middle" fill="#ecf4ea" font-weight="700" font-size="14">四分法分樣</text>
 <text x="74" y="194" text-anchor="middle" fill="#9fb39c" font-size="12">留對角兩份 · 取 ~6 g</text>
 <!-- 2 ball mill -->
 <circle cx="282" cy="100" r="44" fill="#1a241e" stroke="#5fd07f" stroke-width="2"/>
 <circle cx="268" cy="92" r="9" fill="#e7ad4d"/><circle cx="296" cy="108" r="8" fill="#5fd07f"/>
 <circle cx="288" cy="84" r="6" fill="#b6c8b4"/><circle cx="272" cy="114" r="6" fill="#e7ad4d"/>
 <text x="282" y="172" text-anchor="middle" fill="#ecf4ea" font-weight="700" font-size="14">球磨成粉</text>
 <text x="282" y="192" text-anchor="middle" fill="#9fb39c" font-size="12">氧化鋯珠研磨</text>
 <!-- 3 oven -->
 <rect x="392" y="58" width="104" height="84" rx="9" fill="#241d10" stroke="#e7ad4d" stroke-width="2"/>
 <rect x="404" y="116" width="80" height="16" rx="3" fill="rgba(231,173,77,.3)"/>
 <text x="444" y="98" text-anchor="middle" fill="#e7ad4d" font-weight="800" font-size="20">85°C</text>
 <text x="444" y="172" text-anchor="middle" fill="#ecf4ea" font-weight="700" font-size="14">烘乾 15–25 h</text>
 <text x="444" y="192" text-anchor="middle" fill="#9fb39c" font-size="12">乾燥器冷卻</text>
 <!-- 4 weigh -->
 <rect x="556" y="92" width="100" height="14" rx="4" fill="#1a241e" stroke="#5fd07f" stroke-width="2"/>
 <rect x="598" y="106" width="16" height="26" fill="#1a241e" stroke="#5fd07f" stroke-width="2"/>
 <path d="M576 92 q30 34 0 0" fill="none"/>
 <ellipse cx="606" cy="90" rx="26" ry="7" fill="rgba(95,208,127,.34)" stroke="#5fd07f" stroke-width="1.5"/>
 <text x="606" y="158" text-anchor="middle" fill="#ecf4ea" font-weight="700" font-size="14">精稱 ~0.2 g</text>
 <text x="606" y="178" text-anchor="middle" fill="#9fb39c" font-size="12">入微波消化瓶</text>
 <!-- arrows -->
 <g stroke="#6f8472" stroke-width="2.4" fill="none" marker-end="url(#apa)">
  <path d="M128 100 h94"/><path d="M330 100 h56"/><path d="M500 100 h48"/></g>
</svg>"""

SVG_ICPMS = r"""
<svg viewBox="0 0 760 200">
 <defs><marker id="aib" markerWidth="10" markerHeight="10" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#6f8472"/></marker>
  <linearGradient id="pl" x1="0" y1="0" x2="1" y2="0">
   <stop offset="0" stop-color="#e7ad4d"/><stop offset="1" stop-color="#ff7a3c"/></linearGradient></defs>
 <g font-size="13">
  <rect x="10" y="64" width="120" height="68" rx="11" fill="#13201a" stroke="#5fd07f" stroke-width="2"/>
  <text x="70" y="92" text-anchor="middle" fill="#ecf4ea" font-weight="800">霧化</text>
  <text x="70" y="112" text-anchor="middle" fill="#9fb39c">檢液→微滴氣膠</text>
  <rect x="160" y="60" width="128" height="76" rx="11" fill="#241409" stroke="#e7ad4d" stroke-width="2"/>
  <path d="M176 98 q24 -26 48 0 q24 26 48 0" fill="none" stroke="url(#pl)" stroke-width="4"/>
  <text x="224" y="86" text-anchor="middle" fill="#e7ad4d" font-weight="800">氬電漿</text>
  <text x="224" y="124" text-anchor="middle" fill="#f0c074" font-size="12">~6000–8000 K 離子化</text>
  <rect x="318" y="64" width="116" height="68" rx="11" fill="#13201a" stroke="#5fd07f" stroke-width="2"/>
  <text x="376" y="92" text-anchor="middle" fill="#ecf4ea" font-weight="800">介面錐</text>
  <text x="376" y="112" text-anchor="middle" fill="#9fb39c">離子導入真空</text>
  <rect x="464" y="64" width="132" height="68" rx="11" fill="#13201a" stroke="#5fd07f" stroke-width="2"/>
  <text x="530" y="88" text-anchor="middle" fill="#ecf4ea" font-weight="800">質量分析器</text>
  <text x="530" y="108" text-anchor="middle" fill="#9fb39c">依 m/z 分離</text>
  <text x="530" y="124" text-anchor="middle" fill="#9fb39c" font-size="12">氦碰撞氣除干擾</text>
  <rect x="626" y="64" width="124" height="68" rx="11" fill="#13201a" stroke="#5fd07f" stroke-width="2"/>
  <text x="688" y="88" text-anchor="middle" fill="#ecf4ea" font-weight="800">偵測器</text>
  <text x="688" y="108" text-anchor="middle" fill="#9fb39c">數離子數</text>
  <text x="688" y="124" text-anchor="middle" fill="#5fd07f" font-size="12">訊號 ∝ 濃度</text>
  <g stroke="#6f8472" stroke-width="2.4" fill="none" marker-end="url(#aib)">
   <path d="M130 98 h26"/><path d="M288 98 h26"/><path d="M434 98 h26"/><path d="M596 98 h26"/></g>
  <circle cx="300" cy="50" r="3" fill="#5fd07f"/><circle cx="330" cy="44" r="2.4" fill="#e7ad4d"/>
  <circle cx="356" cy="52" r="2.6" fill="#b6c8b4"/>
 </g>
</svg>"""

SVG_DTREE = r"""
<svg viewBox="0 0 920 432">
 <defs><marker id="adt" markerWidth="10" markerHeight="10" refX="7" refY="4" orient="auto">
   <path d="M0 0 L8 4 L0 8 z" fill="#6f8472"/></marker></defs>
 <rect x="320" y="10" width="280" height="54" rx="13" fill="#13201a" stroke="#5fd07f" stroke-width="2"/>
 <text x="460" y="34" text-anchor="middle" fill="#ecf4ea" font-weight="800" font-size="15">檢體：14 元素含量</text>
 <text x="460" y="53" text-anchor="middle" fill="#9fb39c" font-size="12">Li V Cr Ni Cu Zn Rb Sr Cd Cs Ba La Ce Pb (mg/kg)</text>
 <rect x="286" y="92" width="348" height="50" rx="13" fill="#241d10" stroke="#e7ad4d" stroke-width="2"/>
 <text x="460" y="113" text-anchor="middle" fill="#e7ad4d" font-weight="800" font-size="15">茶改場 700+ 筆茶樣資料庫</text>
 <text x="460" y="132" text-anchor="middle" fill="#cdb98a" font-size="12">建立元素指紋的母體基準</text>
 <text x="460" y="167" text-anchor="middle" fill="#b6c8b4" font-size="12.5">5 種統計模型 · k-折交叉驗證選最佳參數</text>
 <g font-size="13" font-weight="800">
  <rect x="40"  y="178" width="150" height="40" rx="9" fill="#1a241e" stroke="#5fd07f" stroke-width="1.6"/><text x="115" y="203" text-anchor="middle" fill="#ecf4ea">LDA 線性判別</text>
  <rect x="210" y="178" width="150" height="40" rx="9" fill="#1a241e" stroke="#5fd07f" stroke-width="1.6"/><text x="285" y="203" text-anchor="middle" fill="#ecf4ea">Ridge 脊迴歸</text>
  <rect x="380" y="178" width="160" height="40" rx="9" fill="#1a241e" stroke="#e7ad4d" stroke-width="1.6"/><text x="460" y="203" text-anchor="middle" fill="#ecf4ea">Random Forest</text>
  <rect x="560" y="178" width="150" height="40" rx="9" fill="#1a241e" stroke="#e7ad4d" stroke-width="1.6"/><text x="635" y="203" text-anchor="middle" fill="#ecf4ea">Boosting 提升</text>
  <rect x="730" y="178" width="150" height="40" rx="9" fill="#1a241e" stroke="#e7ad4d" stroke-width="1.6"/><text x="805" y="203" text-anchor="middle" fill="#ecf4ea">SVM 支援向量</text>
 </g>
 <rect x="280" y="262" width="360" height="40" rx="20" fill="#13201a" stroke="#5fd07f" stroke-width="1.6"/>
 <text x="460" y="287" text-anchor="middle" fill="#5fd07f" font-weight="800" font-size="13.5">綜合 準確率 · 召回率 · 精確值</text>
 <g font-weight="900">
  <rect x="118" y="330" width="300" height="86" rx="15" fill="rgba(95,208,127,.14)" stroke="#5fd07f" stroke-width="2.2"/>
  <text x="268" y="368" text-anchor="middle" fill="#5fd07f" font-size="22">臺灣 Taiwan</text>
  <text x="268" y="394" text-anchor="middle" fill="#b6c8b4" font-size="12.5" font-weight="600">指紋落入臺灣茶分布</text>
  <rect x="502" y="330" width="300" height="86" rx="15" fill="rgba(231,173,77,.15)" stroke="#e7ad4d" stroke-width="2.2"/>
  <text x="652" y="368" text-anchor="middle" fill="#e7ad4d" font-size="22">境外 Non-Taiwan</text>
  <text x="652" y="394" text-anchor="middle" fill="#cdb98a" font-size="12.5" font-weight="600">指紋偏離臺灣茶分布</text>
 </g>
 <g stroke="#6f8472" stroke-width="2.4" fill="none" marker-end="url(#adt)">
  <path d="M460 64 v26"/><path d="M460 220 v40"/>
  <path d="M460 302 C 380 318,330 318,300 330"/><path d="M460 302 C 540 318,590 318,620 330"/></g>
</svg>"""

# ============================================================ slides
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---- 1 cover (full-bleed) ----
COVER_OVL = ('<div class="kicker" style="color:#7be39a">食品分析 · 食品鑑別科學</div>'
  '<h1 style="font-size:clamp(2.1rem,5.4vw,4.1rem);font-weight:900;line-height:1.05;color:#fff;letter-spacing:-.02em">'
  '一杯茶，<br>能驗出它的<span style="color:#7be39a">故鄉</span>嗎？</h1>'
  '<div style="font-family:\'JetBrains Mono\',monospace;color:#7be39a;margin-top:10px;letter-spacing:.06em;font-size:clamp(.85rem,1.6vw,1.2rem)">'
  '茶葉中多重元素檢驗方法 · TFDAF0032.00</div>'
  '<div style="color:rgba(255,255,255,.82);margin-top:16px;font-size:clamp(.92rem,1.5vw,1.18rem);line-height:1.6">'
  'ICP-MS 14 元素指紋 × 機器學習產地判別　·　臺灣 vs 境外烏龍茶</div>'
  '<div style="margin-top:22px">'
  + ''.join('<span class="pill" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.25);color:#eafff0">%s</span>' % x
            for x in ["四分法取樣","微波消化","ICP-MS","元素指紋","5 模型判別"]) + '</div>')
COVER_SCRIM = ("background:linear-gradient(90deg,rgba(8,13,10,.93) 0%,rgba(8,13,10,.66) 40%,rgba(8,13,10,.12) 100%),"
               "linear-gradient(0deg,rgba(8,13,10,.8),transparent 52%)")
add(MOT, fullbleed(IMG_COVER, COVER_OVL, COVER_SCRIM, "bottom:12%"), ' data-full="1"')

# ---- 2 hook ----
add(MOT, """<div style="text-align:center">
  <div class="kicker" style="justify-content:center">先想一想</div>
  <div class="hook">一罐「臺灣高山茶」，<span class="hi">真的來自臺灣嗎？</span></div>
  <p class="subtitle" style="max-width:840px;margin:22px auto 0">臺灣茶價格是進口茶的<strong>數倍</strong>，標示不實時有所聞。
  感官品評、產地證明都<strong>可能造假</strong>——我們需要一個<span class="em">難以偽造的客觀證據</span>。</p>
  <div style="margin-top:24px"><span class="pill">價差誘因</span><span class="pill">標示查核</span>
  <span class="pill">消費信任</span><span class="pill">邊境查驗</span></div>
  <div class="note" style="max-width:760px;margin:24px auto 0;text-align:left">答案，藏在茶葉一生「吃」進去的<strong>土壤與水</strong>裡——也就是它累積的<strong>微量元素</strong>。</div></div>""")

# ---- 3 fingerprint (AI img) ----
add(MOT, dc.kt("核心命題", "茶葉會「記住」它的<span class='hi'>土壤</span>") +
    '<div class="grid2" style="margin-top:14px">' + imgcard(IMG_FINGER, "元素指紋", "tea roots absorbing minerals") +
    '<div><ul class="clean">'
    "<li>茶樹從<strong>土壤、水、氣候</strong>長年吸收微量元素</li>"
    "<li>不同產地的<strong>地質背景</strong>不同 → 元素組成比例不同</li>"
    "<li>14 種元素的相對含量，組成一組難以複製的<span class='em'>產地指紋</span></li>"
    "<li>Sr、Rb、Cs、Ba 等常反映<strong>母岩與地質</strong>，是指紋的關鍵特徵</li>"
    '</ul><div class="note" style="margin-top:14px">這就是<strong>多重元素指紋 (multielement fingerprinting)</strong> 鑑別產地的科學基礎。</div></div></div>')

# ---- 4 method overview (2x3 cards) ----
add(ATT, dc.kt("方法全貌", "從茶葉到判決，<span class='hi'>六步驟</span>") +
    '<div class="grid3" style="margin-top:20px;gap:18px">' +
    dc.card("🍃","① 採樣分樣","以<strong>四分法</strong>取出有代表性的茶樣","b") +
    dc.card("⚙️","② 前處理","球磨成粉、<strong>85°C 烘乾</strong>至乾基","a") +
    dc.card("🔥","③ 微波酸消化","硝酸高溫高壓<strong>打碎基質</strong>釋出元素","b") +
    dc.card("📡","④ ICP-MS 定量","14 元素同時測，達 <strong>ng/mL</strong> 級","a") +
    dc.card("🗂️","⑤ 資料庫比對","對照茶改場 <strong>700+ 筆</strong>茶樣","b") +
    dc.card("⚖️","⑥ 統計判別","5 模型投票 → <strong>臺灣／境外</strong>","a") + '</div>')

# ---- 5 the 14 elements (sortable table) ----
EL_COLS = [{"k":"sym","t":"s","label":"符號"},{"k":"name","t":"s","label":"元素"},
           {"k":"mz","t":"n","label":"質荷比 m/z"},{"k":"cal","t":"n","label":"校準上限 ng/mL"},
           {"k":"cls","t":"s","label":"類別"}]
add(ATT, dc.cmp_inner("14 種元素，一張<span class='hi'>指紋表</span>", EL_COLS,
    "點欄位標題即可排序（試以 m/z 或校準上限）。資料整理自方法 2.6。",
    kicker="2.6 偵測離子 m/z"), ' data-game="cmp"')

# ---- 6 sampling & milling (SVG) ----
add(ATT, dc.kt("第一關 · 前處理", "取出「有代表性」的 <span class='hi'>0.2 克</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + SVG_PREP + '</div>' +
    '<div class="note" style="margin-top:14px"><strong>四分法</strong>反覆對分、留對角，確保 6 g 茶樣能代表整批；'
    "<strong>烘乾</strong>除去水分讓結果以<strong>乾基</strong>表示、可互相比較；最後精稱約 0.2 g 進行消化。</div>")

# ---- 7 microwave digestion ----
add(ATT, dc.kt("第二關 · 微波消化", "把元素「逼」進<span class='hi'>溶液</span>") +
    '<div class="grid2" style="margin-top:14px">' +
    '<div><table class="tbl"><thead><tr><th>步驟</th><th>功率<span class="u">W</span></th><th>升溫<span class="u">min</span></th><th>持續<span class="u">min</span></th><th>溫度<span class="u">°C</span></th></tr></thead>'
    '<tbody><tr><td class="c">1</td><td>1700</td><td>10.5</td><td>5</td><td>170</td></tr>'
    '<tr><td class="c">2</td><td>1700</td><td>5</td><td>20</td><td>180</td></tr></tbody></table>'
    '<p class="subtitle" style="margin-top:12px">茶粉 + <strong>硝酸 6 mL</strong>，靜置 4 h 後上述兩階段消化。</p></div>' +
    '<div class="note">為什麼要酸消化？<br>有機基質會「包住」金屬元素。<strong>濃硝酸 + 微波高溫高壓</strong>'
    "把有機物氧化分解，元素以<strong>離子態</strong>釋入溶液，才能被 ICP-MS 偵測。"
    "<br><br>同時跑一份<strong>空白</strong>，扣除試劑與器具帶入的背景。</div></div>")

# ---- 8 sort game: prep order ----
add(ATT, dc.game_sort_inner("gprep", "互動 ①", "前處理流程，排對順序", 7,
    "用 ▲▼ 把「茶葉 → 檢液」的 7 個步驟排成正確順序。"), ' data-game="gprep"')

# ---- 9 ICP-MS (AI img) ----
add(ATT, dc.kt("核心儀器", "ICP-MS：把原子變成<span class='hi'>離子</span>") +
    '<div class="grid2" style="margin-top:14px">' + imgcard(IMG_ICPMS, "ICP-MS", "argon plasma torch") +
    '<div><ul class="clean">'
    "<li>檢液<strong>霧化</strong>成微滴，送入氬氣電漿炬</li>"
    "<li>電漿高達 <span class='em'>約 6000–8000 K</span>，原子被<strong>離子化</strong></li>"
    "<li>質譜依<strong>質荷比 (m/z)</strong> 分離各元素離子</li>"
    "<li>偵測器<strong>計數離子</strong>，訊號強度 ∝ 元素濃度</li>"
    '</ul><div class="note" style="margin-top:14px">一次進樣即可<strong>同時測 14 元素</strong>，靈敏度達 ppb——量測痕量指紋的理想工具。</div></div></div>')

# ---- 10 ICP-MS schematic + conditions ----
add(ATT, dc.kt("2.6 儀器原理與條件", "原子變離子，再依<span class='hi'>質量</span>點數") +
    '<div class="svgwrap" style="margin-top:4px">' + SVG_ICPMS + '</div>' +
    '<div class="dnums">'
    '<div class="dnum"><div class="v">1550 W</div><div class="k">電漿無線電頻功率</div></div>'
    '<div class="dnum"><div class="v">15 L/min</div><div class="k">電漿氬氣流速</div></div>'
    '<div class="dnum"><div class="v">1.0 L/min</div><div class="k">霧化氬氣流速</div></div>'
    '<div class="dnum"><div class="v">4.3 mL/min</div><div class="k">氦碰撞氣（除多原子干擾）</div></div></div>')

# ---- 11 formula ----
add(ATT, dc.kt("2.8 含量測定", "從訊號到 <span class='hi'>mg/kg</span>") +
    '<div class="grid2" style="margin-top:14px;align-items:center">' +
    '<div class="eq" style="font-size:clamp(1rem,1.7vw,1.4rem)">含量 (mg/kg) = '
    '<span class="frac"><b>(C − C₀) × V × f</b><span>M × 1000</span></span></div>' +
    '<div><ul class="clean">'
    "<li><b>C</b>　檢液中元素濃度 (ng/mL，由標準曲線)</li>"
    "<li><b>C₀</b>　空白檢液濃度 (ng/mL)</li>"
    "<li><b>V</b>　最後定容體積 (mL，本法 50)</li>"
    "<li><b>f</b>　上機稀釋倍數</li>"
    "<li><b>M</b>　乾燥後茶粉取樣重 (g)</li>"
    '</ul></div></div>' +
    '<div class="note" style="margin-top:14px">扣空白 (C−C₀) 去背景；×V 變回總量；÷M 變成「每克茶」；單位換算後得到 <strong>mg/kg</strong>。</div>')

# ---- 12 calc game ----
add(ATT, dc.game_calc_inner("gcalc", "互動 ②", "計算闖關：算出銅含量",
    "某茶粉精稱 <strong>M = 0.2000 g</strong>，消化後定容 <strong>V = 50.0 mL</strong>，上機<strong>稀釋 f = 2</strong>。"
    "測得銅 <strong>C = 8.0 ng/mL</strong>，空白 <strong>C₀ ≈ 0</strong>。求茶葉中銅含量（<strong>mg/kg</strong>）。",
    unit="mg/kg"), ' data-game="gcalc"')

# ---- 13 radar (illustrative; dedicated script: radar-only r-axis, starts at 0) ----
# NB: the shared engine always adds scales:{y} which renders a stray 0-1 cartesian
# axis over a radar and starts r at the data min. Render this radar ourselves instead
# (no data-chart attr -> engine ignores it). Kept local so the shared engine is untouched.
RADAR_SCRIPT = """
<script>
(function(){
  function draw(){
    if(typeof Chart==='undefined') return setTimeout(draw,80);
    var el=document.getElementById('chart_rad'); if(!el||el._done) return; el._done=1;
    new Chart(el,{type:'radar',
      data:{labels:["Rb 銣","Sr 鍶","Cs 銫","Ba 鋇","La 鑭","Pb 鉛","Zn 鋅"],
        datasets:[
          {label:"臺灣茶（示意）",data:[7.5,4,8,4.5,6.5,3,6],
           backgroundColor:"rgba(95,208,127,.34)",borderColor:"#5fd07f",borderWidth:2,pointBackgroundColor:"#5fd07f",pointRadius:3},
          {label:"境外茶（示意）",data:[4,7.5,3.5,8,4,5.5,7.5],
           backgroundColor:"rgba(231,173,77,.30)",borderColor:"#e7ad4d",borderWidth:2,pointBackgroundColor:"#e7ad4d",pointRadius:3}
        ]},
      options:{responsive:true,maintainAspectRatio:false,
        plugins:{legend:{position:"top",labels:{color:"#ecf4ea",font:{size:13}}}},
        scales:{r:{min:0,max:10,
          angleLines:{color:"rgba(255,255,255,.12)"},grid:{color:"rgba(255,255,255,.12)"},
          pointLabels:{color:"#cde0c9",font:{size:13}},
          ticks:{display:false,stepSize:2,backdropColor:"transparent"}}}}});
  }
  if(document.readyState!=="loading") draw(); else document.addEventListener("DOMContentLoaded",draw);
})();
</script>"""
add(ATT, dc.chart_inner("rad", "臺灣 vs 境外茶的<span class='hi'>指紋輪廓</span>",
    "示意圖（非實際數據）：相對含量正規化後的概念輪廓。實務以 700+ 筆資料庫與統計模型綜合判別，而非單一元素。",
    kicker="元素指紋視覺化", height="54vh") + RADAR_SCRIPT)

# ---- 13b foundational study (Tsai et al. 2021, the real PCA paper behind the method) ----
add(ATT, dc.kt("機器學習的資料基礎 · J. Taiwan Agric. Res. 2021", "這個方法，<span class='hi'>從一篇研究</span>開始") +
    '<div class="grid2" style="margin-top:14px;gap:18px">' +
    dc.card("🧪", "樣本 20 件", "台灣 12 vs 國外 8（中 3·越 1·馬 1·斯 2·印 1）", "b") +
    dc.card("🔬", "元素 31 種", "分 微量 / 風化 / 肥料 三群", "a") +
    dc.card("📡", "雙儀器", "ICP-MS 測微量 + ICP-OES 測風化·肥料", "b") +
    dc.card("📊", "分析法", "主成分分析 PCA：降維後看分群", "a") + '</div>' +
    '<div class="note" style="margin-top:16px">蔡承祥、彭宗仁、劉滄棽、林毓雯、詹婉君 (2021)。'
    '<strong>以元素特徵區別台灣茶葉與國外茶葉之初步研究</strong>。台灣農業研究 70(4):231–242。'
    '—— 正是 TFDAF0032.00 官方方法背後的科學依據。</div>')

# ---- 13c no single element is enough ----
add(ATT, dc.kt("為什麼需要「多重」元素", "沒有一個元素，能<span class='hi'>單獨定案</span>") +
    '<div class="grid2" style="margin-top:14px;gap:18px">' +
    dc.card("🔻", "Ti、Se：台灣偏低", "但中國、印度部分樣本與台灣重疊", "b") +
    dc.card("🔺", "Cs：中國偏高", "其他國家偶爾也出現高值樣本", "a") +
    dc.card("🔺", "Ga、Sr、Ba：馬來西亞偏高", "印度也偏高，台灣可能落在範圍內", "b") +
    dc.card("🔺", "Cr、Ni、Co：印度偏高", "越南部分樣本與之重疊", "a") + '</div>' +
    '<div class="note" style="margin-top:16px">任何「單一元素」的高低都會<strong>重疊</strong> → 必須同時看<strong>多個元素的組合</strong>。'
    '這正是 <span class="em">PCA／機器學習</span> 登場的地方。</div>')

# ---- 13d real PCA score plot (Fig 4 reproduction; dedicated scatter script) ----
PCA_SCRIPT = """
<script>
(function(){
  var TW=[[-1.30,-0.20],[-1.15,0.05],[-1.10,-0.05],[-0.95,0.30],[-0.70,0.65],[-0.60,0.60],[-0.50,0.75],[-0.40,1.00],[-0.35,1.00],[-0.15,0.95],[0.05,0.35],[0.35,1.60]];
  var FG=[[0.75,0.10,"C"],[3.00,-0.35,"C"],[-0.30,-1.95,"C"],[1.60,0.20,"I"],[0.60,-0.20,"S"],[0.00,-1.95,"S"],[0.05,-1.80,"M"],[-0.35,-0.85,"V"]];
  function P(a){return a.map(function(p){return {x:p[0],y:p[1]};});}
  var labelFG={id:"lblfg",afterDatasetsDraw:function(ch){var ctx=ch.ctx,m=ch.getDatasetMeta(1);if(!m)return;ctx.save();
    ctx.font="700 12px 'JetBrains Mono',monospace";ctx.fillStyle="#f0c074";ctx.textAlign="left";
    m.data.forEach(function(pt,i){if(FG[i]&&FG[i][2])ctx.fillText(FG[i][2],pt.x+8,pt.y+4);});ctx.restore();}};
  function draw(){
    if(typeof Chart==="undefined") return setTimeout(draw,80);
    var el=document.getElementById("chart_pca"); if(!el||el._done) return; el._done=1;
    new Chart(el,{type:"scatter",
      data:{datasets:[
        {label:"台灣茶 (n=12)",data:P(TW),backgroundColor:"#5fd07f",pointRadius:6,pointHoverRadius:8,borderColor:"#0e1512",borderWidth:1.5},
        {label:"國外茶 (n=8)",data:P(FG),backgroundColor:"#e7ad4d",pointStyle:"rectRot",pointRadius:7,pointHoverRadius:9,borderColor:"#0e1512",borderWidth:1.5},
        {label:"分界線",type:"line",data:[{x:-1.8,y:-1.45},{x:3.5,y:2.68}],borderColor:"rgba(255,255,255,.45)",borderDash:[6,6],borderWidth:1.5,pointRadius:0,fill:false}
      ]},
      options:{responsive:true,maintainAspectRatio:false,
        plugins:{legend:{labels:{color:"#ecf4ea",usePointStyle:true,font:{size:13}}},
          tooltip:{callbacks:{label:function(c){return "("+c.parsed.x.toFixed(2)+", "+c.parsed.y.toFixed(2)+")";}}}},
        scales:{
          x:{title:{display:true,text:"T-PC1 (24.40%)",color:"#cde0c9",font:{size:13}},grid:{color:"rgba(255,255,255,.08)"},ticks:{color:"#b6c8b4"}},
          y:{title:{display:true,text:"T-PC4 (10.18%)",color:"#cde0c9",font:{size:13}},grid:{color:"rgba(255,255,255,.08)"},ticks:{color:"#b6c8b4"}}}},
      plugins:[labelFG]});
  }
  if(document.readyState!=="loading") draw(); else document.addEventListener("DOMContentLoaded",draw);
})();
</script>"""
add(ACT, dc.chart_inner("pca", "PCA：把 31 維壓成<span class='hi'>一張圖</span>",
    "重繪自 Tsai et al. 2021 Fig 4。每點為一茶樣（綠●=台灣、金◆=國外，字母為國別 C/M/V/S/I）；"
    "僅 T-PC1+T-PC4 ≈ 34.6% 變異，台灣茶已自然聚成一群、與國外茶被虛線分開。",
    kicker="原研究結果 · 主成分得分圖", height="52vh") + PCA_SCRIPT)

# ---- 13d2 interactive toggle: live PCA on reconstructed data, switch T/TW/TF/A ----
TOGGLE_SCRIPT = ('<script>(function(){var PCASCORES=' + PCA_SCORES_JSON + ';' + """
  var INFO={
    T:{v:"✓ 乾淨分群",t:"good",n:"只用 13 個微量元素，台灣茶就聚成一群、與國外分開。"},
    TW:{v:"✓ 依然乾淨",t:"good",n:"再加風化元素 Fe/Al/Mn（同屬土壤背景），分群一樣清楚。"},
    TF:{v:"△ 開始變混",t:"warn",n:"加入肥料元素 P/S/K/Ca/Mg 後，部分國外茶（如斯里蘭卡 S）被拉近台灣群——施肥差異是噪音。"},
    A:{v:"▽ 最不乾淨",t:"bad",n:"全部元素混用，雜訊最多，分群品質下降最多。"}
  };
  var chart=null,fgTags=[];
  var lbl={id:"tgl",afterDatasetsDraw:function(ch){var m=ch.getDatasetMeta(1);if(!m)return;var c=ch.ctx;c.save();c.font="700 11px 'JetBrains Mono',monospace";c.fillStyle="#f0c074";m.data.forEach(function(pt,i){if(fgTags[i])c.fillText(fgTags[i],pt.x+7,pt.y+4);});c.restore();}};
  function render(key){
    var s=PCASCORES[key]; if(!s) return;
    var tw=[],fg=[]; fgTags=[];
    s.pts.forEach(function(p){ if(p[2]==="TW") tw.push({x:p[0],y:p[1]}); else {fg.push({x:p[0],y:p[1]});fgTags.push(p[2]);} });
    if(chart) chart.destroy();
    chart=new Chart(document.getElementById("chart_toggle"),{type:"scatter",
      data:{datasets:[
        {label:"台灣茶",data:tw,backgroundColor:"#5fd07f",pointRadius:6,borderColor:"#0e1512",borderWidth:1.3},
        {label:"國外茶",data:fg,backgroundColor:"#e7ad4d",pointStyle:"rectRot",pointRadius:7,borderColor:"#0e1512",borderWidth:1.3}
      ]},
      options:{responsive:true,maintainAspectRatio:false,animation:{duration:400},
        plugins:{legend:{labels:{color:"#ecf4ea",usePointStyle:true}}},
        scales:{x:{min:-2.5,max:8,title:{display:true,text:"PC1 ("+s.pc1+"%)",color:"#cde0c9"},grid:{color:"rgba(255,255,255,.07)"},ticks:{color:"#b6c8b4"}},
                y:{min:-7,max:3.5,title:{display:true,text:"PC2 ("+s.pc2+"%)",color:"#cde0c9"},grid:{color:"rgba(255,255,255,.07)"},ticks:{color:"#b6c8b4"}}}},
      plugins:[lbl]});
    document.getElementById("pcaAcc").textContent=s.acc+"%";
    var info=INFO[key],vd=document.getElementById("pcaVerdict");
    vd.textContent=info.v;
    var col=info.t==="good"?"#5fd07f":(info.t==="warn"?"#e7ad4d":"#ef7373");
    var bg=info.t==="good"?"rgba(95,208,127,.16)":(info.t==="warn"?"rgba(231,173,77,.18)":"rgba(239,115,115,.16)");
    vd.style.color=col; vd.style.background=bg; document.getElementById("pcaAcc").style.color=col;
    document.getElementById("pcaNote").innerHTML=info.n;
    document.querySelectorAll("#pcaSetBtns button").forEach(function(b){b.className=(b.dataset.set===key)?"btn":"btn ghost";});
  }
  function init(){
    if(typeof Chart==="undefined") return setTimeout(init,80);
    var el=document.getElementById("chart_toggle"); if(!el||el._tdone) return; el._tdone=1;
    document.querySelectorAll("#pcaSetBtns button").forEach(function(b){b.onclick=function(){render(b.dataset.set);};});
    render("T");
  }
  if(document.readyState!=="loading") init(); else document.addEventListener("DOMContentLoaded",init);
})();</script>""")
add(ACT, dc.kt("換你試試 · 互動切換", "加不同元素，<span class='hi'>分得開嗎？</span>") +
    '<div class="btnrow no-nav" id="pcaSetBtns" style="margin:12px 0 6px;flex-wrap:wrap">'
    '<button class="btn" data-set="T">微量 T</button>'
    '<button class="btn ghost" data-set="TW">＋風化 TW</button>'
    '<button class="btn ghost" data-set="TF">＋肥料 TF</button>'
    '<button class="btn ghost" data-set="A">全部 A</button></div>'
    '<div class="grid2" style="grid-template-columns:1.5fr .5fr;gap:22px;align-items:stretch;margin-top:2px">'
    '<div class="chartbox" style="height:46vh"><canvas id="chart_toggle"></canvas></div>'
    '<div style="display:flex;flex-direction:column;justify-content:center">'
    '<div class="kicker" style="margin-bottom:2px">分類正確率 · LDA 留一法</div>'
    '<div id="pcaAcc" style="font-family:\'JetBrains Mono\',monospace;font-weight:800;font-size:clamp(2.2rem,5vw,3.4rem);color:var(--accent);line-height:1">95%</div>'
    '<div id="pcaVerdict" style="margin-top:10px;align-self:flex-start;font-weight:800;font-size:clamp(.95rem,1.4vw,1.15rem);padding:5px 13px;border-radius:999px;background:rgba(95,208,127,.16);color:#5fd07f">✓ 乾淨分群</div>'
    '<div id="pcaNote" style="margin-top:12px;color:var(--ink-2);font-size:clamp(.85rem,1.2vw,1rem);line-height:1.6"></div>'
    '<div class="cap" style="margin-top:14px;text-align:left;border-top:1px solid var(--line);padding-top:10px">教學重建資料（依 Tsai 2021）·正確率序列 95→95→90→85%。真實可下載：蜂蜜 ICP-OES CC0 <span class="mono">tt6pp6pbpk</span>。</div>'
    '</div></div>' + TOGGLE_SCRIPT)

# ---- 13e feature selection lesson + hands-on dataset ----
add(ACT, dc.kt("ML 的關鍵一課 + 課堂實作", "選對「特徵」，才<span class='hi'>分得開</span>") +
    '<div class="grid2" style="margin-top:14px">' +
    '<div>' +
    '<div class="minicard b" style="margin-bottom:9px"><div class="mt">T　微量元素　<span style="color:var(--accent)">✓ 可分</span></div><div class="mb">PC1+PC4 ≈ 34.6% 即可分群</div></div>' +
    '<div class="minicard b" style="margin-bottom:9px"><div class="mt">TW　微量+風化　<span style="color:var(--accent)">✓ 可分</span></div><div class="mb">風化元素也帶土壤背景訊號</div></div>' +
    '<div class="minicard b" style="margin-bottom:9px"><div class="mt">A　全部元素　<span style="color:var(--accent)">✓ 可分</span></div><div class="mb">整體仍能區分</div></div>' +
    '<div class="minicard" style="border-top:3px solid var(--bad)"><div class="mt">TF　微量+肥料　<span style="color:var(--bad)">✗ 不可分</span></div><div class="mb">肥料元素受各地施肥影響、變異大，蓋掉產地訊號</div></div>' +
    '</div>' +
    '<div class="note" style="align-self:start"><strong>👉 這就是機器學習的「特徵選擇 (feature selection)」</strong>：加入「對的」特徵幫助分類，加入「噪音」特徵反而更糟。<br><br>'
    '<strong>動手做（dataset/ 資料夾）</strong><br>'
    '• <strong>教學重建 CSV + pca_demo.py</strong>（依 Tsai 2021 統計量模擬 20 樣本）：實跑得 <span class="em">trace 95% 留一法</span>；加肥料降到 90%／85%，重現上方效應。<br>'
    '• <strong>真實可下載</strong>：蜂蜜 ICP-OES（CC0, Mendeley <span class="mono">tt6pp6pbpk</span>）429 樣本×12 元素，同為「元素×樣本」分類，可直接練 PCA／PLS-DA。</div>' +
    '</div>')

# ---- 14 from numbers to origin (decision tree) ----
add(ACT, dc.kt("2.9 檢體鑑別", "從數字到<span class='hi'>產地判決</span>") +
    '<div class="svgwrap" style="margin-top:6px">' + SVG_DTREE + '</div>')

# ---- 15 five models ----
add(ACT, dc.kt("2.9 統計模式", "五種模型，交叉驗證<span class='hi'>定案</span>") +
    '<div class="grid5" style="margin-top:18px">' +
    '<div class="minicard b"><div class="mt">LDA</div><div class="mb">線性判別分析<br><span style="color:var(--accent)">傳統統計</span></div></div>' +
    '<div class="minicard b"><div class="mt">Ridge</div><div class="mb">脊迴歸<br><span style="color:var(--accent)">傳統統計</span></div></div>' +
    '<div class="minicard a"><div class="mt">Random Forest</div><div class="mb">隨機森林<br><span style="color:var(--accent-2)">機器學習</span></div></div>' +
    '<div class="minicard a"><div class="mt">Boosting</div><div class="mb">提升法<br><span style="color:var(--accent-2)">機器學習</span></div></div>' +
    '<div class="minicard a"><div class="mt">SVM</div><div class="mb">支援向量機<br><span style="color:var(--accent-2)">機器學習</span></div></div>' +
    '</div>' +
    '<div class="note" style="margin-top:18px">全部以 <strong>k-折交叉驗證</strong>調參選最佳，再用 <strong>準確率、召回率、精確值</strong> 三項指標綜合評估，'
    "輸出二分結果：<span class='em'>臺灣 Taiwan</span> 或 <span style='color:var(--accent)'>境外 Non-Taiwan</span>。多模型互相印證，結論更穩健。</div>")

# ---- 16 QC & limits ----
add(ACT, dc.kt("附註 · 品保與限制", "數據可信，<span class='hi'>判斷</span>才有意義") +
    '<div class="grid3" style="margin-top:20px">' +
    dc.card("🧼","防污染","器具以 15% 硝酸<strong>蒸氣酸洗</strong>、用 PP／鐵氟龍、超純試劑，並跑<strong>空白</strong>","b") +
    dc.card("🎯","確效驗證","以 <strong>CRM／SRM</strong> 驗證準確度；換儀器或條件須<strong>重新確效</strong>","a") +
    dc.card("🧭","綜合研判","結果受<strong>氣候、品種、栽培</strong>影響，須<strong>併同產地調查</strong>判讀","b") + '</div>' +
    '<div class="note" style="margin-top:18px">本法是<strong>有力的參考證據</strong>，但非唯一證據——科學鑑別講求<strong>多重證據鏈</strong>。</div>')

# ---- 17 checklist ----
add(ACT, dc.checklist_inner("今天結束，你應該會…",
    ["說明為什麼 14 種元素能當作茶葉的「產地指紋」",
     "描述檢液製備：四分法 → 球磨 → 烘乾 → 微波酸消化",
     "說明 ICP-MS 如何把元素變離子、再依 m/z 定量",
     "用 (C−C₀)×V×f÷(M×1000) 算出元素含量",
     "說明資料庫 + 5 種統計模型如何判別臺灣／境外茶",
     "說明為何要用 PCA／機器學習（單一元素會重疊），以及「特徵選擇」為何重要",
     "指出本法的限制，以及為何須併同調查綜合研判"]))

# ---- 18 closing (full-bleed) ----
CLOSE_OVL = ('<div class="kicker" style="color:#7be39a">重點回顧 · TAKE-HOME</div>'
  '<h1 style="font-size:clamp(1.9rem,4.8vw,3.5rem);font-weight:900;line-height:1.1;color:#fff;letter-spacing:-.01em">'
  '從一片茶葉，<span style="color:#f0c074">讀出一座島</span></h1>'
  '<div style="color:rgba(255,255,255,.85);margin-top:16px;font-size:clamp(.95rem,1.6vw,1.2rem);line-height:1.7">'
  '14 種微量元素 = 產地指紋；<strong style="color:#fff">ICP-MS 量它</strong>，<strong style="color:#fff">機器學習判它</strong>。<br>'
  '科學，讓「臺灣茶」三個字更有底氣。</div>'
  '<div style="margin-top:20px;color:#7be39a;font-size:clamp(.85rem,1.4vw,1.05rem)">'
  '🔎 課後想一想：為什麼 Sr、Rb、Cs 特別能反映地質背景？　🔗 延伸：原子光譜 (AAS/ICP-OES)、化學計量學</div>')
CLOSE_SCRIM = ("background:linear-gradient(90deg,rgba(8,13,10,.9) 0%,rgba(8,13,10,.55) 45%,rgba(8,13,10,.1) 100%),"
               "linear-gradient(0deg,rgba(8,13,10,.82),transparent 50%)")
add(ACT, fullbleed(IMG_CLOSE, CLOSE_OVL, CLOSE_SCRIM, "bottom:13%"), ' data-full="1"')

# ============================================================ CFG (games + charts)
CFG = {
  "sort": {
    "gprep": {"steps": [
        "茶樣混勻、四分法取約 6 g",
        "以球磨機磨碎成茶粉",
        "85°C 烘乾 15–25 h，乾燥器冷卻",
        "精稱乾茶粉約 0.2 g 入微波消化瓶",
        "加硝酸 6 mL，靜置 4 h",
        "微波消化（1700 W 兩階段）",
        "定容 50 mL、濾膜過濾 → 檢液"],
      "shuffle": [3, 0, 5, 2, 6, 1, 4],
      "ok": "🎉 順序正確！分樣→磨粉→烘乾→稱重→加酸→消化→定容過濾。",
      "tip": "提示：一定先取樣磨粉、烘乾稱重，加酸消化後才定容過濾。"}
  },
  "calc": {
    "gcalc": {"answer": 4.0, "tol": 0.15,
      "ok": "🎉 正確！含量 = (8.0−0)×50×2 ÷ (0.2×1000) = 800 ÷ 200 = <b>4.0 mg/kg</b>。",
      "bad": "再算算：分子 = (C−C₀)×V×f = 8.0×50×2 = 800；分母 = M×1000 = 0.2×1000 = 200。",
      "hint": "提示：(8.0−0)×50×2 = 800；0.2×1000 = 200；800÷200 = ?"}
  },
  "cmp": {
    "cols": [{"k": "sym"}, {"k": "name"}, {"k": "mz"}, {"k": "cal"}, {"k": "cls"}],
    "rows": [
      {"sym": "Li", "name": "鋰", "mz": 7,   "cal": 1,  "cls": "鹼金屬"},
      {"sym": "V",  "name": "釩", "mz": 51,  "cal": 5,  "cls": "過渡金屬"},
      {"sym": "Cr", "name": "鉻", "mz": 53,  "cal": 10, "cls": "過渡金屬"},
      {"sym": "Ni", "name": "鎳", "mz": 60,  "cal": 10, "cls": "過渡金屬"},
      {"sym": "Cu", "name": "銅", "mz": 63,  "cal": 10, "cls": "過渡金屬"},
      {"sym": "Zn", "name": "鋅", "mz": 66,  "cal": 10, "cls": "過渡金屬"},
      {"sym": "Rb", "name": "銣", "mz": 85,  "cal": 10, "cls": "鹼金屬"},
      {"sym": "Sr", "name": "鍶", "mz": 88,  "cal": 10, "cls": "鹼土金屬"},
      {"sym": "Cd", "name": "鎘", "mz": 111, "cal": 1,  "cls": "重金屬"},
      {"sym": "Cs", "name": "銫", "mz": 133, "cal": 5,  "cls": "鹼金屬"},
      {"sym": "Ba", "name": "鋇", "mz": 137, "cal": 10, "cls": "鹼土金屬"},
      {"sym": "La", "name": "鑭", "mz": 139, "cal": 5,  "cls": "稀土元素"},
      {"sym": "Ce", "name": "鈰", "mz": 140, "cal": 5,  "cls": "稀土元素"},
      {"sym": "Pb", "name": "鉛", "mz": 208, "cal": 5,  "cls": "重金屬"}
    ]
  }
}

dc.build_html(
    {"title": "茶葉多重元素檢驗 · TFDAF0032.00", "brand": "茶葉 · 多元素指紋"},
    S, CFG, OUT)
