**Notes:**

1. The problem asks us to find the sum of intergers (negative and postive) without using the "+" operator.
2. The problem clearly states that we cannot use the + operator, which mean the only other way to arrive at the solution is to perform bit manipulation.
3. Python is not the best language for the bit manipulation of negative numbers in some cases, and this problem is basically one of those cases. The given problem can be solved in Java with the actual algorithm but in python we have to do some extra operations to get the desired results. Here i will implement the python code with those operations and here I will only discuss how this problem can be solved logic wise.
4. So we have two numbers and we need to add them using bit operations only. We know in normal addition when we go to or over 10 adding two digits. The 10's place becomes a carry over.
5. Here in bit manipulation we are working with base 2. So whenever we 1 + 1, we will have a carry over 1 and 1 + 1 = 0. Then on the left of this 0 we add the carry over 1. So the total of adding 1 + 1 in binary is equal to 1+1 = 10. So now the question is how we can achieve this for this problem, which combination of bit operations we can use to have the similar results.
6. The first step of adding 1 + 1 = 0, can be replaced by the use of XOR operation. Why because:

   ```
   1 + 1 = 0 #simple addition in base 2 
   1 ^ 1 = 0 # xor operation
   1 + 0 = 1
   1 ^ 0 = 1
   0 + 1 = 1
   0 ^ 1 = 1
   0 + 0 = 0
   0 ^ 0 = 0
   ```
7. The second step is the carry over, carry over always goes to the left, so basically from the two orignal numbers a and b, we have to find out the carry overs and then shift those to the left. In the example of 1 + 1, the carry over is 1. So which operation can let us know about the carry over. Its the AND operator, that figures out thr carry over. So whenever we try to add the bits 1. like 1 + 1. If we AND 1 & 1 = 1. which is the carry over and we shift it to left as well by 1. So it will (1 & 1) << 1. This will help us place the carry overs at the right spot, then we have to add these new numbers again by XOR and find out the carry over for the second turn of addition. And we will keep on going in the loop till our carry over becomes zero. I will demonstrate this here with an example.

   ```
   #Adding 9, 11 => 20 should be the answer.
   9 =>  a1 => 		1001
   11 => b1 =>		1011
    	a2 => 	       00010	(a1 ^ b1)
   	b2 =>	       10010	(a1 & b1) << 1 	(carry overs)
   	a3 => 	       10000	(a2 ^ b2)  	(xor addition)
   	b3 => 	      000100	(a2 & b2) << 1 	(carry overs)
   	a4 => 	      010100  	(a3 ^ b3) 	(xor addition)
   	b4 => 	     0000000	(a4 & b4) << 1 	(carry overs)

   #since carry overs in b4 are 0 now, a4 is our result of addition. a4 = 10100 = 20
   ```
8. Python implementation of this problem is a needs us to convert the numbers in to 32 bit interger, python only support 64 bit integers by default. So at each step of the algorithm we have to make sure we convert the result of each operation into 32 bit operation and also then convert it back to the 64 bit intergers. Read the following comment by @sysy2152 for better understanding.

To explain, the hexadecimal number 0xffffffff is the same as the binary number 0b1111111111111111111111111111111, containing 32 1's. (It's just easier to type lol.)

In order to make the code work like Java, we want to treat our numbers like they only have 32 bits. ANDing a number with the mask 0xffffffff, or 32 1's, basically turns all of a number's bits into 0's except for the rightmost 32. As a result, the number can be represented as if it only has 32 bits.

We do what Neetcode describes in his video, using XOR for the sum and AND for the carry. We AND with the mask each time we set a and b in order to keep our numbers within 32 bits.

After we exit the while loop, we have our answer a. If a is positive, then we can return it directly. However, in Python, negative numbers are represented in binary as having an unlimited number of leading 1's. The current answer would only have values in the rightmost 32 bits. Therefore, if the answer is negative, we need to convert it into Python's representation of negative numbers.

First, we need to check if the answer is negative. We cannot just check to see if the answer is less than zero because our representation of the answer is not the same as Python's (since Python's have unlimited leading 1's). We are still treating our answer as if it only fits into 32 bits.

A 32-bit signed integer is positive if the 32nd bit is a 0 and is negative if the 32nd bit is a 1. If we divide our mask (0xffffffff) by 2, we will get the binary number 0b0111111111111111111111111111111, which has 31 1's. This number is the greatest value we can have before the 32nd bit becomes a 1. Therefore, if our answer a > mask // 2, it is negative. Otherwise, it is positive and we can just return a itself.

If the number is negative, we then need to convert it into Python's representation of negative numbers. To do so, we can XOR with the mask of 32 1's in order to flip the rightmost 32 bits, since XORing a bit with 1 flips the bit. We can then NOT the number in order to turn all of the leading 0's into 1's. For example, say that the answer is -3, and (....0000000) or (....1111111) denote leading 0's or 1's until the 32nd bit:

Our representation of -3 in 32 bits: (...0000000)11111111111111111111111111111101
XOR with mask, aka flip rightmost 32 bits: (...0000000)00000000000000000000000000000010
NOT, aka flipping all bits: (...1111111)1111111111111111111111111111101
The result is Python's representation of -3, including an unlimited number of leading 1's.

Overall, the code uses the same process as Neetcode's Java code, but with masking to get numbers into 32 bits and some manipulation to get those 32-bit numbers back into Python's representation before returning.
