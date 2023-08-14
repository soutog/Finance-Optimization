\ Model quadratic_program
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
 [ 0.0288 x1 ^2 + 0.0576 x1 * x2 + 0.0048 x1 * x3 + 0.08 x2 ^2
   + 0.02 x2 * x3 + 0.005 x3 ^2 ] / 2 
Subject To
 R0: x1 + x2 + x3 = 1
Bounds
End
