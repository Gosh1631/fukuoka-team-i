const SerialPort = require('serialport');
const Readline = SerialPort.parsers.Readline;

const portName = '/dev/cu.usbmodem14401';
const port = new SerialPort(portName, { baudRate: 9600 })
  .pipe(new Readline())
  .on('data', data => {
    try {
      let jsonData = JSON.parse(data);
    console.log(jsonData);  
    } catch (error) {
      // 開始時などデータが受信できないことがある
      return;
    }
  });