"""
A Domain Name System (DNS) translates domain names to IP addresses 
which are then used by browsers to load internet resources. 
For quicker DNS lookups, browsers often store a number of recent DNS 
queries in a DNS cache. Retrieving data from the cache is often 
faster than retrieving it from a DNS server. 
This task aims to simulate DNS resolution and determine 
the time taken to process different URLs.
Assume that the DNS cache can store a maximum of the cache_size most 
recent DNS requests, i.e., URL-IP mappings. 
The cache is initially empty. It takes cache_time units of time to 
fetch data from the DNS cache, and server_time units of time to 
fetch data from the DNS server.
Given a list of n URLS visited as an array of string urls, 
determine the minimum time taken to resolve each DNS request.
Note: New DNS requests are dynamically added to the cache stores mappings
accoriding to the order in which the requests were made.

Example:
Input
cache_size = 2
cache_time = 2
server_time = 3
urls = ['www.google.com', 'www.yahoo.com', 'www.google.com', 'www.yahoo.com', 'www.coursera.com']

Output:
[3, 3, 2, 2, 3]
"""

from collections import deque


def getMinTime(cache_size:int, cache_time:int, server_time:int, urls):
    cache = deque()
    res = []

    for url in urls:
        if url in cache:
            res.append(cache_time)
        else:
            if len(cache) >= cache_size:
                cache.popleft()
            res.append(server_time)
            cache.append(url)
    
    return res

print("Test Case 1:", getMinTime(2,2,3,['www.google.com', 'www.yahoo.com', 'www.google.com', 'www.yahoo.com', 'www.coursera.com']))







