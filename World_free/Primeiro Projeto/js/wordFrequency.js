export function tokenize(text) {
  return text.toLowerCase().match(/[\p{L}\p{N}']+/gu) || [];
}

export function countWordFrequency(text) {
  const counts = new Map();
  for (const word of tokenize(text)) {
    counts.set(word, (counts.get(word) || 0) + 1);
  }
  return counts;
}

export function sortByFrequency(counts) {
  return [...counts].sort((a, b) => b[1] - a[1]);
}
