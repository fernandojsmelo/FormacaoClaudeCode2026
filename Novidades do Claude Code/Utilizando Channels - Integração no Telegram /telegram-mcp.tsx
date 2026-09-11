// Telegram MCP — servidor MCP remoto + receptor de webhook do Telegram.
// Rodando no Val Town. Docs: https://docs.val.town/guides/telegram
//
// Variáveis de ambiente necessárias:
//   TELEGRAM_TOKEN  — token do bot (BotFather)
//   MCP_BEARER      — senha que o plugin usa para falar com este servidor
//
// Rotas:
//   POST /mcp       — endpoint MCP (JSON-RPC), protegido por MCP_BEARER
//   POST /webhook   — updates do Telegram, protegido pelo secret_token
//   GET  /          — página de status

import { sqlite } from "https://esm.town/v/std/sqlite/main.ts";

const TOKEN = Deno.env.get("TELEGRAM_TOKEN");
const BEARER = Deno.env.get("MCP_BEARER");
const API = `https://api.telegram.org/bot${TOKEN}`;
// Secret do webhook derivado do próprio token (padrão do guia do Val Town).
const WEBHOOK_SECRET = TOKEN ? TOKEN.split(":")[1] : "";

const PROTOCOL_VERSION = "2025-06-18";

// ---------------------------------------------------------------- storage

let schemaReady: Promise<void> | null = null;

function ensureSchema(): Promise<void> {
  schemaReady ??= (async () => {
    await sqlite.execute(`CREATE TABLE IF NOT EXISTS messages (
      id           INTEGER PRIMARY KEY AUTOINCREMENT,
      update_id    INTEGER UNIQUE,
      chat_id      TEXT NOT NULL,
      chat_title   TEXT,
      chat_type    TEXT,
      from_name    TEXT,
      text         TEXT,
      has_media    INTEGER NOT NULL DEFAULT 0,
      sent_at      TEXT NOT NULL,
      received_at  TEXT NOT NULL DEFAULT (datetime('now'))
    )`);
    await sqlite.execute(
      `CREATE INDEX IF NOT EXISTS messages_chat_idx ON messages (chat_id, id DESC)`,
    );
    await sqlite.execute(`CREATE TABLE IF NOT EXISTS settings (
      key   TEXT PRIMARY KEY,
      value TEXT NOT NULL
    )`);
  })();
  return schemaReady;
}

async function getSetting(key: string): Promise<string | null> {
  await ensureSchema();
  const r = await sqlite.execute({
    sql: "SELECT value FROM settings WHERE key = ?",
    args: [key],
  });
  return r.rows.length ? String(r.rows[0].value) : null;
}

async function setSetting(key: string, value: string): Promise<void> {
  await ensureSchema();
  await sqlite.execute({
    sql:
      "INSERT INTO settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
    args: [key, value],
  });
}

// ---------------------------------------------------------------- telegram

