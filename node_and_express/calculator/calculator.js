const express = require("express");
const bodyParser = require("body-parser");
//enables body-parser - urlencode gives access to html form data
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
//express sends request to path - html file using __dirname (file path for server ops)
app.get("/", function(req, res) {
  res.sendFile(__dirname + "/bmicalculator.html");
});
//express sends response to path
app.post("/", function(req, res) {
  var weight = parseFloat(req.body.weight);
  var height = parseFloat(req.body.height);
  var result = (703 * weight) / Math.pow(height, 2);
  res.send("Your BMI is: " + Math.floor(result));
  console.log(weight, height, result);
});
//express listens to port 3000 - serves
app.listen(3000, function() {
  console.log("Express is listening on port 3000");
});
