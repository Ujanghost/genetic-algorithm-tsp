# Solving Travelling Sales Man Problem Using Genetic Algorithm

The Travelling Salesman Problem [TSP](https://en.wikipedia.org/wiki/Travelling_salesman_problem) is a classic problem in computer science where we want to find the shortest possible route that visits a set of cities exactly once and returns to the starting city. A genetic algorithm can be used to solve this problem. In a genetic algorithm, we start with a randomly generated population of potential solutions (i.e., paths through the cities). We then evaluate the fitness of each solution, where fitness is inversely proportional to the total distance traveled. We then select pairs of parents from the population based on their fitness and use crossover and mutation to create new offspring. These offspring then replace some of the weaker members of the population. Over time, the population evolves to contain better and better solutions to the TSP, until we reach the best possible path.

## The Brute Force Algorithm
The brute force method is a simple but exhaustive approach to solve the Travelling Salesman Problem (TSP). This method involves evaluating every possible route through the cities, calculating the total distance traveled for each route, and selecting the route with the shortest distance as the solution. The brute force method works by generating all possible permutations of the cities and computing the distance of each permutation. Each of these permutations is then evaluated by calculating the total distance traveled along the path. The path with the shortest distance is selected as the solution. While the brute force method guarantees an optimal solution, it is computationally expensive and impractical for large numbers of cities. The number of possible permutations increases factorially with the number of cities, making the brute force method infeasible for more than a few dozen cities.
![symmetric TSP with 7 cities using brute force search](https://upload.wikimedia.org/wikipedia/commons/2/2b/Bruteforce.gif)

## The Genetic Algorithm

The Genetic Algorithm is a heuristic optimization technique that can be used to solve the Travelling Salesman Problem (TSP). In this approach, a population of potential solutions (i.e., paths through the cities) is randomly generated, and then fitness is evaluated based on the total distance traveled. Parents are selected from the population based on their fitness, and crossover and mutation are used to create new offspring. Over time, the population evolves to contain better and better solutions, until the best possible path is found. The Genetic Algorithm is computationally efficient and can handle large numbers of cities, making it a popular approach to solving the TSP.

click to learn more[Genetic Algorithms for the TSP](https://www.youtube.com/watch?v=3lc_Fcga5z8)

![Genetic_Algo](https://blogs.mathworks.com/images/pick/will_campbell/potw_salesman/traveling_salesman.gif)

  The Solution:- 

![Genetic_Algo_sol](https://blogs.mathworks.com/images/pick/will_campbell/potw_salesman/traveling_salesman.png)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
