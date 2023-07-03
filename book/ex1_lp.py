import gurobipy as gp
from gurobipy import GRB

opt_mod = gp.Model(name="linear program")

x = opt_mod.addVar(name="x", vtype=GRB.CONTINUOUS, lb=0)
y = opt_mod.addVar(name="y", vtype=GRB.CONTINUOUS, lb=0)
z = opt_mod.addVar(name="z", vtype=GRB.CONTINUOUS, lb=0)
w = opt_mod.addVar(name="w", vtype=GRB.CONTINUOUS, lb=0)

obj_fn = 0.10 * x + 0.15 * y + 0.16 * z + 0.08 * w
opt_mod.setObjective(obj_fn, GRB.MINIMIZE)

c1 = opt_mod.addConstr(0.5 * x + 0.30 * y + 0.25 * z + 0.60 * w >= 0.35 * 80, name="c1")
c2 = opt_mod.addConstr(
    0.30 * x + 0.10 * y + 0.40 * z + 0.20 * w >= 0.30 * 80, name="c2"
)
c3 = opt_mod.addConstr(
    0.20 * x + 0.60 * y + 0.35 * z + 0.20 * w >= 0.15 * 80, name="c3"
)
c3 = opt_mod.addConstr(x + y + z + w == 80, name="c4")

opt_mod.optimize()  # solve the model
opt_mod.write("linear_model.lp")


print(f"Objective Function Value: {opt_mod.ObjVal}")

# Get the values of the decision variables
for v in opt_mod.getVars():
    print(f"{v.varName}: {v.x}")
