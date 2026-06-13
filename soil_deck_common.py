# -*- coding: utf-8 -*-
"""
Shared engine for the Nielsen SOIL HTML teaching decks (light academic style).
Data-driven: each chapter defines slides + a CFG dict; this module supplies the
verified CSS and JS engine (navigation / MCQ / bucket-match / sort / calc /
sortable comparison table / Chart.js) and assembles a single self-contained HTML.

Used by:  ch18_protein_soil/build_ch18.py, ch19_carb_soil/build_ch19.py, ...
This file is the SINGLE SOURCE OF TRUTH for the engine. Edit here, rebuild each ch.
"""
import json, os

# ============================================================ CSS (light academic)
CSS = r"""
*{margin:0;padding:0;box-sizing:border-box}
html,body{font-size:18px}
body{font-family:"Noto Sans TC","Microsoft JhengHei",sans-serif;background:var(--bg);
  color:var(--ink);overflow:hidden;height:100vh;width:100vw}
:root{
  --bg:#eef2f8;--surface:#ffffff;--surface-2:#f6f9fd;
  --ink:#15233f;--ink-2:#48597a;--ink-3:#8493ad;--line:#dde5f0;
  --accent:#1f6feb;--accent-soft:#e7f0fe;
  --accent-2:#d9822b;--accent-2-soft:#fbeede;
  --ok:#1f9d6b;--ok-soft:#e3f6ee;--bad:#d94f4f;--bad-soft:#fbe7e7;--warn:#d9a32b;
  --t2:clamp(1.4rem,3vw,2.3rem);
  --shadow:0 10px 30px rgba(20,40,80,.10);--shadow-sm:0 3px 12px rgba(20,40,80,.08)}
#progress{position:fixed;top:0;left:0;height:4px;width:0;z-index:50;
  background:linear-gradient(90deg,var(--accent),var(--accent-2));transition:width .5s ease}
#section-tag{position:fixed;top:16px;left:24px;z-index:40;font-size:.78rem;letter-spacing:.18em;
  color:var(--accent);font-weight:700;font-family:"JetBrains Mono",monospace}
#pageInfo{position:fixed;right:22px;bottom:16px;z-index:40;font-size:.82rem;color:var(--ink-3);
  font-family:"JetBrains Mono",monospace}
#hint{position:fixed;left:24px;bottom:16px;z-index:40;font-size:.72rem;color:var(--ink-3)}
#brand{position:fixed;right:22px;top:14px;z-index:40;font-size:.72rem;color:var(--ink-3);
  font-family:"JetBrains Mono",monospace}
.slide{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  padding:64px 84px;opacity:0;pointer-events:none;
  transition:opacity .55s ease,transform .55s ease;transform:translateY(14px)}
.slide.active{opacity:1;pointer-events:auto;transform:translateY(0)}
.slide-inner{width:100%;max-width:1280px}
.kicker{font-family:"JetBrains Mono",monospace;font-size:.8rem;letter-spacing:.16em;color:var(--accent);
  font-weight:700;text-transform:uppercase;margin-bottom:10px}
.slide-title{font-size:var(--t2);font-weight:900;line-height:1.18;color:var(--ink);letter-spacing:-.01em}
.slide-title .hi{color:var(--accent-2)}
.subtitle{font-size:clamp(.95rem,1.5vw,1.2rem);color:var(--ink-2);margin-top:12px;line-height:1.6}
p,li{font-size:clamp(.92rem,1.4vw,1.12rem);line-height:1.68;color:var(--ink-2)}
.lead{font-size:clamp(1.05rem,1.8vw,1.35rem);color:var(--ink);line-height:1.6}
strong,b{color:var(--ink);font-weight:800}.em{color:var(--accent-2);font-weight:800}
.divider{height:3px;width:64px;background:var(--accent-2);border-radius:2px;margin:18px 0}
ul.clean{list-style:none}ul.clean li{position:relative;padding-left:26px;margin:10px 0}
ul.clean li:before{content:"";position:absolute;left:4px;top:.62em;width:8px;height:8px;border-radius:2px;
  background:var(--accent);transform:rotate(45deg)}
.mono{font-family:"JetBrains Mono",monospace}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:center}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.grid2-1{display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:center}
.flow6{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:22px;box-shadow:var(--shadow-sm)}
.card .ic{font-size:1.6rem;margin-bottom:8px}
.card .ct{font-weight:800;color:var(--ink);font-size:clamp(1rem,1.5vw,1.2rem);margin-bottom:6px}
.card .cb{font-size:clamp(.85rem,1.25vw,1rem);color:var(--ink-2);line-height:1.55}
.card.b{border-top:4px solid var(--accent)}.card.a{border-top:4px solid var(--accent-2)}
.card.g{border-top:4px solid var(--ok)}
.tag{display:inline-block;font-family:"JetBrains Mono",monospace;font-size:.7rem;padding:3px 9px;border-radius:999px;
  background:var(--accent-soft);color:var(--accent);font-weight:700}
.tag.a{background:var(--accent-2-soft);color:var(--accent-2)}
.pill{display:inline-block;padding:5px 12px;border-radius:999px;background:var(--surface);border:1px solid var(--line);
  font-size:.82rem;color:var(--ink-2);margin:3px 4px}
.note{background:var(--accent-2-soft);border-left:4px solid var(--accent-2);border-radius:8px;padding:14px 18px;
  color:var(--ink);font-size:clamp(.9rem,1.3vw,1.05rem);line-height:1.6}
.eq{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px 22px;
  font-family:"JetBrains Mono",monospace;font-size:clamp(1rem,1.7vw,1.4rem);color:var(--ink);text-align:center;box-shadow:var(--shadow-sm)}
.eq .frac{display:inline-flex;flex-direction:column;text-align:center;vertical-align:middle;margin:0 6px}
.eq .frac b{border-bottom:2px solid var(--ink);padding-bottom:3px}
table.cmp{width:100%;border-collapse:collapse;font-size:clamp(.82rem,1.2vw,1.02rem)}
table.cmp th,table.cmp td{text-align:left;padding:11px 14px;border-bottom:1px solid var(--line)}
table.cmp thead th{color:var(--accent);font-weight:800;border-bottom:2px solid var(--accent);cursor:pointer;
  user-select:none;white-space:nowrap}
table.cmp thead th .ar{opacity:.4;font-size:.8em}
table.cmp tbody tr:hover{background:var(--surface-2)}table.cmp td.c{color:var(--ink);font-weight:700}
.cover{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 100px;
  background:radial-gradient(1200px 600px at 80% 20%,var(--accent-2-soft),transparent 60%),
  radial-gradient(900px 500px at 10% 90%,var(--accent-soft),transparent 55%),linear-gradient(135deg,#ffffff,#eef2f8)}
.cover h1{font-size:clamp(2.4rem,6vw,4.6rem);font-weight:900;line-height:1.05;letter-spacing:-.02em;color:var(--ink)}
.cover .en{font-family:"JetBrains Mono",monospace;font-size:clamp(1rem,2vw,1.5rem);color:var(--accent);letter-spacing:.1em;margin-top:6px}
.cover .meta{margin-top:26px;color:var(--ink-2);font-size:clamp(.9rem,1.4vw,1.1rem)}
.hook{font-size:clamp(2rem,5vw,3.6rem);font-weight:900;color:var(--ink);line-height:1.2;letter-spacing:-.01em}
.hook .hi{color:var(--accent)}
.svgwrap{display:flex;align-items:center;justify-content:center}
.svgwrap svg{max-width:100%;max-height:62vh;height:auto}
.lbl{font-family:"Noto Sans TC",sans-serif;font-size:13px;fill:var(--ink-2)}
.lblb{font-family:"Noto Sans TC",sans-serif;font-size:13px;fill:var(--ink);font-weight:700}
.game{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:20px 24px;box-shadow:var(--shadow)}
.game-head{display:flex;align-items:center;gap:12px;margin-bottom:6px}
.game-head .gt{font-weight:900;font-size:clamp(1.05rem,1.7vw,1.35rem);color:var(--ink)}
.game-head .score{margin-left:auto;font-family:"JetBrains Mono",monospace;font-weight:700;color:var(--accent);
  background:var(--accent-soft);padding:5px 13px;border-radius:999px;font-size:.9rem}
.game-q{font-size:clamp(.95rem,1.5vw,1.18rem);color:var(--ink);font-weight:700;margin:6px 0 14px;line-height:1.5}
.buckets{display:grid;gap:16px;margin-top:14px}
.bucket{min-height:120px;border:2px dashed var(--line);border-radius:14px;padding:12px;background:var(--surface-2);transition:.2s}
.bucket .bh{font-weight:800;color:var(--ink);text-align:center;margin-bottom:8px;font-size:.95rem}
.pool{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;min-height:54px}
.chip{padding:9px 15px;border-radius:10px;background:var(--surface);border:1px solid var(--line);font-weight:700;
  color:var(--ink);cursor:pointer;box-shadow:var(--shadow-sm);font-size:.92rem;transition:.15s}
.chip:hover{border-color:var(--accent);transform:translateY(-1px)}
.chip.sel{background:var(--accent);color:#fff;border-color:var(--accent)}
.chip.ok{background:var(--ok-soft);border-color:var(--ok);color:var(--ok)}
.chip.no{background:var(--bad-soft);border-color:var(--bad);color:var(--bad)}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:6px}
.opt{padding:14px 18px;border-radius:12px;border:1.5px solid var(--line);background:var(--surface);cursor:pointer;
  font-weight:700;color:var(--ink);font-size:clamp(.88rem,1.3vw,1.05rem);transition:.15s}
.opt:hover{border-color:var(--accent);background:var(--accent-soft)}
.opt.ok{border-color:var(--ok);background:var(--ok-soft);color:var(--ok)}
.opt.no{border-color:var(--bad);background:var(--bad-soft);color:var(--bad)}.opt.dim{opacity:.5}
.fb{margin-top:14px;padding:12px 16px;border-radius:10px;font-weight:700;display:none;
  font-size:clamp(.85rem,1.3vw,1.02rem);line-height:1.5}
.fb.show{display:block}.fb.good{background:var(--ok-soft);color:var(--ok)}
.fb.bad{background:var(--bad-soft);color:var(--bad)}.fb.info{background:var(--accent-soft);color:var(--accent)}
.btn{padding:10px 20px;border-radius:10px;border:none;background:var(--accent);color:#fff;font-weight:800;cursor:pointer;
  font-size:.92rem;font-family:inherit;box-shadow:var(--shadow-sm)}
.btn:hover{filter:brightness(1.06)}.btn.ghost{background:var(--surface);color:var(--accent);border:1.5px solid var(--accent)}
.btnrow{display:flex;gap:12px;margin-top:16px;align-items:center}
.sortlist{display:flex;flex-direction:column;gap:6px;margin-top:6px;max-height:44vh;overflow-y:auto;padding-right:4px}
.sortrow{display:flex;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--line);border-radius:10px;
  padding:7px 14px;box-shadow:var(--shadow-sm)}
.sortrow .idx{font-family:"JetBrains Mono",monospace;font-weight:800;color:var(--accent);width:24px}
.sortrow .txt{flex:1;font-weight:700;color:var(--ink);font-size:clamp(.85rem,1.25vw,1.02rem)}
.sortrow .ud{display:flex;flex-direction:column;gap:3px}
.sortrow .ud button{border:none;background:var(--accent-soft);color:var(--accent);border-radius:6px;width:30px;height:20px;
  cursor:pointer;font-weight:900;line-height:1}
.sortrow.ok{border-color:var(--ok);background:var(--ok-soft)}.sortrow.no{border-color:var(--bad)}
.numin{font-family:"JetBrains Mono",monospace;font-size:1.2rem;font-weight:800;padding:10px 14px;border:1.5px solid var(--line);
  border-radius:10px;width:140px;color:var(--ink);text-align:center}
.numin:focus{outline:none;border-color:var(--accent)}
.checklist{list-style:none}
.checklist li{display:flex;align-items:center;gap:12px;padding:11px 14px;border:1px solid var(--line);border-radius:10px;
  margin:8px 0;background:var(--surface);cursor:pointer;font-weight:700;color:var(--ink-2);font-size:clamp(.9rem,1.35vw,1.08rem);transition:.15s}
.checklist li .bx{width:24px;height:24px;border-radius:6px;border:2px solid var(--accent);display:flex;align-items:center;
  justify-content:center;color:#fff;font-weight:900;flex:0 0 auto}
.checklist li.done{background:var(--ok-soft);border-color:var(--ok);color:var(--ink)}
.checklist li.done .bx{background:var(--ok);border-color:var(--ok)}
.chartbox{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:var(--shadow-sm);
  height:60vh;max-height:520px;position:relative}
.cap{font-size:.82rem;color:var(--ink-3);text-align:center;margin-top:8px}
/* ===== MOBILE (phones / narrow screens) — added 2026-06-13 ===== */
@media (max-width:640px){
  html,body{font-size:16px}
  .slide{padding:46px 14px 30px;align-items:flex-start;overflow-y:auto;-webkit-overflow-scrolling:touch}
  .slide-inner{max-width:100%;min-width:0}
  .grid2,.grid2-1,.grid3,.flow6{grid-template-columns:minmax(0,1fr)!important;gap:14px!important}
  .grid2>*,.grid2-1>*,.grid3>*,.flow6>*{min-width:0}
  .opts{grid-template-columns:1fr!important}
  .buckets{grid-template-columns:1fr!important}
  table.cmp{display:block;overflow-x:auto;white-space:nowrap}
  .eq{overflow-x:auto}
  .svgwrap{overflow-x:auto}
  .svgwrap svg{max-height:none}
  .chartbox{height:48vh!important;max-height:none}
  .cover{padding:0 22px!important}
  #hint,#brand{display:none}
  #section-tag{font-size:.62rem;left:12px;top:8px;letter-spacing:.08em}
  #pageInfo{right:10px;bottom:8px;font-size:.7rem}
}
"""

