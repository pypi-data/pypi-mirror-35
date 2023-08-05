# -*- coding: utf-8 -*-

### imports ###################################################################
import logging

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QGroupBox
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QVBoxLayout

###############################################################################
class SequencerBox(QGroupBox):
    '''
    PositionsWidget
    '''
    def __init__(self):
        super(SequencerBox, self).__init__()

        self.logger = logging.getLogger('mikrocad_widget')

        self.initUI()
        # self.initEvents()
        
    def initUI(self):
        self.setStyleSheet(
            "QLabel, " +
            "QListWidget, " +
            "QGroupBox { font-size: 14pt; } QGroupBox { font-weight: bold; }"
        )

        self.setTitle("Messpunkte")

        self.sequencer_widget = SequenceWidget()
        
        layout = QVBoxLayout()
        layout.addWidget(self.sequencer_widget)

        self.setLayout(layout)

    def initEvents(self):
        pass

###############################################################################
class SequenceWidget(QListWidget):
    def __init__(self):
        super(SequenceWidget, self).__init__()

    def set_items(self, receipe):
        self.clear()
        
        for r in receipe:
            name = r['name']
            finished = r['finished']
            
            item = QListWidgetItem()
            
            if finished:
                item.setForeground(Qt.green)

            item.setText(name)
            self.addItem(item)
    
                

###############################################################################
if __name__ == '__main__':
    receipe = (
            {'name': 'Kante', 'finished': True},
            {'name': 'Notch', 'finished': False})

    app = QApplication([])

    pw = SequencerBox()

    pw.show()
    pw.sequence_widget.set_items(receipe)


    app.exec_()
