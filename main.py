import sys
import math
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader


class mainwindow(QWidget):
    def __init__(self):
        super(mainwindow, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
# .................number..............................

        self.ui.btn1.clicked.connect(partial(self.num, '1'))
        self.ui.btn2.clicked.connect(partial(self.num, '2'))
        self.ui.btn3.clicked.connect(partial(self.num, '3'))
        self.ui.btn4.clicked.connect(partial(self.num, '4'))
        self.ui.btn5.clicked.connect(partial(self.num, '5'))
        self.ui.btn6.clicked.connect(partial(self.num, '6'))
        self.ui.btn7.clicked.connect(partial(self.num, '7'))
        self.ui.btn8.clicked.connect(partial(self.num, '8'))
        self.ui.btn9.clicked.connect(partial(self.num, '9'))
        self.ui.btn0.clicked.connect(partial(self.num, '0'))
# ....................def_operation............................
        self.ui.btndarsad.clicked.connect(self.darsad)
        self.ui.btnm.clicked.connect(self.gharine)
        self.ui.btndiv.clicked.connect(self.div)
        self.ui.btnmul.clicked.connect(self.mul)
        self.ui.btnsub.clicked.connect(self.sub)
        self.ui.btnsum.clicked.connect(self.sum)
        self.ui.btnequ.clicked.connect(self.equal)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.btnfloat.clicked.connect(self.dote)
        self.ui.sinbtn.clicked.connect(self.sin)
        self.ui.cosbtn.clicked.connect(self.cos)
        self.ui.sqrtbtn.clicked.connect(self.sqrt)
# --------------------------------------------------------

    def num(self, x):
        self.ui.editor.setText(self.ui.editor.text()+x)

    def equal(self):

        self.b = int(self.ui.editor.text())
        if self.op == '+':
            result = self.a+self.b
        elif self.op == '-':
            result = self.a-self.b
        elif self.op == 'x':
            result = self.a*self.b
        elif self.op == '/':
            result = self.a/self.b
        self.ui.editor.setText(str(result))

    def darsad(self):
        self.op = '%'
        self.a = float(self.ui.editor.text())
        self.ui.editor.setText(str(self.a/100))

    def gharine(self):
        self.op = '-/+'
        self.a = float(self.ui.editor.text())
        self.ui.editor.setText(str(self.a*-1))

    def div(self):
        self.op = '/'
        self.a = float(self.ui.editor.text())
        self.ui.editor.setText("")

    def mul(self):
        self.op = 'x'
        self.a = float(self.ui.editor.text())
        self.ui.editor.setText("")

    def sub(self):
        self.op = '-'
        self.a = float(self.ui.editor.text())
        self.ui.editor.setText("")

    def sum(self):
        self.op = '+'
        self.a = float(self.ui.editor.text())
        self.ui.editor.setText("")

    def dote(self):
        self.a = self.ui.editor.text()
        if (self.a.count('.') == 0):
            self.a = str(self.ui.editor.text() + '.')
            self.ui.editor.setText(self.a)

    def sin(self):
        self.a = self.ui.editor.text()
        if self.a:
            self.ui.editor.setText(str(math.sin(float(self.a))))
        elif self.b:
            self.ui.editor.setText(str(math.sin(float(self.b))))
        self.a = ''

    def cos(self):
        self.a = self.ui.editor.text()
        if self.a:
            self.ui.editor.setText(str(math.cos(float(self.a))))
        elif self.b:
            self.ui.editor.setText(str(math.cos(float(self.b))))
        self.a = ''

    def sqrt(self):
        self.a = self.ui.editor.text()
        if self.a:
            self.ui.editor.setText(str(math.sqrt(float(self.a))))
        self.a = ''

    def clear(self):
        self.ui.editor.setText("")


if __name__ == "__main__":
    app = QApplication([])
    window = mainwindow()
    sys.exit(app.exec_())
