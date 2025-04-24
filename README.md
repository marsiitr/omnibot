# 3 Wheel Omni Wheel Drive
**Move efficiently and easily**

## Introduction

The 3 Wheel Omni Wheel Drive runs the OmniBot using an RC controller (FlySky FS-i6), utilizing ticks for control. It employs three channels: one for providing Vx velocity, another for Vy velocity relative to motor 1, and a third for angular velocity about its own axis. The bot uses NEMA 17 stepper motors to drive the wheels, mounted on a 3D-printed base with omni wheels. Powered by a Raspberry Pi 4B, the system runs all three motors simultaneously and is designed to accommodate future enhancements.

# Omni Bot RC Control - Quick Start Guide

## 1. Hardware Setup

### Components Required
- FlySky FS-i6 Transmitter + iA6B Receiver
- Raspberry Pi 4B (with power supply)
- 3 × Omni-wheel motors + A4988 drivers + battery
- 3 × female-female jumper wires
- (Optional) Logic-level shifter or voltage dividers

### Wiring Receiver → Pi

| Receiver Pin | Purpose                 | Pi GPIO | Pi Pin #  |
|--------------|-----------------       -|---------|-----------|
| CH1          | X-velocity              | GPIO17  | Pin 11    |
| CH2          | Y-velocity              | GPIO27  | Pin 13    |
| CH3          | Angular velocity(w)     | GPIO22  | Pin 15    |
| GND          | Ground                  | GND     | Pin 6     |
| VCC          | 5 V (power only)        | 5 V     | Pin 2/4   |

> **Note:** Use a level shifter or 1 kΩ/2 kΩ voltage divider on each signal line for extra safety.

---

## 2. Software Installation

### 1. Update & Install `pigpio`  
```bash
sudo apt-get update
sudo apt-get install pigpio python3-pigpio
```
## User Instructions

1. **Check Battery Status**  
   Ensure the battery has an EMF of 10–12V. If it's below 10V, charge the battery before use.

2. **Connect the Raspberry Pi**  
   Power the Raspberry Pi using the USB-C port. A red and green LED will start blinking, indicating that the Pi is powered on.

3. **Connect via SSH**  
   - Open the terminal on your laptop.  
   - Connect to the Raspberry Pi using:  
     ```
     ssh pi@<ip-address>
     ```
   - Start the `pigpio` daemon with:  
     ```
     sudo pigpiod
     ```
   - Run the motor control scripts:  
     ```
     python3 motor1_omni.py
     python3 motor2_omni.py
     python3 motor3_omni.py
     ```

4. **Bind the Remote Control**  
   - Turn on the remote.  
   - Insert the binding key into the receiver, then remove it to bind the remote control successfully.

5. **Control the Robot**  
   Provide input in the form of:
   - `Vx` – Linear velocity in the x-direction  
   - `Vy` – Linear velocity in the y-direction (relative to motor 1)  
   - `W` – Angular velocity (rotation about its own axis)  

   These inputs are interpreted by the control system to drive the stepper motors and produce the desired motion.

## Developer Instructions

1. **Clone the Repository**
``` bash
   git clone https://github.com/goelsuchet/omnibot.git
   cd omnibot
 ``` 
2. **Install Required Tools**
- Use a Raspberry Pi (preferably 4B).
- Ensure Python 3 is installed.
- Install the pigpio library:
```sudo apt update
sudo apt install pigpio
```
3. **Start pigpio Daemon**
sudo pigpiod
4. **Folder Structure Overview**
- src/: Motor control code (motor1_omni.py, motor2_omni.py, motor3_omni.py)
- hardware/: 3D CAD models (STL files) and hardware references
- README.md: Full documentation for setup, usage, and development
##Tweak and Extend
1. **Change GPIO Pins**
Update the GPIO pin mappings at the top of each script to match your wiring configuration. You can easily change the GPIO numbers depending on how the motor driver is connected to the Raspberry Pi.
2. **Adjust Motor Parameters**
- Step delay for controlling the motor speed
- Direction logic for tuning movement behavior
- Torque settings using M1, M2, and M3 pins on the A4988 stepper motor driver. This feature is still to be implemented.
3. **Add new features**
- Obstacle Detection: Integrate ultrasonic sensors (e.g., HC-SR04) or LiDAR for detecting obstacles in real-time.
- Advanced Navigation: Use ROS (Robot Operating System) or similar libraries for autonomous movement and mapping.
- Control Interface: Build a web-based or mobile interface for real-time control and monitoring of the robot.

## Known Issues / TODO

- **Threading Integration**
  - Currently, each motor (`motor1_omni.py`, `motor2_omni.py`, `motor3_omni.py`) runs as a separate script.
  - Plan: Combine all motor control scripts into a single multithreaded Python script for better synchronization and cleaner execution.

- **Torque Adjustment**
  - Motor torque is not currently configurable in software.
  - Plan: Add support to adjust torque levels using the `M1`, `M2`, and `M3` terminals of the A4988 stepper motor driver.

- **Obstacle Detection and Mapping**
  - Currently, the bot operates without environment awareness.
  - Plan: Integrate obstacle detection using ultrasonic or LiDAR sensors and implement a basic mapping algorithm for navigation.

- **Testing Required**
  - Unified control script and torque control need field testing.
  - Sensor modules need to be mounted and tested for real-time response.


