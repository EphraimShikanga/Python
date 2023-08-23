"""This module contains the calculations for the calculator"""

from math import sqrt


class CalculatorCalculations:
    """Calculations for the calculator"""
    def __init__(self, calculator_gui):
        self.calculator_gui = calculator_gui
        self.history = []

    def button_clicked(self, button):
        """What happens when a button is clicked"""
        if button == 'C':
            self.calculator_gui.display.clear()
        elif button == 'DEL':
            self.calculator_gui.display.backspace()
        elif button == 'OFF':
            self.calculator_gui.close()
        elif button == 'HIST':
            self.calculator_gui.display.setText(self.get_history())
        elif button == '=':
            try:
                result = str(eval(self.calculator_gui.display.text()))
                self.calculator_gui.display.setText(str(result))
                self.history.append(
                    f"{self.calculator_gui.display.text()} = {result}")
            except SyntaxError:
                self.calculator_gui.display.setText('Syntax Error')
        elif button == 'sqrt':
            try:
                result = sqrt(float(self.calculator_gui.display.text()))
                self.calculator_gui.display.setText(str(result))
                self.history.append(
                    f"sqrt({self.calculator_gui.display.text()}) = {result}")
            except ValueError:
                self.calculator_gui.display.setText('Math Error')
        elif button == 'sqr':
            try:
                result = float(self.calculator_gui.display.text()) ** 2
                self.calculator_gui.display.setText(str(result))
                self.history.append(
                    f"{self.calculator_gui.display.text()}^2 = {result}")
            except SyntaxError:
                self.calculator_gui.display.setText('Syntax Error')
        elif button == 'x^':
            self.calculator_gui.display.setText(
                self.calculator_gui.display.text() + '**')
        else:
            self.calculator_gui.display.setText(
                self.calculator_gui.display.text() + button)

    def get_history(self):
        """Returns the history of the calculator"""
        if self.history:
            for entry in self.history:
                return entry
        else:
            return 'No history yet'
