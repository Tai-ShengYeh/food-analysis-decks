// 食品科學課程 — 內嵌互動遊戲共用 Firebase 模組
// 統一寫入 student_events collection，支援多課程多班級
//
// 使用方式（每個遊戲頁面）：
//   import { initGameSession, logEvent } from './game_firebase.js';
//   await initGameSession({ course: '4y_food_analysis', chapter: 'ch6', game: 'vocab-match' });
//   logEvent({ event_type: 'answer', question_id: 'Q1', is_correct: true, attempts: 1 });
//
// course_id 白名單（必須與 firestore.rules 一致）：
//   '4y_food_analysis' | '5z_food_analysis' | '4y_food_chem' | 'glp1_chinese' | 'vn_chinese'

import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js';
import {
  getFirestore, addDoc, collection, serverTimestamp,
} from 'https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js';

// ─── Firebase 初始化（從 Hosting 自動載入，不寫死 apiKey）──────────────
let db = null;
try {
  const r = await fetch('/__/firebase/init.json');
  if (!r.ok) throw new Error('not on Firebase Hosting');
  const FB = await r.json();
  db = getFirestore(initializeApp(FB));
} catch (e) {
  console.warn('[Firebase] 不在 Hosting 環境，互動資料不會寫入：', e.message);
}

// ─── Supabase 鏡像（並寫一份到 Supabase，給 SQL 統計分析）─────────────
// anon key 設計上可公開：Supabase RLS 限制此 key 只能 INSERT student_events，
// 不能讀/改/刪，即便被人看到也不會洩漏其他學生資料。
const SUPABASE_URL = 'https://qmldcjkllisvfgegkfsz.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFtbGRjamtsbGlzdmZnZWdrZnN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzExMjM5ODYsImV4cCI6MjA4NjY5OTk4Nn0.Bfj0W7HN_n_vcjGe5502Chamk0YV-de8a0fxF4Nyczk';

function logToSupabase(payload) {
  fetch(`${SUPABASE_URL}/rest/v1/student_events`, {
    method: 'POST',
    headers: {
      apikey: SUPABASE_ANON_KEY,
      Authorization: `Bearer ${SUPABASE_ANON_KEY}`,
      'Content-Type': 'application/json',
      Prefer: 'return=minimal',
    },
    body: JSON.stringify(payload),
    keepalive: true,
  }).catch((e) => console.warn('[Supabase] mirror failed:', e.message));
}

// ─── Session 設定（由 initGameSession 設定）────────────────────────
const SESSION = {
  course_id: null,
  class_id: 'A',
  chapter: null,
  game: null,
  ready: false,
};

// ─── 學號管理（localStorage，跨遊戲共享）───────────────────────────
const SID_KEY = 'food_analysis_student_id';

export function getStudentId() {
  return localStorage.getItem(SID_KEY) || null;
}

export function setStudentId(id) {
  localStorage.setItem(SID_KEY, id);
}

export function clearStudentId() {
  localStorage.removeItem(SID_KEY);
}

// ─── 寫入事件 ────────────────────────────────────────────────────
export async function logEvent(data) {
  if (!db) {
    console.warn('[Firebase] db 未就緒，跳過寫入');
    return;
  }
  if (!SESSION.ready) {
    console.warn('[Firebase] 請先呼叫 initGameSession()');
    return;
  }
  const studentId = getStudentId();
  if (!studentId) {
    console.warn('[Firebase] 無學號，跳過寫入');
    return;
  }
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
  // Supabase 鏡像（fire-and-forget，不阻塞 Firebase 寫入）
  logToSupabase({ ...payload, client_ts: new Date().toISOString() });
  // Firebase 寫入（主要儲存）
  try {
    await addDoc(collection(db, 'student_events'), {
      ...payload,
      timestamp: serverTimestamp(),
    });
  } catch (e) {
    console.error('[Firebase] 寫入失敗：', e);
  }
}

// ─── 學號 modal CSS + HTML（注入式）────────────────────────────────
let modalCssInjected = false;

