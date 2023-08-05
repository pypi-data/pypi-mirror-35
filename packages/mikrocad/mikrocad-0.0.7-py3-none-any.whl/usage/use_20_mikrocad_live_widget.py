# -*- coding: utf-8 -*-

### imports ###################################################################
import logging
import sys

### imports from ##############################################################
from PyQt5 import QtWidgets

from mikrocad.mikrocad import MikroCAD
from mikrocad.widgets.mikrocad_live import LiveWidget

###############################################################################
def main():
    logging.basicConfig(level=logging.DEBUG)

    mc = MikroCAD('config/company_mikrocad.cfg')
    mc.initMeasurement()

    app = QtWidgets.QApplication([])
    live_widget = LiveWidget()
    
    handle = live_widget.handle
    mc.start_live_image(handle)

    live_widget.show()
    sys.exit(app.exec_())
    
###############################################################################
if __name__ == '__main__':
    main()
