# Robotic Knee Brace
Assisted walking software for prototype robotic knee brace for users with ALS, MS, MD, etc. The idea is to detect intention to move based on the user's slight movement, then the servo assists in that direction until resistance is detected.


![Knee_Brace](https://github.com/Miimiikiu/Knee-Brace/assets/128089127/2922a470-7a53-4587-b4b8-16d7c9a7749d)

## Usage

Hardware Required: 3D printed STL files (will soon update with those files), Raspberry Pi 3B+, Battery, Boost/Buck Converters (depending on your choice of battery), Servomotor
Software Required: pigpio, Adafruit_GPIO, Adafruit_MCP3008, Ubuntu Server, Python 3.6+ 

### motor_control.py

Main script to read the pressure sensor and watch the servo respond, or just test the servo with manual input.

From this repo's home directory:

`pigpiod` to start the pigpio daemon.

`python3 ./motor_control.py` to run the main script.

When prompted, discrete (0) is for is for accepting manual input for pulse width as integers (valid from 500-2500), whereas binary (1) is for full flexion or full extension for testing purposes.
Manual (0) is for manual entry into the terminal whereas pressure sensing (1) uses the knee brace's pressure sensor as input instead.

### motor_control_automatic.py

This file is the same as motor_control.py but jumps straight into using the pressure sensor without prompting. This was for my own ease of access at the time but I'll remove it soon to consolidate.
From this repo's home directory:

`pigpiod` to start the pigpio daemon.

`python3 ./motor_control_automatic.py` to run the main script.


## #TODO
-Originally made for Raspberry Pi 3B+. Migrate to ESP32 for better performance, efficiency, reliability and especially faster startup.

-Currently only works with one pressure sensor but at least two pressure sensors + stretch sensor band should be required.

-Shin brace should be adjustable but snug.

-Redesign & upload STL files for new hardware compatibilty.

-Properly document wiring.