# ============================================================ JS engine (reads window.CFG)
JS = r"""
var CFG=window.CFG||{};
var slides=[].slice.call(document.querySelectorAll('.slide'));
var total=slides.length,cur=0;
var prog=document.getElementById('progress'),pageInfo=document.getElementById('pageInfo'),secTag=document.getElementById('section-tag');
function show(i){
  cur=Math.max(0,Math.min(total-1,i));
  slides.forEach(function(s,k){s.classList.toggle('active',k===cur)});
  prog.style.width=((cur+1)/total*100)+'%';
  pageInfo.textContent=(cur+1)+' / '+total;
  secTag.textContent='— '+(slides[cur].dataset.section||'')+' —';
  var ch=slides[cur].dataset.chart; if(ch) initChart(ch);
  var g=slides[cur].dataset.game; if(g) initGame(g);
}
function next(){show(cur+1)} function prev(){show(cur-1)}
function toggleFs(){if(!document.fullscreenElement){document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen()}else{document.exitFullscreen&&document.exitFullscreen()}}
document.addEventListener('keydown',function(e){
  if(e.key==='ArrowRight'||e.key===' '){e.preventDefault();next()}
  else if(e.key==='ArrowLeft'){prev()}
  else if(e.key==='f'||e.key==='F'){toggleFs()}
});
document.addEventListener('click',function(e){
  if(e.target.closest('.no-nav')) return;
  if(e.target.closest('button,input,select,textarea,a,.chip,.opt,.bucket')) return;
  var x=e.clientX/window.innerWidth;
  if(x>0.72) next(); else if(x<0.28) prev();
});

/* ---------- charts ---------- */
var chartDone={};
function initChart(id){
  if(chartDone[id]||typeof Chart==='undefined'||!CFG.charts||!CFG.charts[id]) return; chartDone[id]=1;
  Chart.defaults.font.family="'Noto Sans TC',sans-serif"; Chart.defaults.color='#48597a';
  var c=CFG.charts[id];
  var el=document.getElementById('chart_'+id); if(!el) return;
  var ds=c.datasets.map(function(d){return {label:d.label,data:d.data,
    backgroundColor:d.color||'#1f6feb',borderColor:d.color||'#1f6feb',borderRadius:5,
    fill:(c.type==='line'?false:true),tension:.3}});
  new Chart(el,{type:c.type||'bar',data:{labels:c.labels,datasets:ds},
    options:{responsive:true,maintainAspectRatio:false,
      plugins:{legend:{display:(c.datasets.length>1),position:'top'}},
      scales:{y:{beginAtZero:(c.zero!==false),title:{display:!!c.yTitle,text:c.yTitle||''}}}}});
}

/* ---------- games ---------- */
var gameDone={};
function setScore(el,v){var e=document.getElementById(el);if(e)e.textContent=v}
function fb(el,msg,type){var f=document.getElementById(el);if(!f)return;f.className='fb show '+type;f.innerHTML=msg}
function initGame(g){
  if(gameDone[g])return; gameDone[g]=1;
  if(CFG.bucket&&CFG.bucket[g]) return initBucket(g);
  if(CFG.mcq&&CFG.mcq[g]) return initMCQ(g);
  if(CFG.sort&&CFG.sort[g]) return initSort(g);
  if(CFG.calc&&CFG.calc[g]) return initCalc(g);
  if(g==='cmp') return initCmp();
}

function initBucket(g){
  var cfg=CFG.bucket[g];
  var data=cfg.items.map(function(x){return {t:x.t,c:x.c,at:null}});
  var cats=cfg.cats, N=data.length;
  var pool=document.getElementById(g+'pool'), bk=document.getElementById(g+'buckets');
  var sel=null;
  bk.style.gridTemplateColumns='repeat('+cats.length+',1fr)';
  function paint(){[].slice.call(pool.children).forEach(function(c){c.classList.toggle('sel',+c.dataset.i===sel)})}
  function render(){
    pool.innerHTML=''; bk.innerHTML='';
    var placed={}; cats.forEach(function(c){placed[c]=[]});
    data.forEach(function(d,i){if(d.at)placed[d.at].push(i)});
    data.forEach(function(d,i){ if(d.at) return;
      var c=document.createElement('div');c.className='chip';c.textContent=d.t;c.dataset.i=i;
      c.onclick=function(){sel=(sel===i?null:i);paint()}; pool.appendChild(c);
    });
    cats.forEach(function(cat){
      var b=document.createElement('div');b.className='bucket';b.innerHTML='<div class="bh">'+cat+'</div>';
      placed[cat].forEach(function(i){
        var c=document.createElement('div');c.className='chip';c.textContent=data[i].t;
        c.onclick=function(){data[i].at=null;sel=null;render()}; b.appendChild(c);
      });
      b.onclick=function(e){ if(e.target!==b&&!e.target.classList.contains('bh'))return;
        if(sel!=null){data[sel].at=cat;sel=null;render()} };
      bk.appendChild(b);
    });
    paint();
  }
  render();
  document.getElementById(g+'check').onclick=function(){
    var ok=0; data.forEach(function(d){if(d.at===d.c)ok++});
    setScore(g+'score',ok+' / '+N);
    if(ok===N) fb(g+'fb',cfg.ok||'🎉 全對！','good');
    else fb(g+'fb','答對 '+ok+'/'+N+'。'+(cfg.tip||'再調整看看。'),'bad');
  };
  document.getElementById(g+'reset').onclick=function(){
    data.forEach(function(d){d.at=null}); sel=null; render(); setScore(g+'score','0 / '+N);
    var f=document.getElementById(g+'fb'); if(f) f.className='fb';
  };
}

function initMCQ(g){
  var DATA=CFG.mcq[g], nq=DATA.length, idx=0, score=0, locked=false;
  var qEl=document.getElementById(g+'q'), opEl=document.getElementById(g+'opts'), nextBtn=document.getElementById(g+'next');
  function render(){
    locked=false; var d=DATA[idx];
    qEl.innerHTML='<span style="color:var(--accent)">Q'+(idx+1)+'.</span> '+d.q;
    opEl.innerHTML=''; var f=document.getElementById(g+'fb'); if(f)f.className='fb'; if(nextBtn)nextBtn.style.display='none';
    d.o.forEach(function(t,i){
      var o=document.createElement('div');o.className='opt';o.textContent=t;
      o.onclick=function(){
        if(locked)return; locked=true; var ok=(i===d.a);
        if(ok){o.classList.add('ok');score++}else{o.classList.add('no');opEl.children[d.a].classList.add('ok')}
        [].slice.call(opEl.children).forEach(function(c,k){if(k!==i&&k!==d.a)c.classList.add('dim')});
        setScore(g+'score',score+' / '+nq);
        var done=(idx>=DATA.length-1);
        var msg=(ok?'✅ 答對！':'❌ 正解：'+d.o[d.a]+'。')+'<br>'+d.e+(done?'<br><b>完成！總分 '+score+'/'+nq+'</b>':'');
        fb(g+'fb',msg,ok?'good':'bad');
        if(nextBtn) nextBtn.style.display=done?'none':'inline-block';
      };
      opEl.appendChild(o);
    });
  }
  if(nextBtn) nextBtn.onclick=function(){if(idx<DATA.length-1){idx++;render()}};
  render();
}

function initSort(g){
  var cfg=CFG.sort[g], steps=cfg.steps, N=steps.length;
  var order=(cfg.shuffle||steps.map(function(_,i){return i})).slice();
  var list=document.getElementById(g+'list');
  function render(){
    list.innerHTML='';
    order.forEach(function(stepIdx,pos){
      var row=document.createElement('div');row.className='sortrow';
      row.innerHTML='<div class="idx">'+(pos+1)+'</div><div class="txt">'+steps[stepIdx]+'</div>';
      var ud=document.createElement('div');ud.className='ud';
      var up=document.createElement('button');up.textContent='▲';
      up.onclick=function(){if(pos>0){var t=order[pos-1];order[pos-1]=order[pos];order[pos]=t;render()}};
      var dn=document.createElement('button');dn.textContent='▼';
      dn.onclick=function(){if(pos<order.length-1){var t=order[pos+1];order[pos+1]=order[pos];order[pos]=t;render()}};
      ud.appendChild(up);ud.appendChild(dn);row.appendChild(ud);list.appendChild(row);
    });
  }
  render();
  document.getElementById(g+'check').onclick=function(){
    var ok=0; order.forEach(function(v,i){if(v===i)ok++});
    [].slice.call(list.children).forEach(function(r,i){r.classList.toggle('ok',order[i]===i);r.classList.toggle('no',order[i]!==i)});
    setScore(g+'score',ok+' / '+N);
    if(ok===N) fb(g+'fb',cfg.ok||'🎉 順序完全正確！','good');
    else fb(g+'fb','對了 '+ok+'/'+N+' 個位置。'+(cfg.tip||''),'bad');
  };
  document.getElementById(g+'reset').onclick=function(){
    order=(cfg.shuffle||steps.map(function(_,i){return i})).slice().reverse(); render();
    var f=document.getElementById(g+'fb'); if(f)f.className='fb'; setScore(g+'score','— / '+N);
  };
}

function initCalc(g){
  var cfg=CFG.calc[g];
  document.getElementById(g+'check').onclick=function(){
    var v=parseFloat(document.getElementById(g+'in').value);
    if(isNaN(v)){fb(g+'fb','請先輸入一個數字。','info');return}
    if(Math.abs(v-cfg.answer)<=(cfg.tol||0.05)){
      setScore(g+'score','✓ 答對'); fb(g+'fb',cfg.ok||('🎉 正確！答案是 '+cfg.answer),'good');
    } else { setScore(g+'score','再試一次'); fb(g+'fb',cfg.bad||'再算算看。','bad'); }
  };
  var hb=document.getElementById(g+'hint');
  if(hb) hb.onclick=function(){fb(g+'fb',cfg.hint||'提示：對照公式逐步代入。','info')};
}

function stars(n){return '★★★★★'.slice(0,n)+'☆☆☆☆☆'.slice(0,5-n)}
function initCmp(){
  if(!CFG.cmp) return;
  var cols=CFG.cmp.cols, rows=CFG.cmp.rows.slice(), dir={};
  var tb=document.querySelector('#cmpTable tbody');
  function draw(){ tb.innerHTML=''; rows.forEach(function(r){
    var tr=document.createElement('tr');
    tr.innerHTML=cols.map(function(c,ci){
      var v=r[c.k];
      if(c.star) return '<td style="color:var(--accent-2)">'+stars(v)+'</td>';
      return '<td'+(ci===0?' class="c"':'')+'>'+v+'</td>';
    }).join(''); tb.appendChild(tr); }); }
  draw();
  document.querySelectorAll('#cmpTable thead th').forEach(function(th){
    th.onclick=function(){var k=th.dataset.k,t=th.dataset.t;dir[k]=!dir[k];
      rows.sort(function(a,b){var x=a[k],y=b[k];
        if(t==='n')return dir[k]?x-y:y-x;
        return dir[k]?String(x).localeCompare(String(y),'zh-Hant'):String(y).localeCompare(String(x),'zh-Hant')});
      draw();};
  });
}
show(0);
/* ---- touch-swipe navigation (phones); next()/prev() are defined above ---- */
(function(){
  var x0=0,y0=0,t0=0,trk=false;
  document.addEventListener('touchstart',function(e){
    if(e.touches.length>1){trk=false;return;}
    var t=e.changedTouches[0]; x0=t.clientX; y0=t.clientY; t0=Date.now(); trk=true;
  },{passive:true});
  document.addEventListener('touchend',function(e){
    if(!trk) return; trk=false;
    if(e.target.closest('.no-nav,button,input,select,textarea,a,.chip,.opt,.bucket,table,.svgwrap,.checklist,.eq,.sortlist')) return;
    var t=e.changedTouches[0], dx=t.clientX-x0, dy=t.clientY-y0, dt=Date.now()-t0;
    if(dt<700 && Math.abs(dx)>48 && Math.abs(dx)>Math.abs(dy)*1.5){ if(dx<0) next(); else prev(); }
  },{passive:true});
})();
"""

