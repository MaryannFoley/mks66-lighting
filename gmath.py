import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    colors=limit_color(calculate_ambient(ambient,areflect))
    dcolors=calculate_diffuse(light,dreflect,normal)
    scolors=calculate_specular(light, sreflect, view, normal)
    for i in range(3):
        colors[i]+=dcolors[i]
        colors[i]+=scolors[i]
        colors[i]=int(colors[i])
    return colors

def calculate_ambient(alight, areflect):
    return [alight[i]*areflect[i] for i in range(3)]

def calculate_diffuse(light, dreflect, normal):
    color=[]
    normalize(normal)
    normalize(light[0])
    dp=dot_product(normal,light[0])
    color.append(light[1][0]*dreflect[0]*dp)
    color.append(light[1][1]*dreflect[1]*dp)
    color.append(light[1][2]*dreflect[2]*dp)
    return(limit_color(color))
    #light[0] * dreflect * (Dot product of normal and light[1]

def calculate_specular(light, sreflect, view, normal):
    color=[]
    normalize(normal)
    normalize(light[0])
    normalize(view)
    dp=dot_product(normal,light[0])
    r=[]
    for i in range(3):
        r.append(2*normal[i]*dp)
    color.append(light[1][0]*sreflect[0]*dp)
    color.append(light[1][1]*sreflect[1]*dp)
    color.append(light[1][2]*sreflect[2]*dp)
    return(limit_color(color))
    pass

def limit_color(color):
    print(color)
    print(color[0])
    for i in range(len(color)):
        if color[i] <0:
            color[i]=0
        if color[i]>255:
            color[i]=255
    return color

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
