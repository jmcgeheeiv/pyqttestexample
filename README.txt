MargaritaMixer PyQt QtTest Example Code
                              John McGehee
                             August 30, 2015
                            http://johnnado.com

MargaritaMixer demonstrates how to unit test GUIs created with PyQt, the
Python binding of the popular Qt UI and application framework.

See http://johnnado.com/pyqt-qtest-example for documentation. 

To download and run the unit test:

  hg clone https://jmcgeheeiv@bitbucket.org/jmcgeheeiv/pyqttestexample
  cd pyqttestexample/src
  python MargaritaMixerTest.py     # Requires Python 2.6 or higher

If you change pyqttestexample/src/MargaritaMixer.ui (such as with Qt Designer),
you will need to recreate Ui_MargaritaMixer.py before running Python:

   pyuic4 --output Ui_MargaritaMixer.py MargaritaMixer.ui