const express = require('express');
const app = express();

const { SerialPort } = require('serialport')
const port = new SerialPort({
  path: 'COM7',
  baudRate: 9600,
})

port.on('readable', function () {
  console.log('Data:', port.read())
})

app.get("/d", (req, res) => {
    var led = req.params.led;
    port.write("d")
    res.status("200").send("Done.")
})

app.get("/l/:id?", (req, res) => {
  var led = req.params.id;
  if (led == "1") {
    port.write("q")
  } else if (led == "2") {
    port.write("w")
  }
  res.status("200").send("Done.")
})

app.listen(3000, () => {
    console.log("running")
})