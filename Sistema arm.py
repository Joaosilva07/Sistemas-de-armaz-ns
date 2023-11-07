import random
import os
import pandas as pd
import matplotlib.pyplot as plt


class Armazem:
    def __init__(self, tipo):
        if tipo < 1 or tipo > 100:
            raise ValueError("O tipo deve estar entre 1 e 100")
        self.tipo = tipo
        self.quantidade = []
        self.precos = []
        self.vendas = []

    def gerar_dados_aleatorios(self):
        self.quantidade = [random.randint(1, 100) for _ in range(6)]
        self.precos = [round(random.uniform(1, 10), 2) for _ in range(6)]
        self.vendas = [random.randint(1, 10) for _ in range(6)]

    def calcula_faturamento(self):
        faturamento = round(sum(self.quantidade) * sum(self.precos), 2)
        return faturamento

    def percentual_vendas(self):
        total_vendas = sum(self.vendas)
        total_faturamento = self.calcula_faturamento()
        percentual = round((total_faturamento / total_vendas) * 100, 2)
        return percentual

    def impressao(self):
        print("O faturamento do armazem é: ", self.calcula_faturamento())
        print("O percentual de vendas é: ", self.percentual_vendas())

    def write_sales_data(self):
        filename = f"sales_data_{str(self.tipo)}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Quantidade: {self.quantidade}\n")
            f.write(f"Tipo: {self.tipo}\n")
            f.write(f"Preços: {self.precos}\n")
            f.write(f"Vendas: {self.vendas}\n")
            f.write(f"Faturamento: {self.calcula_faturamento()}\n")
            f.write(f"Percentual de vendas: {self.percentual_vendas()}\n")
        print(f"Data written to file {filename} successfully.")


    def menu_armazem(self):
        data = []
        for file in os.listdir():
            if file.startswith("sales_data_") and file.endswith(".txt"):
                with open(file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if len(lines) == 6:
                        quantidade = lines[1].split(": ")[1].strip()
                        tipo = lines[1].split(": ")[1].strip()
                        precos = lines[2].split(": ")[1].strip()
                        vendas = lines[3].split(": ")[1].strip()
                        faturamento = lines[4].split(": ")[1].strip()
                        percentual_vendas = lines[5].split(": ")[1].strip()
                        data.append([quantidade, tipo, precos, vendas, faturamento, percentual_vendas])
                    else:
                        print(f"Arquivo {file} não tem o formato esperado e será ignorado.")
        if data:
            df = pd.DataFrame(data, columns=["Quantidade", "Tipo", "Preços", "Vendas", "Faturamento", "Percentual de vendas"])
            print(df)
        else:
            print("Nenhum dado válido encontrado.")



    def grafico(self):
        x = self.tipo
        y = self.quantidade

        plt.bar(x, y)

        plt.xlabel('Tipo')
        plt.ylabel('Quantidade')
        plt.title('Gráfico de vendas')

        plt.show()


armazens = [Armazem(1), Armazem(2), Armazem(3)]

for armazem in armazens:
    armazem.gerar_dados_aleatorios()
    armazem.write_sales_data()
    armazem.menu_armazem()

plt.figure(figsize=(10, 6))
labels = []
sizes = []
for armazem in armazens:
    labels.append(f"Armazem {armazem.tipo}")
    sizes.append(round(sum(armazem.quantidade), 2))

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Gráfico de vendas de vários Armazens')
plt.show()
