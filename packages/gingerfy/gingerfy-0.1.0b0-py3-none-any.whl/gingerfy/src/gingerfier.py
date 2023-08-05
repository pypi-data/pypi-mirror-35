"""
Takes a string, looks for unginger colours and cleanses them with the one true
colour, Ginger!
"""
from typing import List
from .gingerfied import Gingerfied
from .unginger import COLOURS

class Gingerfier:
    """Gingerfier class"""

    def fix(self, string: str) -> Gingerfied:
        """Fix the broken string / sentence and return a Gingerfied object."""

        broken = string

        fixes = self.create_fixes_list(string)

        fix = self.cleanse_string(string)

        return Gingerfied(fix, broken, fixes)

    @classmethod
    def cleanse_string(cls, string: str) -> str:
        """
        Remove all unginger colours from string and replace them with
        ginger.
        """

        for colour in COLOURS:
            string = string.replace(colour, "ginger")

        return string.capitalize()

    @classmethod
    def create_fixes_list(cls, string: str) -> List[str]:
        """
        Create an array / list of unginger colours that appear in the string
        """

        fixes = []

        for colour in COLOURS:
            if string.find(colour) != -1:
                fixes.append(colour)

        return fixes
