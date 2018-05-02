import sys
import os
import brainfuck

if len(sys.argv) < 2:
  print('You must provide a file argument')
  exit()
source = sys.argv[1]
if not os.path.isfile(source):
  print('The given file does not exist')
  exit()

def isCap(term):
  return term[0] >= 'A' and term[0] <= 'Z'

def toBrainFuck(binary):
  return {
    '000': '>',
    '001': '<',
    '010': '+',
    '011': '-',
    '100': '.',
    '101': ',',
    '110': '[',
    '111': ']'
  }[binary]

index = 0
brainfuckSource = ''
for line in file(source):
  line = line.strip()
  data = line.split(' ')
  isCap1 = isCap(data[0])
  isCap2 = isCap(data[1])
  isCap3 = isCap(data[2])
  binary = '%d%d%d' % (isCap1, isCap2, isCap3)
  brainfuckCommand = toBrainFuck(binary)
  brainfuckSource += brainfuckCommand
  index += 1

brainfuck.evaluate(brainfuckSource)

