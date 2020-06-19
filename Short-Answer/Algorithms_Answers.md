#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n): Directly takes in the input size, and runs only one while loop, returning a math operation

b) O(n^2)... It iterates, and a nested iteration so it does both loopps, comparing it against two lists

c) O(n): Single operant, and based on input

## Exercise II

#what we know:
#building is n tall
#egg breaks at floor f
#currently on floor x

#so, we have to start at floor 1 n[x]):
#continue dropping egg at each floor (n[x] + 1)
#until we reach floor f

#or, we could use a binary search, by starting in the middle
#middle = n / 2

    #seeing if the egg has already broke?
        #middle = middle / 2
      #if true, go down
      #if false, go up
      #return target floor

I'd say run time would be O(n), but if using Binary, we're able to slow it down to O(logn)
