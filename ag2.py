import random
import math
import numpy as np
from funcao_AG import func_obj
import matplotlib.pyplot as plt
from statistics import mean
#from matplotlib import pyplot as plt

nPop = 20
nGer = 20
realMax = 1
taxaCruza = 1
taxaMuta = 0.1
maxNum = 2
minNum = -2 
dimensao = 2
populacao = []
pais=[]
nElitismo = []
vetMin = []
vetMax = []
vetIndexMin = []
alpha = 0.2
beta = 0.4
class individuo:
    def __init__(self,x,dimensao):
        self.x = []
        self.ndim = [dimensao]


def criaPopulacaoInicial(nPop,populacao):
    for i in range(nPop):
        ind = individuo(0,dimensao)
        ind.x = []
        for k in range(dimensao):
            ind.x.append(random.uniform(minNum,maxNum))    
        populacao.append(ind)
    return populacao

def avaliaFitness(minNum,maxNum,populacao):
    fit = []
    for x in populacao:
        fit.append(func_obj(x.x))
    for x in range(len(fit)):
        if(fit[x]==0):
            fit[x]=-0.0001
        fit[x]=1/fit[x]
    return fit

def roleta(nPop,fit,populacao):
    vpais= []
    p = []
    vencedor = individuo(0,2)#dimensao nao dinamica
    a = int()#soma
    q = []
    j=0
    for i in range(nPop):
        a = a + fit[i]

    for i in range(nPop):
        p.append(fit[i]/a)
    
    for j in range(nPop):
        soma = 0
        for i in range(j):
            soma = soma + p[i]
        q.append(soma)
    
    for i in range(nPop):
        r = random.uniform(0,1)#valor do rand, so olhar o soma vai ser maior que 1 
        j=0
        while(r <= q[j]):
            vencedor = populacao[j]
            j=j+1
        vpais.append(vencedor)
    return vpais
def cruzamento(pais,populacao,dimensao,alpha,beta,maxNum,minNum,taxaCruza):
    novaPopulacao = []
    j=0
    while(len(novaPopulacao) <= nPop):
        r=random.random()
        if r< taxaCruza :                    
            X = random.randint(0,nPop-1)
            Y = random.randint(0,nPop-1)
            X=populacao[X]
            Y=populacao[Y]
            #nao iguais
            if func_obj(X.x) < func_obj(Y.x):
                Z = individuo(0,0)
                Z = X
                X = Y
                Y = Z
            d = []
            filho1 = individuo(0,dimensao)
            filho2 = individuo(0,dimensao)    
            for i in range(dimensao):
                d.append(X.x[i] - Y.x[i])
                if X.x[i] <= Y.x[i]:
                    u = random.uniform(X.x[i]-alpha* d[i],Y.x[i] + beta * d[i])        
                    while((u>maxNum)or(u<minNum)):
                        u = random.uniform(X.x[i]-alpha* d[i],Y.x[i] + beta * d[i])        
                    filho1.x.append(u)
                    while((u>maxNum)or(u<minNum)):
                        u = random.uniform(X.x[i]-alpha* d[i],Y.x[i] + beta * d[i])        
                    filho2.x.append(u)
                    novaPopulacao.append(filho1)
                    if(len(novaPopulacao) <= nPop):
                        novaPopulacao.append(filho2)
                else:
                    u = random.uniform(Y.x[i]-beta * d[i],X.x[i] + alpha * d[i])       
                    while((u>maxNum)or(u<minNum)):
                        u = random.uniform(Y.x[i]-beta * d[i],X.x[i] + alpha * d[i])
                    filho1.x.append(u)
                    while((u>maxNum)or(u<minNum)):
                        u = random.uniform(Y.x[i]-beta * d[i],X.x[i] + alpha * d[i])
                    filho2.x.append(u)
                    novaPopulacao.append(filho1)
                    if(len(novaPopulacao) <= nPop):
                        novaPopulacao.append(filho2)
        else:   
            novaPopulacao.append(populacao[i])
        j=j+1
    return novaPopulacao


def mutacao(populacao,taxaMutacao,dimensao,maxNum,minNum):
    for ind in populacao:
        rand = random.random()#confirmar se é assim que define os valores max min
        if rand < taxaMutacao:
            rand = random.randint(0,dimensao + 1)
            ind.x[rand] = random.uniform(minNum,maxNum)
    return populacao

def elitismo(populacaoMutada,populacao,vetFitness):
    novaPopulacao = populacaoMutada
    #o Melhor fitnes que permanece, nao os melhores
    rand = random.randint(0,nPop)
    novaPopulacao[rand] = populacao[melhorFitness(vetFitness)]
    return novaPopulacao


def melhorFitness(vFitness):
    menor = 99999
    iMenor = 0
    for i in range(len(vFitness)):
        if vFitness[i] < menor:
            menor = vFitness[i]
            iMenor = i
    return iMenor

    

populacao = criaPopulacaoInicial(nPop,populacao)
g=0
while(g<nGer):
    fitness = avaliaFitness(minNum,maxNum,populacao)
    pais = roleta(nPop,fitness,populacao)
    populacaoCruzada = cruzamento(pais,populacao,dimensao,alpha,beta,maxNum,minNum,taxaCruza)
    populacaoMutada = mutacao(populacaoCruzada,taxaMuta,dimensao,maxNum,minNum)
    populacaoFinal = elitismo(populacaoMutada,populacao, fitness)
    populacao = populacaoFinal
    vetMin.append(min(fitness))
    vetMax.append(max(fitness))
    #vetIndexMin.append(index(min(fitness)))
    g=g+1
aux = []
for x in range(1,nGer+1):
    aux.append(x)
plt.plot(vetMin)
plt.plot(vetMax)
res = [mean(values) for values in zip(vetMin,vetMax)]
plt.plot(res)
plt.title("Max, Min , Média por Geração")
plt.show()
#print(populacao)







#def cruzamentoAlpha(pais,populacao,dimensao,alpha,maxNum,minNum,taxaCruza):
#    novaPopulacao = []
#    filho1 = individuo(0,0)
#    filho2 = individuo(0,0)
#    j=0
#    while(len(novaPopulacao) <= nPop):
#        r=random.random()
#        if r< taxaCruza :                    
#            X = random.randint(0,nPop)
#            Y = random.randint(0,nPop)
#            X=populacao[X]
#            Y=populacao[Y]
#            d = []
#            for i in range(dimensao):
#                d[i] = X.x[i] - Y.x[i]
#                u = random.uniform(min(X.x[i],Y.x[i])-alpha*d[i],max(X.x[i],Y.x[i]+ alpha * d[i]))        
#                while((u>maxNum)or(u<minNum)):
#                    u = random.uniform(min(X.x[i],Y.x[i])-alpha*d[i],max(X.x[i],Y.x[i]+ alpha * d[i]))        
#                filho1.x[i] = u
#                while((u>maxNum)or(u<minNum)):
#                    u = random.uniform(min(X.x[i],Y.x[i])-alpha*d[i],max(X.x[i],Y.x[i]+ alpha * d[i]))        
#                filho2.x[i] = u
#                novaPopulacao.append(individuo(filho1,dimensao))
#                novaPopulacao.append(individuo(filho2,dimensao))
#        else:
#            novaPopulacao.append(populacao[j])    
#            j=j+1
#    return novaPopulacao
