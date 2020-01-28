## Summary

We are interested in exploring the emergence and evolution of cooperative strategies (trapping, sacrificing, communicating, etc) by playing Tron with teams. It is also interesting to see how the behavior of the agents changes as a response to changes in the environment (e.g. imposing constraints on communication, adding obstacles). The input is a grid representing the current game state with cells indicating the current positions of all agents and walls and the output is a direction for each agent. 

## Evaluation Plan

We will evaluate the success of our project by the creation of a working version of Tron with teams that uses multi-agent reinforcement learning. We aim to start by implementing Q-learning, using a reward table to store the agents’ memory. Next, we will implement Deep Q-learning by changing the reward table to a neural network.

Initially, the trivial reward function would be to reward actions that lead to a Win. However, we need to think of a way to solve the credit assignment problem. Although our reward environment may not be very sparse, we aim to implement new techniques such as curiosity-driven exploration or hindsight experience replay to improve the sample efficiency and performance of our agents.

Our focus will not be solely on analyzing the results/data but we will also be taking a close look at how the agents act in the gameplay as we manipulate the code. Our code, heuristics, and approach will evolve as we see what approaches lead to more intelligent agents. We will know our approach is working by analyzing the actions of our agents: how long they’re able to stay alive, win/loss data, and specific actions they take based on what code we introduce to the program. Our moonshot case would be to successfully implement intelligent code that causes our tron team to work together and dominate the game: a team of agents that collaborate and work together and clearly use strategy to outplay their opponents. 
