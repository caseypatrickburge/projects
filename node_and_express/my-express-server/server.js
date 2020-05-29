//defines express requirement as express
const express = require("express");
//defines express funciton as app
const app = express();
//specifies the request and response with .get
app.get("/", function(req, res) {
  res.send("<h1>Hello World!</h1>");
});
//instructs app to listen to port 3000
app.listen(3000, function() {
  //logs a response in hyper to notify server is serving
  console.log("Server started on port 3000");
});
