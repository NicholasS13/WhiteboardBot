# WhiteboardBot
## To get this code to work you will need to make edits to your installs
You'll need to install a lower version of board manager esp32 by espressif. I installed version 2.0.17.

Also, you will need to install a lower version of the library ArduinoJson by Benoit Blanchon. I installed version 6.21.5.

Once you've done that, reinstall the Painless Mesh library to undo any changes you made to the source code.

## To send messages wirlessly
### install color_test_Recieve code to a random esp
### plug that esp into a device with serial monitor and wait for one of the devices to turn their LED yellow
### type commands in there and make sure there is conditions for them in the RC function in color_stuff_FINAL's MESHOTA.h

## To wirelessly update
### Export code's compiled binary, need the bin file from that folder (in this case should be called "color_stuff_FINAL.ino.bin")
### start up mobile hotspot or connect ESP to same wifi as this device, make sure it has your device IP
### open the directory with the bin file and start a http server (python3 -m http.server)
### send 'update' wirelessly to the light sensing esp then wait for led to go magenta then green, then press reset button