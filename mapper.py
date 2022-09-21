#!/usr/bin/env python
  
import io
import sys

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

  
for line in input_stream:
    line = line.strip()
    words = line.split()
      
    for word in words:
        print('%s\t%s' %(word, 1))
