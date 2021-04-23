import re
import os
import os.path
import sys
import chess
import chess.pgn
import ast

from github import Github
from enum import Enum
from datetime import datetime

import src.tweaks as tweaks
import src.markdown as markdown

# TODO:
# - Use an image instead of a raw link to start new games

class Action(Enum):
	UNKNOWN = 0
	MOVE = 1
	NEW_GAME = 2


def update_top_moves(user):
	with open("data/top_moves.txt", 'r') as file:
		contents = file.read()
		dictionary = ast.literal_eval(contents)

	if user not in dictionary:
		dictionary[user] = 1 # First move
	else:
		dictionary[user] += 1

	with open("data/top_moves.txt", 'w') as file:
		file.write(str(dictionary))


def update_last_moves(line):
	with open("data/last_moves.txt", 'r+') as f:
		content = f.read()
		f.seek(0, 0)
		f.write(line.rstrip('\r\n') + '\n' + content)


def replaceTextBetween(originalText, delimeterA, delimterB, replacementText):
	if originalText.find(delimeterA) == -1 or originalText.find(delimterB) == -1:
		return originalText

	leadingText = originalText.split(delimeterA)[0]
	trailingText = originalText.split(delimterB)[1]

	return leadingText + delimeterA + replacementText + delimterB + trailingText


def parse_issue(title):
	if title.lower() == "chess: start new game":
		return (Action.NEW_GAME, None)
	elif "chess: move" in title.lower():
		matchObj = re.match('Chess: Move ([A-H][1-8]) to ([A-H][1-8])', title, re.I)
		
		source = matchObj.group(1)
		dest   = matchObj.group(2)
		return (Action.MOVE, (source + dest).lower())

	return (Action.UNKNOWN, None)


