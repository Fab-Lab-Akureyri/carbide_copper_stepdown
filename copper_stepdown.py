import re
import sys

# Check if a filename is given as a command line argument
if len(sys.argv) < 2:
    raise ValueError("Please provide the .nc file as a command line argument.")
    
input_file = sys.argv[1]

# Validate if input_file has a .nc extension
if not input_file.endswith('.nc'):
    raise ValueError("The provided file must have a .nc extension.")
    
output_file = 'carbide_copper_stepdown_' + input_file

with open(input_file, 'r') as f:
    lines = f.readlines()

# Extract the original Z depth
original_z_depth = None
for line in lines:
    match = re.search(r'G01 F200 Z(-\d+\.\d+)', line)
    if match:
        original_z_depth = float(match.group(1))
        break

if original_z_depth is None:
    raise ValueError("Original Z depth not found.")

# Find the index where G01 lines start
g01_start_index = None
for i, line in enumerate(lines):
    if re.match(r'G01 F200 X\d+\.\d+ Y\d+\.\d+', line):
        g01_start_index = i
        break

if g01_start_index is None:
    raise ValueError("G01 lines not found.")

# Write the modified file
with open(output_file, 'w') as f:
    # Write all the lines before the G01 lines
    f.writelines(lines[:g01_start_index])
    
    # First pass with 1/3 of the original Z depth
    f.write(f'G01 F200 Z{original_z_depth / 3:.3f}\n')
    f.writelines(lines[g01_start_index:])
    
    # Second pass with 2/3 of the original Z depth
    f.write(f'G01 F200 Z{2 * original_z_depth / 3:.3f}\n')
    f.writelines(lines[g01_start_index:])
    
    # Third pass with the original Z depth
    f.write(f'G01 F200 Z{original_z_depth:.3f}\n')
    f.writelines(lines[g01_start_index:])
    
print(f'Modified file is written to {output_file}')
