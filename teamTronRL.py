import numpy as np
from random import random, choice

from colosseumrl.envs.tron import TronGridEnvironment, TronRender
from time import sleep

from typing import Tuple
from matplotlib import cm


class TronRender(TronRender):

    def __init__(self, board_size: int, num_players: int,
                 window_size: Tuple[int, int] = (600, 600),
                 outside_border: int = 25,
                 grid_space_ratio: float = 6,
                 winner_player: int = None):

        super().__init__(
            board_size,
            num_players,
            window_size,
            outside_border,
            grid_space_ratio,
            winner_player)

        self.colors = cm.plasma(np.linspace(0.1, 0.9, 2))
        self.colors = np.minimum(self.colors * 1.3, 1.0)
        self.colors = np.repeat(self.colors, 2, axis=0)


class SimpleAvoidAgent:
    """ Basic single player agent to test single player version of Tron. """

    def __init__(self, noise=0.1):
        self.noise = noise

    def __call__(self, env, observation):
        # With some probability, select a random action for variation
        # if random() <= self.noise:
            # return choice(['forward', 'right', 'left'])

        # Get game information
        board = observation['board']
        head = observation['heads'][0]
        direction = observation['directions'][0]

        # Find the head of our body
        board_size = board.shape[0]
        x, y = head % board_size, head // board_size

        # Check ahead. If it's clear, then take a step forward.
        nx, ny = env.next_cell(x, y, direction, board_size)
        if board[ny, nx] == 0:
            return 'forward'

        # Check a random direction. If it's clear, then go there.
        offset, action, backup = choice(
            [(1, 'right', 'left'), (-1, 'left', 'right')])
        nx, ny = env.next_cell(x, y, (direction + offset) % 4, board_size)
        if board[ny, nx] == 0:
            return action

        # Otherwise, go the opposite direction.
        return backup

    def play(self):
        # Create a Tron environment on a 25x25 Grid
        env = TronGridEnvironment.create(board_size=25, num_players=4)
        renderer = TronRender(board_size=25, num_players=4)

        # Create our agent with a 5% chance of executing a random action
        agent = SimpleAvoidAgent(noise=0.05)

        # Start the game with 4 players
        state, players = env.new_state()
        terminal = False

        renderer.close()
        renderer.render(state)

        # Play until the game is over
        teamWinner = 0
        while not terminal:
            # Let each player select an action for their respective
            # observations
            actions = [
                agent(
                    env,
                    env.state_to_observation(
                        state,
                        player)) for player in players]

            # Perform actions simultaneously
            state, players, rewards, terminal, winners = env.next_state(
                state, players, actions)

            if 0 not in players and 1 not in players:
                terminal = True
                teamWinner = 2
                winners = players
            if 2 not in players and 3 not in players:
                terminal = True
                teamWinner = 1
                winners = players

            renderer.render(state)

            # Wait so we can see whats happening
            sleep(0.05)

        if winners.size == 0:
            print(f"No team won. Tie with rankings: {env.compute_ranking(state, players, winners)}")
        else:
            if teamWinner == 1:
                print("Team 1 wins")
            else:
                print("Team 2 wins")


ttrl = SimpleAvoidAgent()
for x in range(10):
    SimpleAvoidAgent.play(ttrl)