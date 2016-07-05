# 编写伪码
"""
	显示游戏的操作指南
	决定谁先走
	创建一个空的井字棋盘
	把棋盘显示出来
	当没有人获胜切不是平局时
		如果轮到玩家
			得到玩家的行棋位置
			根据行棋位置去更新棋盘
		否则
			计算得出机器人的行棋位置
			根据行棋位置去更新棋盘
		显示棋盘
		切换行棋方
	向赢家表示恭喜或声明平局
"""

# Tic-Tac-Toe(人机下井字棋AI)
# 全局常量，多个函数需要使用
X = "X" # 表示的是游戏中的两种棋子之一
O = "O"
EMPTY = " " # 棋盘上的空方格
TIE = "TIE" # 表示平局
NUM_SQUARES = 9 # 井字棋盘的方格数

# 显示游戏的操作指南函数 display_instruct()
def display_instruct():
	"""Display game instructions."""
	print(
		"""
		Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
		This will be a showdown between your human brain and my silicon processor.
		You will make your move known by entering a number, 0 - 8. The number will
		correspond to the board position as illistrated:

					0 | 1 | 2
					---------
					3 | 4 | 5
					---------
					6 | 7 | 8

		Prepare yourself, human. The ultimate battle is about to begin. \n 
		"""
		)

# 接收一个问题，回答“是”或者“否”
def ask_yes_no(question):
	"""回答一个是或否的问题"""
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response

# 询问，并返回范围数
def ask_number(question, low, high):
	"""在这个范围内返回一个数字"""
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response

# 询问玩家是否希望先下棋
def pieces():
	"""谁先走就获取X棋子，一般规则X棋子先走"""
	go_first = ask_yes_no("你想先第一个下子吗？(y/n): ")
	if go_first == "y":
		print("\n你选择了是，你是第一个下子，将获得棋子 'X'.")
		human = X
		computer = O
	else:
		print("\n你选择了否，那么你将是第二个下子，将获得棋子 'O'.")
		computer = X
		human = O
	return computer, human

# 创建新棋盘(长度为9的列表，元素为EMPTY)
def new_board():
	"""创建一个新的游戏棋盘"""
	board = []
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return board

# 字符打印到棋盘
def display_board(board):
	print("\n\t",board[0], "|", board[1], "|", board[2])
	print("\t", "---------")
	print("\n\t",board[3], "|", board[4], "|", board[5])
	print("\t", "---------")
	print("\n\t",board[6], "|", board[7], "|", board[8])

# 合法的行棋步骤
def legal_moves(board):
	moves = []
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square)
	return moves

# 判断输赢情况
def winner(board):
	# 设定一个常量元组，8种情况获胜，就是三子连城一线，就是赢
	WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),(2, 4, 6))
	# 判断当前的三个方格是否有相同的值，而且不是EMPTY
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
		if EMPTY not in board:
			return TIE
		return None

# 玩家的棋子走动位置，返回玩家的行棋方案
def human_move(board, human):
	"""Get human move"""
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
		if move not in legal:
			print("\n你的下棋不合规矩，请重新选择。\n")

	print("Fine...")
	return move

# 电脑自动下棋，返回机器人的行棋方案
def computer_move(board, computer, human):
	# 由于该函数会对列表进行修改
	board = board[:]
	BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

	print("小AI将采取的下棋步法: ", end=" ")
	# 如果机器人能赢，就走那个位置
	for move in legal_moves(board):
		board[move] = computer
		if winner(board) == computer:
			print(move)
			return move
		# 结束对当前行棋方案的测试，并取消
		board[move] = EMPTY
	# 如果玩家可以赢，就堵住那个位置
	for move in legal_moves(board):
		board[move] = human
		if winner(board) == human:
			print(move)
			return move
		# 结束对当前行棋方案的测试，并取消
		board[move] = EMPTY

	# 由于本轮谁也赢不了，所以选择最佳的空位来走
	for move in BEST_MOVES:
		if move in legal_moves(board):
			print(move)
			return move

# 该函数接收当前的行棋方，返回下一个行棋方 ,切换下棋方
def next_turn(turn):
	if turn == X:
		return O
	else:
		return X

# 该函数接收游戏的赢家
def congrat_winner(the_winner, computer, human):
	if the_winner != TIE:
		print(the_winner, "won!\n")
	else:
		print("平局!\n")

	if the_winner == computer:
		print("人类，你认输吧！我预测我再一次胜利。\n" \
			"证明机器在所有方面还是优于人类的！")
	elif the_winner == human:
		print("No,no! 不可以！你总是欺骗我，人类。\n" \
			"我绝不会输！我是电脑，我发誓！")
	elif the_winner == TIE:
		print("你是幸运的，人类，这局平局！\n" \
			"不过下一把，我不会饶过你，你最好小心点！")

# 主函数入口
def main():
	display_instruct()
	computer, human = pieces()
	turn = X
	board = new_board()
	display_board(board)

	while not winner(board):
		if turn == human:
			move = human_move(board, human)
			board[move] = human
		else:
			move = computer_move(board, computer, human)
			board[move] = computer
		display_board(board)
		turn = next_turn(turn)

	the_winner = winner(board)
	congrat_winner(the_winner, computer, human)


# 启动程序
main()
input("\n\nPress the enter key to quit")
