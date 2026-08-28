export const MAX_FEEDBACK_CHARS = 500;

export function validateFeedback(text, maxChars = MAX_FEEDBACK_CHARS) {
  const trimmed = text.trim();

  if (trimmed === '') {
    return { valid: false, error: 'Por favor, escreva um feedback antes de enviar.' };
  }

  if (trimmed.length > maxChars) {
    return { valid: false, error: `O feedback deve ter no máximo ${maxChars} caracteres.` };
  }

  return { valid: true, error: null };
}
