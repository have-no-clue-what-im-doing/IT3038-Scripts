# Requirements and Dependencies:

This script checks to see if there is Newcastle United FC game for the day, and if there is, power on a remote computer and display the game.

There are also two versions of this script for either Windows or Debian based Linux\
To test this script you will need the following:

1 Windows computer to display the Newcastle game (as host)\
1 Windows / Linux computer to run the script (as client)

The host machine must have a NIC that allows wake on lan. Otherwise you will have to manually turn on the machine yourself before running the script

Both machines will need `SSH`\
For most Linux distros it should be installed by default. If not you can run `sudo apt-get install openssh-client`\
For windows machines you will need to install [OpenSSH](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell) 
Be sure to add firewall rules to allow SSH traffic.

For the Windows host machine, you need to enable [auto-login](https://learn.microsoft.com/en-us/troubleshoot/windows-server/user-profiles-and-logon/turn-on-automatic-logon)

Be sure to make note of the following on your host machine:

`Username`\
`Password`\
`IP Address`\
`MAC Address`\


For the following functions you will have to add in your own login and machine info:\
`PowerOnComputer`\
`RestartComputer`\
`CreateChromeShortcut`\

Yes, having the password in plain text is bad practice, but this has already taken up enough of my time

Also ensure both machines are on the same broadcast domain so wake on lan works

You'll also need Peacock and YoutubeTV. Technically not if you just want to see if it work without watching the game.

#Installation

This script runs off of Python and Powershell. Your host machine must have Powershell and your client machine must have both Python and Powershell\
[Link to download Python](https://www.python.org/downloads/)\
Powershell should be downloaded by default on Windows unless you disabled / uninstalled it

Before running the script, be sure to install all dependencies:\
`pip install -r requirments.txt` 

If you're running the script off Linux you will also need wakeonlan, which can be installed here:
`apt-get install wakeonlan`

Once all requirements are downloaded and installed you are good to run the script. Feel free to have this run via task scheduler or as a cron job. Best time would be in morning, a couple hours before 9am local time. 