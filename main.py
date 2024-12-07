import sys
from PyQt5.QtWidgets import QApplication
from OS_UI import OS_UI  # Import UI class

def main():
    app = QApplication(sys.argv)
    window = OS_UI()  # Create the UI window
    window.show()  # Display the UI
    sys.exit(app.exec_())  # Execute the app

if __name__ == "__main__":
    main()
