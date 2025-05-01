from abc import ABC, abstractmethod

# 1. Classe e Objeto
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dizer_ola(self):
        print(f"Olá, meu nome é {self.nome}")

# 2. Atributos Públicos e Privados
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo       # protegido
        self.__senha = "1234"     # privado

    def mostrar_saldo(self):
        print(f"Saldo: {self._saldo}")

# 3. Herança
class Animal:
    def falar(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late.")

# 4. Herança Múltipla
class A:
    def metodo_a(self):
        print("A")

class B:
    def metodo_b(self):
        print("B")

class C(A, B):
    pass

# 5. super()
class Pai:
    def falar(self):
        print("Pai falando")

class Filho(Pai):
    def falar(self):
        super().falar()
        print("Filho falando")

# 6. Métodos Especiais
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return f"Livro: {self.titulo}"

# 7. Métodos Estáticos
class Utils:
    @staticmethod
    def somar(a, b):
        return a + b

# 8. Métodos de Classe
class Produto:
    taxa = 1.2

    def __init__(self, preco):
        self.preco = preco * Produto.taxa

    @classmethod
    def com_desconto(cls, preco, desconto):
        return cls(preco * (1 - desconto))

# 9. Abstração
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# 10. Polimorfismo
class FormaBase:
    def desenhar(self):
        print("Desenhando forma")

class Circulo(FormaBase):
    def desenhar(self):
        print("Desenhando círculo")

# 11. Encapsulamento
class ProdutoSeguro:
    def __init__(self, preco):
        self._preco = preco

    def get_preco(self):
        return self._preco

    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self._preco = novo_preco
