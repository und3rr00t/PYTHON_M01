class Plant:
    """Represents a plant with a name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes a plant with name, height, and age.

        Args:
            name: The name of the plant.
            height: Initial height in cm.
            age: Initial age in days.
        """
        self.name = name
        self.height = height
        self._age = age

    def grow(self) -> None:
        """Increases the plant's height by 1 cm."""
        self.height += 1

    def age(self) -> None:
        """Increases the plant's age by 1 day."""
        self._age += 1

    def get_info(self) -> str:
        """Retrieves formatted information about the plant.

        Returns:
            str: Plant info with name, height, and age.
        """
        return f"{self.name}: {self.height}cm, {self._age} days old"


def main() -> None:
    """Simulates a week of growth for plants."""
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 50, 45),
        Plant("Cactus", 15, 120)
        ]
    start_height = {}

    print("=== Day 1 ===")
    for plant in plants:
        start_height[plant.name] = plant.height
        print(plant.get_info())

    for _ in range(6):
        for plant in plants:
            plant.grow()
            plant.age()

    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
        growth = plant.height - start_height[plant.name]
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
