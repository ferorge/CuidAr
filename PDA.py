#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fernando Orge
"""

import configApp


def configurar():
    """Docstring"""
    ###########################################################################

    PDA = configApp.mariaDB.CREAR()
    PDA.NumeroTabla = '0010'
    PDA.NombreTabla = 'PistasAuditoria'
    PDA.ComentarioTabla = 'Registro de ejecución de PistasAuditoria'
    PDA.NombreVista = 'V'
    PDA.NombrePA = 'PDAC'
    PDA.ComentarioPA = 'Crea una nueva pista de auditoria'

    ###########################################################################

    PDA.campo = 'PA'
    PDA.CrearCampo(PA=PDA.NombrePA,
                   id_tabla=PDA.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='4',
                   comentario='Procedimiento almacenado',
                   label='Procedimiento almacenado',
                   readonly=True,
                   name=PDA.campo,
                   value=PDA.NombrePA)

    ###########################################################################

    PDA.campo = 'idAuditoria'
    PDA.CrearCampo(PA=PDA.NombrePA,
                   id_tabla=PDA.NumeroTabla,
                   tipo='MEDIUMINT',
                   tamaño='8',
                   comentario='¿Qué? Id de transacción',
                   pk=True,
                   signo=False,
                   nulo=False,
                   label='Id de pista de auditoria',
                   name=PDA.campo,
                   placeholder='Indicar el id de pista de auditoria',
                   autofocus=True,
                   type='number')

    ###########################################################################

    PDA.campo = 'id_transaccion'
    PDA.CrearCampo(PA=PDA.NombrePA,
                   id_tabla=PDA.NumeroTabla,
                   tipo='CHAR',
                   tamaño='5',
                   nulo=False,
                   comentario='¿Cómo? Descripción o nombre de transacción',
                   label='Id de transacción',
                   name=PDA.campo)

    ###########################################################################

    PDA.campo = 'creado'
    PDA.CrearCampo(PA=PDA.NombrePA,
                   id_tabla=PDA.NumeroTabla,
                   tipo='TIMESTAMP',
                   tamaño='5',
                   nulo=False,
                   default='CURRENT_TIMESTAMP',
                   comentario='¿Cuándo? Fecha y hora de creación del registro',
                   label='Fecha y hora',
                   name=PDA.campo)

    ###########################################################################

    PDA.campo = 'id_usuario'
    PDA.CrearCampo(PA=PDA.NombrePA,
                   id_tabla=PDA.NumeroTabla,
                   tipo='CHAR',
                   tamaño='16',
                   nulo=False,
                   comentario='¿Quién? Id de usuario que creó el registro',
                   label='Id de usuario',
                   name=PDA.campo)

    ###########################################################################

    PDA.campo = 'id_tabla'
    PDA.CrearCampo(PA=PDA.NombrePA,
                   id_tabla=PDA.NumeroTabla,
                   tipo='CHAR',
                   tamaño='5',
                   nulo=False,
                   comentario='¿Dónde? Id de tabla dónde se creó el registro',
                   label='Id de tabla',
                   name=PDA.campo)

    ###########################################################################

    return PDA


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
            sitio.InputList = bd.ObtenerParametros('0010')
            print(sitio.Html(sitio.Body6()))
        except:
            import sys
            print(sys.exc_info())
    else:
        print('PDA importado')
except ImportError:
    print('error al importar PDA.py')
