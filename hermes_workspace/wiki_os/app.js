// ============================================================
// WikiOS — Live App (reads from etisiobi repo via serve.py)
// ============================================================

const API = 'http://localhost:7891/api';

// ── Tag colour palette ────────────────────────────────────────
const TAG_PALETTE = [
  { accent: '#85b9c9', soft: 'rgba(133,185,201,0.12)', text: '#3a7a8f' },
  { accent: '#c4a7e7', soft: 'rgba(196,167,231,0.12)', text: '#7a52a0' },
  { accent: '#85c9a7', soft: 'rgba(133,201,167,0.12)', text: '#3a8f6a' },
  { accent: '#f4b183', soft: 'rgba(244,177,131,0.12)', text: '#b06030' },
  { accent: '#c9a785', soft: 'rgba(201,167,133,0.12)', text: '#8f6a3a' },
  { accent: '#e7a7c4', soft: 'rgba(231,167,196,0.12)', text: '#a0527a' },
  { accent: '#a7c4e7', soft: 'rgba(167,196,231,0.12)', text: '#3a5a9f' },
];
const tagColorMap = {};
function tagStyle(tag) {
  if (!tagColorMap[tag]) {
    const idx = Object.keys(tagColorMap).length % TAG_PALETTE.length;
    tagColorMap[tag] = TAG_PALETTE[idx];
  }
  return tagColorMap[tag];
}

// ── State ─────────────────────────────────────────────────────
let allNotes = [];
let allStats = {};
let activeTag = null;
let currentNote = null;

// ── Fetch helpers ─────────────────────────────────────────────
async function fetchNotes(query = '', tag = '') {
  const params = new URLSearchParams();
  if (query) params.set('q', query);
  if (tag)   params.set('tag', tag);
  const res = await fetch(`${API}/notes?${params}`);
  const data = await res.json();
  return data.notes || [];
}

async function fetchStats() {
  const res = await fetch(`${API}/stats`);
  return res.json();
}

async function fetchNoteContent(path) {
  const res = await fetch(`${API}/note?path=${encodeURIComponent(path)}`);
  return res.json();
}

async function refreshVault() {
  const btn = document.getElementById('btn-refresh');
  btn.disabled = true;
  btn.textContent = 'Refreshing...';
  await fetch(`${API}/refresh`);
  allNotes = await fetchNotes();
  renderCards(allNotes);
  allStats = await fetchStats();
  renderTagCloud(allStats.tags || {});
  renderStats(allStats);
  btn.disabled = false;
  btn.textContent = '↺ Refresh';
}

// ── Render cards ──────────────────────────────────────────────
function renderCards(notes) {
  const grid = document.getElementById('card-grid');
  const count = document.getElementById('section-count');
  grid.innerHTML = '';

  if (!notes.length) {
    grid.innerHTML = `<div class="empty-state"><p>No notes found.</p></div>`;
    count.textContent = '0 notes';
    return;
  }

  count.textContent = `${notes.length} note${notes.length !== 1 ? 's' : ''}`;

  notes.forEach(note => {
    const s = tagStyle(note.tag);
    const card = document.createElement('div');
    card.className = 'note-card';
    card.innerHTML = `
      <div class="note-card-accent" style="background:${s.accent}"></div>
      <span class="note-tag" style="background:${s.soft};color:${s.text}">${note.tag}</span>
      <h3 class="note-title">${escHtml(note.title)}</h3>
      <p class="note-excerpt">${escHtml(note.excerpt)}</p>
      <div class="note-meta">
        <span class="meta-pill">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><polyline points="12 6 12 12 16 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          ${note.date}
        </span>
        <span class="meta-pill">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          ${note.links} links
        </span>
        <span class="meta-pill">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z" stroke="currentColor" stroke-width="2"/></svg>
          ${note.words.toLocaleString()} words
        </span>
        <span class="meta-pill" style="margin-left:auto;color:var(--text-3)">${note.size_kb}kb</span>
      </div>
    `;
    card.addEventListener('click', () => openReader(note));
    grid.appendChild(card);
  });
}

// ── Tag cloud ─────────────────────────────────────────────────
function renderTagCloud(tags) {
  const cloud = document.getElementById('tag-cloud');
  if (!cloud) return;
  cloud.innerHTML = '';
  Object.entries(tags)
    .sort((a, b) => b[1] - a[1])
    .forEach(([tag, count]) => {
      const s = tagStyle(tag);
      const btn = document.createElement('button');
      btn.className = 'tag-btn' + (activeTag === tag ? ' active' : '');
      btn.style.cssText = `background:${s.soft};color:${s.text};border-color:${s.accent}30`;
      btn.innerHTML = `${escHtml(tag)} <span class="tag-count">${count}</span>`;
      btn.addEventListener('click', () => {
        if (activeTag === tag) {
          activeTag = null;
          renderCards(allNotes);
        } else {
          activeTag = tag;
          renderCards(allNotes.filter(n => n.tag === tag));
        }
        renderTagCloud(tags);
      });
      cloud.appendChild(btn);
    });
}

