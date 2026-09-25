import { test } from 'node:test';
import assert from 'node:assert/strict';
import { tokenize, countWordFrequency, sortByFrequency } from '../js/wordFrequency.js';

test('tokenize splits words and lowercases them', () => {
  assert.deepEqual(tokenize('The Cat sat'), ['the', 'cat', 'sat']);
});

test('tokenize ignores punctuation', () => {
  assert.deepEqual(tokenize('Hello, world!'), ['hello', 'world']);
});

test('tokenize returns empty array for empty text', () => {
  assert.deepEqual(tokenize(''), []);
});

test('tokenize handles multiple spaces and line breaks', () => {
  assert.deepEqual(tokenize('foo   bar\nbaz'), ['foo', 'bar', 'baz']);
});

test('countWordFrequency counts repeated words', () => {
  const counts = countWordFrequency('the cat the dog the cat');
  assert.equal(counts.get('the'), 3);
  assert.equal(counts.get('cat'), 2);
  assert.equal(counts.get('dog'), 1);
});

test('countWordFrequency returns empty map for empty text', () => {
  const counts = countWordFrequency('');
  assert.equal(counts.size, 0);
});

test('sortByFrequency orders entries in descending count', () => {
  const counts = countWordFrequency('the cat the dog the cat bird');
  assert.deepEqual(sortByFrequency(counts), [
    ['the', 3],
    ['cat', 2],
    ['dog', 1],
    ['bird', 1],
  ]);
});

test('sortByFrequency returns empty array for empty map', () => {
  assert.deepEqual(sortByFrequency(new Map()), []);
});
