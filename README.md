# Assignment 4: Stable Marriage Problem

## Problem Statement:

You are tasked with solving the Stable Marriage Problem, where there are n boys and n girls. Each boy has a ranked list of all the girls based on his preferences, and each girl has a ranked list of all the boys based on her preferences. The goal is to match each boy to a girl in such a way that the resulting marriages are stable.

## Definitions:
   - Stable Marriage: A marriage arrangement is considered stable if there is no unstable pair of a boy and a girl.

   - Unstable Pair: A boy-girl pair (b, g) is considered unstable if:
                     - Boy b prefers girl g over his current partner.
                     - Girl g prefers boy b over her current partner.
     In other words, an unstable pair is a situation where both the boy and the girl would rather be with each other than their current partners, leading to instability in the matching.

## Task:
Write a program to implement the Gale-Shapley algorithm (also known as the Deferred Acceptance Algorithm) to find a stable marriage for the given preferences of boys and girls.

## Input:
   - An integer n, representing the number of boys and girls.
   - A 2D list 'boy_preferences', **[[1, 2, 3], [2, 1, 3], [1, 2, 3]]** where each element is a list of size n representing a boy's ranked preferences for the girls. Each list contains integers from 1 to n, representing the girls.
     
   - A 2D list 'girl_preferences',**[[2, 1, 3], [1, 3, 2], [3, 1, 2]]** where each element is a list of size n representing a girl's ranked preferences for the boys. Each list contains integers from 1 to n, representing the boys.

## Output:
   - A list of size n, **[(1, 2), (2, 1), (3, 3)]** where each element (b, g) represents that boy b is married to girl g. This output should ensure that there are no unstable pairs, meaning the solution is stable.

for further info please refer the stable marrige recorded lecture.
