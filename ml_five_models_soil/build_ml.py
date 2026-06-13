# -*- coding: utf-8 -*-
"""五種機器學習分類法 × 茶葉產地判別 — SOIL HTML teaching deck.
接續 TFDAF0032.00（茶葉多重元素）方法：14 元素指紋拿到後，電腦怎麼自動判
「臺灣 vs 境外」？本片教 LDA / Ridge / Random Forest / Boosting / SVM 五種分類器，
每一種都給「一句話直覺 + scikit-learn 程式 + Orange Data Mining 積木」兩條實作路線。

Reuses ../soil_deck_common.py engine, re-skinned dark "tea-green + gold"（與 tea deck 同家族）。
真實數字來自 ../tea_multielement_soil/dataset/tea_five_models_demo.py（留一法 LOO-CV）。
Run:  python build_ml.py   ->   index.html
"""
import os, sys, re, json
import html as _html
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import soil_deck_common as dc

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "index.html")
MOT, ATT, ACT = "引起動機", "維持注意", "喚起行動"

# 真實 LOO-CV 結果（由 tea_five_models_demo.py 實跑、可重現）。有檔讀檔，沒有就用內建值。
SCORES = {"LDA": {"acc": 95.0, "precision": 96.2, "recall": 93.8},
          "Ridge": {"acc": 100.0, "precision": 100.0, "recall": 100.0},
          "Random Forest": {"acc": 95.0, "precision": 96.2, "recall": 93.8},
          "Boosting": {"acc": 85.0, "precision": 90.0, "recall": 81.2},
          "SVM": {"acc": 100.0, "precision": 100.0, "recall": 100.0}}
try:
    with open(os.path.join(HERE, "five_models_scores.json"), encoding="utf-8") as _f:
        SCORES = json.load(_f)
except Exception:
    pass

