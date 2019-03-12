import math
import rasterio
import matplotlib.pyplot as plt

image_file = "20160831_174456_0e0f_3B_AnalyticMS.tif"
sat_data = rasterio.open(image_file)

width_in_projected_units = sat_data.bounds.right - sat_data.bounds.left
height_in_projected_units = sat_data.bounds.top - sat_data.bounds.bottom

print("Width: {}, Height: {}".format(width_in_projected_units, height_in_projected_units))


print("Rows: {}, Columns: {}".format(sat_data.height, sat_data.width))

# Upper left pixel
row_min = 0
col_min = 0

# Lower right pixel.  Rows and columns are zero indexing.
row_max = sat_data.height - 1
col_max = sat_data.width - 1

# Transform coordinates with the dataset's affine transformation.
topleft = sat_data.transform * (row_min, col_min)
botright = sat_data.transform * (row_max, col_max)

print("Top left corner coordinates: {}".format(topleft))
print("Bottom right corner coordinates: {}".format(botright))
print(sat_data.count)

# sequence of band indexes
print(sat_data.indexes)

# Load the 4 bands into 2d arrays - recall that we previously learned PlanetScope band order is BGRN.
b, g, r, n = sat_data.read()

# Displaying the blue band.
plt.subplot(2, 2, 1)
fig = plt.imshow(b)
plt.title('Blue')
plt.colorbar()
#plt.show()

# Displaying the green band.
plt.subplot(2, 2, 2)
fig = plt.imshow(g)
fig.set_cmap('gist_earth')
plt.title('Green')
plt.colorbar()
#plt.show()

# Displaying the red band.
plt.subplot(2, 2, 3)
fig = plt.imshow(r)
fig.set_cmap('inferno')
plt.title('Red')
plt.colorbar()
#plt.show()

# Displaying the infrared band.
plt.subplot(2, 2, 4)
fig = plt.imshow(n)
fig.set_cmap('winter')
plt.title('Infrared')
plt.colorbar()

plt.subplots_adjust(hspace=.2,
                    wspace=.5)
plt.show()