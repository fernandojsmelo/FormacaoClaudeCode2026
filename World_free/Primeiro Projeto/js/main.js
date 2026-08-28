import { countWordFrequency, sortByFrequency } from './wordFrequency.js';
import { renderChart, clearChart } from './chart.js';
import { validateFeedback, MAX_FEEDBACK_CHARS } from './feedback.js';

const textInput = document.getElementById('text-input');
const charCount = document.getElementById('char-count');
const translateBtn = document.getElementById('translate-btn');
const tableBody = document.getElementById('frequency-table-body');
const errorMessage = document.getElementById('error-message');
const emptyState = document.getElementById('empty-state');
const chartCanvas = document.getElementById('frequency-chart');
const textInputGroup = document.getElementById('text-input-group');
const urlInputGroup = document.getElementById('url-input-group');
const urlInput = document.getElementById('url-input');
const loadUrlBtn = document.getElementById('load-url-btn');
const urlError = document.getElementById('url-error');
const modeRadios = document.querySelectorAll('input[name="input-mode"]');
const feedbackToggleBtn = document.getElementById('feedback-toggle-btn');
const feedbackPanel = document.getElementById('feedback-panel');
const feedbackInput = document.getElementById('feedback-input');
const feedbackCharCount = document.getElementById('feedback-char-count');
const feedbackSubmitBtn = document.getElementById('feedback-submit-btn');
const feedbackError = document.getElementById('feedback-error');
const feedbackSuccess = document.getElementById('feedback-success');

const MAX_CHARS = 2048;
const CHAR_WARNING_THRESHOLD = 0.9;
const API_BASE_URL = 'http://localhost:3000';
const FEEDBACK_STORAGE_KEY = 'word-frequency-feedback';

textInput.addEventListener('input', () => {
  const length = textInput.value.length;
  charCount.textContent = `${length} / ${MAX_CHARS}`;
  charCount.classList.toggle('char-count--warning', length >= MAX_CHARS * CHAR_WARNING_THRESHOLD);
});

modeRadios.forEach((radio) => {
  radio.addEventListener('change', () => {
    const isUrlMode = radio.value === 'url' && radio.checked;
    textInputGroup.hidden = isUrlMode;
    urlInputGroup.hidden = !isUrlMode;
  });
});

loadUrlBtn.addEventListener('click', async () => {
  const url = urlInput.value.trim();
  urlError.hidden = true;

  if (url === '') {
    urlError.textContent = 'Por favor, insira uma URL.';
    urlError.hidden = false;
    return;
  }

  loadUrlBtn.disabled = true;
  loadUrlBtn.textContent = 'Carregando...';

  try {
    const response = await fetch(`${API_BASE_URL}/api/extract?url=${encodeURIComponent(url)}`);
    const data = await response.json();

    if (!response.ok) {
      urlError.textContent = data.error || 'Não foi possível carregar o conteúdo da URL.';
      urlError.hidden = false;
      return;
    }

    textInput.value = data.text;
    textInput.dispatchEvent(new Event('input'));
  } catch {
    urlError.textContent = 'Não foi possível conectar ao servidor. Verifique se o backend está rodando.';
    urlError.hidden = false;
  } finally {
    loadUrlBtn.disabled = false;
    loadUrlBtn.textContent = 'Carregar';
  }
});

translateBtn.addEventListener('click', () => {
  emptyState.hidden = true;

  if (textInput.value.trim() === '') {
    errorMessage.hidden = false;
    tableBody.innerHTML = '';
    clearChart();
    return;
  }

  errorMessage.hidden = true;
  const entries = sortByFrequency(countWordFrequency(textInput.value));

  if (entries.length === 0) {
    emptyState.hidden = false;
    tableBody.innerHTML = '';
    clearChart();
    return;
  }

  renderTable(entries);
  renderChart(chartCanvas, entries);
  pulseButton();
});

function renderTable(entries) {
  tableBody.innerHTML = '';
  for (const [word, count] of entries) {
    const row = document.createElement('tr');
    row.innerHTML = `<td>${word}</td><td>${count}</td>`;
    tableBody.appendChild(row);
  }
}

function pulseButton() {
  translateBtn.classList.remove('is-active');
  // Força reflow para permitir reiniciar a animação em cliques consecutivos.
  void translateBtn.offsetWidth;
  translateBtn.classList.add('is-active');
}

feedbackToggleBtn.addEventListener('click', () => {
  const isHidden = feedbackPanel.hidden;
  feedbackPanel.hidden = !isHidden;
  feedbackToggleBtn.setAttribute('aria-expanded', String(isHidden));
});

feedbackInput.addEventListener('input', () => {
  feedbackCharCount.textContent = `${feedbackInput.value.length} / ${MAX_FEEDBACK_CHARS}`;
});

feedbackSubmitBtn.addEventListener('click', () => {
  feedbackSuccess.hidden = true;
  const { valid, error } = validateFeedback(feedbackInput.value);

  if (!valid) {
    feedbackError.textContent = error;
    feedbackError.hidden = false;
    return;
  }

  feedbackError.hidden = true;
  saveFeedback(feedbackInput.value.trim());
  feedbackInput.value = '';
  feedbackCharCount.textContent = `0 / ${MAX_FEEDBACK_CHARS}`;
  feedbackSuccess.hidden = false;
});

function saveFeedback(text) {
  const stored = JSON.parse(localStorage.getItem(FEEDBACK_STORAGE_KEY) || '[]');
  stored.push({ text, submittedAt: new Date().toISOString() });
  localStorage.setItem(FEEDBACK_STORAGE_KEY, JSON.stringify(stored));
}
