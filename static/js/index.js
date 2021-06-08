document.getElementById("ienakt").addEventListener("click", () => {
  let popUp = document.getElementById("popUp");
  popUp.style.display = "block";
});

let x = document.getElementById("login");
let y = document.getElementById("register");
let z = document.getElementById("btn");

function register() {
  x.style.left = "-400px";
  y.style.left = "50px";
  z.style.left = "100px";
}

function login() {
  x.style.left = "50px";
  y.style.left = "450px";
  z.style.left = "0px";
}

document.getElementById("iziet").addEventListener("click", () => {
  let popUp = document.getElementById("popUp");
  popUp.style.display = "none";
});