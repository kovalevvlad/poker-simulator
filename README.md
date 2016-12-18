![CircleCI Build Status](https://circleci.com/gh/kovalevvlad/poker-simulator.png?style=shield&circle-token=ce81ae07dd26e397b7a495e336dc6a9a95de9454 "CircleCI Build Status")

# Poker Simulator

### Motivation
Have you ever played poker and wondered what your probability of winning in a particular situation was?
If you have, this project can help.

### Implementation
This project implements a simple REST get endpoint which can be queried with various poker game states to
obtain a probability of winning in that state.

The application works by running a Monte-Carlo simulation evaluating random outcomes of the game. It then
computes the number of random generations in which the player querying the service won. This allows the 
backend to estimate the probability of winning in the specified game state.

### How To Use
The service is a single endpoint - /estimate. To get a probability of winning in a particular state, you need to issue a query in the following format - `/estimate?my_hand=x&table=y&opponent_count=z`. 

#### Parameters
Let's discuss the format of the parameters x,y and z. z is just and integer. Please note that there cannot be more than 22 (`floor((52 - 5) / 2) - 1`) players since the dealer would run out of cards.

x and y are comma separated lists of cards. x has always got to be of size 2, while y can be of the following sizes - 0,3,4,5 (if you are not sure why, you should probably check out [Texas Hold'em rules](https://en.wikipedia.org/wiki/Texas_hold_'em#Rules)).

Cards are represented by 2 characters - the suit character followed by the rank character. There are 4 possible suits - diamonds (represented by character D), clubs (C), spades (S) and hearts (H). Ranks 2 through 9 are represented by the corresponding digit. Ranks 10, jack, queen, king and ace are represented by T, J, Q, K and A respectively. Here are some valid card representations - H2 (two of hearts), CT (10 of clubs), SA (aces of spades).

#### Examples
Armed with the above knowledge we can now issue some queries:
 - Probability of winning with an ace of spades and an ace of hearts against 3 opponents with an empty table - [/estimate?my_hand=SA,CA&table=&opponent_count=3](https://poker-simulator.herokuapp.com/estimate?my_hand=SA,HA&table=&opponent_count=3)
 - Probability of winning with a two of clubs and a seven of clubs against 2 opponents with a three of diamonds, king of hearts and a king of diamonds on the table - [/estimate?my_hand=C2,C7&table=D3,HK,DK&opponent_count=2](https://poker-simulator.herokuapp.com/estimate?my_hand=C2,C7&table=D3,HK,DK&opponent_count=2)
 - Probability of winning with an ace of clubs and a ten of clubs against 5 opponents with a jack of clubs, seven of hearts, queen of clubs, king of clubs, 7 of diamonds on the table - [/estimate?my_hand=CT,CA&table=CJ,CQ,CK,D7,H7&opponent_count=5](https://poker-simulator.herokuapp.com/estimate?my_hand=CT,CA&table=CJ,CQ,CK,D7,H7&opponent_count=5)
