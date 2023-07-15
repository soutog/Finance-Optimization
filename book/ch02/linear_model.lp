\ Model linear program
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.1 x + 0.15 y + 0.16 z + 0.08 w
Subject To
 c1: 0.5 x + 0.3 y + 0.25 z + 0.6 w >= 28
 c2: 0.3 x + 0.1 y + 0.4 z + 0.2 w >= 24
 c3: 0.2 x + 0.6 y + 0.35 z + 0.2 w >= 12
 c4: x + y + z + w = 80
Bounds
End
