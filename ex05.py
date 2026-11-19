semana = ("Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab")

print(semana[0])
print(semana[-1])

semana[0] = "Feriado" # TypeError: 'tuple' object does not support item assignment , objetos de uma tupla não podem ser alterados.