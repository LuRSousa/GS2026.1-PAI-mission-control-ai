import json
import random
from pathlib import Path

def carregar_configuracao_cenarios():
    """Lê de forma segura o arquivo JSON de cenários na pasta data."""
    caminho = Path("data/cenarios.json")
    if not caminho.exists():
        # Fallback de segurança caso o arquivo suma ou mude de lugar
        raise FileNotFoundError("Arquivo data/cenarios.json não foi encontrado.")
        
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def coletar(cenario="nominal"):
    """
    Consome o arquivo data/cenarios.json para simular e retornar 
    os 5 parâmetros operacionais do EnviroSat.
    """
    try:
        cenarios = carregar_configuracao_cenarios()
        
        # Se o cenário solicitado não existir no JSON, força o uso do 'nominal'
        if cenario not in cenarios:
            cenario = "nominal"
            
        config = cenarios[cenario]
        
        # Processa os limites numéricos do JSON aplicando o dinamismo do random
        termico = round(random.uniform(config["sensor_termico"]["min"], config["sensor_termico"]["max"]), 1)
        buffer = round(random.uniform(config["buffer_imagens"]["min"], config["buffer_imagens"]["max"]), 1)
        geolocalizacao = round(random.uniform(config["precisao_geolocalizacao"]["min"], config["precisao_geolocalizacao"]["max"]), 1)
        energia = round(random.uniform(config["energia_disponivel"]["min"], config["energia_disponivel"]["max"]), 1)
        
        # Como o sensor óptico no JSON é uma lista de strings, escolhemos uma delas aleatoriamente
        optico = random.choice(config["sensor_optico"])
        
        return {
            "sensor_termico": termico,
            "sensor_optico": optico,
            "buffer_imagens": buffer,
            "precisao_geolocalizacao": geolocalizacao,
            "energia_disponivel": energia
        }
        
    except Exception as e:
        # Em caso de falha crítica na leitura do JSON, retorna um estado seguro padrão
        return {
            "sensor_termico": 25.0,
            "sensor_optico": "RGB+NIR Nominal (Modo de Segurança)",
            "buffer_imagens": 0.0,
            "precisao_geolocalizacao": 5.0,
            "energia_disponivel": 100.0,
            "erro_leitura": str(e)
        }