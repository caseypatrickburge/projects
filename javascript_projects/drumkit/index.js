//define length of drums for use in for loop
var numOfDrums = document.querySelectorAll(".drum").length;
//define drums  - class = "drum"
var drums = document.querySelectorAll(".drum");

//define audio
var tom1 = new Audio("sounds/tom-1.mp3");
var tom2 = new Audio("sounds/tom-2.mp3");
var tom3 = new Audio("sounds/tom-3.mp3");
var tom4 = new Audio("sounds/tom-4.mp3");
var snare = new Audio("sounds/snare.mp3");
var crash = new Audio("sounds/crash.mp3");
var kick = new Audio("sounds/kick-bass.mp3");

// detecting button press
for (i = 0; i < numOfDrums; i++) {
  drums[i].addEventListener("click", function handleClick() {
    var buttonInnerHTML = this.innerHTML;
    makeSound(buttonInnerHTML);
    buttonAnimation(buttonInnerHTML);
    // tom1.play();
  });
}

// detecting keyboard press
document.addEventListener("keypress", function() {
  makeSound(event.key);
  buttonAnimation(event.key);
});

function makeSound(key) {
  switch (key) {
    case "w":
      tom1.play();
      break;
    case "a":
      tom2.play();
      break;
    case "s":
      tom3.play();
      break;
    case "d":
      tom4.play();
      break;
    case "j":
      snare.play();
      break;
    case "k":
      crash.play();
      break;
    case "l":
      kick.play();
      break;

    default:
      console.log(buttonInnerHTML);
      break;
  }
}

document.addEventListener("keypress", function() {
  makeSound(event.key);
});

function buttonAnimation(currentKey) {
  // add pressed class to button - transparency & shadow
  var activeButton = document.querySelector("." + currentKey);
  activeButton.classList.add("pressed");
  // create timeout to toggle pressed class after .1 second
  setTimeout(function() {
    activeButton.classList.toggle("pressed");
  }, 100);
}
