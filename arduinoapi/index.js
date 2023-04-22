const express = require('express');
const app = express();

const { SerialPort } = require('serialport')
const port = new SerialPort({
  path: '/dev/ttyACM0',
  baudRate: 9600,
})

port.on('readable', function () {
  console.log('Data:', port.read())
})

app.get("/d", (req, res) => {
    var led = req.params.led;
    port.write("0101")
    res.status("200").send("Done.")
})

app.listen(3000, () => {
    console.log("running")
})