"""The complete calculator program."""
import sys
from PyQt5.QtWidgets import QApplication
from graphics import CalculatorGUI


def main():
    """Runs the calculator"""
    calc = QApplication(sys.argv)
    window = CalculatorGUI()
    window.show()
    calc.exec_()


if __name__ == '__main__':
    main()
