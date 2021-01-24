// Setup empty JS object to act as endpoint for all routes
projectData = {};

// Require Express to run server and routes
const express=require('express');
// Start up an instance of app
const app=express();
/* Middleware*/
const bodyParser=require("body-parser")
//Here we are configuring express to use body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Cors for cross origin allowance
const cors=require("cors");
app.use(cors());
// Initialize the main project folder
app.use(express.static('website'));


// Setup Server
    const port = 3000;
//spin up the server
const server = app.listen(port, listening);
function listening() { console.log('server is running '+port) };


/****************************************************************************************************** */
//post route to recieve data from app.js
app.post('/add',addData);

function addData(req,res){ 
projectData['date'] = req.body.date;
projectData['temp'] = req.body.temp;
projectData['content'] = req.body.content;
console.log("post route ",projectData);
res.send(projectData);
}
/************************************************************************************************ */
//get route to send projectData to app.js
app.get("/all",sendData);

function sendData(req,res){
    console.log("get route ",projectData)
    res.send(projectData);
}

