class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        e = {}
        # loop through the string and add each char to the dict.
        # if its not there already, get() counts it as 0
        # and then increments the count by 1
        for letter in s:
            d[letter] = d.get(letter,0) + 1
        for letter in t:
            e[letter] = e.get(letter,0) + 1
        if d == e:
            return True
        else:
            return False