#!/bin/bash
mkdir -p /var/log/capillary/tunnelManager/
echo 'Starting Tunnel Manager on port 6000. To shutdown: curl "http://127.0.0.1:6000/tunnel?command=shutdown"'
python tunnelManager.py >> /var/log/capillary/tunnelManager/tunnelmanager.out 2>&1
stty sane
echo 'Shutting down'
