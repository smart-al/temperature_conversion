#!/usr/bin/env python3


def convert_to_celsius(fahrenheit):
   ''' (number) -> number
   
   Return the number of Celsius degrees equivalent to fahrenheit degrees.
   
   >>> convert_to_celsius(32)
   0
   >>> convert_to_celsius(212)
   100
   '''
   
   return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsuis):
    ''' (number) -> number
     Return the number of Fahrenheit degrees equivalent to Celsuis degrees.
     
     >>> convert_to_fahrenheit(100)
     212
     >>> convert_to_celsuis(0)
     32
     '''
    
    return (celsuis * 9/5) + 32




    
    