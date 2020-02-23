// load "express" modules
var express = require("express");    // require == import
var monogooes = require("mongoose") ;
// var expressHandlebars = require("express-Handlebars") ;

// crreate server 
var app = express() ;  // store module

//create schema 
var courseSchema = new monogooes.Schema ({
    courseno :Number , coursename : String , duretion : String 
}) ;
// create model 
var courseModel = monogooes.model ("courses" , courseSchema);

//set the "handelbars as view engine"
//app.engine ("hbs" , expressHandlebars()) ;
// app.set ("view engine", "hbs") ;

// start listener server
app.listen(6070) ;
console.log("server started at port 6070");

app.get("/home" , function(req ,res) {
    // monogooes.connect ("mongodb ://localhost/naresgit") ;  //connect to db

    //find(retrive data) from database
    courseModel.find(function(err,data)
    {
        if (err = null)
        {
            //success
            console.log(data);
            res.render("courses.hbs" , {courses : data , layout :false}) ;
            //res.send(daa);
        }
        else
        {
            //failure(data not loaded)
            console.log(err);
            res.send("Error")
        }
        monogooes.connection.close() ;});
    
    });
    
    
    
    
    console.log("Request received at /home") ;
    // res.send("Helo from server") ;
    res.sendfile(__dirname + "/home.html") ;

}) ;

// 
app.get("/course" , function (req , res){
    res.sendfile(__dirname + "/courses.html") ;
}) ;

//
app.get ("/contact" , function (req, res ){
    res.sendfile(__dirname + "/contact.html");        // __dirnamme = current path file location
}) ;

