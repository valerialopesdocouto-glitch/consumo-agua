# Sistema de Classificação de Consumo de Água
# Agenda 07 - Desenvolvimento de Sistemas I

# Solicita o tipo de imóvel
tipo_imovel = input(
    "Digite o tipo de imóvel (comercial, casa ou apartamento): "
).lower()

# Solicita o consumo mensal de água
consumo = float(
    input("Digite o consumo mensal de água em m³: ")
)

# Classifica o consumo de acordo com as regras da atividade
if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
