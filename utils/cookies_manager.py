import json
import os


class Cookies:
    @staticmethod
    def save_cookie(cookie: dict) -> None:
        with open("data/cookie.json", "w") as file:
            json.dump(cookie, file, indent=4)

    @staticmethod
    def get_cookie_from_file() -> dict:
        with open("data/cookie.json", "r") as file:
            return json.load(file)

    @staticmethod
    def delete_cookie_file() -> None:
        os.remove("data/cookie.json")
