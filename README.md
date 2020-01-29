## Team Members
[**Andranik Sahakyan**](mailto:saakyana@uci.edu) <br>
[**Arya Kashani**](mailto:akashan1@uci.edu) 
[**Tim Hakobian**](mailto:thakobia@uci.edu)

## Appointment Time
Thursday, January 30, 2020 at 1:15pm

## Summary

We are interested in exploring the emergence and evolution of cooperative strategies (trapping, sacrificing, communicating, etc) by playing Tron with teams. It is also interesting to see how the behavior of the agents changes as a response to changes in the environment (e.g. imposing constraints on communication, adding obstacles). The input is a grid representing the current game state with cells indicating the current positions of all agents and walls and the output is a direction for each agent. 

## Evaluation Plan

We will evaluate the success of our project by the creation of a working version of Tron with teams that uses multi-agent reinforcement learning. We aim to start by implementing Q-learning, using a reward table to store the agents’ memory. Next, we will implement Deep Q-learning by changing the reward table to a neural network.

Initially, the trivial reward function would be to reward actions that lead to a Win. However, we need to think of a way to solve the credit assignment problem. Although our reward environment may not be very sparse, we aim to implement new techniques such as curiosity-driven exploration or hindsight experience replay to improve the sample efficiency and performance of our agents.

Our focus will not be solely on analyzing the results/data but we will also be taking a close look at how the agents act in the gameplay as we manipulate the code. Our code, heuristics, and approach will evolve as we see what approaches lead to more intelligent agents. We will know our approach is working by analyzing the actions of our agents: how long they’re able to stay alive, win/loss data, and specific actions they take based on what code we introduce to the program. Our moonshot case would be to successfully implement intelligent code that causes our tron team to work together and dominate the game: a team of agents that collaborate and work together and clearly use strategy to outplay their opponents. 

## Goals

### Minimum goal: Create a version of Tron with teams.

**Milestone 1:** Run all RLColosseumNotebooks without error; to have our team established with an open line of communication and to have everybody on the same page as to what we plan to do with our project and the exact timeline we plan to do it in; to have set up all necessary software, frameworks, IDEs, etc. along with our Github and website. 

**Milestone 2:** Have written code for Tron and written code for RL lib. For tron, the goal is to have created a version of the game that makes it a team game rather than single player. The goal is to have learned how the code works and clearly manipulated it so that its 2-player versus 2-player. For RL lib the goal is to have created a small coding project of our own so we understand how that code works as well. Even if the code is not directly related to Tron in any way; the point of the goal is to have learned how to use the library to create something. 

### Realistic goal: Create a reinforcement-learning agent that cooperates with teammates to win our version of Tron.

**Milestone 1:** Successfully created and completed a Tron team game that uses reinforcement learning; the goal is to clearly see the teams cooperate and possibly use strategy to try and achieve a win. 

**Milestone 2:**  Implement Deep Q-learning with a neural network in order to 
make our agents more intelligent. 

### Ambitious goal: Make the environment more complex by adding additional constraints/obstacles and observe interesting behavior from agents. Implement new RL techniques such as curiosity-driven exploration and hindsight experience replay.
 
**Milestone:** Allow the agents to view/share each other’s experience when they are physically close as a form of communicating and sharing knowledge. We hope the agents will realize that sharing their experiences will help the team stronger as it will accelerate learning.
