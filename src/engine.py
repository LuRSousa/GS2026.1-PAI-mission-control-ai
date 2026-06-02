"""Mission Control AI — Motor de análise da missão."""

import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path

from src import telemetria
from src import alertas

load_dotenv()

# Identificação da trilha
TRILHA = "envirosat"

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY', '')}
)

def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia prompt ao gpt-oss:120b via Ollama Cloud."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    try:
        return client.chat(
            model="gpt-oss:120b", messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
        )['message']['content'].strip()
    except Exception as e:
        return f"Erro ao consultar IA: {e}"
    
def load_system_prompt():
    """Lê o system prompt do arquivo prompts/system_prompt.md"""
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Você é um assistente de observação ambiental orbital." # fallback genérico

class MissionEngine:
    """Motor de análise"""

    def __init__ (self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()
        self.cenario_atual = "nominal"
    
    def is_ready(self):
        # Troquem para True quando analyze() estiver implementado
        return True
    
    def mudar_cenario(self, novo_cenario):
        """Permite alternar o estado do satélite dinamicamente para testes."""
        self.cenario_atual = novo_cenario
    
    def status_snapshot(self):
        """Retorna um sumário estruturado e puramente técnico da telemetria atual."""
        dados = telemetria.coletar(self.cenario_atual)
        lista_alertas = alertas.avaliar(dados)
        
        status_texto = (
            f"[bold #06B6D4]STATUS ATUAL DO SATÉLITE (Cenário: {self.cenario_atual.upper()})[/]\n"
            f"  Sensor Térmico: {dados['sensor_termico']}°C\n"
            f"  Sensor Óptico: {dados['sensor_optico']}\n"
            f"  Buffer de Imagens: {dados['buffer_imagens']}%\n"
            f"  Precisão Geográfica: Erro de {dados['precisao_geolocalizacao']}m\n"
            f"  Subsistema de Energia: {dados['energia_disponivel']}%\n\n"
        )
        
        if lista_alertas:
            status_texto += "[bold yellow]Alertas Ativos do Sistema (Python Core):[/]\n"
            for alerta in lista_alertas:
                status_texto += f"  {alerta}\n"
        else:
            status_texto += "[bold green]Todos os subsistemas operando em limites nominais.[/]\n"
            
        return status_texto
    
    def _detectar_persona(self, pergunta_usuario):
        """
        Método privado responsável estritamente pelo roteamento 
        dinâmico de personas com base no cenário e intenção.
        """
        pergunta_clean = pergunta_usuario.lower()
        
        if self.cenario_atual == "incendio" or any(w in pergunta_clean for w in ["fogo", "queima", "incêndio"]):
            return (
                "Coordenador de Brigada / Equipes de Resposta em Solo",
                "Foque em ações imediatas de contenção, riscos à vida, fauna e emissão de carbono."
            )
        
        if self.cenario_atual in ["falha_transmissao", "crise_energia"] or any(w in pergunta_clean for w in ["laudo", "legal", "multa", "juridico"]):
            return (
                "Analista de Compliance / Fiscalização Ambiental (IBAMA / Órgãos Jurídicos)",
                "Foque na validade jurídica das provas, brechas para desmatamento ilegal e penalidades administrativas."
            )
            
        return (
            "Operador do Centro de Controle Técnico (INPE / Engenharia Orbital)",
            "Foque na saúde do satélite, estabilidade dos subsistemas e calibração de sensores."
        )

    def analyze(self, pergunta_usuario):
        """
        Interpreta dados e orquestra a geração do laudo pela IA.
        """
        # Coleta e validação (Python Core)
        dados = telemetria.coletar(self.cenario_atual)
        lista_alertas = alertas.avaliar(dados)
        
        # Resolução da persona delegada ao método especializado
        persona_alvo, diretriz_foco = self._detectar_persona(pergunta_usuario)
        
        # Montagem do Contexto Enriquecido
        alertas_formatados = "\n".join(lista_alertas) if lista_alertas else "Nenhuma anomalia detectada pelo Python Core."
        
        prompt_contextualizado = (
            f"CONTEXTO OPERACIONAL DO SATÉLITE ENVIROSAT:\n"
            f"--- TELEMETRIA BRUTA ---\n"
            f"- Sensor Térmico: {dados['sensor_termico']}°C\n"
            f"- Sensor Óptico: {dados['sensor_optico']}\n"
            f"- Ocupação do Buffer: {dados['buffer_imagens']}%\n"
            f"- Margem de Erro de Geolocalização: {dados['precisao_geolocalizacao']} metros\n"
            f"- Carga de Energia Disponível: {dados['energia_disponivel']}%\n\n"
            f"--- DIAGNÓSTICO DE ALERTAS (PYTHON) ---\n"
            f"{alertas_formatados}\n\n"
            f"--- DIRETRIZ DE PERFIL REQUISITADA ---\n"
            f"Você deve responder este laudo sob a perspectiva do: {persona_alvo}.\n"
            f"Diretriz analítica: {diretriz_foco}\n\n"
            f"--- SOLICITAÇÃO DO USUÁRIO ---\n"
            f"\"{pergunta_usuario}\"\n\n"
            f"Gere o laudo estruturado aplicando rigorosamente a persona designada e as regras de amarração socioambiental."
        )
        
        # Execução da inferência via LLM
        return llm(prompt_contextualizado, system=self.system_prompt)