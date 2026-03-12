class Plant:
    """Base class representing a general plant.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in cm.
    """
    _kind = "regular"

    def __init__(self, name: str, height: int):
        """Initializes the plant.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant.
        """
        self.name = name
        self.height = height

    def grow(self, amount: int):
        """Increases the height of the plant.

        Args:
            amount (int): The amount of cm to grow.
        """
        self.height += amount

    def __str__(self) -> str:
        """Returns the string representation of the plant."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Represents a flower that can bloom.

    Attributes:
        color (str): The color of the flowers.
        is_blooming (bool): Whether the flower is currently blooming.
    """
    _kind = "flowering"

    def __init__(self, name: str, height: int, color: str):
        """Initializes the flowering plant.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant.
            color (str): The color of the flowers.
        """
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def __str__(self) -> str:
        """Returns the string representation including bloom status."""
        status = ""
        if self.is_blooming:
            status = " (blooming)"
        return f"{super().__str__()}, {self.color} flowers{status}"


class PrizeFlower(FloweringPlant):
    """A specialized flower that holds points.

    Attributes:
        points (int): The prize points associated with the flower.
    """
    _kind = "prize"

    def __init__(self, name: str, height: int, color: str, points: int):
        """Initializes the prize flower.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant.
            color (str): The color of the flowers.
            points (int): The prize points.
        """
        super().__init__(name, height, color)
        self.points = points

    def __str__(self) -> str:
        """Returns the string representation including prize points."""
        return f"{super().__str__()}, Prize points: {self.points}"


class Garden:
    """Represents a garden containing multiple plants.

    Attributes:
        owner (str): The name of the garden owner.
        plants (list): A list containing plant objects.
        total_growth_applied (int): Sum of growth increments applied.
    """
    def __init__(self, owner: str, plants: list = None):
        """Initializes the garden.

        Args:
            owner (str): The owner of the garden.
            plants (list, optional): Initial list of plants.
        """
        self.owner = owner
        self.plants = plants
        if plants is None:
            self.plants = []
        self.total_growth_applied = 0

    def add_plant(self, plant: Plant):
        """Adds a plant to the collection.

        Args:
            plant (Plant): The plant instance to add.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_growth(self, amount: int):
        """Triggers growth for all plants.

        Args:
            amount (int): Amount of cm each plant grows.
        """
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.total_growth_applied += amount
            print(f"{plant.name} grew {amount}cm")


class GardenManager:
    """Main system to manage gardens and analytics.

    Attributes:
        total_gardens (int): Static count of managed gardens.
    """
    total_gardens = 0

    class GardenStats:
        """Helper class for calculating analytics."""
        def calculate_score(plants: list) -> int:
            """Calculates the total score for a list of plants.

            Args:
                plants (list): List of plants to analyze.

            Returns:
                int: The total calculated score.
            """
            score = 0
            for plant in plants:
                score += plant.height + 10
                if plant._kind == "prize":
                    score += plant.points
            return score

        calculate_score = staticmethod(calculate_score)

    def __init__(self, garden: Garden):
        """Initializes the manager.

        Args:
            garden (Garden): The garden instance to manage.
        """
        self.garden = garden
        GardenManager.total_gardens += 1

    def create_garden_network(cls, gardens_map: dict) -> dict:
        """Creates a network of managers from data.

        Args:
            gardens_map (dict): Dictionary mapping owners to plant lists.

        Returns:
            dict: Dictionary of GardenManager instances.
        """
        network = {}
        for owner in gardens_map:
            plants = gardens_map[owner]
            new_garden = Garden(owner, plants)
            network[owner] = cls(new_garden)
        return network

    create_garden_network = classmethod(create_garden_network)

    def validate_height(val: int) -> bool:
        """Utility function to validate height.

        Args:
            val (int): Height to validate.

        Returns:
            bool: True if height is positive.
        """
        return val > 0

    validate_height = staticmethod(validate_height)

    def generate_report(self) -> int:
        """Generates a detailed report and returns the score.

        Returns:
            int: The garden's total score.
        """
        print(f"=== {self.garden.owner}'s Garden Report ===")
        print("Plants in garden:")

        reg_count = 0
        flow_count = 0
        prize_count = 0
        total_count = 0

        for p in self.garden.plants:
            print(f"- {p}")
            total_count += 1
            if p._kind == "prize":
                prize_count += 1
            elif p._kind == "flowering":
                flow_count += 1
            else:
                reg_count += 1

        score = GardenManager.GardenStats.calculate_score(self.garden.plants)
        print(
            f"\nPlants added: {total_count}, "
            f"Total growth: {self.garden.total_growth_applied}cm"
        )
        print(
            f"Plant types: {reg_count} regular, "
            f"{flow_count} flowering, {prize_count} prize flowers"
        )
        return score


def main() -> None:
    """Main execution flow for the demo."""
    print("=== Garden Management System Demo ===\n")

    initial_data = {
        "Alice": [],
        "Bob": [Plant("Small Tree", 82)]
    }

    network = GardenManager.create_garden_network(initial_data)
    alice_mgr = network["Alice"]

    alice_mgr.garden.add_plant(Plant("Oak Tree", 100))
    alice_mgr.garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_mgr.garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()

    alice_mgr.garden.help_growth(1)
    print()

    alice_mgr.generate_report()
    print()

    is_valid = GardenManager.validate_height(alice_mgr.garden.plants[0].height)
    print(f"Height validation test: {is_valid}")

    output_str = "Garden scores -"
    first = True
    for owner in network:
        mgr = network[owner]
        s = GardenManager.GardenStats.calculate_score(mgr.garden.plants)
        if not first:
            output_str += ","
        output_str += f" {owner}: {s}"
        first = False

    print(output_str)
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
