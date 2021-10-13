# CB: This solution to the clock degrees problem uses the ratio of the current minute / 60 min.  This is the ratio of how far the hour hand has traversed between the hours.  Multiply that ratio by the degrees per hour, 30.  That is what calculates the extra degrees.  Also can use modulo division to enforce periods.

import argparse

# Argument parser to run from the command line.

parser = argparse.ArgumentParser()
parser.add_argument("--hours", "-hr", type=int, help="The hour (integer).")
parser.add_argument("--minutes", "-min", type=int, help="The minutes (integer).") 
args = parser.parse_args()

# Default
hour, minute = 1, 1

# Set to command line args.
if args.hours != None:
    hour = args.hours
    
if args.minutes != None:
    minute = args.minutes



# Function
def clockdegrees(hour,minute):
    
    print('Calculating time {}:{}'.format(hour,minute))
    
    min_deg = ((minute % 60) * 6) 
    hour_deg = ((hour * 30) % 360) + (((minute % 60) / 60) * 30)
    
    return print('Hour hand degree: {}, Minute hand degree: {}, Angle between: {}.'.format(hour_deg, min_deg, abs(hour_deg - min_deg)))

# Execute
clockdegrees(hour,minute)