"""Simple calculator with a graphical_user_interface."""
from calculation import CalculatorCalculations
from PyQt5.QtWidgets import (QMainWindow, QWidget,
                             QLineEdit, QPushButton, QGridLayout)
from PyQt5.QtGui import QIcon, QFont


class CalculatorGUI(QMainWindow):
    """Generates the GUI for the calculator"""
    def __init__(self):
        super().__init__()
        self.calculations = CalculatorCalculations(self)
        self.init_graphics()

    def init_graphics(self):
        """Initializes the GUI"""
        self.setWindowTitle('Calculator de Ephraim')
        self.setGeometry(300, 300, 400, 250)

        font = QFont('Fira Code', 15)
        font.setBold(True)
        self.setFont(font)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # layout = QVBoxLayout()
        grid = QGridLayout()
        central_widget.setLayout(grid)

        self.setWindowIcon(QIcon('disc.ico'))

        self.display = QLineEdit()
        self.display.setFixedHeight(60)
        # self.display.setCursor(QCursor(QPixmap('cursor.png')))
        grid.addWidget(self.display, 0, 0, 1, 5)

        self.create_buttons(grid)

    def create_buttons(self, grid):
        """Creates the buttons for the calculator"""
        buttons = [
            '0', '1', '2', '3', '4',
            '5', '6', '7', '8', '9',
            '+', '-', '*', '/', '.',
            '(', ')', 'sqrt', 'sqr', 'x^',
            '=', 'HIST', 'DEL', 'C', 'OFF',
        ]

        button_positions = [(i, j) for i in range(1, 6) for j in range(5)]
        for button_position, button in zip(button_positions, buttons):
            actual_button = QPushButton(button)
            actual_button.clicked.connect(
                lambda checked, b=button: self.calculations.button_clicked(b)
                )

            grid.addWidget(actual_button, *button_position)
