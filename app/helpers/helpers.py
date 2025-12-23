from datetime import time, timedelta
from math import floor

def formata_tempo_estimado_para_segundos(tempo_estimado):
    t = time.fromisoformat(tempo_estimado)
    tempo_estimado_time = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    total_segundos = int(tempo_estimado_time.total_seconds())
    return total_segundos

def formata_tempo_estimado_para_formato_iso(tempo_estimado):
    segundos = int(tempo_estimado)
    horas = floor(segundos / 3600)
    minutos = floor((segundos % 3600) / 60)
    tempo_estimado_formatado = f"{horas:02d}:{minutos:02d}"

    return tempo_estimado_formatado