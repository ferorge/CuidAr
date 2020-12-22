#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fernando Orge
"""

import configApp


def configurar():
    """Configura los campos de la aplicación.
    
    Generar una instancia del objeto CREAR para crear la tabla, la vista y el procedimiento almacenado.
    
    Indicar los atributos por cada tabla, vista y procedimiento almacenado.
    
    Ejecutar el método CrearCampo por cada campo necesario.
    
    Esta función es ejecutada por la función initApp del módulo INIT.py

    >>> print(configurar().NombrePA)
    CAMC
    """

    CAM = configApp.mariaDB.CREAR()
    CAM.NumeroTabla = '0040'
    CAM.NombreTabla = 'Campos'
    CAM.ComentarioTabla = 'Campos de las tablas'
    CAM.NombreVista = 'V'
    CAM.NombrePA = 'CAMC'
    CAM.ComentarioPA = 'Crea un nuevo campo de tabla'

    ###########################################################################

    CAM.campo = 'PA'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla='0010',
                   tipo='VARCHAR',
                   tamaño='4',
                   comentario='Procedimiento almacenado',
                   pk=True,
                   label='Procedimiento almacenado',
                   readonly=True,
                   name=CAM.campo,
                   value=CAM.NombrePA)

    ###########################################################################

    CAM.campo = 'campo'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='24',
                   comentario='Descripción o nombre de campo',
                   pk=True,
                   label='Campo',
                   name=CAM.campo,
                   placeholder='Indicar el campo',
                   autofocus=True)

    ###########################################################################

    CAM.campo = 'campoActivo'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Campo activo o inactivo',
                   default='1',
                   label='Activo',
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'id_tabla'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='5',
                   comentario='Id de tabla',
                   label='Tabla',
                   name=CAM.campo,
                   placeholder='Indicar el nombre de la tabla')

    ###########################################################################

    CAM.campo = 'AyudaUsuario'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='TEXT',
                   comentario='Ayuda para el usuario',
                   nulo=True,
                   label='Ayuda para el usuario',
                   name=CAM.campo,
                   placeholder='Indicar comentarios sobre la funcionalidad')

    ###########################################################################

    CAM.campo = 'TipoDato'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='16',
                   comentario='Tipo de dato admitido',
                   label='Tipo de dato',
                   name=CAM.campo,
                   placeholder='Indicar el tipo de dato')

    ###########################################################################

    CAM.campo = 'tamaño'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='4',
                   comentario='Cantidad máxima de caracteres',
                   nulo=True,
                   label='Tamaño de campo',
                   name=CAM.campo,
                   placeholder='Indicar la cantidad de caracteres')

    ###########################################################################

    CAM.campo = 'comentario'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='128',
                   comentario='Comentario acerca del campo',
                   label='Comentario',
                   name=CAM.campo,
                   placeholder='Indicar un comentario acerca del campo')

    ###########################################################################

    CAM.campo = 'default'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='128',
                   comentario='Valor por defecto del campo',
                   nulo=True,
                   label='Valor por defecto',
                   name=CAM.campo,
                   placeholder='Indicar el valor por defecto del campo')

    ###########################################################################

    CAM.campo = 'nulo'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Valor nulo posible',
                   default='0',
                   label='Permitir valor nulo',
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'signo'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Valor negativo posible',
                   default='0',
                   nulo=True,
                   label='Permitir valor negativo',
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'pk'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Llave primaria de tabla',
                   default='0',
                   label='Llave primaria',
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'uk'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Llave única de tabla',
                   default='0',
                   label='Llave única',
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'posicion'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='SMALLINT',
                   comentario='Ordenamiento en formulario HTML',
                   default='0',
                   label='Orden',
                   name=CAM.campo,
                   type='number',
                   placeholder='Indicar el ordenamiento en formulario')

    ###########################################################################

    CAM.campo = 'label'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='32',
                   comentario='Valor de <label>',
                   label='Etiqueta HTML',
                   name=CAM.campo,
                   placeholder='Indicar el valor de <label>')

    ###########################################################################

    CAM.campo = 'autocomplete'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='1',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'autofocus'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'dirname'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'disabled'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'form'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'formnovalidate'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'list'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'multiple'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'name'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='24',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'pattern'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'placeholder'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='128',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'readonly'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'required'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'size'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='BOOLEAN',
                   comentario='Parámetro para input',
                   default='0',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'type'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='16',
                   comentario='Parámetro para input',
                   label=CAM.campo,
                   name=CAM.campo)

    ###########################################################################

    CAM.campo = 'value'
    CAM.CrearCampo(PA=CAM.NombrePA,
                   id_tabla=CAM.NumeroTabla,
                   tipo='VARCHAR',
                   tamaño='64',
                   comentario='Parámetro para input',
                   label=CAM.campo,
                   name=CAM.campo)
    return CAM


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
            sitio.InputList = bd.ObtenerParametros('0040')
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
    print('error al importar CAM.py')
