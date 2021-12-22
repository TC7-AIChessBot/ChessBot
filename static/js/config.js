var boardPvp = null;
var boardPvm = null;
var game = new Chess();
var $status = $("#status");
var $fen = $("#fen");
var $pgn = $("#pgn");
var user = null;

const pvpBtn = document.querySelector(".pvp");
const newGameBtn = document.querySelector(".newgame");
const myboardPvp = document.querySelector("#myBoardPvp");
const myboardPvm = document.querySelector("#myBoardPvm");
const boardCtn = document.querySelector(".boardContainer");
const form = document.querySelector(".formINPUT");

pvpBtn.addEventListener("click", () => {
  myboardPvm.style.display = "none";
  myboardPvp.style.display = "block";
  boardPvp?.start();
  game.reset();
  if (!boardPvp) boardPvp = Chessboard("myBoardPvp", configPvp);
  updateStatus();
});

newGameBtn.addEventListener("click", async () => {
  myboardPvm.style.display = "block";
  myboardPvp.style.display = "none";
  boardPvm?.start();
  game.reset();
  user = form.elements["color"].value;
  console.log(user);
  if (!boardPvm) boardPvm = Chessboard("myBoardPvm", configPvm);
  boardPvm.orientation(user == "b" ? "black" : "white");
  await fetch("/newgame", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      color: user == "b" ? "white" : "black",
      level: Number(form.elements["level"].value),
    }),
  })
    .then((res) => res.json())
    .then((data) => console.log(data));
  if (user == "b") {
    initMove = await fetch("/getmove", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ from: "null", to: "null", promotion: "" }),
    }).then((res) => res.json());
    console.log(initMove);
    game.move({ from: initMove["from"], to: initMove["to"] });
    boardPvm.position(game.fen());
  }
  updateStatus();
});

// pvmBtnBlack.addEventListener("click", async () => {
//   myboardPvm.style.display = "block";
//   myboardPvp.style.display = "none";
//   boardPvm?.start();
//   game.reset();
//   user = "b";
//   console.log(user);
//   if (!boardPvm) boardPvm = Chessboard("myBoardPvm", configPvm);
//   boardPvm.orientation(user == "b" ? "black" : "white");
//   await fetch("/newgame", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({ color: user == "b" ? "white" : "black" }),
//   })
//     .then((res) => res.json())
//     .then((data) => console.log(data));
//   if (user == "b") {
//     initMove = await fetch("/getmove", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({ from: "null", to: "null", promotion: "" }),
//     }).then((res) => res.json());
//     console.log(initMove);
//     game.move({ from: initMove["from"], to: initMove["to"] });
//     boardPvm.position(game.fen());
//   }
//   updateStatus();
// });

// var myModal = new bootstrap.Modal(document.getElementById("promotionModal"));
// const test = document.querySelector(".test");

// test.addEventListener("click", async () => {
//   localStorage.setItem("promotionStatus", "false");
//   myModal.show();
//   await waitUserInput();
//   console.log(localStorage.getItem("promotionStatus"));
//   //while (localStorage.getItem("promotionStatus") == "true") {}
// });
