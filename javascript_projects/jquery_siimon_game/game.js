var userClickedPattern = [];

var gamePattern = [];
gamePattern.push(randomColor);

var buttonColors = ["red", "blue", "green", "yellow"];

// var randomColor = buttonColors[Math.floor(Math.random() * 4)];

// var audio = new Audio("sounds/" + randomColor + ".mp3");

$(".btn").click(function() {
  var userChosenColor = this.id;
  userClickedPattern.push(userChosenColor);
});

function playSounds(name) {
  var name = new Audio("sounds/" + userChosenColor + ".mp3");
  $("#" + userChosenColor).click(function() {
    $("#" + userChosenColor)
      .fadeIn(100)
      .fadeIn(100)
      .fadeOut(100)
      .fadeIn(100);
    name.play();
  });
}

function animatePress(currentColor) {}

// $("#" + randomColor).click(function() {
//   $("#" + randomColor)
//     .fadeIn(100)
//     .fadeIn(100)
//     .fadeOut(100)
//     .fadeIn(100);
//   audio.play();
// });

function nextSequence() {
  var randomNumber = Math.floor(Math.random() * 4);
  var randomColor = buttonColors[Math.floor(Math.random() * 4)];
  var audio = new Audio("sounds/" + randomColor + ".mp3");
  $("#" + randomColor).click(function() {
    $("#" + randomColor)
      .fadeIn(100)
      .fadeIn(100)
      .fadeOut(100)
      .fadeIn(100);
    audio.play();
  });
}
