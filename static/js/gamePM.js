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

function requestMove(source, target) {
  fetch("/getmove", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ from: source, to: target }),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data["from"], data["to"]);
      game.move({
        from: data["from"],
        to: data["to"],
        promotion: "q",
      });
      boardPvm.position(game.fen());
      updateStatus();
    });
  console.log(source, target);
}

function onDropPvm(source, target) {
  var move = game.move({
    from: source,
    to: target,
    promotion: "q",
  });

  // illegal move
  if (move === null) return "snapback";

  boardPvm.position(game.fen());

  // make legal move
  requestMove(source, target);

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
  }

  // draw?
  else if (game.in_draw()) {
    status = "Game over, drawn position";
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
