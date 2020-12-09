import os

if os.path.exists('a.txt'):
    # os.rename('a.txt', 'b.txt')
    print(os.renames('a.txt',  'e.txt'))
