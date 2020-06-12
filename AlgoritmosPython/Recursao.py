def funcao(i):
	print("executando")
	if i < 5:
		i += 1
		funcao(i)

i = 1
funcao(i)