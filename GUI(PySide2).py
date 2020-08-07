from PySide2.QtWidgets import QApplication, QWidget, QDesktopWidget , QVBoxLayout, QPushButton , QGroupBox, QGridLayout, QLineEdit,QMessageBox
import sys
from PySide2.QtGui import QIcon, QFont, QIntValidator, QValidator, QDoubleValidator
import matplotlib.pyplot as plt
import math as m
class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plotting Functions")
        self.setGeometry(400,400,400,400)
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        self.setMaximumHeight(600)
        self.setMaximumWidth(800)
        self.equation_line_edit = QLineEdit()
        self.minimum_line_edit = QLineEdit()
        self.maximum_line_edit = QLineEdit()
        self.icon()
        self.centering_window()
        self.layout()
        vbox=QVBoxLayout()
        vbox.addWidget(self.group_message)
        self.setLayout(vbox)
    def icon(self):
        window_icon=QIcon("icon.png")  # object for QICon
        self.setWindowIcon(window_icon)  # Passing the QICon object to setWindowIcon to display it when running the code
    def centering_window(self):
        center=self.frameGeometry()
        center_point=QDesktopWidget().availableGeometry().center()
        center.moveCenter(center_point)
        self.move(center.topLeft())
    def layout(self):
        self.group_message= QGroupBox("Please fill the following spaces")  # Object for GroupBox
        self.group_message.setFont(QFont("Decorative", 14))
        grid_layout=QGridLayout()  #object for QGrid Layout
        button1 = QPushButton("Equation", self)
        grid_layout.addWidget(button1,0,0)  # Button1 is a widget which will be put in the 0 row and 0 column
        grid_layout.addWidget(self.equation_line_edit,0,1)
        button2=QPushButton("Minimum Values of x", self)
        grid_layout.addWidget(button2,1,0)
        #minimum_line_edit.setValidator(QDoubleValidator())                 #PyQt minimum_line_edit.setValidator(QIntValidator)
        grid_layout.addWidget(self.minimum_line_edit, 1, 1)
        button3 = QPushButton("Maximum vales of x", self)
        grid_layout.addWidget(button3,2,0)
        #maximum_line_edit.setValidator(QDoubleValidator())
        grid_layout.addWidget(self.maximum_line_edit,2,1)
        button4 = QPushButton("Setting Values", self)
        button4.clicked.connect(self.setting_values)
        grid_layout.addWidget(button4,3,0)
        button5 = QPushButton("PLot", self)
        button5.clicked.connect(self.message_box)
        grid_layout.addWidget(button5,3,1)
        self.group_message.setLayout(grid_layout)
    def setting_values(self):
        equation = self.equation_line_edit.text()
        mini = int(self.minimum_line_edit.text())
        maxi = int(self.maximum_line_edit.text())
    def equation_data(self):
        return self.equation_line_edit.text()
    def minimum_data(self):
        return int(self.minimum_line_edit.text())
    def maximum_data(self):
        return int(self.maximum_line_edit.text())
    def validations(self):
        equation = GUI.equation_data()
        global total_size_cap
        global array_of_plus
        global total_size_multipliers
        global wrong_sign
        global power
        global powers
        global coefficients
        global equal_sign
        global division
        global array_of_multipliers
        global total_size_multipliers
        list_of_coefficients=[]
        division=0
        array_index_absolute_values=[]
        array1=[]
        array2=[]
        q = 0
        m = 0
        sign=0
        array_of_multipliers = []
        equal_sign = 0
        total_size_multipliers = 0
        total_size_cap = 0
        array_of_caps = []
        array_of_plus = []
        coefficients = []
        array_of_coefficients = []
        array_absolute_values = []
        total_cap = 0
        extra_sign = 0
        power = 0
        powers = []
        num_of_multipliers = 0
        wrong_sign = 0
        list_of_strings = []
        for i in range(len(equation)):
            u = i
            if (equation[i] == '*' or equation[i] == '/') and equation[i+1]=='x':
                t = 0
                while t < u:
                    array_absolute_values.append(equation[t])
                    t += 1
                    if equation[t] == '+' or equation[t] == '-':
                        if equation[t - 1] == '^':
                            # as if the power has a sign +ve or negative i will not take that sign into consideration
                            continue
                        array_index_absolute_values.append(equation.index(array_absolute_values[len(array_absolute_values) - 1]))
                        # As if there is any absolute value in the middle term, before '*' or '/' sign there will be 2 plus sign if i assign the index of each one into list and make while loop i will append the value between two plus sign and this will be the coefficient
                        del array_absolute_values[:]
                        n = array_index_absolute_values[len(array_index_absolute_values) - 2] + 1
                        b = array_index_absolute_values[len(array_index_absolute_values) - 1] + 1
                        # i added 1 to n and b as i check for equation of t after adding 1 to (t) so if the equation is 3*x^2+5+4*x, i will get the index of 2 and 5 but i want the index of '+' sign so i added 1
                        while n < b:
                            array_absolute_values.append(equation[n])
                            # adding the values between the two plus signs to lis then adding it as string and at the end converting it into float
                            n += 1
                            if equation[n] == 'x':
                                del array_absolute_values[:]
                                break
                        summation_absolute_values = ''
                        for s in range(len(array_absolute_values)):
                            summation_absolute_values = summation_absolute_values + array_absolute_values[s]
                        if summation_absolute_values == '':
                            continue
                        del array_absolute_values[:]
                        coefficients.append(summation_absolute_values)
                        total_cap=+1           # To add 1 cap as i compare number of caps to number of pluses
                array_of_multipliers.append(equation[i])
                last_slash = 0
                sign = 0
                r = 0
                number_of_slash = 0
                while r < u:
                    if last_slash == 1:
                        break
                    list_of_coefficients.append(equation[r])
                    r += 1
                    if equation[i - r] == '/' and equation[i - r + 1] != 'x':
                        sign += 1  # indicates that what before '*' or '/' was assigned as coefficient to coefficients and prevent taking what before '*' as coefficient again
                        del list_of_coefficients[:]
                        v = 0
                        # number_of_slash+=1
                        while v < i - r:
                            list_of_coefficients.append(equation[v])  # as if there is fraction before multiplier or divider i will take the value before '/' sign and put it into array and then take the float of this array
                            v += 1
                            if equation[v] == '+' or equation[v] == '-':
                                del list_of_coefficients[:]  # as if the fraction came in any term '/' sign will have '+' or '-' before it so i delete all the values before '+' or '-'
                        last_slash += 1  # as the last slash will be came first as i check for i-r not r and if there is more than 1 one slash, i want the last one only
                        array_before_sign = ''
                        for g in range(len(list_of_coefficients)):
                            array_before_sign = array_before_sign + list_of_coefficients[g]
                        if array_before_sign == '':
                            continue
                        array1.append(float(array_before_sign))
                        del list_of_coefficients[:]
                        index = equation.index(equation[i - r])
                        while index < i:
                            list_of_coefficients.append(equation[index])  # as equation.index(equation[i-r]) will give me the index of '/' sign then adding what after it into array and converting it into float
                            index += 1
                            if equation[index] == '/':
                                del list_of_coefficients[:]

                        list_of_coefficients.pop(0)  # as the first element will be '/' sign
                        array_after_sign = ''
                        for k in range(len(list_of_coefficients)):
                            array_after_sign = array_after_sign + list_of_coefficients[k]
                        j = 0
                        while j < i:
                            if equation[j] == '/' and equation[j + 1] != 'x':
                                number_of_slash += 1
                            j += 1
                        if number_of_slash == len(array_of_multipliers):
                            array2.append(float(array_after_sign))
                        elif number_of_slash == len(array_of_multipliers) - 1:
                            sign = 0
                            continue
                        del list_of_coefficients[:]
                        coefficients.append(str(array1[0] / array2[0]))
                        del array1[:]
                        del array2[:]

                p = 0
                while p < u:
                    array_of_coefficients.append(equation[p])
                    p += 1
                    if equation[p] == '+' or equation[
                        p] == '-':  # to remove the elements before '+' or '-' as the second term coefficient will be lied betweem '+' and '*'
                        del array_of_coefficients[:]
                summation_of_coefficients = ''
                for o in range(len(array_of_coefficients)):
                    summation_of_coefficients = summation_of_coefficients + array_of_coefficients[o]
                del array_of_coefficients[:]
                if sign != 0:
                    continue
                else:
                    coefficients.append(summation_of_coefficients)
            #if equation[i]== '/' and equation[i+1] != 'x':
                #extra_sign+=1
            if equation[i] == '^':
                array_of_caps.append(equation[i])
                if equation[i - 1] == equation[0]:  # input: x^2+..
                    num_of_multipliers += 1  # as i plot by comparing number of multipliers and caps to number of plus
                    coefficients.append('1')
                elif equation[i - 2] == equation[0]:  # input: -x^2+..
                    num_of_multipliers += 1
                    coefficients.append('-1')
                elif equation[i - 3] == '/':  # input: 5/2x^2+..
                    extra_sign += 1
            if equation[i] == '\\':  # input: 5\2*x^2+..
                wrong_sign += 1
            if equation[i] == '+' or equation[i] == '-':
                if equation[i] == equation[0]:
                    continue
                array_of_plus.append(equation[i])
                p = 0
                while p < u:
                    list_of_strings.append(equation[p])
                    p += 1
                    if equation[i - 1] == 'x':  # in case of the input is 4*x^2+3*x+5 or 4*x^2+x+5
                        m = m - 1
                        del list_of_strings[:]
                        list_of_strings.append('1')
                        continue
                    if (equation[p + 1] == '+' or equation[p + 1] == '-') and equation[p] == '^':
                        m = m - 1
                        # as if the power is +ve or negative i neglect that sign in my calculation
                        # continue
                    if equation[p + 1] == '+' or equation[p + 1] == '-':
                        m += 1
                    if equation[p] == '^':
                        m = m - 1
                        q += 1
                        del list_of_strings[:]
                        continue
                    if equation[p] == equation[0] == '+' or equation[p] == equation[0] == '-':
                        m = m - 1
                    if equation[p] == 'x' and (equation[p + 1] == '+' or equation[p + 1] == '-') and equation[i] != '+':
                        m = m - 1
                if q >= 1:
                    list_of_strings.pop(0)
                if m > 0:  # as if there is absolute value between two terms the power of that term should be equal zero, m=2 for 2 plus sign and m=1 for 1 cap so the power of that term = 0
                    del list_of_strings[:]
                    list_of_strings.append('0')
                summation_of_powers = ''
                for w in range(len(list_of_strings)):
                    summation_of_powers = summation_of_powers + list_of_strings[w]
                del list_of_strings[:]
                powers.append(summation_of_powers)
                q = 0
                m = 0
                if equation[i-1] == equation[0] == 'x':              # input: x+..
                    num_of_multipliers+=1
                    total_cap+=1
                    coefficients.append('1')
                elif equation[i - 2] == equation[0]=='x':  # input: -x+..
                    num_of_multipliers+=1
                    total_cap+=1
                    coefficients.append('-1')
                elif equation[i - 2] == '+' and equation[i - 1] == 'x':  # input: +x+...
                    num_of_multipliers += 1
                    total_cap += 1
                    coefficients.append('1')
                elif equation[i - 2] == '-' and equation[i - 1] == 'x':  # input: -x+
                    num_of_multipliers += 1
                    total_cap += 1
                    coefficients.append('-1')
                elif equation[i - 2] == '*' or equation[i - 2] == '/':  # input: +3*x+..
                    total_cap += 1
                elif equation[i - 3] == '+' or equation[i - 3] == '-':  # input: +3x+
                    total_cap += 1
            if equation[i] == '=':
                equal_sign += 1
        n = 1
        while n < len(equation):
            array_of_coefficients.append(equation[len(equation) - n])
            list_of_strings.append(equation[len(equation) - n])  # as if the last term is x^2 i take 2 as power of last term
            n += 1
            if equation[len(equation)-n] == '=':
                break
            if equation[len(equation) - n] == '^':  # in case the input is in the form of: 5*x^5+4*x+5*x^0
                list_of_strings.reverse()
                summation_power_last_term = ''
                for w in range(len(list_of_strings)):
                    summation_power_last_term = summation_power_last_term + list_of_strings[w]
                del list_of_strings[:]
                powers.append(summation_power_last_term)
                # total_cap=total_cap-1
                del array_of_coefficients[:]
                break
            if equation[len(equation) - n] == '*' or equation[len(equation) - n] == '/':  # in case the input is in the form of: 5*x^2+4*x
                # extra_sign+=1
                powers.append('1')
                del array_of_coefficients[:]
                break
            if equation[len(equation) - n] == '+' or equation[len(equation) - n] == '-':  # to get the coefficients of last term: 5*x^2+4*x(+10.3)
                array_of_coefficients.append(equation[len(equation) - n])
                array_of_coefficients.reverse()  # as the list will be reversed; e.g. ['0' , '1' , '+' ] as the last element will be put first so i reversed it in order to manage to add elements
                summation_last_term = ''
                for e in range(len(array_of_coefficients)):
                    summation_last_term = summation_last_term + array_of_coefficients[e]
                del array_of_coefficients[:]
                # summation_last_term
                coefficients.append(summation_last_term)
                if equation[len(equation)-(n+1)] == '^':           #  in case of the input is 3*x+4+5*x^-2, don't take the coefficient if equation[len(equation) - (n+1) ] == '^'
                    coefficients.pop()
                    list_of_strings.append(equation[len(equation)-n]) # to take a sign with the power
                    list_of_strings.reverse()
                    summation_power_last_term = ''
                    for w in range(len(list_of_strings)):
                        summation_power_last_term = summation_power_last_term + list_of_strings[w]
                    del list_of_strings[:]
                    powers.append(summation_power_last_term)
                break


        if equation[len(equation) - 2] == equation[1] == '^':  # input: x^2
            total_cap = total_cap - 1
            # coefficients.append('1')
        if equation[len(equation) - 2] == equation[2] == '^':  # input: -x^2
            total_cap = total_cap - 1
            # coefficients.append('-1')
        total_size_multipliers = len(array_of_multipliers) + num_of_multipliers - extra_sign - wrong_sign
        total_size_cap = len(array_of_caps) + total_cap
        # if equation[len(equation) - 2] == '^' and (equation[len(equation) - 4] == '*' or equation[len(equation) - 4] == '/'):  # input: 5*x^2+3*x+4*x^0
        # total_size_multipliers = total_size_multipliers - 1

    def plot(self):
        GUI.validations()
        global complex_value
        complex_value=0
        global y
        global sum_of_coefficients
        global x
        y = []
        sum_of_coefficients = []
        mini = GUI.minimum_data()
        maxi = GUI.maximum_data()
        x = list(range(mini, maxi + 1))
        q = 0
        multipliers=array_of_multipliers
        if len(coefficients) > len(multipliers):
            difference= len(coefficients)-len(multipliers)
            c=0
            while c < difference:
                multipliers.append("")
                c+=1
        # as i will check for array_of_multipliers[i] and inrease it by 1 like j but array of coefficients is more 1 element than array_of_multipliers, so if i dont't add one element to that array i will exceed the index
        while q < len(x):
            j = 0
            i = 0
            # b = list_of_strings
            b = powers
            if len(coefficients) > len(b):  # to make list_of_strings of the same length of coefficients, so if the difference between them is one so zero is added to list_of_strings
                difference_of_lengths = len(coefficients) - len(b)
                k = 0
                while k < difference_of_lengths:
                    b.extend('0')
                    k += 1
            while j < len(coefficients):
                if multipliers[i] == '/':
                    y.append(float(coefficients[j]) / x[q] ** float(b[j]))
                else:
                    y.append(float(coefficients[j]) * x[q] ** float(b[j]))
                i += 1
                j += 1
            summation = 0
            for u in range(len(y)):
                summation = summation + y[u]
            del y[:]
            sum_of_coefficients.append(summation)
            q = q + 1
        #array_of_multipliers.pop() # to erase the addedd element to the list
    def message_box(self):
        GUI.validations()
        GUI.plot()
        if equal_sign != 0:
            QMessageBox.warning(self, "Warning", "You Can't use equal sign, The equation should be in that form: 5*x^2+3*x+5")
        if wrong_sign != 0:
            QMessageBox.warning(self,"Warning", "You have to use '/' as a division sign")
        if total_size_cap < len(array_of_plus):
            QMessageBox.warning(self,"Warning", "You have to use '^' as a power sign")
        if total_size_multipliers < len(array_of_plus):
            QMessageBox.warning(self, "Warning", "You have to write '*' or '/'; e.g. 5*x^2")
        if total_size_cap == len(array_of_plus) and total_size_multipliers == len(array_of_plus) and wrong_sign == 0 and equal_sign==0 :
            plt.plot(x, sum_of_coefficients, label='Quadratic')
            plt.show()
QApplication_object=QApplication([])
GUI=GUI()
GUI.show()
QApplication_object.exec_()
sys.exit()