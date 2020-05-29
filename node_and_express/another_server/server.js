const express = require("express");

const app = express();

app.get("/", function(req, res) {
  res.send(
    "<h1><strong>Okay, let's try out this nodemon utility-----FOR REAL THIS TIME!</strong></h1>"
  );
});

app.get("/secret", function(req, res) {
  res.send(
    "<h1>Even MORE serving!!!</h1><a href='http://google.com'>Search!</a>"
  );
});

app.get("/about", function(req, res) {
  res.send(
    "<h1>Jerry Seinfeld is a FUNNY GUY!</h1><a href='http://google.com'>Search!</a>"
  );
});

app.listen(3000, function() {
  console.log("Now listening on port 3000.");
});
