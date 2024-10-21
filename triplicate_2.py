from datetime import datetime

input_file = "data_intf.txt"  # Replace with the actual name of your input file
timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
output_file = f"3pli_{timestamp}.txt"  # Replace with the desired name for the output file

# Read data from input file in the working directory
with open(input_file, 'r') as infile:
    data = infile.read()

lines = data.strip().split('\n')

triplicated_data = '\n'.join(line + '\n' + line + '\n' + line for line in lines)

with open(output_file, 'w') as outfile:
    outfile.write(triplicated_data)
timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
file_name = f"3pli_{timestamp}.txt"
print(f'Data has been triplicated and saved to {file_name}.')