// ── Stats ─────────────────────────────────────────────────────
function renderStats(stats) {
  const grid = document.getElementById('stats-grid');
  if (!grid) return;
  const items = [
    { value: stats.total_notes  || 0, label: 'Total Notes',       icon: '◻', accent: '#85b9c9' },
    { value: stats.total_words ? (stats.total_words / 1000).toFixed(1) + 'k' : 0, label: 'Total Words', icon: '◎', accent: '#c4a7e7' },
    { value: stats.total_links  || 0, label: 'Total Links',        icon: '⬡', accent: '#f4b183' },
    { value: stats.total_tags   || 0, label: 'Unique Tags',        icon: '◈', accent: '#85c9a7' },
    { value: stats.pdfs_downloaded || 0, label: 'PDFs Downloaded', icon: '⬇', accent: '#e7a7c4' },
  ];
  grid.innerHTML = '';
  items.forEach(item => {
    const el = document.createElement('div');
    el.className = 'stat-card';
    el.innerHTML = `
      <div class="stat-icon" style="background:${item.accent}18;color:${item.accent};font-size:1.1rem">${item.icon}</div>
      <div class="stat-value" style="color:${item.accent}">${item.value}</div>
      <div class="stat-label">${item.label}</div>
    `;
    grid.appendChild(el);
  });
  if (stats.repo_path) {
    const path = document.getElementById('vault-path');
    if (path) path.textContent = stats.repo_path;
  }
}

// ── Graph ─────────────────────────────────────────────────────
function renderGraph(notes) {
  const canvas = document.getElementById('graph-canvas');
  const svg = document.getElementById('graph-svg');
  if (!canvas || !svg) return;

  const W = canvas.clientWidth || 800;
  const H = canvas.clientHeight || 480;
  svg.innerHTML = '';

  // Group notes by tag
  const groups = {};
  notes.forEach(n => { (groups[n.tag] = groups[n.tag] || []).push(n); });
  const tags = Object.keys(groups);

  // Place tag cluster nodes in a circle
  const cx = W / 2, cy = H / 2;
  const R = Math.min(W, H) * 0.32;
  const tagNodes = tags.map((tag, i) => {
    const angle = (i / tags.length) * 2 * Math.PI - Math.PI / 2;
    const s = tagStyle(tag);
    return {
      tag, color: s.accent,
      x: cx + R * Math.cos(angle),
      y: cy + R * Math.sin(angle),
      r: Math.min(28, 14 + groups[tag].length * 2.5),
      count: groups[tag].length,
    };
  });

  // Draw edges between clusters (all connected to center hub)
  tagNodes.forEach(n => {
    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', cx); line.setAttribute('y1', cy);
    line.setAttribute('x2', n.x); line.setAttribute('y2', n.y);
    line.setAttribute('stroke', 'rgba(21,19,26,0.07)');
    line.setAttribute('stroke-width', '1.5');
    svg.appendChild(line);
  });

  // Center hub
  const hub = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  hub.setAttribute('cx', cx); hub.setAttribute('cy', cy); hub.setAttribute('r', 18);
  hub.setAttribute('fill', '#15131a'); hub.setAttribute('opacity', '0.08');
  svg.appendChild(hub);
  const hubText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  hubText.setAttribute('x', cx); hubText.setAttribute('y', cy + 4);
  hubText.setAttribute('text-anchor', 'middle');
  hubText.setAttribute('font-family', 'Urbanist, sans-serif');
  hubText.setAttribute('font-size', '9');
  hubText.setAttribute('fill', 'rgba(21,19,26,0.4)');
  hubText.setAttribute('font-weight', '600');
  hubText.textContent = 'etisiobi';
  svg.appendChild(hubText);

  // Draw tag cluster nodes
  tagNodes.forEach(n => {
    // Glow
    const glow = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    glow.setAttribute('cx', n.x); glow.setAttribute('cy', n.y);
    glow.setAttribute('r', n.r + 12);
    glow.setAttribute('fill', n.color); glow.setAttribute('opacity', '0.1');
    svg.appendChild(glow);

    // Circle
    const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle.setAttribute('cx', n.x); circle.setAttribute('cy', n.y);
    circle.setAttribute('r', n.r);
    circle.setAttribute('fill', n.color); circle.setAttribute('opacity', '0.82');
    circle.style.cursor = 'pointer';
    circle.addEventListener('click', () => {
      activeTag = n.tag;
      renderCards(allNotes.filter(note => note.tag === n.tag));
      switchView('home');
    });
    circle.addEventListener('mouseenter', () => {
      circle.setAttribute('r', String(n.r + 5));
      glow.setAttribute('opacity', '0.22');
    });
    circle.addEventListener('mouseleave', () => {
      circle.setAttribute('r', String(n.r));
      glow.setAttribute('opacity', '0.1');
    });
    svg.appendChild(circle);

    // Count badge
    const countText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    countText.setAttribute('x', n.x); countText.setAttribute('y', n.y + 4);
    countText.setAttribute('text-anchor', 'middle');
    countText.setAttribute('font-family', 'Urbanist, sans-serif');
    countText.setAttribute('font-size', '11');
    countText.setAttribute('fill', 'white');
    countText.setAttribute('font-weight', '700');
    countText.textContent = n.count;
    svg.appendChild(countText);

    // Label
    const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    label.setAttribute('x', n.x); label.setAttribute('y', n.y + n.r + 16);
    label.setAttribute('text-anchor', 'middle');
    label.setAttribute('font-family', 'Urbanist, sans-serif');
    label.setAttribute('font-size', '10');
    label.setAttribute('fill', 'rgba(21,19,26,0.5)');
    label.setAttribute('font-weight', '500');
    label.textContent = n.tag;
    svg.appendChild(label);
  });
}

