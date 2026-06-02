"""Mission Control AI — Módulo de alertas."""

def avaliar(dados_telemetria):
    """
    Analisa os dados numéricos da telemetria e gera uma lista de strings de alertas.
    """
    alertas = []
    
    # Validação do Sensor Térmico
    termico = dados_telemetria.get("sensor_termico", 25.0)
    if termico >= 300.0:
        alertas.append(f"🚨 [CRÍTICO] Anomalia Térmica Extrema detetada: {termico}°C. Forte indício de incêndio florestal de grandes proporções em solo.")
    elif termico >= 50.0:
        alertas.append(f"⚠️ [AVISO] Temperatura de brilho elevada: {termico}°C. Monitorar possível início de queima ou solo exposto severo.")

    # Validação do Sensor Óptico
    optico = dados_telemetria.get("sensor_optico", "")
    if "Obstruído por Nuvens" in optico or "Obstrução Total" in optico:
        alertas.append("⚠️ [COMPLIANCE] Visibilidade Óptica Comprometida por Nuvens. Risco de 'ponto cego' climático para fiscalização de desmatamento.")
    elif "Anomalia Óptica" in optico:
        alertas.append("🚨 [CRÍTICO] Confirmação visual de pluma de fumo / degradação severa do índice de reflectância da vegetação (NIR).")
    elif "Modo de Economia" in optico:
        alertas.append("⚠️ [SISTEMA] Sensor Óptico operando com taxa de amostragem reduzida por restrições energéticas.")

    # Validação do Buffer de Imagens
    buffer_perc = dados_telemetria.get("buffer_imagens", 0.0)
    if buffer_perc >= 90.0:
        alertas.append(f"🚨 [CRÍTICO] Saturação do Buffer de Bordo: {buffer_perc}%. Risco iminente de perda de imagens orbitais por falta de espaço de armazenamento.")
    elif buffer_perc >= 70.0:
        alertas.append(f"⚠️ [AVISO] Retenção elevada no Buffer: {buffer_perc}%. Latência na transmissão (downlink) com as estações terrestres de recepção.")

    # Validação da Precisão de Geolocalização
    precisao = dados_telemetria.get("precisao_geolocalizacao", 5.0)
    if precisao >= 100.0:
        alertas.append(f"🚨 [CRÍTICO] Degradação severa de Geolocalização: Erro de {precisao}m. Invalida a precisão jurídica de laudos de desmatamento ilegal e dificulta o resgate em campo.")
    elif precisao >= 30.0:
        alertas.append(f"⚠️ [AVISO] Perda parcial de precisão de atitude: Erro de {precisao}m. Coordenadas fora do padrão nominal.")

    # Validação de Energia Disponível
    energia = dados_telemetria.get("energia_disponivel", 100.0)
    if energia <= 35.0:
        alertas.append(f"🚨 [CRÍTICO] Subsistema de Energia Crítico: {energia}%. Subsistemas científicos correm risco de desligamento automático para preservação do barramento principal.")
    elif energia <= 60.0:
        alertas.append(f"⚠️ [AVISO] Balanço energético negativo: {energia}%. Satélite operando sob regime de eclipse ou baixa eficiência dos painéis solares.")

    return alertas