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


const carouselSlide = document.querySelector(".carousel-slide");
const carouselImages = document.querySelectorAll(".carousel-slide img");

//Buttons
const prevBtn = document.querySelector("#prevBtn");
const nextBtn = document.querySelector("#nextBtn");

//Counter
let counter = 1;
const size = carouselImages[0].clientWidth;

carouselSlide.style.transform = "translateX(" + -size * counter + "px)";

//Button Listeners
nextBtn.addEventListener("click", () => {
    if(counter >= carouselImages.length - 1) return;
    carouselSlide.style.transition = "transform 0.8s ease-in-out";
    counter++;
    carouselSlide.style.transform = "translateX(" + -size * counter + "px)";
});

prevBtn.addEventListener("click", () => {
    if(counter <= 0) return;
    carouselSlide.style.transition = "transform 0.8s ease-in-out";
    counter--;
    carouselSlide.style.transform = "translateX(" + -size * counter + "px)";
});

carouselSlide.addEventListener("transitionend", () => {
    if (carouselImages[counter].id === 'lastClone') {
        carouselSlide.style.transition = "none";
        counter = carouselImages.length -2;
        carouselSlide.style.transform = "translateX(" + -size * counter + "px)";
    }
    if (carouselImages[counter].id === 'firstClone') {
        carouselSlide.style.transition = "none";
        counter = carouselImages.length - counter;
        carouselSlide.style.transform = "translateX(" + -size * counter + "px)";
    }
});

const carouselSlide2 = document.querySelector(".carousel-slide2");
const carouselImages2 = document.querySelectorAll(".carousel-slide2 img");

//Buttons
const prevBtn2 = document.querySelector("#prevBtn2");
const nextBtn2 = document.querySelector("#nextBtn2");

//Counter
let counter2 = 1;
const size2 = carouselImages2[0].clientWidth;

carouselSlide2.style.transform = "translateX(" + -size2 * counter2 + "px)";

//Button Listeners
nextBtn2.addEventListener("click", () => {
    if(counter2 >= carouselImages2.length - 1) return;
    carouselSlide2.style.transition = "transform 0.8s ease-in-out";
    counter2++;
    carouselSlide2.style.transform = "translateX(" + -size2 * counter2 + "px)";
});

prevBtn2.addEventListener("click", () => {
    if(counter2 <= 0) return;
    carouselSlide2.style.transition = "transform 0.8s ease-in-out";
    counter2--;
    carouselSlide2.style.transform = "translateX(" + -size2 * counter2 + "px)";
});

carouselSlide2.addEventListener("transitionend", () => {
    if (carouselImages2[counter2].id === 'lastClone') {
        carouselSlide2.style.transition = "none";
        counter2 = carouselImages2.length -2;
        carouselSlide2.style.transform = "translateX(" + -size2 * counter2 + "px)";
    }
    if (carouselImages2[counter2].id === 'firstClone') {
        carouselSlide2.style.transition = "none";
        counter2 = carouselImages2.length - counter2;
        carouselSlide2.style.transform = "translateX(" + -size2 * counter2 + "px)";
    }
});