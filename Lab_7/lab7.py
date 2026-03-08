import arcpy

source = r"C:\Users\neha2003\Desktop\sujith-online-GEOG676-spring2026\Lab_7"
band1 = arcpy.sa.Raster(source + r"\landsat4\blue.tif") #blue
band2 = arcpy.sa.Raster(source + r"\landsat4\green.tif") #green
band3 = arcpy.sa.Raster(source + r"\landsat4\red.tif") #red
band4 = arcpy.sa.Raster(source + r"\landsat4\nir08.tif") #NIR
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif")

# Hillshade
azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r"\dem\dem_30m.tif", source + r"\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)

#Slope
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + "\dem\dem_30m.tif", source + r"\output_Slop.tif", output_measurement, z_factor)
print("success!")