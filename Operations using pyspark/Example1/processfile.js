// Produce an asynchronous function wrapping a NoFlo graph
var noflo = require('noflo');
const {spawn} = require('child_process');  

exports.getComponent = () => {
   const c = new noflo.Component();
   c.icon = 'file';
   c.inPorts.add('in', {
      datatype: 'all'
  });
  c.outPorts.add('out', {
    datatype: 'all'
  });
  c.outPorts.add('error', {
    datatype: 'object'
  });

  c.process((input, output) => {
    if (!input.hasData('in')) {
      return;
    }

   var data = input.getData('in');
    const python = spawn('python', ['example1.py']);
      
      var dataToSend;
      python.stdout.on('data', function (data) {
        //console.log('Pipe data from python script ...');
        dataToSend = data.toString();
        output.send({
          out: dataToSend 
        });
      });
          output.done();
     });
  return c;
}