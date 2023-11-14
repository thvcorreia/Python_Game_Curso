from random import randint


class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:   # (, /) Deixa o (difuldade) posicional, n precisa inform
        self.__dificuldade: int = dificuldade
        self.__valor1: float = self._gerar_valor
        self.__valor2: float = self._gerar_valor
        self.__operacao: int = randint(1, 4)    # 1 = somar, 2 = subtrair, 3 = multiplicar, 4 = dividir
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> float:
        return self.__valor1

    @property
    def valor2(self: object) -> float:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> float:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ' '
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        elif self.operacao == 4:
            op = 'Dividir'
        else:
            op = 'Operação desconhecida'
        return f'Dificuldade: {self.dificuldade} \nOperação: {op} \nValor 1: {self.valor1} \nValor 2: ' \
               f'{self.valor2}'

    @property
    def _gerar_valor(self: object) -> float:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(10, 100)
        elif self.dificuldade == 3:
            return randint(100, 1000)
        elif self.dificuldade == 4:
            return randint(1000, 10000)
        else:
            return randint(10000, 10000000000)

    @property
    def _gerar_resultado(self: object) -> float:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        elif self.operacao == 3:
            return self.valor1 * self.valor2
        else:
            return self.valor1 / self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        else:
            return '/'

    def checar_resultado(self: object, resposta: float) -> bool:
        certo: bool = False
        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2}')
