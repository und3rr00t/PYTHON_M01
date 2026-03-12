class SecurePlant:
    """Represents a protected plant with validated data."""

    def __init__(self, name: str) -> None:
        """Initializes a plant with a name and default values.

        Args:
            name: The name of the plant.
        """
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, height: int) -> None:
        """Sets the height safely. Prints error on negatives.

        Args:
            height: Target height in cm.
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def get_height(self) -> int:
        """Gets the validated height.

        Returns:
            int: The height in cm.
        """
        return self.__height

    def set_age(self, age: int) -> None:
        """Sets the age safely. Prints error on negatives.

        Args:
            age: Target age in days.
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_age(self) -> int:
        """Gets the validated age.

        Returns:
            int: The age in days.
        """
        return self.__age

    def display(self) -> None:
        """Displays the current secure metrics for the plant."""
        print(f"Current plant: {self.name} "
              f"({self.__height}cm, {self.__age} days)")


def main() -> None:
    """Entry point to test secure plant encapsulation mechanics."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")

    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print()

    plant.display()


if __name__ == "__main__":
    main()
