**Notes:**

1. The problem requires us to encode a list of words into a single string. Then decode the string back into original list of words.
2. It's easy to concatenate the words into a single string. But the task is to figure out the delimeter between the words that helps us in decoding the single string back to original list of words.
3. If we use a # between word. We are good in most scenarios but the # can appear in between the words. For example code#hash is one word. But our decoding algorithm has no way knowing that its one word. It will always be decoded as two words.
4. So the next thing that can be used is the length of word as interger. But if we put the length at the start of the string, we still need a delimeter to differntiate between the start of the word and the length integer. So its best to combine the word length integer and # as delimeter between the words.
5. Pro Tip: In decoding, maintain pointers to extract the length interger. Alos make use of while loop instead of for loop. While loop is cleaner and is easier to maintain pointers.
