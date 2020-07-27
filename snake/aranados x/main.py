from game import *
from players import *

size = 10
num_snakes = 1
players = [RandomPlayer(0)]

gui_size = 800

#game = Game(size, num_snakes, players, gui=None, display=True, max_turn=100)
#gui = Gui(game, gui_size)
#print("HERE")
#game.play(True, termination=False)

pop_size = 50
num_generations = 500
num_trails = 2
window_size = 7
hidden_size = 15
board_size = 10;

gen_player = GeneticPlayer(pop_size, num_generations, num_trails, window_size, hidden_size, board_size,
                            mutation_chance=0.2, mutation_size=0.3)

gen_player.evolve_pop()