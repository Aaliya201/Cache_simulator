# Set associative cache , only the LRU policy was tried in this code 

import sys
import argparse


# using parser to add inputs to the file 
#  python3 cachetry12.py --slots 4 --sets 4 --addr 8 --file trace1.txt ( an example line to run the code, note that trace file modified for this code)

arg_parser = argparse.ArgumentParser(
  description='Simulates a set-accociative cache '
)
arg_parser.add_argument('--slots', 
  type=int, required=True,
  help='number of slots in the cache '
)
arg_parser.add_argument('--sets',
  type=int, required=True,
  help='number of sets in each slot '
)
arg_parser.add_argument('--addr', 
  type=int, required=True, 
  help='number of addresses in each set'
)
arg_parser.add_argument('--file', 
  type=str, required=True, 
  help='name of the trace file to use for simulation'
)
args = arg_parser.parse_args()











def main():
  lines = readlines(args.file) #reads line from the file
  memory_access = TraceInfo(lines)  # memory access values are the values in each line
  hit =0
  cache = [[{'tag': None, 'LRU': 0} for x in range(args.sets)] for y in range(args.slots)] # declaring a cache and assignment of other values as zero
  misses = { 'total': 0, 'conflict': 0, 'cold': 0  } # making a dictionary for tag, LRU in cache and misses which contains different types of misses
 
  
  for entry in memory_access:
    slot = cache[entry['slot']]
    match = None
    for set in slot:
      if set['tag'] != entry['tag']: # if the tag value is not equal to the entry or new tag value 
        set['LRU'] += 1
      else:
        set['LRU'] = 0
        match = set
    if not match:
      misses[entry['type']] += 1
      evict_bit = max(slot, key = lambda _set: _set['LRU'])
      evict_bit['tag'] = entry['tag']
      evict_bit['LRU'] = 0
      
  misses['total'] = misses['conflict'] + misses['cold']
  number_of_access = len(memory_access)
  hit = number_of_access -misses['total']
  for key, value in misses.items():
    print("{0} : {1} / {2}".format(key, value, number_of_access))
  print("hit:",hit,"/",number_of_access)



def readlines(trace5): # remember to change the tracefile name here for a different file
  try:
    return [ line.strip() for line in open(r"trace5.txt", "r") ] # add trace file here
  except:
    sys.exit('Error: The provided filename "{0}" does not exist in this directory.'.format(trace5))





def TraceInfo(lines):
  # bits needed to reference each level of the cache.
  a = vars(args).items() 
  bit_lengths = { k: len(bin(v-1)[2:]) for k, v in a if k != 'file' }

  # starting positions of the slot/offset/blockoffset portions of the address
  offset_start = -bit_lengths['addr']
  slot_start = -(bit_lengths['slots'] + bit_lengths['addr'])
  
  #Extract info from each trace entry. 
  
  def ValueFunc(line):
    parts = line.split()
    result = {}
    a = bin(int(parts[0], 16))[2:]
    result['address'] = a
    result['offset'] = int(a[offset_start:], 2) # offset starts from 3rd place
    result['slot'] = int(a[slot_start:offset_start], 2) 
    result['tag'] = int(a[:slot_start]) #tag size after set size
    result['type'] = 'conflict' if parts[1] == 'I' else 'cold'
    return result
    
  return list(map(ValueFunc, lines))
  
main()