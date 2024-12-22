from subprocess import call
import glob
import os

keys = [
    ["", "Esc", "F1"],
   ["!", "0", "F2"],
   ["@", "1", "F3"],
   ["#", "2", "F4"],
   ["$", "3", "F5"],
   ["%", "4", "F6"],
   ["^", "5", "F7"],
   ["&", "6", "F8"],
   ["*", "7", "F9"],
   ["[", "8", "F10"],
   ["]", "9", "F11"],
   ["_", "-", "F12"],

   ["+", "=", ""],
   [":", ";", ""],
   ["<", ",", ""],
   [">", ".", ""],
   ["|", "\\", ""],
   ["?", "/", ""],
   ["\"", "'", ""],

   ["", "←", ""],
   ["", "↓", ""],
   ["", "↑", ""],
   ["", "→", ""],

   ["{", "(", ""],
   ["}", ")", ""],

   ["", "Q", ""],
   ["", "W", ""],
   ["", "E", ""],
   ["", "R", ""],
   ["", "T", ""],
   ["", "Y", ""],
   ["", "U", ""],
   ["", "I", ""],
   ["", "O", ""],
   ["", "P", ""],
   ["", "A", ""],
   ["", "S", ""],
   ["", "D", ""],
   ["", "F", ""],
   ["", "G", ""],
   ["←", "H", ""],
   ["↓", "J", ""],
   ["↑", "K", ""],
   ["→", "L", ""],
   ["", "Z", ""],
   ["", "X", ""],
   ["", "C", ""],
   ["", "V", ""],
   ["", "B", ""],
   ["", "N", ""],
   ["", "M", ""]
]

def read_and_print_file(LT, LB, RT):
    # Read the content of the file as text
    with open('Keycap.scad', 'r') as file:
        content = file.read()
        content = content.replace('LLT', LT)
        content = content.replace('LLB', LB)
        content = content.replace('LRT', RT)

    # Create a filename based on the arguments
    # Replace characters that are not allowed in filenames
    def make_filename_safe(name):
        return name.replace("/", "slash").replace("\\", "backslash").replace(":", "colon").replace("*", "asterisk").replace("?", "question").replace("\"", "quote").replace("<", "less").replace(">", "greater").replace("|", "pipe")

    safe_LT = make_filename_safe(LT)
    safe_LB = make_filename_safe(LB)
    safe_RT = make_filename_safe(RT)

    filename = f"keycaps/Keycap_{safe_LT}_{safe_LB}_{safe_RT}.scad"

    # Create the keycaps directory if it doesn't exist
    if not os.path.exists('keycaps'):
        os.makedirs('keycaps')

    # Write the content to the new file
    with open(filename, 'w') as output_file:
        output_file.write(content)

for key in keys:
    LT, LB, RB = key
    read_and_print_file(LT, LB, RB)

# 変換処理
files = glob.glob('./keycaps/*.scad')
for f in files:
    of = f.replace('.scad', '.stl')  # name of the outfile .stl
    cmd = ["openscad", "-o", of, f]  # create openscad command
    call(cmd)

# 変換済みのファイルを消す
for f in files:
    os.remove(f)