async function tg(method: string, payload: unknown): Promise<any> {
  const res = await fetch(`${API}/${method}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const body = await res.json();
  if (!body.ok) {
    throw new Error(
      `Telegram recusou ${method}: ${body.description ?? res.status}`,
    );
  }
  return body.result;
}

/** Resolve o destino: explícito, ou o chat padrão aprendido pelo webhook. */
async function resolveChat(chatId?: string | number): Promise<string> {
  if (chatId !== undefined && chatId !== null && `${chatId}`.trim() !== "") {
    return `${chatId}`;
  }
  const fromEnv = Deno.env.get("DEFAULT_CHAT_ID");
  if (fromEnv) return fromEnv;
  const stored = await getSetting("default_chat_id");
  if (stored) return stored;
  throw new Error(
    "Nenhum chat padrão definido ainda. Mande uma mensagem qualquer para o bot " +
      "no Telegram (isso registra o chat automaticamente), ou passe chat_id explicitamente.",
  );
}

// ---------------------------------------------------------------- tools

const TOOLS = [
  {
    name: "telegram_send_message",
    description:
      "Envia uma mensagem de texto no Telegram. Sem chat_id, envia para o chat padrão do usuário (ele mesmo).",
    inputSchema: {
      type: "object",
      properties: {
        text: { type: "string", description: "Texto da mensagem." },
        chat_id: {
          type: "string",
          description:
            "Destino. Omita para mandar ao usuário. Use @canal ou um id numérico para grupos/canais.",
        },
        parse_mode: {
          type: "string",
          enum: ["Markdown", "MarkdownV2", "HTML", "none"],
          description: "Formatação do texto. Padrão: Markdown.",
        },
        silent: {
          type: "boolean",
          description: "Envia sem tocar notificação no celular.",
        },
      },
      required: ["text"],
    },
  },
  {
    name: "telegram_send_file",
    description:
      "Envia um arquivo ou imagem no Telegram, por URL pública ou conteúdo em base64.",
    inputSchema: {
      type: "object",
      properties: {
        filename: { type: "string", description: "Nome do arquivo com extensão." },
        file_url: { type: "string", description: "URL pública do arquivo." },
        content_base64: {
          type: "string",
          description: "Conteúdo do arquivo em base64 (alternativa a file_url; até ~5 MB).",
        },
        caption: { type: "string", description: "Legenda opcional." },
        chat_id: { type: "string", description: "Destino. Omita para o chat padrão." },
        as_photo: {
          type: "boolean",
          description: "Envia como foto visível em vez de anexo. Só para imagens.",
        },
      },
      required: ["filename"],
    },
  },
  {
    name: "telegram_read_inbox",
    description:
      "Lê as mensagens que chegaram ao bot, mais recentes primeiro. Use para ver o que o usuário ou o grupo mandou.",
    inputSchema: {
      type: "object",
      properties: {
        limit: { type: "number", description: "Quantas mensagens trazer. Padrão 20, máximo 200." },
        chat_id: { type: "string", description: "Filtra por um chat específico." },
        since: {
          type: "string",
          description: "Só mensagens a partir desta data/hora UTC (ex.: 2026-09-11T12:00:00Z).",
        },
        unread_only: {
          type: "boolean",
          description: "Só o que chegou depois da última leitura marcada.",
        },
      },
    },
  },
  {
    name: "telegram_mark_read",
    description:
      "Marca a caixa de entrada como lida até agora, para que a próxima leitura com unread_only traga só o que for novo.",
    inputSchema: { type: "object", properties: {} },
  },
  {
    name: "telegram_list_chats",
    description:
      "Lista os chats que já falaram com o bot, com nome, tipo e id — útil para descobrir o id de um grupo.",
    inputSchema: { type: "object", properties: {} },
  },
  {
    name: "telegram_status",
    description:
      "Verifica a saúde da ligação: dados do bot, webhook registrado e qual é o chat padrão.",
    inputSchema: { type: "object", properties: {} },
  },
];

function b64ToBytes(b64: string): Uint8Array {
  const clean = b64.includes(",") ? b64.slice(b64.indexOf(",") + 1) : b64;
  const bin = atob(clean.replace(/\s/g, ""));
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

async function callTool(name: string, args: Record<string, any>): Promise<string> {
  switch (name) {
    case "telegram_send_message": {
      const chat = await resolveChat(args.chat_id);
      const payload: Record<string, unknown> = {
        chat_id: chat,
        text: args.text,
        disable_notification: !!args.silent,
      };
      if (args.parse_mode && args.parse_mode !== "none") {
        payload.parse_mode = args.parse_mode;
      } else if (!args.parse_mode) {
        payload.parse_mode = "Markdown";
      }
      let sent;
      try {
        sent = await tg("sendMessage", payload);
      } catch (err) {
        // Markdown malformado é o erro mais comum — reenvia como texto puro.
        if (payload.parse_mode && /parse/i.test(String(err))) {
          delete payload.parse_mode;
          sent = await tg("sendMessage", payload);
        } else throw err;
      }
      return `Mensagem enviada para ${chat} (id ${sent.message_id}).`;
    }

    case "telegram_send_file": {
      const chat = await resolveChat(args.chat_id);
      const method = args.as_photo ? "sendPhoto" : "sendDocument";
      const field = args.as_photo ? "photo" : "document";

      if (args.file_url) {
        const sent = await tg(method, {
          chat_id: chat,
          [field]: args.file_url,
          caption: args.caption,
        });
        return `Arquivo enviado para ${chat} (id ${sent.message_id}).`;
      }

      if (!args.content_base64) {
        throw new Error("Informe file_url ou content_base64.");
      }
      const bytes = b64ToBytes(args.content_base64);
      if (bytes.length > 5 * 1024 * 1024) {
        throw new Error(
          `Arquivo grande demais para enviar em base64 (${
            (bytes.length / 1048576).toFixed(1)
          } MB, limite 5 MB). Hospede o arquivo e use file_url.`,
        );
      }
      const form = new FormData();
      form.append("chat_id", chat);
      if (args.caption) form.append("caption", args.caption);
      form.append(field, new Blob([bytes]), args.filename);

      const res = await fetch(`${API}/${method}`, { method: "POST", body: form });
      const body = await res.json();
      if (!body.ok) throw new Error(`Telegram recusou ${method}: ${body.description}`);
      return `Arquivo "${args.filename}" enviado para ${chat} (id ${body.result.message_id}).`;
    }

    case "telegram_read_inbox": {
      await ensureSchema();
      const limit = Math.min(Math.max(Number(args.limit) || 20, 1), 200);
      const where: string[] = [];
      const params: any[] = [];
      if (args.chat_id) {
        where.push("chat_id = ?");
        params.push(`${args.chat_id}`);
      }
      if (args.since) {
        where.push("received_at >= ?");
        params.push(String(args.since).replace("T", " ").replace(/Z$/, ""));
      }
      if (args.unread_only) {
        const mark = await getSetting("last_read_at");
        if (mark) {
          where.push("received_at > ?");
          params.push(mark);
        }
      }
      const sql = `SELECT chat_id, chat_title, chat_type, from_name, text, has_media, received_at
                   FROM messages
                   ${where.length ? "WHERE " + where.join(" AND ") : ""}
                   ORDER BY id DESC LIMIT ?`;
      const r = await sqlite.execute({ sql, args: [...params, limit] });
      if (!r.rows.length) return "Nenhuma mensagem encontrada.";
      const lines = r.rows.map((m: any) => {
        const onde = m.chat_type === "private" ? "" : ` em ${m.chat_title ?? m.chat_id}`;
        const media = m.has_media ? " [com mídia]" : "";
        return `[${m.received_at} UTC] ${m.from_name}${onde}: ${m.text ?? "(sem texto)"}${media}`;
      });
      return lines.join("\n");
    }

    case "telegram_mark_read": {
      const now = new Date().toISOString().replace("T", " ").slice(0, 19);
      await setSetting("last_read_at", now);
      return `Caixa de entrada marcada como lida até ${now} UTC.`;
    }

    case "telegram_list_chats": {
      await ensureSchema();
      const r = await sqlite.execute(
        `SELECT chat_id, chat_type,
                MAX(chat_title)  AS title,
                COUNT(*)         AS total,
                MAX(received_at) AS ultima
         FROM messages GROUP BY chat_id, chat_type ORDER BY ultima DESC`,
      );
      if (!r.rows.length) {
        return "Nenhum chat registrado ainda. Mande uma mensagem para o bot para registrá-lo.";
      }
      const padrao = await resolveChat().catch(() => null);
      return r.rows
        .map((c: any) =>
          `${c.title ?? "(sem nome)"} — ${c.chat_type}, id ${c.chat_id}` +
          `${c.chat_id === padrao ? " (padrão)" : ""}` +
          ` — ${c.total} msg, última em ${c.ultima} UTC`
        )
        .join("\n");
    }

    case "telegram_status": {
      const me = await tg("getMe", {});
      const hook = await tg("getWebhookInfo", {});
      const padrao = await resolveChat().catch((e) => `não definido (${e.message})`);
      await ensureSchema();
      const c = await sqlite.execute("SELECT COUNT(*) AS n FROM messages");
      return [
        `Bot: @${me.username} (${me.first_name})`,
        `Webhook: ${hook.url || "não registrado"}`,
        hook.last_error_message ? `Último erro do webhook: ${hook.last_error_message}` : null,
        `Pendentes no Telegram: ${hook.pending_update_count ?? 0}`,
        `Chat padrão: ${padrao}`,
        `Mensagens guardadas: ${c.rows[0].n}`,
      ].filter(Boolean).join("\n");
    }

    default:
      throw new Error(`Ferramenta desconhecida: ${name}`);
  }
}

// ---------------------------------------------------------------- MCP

function rpcResult(id: unknown, result: unknown) {
  return Response.json({ jsonrpc: "2.0", id, result });
}

function rpcError(id: unknown, code: number, message: string) {
  return Response.json({ jsonrpc: "2.0", id, error: { code, message } });
}

async function handleMcp(req: Request): Promise<Response> {
  const auth = req.headers.get("authorization") ?? "";
  if (!BEARER || auth !== `Bearer ${BEARER}`) {
    return new Response("Não autorizado", { status: 401 });
  }

  let msg: any;
  try {
    msg = await req.json();
  } catch {
    return rpcError(null, -32700, "JSON inválido");
  }

  // Notificações não levam id e não esperam resposta.
  if (msg.id === undefined || msg.id === null) return new Response(null, { status: 202 });

  switch (msg.method) {
    case "initialize":
      return rpcResult(msg.id, {
        protocolVersion: PROTOCOL_VERSION,
        capabilities: { tools: { listChanged: false } },
        serverInfo: { name: "telegram", version: "1.0.0" },
      });

    case "ping":
      return rpcResult(msg.id, {});

    case "tools/list":
      return rpcResult(msg.id, { tools: TOOLS });

    case "tools/call": {
      const { name, arguments: args } = msg.params ?? {};
      try {
        const text = await callTool(name, args ?? {});
        return rpcResult(msg.id, { content: [{ type: "text", text }] });
      } catch (err) {
        return rpcResult(msg.id, {
          content: [{ type: "text", text: `Erro: ${(err as Error).message}` }],
          isError: true,
        });
      }
    }

    default:
      return rpcError(msg.id, -32601, `Método não suportado: ${msg.method}`);
  }
}

// ---------------------------------------------------------------- webhook

async function handleWebhook(req: Request): Promise<Response> {
  if (req.headers.get("x-telegram-bot-api-secret-token") !== WEBHOOK_SECRET) {
    return new Response("Não autorizado", { status: 401 });
  }
  const update = await req.json();
  const m = update.message ?? update.channel_post ?? update.edited_message;
  if (!m) return new Response("ok");

  await ensureSchema();
  const from = m.from
    ? [m.from.first_name, m.from.last_name].filter(Boolean).join(" ") ||
      m.from.username || `id ${m.from.id}`
    : "(canal)";
  const hasMedia = !!(m.photo || m.document || m.video || m.audio || m.voice || m.sticker);

  await sqlite.execute({
    sql: `INSERT OR IGNORE INTO messages
          (update_id, chat_id, chat_title, chat_type, from_name, text, has_media, sent_at)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
    args: [
      update.update_id,
      `${m.chat.id}`,
      m.chat.title ?? m.chat.first_name ?? null,
      m.chat.type,
      from,
      m.text ?? m.caption ?? null,
      hasMedia ? 1 : 0,
      new Date(m.date * 1000).toISOString(),
    ],
  });

  // A primeira conversa privada vira o chat padrão — é assim que o "manda pra mim" se configura sozinho.
  if (m.chat.type === "private" && !(await getSetting("default_chat_id"))) {
    await setSetting("default_chat_id", `${m.chat.id}`);
  }

  return new Response("ok");
}

