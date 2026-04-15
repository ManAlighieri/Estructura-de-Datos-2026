#5. Análisis Sintáctico de Expresiones (AST)
#Descripción: Tomando como base la expresión matemática (8 + 4) * 2. 
# Tarea: Describe cómo un compilador representaría esta operación mediante un Árbol de Sintaxis Abstracta (AST). 
# Debes identificar cuál sería el nodo raíz (la operación de mayor jerarquía tras evaluar los paréntesis), 
# cuáles serían los nodos internos y cuáles serían las hojas (los literales o números). 
# Explica cómo esta estructura permite al compilador respetar la precedencia de los operadores.

class NodoAST:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

    def es_hoja(self):
        return self.izq is None and self.der is None

    def evaluar(self):
        if self.es_hoja():
            return int(self.valor)
        izq = self.izq.evaluar()
        der = self.der.evaluar()
        ops = {"+": izq + der, "-": izq - der,
               "*": izq * der, "/": izq / der}
        return ops[self.valor]

    def imprimir(self, nivel=0, prefijo=""):
        tipo = "[hoja]" if self.es_hoja() else "[op]  "
        print(prefijo + tipo + " " + str(self.valor))
        if self.izq: self.izq.imprimir(nivel+1, prefijo + "  ├─ ")
        if self.der: self.der.imprimir(nivel+1, prefijo + "  └─ ")

def construir_ast_simple(expr):
    "Parser básico para expresiones con paréntesis."
    expr = expr.replace(" ", "")
    def parse(s):
        if s[0] == "(":
            s = s[1:-1]
        for op in ("+-", "*/"):
            depth = 0
            for i in range(len(s)-1, -1, -1):
                if s[i] == ")": depth += 1
                elif s[i] == "(": depth -= 1
                elif depth == 0 and s[i] in op:
                    nodo     = NodoAST(s[i])
                    nodo.izq = parse(s[:i])
                    nodo.der = parse(s[i+1:])
                    return nodo
        return NodoAST(s)
    return parse(expr)

expresiones = ["(8 + 4) * 2", "10 + 3 * 5", "(6 - 2) * (3 + 1)"]
for expr in expresiones:
    ast = construir_ast_simple(expr)
    print(f"\nExpresión: {expr} = {ast.evaluar():.0f}")
    print("AST:")
    ast.imprimir()