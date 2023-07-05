import gurobipy as gp
from gurobipy import GRB

opt_mod = gp.Model(name="linear program")

x1 = opt_mod.addVar(name="x1", vtype=GRB.CONTINUOUS, lb=0)
x2 = opt_mod.addVar(name="x2", vtype=GRB.CONTINUOUS, lb=0)

obj_fn = 4 * x1 + 3 * x2

opt_mod.setObjective(obj_fn, GRB.MAXIMIZE)

c1 = opt_mod.addConstr(2 * x1 + x2 <= 150, name="c1")

c2 = opt_mod.addConstr(3 * x1 + 4 * x2 <= 360, name="c2")

c3 = opt_mod.addConstr(x1 + x2 <= 100, name="c4")

opt_mod.optimize()  # solve the model
opt_mod.write("class_slide_ex2.lp")

print(f"Objective Function Value: {opt_mod.ObjVal}")

# Get the values of the decision variables
for v in opt_mod.getVars():
    print(f"{v.varName}: {v.x}")
