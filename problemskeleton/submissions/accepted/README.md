# Deliverable 2
Correct and Efficient Solution
## What is the time and space complexity of your solution?
### Time Complexity: O(n+m)
1. Find max_serial -> O(n)
2. Count freq -> O(n)
3. Compute prefix sums (in reverse) -> O(max_serial)
4. Build output array -> O(n)
Tot Time Complexity
n = len(serial_numbers)
m = max_serial + 1
O(n + m)
Since max_serial <= 10,000, so for n approx 1 000 000, it behaves like O(n) in practice.

### Space Complexity: O(n+m)
countArr -> size max_serial + 1 -> O(max_serial)
sorted_serials -> size n -> O(n)
Tot Space Complexity
O(n + m)
Since max_serial <= 10,000, so for n approx 1 000 000, it behaves like O(n) in practice.

## Could a more efficient solution be implemented?
It generally performs faster than all others comparison.
Not so efficient if range to be sorted is too large.
But in our case with 10000 it is the optimal one.


## Could a less efficient solution still pass the test cases?
No, other comparison that is O(nlogn) or O(n^2) would not pass when the test cases is a "stress cases".
When n approx = 1 000 000 and m max number is very small (range from 0 in our case), it is almost O(n).

## Which of the three programming languages performed best?
C++ -> Python -> Java

## Which language was most suitable for implementing your solution, and why?
C++
Counting sort properties:
1. Contiguous arrays for countArr or sorted_serials
vector<int> stores them contiguously in memory so is faster to access it.

In general C++ is compiled directly to machine instruct and loops over int fast

So C++ is better mainly because it accesses memory directly and efficiently for n and M elements.

## What are the best-case and worst-case scenarios for your solution?
### Best-case
small range of numbers from 0 -> so when all numbers is same and is near 0.
and nb of test cases
### Worst-case
when M is very large: large range of numbers
numbers range from 0 to 10 000 -> M = 10 0001
if M is huge compared to n (ex: n = 10, M = 1000 000), counting sort inefficient
but still O(n+M), now M dominating.