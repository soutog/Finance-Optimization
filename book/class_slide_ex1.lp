\ Model linear program
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0.1 x1 + 0.15 x2 + 0.16 x3 + 0.08 x4
Subject To
 c1: 0.5 x1 + 0.3 x2 + 0.25 x3 + 0.6 x4 >= 28
 c2: 0.3 x1 + 0.1 x2 + 0.4 x3 + 0.2 x4 >= 24
 c3: 0.2 x1 + 0.6 x2 + 0.35 x3 + 0.2 x4 >= 12
 c4: x1 + x2 + x3 + x4 = 80
Bounds
End
