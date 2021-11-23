# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given a time in the format of hour and minute, 
# calculate the angle of the hour and minute hand on a clock.

def calcAngle(h, m):
  ma = m/60.0 * 360
  adder = ma/360
  ha = h/12.0 * 360 + adder * 360/12

  res = abs(ha-ma)
  return min(360-res, res)
  

print (calcAngle(3, 30))
# 75
print (calcAngle(12, 30))
# 165