import pytest

@pytest.fixture
def resource():
    print("Setup: abrir conexão")
    yield "dados simulados"
    print("Teardown: fechar conexão")

def test_usa_resource_one(resource):
    print("Executando teste 1")
    assert resource == "dados simulados"

def test_usa_resource_two(resource):
    print("Executando teste 2")
    assert resource == "dados simulados"