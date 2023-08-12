from widgets import *
import sys
import os
import getpass
from typing import List, Any

USERNAME = getpass.getuser()


def get_path():
    try:
        a = sys.argv[1]
    except IndexError:
        a = None
    if a is None:
        try:
            with open(f"C:/Users/{USERNAME}/AppData/Local/Temp/python_notepad.tmp", "rt") as fo:
                paths = fo.read()
                fo.close()
        except FileNotFoundError:
            with open(f"C:/Users/{USERNAME}/AppData/Local/Temp/python_notepad.tmp", "wt") as fo:
                paths = ""
                fo.close()
        if not (os.path.isfile(paths)):
            paths = ""
    else:
        paths = a
    nams = os.path.basename(paths)
    if nams == "" or nams is None:
        nams = "无标题"
    return paths


class MainWindow(QMainWindow):
    """docstring for MainWindow"""
    text: list[Any]

    def __init__(self):
        super().__init__()
        self.resize(1300, 700)
        self.setWindowIcon(QIcon(".//icon//notepad.ico"))
        self.setWindowTitle("python记事本")
        with open("style.qss") as fo:
            self.setStyleSheet(fo.read())
        self.note = QTabWidget(self)
        self.note.setFont(FONT)
        self.note.resize(950, 600)
        self.note.move(150, 0)
        self.text = []
        get = get_path()
        self.paths = [get]
        self.start()
        self.show()

    def resizeEvent(self, *args, **kwargs):
        super().resizeEvent(*args, **kwargs)
        self.note.resize(self.width()-150, self.height())
        for i in self.text:
            i:TextEdit
            i.resize(self.note.width(),self.note.height())


    def start(self):
        if os.path.isfile(self.paths[0]):
            try:
                with open(self.paths[0], 'rt', encoding='ANSI') as fo:
                    read = fo.read()
            except UnicodeError:
                try:
                    with open(self.paths[0], 'rt', encoding='utf-8') as fo:
                        read = fo.read()
                except UnicodeError:
                    read = ''
        else:
            read = ''
        text = TextEdit(self)
        text.resize(self.note.width(), self.note.height())
        text.append(read)
        text.text.setFont(FONT)
        self.note.addTab(text, os.path.basename(self.paths[0]))
        self.text.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
