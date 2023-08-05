# -*- coding: utf-8 -*-

### imports ###################################################################
import logging
import sys

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD
from mikrocad.widgets.mikrocad_mainwindow import MikroCADWindow

from PyQt5.QtWidgets import QApplication

###############################################################################
def main():
    # %% setup logger
    logging.basicConfig(level=logging.DEBUG)

    mc = MikroCAD('config\\company_mikrocad.cfg')

    application_name = 'MikroCAD'

    app = QApplication(sys.argv)
    app.setApplicationName(application_name)

    mw = MikroCADWindow(mc)
    mw.showMaximized()
    mw.initDevice()
    
    sys.exit(app.exec_())

###############################################################################
if __name__ == "__main__":
    main()
        