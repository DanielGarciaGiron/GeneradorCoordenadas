import bpy
import csv
import os
from mathutils import Vector

OriginLoc = Vector((0,0,0))
upVector = Vector((0,0,1))  
#Desktop
#file = csv.reader(open('Coordenadas.csv', newline=''), delimiter=',')

#for row in file:
#    x = row[0]
#    y = row[1]
#    z = row[2]
#    bpy.ops.mesh.primitive_uv_cilinder_add(location = (float(x),float(y),float(z)))
    
#Laptop
#Add path file.    
fp = "Coordenadas.csv"

with open( fp ) as csvfile:
    rdr = csv.reader( csvfile )
    for i, row in enumerate( rdr ):
        x = row[0]
        y = row[1]
        z = row[2]
        #bpy.ops.mesh.primitive_uv_sphere_add(location = (float(x),float(y),float(z)))
        myStartLoc = Vector((float(x),float(y),float(z)))
        myRotQuaternion=upVector.rotation_difference(myStartLoc)
        myRotEulerAngles=myRotQuaternion.to_euler()
        myRotEulerAnglesVec=((myRotEulerAngles.x,myRotEulerAngles.y,myRotEulerAngles.z))
        bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=7.5,depth=75, end_fill_type='NGON', location=myStartLoc, rotation=myRotEulerAnglesVec)

