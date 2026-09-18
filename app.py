# Sistema de Classificação de Consumo de Água

# Solicita o tipo de imóvel
tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# Solicita o consumo mensal de água
consumo = float(input("Digite o consumo mensal de água (m³): "))

# Classificação do consumo
if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")