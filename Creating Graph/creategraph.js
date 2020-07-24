// Produce an asynchronous function wrapping a NoFlo graph
const noflo = require('noflo');
const {spawn} = require('child_process');
    
exports.getComponent = () => {
  
  const c = new noflo.Component();
  
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

    const df=input.getData('in');
    
    const python = spawn('python', ['processinsurance.py',df]);
    
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