'''
Trabalho 01 - Analise de Algoritmo
Grupo:
-Emanuel Umbelino
-Yuri Strack
'''

import random
import time

def BubbleSort(L):
	Lord = L[:]
	trocado = True
	k = 1
	while trocado and k < len(Lord):
		trocado = False
		for i in range(len(Lord)-k):
			if Lord[i] > Lord[i+1]:
				aux = Lord[i]
				Lord[i] = Lord[i+1]
				Lord[i+1] = aux
				trocado = True
		k+1
	return Lord

def SortSelection(A,k):
	Aord = BubbleSort(A)
	return Aord[k-1]

def Sample(max,n):
	return random.sample(range(max),n)

def LinearSelection(A,k):
	if (len(A) <= 1):
		return A[0]
	# divide em grupos de 5
	groups = []
	i = 0
	while i < len(A):
		g = []
		for c in range(5):
			g += [A[i]]
			i += 1
			if (i >= len(A)):
				break
		groups += [g]
	# pega a mediana de cada grupo
	M = []
	for g in groups:
		BubbleSort(g)
		M += [g[len(g)//2]]
	# pega a mediana das medianas
	m = LinearSelection(M,len(M)//2)
	# faz duas listas ao redor da mediana e conta quantos valores iguais a mediana
	L = []
	R = []
	equals = 0
	for i in range(len(A)):
		if (A[i] < m):
			L += [A[i]]
		elif (A[i] > m):
			R += [A[i]]
		else:
			equals += 1
	# se o que eu quero estiver na direita ou na esquerda, recursao pra la
	# se tiver entre os repetidos achei
	if (len(L) >= k):
		return LinearSelection(L,k)
	elif (len(L) + equals >= k):
		return m
	else:
		return LinearSelection(R,k-len(L)-equals)

def teste(func,lista,kPos):
	ini = time.time()
	testMOM = func(lista,kPos)
	fim = time.time()
	tempo = fim - ini
	return tempo

def main():
	MOMmedias = []
	SLmedias = []
	for nTestes in range(1,11):
		tempoTotalMOM = 0
		tempoTotalSL = 0

		for nInstancias in range(10):
			inst = Sample(100000,nTestes * 1000)
			tempo = teste(LinearSelection,inst,(nTestes * 1000)//2)
			tempoTotalMOM += tempo
			tempo = teste(SortSelection,inst,(nTestes * 1000)//2)
			tempoTotalSL += tempo

		MOMmedias.append(tempoTotalMOM/10)
		SLmedias.append(tempoTotalSL/10)

	print(MOMmedias)
	print(sum(MOMmedias))
	print(SLmedias)
	print(sum(SLmedias))

main()
