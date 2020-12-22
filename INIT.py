#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:12:02 2020

@author: fernando
"""

import configApp


def BD():
    """Crea una instancia de SQL para conexión a BBDD.
    
    Indicar el path al fichero de conexión.
    
    >>> print(BD().pathcfg)
    configApp/.CuidAr.cfg
    """
    bd = configApp.mariaDB.SQL()
    bd.pathcfg = 'configApp/.CuidAr.cfg'
    bd.VerificarConexion()
    return bd


def GUI():
    """Crea una instancia de HTML5 para generar una GUI web.
    
    Indicar los atributos comunes a todos los sitios.
    
    >>> print(GUI().charset)
    UTF-8
    """
    gui = configApp.html5.HTML5()
    gui.lang = "es"
    gui.keywords = 'sistema, gestion, calidad'
    gui.author = 'Fernando Orge'
    gui.CSS = 'css/HojaEstilo.css'
    gui.charset = 'UTF-8'
    gui.viewport = 'width=device-width, initial-scale=1.0'
    gui.refresh = '600'
    gui.nombreAp = 'CuidAr'
    gui.eslogan = 'Sistema de gestión de calidad.'
    gui.title = gui.nombreAp + ' | ' + gui.eslogan
    gui.description = gui.title
    return gui


def initApp():
    """Inicia la aplicación web.
    
    Importa todos los módulos que conforman la aplicación y crea 
    la base de datos, las tablas, vistas y procedimientos almacenados.
    
    Agregar doctest
    """
    import BLO
    bloConfig = BLO.configurar()
    bloConfig.reset(bd)
    bd.RegistrarCampos(bloConfig)
    import PDA
    pdaConfig = PDA.configurar()
    pdaConfig.reset(bd)
    bd.RegistrarCampos(pdaConfig)
    import TAB
    tabConfig = TAB.configurar()
    tabConfig.reset(bd)
    bd.RegistrarCampos(tabConfig)
    import CAM
    camConfig = CAM.configurar()
    camConfig.reset(bd)
    bd.RegistrarCampos(camConfig)


# Programa principal


try:
    if __name__ == '__main__':
        try:
            bd = BD()
            sitio = GUI()
            initApp()
            print(sitio.Html(sitio.BodySimple()))
        except:
            import sys
            print(sys.exc_info())
            import doctest
            doctest.testmod()
    else:
        pass
except ImportError:
    print('error al importar INIT.py')
