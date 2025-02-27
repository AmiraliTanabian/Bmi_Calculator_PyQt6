from PyQt6.QtCore import QRect, QMetaObject, QCoreApplication, Qt
from PyQt6.QtWidgets import QLabel, QWidget, QDialog, QApplication, QPushButton
from PyQt6.QtGui import QIcon, QCursor, QPixmap

class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(472, 557)
        Form.setStyleSheet("border-radius:5px; background-color:rgb(36, 31, 49)")
        self.mainTitle = QLabel(parent=Form)
        self.mainTitle.setGeometry(QRect(180, 10, 120, 21))
        self.mainTitle.setStyleSheet("color:white;font-weight:bold;font-size:18px")
        self.mainTitle.setObjectName("mainTitle")
        self.subTitle1 = QLabel(parent=Form)
        self.subTitle1.setGeometry(QRect(10, 40, 190, 19))
        self.subTitle1.setStyleSheet("color:white; font-weight:bold; border-radius:2.5px; border:1px solid white;")
        self.subTitle1.setObjectName("subTitle1")
        self.subText = QLabel(parent=Form)
        self.subText.setGeometry(QRect(10, 70, 460, 80))
        self.subText.setStyleSheet("color:white;")
        self.subText.setObjectName("subText")
        self.subTitle2 = QLabel(parent=Form)
        self.subTitle2.setGeometry(QRect(10, 160, 190, 19))
        self.subTitle2.setStyleSheet("color:white; font-weight:bold; border-radius:2.5px; border:1px solid white;")
        self.subTitle2.setObjectName("subTitle2")
        self.subText2 = QLabel(parent=Form)
        self.subText2.setGeometry(QRect(10, 190, 460, 80))
        self.subText2.setStyleSheet("color:white;")
        self.subText2.setObjectName("subText2")
        self.subTitle3 = QLabel(parent=Form)
        self.subTitle3.setGeometry(QRect(10, 280, 190, 19))
        self.subTitle3.setStyleSheet("color:white; font-weight:bold; border-radius:2.5px; border:1px solid white;")
        self.subTitle3.setObjectName("subTitle3")
        self.subText3 = QLabel(parent=Form)
        self.subText3.setGeometry(QRect(10, 300, 460, 80))
        self.subText3.setStyleSheet("color:white;")
        self.subText3.setObjectName("subText3")
        self.subTitle4 = QLabel(parent=Form)
        self.subTitle4.setGeometry(QRect(10, 390, 190, 19))
        self.subTitle4.setStyleSheet("color:white; font-weight:bold; border-radius:2.5px; border:1px solid white;")
        self.subTitle4.setObjectName("subTitle4")
        self.subText4 = QLabel(parent=Form)
        self.subText4.setGeometry(QRect(10, 420, 460, 80))
        self.subText4.setStyleSheet("color:white;")
        self.subText4.setObjectName("subText4")
        self.alertLbl = QLabel(parent=Form)
        self.alertLbl.setGeometry(QRect(10, 500, 460, 41))
        self.alertLbl.setStyleSheet("color:white; font-weight:bold;font-size:12px;")
        self.alertLbl.setObjectName("alertLbl")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        # Create cancel (close) button
        self.cancelBtn = QPushButton(parent=Form)
        self.cancelBtn.setGeometry(QRect(20, 10, 41, 27))
        self.cancelBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancelBtn.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/CloseIcon.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancelBtn.setIcon(icon)
        self.cancelBtn.clicked.connect(self.closeBtnClicked)
        self.cancelBtn.setObjectName("cancelBtn")

        self.setUp()

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Suggestions"))
        self.mainTitle.setText(_translate("Form", "Suggestions"))
        self.alertLbl.setText(
            _translate("Form", "In the end, these are all just suggestions. Make sure to take your health seriously\n"
                               "and consulta doctor for accurate information."))
    def firstStatus(self):
        _translate = QCoreApplication.translate
        self.subTitle1.setText(_translate("Form", "Increase Caloric Intake"))
        self.subText.setText(_translate("Form", "Consumehigh-calorie and nutritious meals such as nuts,\n"
                                                " peanut butter, full-fat dairy, and dried fruits."))
        self.subTitle2.setText(_translate("Form", "Get Enough Protein"))
        self.subText2.setText(_translate("Form", "Increase the intake of protein sources like meat,  \n"
                                                 " eggs, dairy, and legumes to support healthy weight gain."))
        self.subTitle3.setText(_translate("Form", "Strength Training"))
        self.subText3.setText(_translate("Form", "Engage in strength exercises like \n"
                                                 " weightlifting to help build muscle mass."))
        self.subTitle4.setText(_translate("Form", "Increase Meal Frequency"))
        self.subText4.setText(_translate("Form", "Eat 5 to 6 meals a day instead of the usual 3 to ensure\n"
                                                 "sufficient calorie intake.\n"))


    def secondStatus(self):
        _translate = QCoreApplication.translate
        self.subTitle3.setGeometry(QRect(10, 280, 147, 19))
        self.subTitle2.setGeometry(QRect(10, 160, 236, 19))
        self.subTitle1.setGeometry(QRect(10, 40, 155, 19))
        self.subTitle4.setGeometry(QRect(10, 390, 170, 19))
        self.subTitle1.setText(_translate("Form", "Seek Medical Advice"))
        self.subText.setText(_translate("Form", """Immediately consult a healthcare professional to rule out any\n
        underlying medical conditions causing severe underweight."""))
        self.subTitle2.setText(_translate("Form", "High-Calorie, Nutrient-Rich Diet"))
        self.subText2.setText(_translate("Form", """Focus on consuming high-calorie foods that are also rich in nutrients, such as nuts\n
        dried fruits, whole grains, and healthy fats like olive oil."""))
        self.subTitle3.setText(_translate("Form", "Regular Monitoring"))
        self.subText3.setText(_translate("Form", """ Keep track of your weight and dietary intake regularly to ensure you are\n
        progressing towards a healthier weight."""))
        self.subTitle4.setText(_translate("Form", "Consider Supplements\n"
                                                  "\n"))
        self.subText4.setText(_translate("Form", """Under medical supervision, consider taking nutritional supplements\n
        to help meet your daily caloric and nutritional needs."""))

    def thirdStatus(self):
        _translate = QCoreApplication.translate
        self.subTitle3.setGeometry(QRect(10, 280, 170, 19))
        self.subTitle2.setGeometry(QRect(10, 160, 180, 19))
        self.subTitle1.setGeometry(QRect(10, 40, 150, 19))
        self.subTitle4.setGeometry(QRect(10, 390, 190, 19))
        self.subTitle1.setText(_translate("Form", "Maintain a Balanced Diet"))
        self.subText.setText(_translate("Form", """Continue eating a variety of nutrient-rich foods, including
fruits, vegetables,lean proteins, and whole grains"""))
        self.subTitle2.setText(_translate("Form", "Regular Physical Activity"))
        self.subText2.setText(_translate("Form", """Engage in regular exercise, such as walking, cycling, or 
strength training to support overall health and fitness.."""))
        self.subTitle3.setText(_translate("Form", "Monitor Portion Sizes:"))
        self.subText3.setText(_translate("Form", """Be mindful of portion sizes to avoid overeating and ensure 
you're consuming the right amount of calories for your activity level."""))
        self.subTitle4.setText(_translate("Form", "Routine Health Check-ups"))
        self.subText4.setText(_translate("Form", """Schedule regular check-ups with your healthcare provider to monitor\n
your health and catch any potential issues early."""))

    def fourthStatus(self):
        _translate = QCoreApplication.translate
        self.subTitle3.setGeometry(QRect(10, 280, 145, 19))
        self.subTitle2.setGeometry(QRect(10, 160, 185, 19))
        self.subTitle1.setGeometry(QRect(10, 40, 165, 19))
        self.subTitle4.setGeometry(QRect(10, 390, 172, 19))
        self.subTitle1.setText(_translate("Form", "Healthy Eating Habits"))
        self.subText.setText(_translate("Form", """Focus on a balanced diet with plenty of fruits, vegetables
, lean proteins, and whole grains while ducing intake of processed 
foods and sugary drinks."""))
        self.subTitle2.setText(_translate("Form", "Increase Physical Activity"))
        self.subText2.setText(_translate("Form", """ Aim for at least 30 minutes of moderate exercise, 
such as brisk walking or swimming, most days of the 
week to help with weight management."""))
        self.subTitle3.setText(_translate("Form", "Set Realistic Goals"))
        self.subText3.setText(_translate("Form", """Set achievable weight loss goals and track your progress to
stay motivated and make gradual, sustainable changes."""))
        self.subTitle4.setText(_translate("Form", "Consult a Professional"))
        self.subText4.setText(_translate("Form", """ Seek guidance from a dietitian or healthcare provider to 
create a personalized plan that addresses your specific needs 
and health goals."""))

    def fifthStatus(self):
        _translate = QCoreApplication.translate
        self.subTitle3.setGeometry(QRect(10, 280, 150, 19))
        self.subTitle2.setGeometry(QRect(10, 160, 215, 19))
        self.subTitle1.setGeometry(QRect(10, 40, 180, 19))
        self.subTitle4.setGeometry(QRect(10, 390, 195, 19))
        self.subTitle1.setText(_translate("Form", "Adopt a Structured Diet Plan"))
        self.subText.setText(_translate("Form", """Follow a well-balanced, calorie-controlled diet plan 
that emphasizes whole foods, lean proteins, 
and vegetables while limiting high-calorie and processed foods."""))
        self.subTitle2.setText(_translate("Form", "Incorporate Regular Exercise"))
        self.subText2.setText(_translate("Form", """ Engage in regular physical activity, such as brisk walking, cycling, 
or swimming, for at least 30-60 minutes most days of the 
week to support weight loss. week to help with weight management."""))
        self.subTitle3.setText(_translate("Form", "Behavioral Changes"))
        self.subText3.setText(_translate("Form", """Identify and address emotional or habitual eating patterns, and 
consider techniques like mindful eating or keeping a food diary
to stay on track."""))
        self.subTitle4.setText(_translate("Form", "Seek Professional Support"))
        self.subText4.setText(_translate("Form", """Consult with a healthcare provider, dietitian, or weight management specialist to develop
a safe and effective weight loss plan tailored to your needs."""))

    def sixthStatus(self):
        _translate = QCoreApplication.translate
        self.subTitle3.setGeometry(QRect(10, 280, 165, 19))
        self.subTitle2.setGeometry(QRect(10, 160, 182, 19))
        self.subTitle1.setGeometry(QRect(10, 40, 154, 19))
        self.subTitle4.setGeometry(QRect(10, 390, 160, 19))
        self.subTitle1.setText(_translate("Form", "Controlled Diet Plan"))
        self.subText.setText(_translate("Form", """Follow a low-calorie, nutrient-rich diet plan under the supervision of 
a nutritionist to achieve safe and effective weight loss."""))
        self.subTitle2.setText(_translate("Form", "Regular Physical Activity"))
        self.subText2.setText(_translate("Form", """Engage in regular physical activities such as walking, swimming, or
strength training for at least 60 minutes a day."""))
        self.subTitle3.setText(_translate("Form", "Psychological Support"))
        self.subText3.setText(_translate("Form", """Seek counseling or join support groups to manage psychological 
factors like stress or emotional eating."""))
        self.subTitle4.setText(_translate("Form", "Medical Intervention"))
        self.subText4.setText(_translate("Form", """Consult with your doctor about treatment options such 
as medications or structured weight loss programs."""))


    def seventhStatus(self):
        _translate = QCoreApplication.translate
        self.subTitle3.setGeometry(QRect(10, 280, 150, 19))
        self.subTitle2.setGeometry(QRect(10, 160, 125, 19))
        self.subTitle1.setGeometry(QRect(10, 40, 154, 19))
        self.subTitle4.setGeometry(QRect(10, 390, 205, 19))
        self.subTitle1.setText(_translate("Form", "Structured Diet Plan"))
        self.subText.setText(_translate("Form", """Follow a medically supervised, very low-calorie diet plan that 
focuses on nutrient-dense foods to promote significant weight loss."""))
        self.subTitle2.setText(_translate("Form", "Regular Exercise	"))
        self.subText2.setText(_translate("Form", """Incorporate low-impact exercises like swimming,walking, or yoga
into your daily routine, aiming for at least 60 minutes of activity most days."""))
        self.subText2.setStyleSheet("color:white; font-size:13px")
        self.subTitle3.setText(_translate("Form", "Behavioral Therapy"))
        self.subText3.setText(_translate("Form", """Work with a therapist or counselor to address emotional eating,
stress, and other psychological factors contributing to obesity."""))
        self.subTitle4.setText(_translate("Form", "Medical or Surgical Options"))
        self.subText4.setText(_translate("Form", """Consult with a healthcare provider to explore advanced treatment 
options, such as weight loss medications or bariatric surgery, if necessary."""))
        self.subText4.setStyleSheet('color:white; font-size:13px;')

    def setUp(self):
        'The main function --> read file(group.txt) then according bmi group run one of the above functions'

        # Read bmi_group on group.txt where write on main.py
        with open('group.txt') as File:
            group = int(File.read())

        group_with_status = {
            1:self.firstStatus,
            2:self.secondStatus,
            3:self.thirdStatus,
            4:self.fourthStatus,
            5:self.fifthStatus,
            6:self.sixthStatus,
            7:self.seventhStatus
        }

        # Run the function according BMI group number
        group_with_status[group]()

    def closeBtnClicked(self):
        'Close current window'
        self.Form.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