function injectModalCss() {
  if (modalCssInjected) return;
  modalCssInjected = true;
  const css = `
    .sid-overlay {
      position: fixed; inset: 0;
      background: rgba(13, 27, 42, 0.92);
      display: none; align-items: center; justify-content: center;
      z-index: 9999; padding: 20px;
      font-family: 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
    }
    .sid-overlay.show { display: flex; }
    .sid-card {
      background: #1A3050; border-radius: 14px; max-width: 440px; width: 100%;
      padding: 28px 24px; box-shadow: 0 12px 40px rgba(0,0,0,0.5);
      color: #ECEEF2;
    }
    .sid-card h2 { font-size: 20px; margin-bottom: 8px; color: #00C6FF; }
    .sid-card .sid-hint { font-size: 13px; color: #B8C5E0; margin-bottom: 16px; line-height: 1.5; }
    .sid-card input {
      width: 100%; padding: 12px 14px; border: 2px solid #2A4A6E;
      border-radius: 8px; font-size: 18px; font-family: inherit;
      outline: none; transition: border-color 0.2s;
      background: #0D1B2A; color: #ECEEF2;
    }
    .sid-card input:focus { border-color: #00C6FF; }
    .sid-card .sid-error { color: #E74C3C; font-size: 13px; margin-top: 8px; min-height: 18px; }
    .sid-card .sid-actions { margin-top: 16px; text-align: right; }
    .sid-card button {
      background: #00C6FF; color: #0D1B2A; border: none;
      padding: 10px 22px; border-radius: 8px;
      font-size: 15px; font-weight: bold; cursor: pointer; font-family: inherit;
      min-height: 44px;
    }
    .sid-card button:hover { background: #00A0CC; }
    .sid-pill {
      position: fixed; top: 10px; right: 10px;
      background: #1A3050; color: #ECEEF2;
      padding: 6px 12px; border-radius: 20px;
      font-size: 12px; z-index: 999;
      font-family: 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
      box-shadow: 0 2px 8px rgba(0,0,0,0.3);
      border: 1px solid #2A4A6E;
    }
    .sid-pill .sid-meta { color: #7A91B0; margin-right: 6px; font-size: 11px; }
    .sid-pill .sid-change {
      margin-left: 8px; color: #00C6FF;
      text-decoration: underline; cursor: pointer; font-size: 11px;
    }
  `;
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);
}

function injectModalHtml() {
  const div = document.createElement('div');
  div.className = 'sid-overlay';
  div.id = 'sid-overlay';
  div.innerHTML = `
    <div class="sid-card">
      <h2>📝 請輸入學號</h2>
      <div class="sid-hint">學號用來記錄你的答題狀況。下次玩同一系列遊戲不需重新輸入。<br>例如：B11234567 或 A123456</div>
      <input id="sid-input" type="text" inputmode="text" autocomplete="off" placeholder="例如：B11234567" maxlength="20">
      <div class="sid-error" id="sid-error"></div>
      <div class="sid-actions">
        <button id="sid-confirm">確認</button>
      </div>
    </div>
  `;
  document.body.appendChild(div);
  return div;
}

function injectPill(studentId) {
  let pill = document.getElementById('sid-pill');
  if (!pill) {
    pill = document.createElement('div');
    pill.className = 'sid-pill';
    pill.id = 'sid-pill';
    document.body.appendChild(pill);
  }
  const meta = SESSION.course_id ? `${SESSION.course_id.replace('4y_', '4技').replace('5z_', '5專').replace('_', '')}` : '';
  pill.innerHTML = `<span class="sid-meta">${meta}</span>🎓 ${studentId} <span class="sid-change" id="sid-change">更換</span>`;
  document.getElementById('sid-change').onclick = async () => {
    clearStudentId();
    pill.remove();
    await ensureStudentId();
    location.reload();
  };
}

// ─── 等使用者輸入學號 ────────────────────────────────────────────
function ensureStudentId() {
  injectModalCss();
  return new Promise((resolve) => {
    const existing = getStudentId();
    if (existing) {
      injectPill(existing);
      resolve(existing);
      return;
    }
    const overlay = injectModalHtml();
    overlay.classList.add('show');
    const input = document.getElementById('sid-input');
    const err = document.getElementById('sid-error');
    const btn = document.getElementById('sid-confirm');
    setTimeout(() => input.focus(), 100);

    function submit() {
      const val = input.value.trim();
      if (val.length < 1) { err.textContent = '請輸入學號。'; return; }
      if (val.length > 20) { err.textContent = '學號太長（≤20 字）。'; return; }
      if (!/^[A-Za-z0-9_\-]+$/.test(val)) {
        err.textContent = '學號只能用英文、數字、底線、連字號。';
        return;
      }
      setStudentId(val);
      overlay.classList.remove('show');
      overlay.remove();
      injectPill(val);
      resolve(val);
    }

    btn.onclick = submit;
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') submit();
    });
  });
}

// ─── 主要 API：在遊戲開頭呼叫 ────────────────────────────────────
//   await initGameSession({ course: '4y_food_analysis', chapter: 'ch6', game: 'vocab-match' });
//   或從 URL 讀取：?course=fa&class=A&chapter=ch6
export async function initGameSession(opts = {}) {
  const params = new URLSearchParams(location.search);

  // course alias 簡寫對應
  const COURSE_MAP = {
    'fa': '4y_food_analysis',
    '4y_fa': '4y_food_analysis',
    '5z_fa': '5z_food_analysis',
    'fc': '4y_food_chem',
    'vn': 'vn_chinese',
    'glp1': 'glp1_chinese',
  };

  const classId = opts.class_id || params.get('class') || 'A';

  // course 解析優先序：明確指定 > URL > 從 class 推（食品分析慣例 B=五專/A=四技）> 預設 4y
  let course = opts.course || params.get('course');
  if (!course) {
    course = classId === 'B' ? '5z_food_analysis' : '4y_food_analysis';
  }
  if (COURSE_MAP[course]) course = COURSE_MAP[course];

  SESSION.course_id = course;
  SESSION.class_id = classId;
  SESSION.chapter = opts.chapter || params.get('chapter') || 'ch6';
  SESSION.game = opts.game || 'unknown';
  SESSION.ready = true;

  await ensureStudentId();
  return SESSION;
}

export { SESSION };
