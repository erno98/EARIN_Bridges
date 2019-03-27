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

# moves, brd = generate_tree_bfs(load_map("bridges7x7_1.txt"))
# moves, brd = generate_tree_dfs(load_map("bridges7x7_3.txt"))

start_board = load_map("board-easy.txt")
node, depth, tree = iterative_dfs(start_board)
final_bstate = node.content
final_board = final_bstate.board

print_board(final_board)
print("Solved = ", final_bstate.solved)
print("depth = ", depth)

boards = [start_board, final_board]
#zmienic to (chcesz to zautomatyzuj)
find_1 = 3
find_2 = 1

current = node
current_depth = depth
while current != None:
    current = current.parent
    current_depth -= 1
    if current_depth == find_1 or current_depth == find_2:
        boards.append(current.content.board)

print("---")
for brd in boards:
    print_board(brd)
    print("...")

"""
Zapisać:
depth - głębokość dfsa
boards - cztery plansze - wejściowa, wyjściowa i dwie pośrednie,
        określone przez find_1 i find_2, czyli tu np po 1 i po 3 ruchach
Może dodać timing i patrzenie ile zajmuje dla różnego skomplikowania plansz
I może jeszcze zaraz dodam liczenie ile odwiedził w sumie stanów, bo to chyba też potrzebne
"""
