// FocoFlow — interações da landing page (sem dependências)

// Modo escuro: alterna o atributo data-theme e lembra a escolha.
const botaoTema = document.getElementById('theme-toggle');

function temaAtual() {
  const definido = document.documentElement.getAttribute('data-theme');
  if (definido) return definido;
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

botaoTema.addEventListener('click', () => {
  const novo = temaAtual() === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', novo);
  try { localStorage.setItem('focoflow-tema', novo); } catch (e) {}
});

// Formulário de inscrição: valida o e-mail antes de "enviar".
const form = document.getElementById('signup-form');
const campoEmail = document.getElementById('email');
const mensagem = document.getElementById('form-msg');
const padraoEmail = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

form.addEventListener('submit', (evento) => {
  evento.preventDefault();
  const email = campoEmail.value.trim();

  if (!padraoEmail.test(email)) {
    mensagem.textContent = 'Digite um e-mail válido, como nome@exemplo.com.';
    mensagem.className = 'form-msg erro';
    campoEmail.setAttribute('aria-invalid', 'true');
    campoEmail.focus();
    return;
  }

  campoEmail.removeAttribute('aria-invalid');
  mensagem.textContent = 'Pronto! Enviamos o link de download para ' + email + '.';
  mensagem.className = 'form-msg ok';
  form.reset();
});
