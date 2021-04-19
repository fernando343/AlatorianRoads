from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show

def caminata(campo, pasos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='Steven')
    origen = Coordenada(0, 0)
    campo.anadir_borracho(borracho, origen)

    pasos_x = []
    pasos_y = []

    pasos_x.append(origen.x)
    pasos_y.append(origen.y)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
        
        pasos_x.append(campo.obtener_coordenada(borracho).x)
        pasos_y.append(campo.obtener_coordenada(borracho).y)
    #print(f'x {pasos_x}, y {pasos_y}')
        
    return (pasos_x, pasos_y)


def graficar(x, y,pasos):
    grafica = figure(title='Random Walks',x_axis_label='x axis', y_axis_label='y axis')
    grafica.line(x, y, legend_label='walk', color='skyblue',name='steven') #recorrido
    grafica.line(x[0:-1:pasos-1],y[0:-1:pasos-1], color='black', line_width=1) #linea de punto inicial a punto final
    print(f'x {x[0:-1:pasos-1]}, y {y[0:-1:pasos-1]}')
    show(grafica)

def main(pasos, tipo_de_borracho):
    campo=Campo()
    pasos_x, pasos_y = caminata(campo, pasos, tipo_de_borracho)
    #print(f'x {pasos_x} y {pasos_y}')
    graficar(pasos_x, pasos_y, pasos)


if __name__ == '__main__':

    pasos = 3000
    main(pasos, BorrachoTradicional)