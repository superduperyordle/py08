lista_convidados = []

for i in range(4):
    lista_convidados.append(input("Esira o nome de um convidado"))

lista_convidados.sort()
print(len(lista_convidados))
for convidado in lista_convidados:
    print(convidado)
