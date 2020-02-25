// load "express" modules
var express = require("express");    // require == import
var monogooes = require("mongoose") ;
var expressHandlebars = require("express-handlebars") ;

// crreate server 
var app = express() ;  // store module

//create schema 
var courseSchema = new monogooes.Schema ({
    courseno :Number , coursename : String , duretion : String 
}) ;
// create model 
var courseModel = monogooes.model ("courses" , courseSchema);

//set the "handelbars as view engine"
app.engine ("hbs" , expressHandlebars()) ;
app.set ("view engine", "hbs") ;

// start listener server
app.listen(6070) ;        // 1024 to 65535  proto no.
console.log("server started at port 6070");

app.get("/home" , function(req ,res) {
    res.sendfile(__dirname + "/home.html");
});
app.get ("/courses" , function(req , res)
{
    monogooes.connect ("mongodb ://localhost/nareshit") ;  //connect to db



    //find(retrive data) from database
    courseModel.find(function(err,data)
    {
                //connect to db
        mongoose.connect("mongodb://localhost/nareshit" , {
            useNewUrlParser:true , useUnifiedTopology :true
        });

        //find (retrieve data) from database
        CourseModel.find(function(err, data) {
            if (err == null)
            {
            //success (data loaded from db)
            console.log(data);
            res.render("courses.hbs", { courses: data, layout: false } );
            //res.send(data);
            }
            else
            {
            //failure (data not loaded)
            console.log(err);
            res.send("Error");
            }
            
            mongoose.connection.close();  
        });
    });


app.get ("/contact" , function (req, res ){
    res.sendfile(__dirname + "/contact.html");        // __dirnamme = current path file location
}) ;

