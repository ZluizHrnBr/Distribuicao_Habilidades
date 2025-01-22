import random
import csv
# Definição de habilidades dos desenvolvedores (nome: [habilidades])
desenvolvedores = {f'Aluno{i}': [] for i in range(0, 110)}

habilidades = [
    "DS",
    "DW",
    "DM",
    "DSL",
    "INF1",
    "INF2",
    "GP",
    "AS",
    "DB",
    "DT",
    "TS",
    "DF"
]
def distribuir_habilidades_V_2(desenvolvedores, habilidades):
    matriz_habilidades = {}

    for aluno in desenvolvedores.keys():
        habilidades_aluno = [0] * len(habilidades)  # Inicializa todas as habilidades com 0
        habilidade_selecionada = random.randint(0, len(habilidades) - 1)  # Escolhendo 1 habilidade de modo aleatória
        habilidades_aluno[habilidade_selecionada] = random.randint(1, 3)  # Atribui um nível entre 1 e 3 para a habilidade escolhida

        matriz_habilidades[aluno] = habilidades_aluno  # Adiciona o aluno e suas habilidades ao dicionário

    return matriz_habilidades

matriz = distribuir_habilidades_V_2(desenvolvedores, habilidades)

print("Matriz de Habilidades dos Alunos:")
print("Aluno\t\t", "\t".join(habilidades))

for aluno, linha in matriz.items():
    print(f"{aluno}\t\t", "\t".join(map(str, linha)))


nome_arquivo = "matriz_habilidades.csv"
with open(nome_arquivo, mode="w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    # Escreve o cabeçalho com o nome das habilidades
    escritor.writerow(["Aluno"] + habilidades)
    # Escreve cada aluno e suas habilidades
    for aluno, linha in matriz.items():
        escritor.writerow([aluno] + linha)

print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")