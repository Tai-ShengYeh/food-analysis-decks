// Ch6 SOIL 2026 — 共用 Firebase 紀錄模組
// 寫入 student_events collection，與既有食品分析課程共用 schema
//
// 使用方式：
//   import { initGameSession, logEvent } from './game_firebase.js';
//   await initGameSession({ chapter: 'ch6_soil_2026', game: 'vocab-match' });
//   logEvent({ event_type: 'answer', question_id: 'Q1', is_correct: true, attempts: 1 });

import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js';
import {
  getFirestore, addDoc, collection, serverTimestamp,
} from 'https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js';

// ── Firebase 自動載入（Firebase Hosting 環境）──
let db = null;
let firebaseReady = false;
try {
  const r = await fetch('/__/firebase/init.json');
  if (!r.ok) throw new Error('not on Firebase Hosting');
  const FB = await r.json();
  db = getFirestore(initializeApp(FB));
  firebaseReady = true;
} catch (e) {
  console.warn('[Firebase] 非 Hosting 環境，互動資料只存本機 console：', e.message);
}

// ── Session ──
const SESSION = {
  course_id: null,
  class_id: 'A',
  chapter: null,
  game: null,
  ready: false,
};

// ── 學號 localStorage ──
const SID_KEY = 'food_analysis_student_id';
export const getStudentId = () => localStorage.getItem(SID_KEY) || null;
export const setStudentId = (id) => localStorage.setItem(SID_KEY, id);
export const clearStudentId = () => localStorage.removeItem(SID_KEY);

// ── 主要寫入函式 ──
export async function logEvent(data) {
  const studentId = getStudentId();
  if (!studentId) return;
  if (!SESSION.ready) return;

  const payload = {
    student_id: studentId,
    course_id: SESSION.course_id,
    class_id: SESSION.class_id,
    chapter: SESSION.chapter,
    game: SESSION.game,
    event_type: data.event_type,
    question_id: data.question_id || null,
    is_correct: data.is_correct === undefined ? null : data.is_correct,
    attempts: data.attempts === undefined ? null : data.attempts,
    final_score: data.final_score === undefined ? null : data.final_score,
    user_agent: (navigator.userAgent || '').slice(0, 200),
  };

  if (!firebaseReady || !db) {
    console.log('[Event]', payload);
    return;
  }

  try {
    await addDoc(collection(db, 'student_events'), {
      ...payload,
      timestamp: serverTimestamp(),
    });
  } catch (e) {
    console.error('[Firebase] 寫入失敗：', e);
  }
}

// ── 學號 modal 樣式 ──
let cssInjected = false;
function injectCss() {
  if (cssInjected) return;
  cssInjected = true;
  const css = `
    .sid-overlay{
      position:fixed; inset:0; background:rgba(10,14,39,.95);
      display:none; align-items:center; justify-content:center;
      z-index:9999; padding:20px;
      font-family:'Noto Sans TC','Microsoft JhengHei',sans-serif;
    }
    .sid-overlay.show{display:flex}
    .sid-card{
      background:#11163a; border:1px solid rgba(0,212,255,.25); border-radius:14px;
      max-width:440px; width:100%; padding:28px 24px;
      box-shadow:0 20px 60px rgba(0,0,0,.6);
      color:#eef3ff;
    }
    .sid-card h2{font-size:1.2rem; margin-bottom:8px; color:#00d4ff}
    .sid-card .hint{font-size:.85rem; color:#b8c5e0; margin-bottom:16px; line-height:1.6}
    .sid-card .row{display:flex; gap:8px; margin-bottom:12px}
    .sid-card label{font-size:.75rem; color:#7a8bb8; margin-bottom:4px; display:block; font-family:'JetBrains Mono',monospace}
    .sid-card select, .sid-card input{
      width:100%; padding:10px 12px; border:1px solid #4a5680;
      background:#0a0e27; color:#eef3ff; border-radius:8px;
      font-size:1rem; font-family:inherit; outline:none;
    }
    .sid-card input:focus, .sid-card select:focus{border-color:#00d4ff}
    .sid-card .err{color:#ff006e; font-size:.8rem; min-height:18px; margin-top:6px}
    .sid-card button{
      width:100%; background:linear-gradient(135deg,#00d4ff,#ff006e);
      color:#0a0e27; border:none; padding:12px; border-radius:8px;
      font-weight:700; font-size:1rem; cursor:pointer;
      margin-top:8px; min-height:44px; font-family:inherit;
    }
    .sid-pill{
      position:fixed; top:14px; right:14px;
      background:#11163a; border:1px solid rgba(0,212,255,.2);
      padding:6px 14px; border-radius:18px;
      font-size:.78rem; color:#eef3ff; z-index:200;
      font-family:'Noto Sans TC',sans-serif;
      box-shadow:0 4px 12px rgba(0,0,0,.4);
    }
    .sid-pill .meta{color:#7a8bb8; font-family:'JetBrains Mono',monospace; margin-right:6px; font-size:.7rem}
    .sid-pill .change{
      margin-left:8px; color:#00d4ff;
      text-decoration:underline; cursor:pointer; font-size:.7rem;
    }
  `;
  const s = document.createElement('style');
  s.textContent = css;
  document.head.appendChild(s);
}

