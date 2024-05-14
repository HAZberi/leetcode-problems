**Notes:**

1. The most important thing for this problem is to thoroghly understand the problem. There is a one lane road, cars cannot ovetake. The faster cars can only catch up to the cars in front of them. One the faster car catches up to slower car, they both travel at the same speed (slower speed) to the target. At this point we have a fleet because the two cars reach at the target at the same time. So we need to find how many these fleets are there.
2. The best way to explain the catching up of cars is by drawing a 2-D plot, where position is on y-axis and time on x-axis. The slope is the speed of travel. The important formula here to remember is `time = distance / speed`.  Basically on the x-axis we have time to target. We can get the time to target by taking the difference between target and the positon, then divide it by the corresponding speed at this postion. We will see that once a car catches up it follows the car in front of it at same speed.
3. Position of cars is given and also the speed of cars at a corresponding index in a seprate list.
4. There is one important thing to notice here that the order of position is important because the car that is closest to the target, is catched up by all the faster cars that are on the left or behind it. Clearly, this indicates that we need to sort the positions here. That way, we for sure know that all the cars on the left can catch up to the cars on the right if they are faster.
5. ProTip: Zip the position and speed lists and then sort the zipped list. This operation will be O(nlogn). By doing this we will have access to position and speed in the same list.
6. We also need a stack here where we will add time to targets.
7. It is important that we should loop the zipped list in reverse, because the last value is closest to the target. All the faster cars eventually catchup to this closest to the target car or this car will reach the destionation first and can be considered a fleet.
8. In the reverse loop we calculate the time to target and put it on to the stack.
9. If stack has two values and time to target of last added car is less than the time to target of the second last car then we pop out from stack. This operation will be done for each value in each iteration.
10. Return the lenght of stack.
