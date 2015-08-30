==========================================
MargaritaMixer PyQt QtTest Example Code
==========================================

`MargaritaMixer` demonstrates how to unit test GUIs created with PyQt, the
Python binding of the popular Qt UI and application framework.

See the article
`Test PyQt GUIs with QTest and unittest <http://johnnado.com/pyqt-qtest-example>`_
for documentation. 

`MargaritaMixer` is tested with PyQt4, Python 2.7 and Python 3.4.  To download
and run the unit test::

  hg clone https://jmcgeheeiv@bitbucket.org/jmcgeheeiv/pyqttestexample
  cd pyqttestexample/src
  python MargaritaMixerTest.py

If you change the ``pyqttestexample/src/MargaritaMixer.ui`` user interface 
definition (such as with Qt Designer), you will need to recreate 
``Ui_MargaritaMixer.py`` before running MargaritaMixer again::

   pyuic4 --output Ui_MargaritaMixer.py MargaritaMixer.ui