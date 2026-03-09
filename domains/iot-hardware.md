# IoT & Hardware — Domain Skill

> Activate for projects involving embedded hardware, firmware, and IoT protocols.

## Microcontrollers

| Platform | Toolchain | Flash Tool |
|----------|-----------|-----------|
| **ESP32** | ESP-IDF / Arduino | `esptool` (bundled) |
| **AVR** (ATmega) | avr-gcc | `avrdude` (bundled) |
| **STM32** | STM32CubeIDE | `stm32flash` / ST-Link |

## Programming Patterns

### esptool (ESP32)

```bash
# Flash firmware
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash 0x0 firmware.bin

# Erase flash
esptool --chip esp32 --port /dev/ttyUSB0 erase_flash

# Flash SPIFFS/LittleFS partition
esptool --chip esp32 --port /dev/ttyUSB0 write_flash 0x290000 spiffs.bin
```

### avrdude (AVR)

```bash
# Flash hex file
avrdude -c usbasp -p m328p -U flash:w:firmware.hex:i

# Read EEPROM
avrdude -c usbasp -p m328p -U eeprom:r:dump.hex:i

# Write fuses
avrdude -c usbasp -p m328p -U lfuse:w:0xFF:m -U hfuse:w:0xDE:m
```

## Serial / USB

- Always release USB ports after programming (`await exitCode` or close port handle)
- Linux serial ports: `/dev/ttyUSB0`, `/dev/ttyACM0` — may need `dialout` group membership
- Windows: `COM3`, `COM4`, etc.
- Use `udev` rules for persistent device naming on Linux

## MQTT

- Lightweight pub/sub messaging for IoT device communication
- Standard ports: 1883 (unencrypted), 8883 (TLS)
- Topic naming: `<project>/<device-type>/<device-id>/<action>`
- QoS levels: 0 (fire-and-forget), 1 (at least once), 2 (exactly once)

## IoT Platforms

| Platform | Purpose |
|----------|---------|
| **ThingsBoard** | Device provisioning, telemetry, dashboards |
| **Firebase/Firestore** | Device records, auth, config |
| **InvenTree** | Warehouse/BOM management (planned) |

## Hardware Identity

- **1-Wire** (DS2401): Silicon serial number — unique, read-only, 6-byte ID
- **EEPROM**: Writable identity storage — use for calibration data, serial numbers
- **MAC address**: Use for network-level identification (ESP32 has factory MAC)

## Production Workflow

1. **Serial number provisioning** — assign unique serial from batch
2. **Firmware flash** — MCU + wireless module
3. **EEPROM/config write** — device identity, calibration
4. **IoT platform provisioning** — create device on ThingsBoard/Firebase
5. **Functional test** — automated or manual test plan
6. **Label/package** — print label, assign to build order

## Safety

- **Never leave USB ports locked** — always await process exit
- **Never flash wrong firmware** — verify product type before programming
- **ESD precautions** — handle boards on ESD mat
