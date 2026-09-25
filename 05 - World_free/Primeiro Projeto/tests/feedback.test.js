import { test } from 'node:test';
import assert from 'node:assert/strict';
import { validateFeedback, MAX_FEEDBACK_CHARS } from '../js/feedback.js';

test('validateFeedback rejects empty text', () => {
  const result = validateFeedback('');
  assert.equal(result.valid, false);
  assert.match(result.error, /feedback/i);
});

test('validateFeedback rejects whitespace-only text', () => {
  const result = validateFeedback('   \n  ');
  assert.equal(result.valid, false);
});

test('validateFeedback accepts non-empty text', () => {
  const result = validateFeedback('This app is great!');
  assert.equal(result.valid, true);
  assert.equal(result.error, null);
});

test('validateFeedback accepts text exactly at the max length', () => {
  const text = 'a'.repeat(MAX_FEEDBACK_CHARS);
  const result = validateFeedback(text);
  assert.equal(result.valid, true);
});

test('validateFeedback rejects text over the max length', () => {
  const text = 'a'.repeat(MAX_FEEDBACK_CHARS + 1);
  const result = validateFeedback(text);
  assert.equal(result.valid, false);
  assert.match(result.error, new RegExp(String(MAX_FEEDBACK_CHARS)));
});

test('validateFeedback trims surrounding whitespace before validating length', () => {
  const text = `  ${'a'.repeat(MAX_FEEDBACK_CHARS)}  `;
  const result = validateFeedback(text);
  assert.equal(result.valid, true);
});

test('validateFeedback respects a custom max length', () => {
  const result = validateFeedback('hello world', 5);
  assert.equal(result.valid, false);
});
