function onDragStartPvm(source, piece, position, orientation) {
  if (game.game_over()) return false;

  if (
    (game.turn() === "w" && piece.search(/^b/) !== -1) ||
    (game.turn() === "b" && piece.search(/^w/) !== -1)
  ) {
    return false;
  }

  if (piece.search(`^${user == "b" ? "w" : "b"}`) !== -1) return false;
}

function requestMove(source, target, promotion) {
  fetch("/getmove", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ from: source, to: target, promotion }),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data["from"], data["to"]);
      swapPlayer();
      game.move({
        from: data["from"],
        to: data["to"],
        promotion: data["promotion"],
      });
      boardPvm.position(game.fen());
      updateStatus();
    });
  console.log(source, target);
  swapPlayer();
}

const timeout = async (ms) => new Promise((res) => setTimeout(res, ms));

async function waitUserInput() {
  while (localStorage.getItem("promotionStatus") == "false"){ await timeout(50);}; // pause script but avoid browser to freeze ;)
}

async function onDropPvm(source, target, piece) {
  // console.log(source, target, piece);
  console.log(1);
  var check = game.move({
    from: source,
    to: target,
    promotion: "q",
  });
  if (check === null) return "snapback";
  else game.undo();

  // console.log(source, target, piece);
  if (
    piece.search("P") !== -1 &&
    (target.charAt(1) == "8" || target.charAt(1) == "1")
  ) {
    localStorage.setItem("promotionStatus", "false");
    promotionModal.show();
  } else {
    localStorage.setItem("promotionStatus", "true");
    localStorage.setItem("promotion", "");
  }

  await waitUserInput();

  var move = game.move({
    from: source,
    to: target,
    promotion: localStorage.getItem("promotion"),
  });

  // illegal move
  // if (move === null) return "snapback";

  boardPvm.position(game.fen());

  // make legal move
  requestMove(source, target, localStorage.getItem("promotion"));

  updateStatus();
}

// update the board position after the piece snap
// for castling, en passant, pawn promotion
function onSnapEndPvm() {
  boardPvm.position(game.fen());
  updateStatus();

}

function updateStatus() {
  var status = "";

  var moveColor = "White";
  if (game.turn() === "b") {
    moveColor = "Black";
  }

  // checkmate?
  if (game.in_checkmate()) {
    status = "Game over, " + moveColor + " is in checkmate.";
    clearInterval(timerId);
  }

  // draw?
  else if (game.in_draw()) {
    status = "Game over, drawn position";
    clearInterval(timerId);
  }

  // game still on
  else {
    status = moveColor + " to move";

    // check?
    if (game.in_check()) {
      status += ", " + moveColor + " is in check";
    }
  }

  $status.html(status);
  $fen.html(game.fen());
  $pgn.html(game.pgn());
}

var configPvm = {
  draggable: true,
  position: "start",
  pieceTheme: "/static/img/chesspieces/{piece}.png",
  onDragStart: onDragStartPvm,
  onDrop: onDropPvm,
  onSnapEnd: onSnapEndPvm,
};
