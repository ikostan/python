"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """
    Alien located at given coordinates.

    Attributes
    ----------
    (class)
    total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object
                                                  to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created: int = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        """
        Initialize a new Alien at the provided coordinates.

        Sets health to 3, assigns x and y coordinates, and increments
        Alien.total_aliens_created.

        :param x_coordinate: Position on the x-axis.
        :param y_coordinate: Position on the y-axis.
        :return: None
        """
        self.health: int = 3
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1

    def is_alive(self):
        """
        Return whether the alien is alive.

        :return: True if health > 0, else False.
        """
        return self.health > 0

    def hit(self):
        """
        Decrement the alien's health by one point.

        :return: None
        """
        self.health -= 1

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """
        Decrement the alien's health by one point.

        :return: None
        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """
        Determine whether this Alien collides with another.

        Implementation TBD; currently returns None.

        :param other: Another Alien or object to check for
                      positional overlap.
        :return: None

        `Source: /ellens-alien-game/classes_test.py`
        """
        pass  # pylint: disable=unnecessary-pass


def new_aliens_collection(
    alien_start_positions: list[tuple[int, int]],
) -> list:
    """
    Create a list of Alien objects from starting positions.

    :param alien_start_positions: given a list of positions
    :return: a list of Alien() objects
    """
    return list(Alien(pos[0], pos[1]) for pos in alien_start_positions)