def main():
	g = Github(os.environ["GITHUB_TOKEN"])
	repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
	issue = repo.get_issue(number=int(os.environ["ISSUE_NUMBER"]))

	issue_title  = issue.title
	issue_author = "@" + issue.user.login

	action = parse_issue(issue_title)
	gameboard = chess.Board()

	if action[0] == Action.NEW_GAME:
		if os.path.exists("games/current.pgn") and issue_author != "@" + os.environ["REPOSITORY_OWNER"]:
			issue.create_comment(tweaks.COMMENT_INVALID_NEW_GAME.format(author=issue_author))
			issue.edit(state='closed')
			sys.exit("ERROR: A current game is in progress. Only the repo owner can start a new issue")

		print("Start new game")
		issue.create_comment(tweaks.COMMENT_SUCCESSFUL_NEW_GAME.format(author=issue_author))
		issue.edit(state='closed')

		with open("data/last_moves.txt", 'w') as f:
			f.write("Start game: " + issue_author)

		# Create new game
		game = chess.pgn.Game()
		game.headers["Event"] = os.environ["REPOSITORY_OWNER"] + "'s Online Open Chess Tournament"
		game.headers["Site"] = "https://github.com/" + os.environ["GITHUB_REPOSITORY"]
		game.headers["Date"] = datetime.now().strftime("%Y.%m.%d")
		game.headers["Round"] = "1"

	elif action[0] == Action.MOVE:
		if not os.path.exists("games/current.pgn"):
			sys.exit("ERROR: There is no game in progress! Start a new game first")

		# Load game from "games/current.pgn"
		pgn_file = open("games/current.pgn")
		game = chess.pgn.read_game(pgn_file)
		gameboard = game.board()

		last_player = open('data/last_moves.txt').readline().split(':')[1].strip()
		print(last_player)

		for move in game.mainline_moves():
			gameboard.push(move)

		# Try to move with promotion to queen
		if chess.Move.from_uci(action[1] + "q") in gameboard.legal_moves:
			action = (action[0], action[1] + "q")

		print("Perform move " + action[1])

		move = chess.Move.from_uci(action[1])

		# Check if player is moving twice in a row
		if last_player == issue_author:
			issue.create_comment("Sorry, you can't move twice in a row! You can ask someone to play the next turn :D")
			issue.edit(state='closed', labels=["Invalid"])
			sys.exit("ERROR: Two moves in a row!")

		# Check if move is valid
		if not move in gameboard.legal_moves:
			issue.create_comment(tweaks.COMMENT_INVALID_MOVE.format(author=issue_author, move=action[1]))
			issue.edit(state='closed', labels=["Invalid"])
			sys.exit("ERROR: Move is invalid!")

		# Check if board is valid
		if not gameboard.is_valid():
			issue.create_comment(tweaks.COMMENT_INVALID_BOARD.format(author=issue_author))
			issue.edit(state='closed', labels=["Invalid"])
			sys.exit("ERROR: Board is invalid!")

		issue_labels = ["⚔️ Capture!"] if gameboard.is_capture(move) else []
		issue_labels += ["White" if gameboard.turn == chess.WHITE else "Black"]
		
		issue.create_comment(tweaks.COMMENT_SUCCESSFUL_MOVE.format(author=issue_author, move=action[1]))
		issue.edit(state='closed', labels=issue_labels)

		update_last_moves(action[1] + ": " + issue_author)
		update_top_moves(issue_author)

		# Perform move
		gameboard.push(move)
		game.end().add_main_variation(move, comment=issue_author)
		game.headers["Result"] = gameboard.result()

	elif action[0] == Action.UNKNOWN:
		issue.create_comment(tweaks.COMMENT_UNKNOWN_COMMAND.format(author=issue_author))
		issue.edit(state='closed', labels=["Invalid"])
		sys.exit("ERROR: Unknown action")

	# Save game to "games/current.pgn"
	print(game, file=open("games/current.pgn", "w"), end="\n\n")

	turn = "white" if gameboard.turn == chess.WHITE else "black"
	moves = markdown.generate_moves_list(gameboard)
	board = markdown.board_to_markdown(gameboard)
	lasts = markdown.generate_last_moves()
	top   = markdown.generate_top_moves()

	# If it is a game over, archive current game
	if gameboard.is_game_over():
		winner = gameboard.result()
		win_msg= "It's a draw"

		if winner == "1-0":
			win_msg = "White wins"
		elif winner == "0-1":
			win_msg = "Black wins"

		with open("data/last_moves.txt", "r") as f:
			lines = f.readlines()
			pattern = re.compile('.*: (@[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38})', flags=re.I)
			player_list = [re.match(pattern, line).group(1) for line in lines]
			players = ", ".join(set(player_list))

		issue.add_to_labels("👑 Winner!")
		issue.create_comment(tweaks.COMMENT_GAME_OVER.format(outcome=win_msg, players=players, num_moves=len(lines), num_players=len(set(player_list))))
		os.rename("games/current.pgn", datetime.now().strftime("games/game-%Y%m%d-%H%M%S.pgn"))
		os.remove("data/last_moves.txt")

	with open("README.md", "r") as file:
		readme = file.read()
		readme = replaceTextBetween(readme, tweaks.BOARD_BEGIN_MARKER, tweaks.BOARD_END_MARKER, "{chess_board}")
		readme = replaceTextBetween(readme, tweaks.MOVES_BEGIN_MARKER, tweaks.MOVES_END_MARKER, "{moves_list}")
		readme = replaceTextBetween(readme, tweaks.TURN_BEGIN_MARKER,  tweaks.TURN_END_MARKER,  "{turn}")
		readme = replaceTextBetween(readme, tweaks.LAST_MOVES_BEGIN_MARKER, tweaks.LAST_MOVES_END_MARKER, "{last_moves}")
		readme = replaceTextBetween(readme, tweaks.TOP_MOVERS_BEGIN_MARKER, tweaks.TOP_MOVERS_END_MARKER, "{top_moves}")

	with open("README.md", "w") as file:
		# Write new board & list of movements
		file.write(readme.format(chess_board=board, moves_list=moves, turn=turn, last_moves=lasts, top_moves=top))


if __name__ == "__main__":
	main()
