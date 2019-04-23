# Testing of

import sys
import threading
import time

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QThread


def long_task(limit=None, callback=None):
    """
    Any long running task that does not interact with the GUI.
    For instance, external libraries, opening files etc..
    """
    for i in range(limit):
        time.sleep(1)
        print(i)
    if callback is not None:
        callback.loading_stop()


class LongRunning(QThread):
    """
    This class is not required if you're using the builtin
    version of threading.
    """
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def run(self):
        """This overrides a default run function."""
        long_task(self.limit)


class InfoMessage(QtWidgets.QDialog):
    def __init__(self, msg='Loading ', parent=None):
        super(InfoMessage, self).__init__(parent)
        uic.loadUi('loading.ui', self)

        # Initialize Values
        self.o_msg = msg
        self.msg = msg
        self.val = 0

        self.info_label.setText(msg)
        self.show()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_message)
        self.timer.start()

        self.pushButton.clicked.connect(self.pbtest)

    def update_message(self):
        self.val += 1
        self.msg += '.'

        if self.val < 20:
            self.info_label.setText(self.msg)
        else:
            self.val = 0
            self.msg = self.o_msg

    def loading_stop(self):
        self.timer.stop()
        self.info_label.setText("Done")

        # # call self.done(0) to close this dialog instance
        # self.done(0)

    def pbtest(self):
        # pb = QtWidgets.QProgressDialog
        progress = QtWidgets.QProgressDialog("Please Wait!", "Cancel", 0, 100, self)
        progress.setWindowModality(QtCore.Qt.WindowModal)
        progress.setAutoReset(True)
        progress.setAutoClose(True)
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.resize(500, 100)
        progress.setWindowTitle("Loading, Please Wait!")
        progress.show()
        progress.setValue(0)

class MainDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        # QThread Version - Safe to use
        self.my_thread = LongRunning(limit=10)
        self.my_thread.start()
        self.my_loader = InfoMessage('Loading ')
        self.my_thread.finished.connect(self.my_loader.loading_stop)

        # Builtin Threading - Blocking - Do not use
        # self.my_thread = threading.Thread(
        #     target=long_task,
        #     kwargs={'limit': 10}
        # )
        # self.my_thread.start()
        # self.my_loader = InfoMessage('Loading ')
        # self.my_thread.join()  # Code blocks here
        # self.my_loader.loading_stop()

        # Builtin Threading - Callback - Use with caution
        # self.my_loader = InfoMessage('Loading ')
        # self.my_thread = threading.Thread(
        #     target=long_task,
        #     kwargs={'limit': 10,
        #             'callback': self.my_loader}
        # )
        # self.my_thread.start()


def main():
    app = QtWidgets.QApplication(sys.argv)
    dialog = MainDialog()
    app.exec_()

if __name__ == '__main__':
    main()

