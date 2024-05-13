# SSH FireWall
## Created by Tom Tubinas and Jason Tashman

## Description
The program uses Uncomplicated Firewall (ufw) for an linux machine with an ssh server on it. The firewall also has the ablitiy to read all the connection attempts in auth.log. In the event of an IP address attempting to gain unauthorized access to the ssh server, the firewall will try and pin down where the source is coming from.

## Set Up
1. Download the firewall on your linux machine
2. Navagate to the folder
3. Download the requirments with pip install -r requirements.txt
4. Open up logger.py
5. Put in the path of the auth.log into the script
6. Do the same with clean.py
