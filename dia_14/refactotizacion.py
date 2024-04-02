# Inicio
valor_entrada = 10
valor_1 = valor_entrada**2 + valor_entrada**3
valor_2 = valor_1*2 + valor_1*3 + valor_1*4
valor_3 = valor_2**2 + valor_2**3
valor_4 = valor_3*2 + valor_3*3 + valor_3*4
valor_5 = valor_4**2 + valor_4**3
valor_6 = valor_5*2 +valor_5*3 + valor_5*4

print(valor_entrada)
print(valor_1)
print(valor_2)
print(valor_3)
print(valor_4)
print(valor_5)
print(valor_6)

print("========================================")
# Primera Refactorización
def cuadrado_cubo(valor):
    return valor**2 +valor**3

def mult_234(valor):
    return valor*2 + valor*3 + valor*4

valor_entrada = 10
valor_1 = cuadrado_cubo(valor_entrada)
valor_2 = mult_234(valor_1)
valor_3 = cuadrado_cubo(valor_2)
valor_4 = mult_234(valor_3)
valor_5 = cuadrado_cubo(valor_4)
valor_6 = mult_234(valor_5)

print(valor_entrada)
print(valor_1)
print(valor_2)
print(valor_3)
print(valor_4)
print(valor_5)
print(valor_6)

print("========================================")
# Segunda Refactorización
def cuadrado_cubo(valor):
    return valor**2 +valor**3

def mult_234(valor):
    return valor*2 + valor*3 + valor*4

def op_combinada(valor):
    var_intermedia = cuadrado_cubo(valor)
    return mult_234(var_intermedia)

valor_entrada = 10
valor_2 = op_combinada(valor_entrada)
valor_4 = op_combinada(valor_2)
valor_6 = op_combinada(valor_4)

print(valor_entrada)
print(valor_2)
print(valor_4)
print(valor_6)

print("========================================")
# Segunda Refactorización
def cuadrado_cubo(valor):
    return valor**2 +valor**3

def mult_234(valor):
    return valor*2 + valor*3 + valor*4

def op_combinada(valor):
    var_intermedia = cuadrado_cubo(valor)
    return mult_234(var_intermedia)

def compose(f, n):
    def fn(x):
        for _ in range(n):
            x = f(x)
        return x
    return fn

valor_entrada = 10
valor_6 = compose(op_combinada, 3)(valor_entrada)

print(valor_6)