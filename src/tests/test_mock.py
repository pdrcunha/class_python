import pytest
from controller import UserController, Controller, pick_winner

def test_run(mocker):
    # Instância da classe
    controller = Controller()
    
    # Mock do método get: retorna "nam:joyce"
    mocker.patch.object(controller, 'get', return_value={"nam:joyce"})

    # Mock do requests.post para simular status_code = 200
    mock_post = mocker.patch("controller.requests.post")
    mock_post.return_value.status_code = 200

    # Mock do método post para capturar o argumento
    mock_post_method = mocker.patch.object(controller, 'post')

    # Executa o método run
    controller.run()

    # Verifica se o método post foi chamado com "nam>hoyce"
    mock_post_method.assert_called_once_with({"nam:joyce"})


def test_welcome_user(mocker):
    controller = UserController()
    mocker.patch.object(controller.service, 'get_user', return_value={"id": 1, "name": "Joyce"})

    msg = controller.welcome_user(1)
    assert msg == "Welcome, Joyce!"
    

def test_pick_winner(mocker):
    mocker.patch("controller.random.choice", return_value="Joyce")

    winner = pick_winner()
    assert winner == "Joyce"
