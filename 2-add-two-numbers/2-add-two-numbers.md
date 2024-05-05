**Notes:**

1. The most important thing to remember solving this problem is elementary style addition. where we start adding the two single digits. If their sum is greater than 10, we put a single digit unit's place and the digit at Ten's place is the carry over to the next set of adding two single digits. Then if there is a carry over, we add the sum of two digits and the carry over. Then repeat the same procedure.
2. The one good thing is that our linklists are already reveresed. So we just need to loop over both list and starting adding nodes, which are basically digits.
3. There are three most important things to keep in mind solving this problem. Carry over, if there is no node to add in one list but the other list has a node and if the last two digiits that we added has a remaining carry over.
4. Carry over, we initiate the carry over variable before our while loop and then we keep on updating the carry over each time we add two nodes/digits. For the carry over update, we divide the sum of three by 10 via integer division. For unit's place value we take the mod of value by 10. This gives the unit's place. Then we add this units place value to our resultant linklist.
5. If there are no node to add in one list. We assume its value to be zero, since that would not effect the addition. No node to add situation will arise when the list is at the end.
6. if there are no nodes to add in both the list. But there might be a carry on left over to add. From both the nodes value will be zero we will just add the carry over to the new node.
7. We start the resultant list with a dummy node, we keep on adding nodes to this list til there are no nodes and carry over to add.
8. Return dummy.next
