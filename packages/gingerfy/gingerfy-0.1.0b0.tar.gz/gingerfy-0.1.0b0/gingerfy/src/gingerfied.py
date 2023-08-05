"""
Generated object for gingerfy module defines new fixed string, old unginger
string and the fixes that have been made.
"""
from typing import List

class Gingerfied:
    """Gingerfied class"""

    def __init__(self, fix: str, broken: str, fixes: List[str]) -> None:
        """
        Constructor: consumes and sets fixed sentence, the old broken sentence
        and an array of the fixes.
        """

        self.fix = fix
        self.broken = broken
        self.fixes = fixes

    def get_fix(self) -> str:
        """Get the fixed sentence"""

        return self.fix

    def get_broken(self) -> str:
        """Get the original broken sentence"""

        return self.broken

    def get_fixes(self) -> List[str]:
        """Get the array of fixes made"""

        return self.fixes
