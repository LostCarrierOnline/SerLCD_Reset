# SerLCD_Reset
Simple tool to send a CR reset to the SerLCD
https://www.sparkfun.com/products/258

The reset will cause the serLCD to reset back to the default 9600 baud rate. I created this tool to reset one that had issues with
the backlight not functioning. The device seemed completely dead prior to the reset. Give it a shot.

Example output:

Welcome to the SerLCD Reset Tool!

According to the documentation if you send a CR within the few miliseconds during boot you can reset it.

Please ensure only power and ground are connected, once you start the proceedure connect your UART TX connection to the RX connector on your serLCD package.

['COM1']

Enter com port number ONLY: 1
Press Enter to Start Sending
Sending
press ctrl-c to stop
