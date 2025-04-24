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

| Receiver Pin | Purpose          | Pi GPIO | Pi Pin #  |
|--------------|------------------|---------|-----------|
| CH1          | X-velocity       | GPIO17  | Pin 11    |
| CH2          | Y-velocity       | GPIO27  | Pin 13    |
| CH3          | Rotation (θ)     | GPIO22  | Pin 15    |
| GND          | Ground           | GND     | Pin 6     |
| VCC          | 5 V (power only) | 5 V     | Pin 2/4   |

> **Note:** Use a level shifter or 1 kΩ/2 kΩ voltage divider on each signal line for extra safety.

---

## 2. Software Installation

### 1. Update & Install `pigpio`  
```bash
sudo apt-get update
sudo apt-get install pigpio python3-pigpio

