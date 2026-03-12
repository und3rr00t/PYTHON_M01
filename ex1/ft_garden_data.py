class Plant:
    """Represents a plant with a name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes a plant with name, height, and age.

        Args:
            name: The name of the plant.
            height: Height in cm.
            age: Age in days.
        """
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    """Entry point of the program. Prints basic plant info."""
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()
