class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # whenever an item doesn't exist in the dict,
        # make an empty list for it
        res = defaultdict(list)
        for s in strs:
            # create a list with 26 zeros for each letter
            # in the alphabet
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # since in python lists can't be keys, turn it into a tuple cause it's non-changeable
            res[tuple(count)].append(s)
        # we don't want the keys, just the values of the dict
        return list(res.values())