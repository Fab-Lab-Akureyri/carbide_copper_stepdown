import re
import sys

if len(sys.argv) < 2:
    raise ValueError("Please provide the .nc file as a command line argument.")

input_file = sys.argv[1]
if not input_file.endswith('.nc'):
    raise ValueError("The provided file must have a .nc extension.")

output_file = 'carbide_copper_stepdown_' + input_file

with open(input_file, 'r') as f:
    lines = f.readlines()

original_z_depth = None
z_depth_line_index = None
for i, line in enumerate(lines):
    match = re.search(r'G01 F200 Z(-\d+\.\d+)', line)
    if match:
        original_z_depth = float(match.group(1))
        z_depth_line_index = i
        break

if original_z_depth is None:
    raise ValueError("Original Z depth not found.")

if z_depth_line_index is None:
    raise ValueError("Z depth line not found.")

g01_start_index = None
for i, line in enumerate(lines):
    if re.match(r'G01 F200 X\d+\.\d+ Y\d+\.\d+', line):
        g01_start_index = i
        break

if g01_start_index is None:
    raise ValueError("G01 lines not found.")

with open(output_file, 'w') as f:
    # Write the lines before the original Z depth line
    f.writelines(lines[:z_depth_line_index])

    for multiplier in [1/3, 2/3, 1]:
        # Write the new Z depth
        f.write(f'G01 F200 Z{original_z_depth * multiplier:.3f}\n')
        # Write the G01 lines with X and Y coordinates
        f.writelines(lines[g01_start_index:z_depth_line_index] + lines[z_depth_line_index + 1:])

print(f'Modified file is written to {output_file}')
