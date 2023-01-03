import os
from dotenv import load_dotenv
from unittest.mock import Mock, patch

from app.main import app
from app.core.db.session import Base
from app.core.db.mock_session import engine, test_client

load_dotenv(".env")

# It drops everything from the db and then recreate each time tests runs
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = test_client()
X_TOKEN = os.environ["X_TOKEN"]
HEADERS = {"X-Token": X_TOKEN}
ENDPOINT = "/api/sneakers"
LAST_RECORD_ID = 1
PAYLOAD = {
    "brand_name": "Nike",
    "name": "Nike Air Force 1 '07",
    "description": "The radiance lives on in the Nike Air Force 1 '07, the basketball original that puts a fresh spin on what you know best: durably stitched overlays, clean finishes and the perfect amount of flash to make you shine.",
    "size": 42,
    "color": "White",
    "free_delivery": False,
}


def test_invalid_x_token():
    """
    Test if it the endpoint is invalid without the token
    """
    response = client.get(ENDPOINT, params=PAYLOAD)
    assert response.status_code == 422


def test_add_sneaker():

    """
    Tests if the sneakers are being added to the database
    """

    response = client.post(ENDPOINT, json=PAYLOAD, headers=HEADERS)
    data = response.json()

    # validates if the request was successfull
    assert response.status_code == 201

    print(data)

    # validates the saved record
    assert ("name" in data) and ("brand_name" in data)


def test_get_sneaker():

    """
    Tests if the sneakers get request is successfull
    """

    response = client.get(ENDPOINT, headers=HEADERS)

    LAST_RECORD_ID = response.json()[-1]["id"]

    # validates if the request was successfull
    assert response.status_code == 200


def test_add_invalid_sneaker():

    """
    Tests if it validates the inavlid payload
    """

    invalid_payload = PAYLOAD.copy()
    invalid_payload.pop("brand_name", None)

    response = client.post(ENDPOINT, json=invalid_payload, headers=HEADERS)

    # validates if the request was invalid because of inappropriate data
    assert response.status_code == 422


def test_update_sneaker():

    """
    Tests if the sneaker is being updated
    """

    updated_payload = PAYLOAD.copy()
    updated_payload["brand_name"] = "rawheel"
    response = client.put(
        f"{ENDPOINT}/{LAST_RECORD_ID}", json=updated_payload, headers=HEADERS
    )

    # validates if the request was successfull
    assert response.status_code == 201


def test_invalid_update_sneaker():

    """
    Tests if it doesn't update with invalid id
    """

    updated_payload = PAYLOAD.copy()
    updated_payload["brand_name"] = "rawheel"
    response = client.put(f"{ENDPOINT}/12345", json=updated_payload, headers=HEADERS)

    # validates if the it threw an error on invalid id
    assert response.status_code == 404


def test_delete_sneaker():

    """
    Tests if the sneaker is being delete
    """

    response = client.delete(f"{ENDPOINT}/{LAST_RECORD_ID}", headers=HEADERS)

    # validates if the request was successfull
    assert response.status_code == 204


def test_invalid_delete_sneaker():

    """
    Tests if it doesn't delete with invalid id
    """

    response = client.delete(f"{ENDPOINT}/12345", headers=HEADERS)

    # validates if the it threw an error on invalid id
    assert response.status_code == 404
