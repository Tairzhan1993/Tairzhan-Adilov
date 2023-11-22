'''def draw_tree(height, symbol):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = symbol * (2 * i - 1)
        print(spaces + stars)

# Задайте высоту и символ для ёлки
tree_height = int(input("Введите высоту ёлки: "))
tree_symbol = input("Введите символ для ёлки: ")

draw_tree(tree_height, tree_symbol) '''

'''def create_chessboard():
    chessboard = []
    for i in range(8):
        row = []
        for j in range(8):
            # Определите цвет клетки (черный или белый) на основе индексов i и j
            if (i + j) % 2 == 0:
                cell_color = "white"
            else:
                cell_color = "black"
            row.append(cell_color)
        chessboard.append(row)
    return chessboard

def print_chessboard(board):
    for row in board:
        print(" ".join(row))

# Создаем пустую шахматную доску
chessboard = create_chessboard()

# Выводим шахматную доску
print_chessboard(chessboard)'''

def draw_butterfly(width, height):
    for i in range(1, height + 1):
        if i <= height // 2:
            stars = "*" * i
            spaces = " " * (width - 2 * i)
        else:
            stars = "*" * (height - i + 1)
            spaces = " " * (width - 2 * (height - i + 1))
        row = stars + spaces + stars
        print(row.center(width))

# Задайте ширину и высоту для фигуры "бабочка"
butterfly_width = int(input("Введите ширину фигуры 'бабочка': "))
butterfly_height = int(input("Введите высоту фигуры 'бабочка': "))

# Выведем фигуру "бабочка"
draw_butterfly(butterfly_width, butterfly_height)