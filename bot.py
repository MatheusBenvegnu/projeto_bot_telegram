# Bot Telegram para Atendimento Virtual - Data Max Solutions

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Configuração de logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# --- Constantes --- (Informações da Empresa e Serviços)
TOKEN = "7890837569:AAHivzo3jWx9H3B4_2FRtgpFw9-x1K63fdo"  # Token fornecido pelo usuário

NOME_EMPRESA = "Data Max Solutions"

INFO_EMPRESA = f"""
*{NOME_EMPRESA}*

Somos uma empresa de soluções em TI criada por um grupo de estudantes da UNINOVE:

- Matheus Benvegnu (RA: 923202062)
- Davi Lopes Delfino (RA: 924113462)
- Yuri Silva de Souza (RA: 923108998)
- Adriano Figueiredo da Silva (RA: 924202099)
- Hugo luis da silva santos (RA: 925105927)
- Samuel Falcão Roque (RA: 925101757)
- Geovanna Gomes Lopes Folha (RA: 924103737)

Nosso objetivo é oferecer soluções inovadoras e suporte de qualidade.
"""

SERVICOS = {
    "dev_sistemas": "Desenvolvimento de Sistemas",
    "suporte_tecnico": "Suporte Técnico",
    "consultoria_ti": "Consultoria em TI"
}

MENSAGEM_FEEDBACK = "Sua opinião é muito importante para nós! Fique à vontade para nos enviar suas sugestões ou reclamações respondendo a esta mensagem ou entrando em contato pelos nossos canais."

MENSAGEM_AGENDAMENTO = "Ótima escolha! Para agendar uma reunião e discutir suas necessidades, por favor, entre em contato conosco diretamente. Em breve, teremos um sistema de agendamento automático."

# --- Handlers --- 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia a mensagem de boas-vindas com o menu principal."""
    user = update.effective_user
    logger.info(f"Usuário {user.first_name} ({user.id}) iniciou o bot.")

    keyboard = [
        [InlineKeyboardButton("1) Sobre a empresa", callback_data="sobre_empresa")],
        [InlineKeyboardButton("2) Nossos serviços", callback_data="nossos_servicos")],
        [InlineKeyboardButton("3) Dar um feedback", callback_data="dar_feedback")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Escapar caracteres especiais para MarkdownV2
    nome_empresa_escaped = NOME_EMPRESA.replace("-", "\\-").replace(".", "\\.")
    user_mention = user.mention_markdown_v2()

    # CORRIGIDO: Escapar o '!' na mensagem
    await update.message.reply_text(
        f"Olá, {user_mention}\! Seja bem\-vindo ao atendimento virtual da {nome_empresa_escaped}\ Selecione uma opção para ser atendido:",
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Processa os cliques nos botões do menu."""
    query = update.callback_query
    await query.answer()  # Responde ao callback para remover o "loading" no botão

    data = query.data
    logger.info(f"Callback recebido: {data}")

    if data == "sobre_empresa":
        # Usar Markdown simples aqui para INFO_EMPRESA que já tem formatação
        await query.edit_message_text(text=INFO_EMPRESA, parse_mode='Markdown') 
        # Adicionar botão para voltar ao menu principal
        keyboard = [[InlineKeyboardButton("<< Voltar ao Menu", callback_data="menu_principal")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_reply_markup(reply_markup=reply_markup)

    elif data == "nossos_servicos":
        keyboard = [
            [InlineKeyboardButton(f"1) {SERVICOS['dev_sistemas']}", callback_data="servico_dev_sistemas")],
            [InlineKeyboardButton(f"2) {SERVICOS['suporte_tecnico']}", callback_data="servico_suporte_tecnico")],
            [InlineKeyboardButton(f"3) {SERVICOS['consultoria_ti']}", callback_data="servico_consultoria_ti")],
            [InlineKeyboardButton("<< Voltar ao Menu", callback_data="menu_principal")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Corrigido para usar MarkdownV2 e escapar caracteres
        await query.edit_message_text(text="*Nossos Serviços*:\n\nSelecione uma opção para saber mais e agendar uma conversa:", reply_markup=reply_markup, parse_mode='MarkdownV2')

    elif data.startswith("servico_"):
        # Simplesmente envia a mensagem de agendamento para qualquer serviço selecionado
        await query.edit_message_text(text=MENSAGEM_AGENDAMENTO)
        # Adicionar botão para voltar ao menu principal
        keyboard = [[InlineKeyboardButton("<< Voltar ao Menu", callback_data="menu_principal")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_reply_markup(reply_markup=reply_markup)

    elif data == "dar_feedback":
        await query.edit_message_text(text=MENSAGEM_FEEDBACK)
        # Adicionar botão para voltar ao menu principal
        keyboard = [[InlineKeyboardButton("<< Voltar ao Menu", callback_data="menu_principal")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_reply_markup(reply_markup=reply_markup)

    elif data == "menu_principal":
        # Recria o menu principal como na função start, mas editando a mensagem
        keyboard = [
            [InlineKeyboardButton("1) Sobre a empresa", callback_data="sobre_empresa")],
            [InlineKeyboardButton("2) Nossos serviços", callback_data="nossos_servicos")],
            [InlineKeyboardButton("3) Dar um feedback", callback_data="dar_feedback")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Precisa escapar caracteres especiais para MarkdownV2
        nome_empresa_escaped = NOME_EMPRESA.replace("-", "\\-").replace(".", "\\.") # Exemplo simples
        # CORRIGIDO: Indentação e parse_mode
        await query.edit_message_text(
            text=f"Seja bem\\-vindo novamente ao atendimento virtual da {nome_empresa_escaped}\\.\nSelecione uma opção para ser atendido:",
            reply_markup=reply_markup,
            parse_mode='MarkdownV2' # Corrigido para aspas simples normais
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Loga os erros causados pelos Updates."""
    logger.error("Exception while handling an update:", exc_info=context.error)


def main() -> None:
    """Inicia o bot."""
    # Verifica se o token foi substituído (embora já esteja inserido)
    if TOKEN == "SEU_TOKEN_AQUI":
        logger.error("ERRO: Token do bot não configurado. Edite o arquivo bot.py e substitua 'SEU_TOKEN_AQUI' pelo seu token.")
        return

    # Cria a Application e passa o token do bot.
    application = Application.builder().token(TOKEN).build()

    # Registra os handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))

    # Registra o error handler
    application.add_error_handler(error_handler)

    # Inicia o Bot
    logger.info("Iniciando o bot...")
    application.run_polling()

if __name__ == "__main__":
    main()

