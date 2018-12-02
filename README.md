# Net-Recon
Various scripts used to mix up the user's ip and mac in order to bypass ip/mac blocks of traffic. Purely educational, any good firewall will stop nmap anyway. Good use for this is to try and write a counter script that detects the mac/ip change and updates the blocked connection in real time without blocking the whole network.

# To add?
sudo ifconfig wlo1 down && sudo macchanger -r wlo1 && sudo ifconfig wlo1 up

