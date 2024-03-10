from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QMainWindow
from qt3 import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl


class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()
        self.ui.select.setText('Вибрати музику')
        self.ui.play.setText('Грати')
        self.ui.stop.setText('Зупинити')
        self.ui.play.clicked.connect(self.play_music)
        self.ui.select.clicked.connect(self.select_music)
        self.ui.stop.clicked.connect(self.stop_music)
        self.ui.volume.valueChanged.connect(self.set_volume)
    def select_music(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select Audio File', "", "Audio Files(*.mp3 *.wav)")
        if file:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
            self.player.play()
            self.player.setVolume(0)
    def play_music(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def stop_music(self):
        self.player.stop()
    def set_volume(self, value):
        self.player.setVolume(value)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()