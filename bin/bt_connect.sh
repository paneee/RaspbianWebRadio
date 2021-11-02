#!/bin/bash
# start pulseaudio
pulseaudio --start

# connect bluetooth speaker
# BT-Tool ohne root-Rechte aufrufen
bluetoothctl << EOF
connect F4:4E:FD:7B:E3:44
quit
EOF

