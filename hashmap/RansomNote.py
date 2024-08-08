class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # m is the number of characters in magazine and n is # of characters in ransomNote
        # Time: O(m+n)
        # Space: O(m)

        occurances = {}

        for letter in magazine:
            if letter not in occurances:
                occurances[letter] = 1
            else:
                occurances[letter] += 1
            
        for letter in ransomNote:
            if letter in occurances and occurances[letter] > 0:
                occurances[letter] -= 1
            else:
                return False
                
        return True