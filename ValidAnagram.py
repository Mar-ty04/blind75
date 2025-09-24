class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #create a hashset
        hashset = set()

        #iterate through the list
        for n in nums:

            #check if the element is already in the list (aka our hashset), if so return true 
            if n in hashset:
                return True

            #if not in hashset yet then add it 

            hashset.add(n)
        
        #if broken out of for loop then no duplicates, return false. 
        return False
