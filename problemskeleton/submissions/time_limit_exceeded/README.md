# Deliverable 3
Incorrect or Inefficient Solution
## What is the time and space complexity of this solution? 
# Time Complexity
python sorted() uses Timsort
O(nlogn)
# Space Complexity
O(n) for nb pieces

## Why is this solution incorrect or inefficient? 
This solution is inefficient because it uses sorted() which is O(nlogn) > O(n+m) counting sort

## How many test cases does it fail, and why? 
It would failed in test cases where n is large and range of m (serial number) is small

## How does its performance compare to the correct solution? 
Expected Time for n=1,000,000, M=10,000

Counting Sort
O(n + M)
~1,010,000 iterations

Python sorted()
O(n log n)
~20,000,000 operations -> may not pass

## Does the solution fail in all three programming languages?

Python is most likely to fails. For C++/Java it may pass but if we add more difference to n and m it would fail.