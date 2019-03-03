import pandas as pd
import numpy as np
data = pd.DataFrame({'Sample': range(1, 11), 'Gender': ['Female', 'Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female'],
                    'Handedness': ['Right-handed', 'Left-handed', 'Right-handed', 'Right-handed', 'Left-handed', 'Right-handed', 'Right-handed', 'Left-handed', 'Right-handed', 'Right-handed']})
print(data)
# 方法一：用pivot_table

# 方法二：用crosstab
# crosstab()的前两个参数可以是数组、Series或数组列表

