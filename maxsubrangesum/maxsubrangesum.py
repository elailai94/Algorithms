def maxsubrangesum(x, n):
   maxsofar = 0
   tempstartingindex = 0
   startingindex = 1
   endingindex = 0
   maxsuffixsum = 0

   for i in range(n):
      maxsuffixsum += x[i]
      if (maxsuffixsum < 0):
         tempstartingindex = i + 1
         maxsuffixsum = 0
      else:
         startingindex = tempstartingindex
         endingindex = i
         maxsofar = maxsuffixsum

   return [maxsofar, startingindex, endingindex]
