from planet import Planet
from planet_db import PlanetDB

class App:
    def __init__(self):
        self.planet_db = PlanetDB()


if __name__ == "__main__":
    app = App()
