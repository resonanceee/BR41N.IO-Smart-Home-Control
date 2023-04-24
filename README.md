# [Home Thinker](https://github.com/resonanceee/BR41N.IO-Smart-Home-Control)

## General info
### Overview
[Home Thinker](https://github.com/resonanceee/BR41N.IO-Smart-Home-Control) is a project that uses various arduino components to emulate a smart home that can be controlled by the Unicorn Hybrid Black BCI device.

### Prerequisites
#### Software:
Unicorn Speller
#### Hardware:
Unicorn Hybrid Black BCI
Arduino Breadboard
LED(1x)(the light)
Arduino Engine Block (for the door)
Arduino Servo Motors (2x)(for the blinds)


### main.py and custom board information
If you are going to change stuff in the custom board never forget to add the identifiers before and after the output in the board editor section of the unicorn speller. Note that you can also put your own identifiers in if you wish to, just make sure that they can only be found in the output, not in the filename, item name or simply the UDP request overall.


### Usage
##### BEWARE: YOU WILL NEED TO SET UP YOUR OWN ARDUINO COMPONENTS AND CONNECT THEM CORRECTLY TO THE REST OF THE CODE BY YOURSELF
To use the [Home Thinker](https://github.com/resonanceee/BR41N.IO-Smart-Home-Control) you need to start unicorn speller, load the custom board, run index.js (located in the arduinoapi folder) and run main.py (located in the receiver folder).
After doing that you may calibrate the sensors and and use the program.


<img src="https://i.imgur.com/apkin9h.gif" width="800">
