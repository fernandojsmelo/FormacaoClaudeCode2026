"""
Automação de Resumo Diário de Compromissos
============================================

Fluxo:
    1. Busca os compromissos do dia no Google Calendar.
    2. Para cada compromisso, busca no Gmail e-mails cujo ASSUNTO
       corresponda ao nome/título da reunião.
    3. Baixa os anexos relevantes e salva no Google Drive, em uma
       pasta nomeada com a data do dia (ex: 27-08-2026).
    4. Gera um resumo final com os compromissos e os anexos organizados.

Regras de negócio definidas pelo usuário:
    - Relacionamento e-mail <-> compromisso: por ASSUNTO do e-mail.
    - Organização no Drive: uma pasta por dia (DD-MM-AAAA).
    - Disparo: manual, sob demanda (ex: "roda meu resumo diário"),
      sem agendamento automático.

Requisitos:
    pip install --break-system-packages google-api-python-client \
        google-auth google-auth-oauthlib

Autenticação:
    Este script assume que já existe um fluxo OAuth2 configurado
    (arquivo token.json / credentials.json) com os escopos:
        - https://www.googleapis.com/auth/calendar.readonly
        - https://www.googleapis.com/auth/gmail.readonly
        - https://www.googleapis.com/auth/drive.file
"""

from __future__ import annotations

import base64
import datetime as dt
import os
from dataclasses import dataclass, field
from typing import List, Optional

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io

SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/drive.file",
]

TOKEN_PATH = "token.json"


# --------------------------------------------------------------------------- #
# Modelos de dados
# --------------------------------------------------------------------------- #

@dataclass
class Compromisso:
    id: str
    titulo: str
    inicio: dt.datetime
    fim: dt.datetime
    participantes: List[str] = field(default_factory=list)


@dataclass
class Anexo:
    nome_arquivo: str
    conteudo: bytes
    mime_type: str
    email_assunto: str


# --------------------------------------------------------------------------- #
# Autenticação
# --------------------------------------------------------------------------- #

def carregar_credenciais() -> Credentials:
    """Carrega as credenciais OAuth2 já autorizadas (token.json)."""
    if not os.path.exists(TOKEN_PATH):
        raise FileNotFoundError(
            "token.json não encontrado. Rode o fluxo de autorização OAuth2 "
            "antes de usar este script."
        )
    return Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)


# --------------------------------------------------------------------------- #
# Etapa 1: Google Calendar — buscar compromissos do dia
# --------------------------------------------------------------------------- #

def buscar_compromissos_do_dia(
    creds: Credentials, data: Optional[dt.date] = None
) -> List[Compromisso]:
    """Retorna todos os compromissos do dia informado (padrão: hoje)."""
    data = data or dt.date.today()
    service = build("calendar", "v3", credentials=creds)

    inicio_dia = dt.datetime.combine(data, dt.time.min).isoformat() + "Z"
    fim_dia = dt.datetime.combine(data, dt.time.max).isoformat() + "Z"

    resultado = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=inicio_dia,
            timeMax=fim_dia,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    compromissos = []
    for evento in resultado.get("items", []):
        inicio = evento["start"].get("dateTime", evento["start"].get("date"))
        fim = evento["end"].get("dateTime", evento["end"].get("date"))
        participantes = [
            p.get("email") for p in evento.get("attendees", []) if p.get("email")
        ]
        compromissos.append(
            Compromisso(
                id=evento["id"],
                titulo=evento.get("summary", "(sem título)"),
                inicio=dt.datetime.fromisoformat(inicio),
                fim=dt.datetime.fromisoformat(fim),
                participantes=participantes,
            )
        )
    return compromissos


# --------------------------------------------------------------------------- #
# Etapa 2: Gmail — localizar e-mails cujo assunto bate com o compromisso
# --------------------------------------------------------------------------- #

def buscar_emails_por_assunto(creds: Credentials, titulo_reuniao: str) -> List[dict]:
    """Busca e-mails no Gmail cujo assunto contenha o título da reunião."""
    service = build("gmail", "v1", credentials=creds)
    query = f'subject:"{titulo_reuniao}" has:attachment'

    resultado = service.users().messages().list(userId="me", q=query).execute()
    mensagens = resultado.get("messages", [])

    detalhes = []
    for msg in mensagens:
        detalhe = (
            service.users().messages().get(userId="me", id=msg["id"]).execute()
        )
        detalhes.append(detalhe)
    return detalhes


