import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.EncryptBtn.clicked.connect(self.call_api_encrypt)
        self.ui.DecryptBtn.clicked.connect(self.call_api_decrypt)
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plainTextTxt.toPlainText(),
            "key": int(self.ui.KeyTxt.toPlainText())
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.ui.CiphertextTxt.setPlainText(response.json()["encrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypt Successfully")
                msg.exec_()
            else:
                print("Error when calling API")
        except requests.exceptions.RequestException as e:
            print("Error : %s" % str(e))
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.CiphertextTxt.toPlainText(),
            "key": int(self.ui.KeyTxt.toPlainText())
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.ui.plainTextTxt.setPlainText(response.json()["decrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypt Successfully")
                msg.exec_()
            else:
                print("Error when calling API")
        except requests.exceptions.RequestException as e:
            print("Error : %s" % str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())