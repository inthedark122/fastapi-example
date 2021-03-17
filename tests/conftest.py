import pytest
import requests
from typing import Generator
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="module")
def client() -> Generator[requests.Session, None, None]:
    with TestClient(app) as c:
        yield c