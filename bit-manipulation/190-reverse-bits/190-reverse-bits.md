**Notes:**

1. The problem asks us to reverse all the bits of a given unsigned interger. So if we have a 4, its binary representation is 000..00100 in 32 bits. We reverse it to 00100.....000. Note that both the numbers are actually different.
2. Most of the bit manipulation programs are solver by AND OR XOR and bit shifting. Similar concepts can be applied here to reverse the bits.
3. What we are looking to do is to take the 1's place bit from the input and place it in the 31st place in the resultant number. And keep doing that for all the 32 bits. The question is how can we get the bit of 1's, 2's .... 31st place single bit from the input? If we shift the input number by 1 to the right and take the AND with 1. We will have the bit. Similarly if shift the input number to the right by i and take the AND with 1, we get the ith bit of the input number.
4. Now we have to take this bit and add it to our result but in reverse. How we are suppose to do that? Since we want the first bit, the bit at 0th index to be placed at the 31st index of the result. We initialize the result to 0. To get the 31 index bit, we have to take the current bit which can be either 0 or 1 and shift it to the left 31 times, similarly if take the current bit and shift to the left (31 - i), so the bit will be placed at 31 - i bit location. This is that we have found the currect location of the bit, but how we update the result? We take OR of this bit number and the result. If this bit is zero, then the result will remain the same, if this bit is one then the bit location in result will be changed to 1.
5. After that we can simply return the result.