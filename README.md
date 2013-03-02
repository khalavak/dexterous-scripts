dexterous-scripts
=================

A collection of handy(dexterous) scripts that make life on a *nix box fun and easy.

confscreens.py
==============

Confscreens.py is a python script that can be used to easily switch Xrandr configurations by
configuring the needed xrandr commands in the script and then call the script to cycle through the different modes or pass the mode along as argument.

See the confscreen.py script for more details. 


    confscreens.py --help
    usage: confscreens.py [-h] [-1] [-2] [-3] [-4] [-5] [-6] [-s] [-v]

    Configure screen setups wth Xrandr

    optional arguments:
      -h, --help     show this help message and exit
      -1, --one      Configure LVDS and VGA-0 with --auto and external above
                     laptop screen
      -2, --two      Configure LVDS with --auto and VGA-0 with 1024x768(needed for
                     some projectors to work properly
      -3, --three    Configure screen mirroring on LVDS and VGA-0 with --auto
      -4, --four     Configure scereen mirroring on LVDS and HDMI-0 with --auto
      -5, --five     Configure multiple screens LVDS, DisplayPort-2 and VGA-0
      -6, --six      Configure latop LVDS screen only
      -s, --show     Show Xrandr screen settings
      -v, --verbose  Show verbose debugging information


