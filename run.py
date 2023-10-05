import sys
import os

TITLE = "Tony\'s totally-PC RF Scanner"

# these are just "guard rails" to make sure the user doesn't enter something
# unreasonable
MIN_FREQ = 100
MAX_FREQ = 1000
MIN_SCANS = 1
MAX_SCANS = 10

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def input_int(prompt, min, max):
  while True:
    value = input(prompt)
    try:
      number = int(value)
    except ValueError:
      print(f"  Invalid choice '{value}'. Must be an integer.")
      continue

    if number < min or number > max:
      print(f"  Invalid choice '{number}'. Must be from {min} to {max}.")
      continue

    return number

if os.name == 'nt':
  os.system('title ' + TITLE)

# set SCRIPT_DIR=C:\rfexplorer-detailed-scan\venv\scripts
# set SCANS_DIR=C:\Users\Tony\Desktop\RF Scans
# rem echo %SCRIPT_DIR%
# rem echo %SCANS_DIR%

start_freq = 400
end_freq = 700
number_of_scans = 2

# :MENU
option = None
while True:
  cls()
  print(TITLE)
  print('')
  print(f'   1. Start Frequency         {start_freq}')
  print(f'   2. End Frequency           {end_freq}')
  print(f'   3. Number of Scans         {number_of_scans}')
  print(f'   4. Initiate Scan(s)')
  print('')

  key = input("Select an option or [A]bort> ")

  if key == '1':
    start_freq = input_int('Enter start frequency> ', MIN_FREQ, MAX_FREQ)
  elif key == '2':
    start_freq = input_int('Enter end frequency> ', MIN_FREQ, MAX_FREQ)
  elif key == '3':
    start_freq = input_int('Enter number of scans> ', MIN_SCANS, MAX_SCANS)
  elif key == '4':
    break
  elif key == 'a':
    quit()

for x in range(0, number_of_scans):
  print(f'Connect Antenna for scan {x + 1} of {number_of_scans} and press Enter...')

  # %SCRIPT_DIR%\rfexplorerDetailedScan ^
  # -s %s% -e %e% -a max -r 2 -i 10 -v ^
  # "%SCANS_DIR%\scan-%date:/=-%-%time::=-% Ant %%x.csv"
