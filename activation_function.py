import numpy as np

# 0 ou 1
def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

# 0 a 1 com casa decimal
def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))

def tanFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))
# -1 a 1

def reluFunction(soma):
    if soma >= 0 :
        return soma
    return 0
# 0 ou >0

def linearFunction(soma):
    return soma
# retorna a soma

def softmaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()
#retorna a maior probabilidade

teste = stepFunction(30)
print(f"StepFunction = {teste}")
teste = sigmoidFunction(-0.358)
print(f"SigmoidFunction = {teste}")
teste = tanFunction(-0.358)
print(f"TanFunction = {teste}")
teste = reluFunction(0.358)
print(f"Relufunciton= {teste}")
teste = linearFunction(0.587)
print(f"linearFunction = {teste}")
valores = [5.0, 2.0, 1.3]
print(f"softmax = {softmaxFunction(valores)}")