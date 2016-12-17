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
TODO
