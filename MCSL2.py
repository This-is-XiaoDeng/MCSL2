from os import environ
from platform import system
from sys import argv as SystemArgv
from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtWidgets import QApplication
from MCSL2Lib.initProgram import initializeMCSL2
from qfluentwidgets import FluentTranslator
from MCSL2Lib.windowInterface import Window

if __name__ == '__main__':

    # 初始化
    initializeMCSL2()

    # 高DPI适配
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

    # 适配Linux特殊情况
    if system().lower() == 'linux':
        try:
            if environ["XDG_SESSION_TYPE"].lower() != 'x11':
                environ["QT_QPA_PLATFORM"] = "wayland"
            else:
                pass
        except:
            pass
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "auto"

    # 启动
    app = QApplication(SystemArgv)
    translator = FluentTranslator(QLocale())
    app.installTranslator(translator)
    w = Window()
    w.show()
    app.exec_()
