import pytest

def add(a, b):
    return a + b

# 🚀 Roda uma vez e todo teste pega o retorno dele... 
@pytest.fixture(scope="module")
def db_connection():
    print("Run tests")


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


@pytest.mark.parametrize(
    "a, b, expected",
    [
    (2, 2, 4),
    (10, -5, 5),
    ],
    ids=["soma_positiva", "soma_negativo"]
)

def test_add_parametrizado(a, b, expected):
    assert add(a, b) == expected


# 🚀 Criamos uma fixture que retorna números prontos para teste, roda sempre para todos os testes
@pytest.fixture
def input_numbers():
    return (3, 4)

# 🎯 Usamos a fixture como argumento do teste
def test_add_with_fixture(input_numbers):
    a, b = input_numbers
    assert add(a, b) == 7


@pytest.mark.usefixtures("db_connection")
def test_something():
    print("Executando teste")
    assert True