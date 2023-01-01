# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


import hashlib
import re
from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from dashboard import Ui_MainWindow as dashboard

class Ui_MainWindow(QtWidgets.QMainWindow):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="psudo",
            database="login")
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 589)
        MainWindow.setMinimumSize(QtCore.QSize(955, 589))
        MainWindow.setMaximumSize(QtCore.QSize(955, 589))
        MainWindow.setStyleSheet("background-color: rgb(255, 80, 97);\n"
"background-color: rgb(232, 89, 78);\n"
"background-color: rgb(247, 247, 247);\n"
"background-color: rgb(255, 114, 128);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(390, 120, 461, 371))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.usernamelabel = QtWidgets.QLabel(self.page_1)
        self.usernamelabel.setGeometry(QtCore.QRect(100, 140, 81, 16))
        self.usernamelabel.setObjectName("usernamelabel")
        self.passwordlabel = QtWidgets.QLabel(self.page_1)
        self.passwordlabel.setGeometry(QtCore.QRect(100, 200, 91, 16))
        self.passwordlabel.setObjectName("passwordlabel")
        self.loginButton = QtWidgets.QPushButton(self.page_1)
        self.loginButton.setGeometry(QtCore.QRect(190, 240, 93, 28))
        self.loginButton.setStyleSheet("background-color: rgb(255, 114, 128);\n"
"gridline-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 127);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius: 4px 4px 4px 4px;")
        self.loginButton.setObjectName("loginButton")
        self.signupbutton = QtWidgets.QPushButton(self.page_1)
        self.signupbutton.setGeometry(QtCore.QRect(190, 310, 91, 31))
        self.signupbutton.setStyleSheet("background-color: rgb(255, 114, 128);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 127);\n"
"border-radius: 4px 4px 4px 4px;")
        self.signupbutton.setObjectName("signupbutton")
        self.usernameTextField = QtWidgets.QLineEdit(self.page_1)
        self.usernameTextField.setGeometry(QtCore.QRect(210, 140, 181, 21))
        self.usernameTextField.setStyleSheet("color: rgb(0, 0, 127);\n"
"selection-color: rgb(0, 0, 127);\n"
"border-color: rgb(0, 0, 127);")
        self.usernameTextField.setMaxLength(15)
        self.usernameTextField.setObjectName("usernameTextField")
        self.passwordtextfield = QtWidgets.QLineEdit(self.page_1)
        self.passwordtextfield.setGeometry(QtCore.QRect(210, 200, 181, 22))
        self.passwordtextfield.setStyleSheet("color: rgb(0, 0, 127);")
        self.passwordtextfield.setMaxLength(255)
        self.passwordtextfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordtextfield.setObjectName("passwordtextfield")
        self.label_3 = QtWidgets.QLabel(self.page_1)
        self.label_3.setGeometry(QtCore.QRect(220, 280, 63, 20))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.page_1)
        self.label_5.setGeometry(QtCore.QRect(130, 10, 71, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../Images/pink profile image 80 cropped.jpg"))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.page_1)
        self.label_7.setGeometry(QtCore.QRect(212, 39, 171, 61))
        self.label_7.setStyleSheet("font: 300 24pt \"Yu Gothic Light\";\n"
"color: rgb(0, 0, 127);")
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.username_signup_label = QtWidgets.QLabel(self.page_2)
        self.username_signup_label.setGeometry(QtCore.QRect(100, 60, 71, 16))
        self.username_signup_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 127);")
        self.username_signup_label.setObjectName("username_signup_label")
        self.username_signuptextfield = QtWidgets.QLineEdit(self.page_2)
        self.username_signuptextfield.setGeometry(QtCore.QRect(250, 60, 113, 22))
        self.username_signuptextfield.setStyleSheet("border-color: rgb(0, 0, 127);\n"
"color: rgb(0, 0, 127);")
        self.username_signuptextfield.setMaxLength(15)
        self.username_signuptextfield.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.username_signuptextfield.setObjectName("username_signuptextfield")
        self.website_signup_label = QtWidgets.QLabel(self.page_2)
        self.website_signup_label.setGeometry(QtCore.QRect(100, 90, 61, 16))
        self.website_signup_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.website_signup_label.setObjectName("website_signup_label")
        self.website_signuptextfield = QtWidgets.QLineEdit(self.page_2)
        self.website_signuptextfield.setGeometry(QtCore.QRect(250, 90, 113, 22))
        self.website_signuptextfield.setStyleSheet("color: rgb(0, 0, 127);")
        self.website_signuptextfield.setMaxLength(255)
        self.website_signuptextfield.setObjectName("website_signuptextfield")
        self.email_signup_label = QtWidgets.QLabel(self.page_2)
        self.email_signup_label.setGeometry(QtCore.QRect(100, 130, 55, 16))
        self.email_signup_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.email_signup_label.setObjectName("email_signup_label")
        self.email_signuptextfield = QtWidgets.QLineEdit(self.page_2)
        self.email_signuptextfield.setGeometry(QtCore.QRect(250, 120, 113, 22))
        self.email_signuptextfield.setStyleSheet("color: rgb(0, 0, 127);")
        self.email_signuptextfield.setMaxLength(100)
        self.email_signuptextfield.setObjectName("email_signuptextfield")
        self.city_signup_label = QtWidgets.QLabel(self.page_2)
        self.city_signup_label.setGeometry(QtCore.QRect(100, 160, 55, 21))
        self.city_signup_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.city_signup_label.setObjectName("city_signup_label")
        self.phone_signup_label = QtWidgets.QLabel(self.page_2)
        self.phone_signup_label.setGeometry(QtCore.QRect(100, 200, 55, 16))
        self.phone_signup_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.phone_signup_label.setObjectName("phone_signup_label")
        self.phone_signuptextfield = QtWidgets.QLineEdit(self.page_2)
        self.phone_signuptextfield.setGeometry(QtCore.QRect(250, 200, 113, 22))
        self.phone_signuptextfield.setStyleSheet("color: rgb(0, 0, 127);")
        self.phone_signuptextfield.setMaxLength(11)
        self.phone_signuptextfield.setFrame(True)
        self.phone_signuptextfield.setObjectName("phone_signuptextfield")
        self.password_signup_label = QtWidgets.QLabel(self.page_2)
        self.password_signup_label.setGeometry(QtCore.QRect(100, 240, 71, 16))
        self.password_signup_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.password_signup_label.setObjectName("password_signup_label")
        self.password_signuptextfield = QtWidgets.QLineEdit(self.page_2)
        self.password_signuptextfield.setGeometry(QtCore.QRect(250, 240, 113, 22))
        self.password_signuptextfield.setStyleSheet("color: rgb(0, 0, 127);")
        self.password_signuptextfield.setText("")
        self.password_signuptextfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_signuptextfield.setReadOnly(False)
        self.password_signuptextfield.setObjectName("password_signuptextfield")
        self.confirmpassword_signup_label = QtWidgets.QLabel(self.page_2)
        self.confirmpassword_signup_label.setGeometry(QtCore.QRect(100, 270, 141, 16))
        self.confirmpassword_signup_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.confirmpassword_signup_label.setObjectName("confirmpassword_signup_label")
        self.confirmpassword_signuptextfield = QtWidgets.QLineEdit(self.page_2)
        self.confirmpassword_signuptextfield.setGeometry(QtCore.QRect(250, 270, 113, 22))
        self.confirmpassword_signuptextfield.setStyleSheet("color: rgb(0, 0, 127);")
        self.confirmpassword_signuptextfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirmpassword_signuptextfield.setObjectName("confirmpassword_signuptextfield")
        self.signup_pushbutton = QtWidgets.QPushButton(self.page_2)
        self.signup_pushbutton.setGeometry(QtCore.QRect(180, 300, 93, 28))
        self.signup_pushbutton.setStyleSheet("background-color: rgb(255, 114, 128);\n"
"gridline-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 127);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-radius: 4px 4px 4px 4px;")
        self.signup_pushbutton.setObjectName("signup_pushbutton")
        self.comboBox = QtWidgets.QComboBox(self.page_2)
        self.comboBox.setGeometry(QtCore.QRect(250, 160, 111, 21))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 127);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.signin_LinkButton = QtWidgets.QPushButton(self.page_2)
        self.signin_LinkButton.setGeometry(QtCore.QRect(290, 340, 71, 31))
        self.signin_LinkButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 127);\n"