// ---------------------------------------------------------------- entrada

let webhookRegistered = false;

export default async function (req: Request): Promise<Response> {
  const url = new URL(req.url);

  if (!TOKEN) return new Response("Falta a variável TELEGRAM_TOKEN.", { status: 500 });

  // Auto-registra o webhook na primeira requisição, apontando para esta própria val.
  if (!webhookRegistered) {
    webhookRegistered = true;
    tg("setWebhook", {
      url: `${url.origin}/webhook`,
      secret_token: WEBHOOK_SECRET,
      allowed_updates: ["message", "edited_message", "channel_post"],
    }).catch((e) => console.error("Falha ao registrar webhook:", e.message));
  }

  if (url.pathname === "/webhook" && req.method === "POST") return handleWebhook(req);
  if (url.pathname === "/mcp") {
    if (req.method !== "POST") return new Response("Use POST", { status: 405 });
    return handleMcp(req);
  }

  const configurado = !!BEARER;
  return new Response(
    `Telegram MCP\n\n` +
      `MCP:     ${url.origin}/mcp  ${configurado ? "(protegido)" : "⚠ falta MCP_BEARER"}\n` +
      `Webhook: ${url.origin}/webhook\n`,
    { headers: { "Content-Type": "text/plain; charset=utf-8" } },
  );
}
