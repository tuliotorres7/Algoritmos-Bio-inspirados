import random
import math
import numpy as np
from funcao_AG import func_obj
import matplotlib.pyplot as plt
from statistics import mean
from random import sample
#from matplotlib import pyplot as plt

nPop = 5
nGer = 30
taxaCruza = 1
taxaMuta = 0.1
dimensao = 2
populacao = []
pais=[]
nElitismo = []
vetMin = []
vetMax = []
vetIndexMin = []

class individuo:
    def __init__(self,x):
        self.x = list(x)

def criaPopulacaoInicial(nPop,populacao):
    for i in range(nPop):
        permuta = sample(range(0, nPop), nPop)
        ind = individuo(permuta)
        
        populacao.append(ind)
    return populacao

def avaliaFitness(populacao,matriz):
    fit = []
    soma = 0
    for ind in populacao:
        for j in range(nPop-1):
            soma = soma + matriz[ind.x[j]][ind.x[j+1]]
            
        soma = soma + matriz[ind.x[nPop-1]][ind.x[0]]
        fit.append(soma)
    return fit

def torneio(nPop,fit,populacao):
    vpais= []
    pv = 0.9
    i = 0
    vencedor = 0
    while( i < nPop ):
        p1 = random.randint(0,nPop-1)
        p2 = random.randint(0,nPop-1)
        while(p1==p2):
            p2 = random.randint(0,nPop-1)
        r = random.randint(0,1)
        if(fit[p2]>fit[p1]):
            vencedor = p1
            if(r>pv):
                vencedor = p2
        else:
            vencedor = p2
        if(r>pv):
            vencedor = p1
        vpais.append(populacao[vencedor])
        i=i + 1
    return vpais
def cruzamento(pais,populacao,taxaCruzamento):
    i = 0
    novaPopulacao = []
    rand = random.random()
    if rand < taxaCruzamento:
        while(len(novaPopulacao)< nPop):
            corteInicio = random.randint(0,nPop)
            corteFim = random.randint(0,nPop)
            while(corteInicio>= corteFim):
                corteInicio = random.randint(0,nPop)
                corteFim = random.randint(0,nPop)
            
            filho1 = individuo([-1]*nPop)
            filho2 = individuo([-1]*nPop)

            for i in range(corteInicio,corteFim):
                filho1.x[i] = pais[1].x[i]
                filho2.x[i] = pais[0].x[i]
            
            dentro0=list()
            dentro0 = pais[1].x[corteInicio:corteFim]
            dentro1 = pais[0].x[corteInicio:corteFim]
            
            vet0 = pais[0].x[corteFim:nPop] + pais[0].x[0:corteFim]
            vet1 = pais[1].x[corteFim:nPop] + pais[1].x[0:corteFim]
            
            j=corteFim+1
            for i in vet0:
                if(j >= nPop):
                    j=0
                if not i in dentro0:
                    filho1.x[j]=i
                j=j+1
            j=corteFim+1
            for i in vet1:
                if(j >= nPop):
                    j=0
                if not i in dentro1:
                    filho2.x[j]=i
                j=j+1
                
                novaPopulacao.append(filho1)
                novaPopulacao.append(filho2)
                i= i + 2
    else:
        novaPopulacao.append(populacao[i])
        i=i+1
    if(len(novaPopulacao)>nPop):
        novaPopulacao.pop(len(novaPopulacao)-1)
    
    return novaPopulacao

def mutacao(populacao,taxaMutacao):
    for ind in populacao:
        rand = random.random()
        if rand < taxaMutacao:
            r = random.randint(0,nPop-1)
            r2 = random.randint(0,nPop-1)
            ind.x[r]= ind.x[r2]
            ind.x[r2] = ind.x[r]
    return populacao

def elitismo(populacaoMutada,populacao,vetFitness):
    novaPopulacao = populacaoMutada
    #o Melhor fitnes que permanece, nao os melhores
    novaPopulacao[2] = populacao[melhorFitness(vetFitness)]
    return novaPopulacao


def melhorFitness(vFitness):
    maior = -99999
    iMaior = 0
    for i in range(len(vFitness)):
        if vFitness[i] > maior:
            maior = vFitness[i]
            iMaior = i
    return iMaior

    

populacao = criaPopulacaoInicial(nPop,populacao)
g=0
while(g<nGer):
    matriz =[ [ 0 , 29 , 82 , 46 , 68 , 52 , 72 , 42 , 51 , 55 , 29 , 74 , 23 , 72 , 46 ],
    [29 ,  0 , 55 , 46 , 42 , 43 , 43 , 23 , 23 , 31 , 41 , 51 , 11 , 52 , 21 ], 
    [82 , 55 ,  0 , 68 , 46 , 55 , 23 , 43 , 41 , 29 , 79 , 21 , 64 , 31 , 51 ], 
    [46 , 46 , 68 ,  0 , 82 , 15 , 72 , 31 , 62 , 42 , 21 , 51 , 51 , 43 , 64 ], 
    [68 , 42 , 46 , 82 ,  0 , 74 , 23 , 52 , 21 , 46 , 82 , 58 , 46 , 65 , 23 ], 
    [52 , 43 , 55 , 15 , 74 ,  0 , 61 , 23 , 55 , 31 , 33 , 37 , 51 , 29 , 59 ], 
    [72 , 43 , 23 , 72 , 23 , 61 ,  0 , 42 , 23 , 31 , 77 , 37 , 51 , 46 , 33 ], 
    [42 , 23 , 43 , 31 , 52 , 23 , 42 , 0  ,33  , 15 , 37 , 33 , 33 , 31 , 37 ], 
    [51 , 23 , 41 , 62 , 21 , 55 , 23 , 33 ,  0 , 29 , 62 , 46 , 29 , 51 , 11 ], 
    [55 , 31 , 29 , 42 , 46 , 31 , 31 , 15 , 29 ,  0 , 51 , 21 , 41 , 23 , 37 ], 
    [29 , 41 , 79 , 21 , 82 , 33 , 77 , 37 , 62 , 51 ,  0 , 65 , 42 , 59 , 61 ], 
    [74 , 51 , 21 , 51 , 58 , 37 , 37 , 33 , 46 , 21 , 65 ,  0 , 61 , 11 , 55 ], 
    [23 , 11 , 64 , 51 , 46 , 51 , 51 , 33 , 29 , 41 , 42 , 61 ,  0 , 62 , 23 ], 
    [72,  52,  31,  43,  65,  29,  46,  31,  51,  23,  59,  11,  62,   0,  59],  
    [46 , 21 , 51 , 64 , 23 , 59 , 33 , 37 , 11 , 37 , 61 , 55 , 23 , 59 ,  0 ],]
    fitness = avaliaFitness(populacao,matriz)
    pais = torneio(nPop,fitness,populacao)
    populacaoCruzada = cruzamento(pais,populacao,taxaCruza)
    populacaoMutada = mutacao(populacaoCruzada,taxaMuta)
    populacaoFinal = elitismo(populacaoMutada,populacao, fitness)
    populacao = populacaoFinal
    vetMin.append(min(fitness))

    vetMax.append(max(fitness))
    print(vetMax)
    #vetIndexMin.append(index(min(fitness)))
    g=g+1
aux = []
for x in range(1,nGer+1):
    aux.append(x)
#plt.plot(vetMin)
#plt.plot(vetMax)
#res = [mean(values) for values in zip(vetMin,vetMax)]
#plt.plot(res)
#plt.title("Max, Min , Média por Geração")
#plt.show()
#print(populacao)
     