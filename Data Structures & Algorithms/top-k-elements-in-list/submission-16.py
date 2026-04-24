class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        res = {}
        output = []
        
        for n in nums:
            
            if n not in res:
                res[n] = 0
            
            res[n] +=1
        
        arr = []
        for number, frequency in res.items():
            arr.append([frequency, number])

        arr.sort()
        
        i = 0
        while i < k:
            _, number = arr[-(i+1)]
            output.append(number)
            i+=1
        

        
        return output

        # sort res by value
        # then 