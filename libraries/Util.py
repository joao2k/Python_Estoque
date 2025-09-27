import os
from datetime import datetime
def registrar_erro(erro):
    # 1️⃣ cria pasta log se não existir
    pasta_log = "log"
    if not os.path.exists(pasta_log):
        os.makedirs(pasta_log)

    # 2️⃣ cria nome do arquivo com a data atual
    data_hoje = datetime.now().strftime("%d_%m_%Y")
    arquivo_log = os.path.join(pasta_log, f"LOG_{data_hoje}.txt")

    # 3️⃣ escreve no arquivo
    hora_atual = datetime.now().strftime("%H:%M:%S")
    with open(arquivo_log, "a", encoding="utf-8") as f:
        f.write(f"[{hora_atual}] {str(erro)}\n")