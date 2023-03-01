from enum import Enum


class MapsIndex(Enum):
    EMPTY = "empty_room"
    EMPTY_LARGE = "empty_room_large"
    FOUR_ROOMS = "four_rooms"
    HARD = "hard_maze"
    MEDIUM = "medium_maze"
    EXTREME = "extreme_maze"
    IMPOSSIBLE = "impossible_maze"


class TileType(Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    REWARD = 3
