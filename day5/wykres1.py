import matplotlib.pyplot as plt
from PIL.ImageColor import colormap

# pip install matplotlib

x = [1, 2, 3, 4, 5]
y = [3, 6, 9, 12, 27]

plt.plot(x, y, color="red")
plt.title("Wykres liniowy")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")

plt.savefig('wykres.png')
plt.savefig('wykres.pdf')
plt.show()
