**Notes:**

1. The problem asks us to find the whether the given number is a happy number or not. A given number is a happy number if the sum of squares of it's digits ever becomes equal to 1. We have to keep on summing the squares of the digits, starting from the inputs endlessly until we have reduced the number to 1. If the number cannot be reduced to 1 this way then we will return False.
2. If we reach a 1 in the loop we will return True, but what happens if we are unable to reach 1, how we are going to determine that the given number is not a happy number. Let's dry run this mathematical problem to understand both the cases, so we know how to terminate the loop.
3. Example for happy number. Termination condition is whenever the input is reduced to 1.

   ```
   input = 19

   1^2 + 9^2 	= 82
   8^2 + 2^2 	= 68
   6^2 + 8^2	= 100
   1^2 + 0^2 + 0^2	= 1

   ```
4. Example for an unhappy number. We will run into a cycle if we cant reduce the input with given algorithm to 1. So in order to detect cycles, we can use a hashset, if we have already seen a value then we will terminate the loop and return False.

   ```
   input = 2

   2^2		= 4 #repeated
   4^2		= 16
   1^2 + 6^2	= 37
   3^2 + 7^2	= 58
   5^2 + 8^2	= 89
   8^2 + 9^2 	= 145
   1^2 + 4^2 + 5^2	= 42
   4^2 + 2^2	= 20
   2^2 + 0^2 	= 4 #repeated

   ```
5. Now with that sorted out, we have one more thing to do. How to get the sum of squares of the digits. We will have to separate the digits, square them and add them up. This will be our updated input. For this we will have to make a helper function that sums up the square of digits. We can use it as the updated input (reduced input) in our primary loop. Let's how we can sum the squared digits of 145.

   ```
   n = 145

   145 % 10 = 5 => #last digit => output = 5^2
   n = 145 // 10 = 14 #remaining 2 digits
   14 % 10  = 4 => #last digit => output = 5^2 + 4^2
   n = 14 // 10 = 1 #remaining 1 digit 
   1 % 10.  = 1 => last digit  => output = 5^2 + 4^2 + 1^2
   n = 1 // 10 = 0

   Since n becomes zero we have successfully computed the sum of squared digits for 145
   ```
