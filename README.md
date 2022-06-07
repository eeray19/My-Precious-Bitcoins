# My-Precious-Bitcoins

# To DO:

- [x] The algorithm you designed to solve the problem, the choices of the data structures you used and your reasoning.
- [ ] In addition to your actual code, write a pseudo code for your algorithm
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

## The Time Complexity of the Algorithm: O(n^3)
In the first for loop, we have n iterations for all the possible starting combinations for (x,y) starting from (0,0) and incrementing the starting value of y in each iteration. ---> O(n)
We need to go over all possible x values by using a for loop, inside the second for loop is the third for loop to go over all possible y values. ---> O(n^2).
Combined into ---> O(n^3)

## The Space Complexity of the Algorithm: O(n)
Because the number of solutions is printed before the actual solution list, the solution list needs to be saved before printing. 
There are always less than n solutions (~2n/3). That gives an O(n) complexity. 
Since we already have an O(n) space complexity, we can freely store the tested values in arrays of size n.


## Coreect Results
![image](https://user-images.githubusercontent.com/59393430/172411043-bdfae646-b965-42fc-ba64-0a364e523675.png)
![image](https://user-images.githubusercontent.com/59393430/172411456-139c587a-f3bc-4957-b717-ea42808db9d7.png)
![image](https://user-images.githubusercontent.com/59393430/172411633-8619c204-836d-4d06-bf67-f7223b891397.png)
![image](https://user-images.githubusercontent.com/59393430/172412123-5ed35799-378a-4ed7-892c-7c65b3501718.png)



