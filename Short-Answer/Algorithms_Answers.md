# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

a) `O(n)` because it will only ever go as high as "a" so the n^3 does not affect the time complexity.

```
b)  sum = 0
    for i in range(n): # O(n)
      i += 1
      for j in range(i + 1, n): # O(n)
        j += 1
        for k in range(j + 1, n): # O(n)
          k += 1
          for l in range(k + 1, 10 + k): # O(1)
            l += 1
            sum += 1
```

b) `n^3` This looks like three nested loops running each at O(n) and the last one running O(1) because it looks like the constants are only 10 apart.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

c) looks like `O(n)` since it is doing a simple recursion that calls itself once per loop until it hits zero, and it doesn't do anything complicated in the recursion. Probally could use a simple for loop here tbh.

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

I can essentially start in the middle of the building n/2 and see if it breaks. If it breaks, I go halfway between the floor I am on right now and the ground floor. If not, then I know for a fact that I must go higher. I drop the egg again and test it another time using the same logic, just at a different levl which will depend on if the egg breaks or not.

Throw egg on middle floor of building (n/2)
if egg breaks then throw in the middle of where it broke and the floor so n/2 again
if not, then throw in the middle of where it didn't break and the top floor so (n-currFloor)/2
cut floors in half each time until you arrive at the answer.

This would be `O(log n)` time complexity because it is cutting n in half each time it runs