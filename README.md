# How to use

> [!IMPORTANT]
> Installing OpenSCAD is required.

> [!WARNING]
> When using it, please change the font in the `Keycap.scad` file as needed.

- Modify keys array on ``gen_keys.py`` as you want.

  ```python
  # 0...Left top, for shift key
  # 1...Left bottom, for main key
  # 2...Right bottom, for fn key
  ["*", "7", "F9"]
  ```

- Run

  ```shell
  python gen_key.py
  ```

- You can get ``.stl`` in the keycaps folder!

## Environment

- Bambu Lab A1 Combo (0.2mm nozzle)
- [ELEGOO PLA filament](https://amzn.asia/d/7IzwUUX) for base (I choose white.)
- [ELEGOO PLA filament](https://amzn.asia/d/7IzwUUX) for legend (I choose navy. Pretty cool!)

## Note

If you have any questions, please contact [Twitter](https://twitter.com/Ruchi12377)!
