import os
import random

import requests
from requests.sessions import session
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS


def get_random_number():
    return random.choice([1, 2, 3, 4])


def create_session():

    # proxy = FreeProxy().get()

    # proxies = {"http": proxy}

    """random_number = get_random_number()
    gateway = ApiGateway(
        "https://api.gdeltproject.org",
        regions=EXTRA_REGIONS,
        access_key_id=os.getenv(f"AWS_ACCESS_KEY_ID_{random_number}"),
        access_key_secret=os.getenv(f"AWS_SECRET_ACCESS_KEY_{random_number}"),
    )"""
    # gateway.start()
    session = requests.Session()

    # session.proxies.update(proxies)
    # session.mount("https://api.gdeltproject.org", gateway)

    return session
