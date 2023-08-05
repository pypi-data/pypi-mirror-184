from http import HTTPStatus
import requests
import numpy as np
from typing import List


def create_random_vectors(nvects: int, dim: int) -> List[List[float]]:
    return [np.random.rand(dim).tolist() for _ in range(nvects)]

def check_ok(resp: requests.Response):
    if resp.status_code != HTTPStatus.OK:
        raise RuntimeError(resp.json())