def extrair_anexos(creds: Credentials, mensagem: dict) -> List[Anexo]:
    """Extrai os anexos de uma mensagem do Gmail."""
    service = build("gmail", "v1", credentials=creds)
    anexos = []

    assunto = next(
        (h["value"] for h in mensagem["payload"]["headers"] if h["name"] == "Subject"),
        "(sem assunto)",
    )

    partes = mensagem.get("payload", {}).get("parts", []) or []
    for parte in partes:
        if parte.get("filename") and parte.get("body", {}).get("attachmentId"):
            anexo_id = parte["body"]["attachmentId"]
            anexo_dados = (
                service.users()
                .messages()
                .attachments()
                .get(userId="me", messageId=mensagem["id"], id=anexo_id)
                .execute()
            )
            conteudo = base64.urlsafe_b64decode(anexo_dados["data"])
            anexos.append(
                Anexo(
                    nome_arquivo=parte["filename"],
                    conteudo=conteudo,
                    mime_type=parte.get("mimeType", "application/octet-stream"),
                    email_assunto=assunto,
                )
            )
    return anexos


# --------------------------------------------------------------------------- #
# Etapa 3: Google Drive — organizar anexos em pasta por dia
# --------------------------------------------------------------------------- #

def obter_ou_criar_pasta_do_dia(
    creds: Credentials, data: Optional[dt.date] = None
) -> str:
    """Obtém (ou cria) a pasta do Drive nomeada com a data (DD-MM-AAAA)."""
    data = data or dt.date.today()
    nome_pasta = data.strftime("%d-%m-%Y")
    service = build("drive", "v3", credentials=creds)

    query = (
        f"name = '{nome_pasta}' and mimeType = 'application/vnd.google-apps.folder' "
        "and trashed = false"
    )
    resultado = service.files().list(q=query, fields="files(id, name)").execute()
    pastas = resultado.get("files", [])

    if pastas:
        return pastas[0]["id"]

    metadata = {
        "name": nome_pasta,
        "mimeType": "application/vnd.google-apps.folder",
    }
    pasta = service.files().create(body=metadata, fields="id").execute()
    return pasta["id"]


def salvar_anexo_no_drive(creds: Credentials, pasta_id: str, anexo: Anexo) -> str:
    """Salva um anexo dentro da pasta do dia no Drive."""
    service = build("drive", "v3", credentials=creds)

    media = MediaIoBaseUpload(
        io.BytesIO(anexo.conteudo), mimetype=anexo.mime_type, resumable=True
    )
    metadata = {"name": anexo.nome_arquivo, "parents": [pasta_id]}

    arquivo = (
        service.files().create(body=metadata, media_body=media, fields="id").execute()
    )
    return arquivo["id"]


# --------------------------------------------------------------------------- #
# Etapa 4: Orquestração — gerar o resumo diário completo
# --------------------------------------------------------------------------- #

def rodar_resumo_diario(data: Optional[dt.date] = None) -> str:
    """Executa o fluxo completo e retorna um resumo em texto."""
    creds = carregar_credenciais()
    data = data or dt.date.today()

    compromissos = buscar_compromissos_do_dia(creds, data)
    if not compromissos:
        return f"Nenhum compromisso encontrado para {data.strftime('%d/%m/%Y')}."

    pasta_id = obter_ou_criar_pasta_do_dia(creds, data)

    linhas_resumo = [f"Resumo de {data.strftime('%d/%m/%Y')}:\n"]

    for compromisso in compromissos:
        linhas_resumo.append(
            f"- {compromisso.inicio.strftime('%H:%M')} | {compromisso.titulo}"
        )

        emails = buscar_emails_por_assunto(creds, compromisso.titulo)
        total_anexos = 0

        for email in emails:
            anexos = extrair_anexos(creds, email)
            for anexo in anexos:
                salvar_anexo_no_drive(creds, pasta_id, anexo)
                total_anexos += 1

        if total_anexos:
            linhas_resumo.append(
                f"    -> {total_anexos} anexo(s) salvo(s) na pasta do dia no Drive."
            )
        else:
            linhas_resumo.append("    -> Nenhum e-mail/anexo relacionado encontrado.")

    return "\n".join(linhas_resumo)


if __name__ == "__main__":
    print(rodar_resumo_diario())