function injectPill(studentId) {
  let pill = document.getElementById('sid-pill');
  if (!pill) {
    pill = document.createElement('div');
    pill.className = 'sid-pill';
    pill.id = 'sid-pill';
    document.body.appendChild(pill);
  }
  const cls = SESSION.class_id === 'B' ? '五專' : '四技';
  pill.innerHTML = `<span class="meta">${cls}・${SESSION.chapter || ''}</span>🎓 ${studentId} <span class="change" id="sid-change">更換</span>`;
  document.getElementById('sid-change').onclick = () => {
    clearStudentId();
    pill.remove();
    location.reload();
  };
}

function ensureStudentId() {
  injectCss();
  return new Promise((resolve) => {
    const existing = getStudentId();
    if (existing) {
      injectPill(existing);
      resolve(existing);
      return;
    }
    const div = document.createElement('div');
    div.className = 'sid-overlay show';
    div.innerHTML = `
      <div class="sid-card">
        <h2>📝 開始之前</h2>
        <div class="hint">輸入學號以記錄你的答題狀況。同一系列遊戲只需輸入一次。</div>
        <div>
          <label>班級</label>
          <select id="sid-class">
            <option value="A">四技 A 班</option>
            <option value="B">五專 B 班</option>
          </select>
        </div>
        <div style="margin-top:10px">
          <label>學號</label>
          <input id="sid-input" type="text" inputmode="text" autocomplete="off" placeholder="例如：B11234567" maxlength="20">
        </div>
        <div class="err" id="sid-err"></div>
        <button id="sid-confirm">確認進入</button>
      </div>
    `;
    document.body.appendChild(div);

    const input = div.querySelector('#sid-input');
    const sel = div.querySelector('#sid-class');
    const err = div.querySelector('#sid-err');
    const btn = div.querySelector('#sid-confirm');

    // 預設班級對應課程
    sel.value = SESSION.class_id || 'A';
    setTimeout(() => input.focus(), 100);

    const submit = () => {
      const val = input.value.trim();
      if (val.length < 1) { err.textContent = '請輸入學號。'; return; }
      if (val.length > 20) { err.textContent = '學號太長（≤20 字）。'; return; }
      if (!/^[A-Za-z0-9_\-]+$/.test(val)) {
        err.textContent = '學號只能用英文、數字、底線、連字號。';
        return;
      }
      setStudentId(val);
      SESSION.class_id = sel.value;
      SESSION.course_id = sel.value === 'B' ? '5z_food_analysis' : '4y_food_analysis';
      div.remove();
      injectPill(val);
      resolve(val);
    };
    btn.onclick = submit;
    input.addEventListener('keydown', (e) => { if (e.key === 'Enter') submit(); });
  });
}

// ── 主要 API ──
export async function initGameSession(opts = {}) {
  const params = new URLSearchParams(location.search);

  const COURSE_MAP = {
    'fa': '4y_food_analysis',
    '4y_fa': '4y_food_analysis',
    '5z_fa': '5z_food_analysis',
  };

  const classId = opts.class_id || params.get('class') || 'A';
  let course = opts.course || params.get('course');
  if (!course) course = classId === 'B' ? '5z_food_analysis' : '4y_food_analysis';
  if (COURSE_MAP[course]) course = COURSE_MAP[course];

  SESSION.course_id = course;
  SESSION.class_id = classId;
  SESSION.chapter = opts.chapter || params.get('chapter') || 'ch6_soil_2026';
  SESSION.game = opts.game || 'unknown';
  SESSION.ready = true;

  await ensureStudentId();
  return SESSION;
}

export { SESSION };
