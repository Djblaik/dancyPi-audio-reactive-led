import time
import numpy as np
import board
import neopixel
import config

# Initialize the LED strip with built-in gamma correction
# NeoPixel's gamma is approximately 2.8 by default; you can adjust if needed
strip = neopixel.NeoPixel(
    getattr(board, f"D{config.LED_PIN}"),  # GPIO pin
    config.N_PIXELS,
    brightness=config.BRIGHTNESS / 255,    # 0.0–1.0
    auto_write=False,
    pixel_order=neopixel.GRB,             # adjust to your strip
)

# Pixel arrays (R, G, B × number of pixels)
pixels = np.zeros((3, config.N_PIXELS), dtype=int)
_prev_pixels = np.zeros((3, config.N_PIXELS), dtype=int)  # store previous state


def _update_strip():
    """Update NeoPixel strip efficiently using NumPy, skipping unchanged pixels."""
    global _prev_pixels

    # Clamp values 0–255
    p = np.clip(pixels, 0, 255).astype(int)

    # Only update pixels that changed
    for i in range(config.N_PIXELS):
        if np.array_equal(p[:, i], _prev_pixels[:, i]):
            continue  # skip unchanged pixels
        strip[i] = (int(p[0, i]), int(p[1, i]), int(p[2, i]))  # R,G,B

    strip.show()
    _prev_pixels[:] = p


if __name__ == "__main__":
    # Test pattern: red, green, blue
    pixels[:, :] = 0
    pixels[0, 0] = 255  # Red
    pixels[1, 1] = 255  # Green
    pixels[2, 2] = 255  # Blue

    print("Starting NeoPixel strand test")
    _update_strip()

    # Example rolling animation
    while True:
        pixels = np.roll(pixels, 1, axis=1)
        _update_strip()
        time.sleep(0.1)
