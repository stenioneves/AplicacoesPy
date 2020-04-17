# Aplicativo para calcular e projetar redimentos de fundos financeiros 
#Autor : Stenio neves data: 15/04/2020


print(" Caculador de investimentos", "Teste ", sep="*#", end="#*")
print()
nome_fundo= input("Digite o codigo do fundo ")
valor_fundo_cota= float(input("Digite o valor da cota do fundo na B3  R$: "))
quantidade_cota= int(input("Digite números de cotas que tem ou pretende compras: "))
dividendo_mes = float(input("Digite o valor do ultimo dividendo pago R$: "))
print("Valor total investido ou previsto R$ ",valor_fundo_cota*quantidade_cota)
print("Rentabilidade : ", dividendo_mes/valor_fundo_cota,"%")
print("Total de dividendo recebidos ou projetados ",nome_fundo," R$: ",dividendo_mes*quantidade_cota)
#Futura interação

print("Esse programa é somente para teste !")


