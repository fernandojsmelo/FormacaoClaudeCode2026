/**
 * Automação de Resumo Diário de Compromissos
 * ============================================
 *
 * Fluxo:
 *   1. Busca os compromissos do dia no Google Calendar.
 *   2. Para cada compromisso, busca no Gmail e-mails cujo ASSUNTO
 *      corresponda ao nome/título da reunião.
 *   3. Baixa os anexos relevantes e salva no Google Drive, em uma
 *      pasta nomeada com a data do dia (ex: 27-08-2026).
 *   4. Gera um resumo final com os compromissos e os anexos organizados.
 *
 * Regras de negócio definidas pelo usuário:
 *   - Relacionamento e-mail <-> compromisso: por ASSUNTO do e-mail.
 *   - Organização no Drive: uma pasta por dia (DD-MM-AAAA).
 *   - Disparo: manual, sob demanda (ex: "roda meu resumo diário"),
 *     sem agendamento automático.
 *
 * Requisitos:
 *   npm install googleapis
 *
 * Autenticação:
 *   Este script assume que já existe um fluxo OAuth2 configurado
 *   (arquivo token.json / credentials.json) com os escopos:
 *     - https://www.googleapis.com/auth/calendar.readonly
 *     - https://www.googleapis.com/auth/gmail.readonly
 *     - https://www.googleapis.com/auth/drive.file
 */

const fs = require("fs");
const { google } = require("googleapis");
const { Readable } = require("stream");

const SCOPES = [
  "https://www.googleapis.com/auth/calendar.readonly",
  "https://www.googleapis.com/auth/gmail.readonly",
  "https://www.googleapis.com/auth/drive.file",
];

const TOKEN_PATH = "token.json";

// --------------------------------------------------------------------------- //
// Autenticação
// --------------------------------------------------------------------------- //

/**
 * Carrega as credenciais OAuth2 já autorizadas (token.json) e devolve
 * um cliente autenticado do Google.
 */
function carregarCredenciais() {
  if (!fs.existsSync(TOKEN_PATH)) {
    throw new Error(
      "token.json não encontrado. Rode o fluxo de autorização OAuth2 " +
        "antes de usar este script.",
    );
  }

  const token = JSON.parse(fs.readFileSync(TOKEN_PATH, "utf-8"));

  const oAuth2Client = new google.auth.OAuth2(
    token.client_id,
    token.client_secret,
    token.redirect_uri,
  );
  oAuth2Client.setCredentials(token);

  return oAuth2Client;
}

// --------------------------------------------------------------------------- //
// Etapa 1: Google Calendar — buscar compromissos do dia
// --------------------------------------------------------------------------- //

/**
 * Retorna todos os compromissos do dia informado (padrão: hoje).
 * @param {import('google-auth-library').OAuth2Client} auth
 * @param {Date} [data]
 * @returns {Promise<Array<Object>>}
 */
async function buscarCompromissosDoDia(auth, data = new Date()) {
  const calendar = google.calendar({ version: "v3", auth });

  const inicioDia = new Date(data);
  inicioDia.setHours(0, 0, 0, 0);
  const fimDia = new Date(data);
  fimDia.setHours(23, 59, 59, 999);

  const resultado = await calendar.events.list({
    calendarId: "primary",
    timeMin: inicioDia.toISOString(),
    timeMax: fimDia.toISOString(),
    singleEvents: true,
    orderBy: "startTime",
  });

  const eventos = resultado.data.items || [];

  return eventos.map((evento) => ({
    id: evento.id,
    titulo: evento.summary || "(sem título)",
    inicio: new Date(evento.start.dateTime || evento.start.date),
    fim: new Date(evento.end.dateTime || evento.end.date),
    participantes: (evento.attendees || []).map((p) => p.email).filter(Boolean),
  }));
}

// --------------------------------------------------------------------------- //
// Etapa 2: Gmail — localizar e-mails cujo assunto bate com o compromisso
// --------------------------------------------------------------------------- //

/**
 * Busca e-mails no Gmail cujo assunto contenha o título da reunião.
 */
async function buscarEmailsPorAssunto(auth, tituloReuniao) {
  const gmail = google.gmail({ version: "v1", auth });
  const query = `subject:"${tituloReuniao}" has:attachment`;

  const resultado = await gmail.users.messages.list({
    userId: "me",
    q: query,
  });

  const mensagens = resultado.data.messages || [];

  const detalhes = [];
  for (const msg of mensagens) {
    const detalhe = await gmail.users.messages.get({
      userId: "me",
      id: msg.id,
    });
    detalhes.push(detalhe.data);
  }
  return detalhes;
}

/**
 * Extrai os anexos de uma mensagem do Gmail.
 */
