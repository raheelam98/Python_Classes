# leed code 9. palindrome number

### palindrome:- any number or a string which remains unaltered when reversed.

### 1- Palindrome Program using While Loop
num=int(input("Enter a number1:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

### 2 - Palindrome Program( String) using inbuilt Method   
    
string=input(("Enter a string2:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")    

#  slice operation [start:end:step]
# Explanation: In the above program, first take input from the user
# (using input OR raw_input() method) to check for palindrome.
# Then using slice operation [start:end:step], check whether 
# the string is reversed or not. Here, step value of -1 reverses a string. 
# If yes, it prints a palindrome else, not a palindrome.      
      
# https://medium.com/@luckyudbhav/9-palindrome-number-leetcode-solution-abd0d3c4f59c      

### PROBLEM : CHECK IMPORTAN
##  how call class function and take input
### to  call the function of the class and take user input, 
### you can create an instance of the class and call the method on that instance.                          

class Solution(object):
    def isPalindrome(self, x):
        ## not here:-  temp=int(input("Enter a number1:"))
        """
        :type x: int
        :rtype: bool
        """
        # If the input number is negative, it's not a palindrome
        if(x<0):
            return False 
        
        # If the input number is a single digit (between 0 and 9), it's a palindrome
        if(x>=0 and x<10):
            return True 
        
        # Initialize a temporary variable to store the value of x for processing
        temp=x

        # Initialize a variable to store the reversed number
        k=0

         # Loop until temp becomes 0
        while(temp>0):
            # Reverse the number by adding the last digit of temp to k
            # and removing the last digit from temp
            k = (k*10)+temp%10
            temp = temp//10
        
        #return (k==x) 
        # Return True if the reversed number is equal to the original number
        # Otherwise, return False    
        if(k==x):
            print("The number is palindrome!")
        else:
            print("Not a palindrome!") 

# create an instance of the class
solution = Solution()

# take user input
num = int(input("Enter a number3: "))

# call the method on the instance
solution.isPalindrome(num)
