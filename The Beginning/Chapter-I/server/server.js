//Load HTTP module
const http = require("http");
const hostname = '0.0.0.0';
const port = 5000;

/*
//Create HTTP server and listen on port 5000 for requests
const server = http.createServer((req, res) => {

  //Set the response HTTP header with HTTP status and Content type
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
});

//listen for request on port 5000, and as a callback function have the port listened on logged
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
*/

const express = require('express')
const app = express();
const bodyParser = require('body-parser')

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
})); 
app.use(express.static(__dirname + '/views'));
app.get('/', (req, res) => {
    res.sendFile('index.html');
});




/*
  Call api from the python server that runs locally
*/
app.post('/sendemail', (req, res) => {
    console.log(req.body.email);

    var request = require('request');
    
    // Send the email to python server that runs localy
    request.post(
        'http://127.0.0.1:6000/email',
        { json: { email: req.body.email } },
        function (error, response, body) {
            if (!error && response.statusCode == 200) {
                //msg = JSON.parse(body);
                req.msgFromPythonServer = "";
                
                console.log(body);
                console.log(body.result);

                // Decode the response from the python server
                switch(body.result){
                  case 0:
                    req.msgFromPythonServer = "Thanks for your time!";
                    break;
                  case '1':
                    req.msgFromPythonServer = "Your email is not valid!";
                    break;
                  case -1:
                    req.msgFromPythonServer = "Server: Mr. Guest i do not feel so good... \n And then he vanished. Now everything fall on Admin's shoulders.";
                  break;
                  default:
                    console.log("The result code from python server is not implemented!");
                }
                // Send the response from the python server back to the main page
                res.jsonp({ result: req.msgFromPythonServer });
            }
          else {
            req.msgFromPythonServer = "Something is rotten in Denmark";
            console.log("[ ! ] There is an error in the python server!");
            res.jsonp({ result: req.msgFromPythonServer });
          }
        }
    );
     
});

app.listen(port, hostname, () => {
  console.log('Server is up!');
});
