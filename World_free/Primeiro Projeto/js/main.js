import { countWordFrequency, sortByFrequency } from './wordFrequency.js';
import { renderChart, clearChart } from './chart.js';

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

const MAX_CHARS = 2048;
const CHAR_WARNING_THRESHOLD = 0.9;
const API_BASE_URL = 'http://localhost:3000';

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
