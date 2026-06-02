"""Mission Control AI — Customizando interface CLI estilo Claude Code."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import pyfiglet
from datetime import datetime

console = Console()
session = PromptSession(style=Style.from_dict({"prompt": "fg:#06B6D4 bold"}))

def show_banner():
    """Exibe banner ASCII colorido no início."""
    banner = pyfiglet.figlet_format("Mission Control", font="ansi_shadow")
    console.print(Text(banner, style="bold #06B6D4"))
    console.print(Panel.fit(
        "Sistema de monitoramento e análise por IA generativa.\n"
        "Use /help para ver os comandos · /exit para sair.\n"
        "Modelo: gpt-oss:120b via Ollama Cloud",
        title="MISSION CONTROL", border_style="#06B6D4"
    ))

def show_response(text):
    """Renderiza resposta da IA em painel com timestamp."""
    now = datetime.now().strftime("%H:%M")
    console.print(Panel(text, title="Mission Control",
        subtitle=now, border_style="#06B6D4"))
    
def run_cli(engine):
    """Loop principal da CLI."""
    show_banner()
    if not engine.is_ready():
        console.print("Engine status: AGUARDANDO IMPLEMENTAÇÃO ✗\n",
            style="yellow")
    while True:
        try:
            user_input = session.prompt([("class:prompt", "❯ ")]).strip()
        except (KeyboardInterrupt, EOFError):
            break
        if not user_input:
            continue

        #Sair do sistema
        if user_input == "/exit":
            break

        #Abre o menu de ajuda
        if user_input == "/help":
            console.print("Comandos: /help /status /about /clear /exit")
            console.print("[bold yellow]Comandos de Simulação:[/] /cenario (nominal | incendio | falha_transmissao | crise_energia)")
            continue

        #Mostra o status atual
        if user_input == "/status":
            show_response(engine.status_snapshot())
            continue

        #TESTES: altera o cenário para testes
        CENARIOS_VALIDOS = {"nominal", "incendio", "falha_transmissao", "crise_energia"}

        if user_input.startswith("/cenario "):
            partes = user_input.split(" ", 1)
            novo_cenario = partes[1].strip().lower() if len(partes) > 1 else ""
            
            if novo_cenario not in CENARIOS_VALIDOS:
                console.print(
                    f"[bold #F43F5E]✕ Erro:[/] Cenário '[yellow]{novo_cenario}[/]' inválido.\n"
                    f"[dim]Opções disponíveis: {', '.join(sorted(CENARIOS_VALIDOS))}[/]"
                )
            else:
                engine.mudar_cenario(novo_cenario)
                console.print(f"[bold #10B981]✓[/] Simulador orbital alternado para o cenário: [bold #A855F7]{novo_cenario}[/]")
            continue

        #Mostra mensagem fixa sobre o projeto
        if user_input == "/about":
            about_text = (
                "[bold #A855F7]MISSION CONTROL AI — ENVIROSAT[/]\n\n"
                "Sistema especialista de monitoramento orbital desenvolvido para a "
                "Global Solution 2026.1 na FIAP (Curso de Ciência da Computação).\n\n"
                "[bold]Propósito:[/] Cruzar dados de telemetria de microssatélites com inteligência "
                "generativa para antecipar desastres ecológicos, monitorar a saúde de biomas e "
                "garantir a conformidade legal (compliance) ambiental em solo terrestre.\n\n"
                "[bold]Tecnologias:[/] Python 3, Rich, Prompt-Toolkit e gpt-oss:120b via Ollama Cloud."
            )
            console.print(Panel(about_text, title="Sobre a Missão", border_style="#A855F7"))
            continue
        if user_input == "/clear":
            console.clear(); show_banner(); continue
        # Qualquer outra entrada vai para o motor de análise
        resposta = engine.analyze(user_input)
        show_response(resposta)