//require express package
const express = require("express");
//require native https package in node
const https = require("https");
//require body-parser package
const bodyParser = require("body-parser");

//intitialize new express app
const app = express();
//use bodyParser to parse thru post request
app.use(bodyParser.urlencoded({ extended: true }));

//express get request and response
app.get("/", function (req, res) {
  res.sendFile(__dirname + "/index.html");
});

app.post("/", function (req, res) {
  console.log("Post request received!");
});

// const query = "London";
// const apiKey = "7c1c16239918b6e07d4c583e22ce4ec4";
// const units = "imperial";
// //save url in variable for easy fetch/use
// const url =
//   "https://api.openweathermap.org/data/2.5/weather?q=" +
//   query +
//   "&units=" +
//   units +
//   "&appid=" +
//   apiKey +
//   "";

// //use https to get response from api
// https.get(url, function (response) {
//   //log statusCode in command line
//   console.log(response.statusCode);

//   //receive data from api
//   response.on("data", function (data) {
//     //parse JSON and contain in weatherData variable
//     const weatherData = JSON.parse(data);
//     //log weatherData in console
//     console.log(weatherData);

//     //put data values into variables for further use
//     const temp = weatherData.main.temp;
//     const icon = weatherData.weather[0].icon;
//     const imageURL = "http://openweathermap.org/img/wn/" + icon + "@2x.png";
//     const description = weatherData.weather[0].description;

//     //send response to browser
//     res.write(
//       "<h1>The current temperature in " +
//         query +
//         " is " +
//         temp +
//         " degrees Fahrenheit.</h1>"
//     );
//     res.write("<h3>Current  weather condition: " + description + "</h3>");
//     res.write("<img src=" + imageURL + ">");
//     res.send();
//   });
// });

//listen on port 3000
app.listen(3000, function () {
  console.log("Server is running on port 3000");
});
