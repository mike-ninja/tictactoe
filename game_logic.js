let playerText = document.getElementById("playerText")
let restartBtn = document.getElementById("restartBtn")
let boxes = document.getElementsByClassName("box")

let winnerIndicator = getComputedStyle(document.body).getPropertyValue('--winning-blocks')    

const O_TEXT = "O"
const X_TEXT = "X"
let currentPlayer = X_TEXT
let spaces = Array(9).fill(null)

const startGame = () => {
    for (let i = 0; i < boxes.length; i++) {
        boxes[i].addEventListener('click', boxClicked)
    }
}

function boxClicked(event) {
    const id = event.target.id
    if (!spaces[id]) {
        spaces[id] = currentPlayer
        event.target.innerText = currentPlayer

        if (playerHasWon() !== false){
            playerText = `${currentPlayer} has won!`
            let winningBlocks = playerHasWon()
            
            winningBlocks.map ( box => boxes[box].style.backgroundColor = winnerIndicator)
            return            

        }
        currentPlayer = currentPlayer == X_TEXT ? O_TEXT : X_TEXT
    }
}

const winningCombos = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

function playerHasWon() {
    for (const condition of winningCombos) {
        let [a, b, c] = condition

        if (spaces[a] && (spaces[a] == spaces[b] && spaces[b] == spaces[c])) {
            return [a, b, c]
        }
    }
    return false
}

restartBtn.addEventListener('click', restart)

function restart() {
    spaces.fill(null)
    for (let i = 0; i < boxes.length; i++) {
        boxes[i].innerText = ''
        boxes[i].style.backgroundColor =''
    }

    playerText = "Tic Tac Toe"

    currentPlayer = X_TEXT
}

startGame()