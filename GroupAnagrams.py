class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #mapping char count to list of anagrams
        res = defaultdict(list)

        for s in strs:
            #a...z
            count = [0] * 26

            for c in s:
                #using ASCII Values
                count[ord(c) - ord("a")] += 1

            #append string s to the res
            #use tuple because to make it immutable
            res[tuple(count)].append(s)
        
        return list(res.values())