async function extrairAnexos(auth, mensagem) {
  const gmail = google.gmail({ version: "v1", auth });
  const anexos = [];

  const headers = mensagem.payload.headers || [];
  const assunto =
    headers.find((h) => h.name === "Subject")?.value || "(sem assunto)";

  const partes = mensagem.payload.parts || [];

  for (const parte of partes) {
    if (parte.filename && parte.body?.attachmentId) {
      const anexoDados = await gmail.users.messages.attachments.get({
        userId: "me",
        messageId: mensagem.id,
        id: parte.body.attachmentId,
      });

      const conteudo = Buffer.from(anexoDados.data.data, "base64");

      anexos.push({
        nomeArquivo: parte.filename,
        conteudo,
        mimeType: parte.mimeType || "application/octet-stream",
        emailAssunto: assunto,
      });
    }
  }
  return anexos;
}

// --------------------------------------------------------------------------- //
// Etapa 3: Google Drive — organizar anexos em pasta por dia
// --------------------------------------------------------------------------- //

/**
 * Obtém (ou cria) a pasta do Drive nomeada com a data (DD-MM-AAAA).
 */
async function obterOuCriarPastaDoDia(auth, data = new Date()) {
  const drive = google.drive({ version: "v3", auth });

  const dia = String(data.getDate()).padStart(2, "0");
  const mes = String(data.getMonth() + 1).padStart(2, "0");
  const ano = data.getFullYear();
  const nomePasta = `${dia}-${mes}-${ano}`;

  const query =
    `name = '${nomePasta}' and mimeType = 'application/vnd.google-apps.folder' ` +
    "and trashed = false";

  const resultado = await drive.files.list({
    q: query,
    fields: "files(id, name)",
  });

  const pastas = resultado.data.files || [];
  if (pastas.length > 0) {
    return pastas[0].id;
  }

  const pasta = await drive.files.create({
    requestBody: {
      name: nomePasta,
      mimeType: "application/vnd.google-apps.folder",
    },
    fields: "id",
  });

  return pasta.data.id;
}

/**
 * Salva um anexo dentro da pasta do dia no Drive.
 */
async function salvarAnexoNoDrive(auth, pastaId, anexo) {
  const drive = google.drive({ version: "v3", auth });

  const arquivo = await drive.files.create({
    requestBody: {
      name: anexo.nomeArquivo,
      parents: [pastaId],
    },
    media: {
      mimeType: anexo.mimeType,
      body: Readable.from(anexo.conteudo),
    },
    fields: "id",
  });

  return arquivo.data.id;
}

// --------------------------------------------------------------------------- //
// Etapa 4: Orquestração — gerar o resumo diário completo
// --------------------------------------------------------------------------- //

/**
 * Executa o fluxo completo e retorna um resumo em texto.
 * @param {Date} [data]
 * @returns {Promise<string>}
 */
async function rodarResumoDiario(data = new Date()) {
  const auth = carregarCredenciais();

  const compromissos = await buscarCompromissosDoDia(auth, data);
  const dataFormatada = data.toLocaleDateString("pt-BR");

  if (compromissos.length === 0) {
    return `Nenhum compromisso encontrado para ${dataFormatada}.`;
  }

  const pastaId = await obterOuCriarPastaDoDia(auth, data);

  const linhasResumo = [`Resumo de ${dataFormatada}:\n`];

  for (const compromisso of compromissos) {
    const hora = compromisso.inicio.toLocaleTimeString("pt-BR", {
      hour: "2-digit",
      minute: "2-digit",
    });
    linhasResumo.push(`- ${hora} | ${compromisso.titulo}`);

    const emails = await buscarEmailsPorAssunto(auth, compromisso.titulo);
    let totalAnexos = 0;

    for (const email of emails) {
      const anexos = await extrairAnexos(auth, email);
      for (const anexo of anexos) {
        await salvarAnexoNoDrive(auth, pastaId, anexo);
        totalAnexos += 1;
      }
    }

    if (totalAnexos > 0) {
      linhasResumo.push(
        `    -> ${totalAnexos} anexo(s) salvo(s) na pasta do dia no Drive.`,
      );
    } else {
      linhasResumo.push("    -> Nenhum e-mail/anexo relacionado encontrado.");
    }
  }

  return linhasResumo.join("\n");
}

// --------------------------------------------------------------------------- //
// Execução direta via linha de comando
// --------------------------------------------------------------------------- //

if (require.main === module) {
  rodarResumoDiario()
    .then((resumo) => console.log(resumo))
    .catch((erro) => {
      console.error("Erro ao rodar o resumo diário:", erro.message);
      process.exit(1);
    });
}

module.exports = {
  carregarCredenciais,
  buscarCompromissosDoDia,
  buscarEmailsPorAssunto,
  extrairAnexos,
  obterOuCriarPastaDoDia,
  salvarAnexoNoDrive,
  rodarResumoDiario,
};
