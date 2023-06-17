from PyQt5.QtWidgets import*
from PyQt5.QtGui import QFont
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui',self)
        self.show()

        self.setWindowTitle("CodeClause Notepad")
        self.action12.triggered.connect(lambda: self.change_size(12))
        self.action18.triggered.connect(lambda: self.change_size(18))
        self.action24.triggered.connect(lambda: self.change_size(24))

        self.actionOpen.triggered.connect(lambda:self.open_file())
        self.actionSave.triggered.connect(lambda: self.save_file())
        self.actionClose.triggered.connect(exit)

    def change_size(self,size):
        self.plainTextEdit.setFont(QFont("Arial",size))

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "","Text Files(*.txt);; Python(*.py)", options = options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())


    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files(*.txt);; ALL(*)", options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self, event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)

        answer = dialog.exec_()

        if answer == 0:
            self.save_file()
            event.accept()
        elif answer == 2 :
            event.ignore()



def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()