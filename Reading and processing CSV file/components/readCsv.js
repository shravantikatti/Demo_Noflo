// Produce an asynchronous function wrapping a NoFlo graph
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

    var filename=input.getData('in');
    const {spawn} = require('child_process');
    const python = spawn('python', ['readCsv.py',filename]);      
      var dataToSend;
      python.stdout.on('data', function (data) {
        dataToSend = data.toString();
        output.send({
          out: dataToSend 
        });
      });
    
      output.done();
     
  });
  return c;
}