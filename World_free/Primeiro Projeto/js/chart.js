const MAX_CHART_ENTRIES = 15;

let chartInstance = null;

export function renderChart(canvas, entries) {
  const topEntries = entries.slice(0, MAX_CHART_ENTRIES);
  const styles = getComputedStyle(document.documentElement);
  const accent = styles.getPropertyValue('--accent').trim();
  const fg = styles.getPropertyValue('--fg').trim();
  const border = styles.getPropertyValue('--border').trim();

  if (chartInstance) {
    chartInstance.destroy();
  }

  chartInstance = new Chart(canvas, {
    type: 'bar',
    data: {
      labels: topEntries.map(([word]) => word),
      datasets: [
        {
          label: 'Frequência',
          data: topEntries.map(([, count]) => count),
          backgroundColor: accent,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
      },
      scales: {
        x: {
          ticks: { color: fg },
          grid: { color: border },
        },
        y: {
          beginAtZero: true,
          ticks: { color: fg, precision: 0 },
          grid: { color: border },
        },
      },
    },
  });
}

export function clearChart() {
  if (chartInstance) {
    chartInstance.destroy();
    chartInstance = null;
  }
}
