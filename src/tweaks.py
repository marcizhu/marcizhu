from urllib.parse import urlencode


GITHUB_USER      = "marcizhu"      # GitHub user where this file is located
GITHUB_REPO_NAME = "readme-chess"  # GitHub repo for this project

# Contents of the issue to create as a template
GITHUB_MOVE_ISSUE_CONTENTS = {
	"title": "Chess: Move {source} to {dest}",
	"body": "Please do not change the title. Just click \"Submit new issue\". You don't need to do anything else :D"
}

GITHUB_NEW_GAME_ISSUE_CONTENTS = {
	"title": "Chess: Start new game",
	"body": "Please do not change the title. Just click \"Submit new issue\". You don't need to do anything else :D"
}

# Link of the move issue
GITHUB_MOVE_ISSUE_LINK = "https://github.com/" + GITHUB_USER + "/" + GITHUB_REPO_NAME + "/issues/new?" + urlencode(GITHUB_MOVE_ISSUE_CONTENTS, safe="{}")

# Link of the new game issue
GITHUB_NEW_GAME_ISSUE_LINK = "https://github.com/" + GITHUB_USER + "/" + GITHUB_REPO_NAME + "/issues/new?" + urlencode(GITHUB_NEW_GAME_ISSUE_CONTENTS)

MAX_LAST_MOVERS = 5 # Maximum moves to display
MAX_TOP_MOVERS = 10 # Top most moves to display

# Markers
# Chess board marker
BOARD_BEGIN_MARKER = "<!-- BEGIN CHESS BOARD -->\n"
BOARD_END_MARKER   = "<!-- END CHESS BOARD -->\n"

# Moves list marker
MOVES_BEGIN_MARKER = "<!-- BEGIN MOVES LIST -->\n"
MOVES_END_MARKER   = "<!-- END MOVES LIST -->\n"

# Turn marker
TURN_BEGIN_MARKER = "<!-- BEGIN TURN -->"
TURN_END_MARKER   = "<!-- END TURN -->"

# Last moves marker
LAST_MOVES_BEGIN_MARKER = "<!-- BEGIN LAST MOVES -->\n"
LAST_MOVES_END_MARKER   = "<!-- END LAST MOVES -->\n"

# Top movers marker
TOP_MOVERS_BEGIN_MARKER = "<!-- BEGIN TOP MOVES -->\n"
TOP_MOVERS_END_MARKER   = "<!-- END TOP MOVES -->\n"

# Comments
# Comment if the board is invalid
COMMENT_INVALID_BOARD="{author} Sorry, I can't perform the specified move. The board is invalid!"

# Comment for invalid moves
COMMENT_INVALID_MOVE="{author} Whaaaat? The move `{move}` is invalid!\nMaybe someone squeezed a move before you. Please try again."

# Comment for invalid new games
COMMENT_INVALID_NEW_GAME="{author} Sorry, but you cannot start a new game while the old one is still in progress. Only the repo owner can do that."

# Comment for valid moves
COMMENT_SUCCESSFUL_MOVE="{author} done! Successfully played move `{move}` for current game.\nThanks for playing!"

# Comment for valid new games
COMMENT_SUCCESSFUL_NEW_GAME="{author} done! New game successfully started!"

# Comment for unknown commands
COMMENT_UNKNOWN_COMMAND="{author} Sorry, I can't understand the command. Please try again and do not modify the issue title!"

# Comment for game overs
COMMENT_GAME_OVER="And that's a game over! {winner}! This game had {num_moves} moves made by {num_players}.\n\nThanks to {players} for participating!"
