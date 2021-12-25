let playing = false;
let currentPlayer = 1;
const buttonPvP = document.querySelector('.pvp');
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

buttonPvP.addEventListener('click', () => {
    clearInterval(timerId);
    currentPlayer = 1;
    document.getElementById('min1').innerHTML = '10';
    document.getElementById('sec1').innerHTML = '00';
    document.getElementById('min2').innerHTML = '10';
    document.getElementById('sec2').innerHTML = '00';
    startTimer();
    // location.reload(true);
  });

buttonPvM.addEventListener('click', () => {
    clearInterval(timerId);
    currentPlayer = 1;
    if(form.elements["color"].value === 'b') currentPlayer = 2;
    document.getElementById('min1').innerHTML = '10';
    document.getElementById('sec1').innerHTML = '00';
    document.getElementById('min2').innerHTML = '10';
    document.getElementById('sec2').innerHTML = '00';
    startTimer();
    // location.reload(true);
  });  