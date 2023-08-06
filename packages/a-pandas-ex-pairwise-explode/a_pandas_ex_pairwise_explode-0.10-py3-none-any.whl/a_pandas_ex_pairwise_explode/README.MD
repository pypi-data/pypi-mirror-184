# Pairwise explode columns in a pandas DataFrame

```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install a-pandas-ex-pairwise-explode



from a_pandas_ex_pairwise_explode import pd_add_pairwise_explode
import pandas as pd
pd_add_pairwise_explode()
df = pd.DataFrame(
    [
        ((244, 22, 12), (1, 3, 4), "a"),
        ((2424, 221), (1, 3), "b"),
        ((26544, 22, 12, "1"), (1, 3, 4, "dd"), "c"),
        ((244, 22, 12), (1, 3, 4), "d"),
    ]
)
"""
                    0              1  2
0       (244, 22, 12)      (1, 3, 4)  a
1         (2424, 221)         (1, 3)  b
2  (26544, 22, 12, 1)  (1, 3, 4, dd)  c
3       (244, 22, 12)      (1, 3, 4)  d

"""

dfnew = df.d_pairwise_explode(columns=[0, 1])
"""
       0   1  2
0    244   1  a
0     22   3  a
0     12   4  a
1   2424   1  b
1    221   3  b
2  26544   1  c
2     22   3  c
2     12   4  c
2      1  dd  c
3    244   1  d
3     22   3  d
3     12   4  d
"""



```



