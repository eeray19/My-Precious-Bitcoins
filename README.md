# My-Precious-Bitcoins

# To DO:

- [x] The algorithm you designed to solve the problem, the choices of the data structures you used and your reasoning.
- [x] In addition to your actual code, write a pseudo code for your algorithm
- [ ] Compare it with another algorithmic approaches
- [x] The time complexity of your algorithm (and the space complexity if applicable)
- [x] Prove that your algorithms gives correct results
- [ ] Further improvements that can be done as future works.


TO DO List:
  Take an integer input "n" for representing the sum of x, y and z.
  Keep a counter integer for counting the number of candidates.
  Come up with a method to find optimal combinations of x, y and z.
  Print line by line the combinations of x, y and z converted as strings splitted with spaces.


# Pseudo Code of the Algorithm:

```
maxCount = -1
for i in [0,n-1]
    count = 0
    for x in [0,n]
        for y in [i,n] U [0,i-1]
            z = n-x-y
            if z < 0 continue
            if (none of x,y,z tested before)
                save(x,y,z) in toPrint
                makeTested(x,y,z)
                count++
    if count > maxCount
        maxCount = count
        maxToPrint = toPrint
print(maxCount)
printAllOf(maxToPrint)

```


## The Time Complexity of the Algorithm: O(n^3)
In the first for loop, we have n iterations for all the possible starting combinations for (x,y) starting from (0,0) and incrementing the starting value of y in each iteration. ---> O(n)
We need to go over all possible x values by using a for loop, inside the second for loop is the third for loop to go over all possible y values. ---> O(n^2).
Combined into ---> O(n^3)

## The Space Complexity of the Algorithm: O(n)
Because the number of solutions is printed before the actual solution list, the solution list needs to be saved before printing. 
There are always less than n solutions (~2n/3). That gives an O(n) complexity. 
Since we already have an O(n) space complexity, we can freely store the tested values in arrays of size n.

## Correct Results

Our code considers every possible unique ordering of the (x,y,z) values and compares the number of tested candidates. After the comparison, it takes the ordering which results in the largest number of tested candidates. Since each possible ordering is considered, the code always outputs the correct result with the number of candidates maximized and (x,y,z) values equal to the input n.

![image](https://user-images.githubusercontent.com/59393430/172411043-bdfae646-b965-42fc-ba64-0a364e523675.png)
![image](https://user-images.githubusercontent.com/59393430/172411456-139c587a-f3bc-4957-b717-ea42808db9d7.png)
![image](https://user-images.githubusercontent.com/59393430/172411633-8619c204-836d-4d06-bf67-f7223b891397.png)
![image](https://user-images.githubusercontent.com/59393430/172412123-5ed35799-378a-4ed7-892c-7c65b3501718.png)

## Compare with Other Algorithmic Approaches 

- Before coming up with the present algorithmic approach, we tried a solution which testes x y and z results starting from x = 0, y = 1 and incrementing x and y by 1 until either y surpassed n or z became less than 0. 
- However, after running the old version trying small values for n, we observed that the algorithm printed less candidates than we could write on paper. 
- We can observe that in our present solution, the values of x y and z starts at 0, n/3 and 2n/3 and then x and y increases by 1 and the value of z drops by 2 after each print. We could hard code this without going over the non-correct solutions and reduce the runtime to O(n). However, the correctness of the mentioned solution would be hard to prove without using our O(n^3) algorithm.