// ── Note Reader Modal ─────────────────────────────────────────
function openReader(note) {
  currentNote = note;
  document.getElementById('reader-title').textContent = note.title;
  document.getElementById('reader-tag').textContent   = note.tag;
  document.getElementById('reader-date').textContent  = note.date;
  document.getElementById('reader-words').textContent = note.words.toLocaleString() + ' words';
  document.getElementById('reader-path').textContent  = note.path;
  const body = document.getElementById('reader-body');
  body.innerHTML = '<p class="reader-loading">Loading...</p>';
  document.getElementById('reader-overlay').classList.remove('hidden');
  document.body.style.overflow = 'hidden';

  // Fetch full content
  fetchNoteContent(note.path).then(data => {
    body.innerHTML = renderMarkdown(data.content || note.content || '');
  }).catch(() => {
    body.innerHTML = renderMarkdown(note.content || note.excerpt || '');
  });
}

function closeReader() {
  document.getElementById('reader-overlay').classList.add('hidden');
  document.body.style.overflow = '';
  currentNote = null;
}

// Very lightweight markdown → HTML renderer
function renderMarkdown(md) {
  if (!md) return '';
  let html = escHtml(md);

  // Code blocks
  html = html.replace(/```[\s\S]*?```/g, m => {
    const code = m.slice(3, -3).replace(/^[a-z]*\n/, '');
    return `<pre class="md-code"><code>${code}</code></pre>`;
  });
  // Inline code
  html = html.replace(/`([^`]+)`/g, '<code class="md-inline">$1</code>');
  // Headers
  html = html.replace(/^### (.+)$/gm, '<h3 class="md-h3">$1</h3>');
  html = html.replace(/^## (.+)$/gm, '<h2 class="md-h2">$1</h2>');
  html = html.replace(/^# (.+)$/gm, '<h1 class="md-h1">$1</h1>');
  // Bold/italic
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
  // Links
  html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener" class="md-link">$1</a>');
  // Wiki links
  html = html.replace(/\[\[([^\]]+)\]\]/g, '<span class="md-wikilink">$1</span>');
  // Blockquote
  html = html.replace(/^&gt; (.+)$/gm, '<blockquote class="md-quote">$1</blockquote>');
  // HR
  html = html.replace(/^---+$/gm, '<hr class="md-hr"/>');
  // Lists
  html = html.replace(/^- (.+)$/gm, '<li class="md-li">$1</li>');
  html = html.replace(/(<li[^>]*>[\s\S]*?<\/li>)+/g, m => `<ul class="md-ul">${m}</ul>`);
  // Paragraphs
  html = html.replace(/\n{2,}/g, '</p><p class="md-p">');
  html = '<p class="md-p">' + html + '</p>';
  // Clean up empty paras
  html = html.replace(/<p class="md-p"><\/p>/g, '');

  return html;
}

// ── Search ────────────────────────────────────────────────────
function setupSearch() {
  const input    = document.getElementById('search-input');
  const dropdown = document.getElementById('search-dropdown');
  let debounce;

  input.addEventListener('input', () => {
    clearTimeout(debounce);
    debounce = setTimeout(async () => {
      const q = input.value.trim();
      if (!q) {
        dropdown.classList.remove('open');
        renderCards(activeTag ? allNotes.filter(n => n.tag === activeTag) : allNotes);
        return;
      }
      const results = await fetchNotes(q, activeTag || '');
      renderCards(results);
      renderDropdown(results.slice(0, 6));
    }, 220);
  });

  function renderDropdown(items) {
    dropdown.innerHTML = '';
    if (!items.length) {
      dropdown.innerHTML = '<div class="search-empty">No results found.</div>';
    } else {
      items.forEach(note => {
        const s = tagStyle(note.tag);
        const el = document.createElement('div');
        el.className = 'search-item';
        el.innerHTML = `
          <div class="search-icon-wrap" style="background:${s.soft}">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="${s.text}" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          </div>
          <div>
            <div class="search-item-title">${escHtml(note.title)}</div>
            <div class="search-item-tag">${escHtml(note.tag)} · ${note.words.toLocaleString()} words</div>
          </div>
        `;
        el.addEventListener('click', () => { openReader(note); dropdown.classList.remove('open'); });
        dropdown.appendChild(el);
      });
    }
    dropdown.classList.add('open');
  }

  document.addEventListener('click', e => {
    if (!document.getElementById('search-bar').contains(e.target)) {
      dropdown.classList.remove('open');
    }
  });

  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') { e.preventDefault(); input.focus(); input.select(); }
    if (e.key === 'Escape') {
      dropdown.classList.remove('open');
      closeReader();
    }
  });
}

// ── View switching ────────────────────────────────────────────
function switchView(view) {
  document.querySelectorAll('.view').forEach(v => v.classList.add('hidden'));
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  document.getElementById(`view-${view}`).classList.remove('hidden');
  document.querySelector(`[data-view="${view}"]`)?.classList.add('active');
  if (view === 'graph') renderGraph(allNotes);
  if (view === 'stats') renderStats(allStats);
}

function setupNav() {
  document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      switchView(link.dataset.view);
    });
  });
}

// ── Theme toggle ──────────────────────────────────────────────
function setupTheme() {
  let dark = false;
  document.getElementById('btn-theme')?.addEventListener('click', () => {
    dark = !dark;
    const root = document.documentElement;
    if (dark) {
      root.style.setProperty('--bg',            '#12101a');
      root.style.setProperty('--bg-alt',        '#1a1725');
      root.style.setProperty('--bg-card',       '#1e1b2a');
      root.style.setProperty('--text',          '#f0ece6');
      root.style.setProperty('--text-2',        '#9490a0');
      root.style.setProperty('--text-3',        '#5e5a6a');
      root.style.setProperty('--border',        'rgba(240,236,230,0.07)');
      root.style.setProperty('--border-hover',  'rgba(240,236,230,0.14)');
    } else {
      root.style.setProperty('--bg',            '#faf7f3');
      root.style.setProperty('--bg-alt',        '#f4ede6');
      root.style.setProperty('--bg-card',       '#ffffff');
      root.style.setProperty('--text',          '#15131a');
      root.style.setProperty('--text-2',        '#6b6478');
      root.style.setProperty('--text-3',        '#a89eb4');
      root.style.setProperty('--border',        'rgba(21,19,26,0.08)');
      root.style.setProperty('--border-hover',  'rgba(21,19,26,0.15)');
    }
  });
}

// ── Util ──────────────────────────────────────────────────────
function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ── Loading state ─────────────────────────────────────────────
function showLoading() {
  document.getElementById('card-grid').innerHTML = `
    <div class="loading-state">
      <div class="loader"></div>
      <p>Loading your vault…</p>
    </div>`;
}

function showError(msg) {
  document.getElementById('card-grid').innerHTML = `
    <div class="empty-state error-state">
      <p>⚠️ ${msg}</p>
      <p style="font-size:0.8rem;margin-top:8px;color:var(--text-3)">Make sure <code>serve.py</code> is running on port 7891.</p>
    </div>`;
}

// ── Init ──────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', async () => {
  setupSearch();
  setupNav();
  setupTheme();

  // Reader close
  document.getElementById('reader-close')?.addEventListener('click', closeReader);
  document.getElementById('reader-overlay')?.addEventListener('click', e => {
    if (e.target === document.getElementById('reader-overlay')) closeReader();
  });

  // Refresh button
  document.getElementById('btn-refresh')?.addEventListener('click', refreshVault);

  showLoading();
  try {
    [allNotes, allStats] = await Promise.all([fetchNotes(), fetchStats()]);
    renderCards(allNotes);
    renderTagCloud(allStats.tags || {});
    renderStats(allStats);
  } catch (err) {
    showError('Could not connect to WikiOS server.');
  }
});
