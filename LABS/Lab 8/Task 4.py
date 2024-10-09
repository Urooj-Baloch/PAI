import numpy as np
dtype = [('name', 'U20'), ('height', 'f4'), ('class', 'U10')]
data = np.array([
    ('John', 5.9, '2A'),
    ('Alizay', 5.5, '1B'),
    ('Minahil', 5.7, '2A'),
    ('Sara', 5.8, '1A'),
    ('Tara', 5.6, '1B')
], dtype=dtype)
sorted_data = np.sort(data, order=['class', 'height'])
for student in sorted_data:
    print(student)
