# Mission Control AI — [Missão EnviroSat]

---

## Integrantes

| Nome | RM | Turma |
|------|----|-------|
| Enzo Caruso Peter | RM570908 | 1CCPG |
| Leonardo Robert Maulicino | RM570329 | 1CCPG |
| Lucas Ramos de Sousa | RM573901 | 1CCPG |

---

## Sobre a Missão EnviroSat

O **EnviroSat** é um sistema especialista de monitoramento orbital desenvolvido para mitigar desastres ecológicos e garantir o compliance ambiental em biomas terrestres através do cruzamento de dados de telemetria de microssatélites. 

A inteligência artificial, alimentada pelo modelo **gpt-oss:120b**, está integrada diretamente ao core da aplicação via **Ollama Cloud**, atuando como um motor analítico que interpreta os diagnósticos gerados em Python para chavear dinamicamente entre personas e emitir laudos técnicos estruturados. 

Desse modo, o ecossistema une a precisão da validação lógica estrita no back-end à flexibilidade narrativa da IA generativa para gerar análises de causa e efeito socioambiental em tempo real.

---

## Personas Atendidas
- **Operador do Centro de Controle (INPE / Órgão Estadual):** Esta persona precisa de um diagnóstico imediato sobre a saúde e calibração dos subsistemas do satélite para garantir a estabilidade operacional da missão e a integridade da coleta de dados brutos. O sistema o atende fornecendo análises em tempo real que traduzem oscilações térmicas e energéticas em ações preventivas na engenharia orbital.

- **Coordenador de Brigada de Combate a Incêndio:** Focado em ações táticas imediatas de contenção e mitigação de riscos em solo, este perfil necessita de dados precisos e contextualizados sobre a gravidade dos incêndios e as frentes de fogo ativas. O sistema traduz a telemetria em relatórios de impacto imediato à fauna e à segurança das equipes florestais, otimizando o envio de brigadistas.
  
- **Analista de Compliance Ambiental:** Esta persona atua na esfera regulatória, precisando auditar brechas de monitoramento e validar a precisão geográfica dos dados para garantir que os laudos técnicos tenham força legal contra o desmatamento clandestino. O sistema o apoia correlacionando falhas de transmissão e imprecisões métricas aos riscos jurídicos e administrativas de omissão de provas.

---

## Tecnologias Utilizadas

- Python 3.10+
- Ollama Cloud API (modelo gpt-oss:120b)
- Bibliotecas: ollama (0.6.2), python-dotenv (1.2.2), rich (15.0.0), prompt_toolkit (3.0.52), pyfiglet (1.0.4)

---

## Como Executar

### 1. Clone o repositório:
Abra o terminal do seu dispositivo e cole o comando abaixo:
```bash
git clone https://github.com/LuRSousa/GS2026.1-PAI-mission-control-ai
```

### 2. Crie o ambiente virtual:
Com o repositório aberto, novamente no terminal, cole o comando abaixo:
```bash
python -m venv .venv & source .venv/bin/activate
```

### 3. Instale dependências:
Com o repositório aberto, novamente no terminal, cole o comando abaixo:
```bash
pip install -r requirements.txt
```

### 4. Crie o arquivo '.env' na raíz:
Abra o arquivo e insira o código abaixo:
```bash
OLLAMA_API_KEY=sua_chave_aqui
```
> O arquivo `.env` já está no `.gitignore` — nunca suba sua chave para o repositório.


### 5. Execute o programa:
Novamente no terminal, cole o comando abaixo:
```bash
python main.py
```

---

## Demonstração



---

## System Prompt

Visualize o system prompt utilizado para configurar a IA do sistema: [prompts/system_prompt.md](prompts/system_prompt.md)

---

## Cenários de Teste Demonstrados

- **Nominal:** Operação nominal — todos os parâmetros dentro do range seguro e subsistemas operando de forma estável.
- **Incêndio:** Temperatura crítica — sensor térmico acima do limiar de ignição + análise e laudo socioambiental da IA.
- **Falha na Transmissão:** Saturação do buffer — retenção crítica de dados por falha de downlink + resposta automatizada de segurança.
- **Crise de Energia:** Regressão energética — subsistema de energia crítico + degradação de atitude e perda de precisão geográfica.

---

## Limitações Conhecidas
Como este ecossistema foi desenvolvido como um protótipo focado na validação de arquitetura e integração de Inteligência Artificial para a Global Solution, ele possui as seguintes limitações de escopo projetadas:

- **Simulação de Telemetria Estática/Baseada em JSON:** O sistema não está conectado a um satélite físico ou a uma API de fluxo de dados (data stream) em tempo real. As anomalias e leituras operacionais são geradas de forma determinística ou semi-aleatória a partir de faixas pré-configuradas no arquivo [data/cenarios.json](data/cenarios.json).

- **Dependência de Conectividade com a Nuvem (Ollama Cloud):** Toda a inteligência analítica e o chaveamento dinâmico de personas dependem de uma conexão ativa com a internet para consumir o modelo gpt-oss:120b. O sistema não possui capacidade de processamento de linguagem natural offline local (Edge AI), o que geraria falhas de inferência em cenários reais de isolamento em solo terrestre.

- **Janela de Contexto Volátil (Stateless CLI):** A CLI opera no formato de requisição e resposta sem persistência de memória histórica longa entre comandos consecutivos. O modelo analisa o "snapshot" daquele instante enviado pelo Python Core, o que impede análises preditivas profundas baseadas em séries temporais complexas ou histórico de órbitas passadas diretamente no prompt.

- **Precisão Métrica Simulada:** Os alertas de geolocalização e as amarrações jurídicas de compliance são inferências lógicas baseadas nas strings do contexto. O sistema não processa arquivos georreferenciados reais (como Shapefiles, GeoJSON ou imagens de satélite raster TIFF) nem possui integração com Sistemas de Informação Geográfica (SIG).

---

## Vídeo de Demonstração
[Assistir no YouTube]()














