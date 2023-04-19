def funcionA(funcionB):

    def funcionC(*args, **kwargs):
        print("Está por ejecutarse la función")
        print("Valores de *args: {}".format(args))
        print("Valores de kwargs: {}".format(kwargs.items()))
        resultado = funcionB(*args, **kwargs)
        print("“La función ha sido ejecutado correctamente")
        return resultado
    return funcionC


@funcionA
def multiplica(n1, n2, n3, n4):
    print("La multiplicación es: {}".format(n1 * n2 * n3 * n4))


@funcionA
def suma(n1, n2):
    print("La suma es: {}".format(n1 + n2))


suma(1, 3)
multiplica(1, 2, 3, 4)
