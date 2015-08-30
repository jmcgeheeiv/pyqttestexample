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
Test the margarita mixer GUI.
"""

__author__ = "John McGehee, http://johnnado.com/"
__version__ = "$Revision: 1.1 $"
__date__ = "$Date: 2015/07/30 $"
__copyright__ = "Copyright 2011 Voom, Inc."

import sys
import unittest
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt

import MargaritaMixer

app = QApplication(sys.argv)

class MargaritaMixerTest(unittest.TestCase):
    '''Test the margarita mixer GUI'''
    def setUp(self):
        '''Create the GUI'''
        self.form = MargaritaMixer.MargaritaMixer()

    def setFormToZero(self):
        '''Set all ingredients to zero in preparation for setting just one
        to a nonzero value.
        '''
        self.form.ui.tequilaScrollBar.setValue(0)
        self.form.ui.tripleSecSpinBox.setValue(0)
        self.form.ui.limeJuiceLineEdit.setText("0.0")
        self.form.ui.iceHorizontalSlider.setValue(0)

    def test_defaults(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.form.ui.tequilaScrollBar.value(), 8)
        self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 4)
        self.assertEqual(self.form.ui.limeJuiceLineEdit.text(), "12.0")
        self.assertEqual(self.form.ui.iceHorizontalSlider.value(), 12)
        self.assertEqual(self.form.ui.speedButtonGroup.checkedButton().text(), "&Karate Chop")

        # Class is in the default state even without pressing OK
        self.assertEqual(self.form.jiggers, 36.0)
        self.assertEqual(self.form.speedName, "&Karate Chop")
        
        # Push OK with the left mouse button
        okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.jiggers, 36.0)
        self.assertEqual(self.form.speedName, "&Karate Chop")
        

    def test_tequilaScrollBar(self):
        '''Test the tequila scroll bar'''
        self.setFormToZero()
        
        # Test the maximum.  This one goes to 11.
        self.form.ui.tequilaScrollBar.setValue(12)
        self.assertEqual(self.form.ui.tequilaScrollBar.value(), 11)

        # Test the minimum of zero.
        self.form.ui.tequilaScrollBar.setValue(-1)
        self.assertEqual(self.form.ui.tequilaScrollBar.value(), 0)

        self.form.ui.tequilaScrollBar.setValue(5)
        
        # Push OK with the left mouse button
        okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.jiggers, 5)
   
    def test_tripleSecSpinBox(self):
        '''Test the triple sec spin box.
        Testing the minimum and maximum is left as an exercise for the reader.
        '''
        self.setFormToZero()
        self.form.ui.tripleSecSpinBox.setValue(2)

        # Push OK with the left mouse button
        okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.jiggers, 2)
        
    def test_limeJuiceLineEdit(self):
        '''Test the lime juice line edit.
        Testing the minimum and maximum is left as an exercise for the reader.
        '''
        self.setFormToZero()
        # Clear and then type "3.5" into the lineEdit widget
        self.form.ui.limeJuiceLineEdit.clear()
        QTest.keyClicks(self.form.ui.limeJuiceLineEdit, "3.5")

        # Push OK with the left mouse button
        okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.jiggers, 3.5)

    def test_iceHorizontalSlider(self):
        '''Test the ice slider.
        Testing the minimum and maximum is left as an exercise for the reader.
        '''
        self.setFormToZero()
        self.form.ui.iceHorizontalSlider.setValue(4)

        # Push OK with the left mouse button
        okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.jiggers, 4)
        
    def test_liters(self):
        '''Test the jiggers-to-liters conversion.'''
        self.setFormToZero()
        self.assertAlmostEqual(self.form.liters, 0.0)
        self.form.ui.iceHorizontalSlider.setValue(1)
        self.assertAlmostEqual(self.form.liters, 0.0444)
        self.form.ui.iceHorizontalSlider.setValue(2)
        self.assertAlmostEqual(self.form.liters, 0.0444 * 2)
        
    def test_blenderSpeedButtons(self):
        '''Test the blender speed buttons'''
        self.form.ui.speedButton1.click()
        self.assertEqual(self.form.speedName, "&Mix")
        self.form.ui.speedButton2.click()
        self.assertEqual(self.form.speedName, "&Whip")
        self.form.ui.speedButton3.click()
        self.assertEqual(self.form.speedName, "&Puree")
        self.form.ui.speedButton4.click()
        self.assertEqual(self.form.speedName, "&Chop")
        self.form.ui.speedButton5.click()
        self.assertEqual(self.form.speedName, "&Karate Chop")
        self.form.ui.speedButton6.click()
        self.assertEqual(self.form.speedName, "&Beat")
        self.form.ui.speedButton7.click()
        self.assertEqual(self.form.speedName, "&Smash")
        self.form.ui.speedButton8.click()
        self.assertEqual(self.form.speedName, "&Liquefy")
        self.form.ui.speedButton9.click()
        self.assertEqual(self.form.speedName, "&Vaporize")


if __name__ == "__main__":
    unittest.main()
