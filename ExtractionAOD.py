# Name: Rename.py
# Developed: shivaprakash yaragal
# Description: Rename tiff file 

# Import system modules
import arcpy
from arcpy.sa import *

# Set workspace
arcpy.env.workspace = "E:\\Shivaprakash\\TEST\\Neemrana\\NeemranaProjectManagement\\NEO_DATA\\Aerosol_raw"
#listing the raster 
rasterlist = arcpy.ListRasters("*","TIFF")
# raster renaming
for raster in rasterlist:
	raster1=raster.split('_')
	raster2=raster1[4].split('-')
	out="aod"+raster2[1]+raster2[0]
	print(out)
	arcpy.Rename_management(raster, out)


arcpy.env.workspace = "E:\\Shivaprakash\\TEST\\Neemrana\\NeemranaProjectManagement\\NEO_DATA\\Aerosol_raw"
rasterlist = arcpy.ListRasters("*","TIFF")
input1="E:\\Shivaprakash\\TEST\\Neemrana\\NeemranaProjectManagement\\Neemrana.gdb"
ExtractMultiValuesToPoints(input1,rasterlist)




arcpy.env.workspace = "D:\\Shivaprakash\\TEST\\project_aerosol\\Aerosol_raw"
rasterlist = arcpy.ListRasters("*","TIFF")
input1="D:\\Shivaprakash\\TEST\\project_aerosol\\PrjData.gdb\\MegaCities"
ExtractMultiValuesToPoints(input1,rasterlist)