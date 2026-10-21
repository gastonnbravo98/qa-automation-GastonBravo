import pytest
import requests

def obtener_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    return requests.get(url)


@pytest.fixture(scope="module")
def respuesta():
    return obtener_pokemon("pikachu")


def test_status_code_es_200(respuesta):
    assert respuesta.status_code == 200


def test_nombre_es_pikachu(respuesta):
#    data = respuesta.json()
#    assert data["name"] == "pikachu"
    assert respuesta.json()["name"] == "pikachu"


def test_id_es_25(respuesta):
  #   assert data["id"] == 25
    assert respuesta.json()["id"] == 25