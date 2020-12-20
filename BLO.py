#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fernando Orge
"""

import configApp


def configurar():
    """Docstring"""
    ###########################################################################

    BLO = configApp.mariaDB.CREAR()
    BLO.NumeroTabla = '0000'
    BLO.NombreTabla = 'Bloques'
    BLO.ComentarioTabla = 'Registro de cadena de bloques'
    BLO.NombreVista = 'V'
    BLO.NombrePA = 'BLOC'
    BLO.ComentarioPA = 'Crea un nuevo bloque en la cadena.'

    ###########################################################################

    BLO.campo = 'PA'
    BLO.CrearCampo(PA=BLO.NombrePA,
                   id_tabla=BLO.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='4',
                   comentario='Procedimiento almacenado',
                   label='Procedimiento almacenado',
                   readonly=True,
                   name=BLO.campo,
                   value=BLO.NombrePA)

    ###########################################################################

    BLO.campo = 'idBloque'
    BLO.CrearCampo(PA=BLO.NombrePA,
                   id_tabla=BLO.NumeroTabla,
                   tipo='MEDIUMINT',
                   tamaño='8',
                   comentario='Id de bloque',
                   pk=True,
                   signo=False,
                   nulo=False,
                   label='Id de bloque',
                   name=BLO.campo,
                   placeholder='Indicar el id de bloque',
                   autofocus=True,
                   type='number')

    ###########################################################################

    BLO.campo = 'creado'
    BLO.CrearCampo(PA=BLO.NombrePA,
                   id_tabla=BLO.NumeroTabla,
                   tipo='TIMESTAMP',
                   nulo=False,
                   default='CURRENT_TIMESTAMP',
                   comentario='Fecha y hora de creación del bloque',
                   label='Fecha y hora',
                   name=BLO.campo)

    ###########################################################################

    BLO.campo = 'HashPrevio'
    BLO.CrearCampo(PA=BLO.NombrePA,
                   id_tabla=BLO.NumeroTabla,
                   tipo='CHAR',
                   tamaño='128',
                   nulo=False,
                   comentario='Hash del bloque anterior',
                   label='Hash previo',
                   name=BLO.campo)

    ###########################################################################

    BLO.campo = 'nonce'
    BLO.CrearCampo(PA=BLO.NombrePA,
                   id_tabla=BLO.NumeroTabla,
                   tipo='MEDIUMINT',
                   tamaño='8',
                   comentario='Valor utilizado por única vez',
                   signo=False,
                   label='nonce',
                   name=BLO.campo,
                   placeholder='Indicar el nonce',
                   type='number')

    ###########################################################################

    BLO.campo = 'tiempo'
    BLO.CrearCampo(PA=BLO.NombrePA,
                   id_tabla=BLO.NumeroTabla,
                   tipo='MEDIUMINT',
                   tamaño='8',
                   comentario='Tiempo de bloque en segundos',
                   signo=False,
                   label='Tiempo',
                   name=BLO.campo,
                   placeholder='Indicar el tiempo de segundos',
                   type='number')

    ###########################################################################

    BLO.campo = 'dificultad'
    BLO.CrearCampo(PA=BLO.NombrePA,
                   id_tabla=BLO.NumeroTabla,
                   tipo='TINYINT',
                   tamaño='3',
                   comentario='Dificultad del bloque',
                   signo=False,
                   label='Dificultad',
                   name=BLO.campo,
                   placeholder='Indicar la dificultad del bloque actual',
                   type='number')

    ###########################################################################

    return BLO


####################################
# sitio.TablaTitulo = 'Campos'
# sitio.TablaEncabezado = db.cabecera
# sitio.TablaFilas = db.filas
####################################


# Programa principal


try:
    if __name__ == '__main__':
        try:
            import INIT
            bd = INIT.BD()
            sitio = INIT.GUI()
            sitio.InputList = bd.ObtenerParametros('0000')
            print(sitio.Html(sitio.Body6()))
        except:
            import sys
            print(sys.exc_info())
    else:
        print('BLO importado')
except ImportError:
    print('error al importar BLO.py')
