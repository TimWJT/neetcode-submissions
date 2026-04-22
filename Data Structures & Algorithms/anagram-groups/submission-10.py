class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            sortedS = ''.join(sorted(s))
            
            # If key doesn't exist, create an empty list
            if sortedS not in res:
                res[sortedS] = []
            
            # Append the original word to the list
            res[sortedS].append(s)
        
        # Return all the lists (values) as a list
        return list(res.values())

        # new_strs = strs[:]
        # output = []
        # checked_set = set()

        # for i, s in enumerate(new_strs):
        #     new_strs[i] = sorted(s)
        
        # for i, s in enumerate(new_strs):
        #     if strs[i] in checked_set:
        #         continue


        #     anagram_group = []
        #     checked_set.add(strs[i])
        #     for j, other_s in enumerate(new_strs):

        #         if len(strs[i]) != len(strs[j]):
        #             continue

        #         if s == other_s:
        #             checked_set.add(strs[j])
        #             anagram_group.append(strs[j])
        
        #     output.append(anagram_group)
        
        # return output