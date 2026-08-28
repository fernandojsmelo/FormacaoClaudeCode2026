import express from 'express';
import cors from 'cors';
import * as cheerio from 'cheerio';

const app = express();
const PORT = process.env.PORT || 3000;
const MAX_CHARS = 2048;
const FETCH_TIMEOUT_MS = 8000;

app.use(cors());

app.get('/api/extract', async (req, res) => {
  const { url } = req.query;

  let parsedUrl;
  try {
    parsedUrl = new URL(url);
  } catch {
    return res.status(400).json({ error: 'URL inválida.' });
  }

  if (!['http:', 'https:'].includes(parsedUrl.protocol)) {
    return res.status(400).json({ error: 'A URL deve usar http ou https.' });
  }

  let response;
  try {
    response = await fetch(parsedUrl, { signal: AbortSignal.timeout(FETCH_TIMEOUT_MS) });
  } catch {
    return res.status(502).json({ error: 'Não foi possível acessar a URL informada.' });
  }

  if (!response.ok) {
    return res.status(502).json({ error: `A URL retornou status ${response.status}.` });
  }

  const contentType = response.headers.get('content-type') || '';
  if (!contentType.includes('text/html')) {
    return res.status(415).json({ error: 'A URL não retornou conteúdo HTML.' });
  }

  const html = await response.text();
  const text = extractText(html).slice(0, MAX_CHARS);
  res.json({ text });
});

export function extractText(html) {
  const $ = cheerio.load(html);
  $('script, style, noscript').remove();
  return $('body').text().replace(/\s+/g, ' ').trim();
}

app.listen(PORT, () => {
  console.log(`Word Frequency backend rodando em http://localhost:${PORT}`);
});
