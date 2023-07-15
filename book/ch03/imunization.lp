\ Model linear program
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  z[5]
Subject To
 R0: x[0] + y[0] - z[0] = 150
 R1: - 1.01 x[0] + x[1] + y[1] + 1.003 z[0] - z[1] = 100
 R2: - 1.01 x[1] + x[2] + y[2] + 1.003 z[1] - z[2] = -200
 R3: - 1.01 x[2] + x[3] - 1.02 y[0] + 1.003 z[2] - z[3] = 200
 R4: - 1.01 x[3] + x[4] - 1.02 y[1] + 1.003 z[3] - z[4] = -50
 R5: - 1.01 x[4] - 1.02 y[2] + 1.003 z[4] - z[5] = -300
Bounds
 x[0] <= 100
 x[1] <= 100
 x[2] <= 100
 x[3] <= 100
 x[4] <= 100
End
