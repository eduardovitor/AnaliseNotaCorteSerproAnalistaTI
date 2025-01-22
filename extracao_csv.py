import re
import glob
import csv

# Dados extraídos do link: https://www.transparencia.serpro.gov.br/acesso-a-informacao/servidores/concurso-publico/concurso-publico-2023/ed_9_serpro_res_fin_concurso.pdf

# Primeiras 361 notas, que correspondem à ampla concorrência
HEADERS = ["Nota/AC"]

dados = []
dados.insert(0,HEADERS)
nome_dataset = "dataset_ac_serpro.csv"

for arquivo in glob.glob("data/*.txt"):
    with open(arquivo, "r") as f:
        conteudo = f.read()
        notas = re.findall(r'\d+\.\d{2}',conteudo)
        for nota in notas:
            dados.append([nota])

with open(nome_dataset, "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(dados)
