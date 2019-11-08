################################################################
# This script is used for setting the brightness of HDMI output.
# It executes xrandr command with given brightness value
# Developed by JamCry - jamcry.xyz - 10/2019
###################################################################

import subprocess
import sys

# Returns the command and args as array (to use in subprocess.call)
def get_args(brightness, output="HDMI-1-1"):
    full_command = "xrandr --output " + output + " --brightness " + str(brightness)
    command_args = full_command.split(" ")
    return command_args

# Set brightness to given percent
def set_brightness(percent):
    percent_perten = percent / 100
    command_args = get_args(percent_perten)
    while True:
        try:
            subprocess.check_output(command_args)
            print(f"☑ SET BRIGHTNESS TO {percent}%.")
            break
        except subprocess.CalledProcessError as e:
            print("☒ ERROR: Couldn't find the monitor. Trying again...\n...")
            command_args = get_args(percent_perten, "HDMI-1")
    
# Set new brigtness value to cmdline argument if any, 100 otherwise
new_brightness = int(sys.argv[1]) if (len(sys.argv) > 1) else 100

set_brightness(new_brightness)
