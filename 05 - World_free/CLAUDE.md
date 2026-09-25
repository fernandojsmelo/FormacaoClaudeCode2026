# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository layout

This repository currently contains a single project, **Word Frequency**, under
`Primeiro Projeto/`. All commands below must be run from that directory
(`cd "Primeiro Projeto"`).

Full spec (user stories) is in `Primeiro Projeto/App.md`; a Portuguese
project-specific guide already exists at `Primeiro Projeto/CLAUDE.md` — read
it for phase-by-phase scope and code conventions.

## What it is

A vanilla JS app that tokenizes a block of text (or text extracted from a
URL), counts word frequency, and renders it as a table + bar chart. No
framework, no database — all counting logic runs client-side in memory.

## Commands

Run from `Primeiro Projeto/`:

```bash
# Serve the static front-end
npx serve .
# or
python3 -m http.server 8000

# Run the test suite (Node's built-in test runner)
npm test

# Run a single test file
node --test tests/wordFrequency.test.js

# Run the backend (only needed for the URL-input feature)
cd server
npm install
npm start
```

The backend listens on `http://localhost:3000` and is hardcoded as
`API_BASE_URL` in `js/main.js` — the front-end's URL-mode input will fail
silently (caught fetch error) if the backend isn't running.

## Architecture

- **`js/wordFrequency.js`** — pure logic, no DOM access: `tokenize` (case
  folds and strips punctuation via a Unicode-aware regex), `countWordFrequency`
  (returns a `Map`), `sortByFrequency` (descending by count). This is the only
  module covered by tests — keep it side-effect-free so it stays that way.
- **`js/main.js`** — wires up DOM events (mode toggle between text/URL input,
  char-count display, Translate click) and calls into `wordFrequency.js` and
  `chart.js`. Owns all rendering/DOM mutation.
- **`js/chart.js`** — Chart.js wrapper (loaded via CDN `<script>` in
  `index.html`, not npm). Reads CSS custom properties (`--accent`, `--fg`,
  `--border`) off `document.documentElement` so the chart matches the page
  theme; caps rendered bars at `MAX_CHART_ENTRIES` (15).
- **`server/index.js`** — standalone Express service, separate `package.json`/
  `node_modules` from the front-end. Single endpoint `GET /api/extract?url=`:
  validates the URL is http(s), fetches it, strips `script`/`style`/`noscript`
  with cheerio, and returns plain text truncated to `MAX_CHARS` (2048, kept in
  sync manually with the front-end's own limit — no shared constant). Exists
  solely to work around CORS when analyzing an external page from the browser.
- Two ES module trees with no shared tooling: the front-end (`js/`, root
  `package.json`, `type: module`, tests via `node --test`) and the server
  (`server/`, its own `package.json`) are installed/run independently.