# ============================================================ DARK SKIN + code/orange CSS
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
.note{color:var(--ink)}
.lbl{fill:var(--ink-2)}.lblb{fill:var(--ink)}
table.cmp tbody tr:hover{background:rgba(95,208,127,.07)}
table.cmp thead th{color:var(--accent)}
table.cmp td.c{color:var(--accent);font-weight:800}
.cover2{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 8%;
  background:
   radial-gradient(1100px 560px at 82% 14%,rgba(231,173,77,.18),transparent 60%),
   radial-gradient(880px 520px at 6% 92%,rgba(95,208,127,.18),transparent 55%),
   linear-gradient(135deg,#0f1714,#13211a 55%,#0c1310)}
/* five-up cards */
.grid5{display:grid;grid-template-columns:repeat(5,1fr);gap:13px}
.minicard{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:13px 15px}
.minicard .mt{font-weight:800;color:var(--ink);font-size:clamp(.92rem,1.4vw,1.08rem);margin-bottom:4px}
.minicard .mb{color:var(--ink-2);font-size:clamp(.78rem,1.12vw,.94rem);line-height:1.5}
.minicard.b{border-top:3px solid var(--accent)}.minicard.a{border-top:3px solid var(--accent-2)}
/* code block */
.codeh{display:flex;align-items:center;gap:8px;margin-bottom:6px;font-family:"JetBrains Mono",monospace;
  font-size:.72rem;letter-spacing:.04em;color:var(--ink-3)}
.codeh .dot{width:9px;height:9px;border-radius:50%;background:var(--accent)}
.code{background:#0b110d;border:1px solid var(--line);border-radius:12px;padding:13px 15px;
  font-family:"JetBrains Mono",monospace;font-size:clamp(.7rem,1.02vw,.9rem);line-height:1.62;
  color:#d6e8d2;white-space:pre;overflow-x:auto;box-shadow:var(--shadow-sm)}
.code .cm{color:#6f8472;font-style:italic}.code .kw{color:#7be39a;font-weight:700}
.code .st{color:#e7ad4d}.code .nm{color:#9ec7ff}
/* orange how-to box */
.obox{background:var(--accent-2-soft);border:1px solid var(--line);border-left:3px solid var(--accent-2);
  border-radius:12px;padding:11px 14px;margin-top:11px}
.obox .oh{font-weight:800;color:var(--accent-2);font-size:clamp(.88rem,1.3vw,1.04rem);margin-bottom:5px}
.obox ul{list-style:none;margin:0}
.obox li{position:relative;padding-left:17px;margin:5px 0;color:var(--ink-2);
  font-size:clamp(.8rem,1.13vw,.96rem);line-height:1.5}
.obox li:before{content:"▸";position:absolute;left:0;color:var(--accent-2);font-weight:800}
.obox li b{color:var(--ink)}
/* svg wrap a touch smaller for method slides */
.svgm{display:flex;align-items:center;justify-content:center}
.svgm svg{max-width:100%;max-height:34vh;height:auto}
/* path chips */
.pyc{color:#7be39a}.orc{color:var(--accent-2)}
.dnums{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:16px}
.dnum{background:var(--surface);border:1px solid var(--line);border-top:3px solid var(--accent-2);
  border-radius:14px;padding:13px 16px;box-shadow:var(--shadow-sm)}
.dnum .v{font-family:"JetBrains Mono",monospace;font-weight:800;color:var(--accent);font-size:clamp(1.05rem,1.9vw,1.45rem)}
.dnum .k{color:var(--ink-2);font-size:.84rem;margin-top:5px;line-height:1.4}
/* Orange canvas wrapper: centred on desktop, horizontally scrollable on phones */
.owrap{display:flex;align-items:center;justify-content:center}
.owrap svg{max-width:100%;max-height:42vh;height:auto}

/* ===================== MOBILE (phones / narrow screens) ===================== */
@media (max-width:640px){
  html,body{font-size:16px}
  /* per-slide vertical scroll, top-aligned so nothing is clipped */
  .slide{padding:50px 15px 38px;align-items:flex-start;overflow-y:auto;-webkit-overflow-scrolling:touch}
  .slide-inner{max-width:100%;min-width:0}
  /* collapse every multi-column grid; minmax(0,1fr)+min-width:0 lets wide children
     (white-space:pre code, long class names) shrink & scroll instead of stretching the slide */
  .grid2,.grid2-1,.grid3{grid-template-columns:minmax(0,1fr)!important;gap:14px!important}
  .grid5{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:9px!important}
  .dnums{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:10px!important}
  .grid2>*,.grid2-1>*,.grid3>*,.grid5>*,.dnums>*{min-width:0}
  /* schematics use full width */
  .svgm svg{max-height:48vh;width:100%}
  .svgwrap svg{max-height:44vh}
  /* wide Orange canvas + decision table scroll sideways instead of breaking layout */
  .owrap{overflow-x:auto;justify-content:flex-start}
  .owrap svg{min-width:680px;max-height:none}
  table.cmp{display:block;overflow-x:auto;white-space:nowrap}
  .code{font-size:.8rem;padding:11px 12px}
  .chartbox{height:40vh!important;max-height:none}
  .cover2{padding:30px 20px!important}
  .note,.obox{padding:11px 13px}
  #hint,#brand{display:none}
  #section-tag{font-size:.64rem;left:13px;top:9px;letter-spacing:.08em}
  #pageInfo{right:11px;bottom:9px;font-size:.72rem}
}
"""
dc.CSS = dc.CSS + DARK
dc.JS = dc.JS.replace(
    "Chart.defaults.color='#48597a';",
    "Chart.defaults.color='#b6c8b4';Chart.defaults.borderColor='rgba(255,255,255,.12)';")
# Touch-swipe navigation for phones (appended to THIS deck's engine copy only).
# Horizontal swipe = prev/next; vertical scroll untouched; skips interactive/scrollable areas.
MOBILE_JS = r"""
;(function(){
  var x0=0,y0=0,t0=0,track=false;
  document.addEventListener('touchstart',function(e){
    if(e.touches.length>1){track=false;return;}
    var t=e.changedTouches[0]; x0=t.clientX; y0=t.clientY; t0=Date.now(); track=true;
  },{passive:true});
  document.addEventListener('touchend',function(e){
    if(!track) return; track=false;
    if(e.target.closest('.no-nav,button,input,select,textarea,a,.chip,.opt,.bucket,.code,table,.owrap,.checklist')) return;
    var t=e.changedTouches[0], dx=t.clientX-x0, dy=t.clientY-y0, dt=Date.now()-t0;
    if(dt<700 && Math.abs(dx)>48 && Math.abs(dx)>Math.abs(dy)*1.5){ if(dx<0) next(); else prev(); }
  },{passive:true});
})();
"""
dc.JS = dc.JS + MOBILE_JS

# ============================================================ Python syntax highlighter
# Single-pass tokeniser: strings + keywords in ONE re.sub so the keyword pass never
# re-scans the <span> markup we insert (two passes corrupted class="st" -> class kw).
_TOK = re.compile(
    r"('[^']*'|\"[^\"]*\")"                                    # group 1: string literal
    r"|\b(from|import|as|for|in|def|return|if|else|elif|None|True|False|"
    r"and|or|not|with|lambda|print)\b")                       # group 2: keyword
def _tok_repl(m):
    if m.group(1) is not None:
        return '<span class="st">%s</span>' % m.group(1)
    return '<span class="kw">%s</span>' % m.group(2)
def pycode(src, title="Python · scikit-learn"):
    """Light, robust highlighter for the snippets we author (no '#' inside strings)."""
    lines = src.strip("\n").split("\n")
    rendered = []
    for ln in lines:
        code, sep, comment = ln.partition("#")
        e = _html.escape(code, quote=False)             # only & < >  (keep quotes literal)
        e = _TOK.sub(_tok_repl, e)                      # strings + keywords, one pass
        if sep:
            e += '<span class="cm">#%s</span>' % _html.escape(comment, quote=False)
        rendered.append(e)
    body = "\n".join(rendered)
    return ('<div class="codeh"><span class="dot"></span>%s</div>'
            '<div class="code">%s</div>') % (title, body)

def orange_box(items, title="Orange Data Mining 做法"):
    lis = "".join("<li>%s</li>" % x for x in items)
    return '<div class="obox"><div class="oh">🧩 %s</div><ul>%s</ul></div>' % (title, lis)

# ============================================================ method schematics (dark SVG)
SVG_LDA = r"""
<svg viewBox="0 0 380 230">
 <defs><marker id="al" markerWidth="9" markerHeight="9" refX="6" refY="4" orient="auto">
   <path d="M0 0 L7 4 L0 8 z" fill="#cbd9c6"/></marker></defs>
 <!-- two clouds -->
 <g fill="#5fd07f"><circle cx="70" cy="60" r="5"/><circle cx="92" cy="52" r="5"/><circle cx="84" cy="78" r="5"/>
   <circle cx="108" cy="66" r="5"/><circle cx="64" cy="86" r="5"/></g>
 <g fill="#e7ad4d"><circle cx="210" cy="150" r="5"/><circle cx="232" cy="138" r="5"/><circle cx="224" cy="166" r="5"/>
   <circle cx="248" cy="154" r="5"/><circle cx="200" cy="170" r="5"/></g>
 <!-- projection axis -->
 <line x1="40" y1="190" x2="300" y2="30" stroke="#cbd9c6" stroke-width="2" stroke-dasharray="2 4" marker-end="url(#al)"/>
 <text x="300" y="26" fill="#cbd9c6" font-size="13" font-weight="700">投影軸 LD1</text>
 <!-- projected marks (separated on the axis) -->
 <g><circle cx="120" cy="142" r="4" fill="#5fd07f"/><circle cx="135" cy="133" r="4" fill="#5fd07f"/>
    <circle cx="150" cy="124" r="4" fill="#5fd07f"/></g>
 <g><circle cx="205" cy="90" r="4" fill="#e7ad4d"/><circle cx="220" cy="81" r="4" fill="#e7ad4d"/>
    <circle cx="235" cy="72" r="4" fill="#e7ad4d"/></g>
 <text x="70" y="42" fill="#9fb39c" font-size="12">臺灣</text>
 <text x="250" y="190" fill="#cdb98a" font-size="12">境外</text>
 <text x="60" y="218" fill="#b6c8b4" font-size="12.5">組間最遠 · 組內最密</text>
</svg>"""

SVG_RIDGE = r"""
<svg viewBox="0 0 380 230">
 <defs><marker id="ar" markerWidth="9" markerHeight="9" refX="6" refY="4" orient="auto">
   <path d="M0 0 L7 4 L0 8 z" fill="#e7ad4d"/></marker></defs>
 <text x="64" y="26" fill="#9fb39c" font-size="12.5" text-anchor="middle">無懲罰（亂、過擬合）</text>
 <text x="300" y="26" fill="#9fb39c" font-size="12.5" text-anchor="middle">＋L2 收縮（穩）</text>
 <line x1="20" y1="170" x2="150" y2="170" stroke="#2b3c32" stroke-width="1.5"/>
 <line x1="232" y1="170" x2="362" y2="170" stroke="#2b3c32" stroke-width="1.5"/>
 <!-- wild coefficients -->
 <g fill="#5fd07f"><rect x="30" y="70" width="16" height="100"/><rect x="54" y="120" width="16" height="50"/>
   <rect x="78" y="46" width="16" height="124"/><rect x="102" y="132" width="16" height="38"/>
   <rect x="126" y="92" width="16" height="78"/></g>
 <!-- shrunk coefficients -->
 <g fill="#e7ad4d"><rect x="242" y="132" width="16" height="38"/><rect x="266" y="146" width="16" height="24"/>
   <rect x="290" y="120" width="16" height="50"/><rect x="314" y="150" width="16" height="20"/>
   <rect x="338" y="138" width="16" height="32"/></g>
 <line x1="160" y1="110" x2="226" y2="110" stroke="#e7ad4d" stroke-width="2.4" marker-end="url(#ar)"/>
 <text x="193" y="100" fill="#e7ad4d" font-size="12.5" text-anchor="middle" font-weight="700">L2 懲罰</text>
 <text x="64" y="200" fill="#b6c8b4" font-size="12" text-anchor="middle">係數大、隨雜訊亂跳</text>
 <text x="300" y="200" fill="#b6c8b4" font-size="12" text-anchor="middle">係數變小、更穩健</text>
</svg>"""

SVG_RF = r"""
<svg viewBox="0 0 380 230">
 <defs><marker id="af" markerWidth="9" markerHeight="9" refX="6" refY="4" orient="auto">
   <path d="M0 0 L7 4 L0 8 z" fill="#6f8472"/></marker></defs>
 <g stroke="#5fd07f" stroke-width="2" fill="none">
  <g transform="translate(28,30)"><circle cx="30" cy="6" r="6" fill="#1a241e"/><line x1="30" y1="12" x2="14" y2="36"/>
    <line x1="30" y1="12" x2="46" y2="36"/><circle cx="14" cy="42" r="6" fill="#1a241e"/><circle cx="46" cy="42" r="6" fill="#1a241e"/></g>
  <g transform="translate(120,30)"><circle cx="30" cy="6" r="6" fill="#1a241e"/><line x1="30" y1="12" x2="14" y2="36"/>
    <line x1="30" y1="12" x2="46" y2="36"/><circle cx="14" cy="42" r="6" fill="#1a241e"/><circle cx="46" cy="42" r="6" fill="#1a241e"/></g>
  <g transform="translate(212,30)"><circle cx="30" cy="6" r="6" fill="#1a241e"/><line x1="30" y1="12" x2="14" y2="36"/>
    <line x1="30" y1="12" x2="46" y2="36"/><circle cx="14" cy="42" r="6" fill="#1a241e"/><circle cx="46" cy="42" r="6" fill="#1a241e"/></g>
 </g>
 <text x="58" y="96" fill="#9fb39c" font-size="11" text-anchor="middle">樹1→臺灣</text>
 <text x="150" y="96" fill="#9fb39c" font-size="11" text-anchor="middle">樹2→臺灣</text>
 <text x="242" y="96" fill="#cdb98a" font-size="11" text-anchor="middle">樹3→境外</text>
 <text x="328" y="58" fill="#cbd9c6" font-size="12" text-anchor="middle">…300 棵</text>
 <g stroke="#6f8472" stroke-width="2.2" fill="none" marker-end="url(#af)">
   <path d="M58 100 C 90 130,150 130,182 150"/><path d="M150 100 L 190 148"/><path d="M242 100 C 220 130,210 132,200 148"/></g>
 <rect x="118" y="152" width="150" height="44" rx="11" fill="rgba(95,208,127,.16)" stroke="#5fd07f" stroke-width="2"/>
 <text x="193" y="172" fill="#5fd07f" font-size="14" font-weight="800" text-anchor="middle">多數決投票</text>
 <text x="193" y="190" fill="#b6c8b4" font-size="11.5" text-anchor="middle">→ 臺灣</text>
 <text x="193" y="220" fill="#b6c8b4" font-size="12.5" text-anchor="middle">很多棵「看法略不同」的樹，一起投票</text>
</svg>"""

SVG_BOOST = r"""
<svg viewBox="0 0 380 230">
 <defs><marker id="ab" markerWidth="9" markerHeight="9" refX="6" refY="4" orient="auto">
   <path d="M0 0 L7 4 L0 8 z" fill="#6f8472"/></marker></defs>
 <g stroke="#e7ad4d" stroke-width="2" fill="none">
  <g transform="translate(20,52)"><circle cx="24" cy="6" r="6" fill="#1a241e"/><line x1="24" y1="12" x2="12" y2="32"/>
    <line x1="24" y1="12" x2="36" y2="32"/><circle cx="12" cy="38" r="6" fill="#1a241e"/><circle cx="36" cy="38" r="6" fill="#1a241e"/></g>
  <g transform="translate(150,52)"><circle cx="24" cy="6" r="6" fill="#1a241e"/><line x1="24" y1="12" x2="12" y2="32"/>
    <line x1="24" y1="12" x2="36" y2="32"/><circle cx="12" cy="38" r="6" fill="#1a241e"/><circle cx="36" cy="38" r="6" fill="#1a241e"/></g>
  <g transform="translate(280,52)"><circle cx="24" cy="6" r="6" fill="#1a241e"/><line x1="24" y1="12" x2="12" y2="32"/>
    <line x1="24" y1="12" x2="36" y2="32"/><circle cx="12" cy="38" r="6" fill="#1a241e"/><circle cx="36" cy="38" r="6" fill="#1a241e"/></g>
 </g>
 <text x="44" y="116" fill="#9fb39c" font-size="11.5" text-anchor="middle">樹1</text>
 <text x="174" y="116" fill="#9fb39c" font-size="11.5" text-anchor="middle">樹2 補錯</text>
 <text x="304" y="116" fill="#9fb39c" font-size="11.5" text-anchor="middle">樹3 再補錯</text>
 <g stroke="#6f8472" stroke-width="2.4" fill="none" marker-end="url(#ab)">
   <path d="M92 78 h44"/><path d="M222 78 h44"/></g>
 <text x="114" y="68" fill="#ef9b9b" font-size="11" text-anchor="middle">殘差</text>
 <text x="244" y="68" fill="#ef9b9b" font-size="11" text-anchor="middle">殘差</text>
 <rect x="96" y="150" width="190" height="44" rx="11" fill="rgba(231,173,77,.16)" stroke="#e7ad4d" stroke-width="2"/>
 <text x="191" y="170" fill="#e7ad4d" font-size="14" font-weight="800" text-anchor="middle">Σ 逐步加總</text>
 <text x="191" y="188" fill="#b6c8b4" font-size="11.5" text-anchor="middle">一棵接一棵、愈來愈準</text>
 <g stroke="#6f8472" stroke-width="2.2" fill="none" marker-end="url(#ab)">
   <path d="M44 96 C 60 130,150 130,150 148"/><path d="M174 96 L 180 148"/><path d="M304 96 C 290 130,210 132,212 148"/></g>
 <text x="191" y="220" fill="#b6c8b4" font-size="12.5" text-anchor="middle">強，但小資料容易過擬合</text>
</svg>"""

SVG_SVM = r"""
<svg viewBox="0 0 380 230">
 <!-- margins -->
 <line x1="60" y1="210" x2="300" y2="20" stroke="#cbd9c6" stroke-width="2.4"/>
 <line x1="30" y1="200" x2="270" y2="10" stroke="#83977f" stroke-width="1.4" stroke-dasharray="4 4"/>
 <line x1="90" y1="220" x2="330" y2="30" stroke="#83977f" stroke-width="1.4" stroke-dasharray="4 4"/>
 <!-- class TW (upper-left) -->
 <g fill="#5fd07f"><circle cx="70" cy="50" r="5"/><circle cx="96" cy="40" r="5"/><circle cx="60" cy="84" r="5"/>
   <circle cx="118" cy="64" r="5"/></g>
 <!-- support vectors (ringed) -->
 <circle cx="104" cy="96" r="7" fill="#5fd07f" stroke="#ecf4ea" stroke-width="2"/>
 <!-- class FG (lower-right) -->
 <g fill="#e7ad4d"><circle cx="250" cy="150" r="5"/><circle cx="278" cy="140" r="5"/><circle cx="300" cy="170" r="5"/>
   <circle cx="320" cy="150" r="5"/></g>
 <circle cx="222" cy="128" r="7" fill="#e7ad4d" stroke="#ecf4ea" stroke-width="2"/>
 <text x="300" y="16" fill="#cbd9c6" font-size="12.5" font-weight="700">分界線</text>
 <text x="150" y="205" fill="#b6c8b4" font-size="12" text-anchor="middle">↔ 最大間隔 margin</text>
 <text x="40" y="40" fill="#9fb39c" font-size="12">臺灣</text>
 <text x="300" y="200" fill="#cdb98a" font-size="12">境外</text>
 <text x="150" y="226" fill="#83977f" font-size="11.5" text-anchor="middle">⊙ 支援向量決定邊界 · 核函數可處理非線性</text>
</svg>"""

# ============================================================ Orange canvas (faithful-ish)
def owidget(x, y, label, sub, accent="#5fd07f", glyph=""):
    g = ('<g transform="translate(%d,%d)">'
         '<rect x="0" y="0" width="108" height="48" rx="11" fill="#1a241e" stroke="%s" stroke-width="2"/>'
         '<rect x="0" y="0" width="108" height="7" rx="3.5" fill="%s"/>'
         '<text x="54" y="30" text-anchor="middle" fill="#ecf4ea" font-size="13" font-weight="800">%s</text>'
         '<text x="54" y="66" text-anchor="middle" fill="#9fb39c" font-size="10.5">%s</text>'
         '%s</g>') % (x, y, accent, accent, label, sub, glyph)
    return g

SVG_ORANGE = (
 '<svg viewBox="0 0 940 430">'
 '<defs><marker id="ao" markerWidth="9" markerHeight="9" refX="6" refY="4" orient="auto">'
 '<path d="M0 0 L7 4 L0 8 z" fill="#7da17f"/></marker></defs>'
 # top pipeline
 + owidget(20, 40, "File", "tea CSV", "#5fd07f")
 + owidget(190, 40, "Preprocess", "Normalize 標準化", "#5fd07f")
 + owidget(372, 40, "Test &amp; Score", "留一法 LOO-CV", "#e7ad4d")
 + owidget(560, 40, "Confusion", "Matrix 混淆矩陣", "#e7ad4d")
 + owidget(748, 40, "Data Table", "看資料", "#5fd07f")
 # learners row
 + owidget(150, 250, "Random", "Forest 隨機森林", "#5fd07f")
 + owidget(300, 250, "Gradient", "Boosting 提升", "#5fd07f")
 + owidget(450, 250, "SVM", "支援向量機", "#5fd07f")
 + owidget(600, 250, "Logistic", "Reg. (Ridge L2 / 線性)", "#e7ad4d")
 # connections
 + '<g stroke="#7da17f" stroke-width="2.2" fill="none" marker-end="url(#ao)">'
 + '<path d="M128 64 h60"/>'                       # File -> Preprocess
 + '<path d="M298 64 h72"/>'                       # Preprocess -> Test&Score
 + '<path d="M480 64 h78"/>'                       # Test&Score -> Confusion
 + '<path d="M128 56 C 700 -10,700 -10,748 52"/>'  # File -> Data Table (top arc)
 + '<path d="M204 250 C 300 180,380 150,418 92"/>' # RF -> Test&Score
 + '<path d="M354 250 C 390 190,400 160,430 92"/>' # Boosting -> Test&Score
 + '<path d="M504 250 C 480 190,470 150,444 92"/>' # SVM -> Test&Score
 + '<path d="M654 250 C 620 180,520 150,470 90"/>' # LogReg -> Test&Score
 + '</g>'
 '<text x="470" y="200" text-anchor="middle" fill="#b6c8b4" font-size="12.5">4 個 Learner 一起接進 Test &amp; Score，表格直接比正確率</text>'
 '</svg>')

# ============================================================ bar chart (real LOO-CV)
def barcolor(v):
    return "#5fd07f" if v >= 95 else ("#e7ad4d" if v >= 90 else "#ef7373")
_BARVALS = [SCORES[m]["acc"] for m in ["LDA", "Ridge", "Random Forest", "Boosting", "SVM"]]
BAR_SCRIPT = ("""
<script>(function(){
  var V=%s, C=%s;
  function draw(){
    if(typeof Chart==="undefined") return setTimeout(draw,80);
    var el=document.getElementById("chart_bars"); if(!el||el._done) return;
    var sl=el.closest(".slide"); if(sl&&!sl.classList.contains("active")) return;  // draw only when container is sized
    el._done=1;
    new Chart(el,{type:"bar",
      data:{labels:["LDA","Ridge","Random\\nForest","Boosting","SVM"],
        datasets:[{label:"留一法正確率 %%",data:V,backgroundColor:C,borderRadius:7,
          borderColor:"#0e1512",borderWidth:1.5,maxBarThickness:74}]},
      options:{responsive:true,maintainAspectRatio:false,
        plugins:{legend:{display:false},
          tooltip:{callbacks:{label:function(c){return c.parsed.y.toFixed(0)+"%%";}}}},
        scales:{y:{min:0,max:100,ticks:{color:"#b6c8b4",callback:function(v){return v+"%%";}},
                   grid:{color:"rgba(255,255,255,.08)"},title:{display:true,text:"LOO-CV 正確率",color:"#cde0c9"}},
                x:{ticks:{color:"#cde0c9",font:{size:13,weight:"700"}},grid:{display:false}}}},
      plugins:[{id:"vlab",afterDatasetsDraw:function(ch){var c=ch.ctx,m=ch.getDatasetMeta(0);
        c.save();c.font="800 14px 'JetBrains Mono',monospace";c.fillStyle="#ecf4ea";c.textAlign="center";
        m.data.forEach(function(b,i){c.fillText(V[i].toFixed(0)+"%%",b.x,b.y-8);});c.restore();}}]});
  }
  function arm(){
    var el=document.getElementById("chart_bars"); if(!el) return setTimeout(arm,100);
    var sl=el.closest(".slide");
    if(sl) new MutationObserver(draw).observe(sl,{attributes:true,attributeFilter:["class"]});
    draw();
  }
  if(document.readyState!=="loading") arm(); else document.addEventListener("DOMContentLoaded",arm);
})();</script>""" % (json.dumps(_BARVALS), json.dumps([barcolor(v) for v in _BARVALS])))

# ============================================================ slides
S = []
def add(sec, inner, attr=""):
    S.append((sec, attr, inner))

# ---- 1 cover ----
add(MOT, '<div class="cover2">'
  '<div class="kicker" style="color:#7be39a">食品分析 · 化學計量學 × 機器學習</div>'
  '<h1 style="font-size:clamp(2rem,5.2vw,4rem);font-weight:900;line-height:1.06;color:#fff;letter-spacing:-.02em">'
  '五種模型，<br>幫茶葉<span style="color:#7be39a">驗明正身</span></h1>'
  '<div style="font-family:\'JetBrains Mono\',monospace;color:#7be39a;margin-top:12px;letter-spacing:.05em;font-size:clamp(.85rem,1.6vw,1.2rem)">'
  'LDA · Ridge · Random Forest · Boosting · SVM</div>'
  '<div style="color:rgba(255,255,255,.82);margin-top:16px;font-size:clamp(.92rem,1.5vw,1.18rem);line-height:1.6">'
  '用 14 元素指紋判別「臺灣 vs 境外」茶　·　每種模型都教<strong style="color:#fff">兩條路</strong>：'
  'Python 寫程式 × Orange 拉積木</div>'
  '<div style="margin-top:22px">'
  + "".join('<span class="pill" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.25);color:#eafff0">%s</span>' % x
            for x in ["監督式分類", "標準化", "留一法 LOO-CV", "scikit-learn", "Orange"]) + '</div>'
  '<div style="margin-top:18px;color:rgba(255,255,255,.6);font-size:clamp(.8rem,1.3vw,1rem)">接續 · 茶葉多重元素檢驗 TFDAF0032.00</div>'
  '</div>', ' data-full="1"')

# ---- 2 hook ----
add(MOT, '<div style="text-align:center">'
  '<div class="kicker" style="justify-content:center">承上 · 指紋拿到了，然後呢？</div>'
  '<div class="hook">14 個元素數字攤在眼前，<br><span class="hi">電腦怎麼自己判台灣／境外？</span></div>'
  '<p class="subtitle" style="max-width:860px;margin:22px auto 0">人腦看 2 個元素還行，看 <strong>14 維</strong>就投降了。'
  '我們需要一個能<strong>自動找出分界</strong>的工具——這就是<span class="em">分類器 (classifier)</span>，機器學習的核心。</p>'
  '<div style="margin-top:24px"><span class="pill">14 維太難用眼睛看</span><span class="pill">要能自動判</span>'
  '<span class="pill">要能說多準</span><span class="pill">要能換新樣本就用</span></div>'
  '<div class="note" style="max-width:780px;margin:24px auto 0;text-align:left">本片把 TFDAF0032.00 列的 <strong>5 種統計／機器學習模型</strong>一字排開，'
  '同一份茶葉資料，看它們各自怎麼學會「畫出那條產地分界線」。</div></div>')

# ---- 3 core proposition: one data, five models, two paths ----
add(MOT, dc.kt("本片怎麼學", "一份資料　×　五模型　×　<span class='hi'>兩條路</span>") +
  '<div class="grid3" style="margin-top:18px;gap:18px">' +
  dc.card("📋", "同一份資料", "茶葉 20 樣本 × 元素指紋，標籤＝臺灣／境外。所有模型公平比", "b") +
  dc.card("🤖", "五種模型", "LDA·Ridge（傳統線性）＋ RF·Boosting·SVM（機器學習）", "a") +
  dc.card("🛣️", "兩條實作路", "🐍 Python 寫幾行程式　🧩 Orange 拉積木不寫碼", "b") + '</div>' +
  '<div class="note" style="margin-top:18px">每個模型的詳解頁都長一樣：<strong>左邊一張圖看直覺</strong>、'
  '<strong>右邊 Python 程式 + Orange 積木</strong>。看完你能在兩種工具裡都把它跑起來。</div>')

# ---- 4 what is supervised classification + why LOO-CV ----
add(ATT, dc.kt("先懂這件事", "監督式分類：給<span class='hi'>答案</span>學分界") +
  '<div class="grid2" style="margin-top:12px;align-items:start">' +
  '<div><ul class="clean">'
  "<li><strong>特徵 X</strong>：每個茶樣的 14 個元素含量（一列＝一個樣本）</li>"
  "<li><strong>標籤 y</strong>：這個樣本的產地（臺灣＝1／境外＝0）</li>"
  "<li>模型從「X→y」的例子中<strong>學出一條分界</strong>，之後拿新樣本就能判</li>"
  "<li>5 種模型差在<strong>「怎麼畫這條界」</strong>——直線、曲線、還是一堆樹投票</li>"
  '</ul></div>' +
  '<div class="note"><strong>怎麼知道模型「真的會」而不是死背？</strong><br>'
  '不能看訓練資料的分數（會<strong>過擬合</strong>、虛高）。本片用<span class="em">留一法 LOO-CV</span>：'
  '每次留 1 個樣本當考題、其餘 19 個當課本，輪流考 20 次，平均才是「對新樣本」的真實實力。</div>' +
  '</div>' +
  '<div class="dnums"><div class="dnum"><div class="v">20</div><div class="k">茶樣（臺灣 12 / 境外 8）</div></div>'
  '<div class="dnum"><div class="v">13</div><div class="k">微量元素特徵（T 子集）</div></div>'
  '<div class="dnum"><div class="v">20 折</div><div class="k">留一法輪流當考題</div></div></div>')

# ---- 5 common starting point: standardize + pipeline ----
add(ATT, dc.kt("共同起點", "先<span class='hi'>標準化</span>，再交給任何模型") +
  '<div class="grid2" style="margin-top:12px;align-items:start">' +
  '<div>' +
  '<div class="note" style="margin-bottom:11px"><strong>為什麼要標準化？</strong><br>元素單位差很多：'
  'P/K/Ca 是 <strong>%</strong>、Sr/Pb 是 <strong>mg/kg</strong>。不處理的話，數值大的元素會「霸佔」距離與係數，'
  '小元素的訊號被蓋掉。標準化把每個元素轉成<strong>平均 0、標準差 1</strong>，大家站同一起跑線。</div>' +
  '<div class="obox" style="border-left-color:var(--accent)"><div class="oh" style="color:var(--accent)">⚠️ 別讓答案偷看</div>'
  '<ul><li>標準化要<b>包進交叉驗證</b>裡：只用訓練折算平均/標準差</li>'
  '<li>Python 用 <b>Pipeline</b>、Orange 把 <b>Preprocess</b> 接進 Test&amp;Score，都是同一個道理</li></ul></div>' +
  '</div>' +
  '<div>' + pycode(
    "from sklearn.preprocessing import StandardScaler\n"
    "from sklearn.pipeline import make_pipeline\n"
    "from sklearn.model_selection import cross_val_predict, LeaveOneOut\n\n"
    "# 標準化 + 模型 綁成一條 pipeline，避免資訊洩漏\n"
    "pipe = make_pipeline(StandardScaler(), model)\n"
    "pred = cross_val_predict(pipe, X, y, cv=LeaveOneOut())",
    title="所有模型共用的骨架") +
  '</div></div>')

# ---- 6 five models overview ----
add(ATT, dc.kt("五位選手", "兩大家族，<span class='hi'>同場較勁</span>") +
  '<div class="grid5" style="margin-top:18px">' +
  '<div class="minicard b"><div class="mt">LDA</div><div class="mb">線性判別<br><span style="color:var(--accent)">傳統統計 · 線性</span></div></div>' +
  '<div class="minicard b"><div class="mt">Ridge</div><div class="mb">脊迴歸分類<br><span style="color:var(--accent)">傳統統計 · 線性</span></div></div>' +
  '<div class="minicard a"><div class="mt">Random Forest</div><div class="mb">隨機森林<br><span style="color:var(--accent-2)">機器學習 · 樹集成</span></div></div>' +
  '<div class="minicard a"><div class="mt">Boosting</div><div class="mb">梯度提升<br><span style="color:var(--accent-2)">機器學習 · 樹集成</span></div></div>' +
  '<div class="minicard a"><div class="mt">SVM</div><div class="mb">支援向量機<br><span style="color:var(--accent-2)">機器學習 · 間隔/核</span></div></div>' +
  '</div>' +
  '<div class="grid2" style="margin-top:18px;gap:18px">' +
  '<div class="note" style="border-left-color:var(--accent)"><strong>左二｜傳統統計（線性）</strong><br>'
  'LDA、Ridge 畫的是<strong>直線分界</strong>，係數可解讀、小樣本穩。是統計學的老將。</div>' +
  '<div class="note"><strong>右三｜機器學習</strong><br>'
  'RF／Boosting 用<strong>很多決策樹</strong>抓非線性與交互作用；SVM 找<strong>最大間隔</strong>、核函數可彎曲分界。</div>' +
  '</div>')

# ---- 7 LDA detail ----
add(ATT, dc.kt("模型 ① · 傳統統計 · 線性", "LDA：找一條<span class='hi'>投影軸</span>拉開兩群") +
  '<div class="grid2" style="margin-top:8px;align-items:start">' +
  '<div><div class="svgm">' + SVG_LDA + '</div>'
  '<div class="note" style="margin-top:8px"><strong>一句話：</strong>找一個投影方向，讓投影後'
  '<strong>組間距離最大、組內散布最小</strong>，兩群自然分兩邊。</div></div>' +
  '<div>' + pycode(
    "from sklearn.discriminant_analysis import \\\n"
    "    LinearDiscriminantAnalysis\n"
    "clf = LinearDiscriminantAnalysis()\n"
    "clf.fit(X_std, y)        # X_std=標準化元素, y=產地\n"
    "clf.predict(X_new)       # 判新茶樣") +
  orange_box([
    "Orange <b>無原生 LDA 分類積木</b>",
    "改用 <b>Logistic Regression</b> 積木（同為線性分界，效果近似）",
    "想看 LDA「投影圖」可另裝 add-on 的投影視覺化",
  ]) +
  '<div style="margin-top:9px"><span class="pill">線性</span><span class="pill">可解釋</span>'
  '<span class="pill" style="border-color:var(--accent);color:var(--accent)">LOO-CV 95%</span></div>' +
  '</div></div>')

# ---- 8 Ridge detail ----
add(ATT, dc.kt("模型 ② · 傳統統計 · 線性", "Ridge：加 L2 懲罰，<span class='hi'>抗過擬合</span>") +
  '<div class="grid2" style="margin-top:8px;align-items:start">' +
  '<div><div class="svgm">' + SVG_RIDGE + '</div>'
  '<div class="note" style="margin-top:8px"><strong>一句話：</strong>線性模型 + <strong>L2 懲罰</strong>把係數「收縮」變小，'
  '不讓少數雜訊元素把分界帶歪 → 更穩、更能用在新樣本。</div></div>' +
  '<div>' + pycode(
    "from sklearn.linear_model import RidgeClassifier\n"
    "clf = RidgeClassifier(alpha=1.0)  # alpha 越大懲罰越強\n"
    "clf.fit(X_std, y)\n"
    "clf.predict(X_new)") +
  orange_box([
    "Orange <b>無原生 Ridge 分類積木</b>",
    "用 <b>Logistic Regression</b> 積木 → Regularization 選 <b>Ridge (L2)</b>",
    "調 <b>C</b>：C 越小＝懲罰越強（與 alpha 相反方向）",
  ]) +
  '<div style="margin-top:9px"><span class="pill">線性</span><span class="pill">正則化</span>'
  '<span class="pill" style="border-color:var(--accent);color:var(--accent)">LOO-CV 100%</span></div>' +
  '</div></div>')

# ---- 9 Random Forest detail ----
add(ATT, dc.kt("模型 ③ · 機器學習 · 樹集成", "Random Forest：一片<span class='hi'>樹林投票</span>") +
  '<div class="grid2" style="margin-top:8px;align-items:start">' +
  '<div><div class="svgm">' + SVG_RF + '</div>'
  '<div class="note" style="margin-top:8px"><strong>一句話：</strong>種很多棵「各看資料不同子集、不同元素」的決策樹，'
  '最後<strong>多數決投票</strong>。能抓非線性、還會告訴你<strong>哪個元素最重要</strong>。</div></div>' +
  '<div>' + pycode(
    "from sklearn.ensemble import RandomForestClassifier\n"
    "clf = RandomForestClassifier(n_estimators=300,\n"
    "                             random_state=0)\n"
    "clf.fit(X_std, y)\n"
    "clf.feature_importances_   # 哪些元素最關鍵") +
  orange_box([
    "Orange 有原生 <b>Random Forest</b> 積木 ✓",
    "設 <b>Number of trees</b>（樹的數量）即可",
    "接 <b>Test &amp; Score</b> 比正確率、接 <b>Confusion Matrix</b> 看錯在哪",
  ]) +
  '<div style="margin-top:9px"><span class="pill">非線性</span><span class="pill">特徵重要度</span>'
  '<span class="pill" style="border-color:var(--accent);color:var(--accent)">LOO-CV 95%</span></div>' +
  '</div></div>')

# ---- 10 Boosting detail ----
add(ATT, dc.kt("模型 ④ · 機器學習 · 樹集成", "Boosting：一棵<span class='hi'>接著一棵補錯</span>") +
  '<div class="grid2" style="margin-top:8px;align-items:start">' +
  '<div><div class="svgm">' + SVG_BOOST + '</div>'
  '<div class="note" style="margin-top:8px"><strong>一句話：</strong>樹不是各自獨立，而是<strong>一棵接一棵</strong>，'
  '每棵專門修正前一棵的<strong>錯誤（殘差）</strong>，逐步加總變強。</div></div>' +
  '<div>' + pycode(
    "from sklearn.ensemble import \\\n"
    "    GradientBoostingClassifier\n"
    "clf = GradientBoostingClassifier(random_state=0)\n"
    "clf.fit(X_std, y)\n"
    "clf.predict(X_new)") +
  orange_box([
    "Orange 有原生 <b>Gradient Boosting</b> 積木 ✓（另有 <b>AdaBoost</b>）",
    "可選底層：scikit-learn / XGBoost / CatBoost",
    "<b>強，但小資料容易過擬合</b> → 本片 20 樣本只拿 85%（最低）",
  ]) +
  '<div style="margin-top:9px"><span class="pill">非線性</span><span class="pill">序列集成</span>'
  '<span class="pill" style="border-color:var(--bad);color:var(--bad)">LOO-CV 85%</span></div>' +
  '</div></div>')

# ---- 11 SVM detail ----
add(ATT, dc.kt("模型 ⑤ · 機器學習 · 間隔/核", "SVM：找一條<span class='hi'>間隔最大</span>的界") +
  '<div class="grid2" style="margin-top:8px;align-items:start">' +
  '<div><div class="svgm">' + SVG_SVM + '</div>'
  '<div class="note" style="margin-top:8px"><strong>一句話：</strong>在兩群之間找一條<strong>「左右留白最大」</strong>的分界線；'
  '邊界只由少數<strong>支援向量</strong>決定，<strong>核函數</strong>還能把分界彎成曲線。</div></div>' +
  '<div>' + pycode(
    "from sklearn.svm import SVC\n"
    "clf = SVC(kernel='rbf', C=1.0, gamma='scale')\n"
    "clf.fit(X_std, y)        # SVM 對標準化特別敏感\n"
    "clf.predict(X_new)") +
  orange_box([
    "Orange 有原生 <b>SVM</b> 積木 ✓",
    "選 <b>Kernel</b>（RBF 非線性 / Linear 線性）、調 <b>C</b>、<b>gamma</b>",
    "務必先接 <b>Preprocess→Normalize</b>，SVM 沒標準化會很差",
  ]) +
  '<div style="margin-top:9px"><span class="pill">線性或核</span><span class="pill">小樣本佳</span>'
  '<span class="pill" style="border-color:var(--accent);color:var(--accent)">LOO-CV 100%</span></div>' +
  '</div></div>')

# ---- 12 comparison bar chart (real) ----
add(ATT, dc.kt("攤牌 · 同一份資料", "誰最準？答案<span class='hi'>可能跌破眼鏡</span>") +
  '<div class="grid2" style="margin-top:10px;grid-template-columns:1.45fr .55fr;align-items:stretch">' +
  '<div class="chartbox" style="height:50vh"><canvas id="chart_bars"></canvas></div>' +
  '<div style="display:flex;flex-direction:column;justify-content:center">' +
  '<div class="note" style="border-left-color:var(--accent)"><strong>看出來了嗎？</strong>'
  '最「高級」的 <strong style="color:var(--bad)">Boosting 反而最低（85%）</strong>，'
  '樸素的 <strong style="color:var(--accent)">Ridge／SVM 卻滿分</strong>。<br><br>'
  '<strong>為什麼？</strong>資料只有 20 筆——集成樹（尤其 Boosting）<strong>胃口大</strong>、'
  '餵不飽就<strong>過擬合</strong>；線性模型在小而乾淨的資料上<strong>又穩又準</strong>。</div>' +
  '<div class="cap" style="text-align:left;margin-top:12px;border-top:1px solid var(--line);padding-top:9px">'
  '真實留一法結果，由 <span class="mono">tea_five_models_demo.py</span> 實跑、可重現（微量元素 T13）。</div>' +
  '</div></div>' + BAR_SCRIPT)

# ---- 13 game: match sklearn class to method (bucket) ----
add(ATT, dc.game_bucket_inner("gmatch", "互動 ①", "把程式類別配到對的模型", 5,
    "下面是 scikit-learn 的 5 個類別名稱，把每個拖（點選→點桶）到它對應的模型。"),
    ' data-game="gmatch"')

# ---- 14 Orange full workflow ----
add(ACT, dc.kt("路線 A · 不寫程式", "Orange：把模型<span class='hi'>拉成一張圖</span>") +
  '<div class="owrap" style="margin-top:4px">' + SVG_ORANGE + '</div>' +
  '<div class="grid2" style="margin-top:12px;gap:18px">' +
  '<div class="obox"><div class="oh">🧩 五個積木串起來</div><ul>'
  '<li><b>File</b> 讀 tea CSV → <b>Select Columns</b> 設元素為特徵、origin 為 target</li>'
  '<li><b>Preprocess</b>（Normalize）→ <b>Test &amp; Score</b>（Cross validation 設 LOO）</li>'
  '<li>把 <b>Random Forest／Gradient Boosting／SVM／Logistic Regression</b> 接進去</li>'
  '<li><b>Confusion Matrix</b> 看哪些茶被判錯</li></ul></div>' +
  '<div class="note"><strong>誠實提醒</strong>：Orange 沒有現成的 <strong>LDA／Ridge 分類</strong>積木；'
  '上圖用 <strong>Logistic Regression</strong>（可選 Ridge L2 正則化）代表「線性分界」這一家。'
  'RF／Gradient Boosting／SVM 則都是<strong>原生積木</strong>，零程式碼即可比較。</div>' +
  '</div>')

# ---- 15 Python full workflow ----
add(ACT, dc.kt("路線 B · 寫幾行程式", "Python：<span class='hi'>一個迴圈</span>比完五模型") +
  '<div class="grid2" style="margin-top:10px;align-items:start;grid-template-columns:1.25fr .75fr">' +
  '<div>' + pycode(
    "from sklearn.discriminant_analysis import LinearDiscriminantAnalysis\n"
    "from sklearn.linear_model import RidgeClassifier\n"
    "from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier\n"
    "from sklearn.svm import SVC\n\n"
    "models = {\n"
    "    'LDA':   LinearDiscriminantAnalysis(),\n"
    "    'Ridge': RidgeClassifier(),\n"
    "    'RF':    RandomForestClassifier(n_estimators=300, random_state=0),\n"
    "    'Boost': GradientBoostingClassifier(random_state=0),\n"
    "    'SVM':   SVC(kernel='rbf'),\n"
    "}\n"
    "for name, model in models.items():\n"
    "    pipe = make_pipeline(StandardScaler(), model)\n"
    "    pred = cross_val_predict(pipe, X, y, cv=LeaveOneOut())\n"
    "    print(name, accuracy_score(y, pred))",
    title="五模型一起跑 · 完整可執行") +
  '</div>' +
  '<div><div class="note" style="border-left-color:var(--accent)"><strong>程式路的好處</strong><br>'
  '5 種模型只差<strong>字典裡一行</strong>，換模型／調參數／加指標都很快，'
  '全部 <strong>5 種</strong>都有現成類別（含 LDA、Ridge）。</div>' +
  '<div class="obox" style="margin-top:11px"><div class="oh">📁 檔案都在 dataset/</div><ul>'
  '<li><b>tea_five_models_demo.py</b> — 上面這段的完整版（本片數字來源）</li>'
  '<li><b>tea_origin_teaching.csv</b> — 20 樣本 × 元素</li>'
  '<li>執行：<b>python tea_five_models_demo.py</b></li></ul></div>' +
  '</div></div>')

# ---- 16 which model when (sortable cmp) ----
CMP_COLS = [{"k": "m", "t": "s", "label": "模型"}, {"k": "fam", "t": "s", "label": "家族"},
            {"k": "sk", "t": "s", "label": "scikit-learn"}, {"k": "og", "t": "s", "label": "Orange 積木"},
            {"k": "acc", "t": "n", "label": "本片正確率"}, {"k": "when", "t": "s", "label": "什麼時候用"}]
add(ACT, dc.cmp_inner("該用<span class='hi'>哪一個</span>？一張表收齊", CMP_COLS,
    "點欄位標題可排序（試以「本片正確率」）。沒有最強模型，只有最適合資料的模型。",
    kicker="決策參考 · 可排序") + ' ' +
    '<div class="cap" style="margin-top:8px">小樣本＋要解釋 → 線性（LDA/Ridge/SVM）；要抓非線性或看元素重要度 → RF/Boosting（但要夠多資料）。</div>',
    ' data-game="cmp"')

# ---- 17 MCQ ----
add(ACT, dc.game_mcq_inner("gq", "互動 ②", "觀念速測（5 題）", 5), ' data-game="gq"')

# ---- 18 hands-on (two paths) ----
add(ACT, dc.kt("動手做 · 兩條路都跑一次", "從<span class='hi'>看懂</span>到<span class='hi'>跑出來</span>") +
  '<div class="grid2" style="margin-top:16px;gap:22px">' +
  '<div class="obox" style="border-left-color:#7be39a"><div class="oh" style="color:#7be39a">🐍 Python 路</div><ul>'
  '<li>裝 <b>scikit-learn</b>：<span class="mono">pip install scikit-learn pandas</span></li>'
  '<li>進 <b>dataset/</b> 跑 <b>python tea_five_models_demo.py</b></li>'
  '<li>看終端機印出 5 模型的 accuracy／precision／recall</li>'
  '<li>改字典加一個模型、或換特徵子集，再跑一次比差異</li></ul></div>' +
  '<div class="obox"><div class="oh">🧩 Orange 路</div><ul>'
  '<li>下載 <b>Orange Data Mining</b>（orangedatamining.com，免費）</li>'
  '<li><b>File</b> 載入 tea CSV → <b>Select Columns</b> 設 target</li>'
  '<li>串 <b>Preprocess→Test &amp; Score</b>，接 RF／Boosting／SVM／LogReg</li>'
  '<li>看 <b>Confusion Matrix</b>：哪些境外茶被誤判成臺灣？</li></ul></div>' +
  '</div>' +
  '<div class="note" style="margin-top:18px">兩條路<strong>跑同一份資料、得同一組結論</strong>：'
  'Python 適合要彈性與自動化，Orange 適合快速探索與課堂示範。建議<strong>都跑一次</strong>，對照著學最快。</div>')

# ---- 19 checklist ----
add(ACT, dc.checklist_inner("今天結束，你應該會…", [
    "說明「監督式分類」：用特徵 X + 標籤 y 學出產地分界",
    "解釋為何要標準化、以及留一法 LOO-CV 在防什麼",
    "用一句話講出 LDA／Ridge／RF／Boosting／SVM 各自的精神",
    "在 Python 用 5 個類別、在 Orange 用對應積木把模型跑起來",
    "說明為何小資料上 Boosting 反而輸給線性模型（過擬合）",
    "知道 Orange 沒有 LDA／Ridge 原生積木，要用 Logistic Regression 代替",
  ], kicker="自我檢核", sub="點一下打勾——兩條路你都能跑了嗎？"))

# ---- 20 closing ----
add(ACT, '<div class="cover2">'
  '<div class="kicker" style="color:#7be39a">重點回顧 · TAKE-HOME</div>'
  '<h1 style="font-size:clamp(1.8rem,4.6vw,3.4rem);font-weight:900;line-height:1.1;color:#fff;letter-spacing:-.01em">'
  '同一份資料，<span style="color:#f0c074">五種看法</span></h1>'
  '<div style="color:rgba(255,255,255,.86);margin-top:16px;font-size:clamp(.95rem,1.6vw,1.2rem);line-height:1.7">'
  '分類器幫 14 元素指紋<strong style="color:#fff">畫出產地分界</strong>；'
  '<strong style="color:#fff">Python</strong> 給你全部彈性、<strong style="color:#fff">Orange</strong> 給你零程式碼。<br>'
  '記得：<strong style="color:#f0c074">資料小的時候，簡單模型常常最聰明。</strong></div>'
  '<div style="margin-top:20px;color:#7be39a;font-size:clamp(.85rem,1.4vw,1.05rem)">'
  '🔎 想一想：換成「微量+肥料」特徵，五個模型的正確率會怎麼變？　🔗 延伸：PCA 降維、交叉驗證調參、特徵重要度</div>'
  '<div style="margin-top:16px;color:rgba(255,255,255,.55);font-size:clamp(.78rem,1.2vw,.96rem)">'
  '搭配 · 茶葉多重元素檢驗 TFDAF0032.00　·　資料：蔡承祥等 2021（教學重建）</div>'
  '</div>', ' data-full="1"')

# ============================================================ CFG (games)
CFG = {
  "bucket": {
    "gmatch": {
      "cats": ["LDA", "Ridge", "隨機森林", "梯度提升", "SVM"],
      "items": [
        {"t": "LinearDiscriminantAnalysis", "c": "LDA"},
        {"t": "RidgeClassifier", "c": "Ridge"},
        {"t": "RandomForestClassifier", "c": "隨機森林"},
        {"t": "GradientBoostingClassifier", "c": "梯度提升"},
        {"t": "SVC", "c": "SVM"},
      ],
      "ok": "🎉 全對！這 5 個 scikit-learn 類別就是五種模型的程式入口。",
      "tip": "提示：Discriminant=判別(LDA)；Ridge=脊；Forest=森林；GradientBoosting=梯度提升；SVC=Support Vector Classifier。"}
  },
  "mcq": {
    "gq": [
      {"q": "同一份 20 筆茶葉資料，下列哪個模型的留一法正確率<strong>反而最低</strong>？",
       "o": ["Ridge", "SVM", "Boosting（梯度提升）", "LDA"], "a": 2,
       "e": "Boosting 只拿 85%。集成樹胃口大，20 筆小資料餵不飽就過擬合；線性模型反而更穩。"},
      {"q": "Ridge 分類器的 <strong>L2 懲罰</strong>主要目的是？",
       "o": ["讓訓練正確率變高", "收縮係數、抑制過擬合", "加快運算速度", "自動選出最佳元素"], "a": 1,
       "e": "L2 懲罰把係數往 0 收縮，不讓少數雜訊元素主導分界，模型對新樣本更穩健。"},
      {"q": "在 <strong>Orange</strong> 裡，下列哪一組<strong>沒有</strong>原生分類積木、要用 Logistic Regression 代替？",
       "o": ["Random Forest 與 SVM", "Gradient Boosting 與 SVM", "LDA 與 Ridge", "SVM 與 Random Forest"], "a": 2,
       "e": "Orange 的 Model 類別有 RF／Gradient Boosting／SVM，但沒有 LDA／Ridge 分類器；用 Logistic Regression（可選 Ridge L2）代表線性分界。"},
      {"q": "為什麼用<strong>留一法 LOO-CV</strong>，而不是直接看訓練資料的正確率？",
       "o": ["訓練正確率會高估、無法反映對新樣本的實力", "LOO 跑比較快", "訓練正確率不能算百分比", "LOO 一定得到 100%"], "a": 0,
       "e": "模型在看過的資料上當然準（甚至死背），那是過擬合假象。LOO 用「沒看過的樣本」考試，才是真實力。"},
      {"q": "為什麼所有模型之前都要先做<strong>標準化</strong>？",
       "o": ["讓圖比較好看", "因為元素單位差很多(% vs mg/kg)，否則大數值元素會霸佔距離與係數", "標準化會提高樣本數", "只有 SVM 需要、其它不用"], "a": 1,
       "e": "P/K/Ca 是百分比、Sr/Pb 是 mg/kg。不標準化，數值大的元素會主導；標準化讓每個元素平均0、標準差1，公平競爭。"},
    ]
  },
  "cmp": {
    "cols": [{"k": "m"}, {"k": "fam"}, {"k": "sk"}, {"k": "og"}, {"k": "acc"}, {"k": "when"}],
    "rows": [
      {"m": "LDA", "fam": "傳統·線性", "sk": "LinearDiscriminantAnalysis", "og": "（用 LogReg）", "acc": 95, "when": "小樣本、要可解釋"},
      {"m": "Ridge", "fam": "傳統·線性", "sk": "RidgeClassifier", "og": "LogReg(L2)", "acc": 100, "when": "特徵多、怕過擬合"},
      {"m": "Random Forest", "fam": "ML·樹集成", "sk": "RandomForestClassifier", "og": "Random Forest ✓", "acc": 95, "when": "非線性、要特徵重要度"},
      {"m": "Boosting", "fam": "ML·樹集成", "sk": "GradientBoostingClassifier", "og": "Gradient Boosting ✓", "acc": 85, "when": "資料夠多、追高準度"},
      {"m": "SVM", "fam": "ML·間隔/核", "sk": "SVC", "og": "SVM ✓", "acc": 100, "when": "小樣本、可線性或非線性"},
    ]
  }
}

dc.build_html(
    {"title": "五種機器學習分類法 · 茶葉產地判別", "brand": "ML 分類 · Python × Orange"},
    S, CFG, OUT)
