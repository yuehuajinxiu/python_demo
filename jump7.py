#!/usr/bin/env python3
for a in range(1,101):
    if a%10 == 7 or a%7 == 0:
	   continue
    elif a // 10 == 7:
	    continue
    else:
	   print(a)