# ============================================================ slide builders
def kt(kicker, title, sub=""):
    h = '<div class="kicker">%s</div><h2 class="slide-title">%s</h2>' % (kicker, title)
    if sub:
        h += '<p class="subtitle">%s</p>' % sub
    return h

def card(ic, ct, cb, tone="b"):
    return '<div class="card %s"><div class="ic">%s</div><div class="ct">%s</div><div class="cb">%s</div></div>' % (tone, ic, ct, cb)

def cover(kicker, title_html, en, meta_html, pills=None):
    p = ''
    if pills:
        p = '<div style="margin-top:24px">' + ''.join('<span class="pill">%s</span>' % x for x in pills) + '</div>'
    return ('<div class="cover"><div class="kicker">%s</div><h1>%s</h1>'
            '<div class="en">%s</div><div class="meta">%s</div>%s</div>') % (kicker, title_html, en, meta_html, p)

def chart_inner(cid, title_html, cap, kicker="數據", height=None):
    h = ' style="height:%s"' % height if height else ''
    return (kt(kicker, title_html) +
            '<div class="chartbox"%s><canvas id="chart_%s"></canvas></div><div class="cap">%s</div>' % (h, cid, cap))

def game_bucket_inner(gid, badge, title, n, question):
    return ('<div class="game no-nav" data-game="%s"><div class="game-head"><span class="tag a">%s</span>'
            '<span class="gt">%s</span><span class="score" id="%sscore">0 / %d</span></div>'
            '<div class="game-q">%s</div><div class="pool" id="%spool"></div>'
            '<div class="buckets" id="%sbuckets"></div><div class="fb" id="%sfb"></div>'
            '<div class="btnrow"><button class="btn" id="%scheck">檢查答案</button>'
            '<button class="btn ghost" id="%sreset">重來</button></div></div>') % (
            gid, badge, title, gid, n, question, gid, gid, gid, gid, gid)

