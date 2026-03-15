/**
 * Kanoon Mitra – Legal Advisory Bot
 * Client-side chat logic with double-tick read receipts
 */

(function () {
  'use strict';

  // ── DOM refs ──────────────────────────────────────────────────────────
  const messagesContainer = document.getElementById('messagesContainer');
  const userInput         = document.getElementById('userInput');
  const sendBtn           = document.getElementById('sendBtn');
  const legalRefs         = document.getElementById('legalRefs');
  const sidebar           = document.getElementById('sidebar');
  const menuBtn           = document.getElementById('menuBtn');
  const sidebarClose      = document.getElementById('sidebarClose');
  const overlay           = document.getElementById('overlay');

  // ── State ─────────────────────────────────────────────────────────────
  const history = [];

  // ── Sidebar toggle ────────────────────────────────────────────────────
  function openSidebar()  { sidebar.classList.add('is-open'); overlay.classList.add('is-active'); }
  function closeSidebar() { sidebar.classList.remove('is-open'); overlay.classList.remove('is-active'); }
  menuBtn.addEventListener('click', openSidebar);
  sidebarClose.addEventListener('click', closeSidebar);
  overlay.addEventListener('click', closeSidebar);

  // ── Helpers ───────────────────────────────────────────────────────────
  function formatTime() {
    return new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit', hour12: true });
  }

  /** Very lightweight Markdown-like renderer (bold, code, lists, hr) */
  function renderMarkdown(text) {
    // Guard against extremely long inputs to prevent ReDoS
    const safeText = text.length > 20000 ? text.slice(0, 20000) + '…' : text;
    return safeText
      // Escape HTML
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      // **bold**
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      // *italic*
      .replace(/\*(.+?)\*/g, '<em>$1</em>')
      // `code`
      .replace(/`(.+?)`/g, '<code class="md-code">$1</code>')
      // Horizontal rule
      .replace(/^---$/gm, '<hr class="md-hr" />')
      // Unordered list lines starting with - or •
      .replace(/^[-•] (.+)$/gm, '<li>$1</li>')
      // Wrap consecutive <li> items in <ul> (non-greedy to avoid ReDoS)
      .replace(/(?:<li>.*?<\/li>\n?)+/g, m => `<ul>${m}</ul>`)
      // Numbered list
      .replace(/^\d+\. (.+)$/gm, '<li>$1</li>')
      // Line breaks to <br>
      .replace(/\n/g, '<br />');
  }

  /** Scroll messages to bottom */
  function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  // ── Message rendering ─────────────────────────────────────────────────
  /**
   * @param {'user'|'bot'} role
   * @param {string}       text   – plain text or markdown
   * @param {'sent'|'read'} tickState
   */
  function addMessage(role, text, tickState) {
    const wrapper = document.createElement('div');
    wrapper.classList.add('message', `message--${role}`);

    const bubble = document.createElement('div');
    bubble.classList.add('message-bubble');
    bubble.innerHTML = renderMarkdown(text);

    // Meta row (time + ticks)
    const meta = document.createElement('div');
    meta.classList.add('message-meta');

    const timeEl = document.createElement('span');
    timeEl.classList.add('message-time');
    timeEl.textContent = formatTime();

    const ticks = document.createElement('span');
    ticks.classList.add('ticks');
    setTickState(ticks, tickState || (role === 'user' ? 'sent' : 'read'));

    meta.appendChild(timeEl);
    meta.appendChild(ticks);
    bubble.appendChild(meta);
    wrapper.appendChild(bubble);
    messagesContainer.appendChild(wrapper);
    scrollToBottom();
    return { wrapper, ticks };
  }

  /** Update tick appearance: 'sending' | 'sent' | 'read' */
  function setTickState(tickEl, state) {
    tickEl.className = 'ticks';
    if (state === 'sending') {
      tickEl.textContent = '✓';
      tickEl.classList.add('ticks--sent');
      tickEl.title = 'Sending…';
    } else if (state === 'sent') {
      tickEl.textContent = '✓✓';
      tickEl.classList.add('ticks--sent');
      tickEl.title = 'Sent';
    } else if (state === 'read') {
      tickEl.textContent = '✓✓';
      tickEl.classList.add('ticks--read');
      tickEl.title = 'Read';
    }
  }

  /** Show animated typing indicator */
  function showTypingIndicator() {
    const wrapper = document.createElement('div');
    wrapper.classList.add('message', 'message--bot', 'typing-indicator');
    wrapper.id = 'typingIndicator';
    const bubble = document.createElement('div');
    bubble.classList.add('message-bubble');
    [0, 1, 2].forEach(() => {
      const dot = document.createElement('div');
      dot.classList.add('typing-dot');
      bubble.appendChild(dot);
    });
    wrapper.appendChild(bubble);
    messagesContainer.appendChild(wrapper);
    scrollToBottom();
  }

  function removeTypingIndicator() {
    const el = document.getElementById('typingIndicator');
    if (el) el.remove();
  }

  // ── Legal refs sidebar ────────────────────────────────────────────────
  function renderLegalRefs(refs) {
    if (!refs) return;
    const {
      domains = [],
      bns_sections = [],
      bnss_sections = [],
      bsa_sections = [],
      personal_law = [],
      cases = [],
    } = refs;

    let html = '';

    if (domains.length) {
      html += `<div class="ref-section"><h3>Legal Domain</h3>`;
      domains.forEach(d => {
        html += `<span class="ref-badge ref-badge--domain">${escHtml(d)}</span>`;
      });
      html += `</div>`;
    }

    if (bns_sections.length) {
      html += `<div class="ref-section"><h3>BNS (Bharatiya Nyaya Sanhita)</h3>`;
      bns_sections.forEach(s => {
        html += `<span class="ref-badge" title="${escHtml(s.title)}">§ ${escHtml(String(s.section))} – ${escHtml(s.title)}</span>`;
      });
      html += `</div>`;
    }

    if (bnss_sections.length) {
      html += `<div class="ref-section"><h3>BNSS (Bharatiya Nagarik Suraksha Sanhita)</h3>`;
      bnss_sections.forEach(s => {
        html += `<span class="ref-badge" title="${escHtml(s.title)}">§ ${escHtml(String(s.section))} – ${escHtml(s.title)}</span>`;
      });
      html += `</div>`;
    }

    if (bsa_sections.length) {
      html += `<div class="ref-section"><h3>BSA (Bharatiya Sakshya Adhiniyam)</h3>`;
      bsa_sections.forEach(s => {
        html += `<span class="ref-badge" title="${escHtml(s.title)}">§ ${escHtml(String(s.section))} – ${escHtml(s.title)}</span>`;
      });
      html += `</div>`;
    }

    if (personal_law.length) {
      html += `<div class="ref-section"><h3>Personal Laws</h3>`;
      personal_law.forEach(p => {
        html += `<span class="ref-badge ref-badge--personal" title="${escHtml(p.law)}">${escHtml(p.law)} – ${escHtml(p.title)}</span>`;
      });
      html += `</div>`;
    }

    if (cases.length) {
      html += `<div class="ref-section"><h3>Supreme Court Cases</h3>`;
      cases.forEach(c => {
        html += `<span class="ref-badge ref-badge--case" title="${escHtml(c.citation)}">${escHtml(c.name)} (${escHtml(String(c.year))})</span>`;
      });
      html += `</div>`;
    }

    legalRefs.innerHTML = html || '<p class="sidebar-placeholder">No specific laws matched. Showing general guidance.</p>';
  }

  function escHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // ── Send message ──────────────────────────────────────────────────────
  async function sendMessage() {
    const text = userInput.value.trim();
    if (!text || sendBtn.disabled) return;

    userInput.value = '';
    autoResize();
    sendBtn.disabled = true;

    // Show user message with single-tick (sending)
    const { ticks: userTicks } = addMessage('user', text, 'sending');

    // Immediately upgrade to double-tick "sent"
    setTimeout(() => setTickState(userTicks, 'sent'), 300);

    history.push({ role: 'user', content: text });
    showTypingIndicator();

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, history: history.slice(-10) }),
      });

      removeTypingIndicator();

      if (!response.ok) {
        const err = await response.json().catch(() => ({}));
        addMessage('bot', `⚠️ Error: ${err.error || response.statusText}`, 'read');
        sendBtn.disabled = false;
        return;
      }

      const data = await response.json();
      const reply = data.reply || '(No response)';

      // Mark user message as read (blue double ticks) once bot replies
      setTickState(userTicks, 'read');

      addMessage('bot', reply, 'read');
      history.push({ role: 'assistant', content: reply });

      renderLegalRefs(data.legal_refs);

    } catch (err) {
      removeTypingIndicator();
      addMessage('bot', `⚠️ Network error: ${err.message}`, 'read');
    }

    sendBtn.disabled = false;
    userInput.focus();
  }

  // ── Auto-resize textarea ──────────────────────────────────────────────
  function autoResize() {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 120) + 'px';
  }

  userInput.addEventListener('input', autoResize);

  // Send on Enter (Shift+Enter for newline)
  userInput.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  sendBtn.addEventListener('click', sendMessage);

  // Set initial timestamps on pre-rendered welcome message
  document.querySelectorAll('.message-time[data-time="now"]').forEach(el => {
    el.textContent = formatTime();
    el.removeAttribute('data-time');
  });

  userInput.focus();
})();
