# Sistema de Classificação de Consumo de Água
# Projeto desenvolvido em Python

# Solicita o tipo de imóvel
tipo_imovel = input("Digite o tipo de imóvel (casa, apartamento ou comércio): ")

# Solicita o consumo mensal de água
consumo = float(input("Digite o consumo mensal de água em m³: "))

# Classifica o consumo de acordo com o valor informado
if consumo < 10:
    classificacao = "Consumo baixo"
    alerta = "O consumo está dentro de uma faixa baixa."
elif consumo < 20:
    classificacao = "Consumo moderado"
    alerta = "Fique atento ao consumo de água."
else:
    classificacao = "Consumo alto"
    alerta = "É recomendado reduzir o consumo de água."

# Exibe os resultados
print("\n--- Resultado ---")
print("Tipo de imóvel:", tipo_imovel)
print("Consumo mensal:", consumo, "m³")
print("Classificação:", classificacao)
print("Alerta:", alerta)
