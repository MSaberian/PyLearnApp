import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        self.read_from_database()
        
        self.ui.btn_newtask.clicked.connect(self.new_task)

    def new_task(self):
        new_title = self.ui.tb_new_task_title.text()
        new_description = self.ui.tb_new_task_description.toPlainText()
        feedback = self.db.add_new_task(new_title, new_description)
        self.ui.tb_new_task_title.clear()
        self.ui.tb_new_task_description.clear()

        if feedback == True:
            self.read_from_database()

        else:
            msg_box = QMessageBox()
            msg_box.setText("you have problem")
            msg_box.exec()

    def done_tasks(self, id, checked):
        self.db.done_task(id, checked)
            
    def remove_task(self,index,id):
        # self.ui.remove_task(id)
        # self.ui.gl_tasks.
        children = []
        for i in range(self.ui.gl_tasks.count()):
            child = self.ui.gl_tasks.itemAt(i).widget()
            if child:
                children.append(child)
        for child in children:
            # child.deleteLater()
            print(child)

    def read_from_database(self):
        tasks = self.db.get_tasks()

        for i in range(len(tasks)):
            # count = self.scrollAreaWidgetLayout.count() - 1
            # groupBox = QtWidgets.QGroupBox('GroupBox ' + str(count), self.scrollAreaWidget)
            # self.scrollAreaWidgetLayout.insertWidget(count, groupBox)
            new_checkbox = QCheckBox()
            new_label = QLabel()
            new_btn = QPushButton()
            new_label.setText(tasks[i][2])
            new_checkbox.setText(tasks[i][1])
            new_btn.setText('❌')
            new_checkbox.setChecked(tasks[i][3])
            
            self.ui.gl_tasks.addWidget(new_checkbox, i, 0)
            self.ui.gl_tasks.addWidget(new_label, i, 1)
            self.ui.gl_tasks.addWidget(new_btn, i, 2)

            new_checkbox.toggled.connect(partial(self.done_tasks,tasks[i][0]))
            new_btn.clicked.connect(partial(self.remove_task,i,tasks[i][0]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
