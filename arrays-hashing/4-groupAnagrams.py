class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}

        # iterate over the input
        for str in strs:
            # sort each string
            tmp = ''.join(sorted(str))
            # check if the sorted string exists in the dictionary
            if tmp in dict.keys(): dict[tmp].append(str)
            else: dict[tmp] = [str]

        result = []
        # iterate over each sorted string
        for key in dict.keys():
            result.append(dict[key])

        return result