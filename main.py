"""tutaj wszystko do kupy skleimy
a na razie cos tam se testuje
"""
# TODO: Save tree to file:
#       https://stackoverflow.com/questions/1047318/easiest-way-to-persist-a-data-structure-to-a-file-in-python

#tescior
from loadboard import load_map
from generate_tree import generate_tree_bfs, generate_tree_dfs
from debug import print_board
from uninformed import iterative_dfs
from informed import a_star
from time import process_time
from heuristic import board_cost
from boardstate import BoardState

# moves, brd = generate_tree_bfs(load_map("bridges7x7_1.txt"))
# moves, brd = generate_tree_dfs(load_map("bridges7x7_3.txt"))

start_board = load_map("board-easy.txt")
time_start = process_time()
#-
#node, depth, tree, visited = iterative_dfs(start_board)
#-
node, tree, visited = a_star(start_board)
depth = 6
#-
time = process_time() - time_start
final_bstate = node.content
final_board = final_bstate.board

print_board(final_board)
print("Solved = ", final_bstate.solved)
print("depth = ", depth)
print("nodes visited: ", visited)
print("time: ", time, " [s]")


boards = [start_board, final_board]
#zmienic to (chcesz to zautomatyzuj)
find_1 = int(depth/2)
find_2 = 1

current = node
current_depth = depth
while current != None:
    #test
    print_board(current.content.board)
    print("cost: ", board_cost(current.content))
    #/test    
    current = current.parent
    current_depth -= 1
    if current_depth == find_1 or current_depth == find_2:
        boards.append(current.content.board)

print("---")
for brd in boards:
    print_board(brd)
#     to sie mordo nie zrobi bo jak tworzysz sobie nowy obiekt boardstate to nie ma w ogóle listy wysp i połączeń
#     a żeśmy nie zrobili tworzenia boardstate z niepustej planszy
#     print(f"COST = {board_cost(BoardState(brd))}")
    print("...")

"""
Zapisać:
depth - głębokość dfsa
boards - cztery plansze - wejściowa, wyjściowa i dwie pośrednie,
        określone przez find_1 i find_2, czyli tu np po 1 i po 3 ruchach
time - czas wykonywania algorytmu
visited - ilość odwiedzonych stanów
"""
