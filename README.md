# Marc's Open Chess Tournament

This is an open chess tournament where ANYONE can play. That's the fun part.  
It's your turn to play! Move a <!-- BEGIN TURN -->white<!-- END TURN --> piece.

<!-- BEGIN CHESS BOARD -->
|   | A | B | C | D | E | F | G | H |   |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **8** | <img src="img/black/rook.svg" width=50px> | <img src="img/black/knight.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/black/king.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/black/knight.svg" width=50px> | <img src="img/black/rook.svg" width=50px> | **8** |
| **7** | <img src="img/blank.png" width=50px> | <img src="img/black/pawn.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/black/pawn.svg" width=50px> | <img src="img/black/bishop.svg" width=50px> | **7** |
| **6** | <img src="img/blank.png" width=50px> | <img src="img/white/knight.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/black/pawn.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | **6** |
| **5** | <img src="img/blank.png" width=50px> | <img src="img/black/pawn.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/black/pawn.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/white/bishop.svg" width=50px> | <img src="img/black/pawn.svg" width=50px> | **5** |
| **4** | <img src="img/black/pawn.svg" width=50px> | <img src="img/black/bishop.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | **4** |
| **3** | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/white/pawn.svg" width=50px> | <img src="img/white/pawn.svg" width=50px> | <img src="img/white/knight.svg" width=50px> | **3** |
| **2** | <img src="img/white/pawn.svg" width=50px> | <img src="img/white/pawn.svg" width=50px> | <img src="img/white/pawn.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/white/pawn.svg" width=50px> | **2** |
| **1** | <img src="img/white/rook.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/white/queen.svg" width=50px> | <img src="img/white/king.svg" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/blank.png" width=50px> | <img src="img/white/rook.svg" width=50px> | **1** |
|   | **A** | **B** | **C** | **D** | **E** | **F** | **G** | **H** |   |
<!-- END CHESS BOARD -->

**It's your turn to move! Choose one from the following table**
<!-- BEGIN MOVES LIST -->
**CHECK!** Choose your move wisely!
|  FROM  | TO (Just click a link!) |
| :----: | :---------------------- |
| **C2** | [C3](https://github.com/marcizhu/marcizhu/issues/new?body=Please+do+not+change+the+title.+Just+click+%22Submit+new+issue%22.+You+don%27t+need+to+do+anything+else+%3AD&title=Chess%3A+Move+C2+to+C3) |
| **D1** | [D2](https://github.com/marcizhu/marcizhu/issues/new?body=Please+do+not+change+the+title.+Just+click+%22Submit+new+issue%22.+You+don%27t+need+to+do+anything+else+%3AD&title=Chess%3A+Move+D1+to+D2) |
| **E1** | [E2](https://github.com/marcizhu/marcizhu/issues/new?body=Please+do+not+change+the+title.+Just+click+%22Submit+new+issue%22.+You+don%27t+need+to+do+anything+else+%3AD&title=Chess%3A+Move+E1+to+E2), [F1](https://github.com/marcizhu/marcizhu/issues/new?body=Please+do+not+change+the+title.+Just+click+%22Submit+new+issue%22.+You+don%27t+need+to+do+anything+else+%3AD&title=Chess%3A+Move+E1+to+F1), [F2](https://github.com/marcizhu/marcizhu/issues/new?body=Please+do+not+change+the+title.+Just+click+%22Submit+new+issue%22.+You+don%27t+need+to+do+anything+else+%3AD&title=Chess%3A+Move+E1+to+F2) |
| **G5** | [D2](https://github.com/marcizhu/marcizhu/issues/new?body=Please+do+not+change+the+title.+Just+click+%22Submit+new+issue%22.+You+don%27t+need+to+do+anything+else+%3AD&title=Chess%3A+Move+G5+to+D2) |
<!-- END MOVES LIST -->

Having fun? Ask a friend to do the next move!

#### How it works

When you click on a link and submit a new issue with the desired move, a GitHub action is triggered, which in turn runs a small python script that performs the specified movement, updates this README file and commits the changes.

Have you spotted a bug? Something missing? Feel free to open an [issue](https://github.com/marcizhu/readme-chess/issues) and I will try to fix it as soon as possible :D


<details>
  <summary>Last 5 moves in this game</summary>
  <!-- BEGIN LAST MOVES -->

| Move | Author |
| :--: | :----- |
| `F8` to `B4` | [ @MatissesProjects](https://github.com/MatissesProjects) |
| `D5` to `B6` | [ @MatthiasGN](https://github.com/MatthiasGN) |
| `F7` to `E6` | [ @olmemer](https://github.com/olmemer) |
| `C3` to `D5` | [ @marcizhu](https://github.com/marcizhu) |
| `A5` to `A4` | [ @GarrySarry](https://github.com/GarrySarry) |

<!-- END LAST MOVES -->
</details>

<details>
  <summary>Top 10 most moves across all games</summary>
  <!-- BEGIN TOP MOVES -->

| Total moves |  User  |
| :---------: | :----- |
| 692 | [@JohnyP36](https://github.com/JohnyP36) |
| 378 | [@marcizhu](https://github.com/marcizhu) |
| 358 | [@mishmanners](https://github.com/mishmanners) |
| 196 | [@KubaRocks](https://github.com/KubaRocks) |
| 116 | [@the1Riddle](https://github.com/the1Riddle) |
| 109 | [@viktoriussuwandi](https://github.com/viktoriussuwandi) |
| 68 | [@N-NeelPatel](https://github.com/N-NeelPatel) |
| 67 | [@lulunac27a](https://github.com/lulunac27a) |
| 65 | [@huuquyet](https://github.com/huuquyet) |
| 62 | [@herndev](https://github.com/herndev) |

<!-- END TOP MOVES -->
</details>

---

Do you want to make your own? Check out my [readme chess template](https://github.com/marcizhu/readme-chess)!
![](https://hit.yhype.me/github/profile?user_id=6199781)
