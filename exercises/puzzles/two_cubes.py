#two_cubes.py
# i**3 + j**3 == k**3 + l**3    # {i,j} != {k,l}
def two_cube(max=15):
    for i in range(1,max):
        for j in range(1,max):
            for k in range(1,max):
                for l in range(1,max):
                    if k==i or k==j or l==i or l==j:
                        continue
                    if i**3+j**3 == k**3+l**3:
                        print(i,j,k,l)
                        return True
    return False

for max in range(1,15):
    if two_cube(max):
        break
