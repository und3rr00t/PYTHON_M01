
class Plant:
    """Base class representing common features of a plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes common plant features.

        Args:
            name: Plant name.
            height: Height in cm.
            age: Age in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def base_info(self) -> str:
        """Returns base info for printing.

        Returns:
            str: common stats string
        """
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    """Represents a flowering plant."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializes a flower.

        Args:
            name: Plant name.
            height: Height in cm.
            age: Age in days.
            color: Color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Prints the flower blooming message."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """Returns string representation of the Flower.

        Returns:
            str: flower info
        """
        return f"{self.name} (Flower): {self.base_info()}, {self.color} color"


class Tree(Plant):
    """Represents a tree plant."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initializes a tree.

        Args:
            name: Plant name.
            height: Height in cm.
            age: Age in days.
            trunk_diameter: Diameter of the trunk in cm.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculates and prints the amount of shade produced.
        """
        radius = self.trunk_diameter / 10
        area = (3.14 * (radius ** 2))
        print(f"{self.name} provides {area:.0f} square meters of shade")

    def get_info(self) -> str:
        """Returns string representation of the Tree.

        Returns:
            str: tree info
        """
        return (f"{self.name} (Tree): {self.base_info()}, "
                f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """Represents a vegetable plant."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initializes a vegetable.

        Args:
            name: Plant name.
            height: Height in cm.
            age: Age in days.
            harvest_season: Season of harvest.
            nutritional_value: Vitamin content info.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition(self) -> None:
        """Prints the vegetable's nutritional info."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self) -> str:
        """Returns string representation of the Vegetable.

        Returns:
            str: vegetable info
        """
        return (f"{self.name} (Vegetable): {self.base_info()}, "
                f"{self.harvest_season} harvest")


def main() -> None:
    """Entry point showing inheritance mapping down to output."""
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Sunflower", 130, 85, "yellow")
    ]
    for flower in flowers:
        print()
        print(flower.get_info())
        flower.bloom()

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Willow", 1200, 18250, 80)
    ]
    for tree in trees:
        print()
        print(tree.get_info())
        tree.produce_shade()

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 75, "autumn", "vitamin A")
    ]
    for vegetable in vegetables:
        print()
        print(vegetable.get_info())
        vegetable.get_nutrition()


if __name__ == "__main__":
    main()
