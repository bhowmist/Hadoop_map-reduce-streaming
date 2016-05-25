#!/usr/bin/env python
import sys
import string
import math

sum=0
prime_count=0
total_count=0

for line in sys.stdin:
  (key,val) = line.split('\t',1)
  if key!= 'Count' and key!='Prime number':
     sum+= (int(key)*int(val))
  if key== 'Prime number':
      prime_count+=int(val)   
  if key=='Count':
     total_count=total_count+int(val)

print "Count:  ",total_count
print "Primes: ", prime_count
print 'Sum:    ',sum                
         
	
	
