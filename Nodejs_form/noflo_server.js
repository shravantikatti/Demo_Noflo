var noflo = require('noflo');

exports.getComponent = () => {
  
  const c = new noflo.Component();

  c.description = 'multiply a number';
  c.icon = 'file';

  c.inPorts.add('in', {
      datatype: 'int'
  });
  c.outPorts.add('out', {
    datatype: 'all'
  });
  
  c.process((input, output) => {

    if (!input.hasData('in')) {
      return;
    }
	var express = require('express');
	var app = express();
	var bodyParser = require('body-parser');

// Create application/x-www-form-urlencoded parser
	var urlencodedParser = bodyParser.urlencoded({ extended: false })

	app.use(express.static('public'));
	app.get('/index.html', function (req, res) {
   	res.sendFile( __dirname + "/" + "index.html" );	
	})

	app.post('/process_post', urlencodedParser, function (req, res) {
   // Prepare output in JSON format
   	response = {
      first_name:req.body.first_name,
      last_name:req.body.last_name
   };
   console.log("Print Data")
   output.send({
          out: response 
   });
//   console.log(response);
   res.end(JSON.stringify(response));
	})
/*
app.get('/process_get', function (req, res) {
   // Prepare output in JSON format
   response = {
      first_name:req.query.first_name,
      last_name:req.query.last_name
   };
   console.log(response);
   res.end(JSON.stringify(response));
})
*/
var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})


});
  return c;
}