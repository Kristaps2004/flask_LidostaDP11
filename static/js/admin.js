document.getElementById("pievienotLidostas").addEventListener("click", () => {
  let popUp = document.getElementById("popUp");
  popUp.style.display = "block";
});

document.getElementById("labotLidostas").addEventListener("click", () => {
  let popUp1 = document.getElementById("popUp1");
  popUp1.style.display = "block";
});

document.getElementById("dzestLidostas").addEventListener("click", () => {
  let popUp2 = document.getElementById("popUp2");
  popUp2.style.display = "block";
});

document.getElementById("pievienotLidmasinas").addEventListener("click", () => {
  let popUp3 = document.getElementById("popUp3");
  popUp3.style.display = "block";
});

document.getElementById("labotLidmasinas").addEventListener("click", () => {
  let popUp4 = document.getElementById("popUp4");
  popUp4.style.display = "block";
});

document.getElementById("dzestLidmasinas").addEventListener("click", () => {
  let popUp5 = document.getElementById("popUp5");
  popUp5.style.display = "block";
});

document.getElementById("pievienotReisi").addEventListener("click", () => {
  let popUp6 = document.getElementById("popUp6");
  popUp6.style.display = "block";
});

document.getElementById("labotReisi").addEventListener("click", () => {
  let popUp7 = document.getElementById("popUp7");
  popUp7.style.display = "block";
});

document.getElementById("dzestReisi").addEventListener("click", () => {
  let popUp8 = document.getElementById("popUp8");
  popUp8.style.display = "block";
});

document.getElementById("labott").addEventListener("click", () => {
  let popUp8 = document.getElementById("popUp8");
  popUp8.style.display = "block";
});

//form

function validateForm() {
  var x = document.forms["pievienotLidostuForm"]["nosaukums"].value;
  /*if (x == "") {
    alert("Nav ievadīts lidostas nosaukums");
    return false;
  }*/
}
