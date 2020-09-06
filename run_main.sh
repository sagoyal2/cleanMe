#!/bin/bash

#add this to .bash_profile
#https://gist.github.com/bobthecow/757788
# tab call_main.py

#import os
#open new terminal and run command
#https://stackoverflow.com/questions/39840632/launch-python-script-in-new-terminal
#os.system("""osascript -e 'tell application "Terminal" to do script "python Documents/cleanMe/main.py"'""")



#modifed from https://gist.github.com/bobthecow/757788
#this script will open a new tab in iTerm2 and run the main.py program

#set up cron job permission: https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/

osascript -i <<EOF
    tell application "iTerm2"
            tell current window
                    create tab with default profile
                    tell the current session
                            write text "cd /Users/hgm/Documents/cleanMe && python main.py"
                    end tell
            end tell
    end tell
EOF