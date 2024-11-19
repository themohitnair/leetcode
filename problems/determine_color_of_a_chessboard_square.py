from typing import Dict

class Solution:
    files: Dict[str, int] = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }
    ranks: List[str] = [str(i) for i in range(1, 9)]
    def squareIsWhite(self, coordinates: str) -> bool:
        if (self.files[coordinates[0]] + int(coordinates[1]) - 1) % 2 == 0:
            return False
        return True