**Notes:**

1. This problem asks us to find the max profit we can get, if we have the value of stock at each day. Selling day is always in future.
2. For this, we keep a left pointer and a right pointer. We have a variable that tracks the max profit. We can intialize it zero as default value.
3. We start a for loop where right pointer starts from 1 until the end of the prices list.
4. We check if the price at L pointer is greater than or equal to price at R pointer. It means price of the stock is higher on the selling day and buying day has a lesser stock price. This transaction is not profitable. We bring our left pointer to the right pointer. Basically making the day with lesser stock price a selling day.
5. If price at L pointer is smaller than price at R pointer. We calculate the profit by subtracting the price at R pointer with the price at L pointer. Then we update the max profit.
6. Return the max profit.
