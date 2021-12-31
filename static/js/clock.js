let playing = false;
let currentPlayer = 1;
const buttonPvP = document.querySelector('.newgamePvP');
const buttonPvM = document.querySelector('.newgame');

const padZero = (number) => {
    if (number < 10) {
        return '0' + number;
    }
    return number;
}
class Timer {
    constructor(player, minutes) {
        this.player = player;
        this.minutes = minutes;
    }
    getMinutes(timeId) {
        return document.getElementById(timeId).textContent;
    }
}

// Create an instance of the timer for each player.

let p1time = new Timer('min1', document.getElementById('min1').textContent);
let p2time = new Timer('min2', document.getElementById('min2').textContent);
// Swap player's timer after a move (player1 = 1, player2 = 2).

const swapPlayer = () => {
    if (!playing) return;
    currentPlayer = currentPlayer === 1 ? 2 : 1;
}

// Start timer countdown to zero.
let timerId;
const startTimer = () => {
    playing = true;
    let p1sec = 60;
    let p2sec = 60;

    timerId = setInterval(function() {
        // Player 1.
        if (currentPlayer === 1) {
            if (playing) {
                p1time.minutes = parseInt(p1time.getMinutes('min1'), 10);
                if (p1sec === 60) {
                    p1time.minutes = p1time.minutes - 1;
                }
                p1sec = p1sec - 1;
                document.getElementById('sec1').textContent = padZero(p1sec);
                document.getElementById('min1').textContent = padZero(p1time.minutes);
                if (p1sec === 0) {
                    // If minutes and seconds are zero stop timer with the clearInterval method.
                    if (p1sec === 0 && p1time.minutes === 0) {
                        let status = document.querySelector('#status');
                        status.innerHTML = "White: Time Out!";
                        let layer = document.querySelector('#layer_game_over');
                        layer.classList.add("layer");
                        // Stop timer.
                        clearInterval(timerId);
                        playing = false;
                    }
                    p1sec = 60;
                }
            }
        } else {
            // Player 2.
            if (playing) {
                p2time.minutes = parseInt(p2time.getMinutes('min2'), 10);
                if (p2sec === 60) {
                    p2time.minutes = p2time.minutes - 1;
                }
                p2sec = p2sec - 1;
                document.getElementById('sec2').textContent = padZero(p2sec);
                document.getElementById('min2').textContent = padZero(p2time.minutes);
                if (p2sec === 0) {
                    // If minutes and seconds are zero stop timer with the clearInterval method.
                    if (p2sec === 0 && p2time.minutes === 0) {
                        let status = document.querySelector('#status');
                        status.innerHTML = "Black: Time Out!";
                        let layer = document.querySelector('#layer_game_over');
                        layer.classList.add("layer");
                        // Stop timer.
                        clearInterval(timerId);
                        playing = false;
                    }
                    p2sec = 60;
                }
            }
        }
    }, 1000);
}

function setTimerPvP(timer){
    clearInterval(timerId);
    currentPlayer = 1;
    console.log(timer);
    document.getElementById('min1').innerHTML = timer;
    document.getElementById('sec1').innerHTML = '00';
    document.getElementById('min2').innerHTML = timer;
    document.getElementById('sec2').innerHTML = '00';
    var remove_class_layer = document.querySelector("#layer_game_over");
    if(remove_class_layer.className = "layer")
        remove_class_layer.classList.remove("layer");
    if(timer != "00")
        startTimer();
    // location.reload(true);
  }

function setTimerPvM(timer,user) {
    clearInterval(timerId);
    currentPlayer = 1;
    console.log(timer + " " + user);
    if(user == 'b') currentPlayer = 2;
    document.getElementById('min1').innerHTML = timer;
    document.getElementById('sec1').innerHTML = '00';
    document.getElementById('min2').innerHTML = timer;
    document.getElementById('sec2').innerHTML = '00';
    var remove_class_layer = document.querySelector("#layer_game_over");
    if(remove_class_layer.className = "layer")
        remove_class_layer.classList.remove("layer");
    if(timer != "00")
        startTimer();
    // location.reload(true);
  }
