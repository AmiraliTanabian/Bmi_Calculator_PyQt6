from PyQt6.QtWidgets import QPushButton, QDialog, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QApplication
import resultPage
from PyQt6.QtGui import QCursor, QDoubleValidator
from PyQt6.QtCore import QRect, Qt, QMetaObject, QCoreApplication

class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(370, 303)
        Form.setStyleSheet("background-color:rgb(61, 56, 70)")
        self.CloseBtn = QPushButton(parent=Form)
        self.CloseBtn.setGeometry(QRect(40, 230, 88, 27))
        self.CloseBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CloseBtn.setObjectName("CloseBtn")
        self.CloseBtn.clicked.connect(self.close)
        self.CalcBtn = QPushButton(parent=Form)
        self.CalcBtn.setGeometry(QRect(250, 230, 88, 27))
        self.CalcBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CalcBtn.setObjectName("CalcBtn")
        self.CalcBtn.clicked.connect(self.calcBtnPressed)
        self.label_3 = QLabel(parent=Form)
        self.label_3.setGeometry(QRect(140, 20, 110, 19))
        self.label_3.setStyleSheet("color:white;font-weight:bold;")
        self.label_3.setObjectName("label_3")
        self.widget = QWidget(parent=Form)
        self.widget.setGeometry(QRect(80, 50, 220, 83))
        self.widget.setObjectName("widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HeightLbl = QLabel(parent=self.widget)
        self.HeightLbl.setStyleSheet("color:white;")
        self.HeightLbl.setObjectName("HeightLbl")
        self.horizontalLayout.addWidget(self.HeightLbl)
        self.HeightEdit = QLineEdit(parent=self.widget)
        self.HeightEdit.setStyleSheet("border:1px solid white; border-radius:2.5px; color:white;")
        self.HeightEdit.setObjectName("HeightEdit")
        self.HeightEdit.setPlaceholderText(" m ")
        self.HeightEdit.setValidator(QDoubleValidator(100, 250, 3))
        self.horizontalLayout.addWidget(self.HeightEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.WeightLbl = QLabel(parent=self.widget)
        self.WeightLbl.setStyleSheet("color:white;")
        self.WeightLbl.setObjectName("WeightLbl")
        self.horizontalLayout_2.addWidget(self.WeightLbl)
        self.WeightEdit = QLineEdit(parent=self.widget)
        self.WeightEdit.setPlaceholderText("Kg")
        self.WeightEdit.setValidator(QDoubleValidator(30, 300, 3))
        self.WeightEdit.setStyleSheet("border:1px solid white; border-radius:2.5px; color:white;")
        self.WeightEdit.setObjectName("WeightEdit")
        self.horizontalLayout_2.addWidget(self.WeightEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BMI Calculator"))
        self.CloseBtn.setText(_translate("Form", "Close"))
        self.CalcBtn.setText(_translate("Form", "Calc"))
        self.label_3.setText(_translate("Form", "BMI Calculator"))
        self.HeightLbl.setText(_translate("Form", "Height"))
        self.WeightLbl.setText(_translate("Form", "Weight"))

    def close(self):
        raise SystemExit


    def calcBtnPressed(self):
        height = float(self.HeightEdit.text())
        weight = float(self.WeightEdit.text())

        bmi = weight / height ** 2

        # Severely underweight
        if bmi < 16.5 :
            self.bmi_group = 1
            result = {
                'title': 'Severely underweight',
                'msg' : '''A BMI below 16.5 indicates severe underweight, leading to health risks like weakness and nutrient deficiencies.\n
                Medical and nutritional support is often needed.''',
                'color':'#FF4D4D',
            }

        # Underweight
        elif 16.5 < bmi < 18.5 :
            self.bmi_group = 2
            result = {
                'title': 'Underweight',
                'msg': '''Someone with a BMI between 16.5 and 18.5 is \nunderweight, which may cause low energy, weakened immunity,
\nand nutritional deficiencies.\nA balanced diet and proper care can help restore a\nhealthy weight.''',
                'color':'#FFA07A',
            }

        # Normal
        elif 18.5 < bmi < 25 :
            self.bmi_group = 3
            result = {
                'title': 'Normal',
                'msg': '''Someone with a BMI between 18.5 and 25 has a\nnormal weight, indicating a balanced body\ncomposition.
Maintaining a healthy diet and\nlifestyle helps sustain this condition.''',
                'color':'#32CD32',
            }

        # Overweight
        elif 25 < bmi < 30 :
            self.bmi_group = 4
            result = {
                'title': 'Overweight',
                'msg': '''Someone with a BMI between 25 and 30 is overweight,\nwhich may increase the risk of
health issues over time.\nA balanced diet and regular exercise can help\nmanage weight effectively.''',
                'color':'#FFD700',

            }

        # Grade 1 obesity
        elif 30 < bmi < 35 :
            self.bmi_group = 5
            result = {
                'title': 'Grade 1 obesity',
                'msg':'''Someone with a BMI of 30-35 is obese, increasing the risk of health issues like heart disease and diabetes,\n
                often due to poor lifestyle choices and requiring monitoring.''',
                'color':'#FF8C00',
            }

        # Obesity grade 2
        elif 35 < bmi < 40 :
            self.bmi_group = 6
            result = {
                'title': 'Obesity grade 2',
                'msg': '''A BMI of 35-40 indicates class 2 obesity, raising risks of heart disease,\nstroke, and diabetes.
Managing it often requires medical intervention and lifestyle changes.''',

                'color':'#FF4500'
            }

        # Obesity grade 3
        elif bmi > 40 :
            self.bmi_group = 7
            result = {
                'title': 'Obesity grade 3',
                'msg': '''A BMI above 40 indicates class 3 (extreme) obesity, posing high risks for heart failure,\nstroke, and severe diabetes.
Intensive treatment, lifestyle changes\nand possibly surgery are often needed.''',
                'color':'#8B0000',
            }

        # add Bmi number to result
        result.update({'bmi':bmi})


        # Write 'result' on txt file to show on the result page
        with open('result.txt', 'w') as File:
            File.write(str(result))

        # Write bmi_group on group.txt to use for "Suggestions.py"
        with open('group.txt', 'w') as File2 :
            File2.write(str(self.bmi_group))

        # close current window
        self.Form.close()

        # Open result Page
        SecondForm = QDialog()
        SecondUi = resultPage.Ui_Form()
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
