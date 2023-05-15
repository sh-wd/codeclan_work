const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());

app.listen(9000, function(){
    console.log("App running on port 9000");
});

app.get("/", function(req, res){
    res.json({message: "Hello World"});
});