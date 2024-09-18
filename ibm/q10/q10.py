"""

There is a shop with old-style cash registers. 
Rather than scanning items and pulling the price from a database, 
the price of each item is typed in manually. This method sometimes 
leads to errors. Given a list of items and their correct prices, 
compare the prices to those entered when each item was sold. 
Determine the number of errors in selling prices.
Example
products = ['eggs', 'milk', 'cheese']
productPrices = [2.89, 3.29, 5.79]
productSold = ['eggs', 'eggs', 'cheese', 'milk']
soldPrice = [2.89, 2.99, 5.97, 3.29].

Product ActualPrice Expected    Error
eggs    2.89        2.89
eggs    2.99        2.89        1
cheese  5.97        5.79        1
milk    3.29        3.29
The second sale of eggs has a wrong price, as does the sale of cheese. 
There are 2 errors in pricing.
Function Description
Complete the function priceCheck in the editor below.
"""

from typing import List


def priceCheck(products:List[str], productPrices:List[float], productSold:List[str], soldPrice:List[float]):
    res = 0

    productMap = {}
    for i in range(len(products)):
        productMap[products[i]] = productPrices[i]
    
    for j in range(len(productSold)):
        p = productSold[j]
        if p in productMap and productMap[p] != soldPrice[j]:
            res += 1
    
    return res

#Test Cases 
print("Test Case 1:", priceCheck(['eggs', 'milk', 'cheese'], [2.89, 3.29, 5.79], ['eggs','eggs', 'cheese', 'milk'], [2.89,2.99,5.97,3.29]))






