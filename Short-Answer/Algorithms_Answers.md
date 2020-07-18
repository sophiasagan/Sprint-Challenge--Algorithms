#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - linear - function is dependent on loops through n


b) O(n^2) - quadratic - nested loops - outer loop is performing n iterations and inner loop is performing n iterations for every iteration of of the outer loop - i.e. (n*n) == (n^2)


c) O(n) - linear - recursive - function is dependent on loops through n('bunnies')

## Exercise II

a. Suppose that you have an n-story building and plenty of eggs. 
    * building_level = n
    * eggs = 
b. Suppose also that an egg gets broken if it is thrown off floor f or higher, 
    * if floor >= f:
        break
c. and doesn't get broken if dropped off a floor less than floor f. 
    * if floor < f:
        survive

Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Option 1: (iterative)
    + start at bottom floor and work your way up until find the floor that breaks eggs
    or
    + start at top floor and work your way down until eggs don't break

Option 2: (recursive)
    + start with middle floor if egg breaks go down halfway of remaining bottom floors, if egg doesn't break go up halfway of remaining top floors

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Iterative Option:
eggs = all # initialize eggs
building_level = len(f) # set building length number of possible floors
egg_drop = egg # egg for iteration
start egg_drop f[0]:
    if survives:
        f += 1
        (egg is still reusable)
    if breaks:
        eggs -= 1
        return eggs
return f[n]

Recursive Option: (binary search) BEST METHOD
floor_egg_breaker(f, low, high):
    if f < 0:
        return none # can't drop from basement
    if f >= 1:
        find mid_floor_of_floors = low + high // 2
        drop egg
        if survives:
            low = current floor
            recursive call
        if breaks:
            high = current floor
            recursive call
        if f = (mid == low == high):
            return [f]

* Runtime:
    O(logn) - binary search - recursive function, search is divided in half each iteration vs going floor by floor. 
    + also minimizes eggs broken especially if it's a tall building 

