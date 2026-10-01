class Estinien:

    def __init__(self, name: str, level: int, health: int, isAzureDragoon: bool):
        self.name = name
        self.level = level

        self.__health = health
        self.__isAzureDragoon = isAzureDragoon

    def TrueThrust(self, damage: int):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
        print(f"{self.name} performed TrueThrust for {damage}.")
    def DragonDive(self, damage: int):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
        print(f">> {self.name} used Dragon Dive for {damage} damage.")
    def get_details(self) -> str:
        return (
            f"{self.name} | Level: {self.level} | "
            f"Health: {self.__health} | "
            f"Azure Dragoon: {self.__isAzureDragoon}"
        )
if __name__ == "__main__":
    estinien1 = Estinien(
        name="Estinien",
        level=90,
        health=1000,
        isAzureDragoon=True
    )
    estinien2 = Estinien(
        name="Estinien",
        level=80,
        health=850,
        isAzureDragoon=True
    )
    print("Before:")
    print(f"Object 1: {estinien1.get_details()}")
    print(f"Object 2: {estinien2.get_details()}")
    print()

    print("Action: Performing TrueThrust(200) on Object 1...")
    estinien1.TrueThrust(200)
    print()

    print("After:")
    print(f"Object 1: {estinien1.get_details()}")
    print(f"Object 2: {estinien2.get_details()}")

