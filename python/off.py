#!/usr/bin/env python3

import time
import argparse
import config
import board
import neopixel

# LED strip configuration:
LED_COUNT = config.N_PIXELS       # Number of LED pixels.
LED_PIN = board.D18               # GPIO pin (using board notation).
LED_BRIGHTNESS = config.BRIGHTNESS / 255.0  # NeoPixel expects 0.0–1.0

# Create NeoPixel object with appropriate configuration.
strip = neopixel.NeoPixel(
    LED_PIN,
    LED_COUNT,
    brightness=LED_BRIGHTNESS,
    auto_write=False,   # Don’t update until .show()
    pixel_order=neopixel.GRB  # WS2812 LEDs are usually GRB
)

# Define functions which animate LEDs in various ways.
def color_wipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(len(strip)):
        strip[i] = color
        strip.show()
        time.sleep(wait_ms / 1000.0)

# Main program logic follows:
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true',
                        help='clear the display on exit')
    args = parser.parse_args()

    try:
        # Example: Wipe red across display
        color_wipe(strip, (255, 0, 0), 10)

    finally:
        if args.clear:
            color_wipe(strip, (0, 0, 0), 10)
