class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        nums = sorted(nums)
        
        print(nums)

        previous_n = None

        for index, n in enumerate(nums):

            print("previous: " + str(previous_n))
            print("n: " + str(n))
            if n == previous_n:
                print("skipping")
                continue
            previous_n = n

            left = index
            right = len(nums) - 1

            print(index)

            while left < len(nums) and right > index and left < right:
                if left == index:
                    left +=1
                    continue

                if right == index:
                    right -=1
                    continue
                


                if nums[left] + nums[right] == -n:
                    output.append([n, nums[left], nums[right]])
                    
                    print("appending: "+ str([n, nums[left], nums[right]]))

                    while left < len(nums)-1 and nums[left] == nums[left + 1]:
                        left +=1
                    while right > index and nums[right] == nums[right - 1]:
                        right -=1

                    left += 1
                    right -= 1 

                else:

                    if nums[left] + nums[right] < -n:
                        left +=1
                    else:
                        right -=1
                

        # print(index)
        return output

                
                