def game_mcq_inner(gid, badge, title, n):
    return ('<div class="game no-nav" data-game="%s"><div class="game-head"><span class="tag a">%s</span>'
            '<span class="gt">%s</span><span class="score" id="%sscore">0 / %d</span></div>'
            '<div class="game-q" id="%sq"></div><div class="opts" id="%sopts"></div>'
            '<div class="fb" id="%sfb"></div><div class="btnrow">'
            '<button class="btn ghost" id="%snext" style="display:none">下一題 →</button></div></div>') % (
            gid, badge, title, gid, n, gid, gid, gid, gid)

def game_sort_inner(gid, badge, title, n, question):
    return ('<div class="game no-nav" data-game="%s"><div class="game-head"><span class="tag a">%s</span>'
            '<span class="gt">%s</span><span class="score" id="%sscore">— / %d</span></div>'
            '<div class="game-q">%s</div><div class="sortlist" id="%slist"></div>'
            '<div class="fb" id="%sfb"></div><div class="btnrow">'
            '<button class="btn" id="%scheck">檢查順序</button>'
            '<button class="btn ghost" id="%sreset">打亂重排</button></div></div>') % (
            gid, badge, title, gid, n, question, gid, gid, gid, gid)

def game_calc_inner(gid, badge, title, question, unit="%"):
    return ('<div class="game no-nav" data-game="%s"><div class="game-head"><span class="tag a">%s</span>'
            '<span class="gt">%s</span><span class="score" id="%sscore">未作答</span></div>'
            '<div class="game-q">%s</div><div class="btnrow">'
            '<input class="numin" id="%sin" type="number" step="any" placeholder="?"> '
            '<span style="font-weight:800;color:var(--ink)">%s</span>'
            '<button class="btn" id="%scheck">對答案</button>'
            '<button class="btn ghost" id="%shint">提示</button></div>'
            '<div class="fb" id="%sfb"></div></div>') % (
            gid, badge, title, gid, question, gid, unit, gid, gid, gid)

