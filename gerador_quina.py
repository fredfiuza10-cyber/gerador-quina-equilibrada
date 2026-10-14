import random
from collections import Counter
import ast

# ==============================
# CONFIGURAÇÕES
# ==============================
ARQUIVO_HISTORICO = "quina_historico.txt"
NUMEROS_QUINA = list(range(1, 81))


# ==============================
# LEITURA DO HISTÓRICO (ROBUSTA)
# ==============================
def ler_historico():
    historico = []

    with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()

            if not linha:
                continue

            try:
                # Converte string "[08, 54, ...]" em lista real
                jogo = ast.literal_eval(linha)

                # Garante que são inteiros válidos
                if (
                    isinstance(jogo, list)
                    and len(jogo) == 5
                    and all(isinstance(n, int) for n in jogo)
                ):
                    historico.append(sorted(jogo))

            except Exception:
                # ignora linhas mal formatadas
                continue

    return historico


# ==============================
# ANÁLISE DO HISTÓRICO (CONSULTA)
# ==============================
def analisar_historico(historico):
    freq = Counter(n for jogo in historico for n in jogo)
    media = sum(freq.values()) / len(freq)
    return freq, media


# ==============================
# GERAÇÃO DE JOGO EQUILIBRADO
# ==============================
def gerar_jogo_equilibrado():
    while True:
        jogo = sorted(random.sample(NUMEROS_QUINA, 5))

        pares = sum(1 for n in jogo if n % 2 == 0)
        baixos = sum(1 for n in jogo if n <= 40)

        # filtros neutros (não reduzem probabilidade)
        if 2 <= pares <= 3 and 2 <= baixos <= 3:
            return jogo


# ==============================
# EXECUÇÃO
# ==============================
if __name__ == "__main__":
    historico = ler_historico()

    if not historico:
        raise ValueError("Histórico vazio ou mal formatado.")

    freq, media = analisar_historico(historico)
    jogo = gerar_jogo_equilibrado()

    print("JOGO GERADO:", jogo)

    # Diagnóstico informativo (não influencia o jogo)
    print("\nDiagnóstico do jogo:")
    print("Pares:", sum(n % 2 == 0 for n in jogo))
    print("Ímpares:", sum(n % 2 != 0 for n in jogo))
    print("Baixos (1–40):", sum(n <= 40 for n in jogo))
    print("Altos (41–80):", sum(n > 40 for n in jogo))
