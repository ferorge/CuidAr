#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fernando Orge
"""

import configApp


def configurar():
    """Docstring"""
    ###########################################################################

    TRA = configApp.mariaDB.CREAR()
    TRA.NumeroTabla = '0050'
    TRA.NombreTabla = 'Transacciones'
    TRA.ComentarioTabla = 'Transacciones dentro de la aplicación'
    TRA.NombreVista = 'V'
    TRA.NombrePA = 'TRAC'
    TRA.ComentarioPA = 'Crea una nueva transaccion'

    ###########################################################################

    TRA.campo = 'PA'
    TRA.CrearCampo(PA=TRA.NombrePA,
                   id_tabla=TRA.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='4',
                   comentario='Procedimiento almacenado',
                   label='Procedimiento almacenado',
                   readonly=True,
                   name=TRA.campo,
                   value=TRA.NombrePA)

    ###########################################################################

    TRA.campo = 'idTransaccion'
    TRA.CrearCampo(PA=TRA.NombrePA,
                   id_tabla=TRA.NumeroTabla,
                   tipo='CHAR',
                   tamaño='5',
                   comentario='Id de transacción',
                   pk=True,
                   nulo=False,
                   label='Id de transacción',
                   name=TRA.campo,
                   placeholder='Indicar el id de transacción',
                   autofocus=True)

    ###########################################################################

    TRA.campo = 'transaccion'
    TRA.CrearCampo(PA=TRA.NombrePA,
                   id_tabla=TRA.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='64',
                   uk=True,
                   nulo=False,
                   comentario='Descripción o nombre de transacción',
                   label='Descripción',
                   name=TRA.campo)

    ###########################################################################

    TRA.campo = 'TransaccionNegocio'
    TRA.CrearCampo(PA=TRA.NombrePA,
                   id_tabla=TRA.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='64',
                   nulo=False,
                   comentario='Descripción de transacción para el negocio',
                   label='Descripción para el negocio',
                   name=TRA.campo)

    ###########################################################################

    TRA.campo = 'transaccionActiva'
    TRA.CrearCampo(PA=TRA.NombrePA,
                   id_tabla=TRA.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Transacción activa o inactiva',
                   default='1',
                   label='Activa',
                   name=TRA.campo)

    ###########################################################################

    TRA.campo = 'AyudaTransaccion'
    TRA.CrearCampo(PA=TRA.NombrePA,
                   id_tabla=TRA.NumeroTabla,
                   tipo='TEXT',
                   comentario='Ayuda para el usuario',
                   nulo=True,
                   label='Ayuda para el usuario',
                   name=TRA.campo,
                   placeholder='Indicar comentarios sobre la funcionalidad')

    ###########################################################################

    TRA.campo = 'id_tabla'
    TRA.CrearCampo(PA=TRA.NombrePA,
                   id_tabla=TRA.NumeroTabla,
                   tipo='CHAR',
                   tamaño='5',
                   comentario='Id de tabla',
                   fk=(TRA.campo, '0030_Tablas', 'idTabla'),
                   label='Id de tabla',
                   name=TRA.campo,
                   placeholder='Indicar el id de la tabla')

    ###########################################################################

    return TRA


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
            sitio.InputList = bd.ObtenerParametros('0050')
            print(sitio.Html(sitio.Body6()))
        except:
            import sys
            print(sys.exc_info())
    else:
        print('TRA importado')
except ImportError:
    print('error al importar TRA.py')
