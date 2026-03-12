class Plant:
    """Represents a plant with a name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes a plant with its starting values.

        Args:
            name: The name of the plant.
            height: Starting height in cm.
            age: Starting age in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Returns string representation of the plant.

        Returns:
            str: the plant's stats
        """
        return f"{self.name} ({self.height}cm, {self.age} days)"


def main() -> None:
    """Entry point of the program. Prints basic plant info."""
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    print("=== Plant Factory Output ===")
    total = 0
    for plant in plants:
        print(f"Created: {plant.get_info()}")
        total += 1

    print(f"\nTotal plants created: {total}")


if __name__ == "__main__":
    main()
