import pandas as pd
# After researching this very quickly it seems that pandas eval is much safer than python eval. Eval is safe if you are the only user, it is not safe if others will use the program.
try:
    result = pd.eval(input("Please input your calculation: "))
except ValueError:
    print("Please enter arithmetic expressions.")
print(result)