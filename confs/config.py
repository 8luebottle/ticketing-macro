import yaml

from pathlib import Path


yaml_file = "config.yaml"

p = Path(__file__).resolve()
conf_path = p.parent / yaml_file

with conf_path.open() as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


class Login(object):
    def __init__(self):
        self._login = config["login"]

    def id(self):
        return self._login["id"]

    def pw(self):
        return self._login["pw"]


class Site(object):
    def __init__(self):
        self._site = config["site"]

    def url(self):
        return self._site["url"]


conf = {
    "login": Login(),
    "site": Site(),
}
