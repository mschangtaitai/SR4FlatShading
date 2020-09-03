#Michael Chan 18562
#Graficas por computadora
#SR4FlatShading
from gl import Render

modelName = input('Ingrese el path del modelo: ')

r = Render()
r.glInit(800,600)
r.load(modelName, [2,2,1], [150, 150, 150])
r.glFinish("SR4.bmp")