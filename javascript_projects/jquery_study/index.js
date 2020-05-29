//target h1 and add classes
$("h1").addClass("big-title margin-50");
//target h1 and update innerHTML
$("h1").html("JQuery STUFF");
//target h1, add click event listener and run function changing css color
$("h1").click(function() {
  $("h1").css("color", "seagreen");
});

//target button and update innerHTML
$("button").html("<em>DON'T CLiCK!</em>");
//target all buttons, add click listener and function that targets/updates h1 css color
$("button").click(function() {
  //target h1 and slides up or down on button click
  //   $("h1").slideToggle();
  //target h1 and fades in or out on button click
  //   $("h1").fadeToggle();
  //target h1 and slide up, slide back down before an animated opacity change - chained anumations
  $("h1")
    .slideUp()
    .slideDown()
    .animate({ opacity: 0.5 });
});

//target a tag and update attribute - href
$("a").attr("href", "https://www.mindenmusic.com");
//target a tag and update innerHTML
$("a").html("<strong>MINDEN!!</strong>");

//target input, add keypress listener and function that updates h1 text according to event.key
$("input").keypress(function(event) {
  $("h1").text(event.key);
});
// target input, use .on() method to add an event listener. listen for click and then update input css background-color
$("input").on("click", function() {
  $("input").css("background-color", "turquoise");
});