"font: 9pt \"Sitka Small\";\n"
"selection-color: rgb(85, 170, 255);\n"
"")
        self.signin_LinkButton.setIconSize(QtCore.QSize(20, 20))
        self.signin_LinkButton.setCheckable(False)
        self.signin_LinkButton.setObjectName("signin_LinkButton")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(110, 340, 171, 31))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(80, 10, 331, 41))
        self.label_6.setStyleSheet("font: 700 italic 9pt \"Segoe UI\";")
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.page_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 90, 291, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/resized 300.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 380, 291, 111))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 24pt \"Yu Gothic\";\n"
"font: 700 16pt \"Yu Gothic\";\n"
"background-color: rgb(0, 0, 63);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loginButton.clicked.connect(self.login)
        self.signupbutton.clicked.connect(self.switch_page)
        self.signup_pushbutton.clicked.connect(self.signup)
        self.signin_LinkButton.clicked.connect(self.switch_page)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usernamelabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">Username</span></p></body></html>"))
        self.passwordlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">Password</span></p></body></html>"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.signupbutton.setText(_translate("MainWindow", "Sign Up!"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">  OR</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "LOGIN"))
        self.username_signup_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Username</span></p></body></html>"))
        self.website_signup_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">Website</span></p></body></html>"))
        self.email_signup_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">Email</span></p></body></html>"))
        self.city_signup_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">City</span></p></body></html>"))
        self.phone_signup_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">Phone</span></p></body></html>"))
        self.password_signup_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">Password</span></p></body></html>"))
        self.confirmpassword_signup_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">Confirm Password</span></p></body></html>"))
        self.signup_pushbutton.setText(_translate("MainWindow", "Sign Up"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Islamabad"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Lahore"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Karachi"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Sialkot"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Faisalabad"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Multan"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Quetta"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Peshawar"))
        self.signin_LinkButton.setText(_translate("MainWindow", " Sign In."))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Already have an account!</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#00007f;\">USER INFORMATION</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:400; color:#ff7280;\">@ONEBLOOD</span></p></body></html>"))

    def switch_page(self):
        if self.stackedWidget.currentIndex() == 0:
            self.clearEntries()
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.clearEntries()
            self.stackedWidget.setCurrentIndex(0)
    
    def signup(self):
        username = self.username_signuptextfield.text()
        password = self.password_signuptextfield.text()    
        website= self.website_signuptextfield.text()
        email=self.email_signuptextfield.text()
        city=self.comboBox.currentText()
        phone=self.phone_signuptextfield.text()
        confirmpassword= self.confirmpassword_signuptextfield.text()
        
        # Encrypting the password
        password=hashlib.sha256(password.encode()).hexdigest()
        confirmpassword=hashlib.sha256(confirmpassword.encode()).hexdigest()

        # Validating the input fields
        if(username == "" or password == "" or website == "" or email == "" or city == "" or phone == "" or confirmpassword == ""):
                print("Empty fields")
                QtWidgets.QMessageBox.warning(self, "Error", "Empty Fields")
                self.username_signuptextfield.setText("")
                self.password_signuptextfield.setText("")
                self.website_signuptextfield.setText("")
                self.email_signuptextfield.setText("")
                self.phone_signuptextfield.setText("")
                self.confirmpassword_signuptextfield.setText("")
                return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Invalid Email")
                QtWidgets.QMessageBox.warning(self, "Error", "Invalid Email")
                self.email_signuptextfield.setText("")
                return
        
        if not re.match(r"^[0-9]{11}$", phone):
                print("Invalid Phone Number")
                QtWidgets.QMessageBox.warning(self, "Error", "Invalid Phone Number")
                self.phone_signuptextfield.setText("")
                return
        
        if not re.match(r"^[a-zA-Z0-9]*$", username):
                print("Invalid Username")
                QtWidgets.QMessageBox.warning(self, "Error", "Invalid Username")
                self.username_signuptextfield.setText("")
                return
        
        if not re.match(r"^[a-zA-Z0-9]*$", password):
                print("Invalid Password")
                QtWidgets.QMessageBox.warning(self, "Error", "Invalid Password")
                self.password_signuptextfield.setText("")
                return
        
        if not re.match(r"^[a-zA-Z0-9]*$", confirmpassword):
                print("Invalid Password")
                QtWidgets.QMessageBox.warning(self, "Error", "Invalid Password")
                self.confirmpassword_signuptextfield.setText("")
                return


        # Checking if the password is matched or not
        if(password != confirmpassword):
            print("password not matched")
            QtWidgets.QMessageBox.warning(self, "Error", "Password Not Matched")
            self.password_signuptextfield.setText("")
            self.confirmpassword_signuptextfield.setText("")
    
        else:
            # Adding the data to the database
            mycursor = self.mydb.cursor(buffered=True)
            try:
                mycursor.execute("INSERT INTO sign_up (username, password, website, email, city, Phone_Number) VALUES (%s, %s, %s, %s, %s, %s)", (username, password, website, email, city, phone))
                mycursor.execute("INSERT INTO registered_accounts (userid, username, password, email) SELECT userid, username, password, email FROM sign_up WHERE username = %s", (username, ))
                
                self.mydb.commit()
            except:
                print("error")
                errormsg = QtWidgets.QErrorMessage()
                errormsg.showMessage("An Error Occured. Please Try Again")
                errormsg.exec()

            mycursor.execute("SELECT * FROM registered_accounts")
            print(mycursor.fetchall())

            self.switch_page()

    def login(self):
        login_status = False

        username = self.usernameTextField.text()
        password = self.passwordtextfield.text()

        password = hashlib.sha256(password.encode()).hexdigest()

        mycursor = self.mydb.cursor(buffered=True)
        mycursor.execute("SELECT username, password FROM registered_accounts")        
        
        for x in mycursor:
            if(x[0] == username and x[1] == password):
                print("login successfull")
                login_status = True
                break
        else:
            print("login failed")
            QtWidgets.QMessageBox.warning(self, "Error", "Username or Password is Incorrect")
        
        if(login_status):
            mycursor.execute("INSERT INTO sessions (UserID) SELECT userid FROM registered_accounts WHERE username = %s", (username,))
            self.mydb.commit()

            print("session created")
            self.goToDashboard()
    
    def goToDashboard(self):
        self.dashboard = QtWidgets.QMainWindow()
        self.ui = dashboard()
        self.ui.setupUi(self.dashboard)
        self.dashboard.show()
        MainWindow.hide()

    def clearEntries(self):
        self.usernameTextField.setText("")
        self.passwordtextfield.setText("")
        self.username_signuptextfield.setText("")
        self.password_signuptextfield.setText("")
        self.website_signuptextfield.setText("")
        self.email_signuptextfield.setText("")
        self.phone_signuptextfield.setText("")
        self.confirmpassword_signuptextfield.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())