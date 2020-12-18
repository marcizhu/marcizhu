# GitHub README Chess Tournament

This template repository contains the source code for a Python Chess bot, together with GitHub Workflows in order to allow ANYONE to play chess from a README file. Want to see this in action? Go to my [profile page](https://github.com/marcizhu) and feel free to try it out by yourself!


## Steps to make your own repo

1. First, create a new repository based on this template. Call it whatever you want!

2. Tweak the bot settings to your linking. These settings are located in the file `src/tweaks.py`. Specially, make sure to update the following parameters:
    - `GITHUB_USER`: Your GitHub username
    - `GITHUB_REPO_NAME`: Name of your newly created GitHub repository
    
    The rest of the settings are optional and can be changed to your liking, but leaving them as they are is more than enough.

3. Rename the folder `.github/_workflows` to `.github/workflows` in order to enable the GitHub Actions workflow that does all the magic.

4. Delete this README file and make your own `README.md`. I recommend using `README.template` as a starting point. Keep in mind that the text between the HTML comments like `<-- BEGIN CHESS BOARD -->` and `<-- END CHESS BOARD -->` will be recreated after each move, so don't waste your time changing anything in there ;)

5. Commit and push all the settings and create a new issue with title `Chess: Start new game`. If all goes well, after a few seconds a new response should appear telling you that a new game was successfully started and the issue should be automatically closed. Then, a new commit should appear and your repository should be ready to go! Just click on any of the links on the table of available moves, click on "Submit new issue" and after a few seconds, the move should be performed!

Don't forget to share, have fun and enjoy your games!


## Some extra information

All games are automatically archived into the `games/` folder. The current game is always called `games/current.pgn`, and the archived games always follow the pattern `games/game-yyyymmdd-HHMMSS.pgn`. You can download the archived games and review them using an external application. Each move in that PGN file has a comment specifying who performed each move so you can see which moves you made!

Finally, this is my first project using Python, so don't be too harsh on my coding skills. If you find any problem, feel free to submit an issue or open a PR and I will be more than happy to take a look at it!


## Credits

Thanks to @timburgan for the initial idea. This project is heavily inspired on his. Also, big thanks to the authors and contributors of [python-chess](https://python-chess.readthedocs.io/en/latest/), [PyGithub](https://pygithub.readthedocs.io/en/latest/) and [EndBug/add-and-commit](https://github.com/EndBug/add-and-commit). Without their libraries, this project would have been impossible :heart:


## License

This template and the code in it is licensed under the [MIT License](https://github.com/marcizhu/readme-chess/LICENSE).  
If you use this on your own repositories, please add a link back to this repo :D
