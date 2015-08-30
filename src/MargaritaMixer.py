# vim: set fileencoding=utf-8 :
# $Header:  $
#
# Copyright 2011 Voom, Inc.
#
# This file is part of the Voom PyQt QTest Example.
# See http://www.voom.net/pyqt-qtest-example/ for documentation.
#
# PyQt QTest Example is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyQt QTest Example is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyQt QTest Example.  If not, see <http://www.gnu.org/licenses/>.

"""
GUI for a margarita mixing machine.
Extract Ui_MargaritaMixer.py using:
   pyuic4 --output Ui_MargaritaMixer.py MargaritaMixer.ui
"""

__author__ = "John McGehee, http://johnnado.com/"
__version__ = "$Revision: 1.1 $"
__date__ = "$Date: 2015/07/30 $"
__copyright__ = "Copyright 2011 Voom, Inc."

import sys
from PyQt4 import QtGui, QtCore

from Ui_MargaritaMixer import Ui_MargaritaMixer

class MargaritaMixer(QtGui.QWidget):
  
    def __init__(self):
        super(MargaritaMixer, self).__init__()
        
        self.ui = Ui_MargaritaMixer()
        self.ui.setupUi(self)
        
    @property
    def jiggers(self):
        '''Return the total volume of the margaritas in units of jiggers.
        One jigger is 0.0444 liters.
        '''
        jiggersTequila = self.ui.tequilaScrollBar.value()
        jiggersTripleSec = self.ui.tripleSecSpinBox.value()
        jiggersLimeJuice = float(self.ui.limeJuiceLineEdit.text())
        jiggersIce = self.ui.iceHorizontalSlider.value()
        return jiggersTequila + jiggersTripleSec + jiggersLimeJuice + jiggersIce
    
    @property
    def liters(self):
        '''Return the total volume of the margaritas in liters.'''
        return 0.0444 * self.jiggers
        
    @property
    def speedName(self):
        speedButton = self.ui.speedButtonGroup.checkedButton()
        if speedButton is None:
            return None
        return speedButton.text()

    def accept(self):
        '''Execute the command in response to the OK button.'''
        print('The volume of drinks is {0} liters ({1} jiggers).'
              ''.format(self.liters, self.jiggers))
        print('The blender is running at speed "{0}"'.format(self.speedName))
        self.close()

    def reject(self):
        '''Cancel.'''
        self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MargaritaMixer()
    myapp.show()
    sys.exit(app.exec_())
