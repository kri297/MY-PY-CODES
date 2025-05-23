import pandas as pd
import numpy as np

data = {'X': [78, 85, 96, 80, 86],
        'Y': [84, 94, 89, 83, 86],
        'Z': [86, 97, 96, 72, 83]}

df = pd.DataFrame(data)

x_pow_y = np.power(df['X'], df['Y'])
y_pow_z = np.power(df['Y'], df['Z'])
z_pow_x = np.power(df['Z'], df['X'])

print("Original DataFrame:")
print(df)
print("\nX ** Y:")
print(x_pow_y)
print("\nY ** Z:")
print(y_pow_z)
print("\nZ ** X:")
print(z_pow_x)
