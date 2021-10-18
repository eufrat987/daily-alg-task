def witnesses(heights):
  res = []
  mh = 0
  heights.reverse()
  for h in heights:
      if h > mh:
          mh = h
          res.append(h)
  return len(res)

print (witnesses([3, 6, 3, 4, 1]))
# 3