def cmp_inner(title_html, cols, cap, kicker="方法比較"):
    th = ''.join('<th data-k="%s" data-t="%s">%s <span class="ar">⇅</span></th>' % (c['k'], c.get('t', 's'), c['label']) for c in cols)
    return (kt(kicker, title_html) +
            '<table class="cmp" id="cmpTable" style="margin-top:14px"><thead><tr>%s</tr></thead><tbody></tbody></table>'
            '<div class="cap">%s</div>' % (th, cap))

def checklist_inner(title_html, items, kicker="自我檢核", sub="點一下打勾——確認自己真的會了。"):
    lis = ''.join('<li data-k><span class="bx">✓</span>%s</li>' % x for x in items)
    return (kt(kicker, title_html) +
            '<ul class="checklist no-nav" id="selfcheck" style="margin-top:18px;max-width:980px">%s</ul>'
            '<p class="subtitle" style="margin-top:12px">%s</p>' % (lis, sub))

CHECKLIST_JS = """
<script>document.addEventListener('click',function(e){var li=e.target.closest('#selfcheck li');if(li)li.classList.toggle('done')});</script>
"""

# ============================================================ assemble
def build_html(meta, slides, cfg, out_path):
    """meta: {title, brand, course}; slides: list of (section, attr, inner); cfg: dict for window.CFG"""
    cfg_json = json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")
    p = []
    p.append('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">')
    p.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    p.append('<title>%s</title>' % meta["title"])
    p.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
    p.append('<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">')
    p.append('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>')
    p.append('<style>' + CSS + '</style></head><body>')
    p.append('<div id="progress"></div><div id="section-tag"></div>')
    p.append('<div id="brand">%s</div>' % meta.get("brand", ""))
    p.append('<div id="pageInfo"></div><div id="hint">← → / 空白鍵切頁　·　F 全螢幕　·　點兩側翻頁</div>')
    for i, (sec, attr, inner) in enumerate(slides, start=1):
        p.append('<section class="slide" data-slide="%d" data-section="%s"%s><div class="slide-inner">%s</div></section>' % (i, sec, attr, inner))
    p.append('<script>window.CFG=' + cfg_json + ';</script>')
    p.append('<script>' + JS + '</script>')
    p.append(CHECKLIST_JS)
    p.append('</body></html>')
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(p))
    print("OK ->", out_path, "| slides:", len(slides))
