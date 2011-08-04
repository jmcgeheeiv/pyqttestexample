                    MargaritaMixer PyQt QtTest Example Code
                              John McGehee
                              August 1, 2011
                            http://www.voom.net

MargaritaMixer demonstrates how to unit test GUIs created with PyQt, the
Python binding of the popular Qt UI and application framework.

See http://www.voom.net/pyqt-qtest-example for documentation. 

To download and run the unit test:

  hg clone https://voom.kilnhg.com/Repo/Make-Stuff-Happen/Group/PyQtTestExample
  cd PyQtTestExample/src
  python MargaritaMixerTest.py     # Requires Python 2.6 or higher

If you change PyQtTestExample/src/MargaritaMixer.ui (such as with Qt Designer),
you will need to recreate Ui_MargaritaMixer.py before running Python:

   pyuic4 --output Ui_MargaritaMixer.py MargaritaMixer.ui
