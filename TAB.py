#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fernando Orge
"""

import configApp


def configurar():
    """Configura las tablas de la aplicación.
    
    Generar una instancia del objeto CREAR para crear la tabla, la vista y el procedimiento almacenado.
    
    Indicar los atributos por cada tabla, vista y procedimiento almacenado.
    
    Ejecutar el método CrearCampo por cada campo necesario.
    
    Esta función es ejecutada por la función initApp del módulo INIT.py

    >>> print(configurar().NombrePA)
    TABC
    """

    TAB = configApp.mariaDB.CREAR()
    TAB.NumeroTabla = '0030'
    TAB.NombreTabla = 'Tablas'
    TAB.ComentarioTabla = 'Tablas de la aplicación'
    TAB.NombreVista = 'V'
    TAB.NombrePA = 'TABC'
    TAB.ComentarioPA = 'Crea una nueva tabla'

    ###########################################################################

    TAB.campo = 'PA'
    TAB.CrearCampo(PA=TAB.NombrePA,
                   id_tabla=TAB.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='4',
                   comentario='Procedimiento almacenado',
                   label='Procedimiento almacenado',
                   readonly=True,
                   name=TAB.campo,
                   value=TAB.NombrePA)

    ###########################################################################

    TAB.campo = 'idTabla'
    TAB.CrearCampo(PA=TAB.NombrePA,
                   id_tabla=TAB.NumeroTabla,
                   tipo='CHAR',
                   tamaño='5',
                   comentario='Id de tabla',
                   pk=True,
                   label='Id de tabla',
                   name=TAB.campo,
                   placeholder='Indicar el id de la tabla',
                   autofocus=True)

    ###########################################################################

    TAB.campo = 'tablaActiva'
    TAB.CrearCampo(PA=TAB.NombrePA,
                   id_tabla=TAB.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Tabla activa o inactiva',
                   default='1',
                   label='Activa',
                   name=TAB.campo)

    ###########################################################################

    TAB.campo = 'tabla'
    TAB.CrearCampo(PA=TAB.NombrePA,
                   id_tabla=TAB.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='24',
                   comentario='Descripción o nombre de tabla',
                   label='Tabla',
                   name=TAB.campo,
                   placeholder='Indicar el nombre de la tabla')

    ###########################################################################

    TAB.campo = 'AyudaTabla'
    TAB.CrearCampo(PA=TAB.NombrePA,
                   id_tabla=TAB.NumeroTabla,
                   tipo='TEXT',
                   comentario='Ayuda para el usuario',
                   nulo=True,
                   label='Ayuda para el usuario',
                   name=TAB.campo,
                   placeholder='Indicar comentarios sobre la funcionalidad')
    return TAB


# Programa principal


try:
    if __name__ == '__main__':
        try:
            """
            Obtiene la conexión a la BBDD y los atributos comunes a todos 
            los sitios del modulo INIT.
            
            Vincula los parámetros almacenados en la BBDD con la GUI web.
            
            Debe indicarse como parámetro del método ObtenerParametros el valor
            del atributo NumeroTabla indicado en la función configurar().
            """
            import INIT
            bd = INIT.BD()
            sitio = INIT.GUI()
            sitio.InputList = bd.ObtenerParametros('0030')
            print(sitio.Html(sitio.Body6()))
        except:
            import sys
            print(sys.exc_info())
            import doctest
            doctest.testmod()
    else:
        # Módulo importado
        pass
except ImportError:
    print('error al importar TAB.py')
