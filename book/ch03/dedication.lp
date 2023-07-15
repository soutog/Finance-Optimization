\ Model linear program
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  109 x1 + 94.8 x2 + 99.5 x3 + 93.1 x4 + 97.2 x5 + 92.9 x6 + 110 x7 + 104 x8
   + 102 x9 + 95.2 x10
Subject To
 R0: 10 x1 + 7 x2 + 8 x3 + 6 x4 + 7 x5 + 5 x6 + 10 x7 + 8 x8 + 7 x9
   + 100 x10 - s1 = 100
 R1: 10 x1 + 7 x2 + 8 x3 + 6 x4 + 7 x5 + 5 x6 + 10 x7 + 8 x8 + 107 x9 + s1
   - s2 = 200
 R2: 10 x1 + 7 x2 + 8 x3 + 6 x4 + 7 x5 + 5 x6 + 110 x7 + 108 x8 + s2 - s3
   = 800
 R3: 10 x1 + 7 x2 + 8 x3 + 6 x4 + 7 x5 + 105 x6 + s3 - s4 = 100
 R4: 10 x1 + 7 x2 + 8 x3 + 106 x4 + 107 x5 + s4 - s5 = 800
 R5: 110 x1 + 107 x2 + 108 x3 + s5 - s6 = 1200
Bounds
End
