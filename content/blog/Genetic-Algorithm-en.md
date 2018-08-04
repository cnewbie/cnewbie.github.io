Title: Introduction of Genetic Algorithm
Tags: Algorithm
lang: en
Summary: Introduction of the Basic Genetic Algorithm
Date: 2017-04-12
Modified: 2018-07-05

---
title: Introduction of Genetic Algorithm

---

-----------------------------

# Outline of GA

Outline of the Basic Genetic Algorithm

1. [Start] Generate random population of n chromosomes (suitable solutions for the problem)
2. [Fitness] Evaluate the fitness f(x) of each chromosome x in the population
3. [New population] Create a new population by repeating following steps until the new population is complete

    - [Selection] Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)

    - [Crossover] With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.

    - [Mutation] With a mutation probability mutate new offspring at each locus (position in chromosome).

    - [Accepting] Place new offspring in a new population

4. [Replace] Use new generated population for a further run of algorithm
5. [Test] If the end condition is satisfied, stop, and return the best solution in current population
6. [Loop] Go to step 2

# Selection

- Roulette Wheel Selection

This method have problems when the fitnesses differs very much.

- Rank Selection

This method can lead to slower convergence, because the best chromosomes do not differ so much from other ones.

- Steady-state Selection

Main idea of this selection is that big part of chromosomes should survive to next generation.

- Elitism

Elitism is name of method, which first copies the best chromosome (or a few best chromosomes) to new population. The rest is done in classical way. Elitism can very rapidly increase performance of GA, because it prevents losing the best found solution.

# Encoding

- Binary Encoding

Binary encoding is the most common, mainly because first works about GA used this type of encoding.

- Permutation Encoding

Permutation encoding can be used in ordering problems, such as traveling salesman problem or task ordering problem.

Permutation encoding is only useful for ordering problems. Even for this problems for some types of crossover and mutation corrections must be made to leave the chromosome consistent (i.e. have real sequence in it).

- Value Encoding

Direct value encoding can be used in problems, where some complicated value, such as real numbers, are used. Use of binary encoding for this type of problems would be very difficult.

- Tree Encoding

Tree encoding is used mainly for evolving programs or expressions, for genetic programming.

Tree encoding is good for evolving programs. Programing language LISP is often used to this, because programs in it are represented in this form and can be easily parsed as a tree, so the crossover and mutation can be done relatively easily.

# Crossover and Mutation

## Binary Encoding

- Crossover

    - Single point crossover - one crossover point is selected, binary string from beginning of chromosome to the crossover point is copied from one parent, the rest is copied from the second parent

    - Two point crossover - two crossover point are selected, binary string from beginning of chromosome to the first crossover point is copied from one parent, the part from the first to the second crossover point is copied from the second parent and the rest is copied from the first parent

    - Uniform crossover - bits are randomly copied from the first or from the second parent

    - Arithmetic crossover - some arithmetic operation is performed to make a new offspring

- Mutation

Bit inversion - selected bits are inverted

###Permutation Encoding

- Crossover

Single point crossover - one crossover point is selected, till this point the permutation is copied from the first parent, then the second parent is scanned and if the number is not yet in the offspring it is added

- Mutation

Order changing - two numbers are selected and exchanged

## Value Encoding

- Crossover

All crossovers from binary encoding can be used

- Mutation

Adding a small number (for real value encoding) - to selected values is added (or subtracted) a small number

## Tree Encoding

- Crossover

Tree crossover - in both parent one crossover point is selected, parents are divided in that point and exchange part below crossover point to produce new offspring

- Mutation

Changing operator, number - selected nodes are changed


# References
[Traveling Salesman Problem](http://www.cnblogs.com/biaoyu/archive/2012/10/02/2710267.html)

[Genetic Algorithm](http://www.obitko.com/tutorials/genetic-algorithms/)
