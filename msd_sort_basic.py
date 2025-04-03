from typing import List

class MSDSortBasic:
    """
    Basic implementation of MSD (Most Significant Digit) sorting for strings.
    
    This implementation focuses on the key-indexed counting aspect of MSD sort
    by sorting strings based on a single character position.
    It's a simplified version that demonstrates the counting technique without recursion.
    """
    
    # ASCII range
    R = 256
    
    def __init__(self):
        """Initialize a new MSDSortBasic instance."""
        self.accesses = 0
    
    def _char_at(self, s: str, d: int) -> int:
        """
        Get the character at position d in string s, or -1 if d is past the end.
        
        Args:
            s: The string to examine
            d: The position to check
            
        Returns:
            The integer value of the character at position d, or -1 if d >= len(s)
        """
        self.accesses += 1
        if d < len(s):
            return ord(s[d])
        return -1
    
    def sort_by_position(self, arr: List[str], d: int) -> None:
        n = len(arr)
        if n <= 1:
            return

        count = [0] * (self.R + 2)  # Room for -1 to 255 (shifted)

        # Step 1: Frequency counts
        for s in arr:
            c = self._char_at(s, d) + 1
            count[c + 1] += 1

        # Step 2: Cumulative counts
        for r in range(self.R + 1):
            count[r + 1] += count[r]

        # Step 3: Distribute (stable)
        aux = [None] * n
        for s in arr:
            c = self._char_at(s, d) + 1
            aux[count[c]] = s
            count[c] += 1

        # Step 4: Copy back
        for i in range(n):
            arr[i] = aux[i]


    def is_sorted_by_position(self, arr: List[str], d: int) -> bool:
        """
        Check if the array is sorted by the character at position d.
        
        Args:
            arr: The array to check
            d: The position to check
            
        Returns:
            True if the array is sorted by position d, False otherwise
        """
        for i in range(1, len(arr)):
            if self._char_at(arr[i], d) < self._char_at(arr[i-1], d):
                return False
        return True