from random import randint
import os
MIN_MERGE = 32

# Retorna o tamanho mínimo de uma run
def calculaRunMinima(tamanho):
	run = 0
	while tamanho >= MIN_MERGE: #Exemplo: caso o tamanho da run seja 32, o minimal run será 16.
		run |= tamanho & 1 ##operação bitwise, bit a bit. Por exemplo: se tamanho = 5 a operação resultara em 1. Porque em binário 5 é equivalente a 101
		# e 1 é equivalente à 001. E o bit a bit desses números resultará em 001. Essa linha tem como o objetivo garantir que run seja equivalente a 1 caso o tamanho
    #da run for impar
		tamanho >>= 1 ##divide o valor de tamanho em 2
	return tamanho + run

def insertionSort(array, esquerda, direita):
	for i in range(esquerda + 1, direita + 1):
		j = i
		while j > esquerda and array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j]
			j -= 1


def merge(array, esquerda, meio, direita):

	len1, len2 = meio - esquerda + 1, direita - meio
	left, right = [], []
	for i in range(0, len1):
		left.append(array[esquerda + i])
	for i in range(0, len2):
		right.append(array[meio + 1 + i])

	i, j, k = 0, 0, esquerda

	while i < len1 and j < len2:
		if left[i] <= right[j]:
			array[k] = left[i]
			i += 1

		else:
			array[k] = right[j]
			j += 1

		k += 1

	while i < len1:
		array[k] = left[i]
		k += 1
		i += 1

	while j < len2:
		array[k] = right[j]
		k += 1
		j += 1

def timSort(array):
	tamanho = len(array)
	minRun = calculaRunMinima(tamanho)
	for inicio in range(0, tamanho, minRun):
		fim = min(inicio + minRun - 1, tamanho - 1)
		insertionSort(array, inicio, fim)
	size = minRun
	while size < tamanho:
		for esquerda in range(0, tamanho, 2 * size):
			meio = min(tamanho - 1, esquerda + size - 1)
			direita = min((esquerda + 2 * size - 1), (tamanho - 1))

			if meio < direita:
				merge(array, esquerda, meio, direita)

		size = 2 * size

def gerarVetor(tamanho): 
	vetor = []
	for index in range(0, tamanho, 1):
		vetor.append(randint(-100, 100))
	return vetor


os.system('clear')
print("Tim Sort com um array de 64 elementos no intervalo de -100 até 100")
vetorInicial = gerarVetor(64)
print("O Array que vamos ordenar é: ")
print(vetorInicial)

timSort(vetorInicial)

print("Array ordenado através do Tim Sort: ")
print(vetorInicial)
	
	