import sys

class Solution:
    stack = []
    queue = []
    
    def pushCharacter(self, c: str):
        self.stack.append(c)
        
    def enqueueCharacter(self, c: str):
        self.queue.append(c)
        
    def popCharacter(self) -> str:
        return self.stack.pop(-1)
        
    def dequeueCharacter(self) -> str:
        return self.queue.pop(0)

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    