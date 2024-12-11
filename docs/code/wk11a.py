###
### Plot cubes from 1 to 1,00
###
import matplotlib.pyplot as plt

source = range(1,101)
cubes = [s*s*s for s in source]


print("Available styles", plt.style.available)

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()

ax.plot(source, cubes)

#plt.savefig("example.png")
ax.set_ylabel("Cube")  # Add a y-label to the axes.
ax.set_title("Cubes")  # Add a title to the axes.

plt.savefig("wk11a-fig1.png")
#plt.show()

##  Graph the squares and cubes from 1-100, and save them as a png file.

squares = [s*s for s in source]

fig2, ax2 = plt.subplots()
ax2.plot(source, squares, label = 'X²')
ax2.plot(source, cubes, label = 'X³')
ax2.set_title("Squares and Cubes") 
ax2.legend()

plt.savefig("wk11a-fig2.png")
