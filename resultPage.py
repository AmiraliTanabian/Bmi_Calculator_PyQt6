from ast import literal_eval
from PyQt6.QtCore import QRect, Qt, QMetaObject, QCoreApplication
from PyQt6.QtWidgets import QLabel, QPushButton, QApplication, QWidget, QDialog
from PyQt6.QtGui import QCursor, QPixmap, QIcon
import main
import Suggestions


class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background:rgb(61, 56, 70)")
        self.BmiNumber = QLabel(parent=Form)
        self.BmiNumber.setGeometry(QRect(40, 30, 80, 60))
        self.BmiNumber.setStyleSheet("color:white;font-weight:bold;font-size:40px")
        self.BmiNumber.setObjectName("BmiNumber")
        self.BmiStatus = QLabel(parent=Form)
        self.BmiStatus.setGeometry(QRect(130, 20, 230, 70))
        self.BmiStatus.setStyleSheet("color:white;font-weight:bold; font-size:25px")
        self.BmiStatus.setObjectName("BmiStatus")
        self.closeBtn = QPushButton(parent=Form)
        self.closeBtn.setGeometry(QRect(20, 250, 88, 27))
        self.closeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeBtn.setStyleSheet("color:white;")
        self.closeBtn.setObjectName("closeBtn")
        self.SuggestionsBtn = QPushButton(parent=Form)
        self.SuggestionsBtn.clicked.connect(self.suggestionsBtnPressed)
        self.SuggestionsBtn.setGeometry(QRect(250, 250, 140, 27))
        self.SuggestionsBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SuggestionsBtn.setStyleSheet("color:white;")
        self.SuggestionsBtn.setObjectName("SuggestionsBtn")
        self.MsgLabel = QLabel(parent=Form)
        self.MsgLabel.setGeometry(QRect(20, 100, 361, 121))
        self.MsgLabel.setStyleSheet("color:white; font-size:15px")
        self.MsgLabel.setObjectName("label")

        # Create back button
        self.backBtn = QPushButton(parent=Form)
        self.backBtn.setGeometry(QRect(20, 10, 40, 31))
        self.backBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backBtn.setStyleSheet("background: transparent; border: none;")
        self.backBtn.setText("")
        self.backBtn.clicked.connect(self.backClicked)
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/back.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setObjectName("backBtn")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        self.setUp()

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.BmiNumber.setText(_translate("Form", "135"))
        self.BmiStatus.setText(_translate("Form", "Underweight \n"
"(Severe thinness)    "))
        self.closeBtn.setText(_translate("Form", "Close"))
        self.SuggestionsBtn.setText(_translate("Form", "Suggestions"))
        self.MsgLabel.setText(_translate("Form", "Someone with a BMI below 16.5 has severe underweight, \n"
" which can lead to muscle weakness, vitamin deficiencies, and an increased risk of immune problems and osteoporosis. This condition usually requires medical and nutritional \n"
" intervention."))

    def setUp(self):
        # open result.txt and read the result where send on "main.py"
        with open("result.txt", 'r') as File:
            # The file is not compact enough to use loops.
            result = File.read()
        result = dict(literal_eval(result))

        self.BmiStatus.setText(result['title'])
        self.BmiNumber.setText(str(round(result['bmi'], 1)))
        self.MsgLabel.setText(result['msg'])
        color = result['color']
        self.BmiStatus.setStyleSheet(f'color:{color}; font-weight:bold; font-size:25px')
        self.BmiNumber.setStyleSheet(f'color:{color}; font-weight:bold;font-size:40px')

    def backClicked(self):
        # close current window
        self.Form.close()

        # Open The main window
        SecondForm = QDialog()
        SecondUi = main.Ui_Form()
        SecondUi.setupUi(SecondForm)
        SecondForm.show()
        SecondForm.exec()

    def suggestionsBtnPressed(self):
        'Open the suggestions page'
        SecondForm = QDialog()
        SecondUi = Suggestions.Ui_Form()
        SecondUi.setupUi(SecondForm)
        SecondForm.show()
        SecondForm.exec()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
