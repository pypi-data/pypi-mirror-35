# -*- coding: utf-8 -*-

### imports ###################################################################
import logging
import sys

### imports from ##############################################################
from PyQt5.QtWidgets import QApplication

# from mikrocad.mikrocad import MikroCAD
from mikrocad.widgets.mikrocad_live import LiveWidget

###############################################################################
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = QApplication([])
    live_widget = LiveWidget(False)
    
    handle = live_widget.handle

    live_widget.show()
    sys.exit(app.exec_())
