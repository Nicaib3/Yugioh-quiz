from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []

question_list.append(Question('cual es el mounstro insignia de yugi?', 'mago oscuro', 'buster blader','kuriboh', 'mago del tiempo'))
question_list.append(Question('cual es el ataque de el dragon blanco de ojos azules?', '3000', '2500', '5000', '4500'))
question_list.append(Question('cual es el mejor personaje de yugioh?', 'joey wheeler', 'tae gardner', 'seto kaiba', 'yugi muto'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')

ans = QPushButton('Responder')
quest = QLabel('Qué nacionalidad no existe?')

RadioGroupBox = QGroupBox('Opciones de respuesta')
btn1 = QRadioButton('Pitufos')
btn2 = QRadioButton('Enets')
btn3 = QRadioButton('Chulyms')
btn4 = QRadioButton('Aleutas')

Layout1 = QHBoxLayout()
Layout2 = QVBoxLayout()
Layout3 = QVBoxLayout()

Layout2.addWidget(btn1)
Layout2.addWidget(btn2)
Layout3.addWidget(btn3)
Layout3.addWidget(btn4)
Layout1.addLayout(Layout2)
Layout1.addLayout(Layout3)

RadioGroupBox.setLayout(Layout1)

AnsGroupBox = QGroupBox('Resultado de la prueba')
result = QLabel('Es correcto o no')
correct = QLabel('Aqui esta la respuesta:')
AnsGroupBox.hide()

ans_layout = QVBoxLayout()
ans_layout.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignTop))
ans_layout.addWidget(correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(ans_layout)

LayoutH1 = QHBoxLayout()
LayoutH2 = QHBoxLayout()
LayoutH3 = QHBoxLayout()

LayoutH1.addWidget(quest, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
LayoutH2.addWidget(RadioGroupBox)
LayoutH2.addWidget(AnsGroupBox)
LayoutH3.addWidget(ans, stretch = 3)

Main_layout = QVBoxLayout()
Main_layout.addLayout(LayoutH1, stretch = 2)
Main_layout.addLayout(LayoutH2, stretch = 8)
Main_layout.addLayout(LayoutH3, stretch = 1)
Main_layout.setSpacing(5)

BtnnGroup = QButtonGroup()
BtnnGroup.addButton(btn1)
BtnnGroup.addButton(btn2)
BtnnGroup.addButton(btn3)
BtnnGroup.addButton(btn4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    ans.setText('Siguiente pregunta')

ans.clicked.connect(show_result)

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    ans.setText('Responder')
    BtnnGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    BtnnGroup.setExclusive(True)

ans.clicked.connect(show_question)

answers = [btn1, btn2, btn3, btn4]

def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    quest.setText(q.question)
    correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    result.setText(res)
    show_result()

def check_ans():
    if answers[0].isChecked():
        show_correct('Es correcto!')
    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            show_correct('Incorrecto...')

def next_question():
    window.cur_question = window.cur_question +1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if ans.text == 'Responder':
        check_ans()
    else:
        next_question()

window.setLayout(Main_layout)
window.cur_question = -1
ans.clicked.connect(click_OK)
next_question()
window.show()
app.exec_()