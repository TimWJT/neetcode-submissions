class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = 1
        while i < len(s) and j < len(s):
            print("i: " + s[i])
            print("j: " + s[-j])
            
    

            while not s[-j].isalnum():
                j+=1
                if j > len(s):
                    return True

            while not s[i].isalnum():
                i+=1
                

            if s[i].upper() != s[-j].upper():
                
                return False

            i +=1
            j+=1
        return True