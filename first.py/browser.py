#this BROWSER is LICENSED TO Prakhar
#Do not try to copy the code
#HAVE A GOOD DAY

import subprocess
from subprocess import call
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import  filedialog
from PyQt5.QtCore import*
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import*
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtPrintSupport import *
import sys
import atexit
from selenium import webdriver

class AboutDialog(QDialog):

    def __init__(self, *args, **kwargs):

        super(AboutDialog, self).__init__(*args, **kwargs)

        Qbtn = QDialogButtonBox.Ok                                                                          #No cancel
        self.buttonbox = QDialogButtonBox(Qbtn)
        self.buttonbox.accepted.connect(self.accept)
        self.buttonbox.rejected.connect(self.reject)

        layout = QVBoxLayout()


        title = QLabel("Prakhar Browser")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap('download.jpg'))
        logo.setAlignment(Qt.AlignHCenter)
        layout.addWidget(logo)

        n1 = QLabel("Version 1.2.2.0")
        n1.setAlignment(Qt.AlignHCenter)
        layout.addWidget(n1)

        n2 = QLabel("Copyright 2017 Prakhar Inc.")
        n2.setAlignment(Qt.AlignHCenter)
        layout.addWidget(n2)

        layout.addWidget(self.buttonbox)

        self.setLayout(layout)

class MainWindow(QMainWindow):

         def __init__(self, *args, **kwargs):

             super(MainWindow, self).__init__(*args, **kwargs)
             self.show()

             self.setWindowTitle("Prakhar")                                                                #window tiltle
             self.setWindowIcon(QIcon('download.jpg'))                                                  #Window Icon
             self.height = 1000
             self.width = 1000
             self.top = 50
             self.left = 50
             self.statusMessage = "Quote of the day      :     Love is not to be Purchased, And Affection has No Price"
             self.setGeometry(self.top,self.left,self.width,self.height)
             self.statusBar().showMessage(self.statusMessage)
             self.browser = QWebView()

             """Tabs Coding Is From Here"""

             self.tabs = QTabWidget()
             self.tabs.setDocumentMode(True)
             self.tabs.tabBarDoubleClicked.connect(self.tab_open_double_click)
             self.tabs.currentChanged.connect(self.current_tabChanged)
             self.add_new_tab(QUrl("https://www.google.com"),'Hometab')                                  #home page google
             self.tabs.setTabsClosable(True)
             self.tabs.tabCloseRequested.connect(self.close_current_tab)
             self.setCentralWidget(self.tabs)

             """Till Here"""

             QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True);             #Plugins Enabled

             nav = QToolBar("Navigation")                                                               #Navigation Tab
             nav.setIconSize(QSize(16,16))
             self.addToolBar(nav)

             back_btn = QAction(QIcon("left.ico"),"back",self)                                          #Back Button
             back_btn.setStatusTip("Previous Page")
             back_btn.triggered.connect(lambda :self.tabs.currentWidget().back())
             nav.addAction(back_btn)

             for_btn = QAction(QIcon("right.ico"),"front",self)                                         #Forward Button
             for_btn.setStatusTip("Next Page")
             for_btn.triggered.connect(lambda :self.tabs.currentWidget().forward())
             nav.addAction(for_btn)

             reload_btn = QAction(QIcon("restart.ico"),"Restart",self)                                  #Reload Button
             reload_btn.setStatusTip("Restart Loading")
             reload_btn.triggered.connect(lambda :self.tabs.currentWidget().reload())
             nav.addAction(reload_btn)

             home_btn = QAction(QIcon("home.ico"), "Home", self)                                        #Home Button
             home_btn.setStatusTip("Take Me to the Home Page")
             home_btn.triggered.connect(self.navigate_home)
             nav.addAction(home_btn)

             nav.addSeparator()

             self.httpsicon = QLabel()                                                                #Security Lock
             self.httpsicon.setPixmap(QPixmap('unlock.png'))
             nav.addWidget(self.httpsicon)

             self.urlbar = QLineEdit()                                                                #editing of Url in navigation Tab
             self.urlbar.returnPressed.connect(self.navigate_to_url)
             nav.addWidget(self.urlbar)

             stop_btn = QAction(QIcon("stop.ico"),"Stop",self)                                       #Stop Loading Button
             stop_btn.setStatusTip("Stop Loading")
             stop_btn.triggered.connect(lambda :self.tabs.currentWidget().stop())
             nav.addAction(stop_btn)

             self.menuBar().setNativeMenuBar(False)
             bar_menu = self.menuBar()
             file_menu = self.menuBar().addMenu(QIcon('filemenu.ico'),"&File")
             #graph = self.menuBar().addMenu("&Graphs")

             new_tab_action = QAction("New Tab",self)                                              #Print /menu
             new_tab_action.setStatusTip("Opens a New Page")
             new_tab_action.triggered.connect(lambda x : self.add_new_tab())
             file_menu.addAction(new_tab_action)

             self.menuBar().setNativeMenuBar(False)
             bar_menu = self.menuBar()
             file_menu = self.menuBar().addMenu(QIcon('game.ico'), "&Games")

             #threeD = QAction("3-Dimentional",self)
             #threeD.setStatusTip("Makes A 3-D Graph of the File you provide")
             #threeD.triggered.connect(self.graph)
             #graph.addAction(threeD)

             print_action = QAction("Print_Page",self)                                              #Print /menu
             print_action.setStatusTip("Print This Page")
             print_action.triggered.connect(self.print_page)
             bar_menu.addAction(print_action)

             open_action = QAction("Open_File", self)                                                  #OPEN MENU
             open_action.setStatusTip("Open A File")
             open_action.triggered.connect(self.open_file)
             bar_menu.addAction(open_action)

             save_action = QAction("Save_As", self)                                                      #Save MEnu
             save_action.setStatusTip("Save This Page")
             save_action.triggered.connect(self.save_file)
             bar_menu.addAction(save_action)

             about_action = QAction("About_Prakhar_Browser", self)                                           #About About Us
             about_action.setStatusTip("Know More About Prakhar")
             about_action.triggered.connect(self.about)
             bar_menu.addAction(about_action)

             navigate_pasha_action = QAction("Prakhar's_Home_Page", self)                                   #About Prakhar home page
             navigate_pasha_action.setStatusTip("Go To Prakhar's Home Page")
             navigate_pasha_action.triggered.connect(self.navigatePasha)
             bar_menu.addAction(navigate_pasha_action)

             game_action = QAction("Snake Game", self)                                                      #Game
             game_action.setStatusTip("snakess all Around")
             game_action.triggered.connect(self.game)
             file_menu.addAction(game_action)

             air_action = QAction("Air Hockey", self)                                                      #Game
             air_action.setStatusTip("It's Hockey")
             air_action.triggered.connect(self.air)
             file_menu.addAction(air_action)

             calc_action = QAction("Prakhar Calculator", self)                                                      #Game
             calc_action.setStatusTip("Calculating")
             calc_action.triggered.connect(self.calculate)
             bar_menu.addAction(calc_action)

         def close_current_tab(self, i):

             if self.tabs.count()<2:
                 return

             self.tabs.removeTab(i)

         def current_tabChanged(self, i):

             qurl = self.tabs.currentWidget().url()
             self.update_urlbar(qurl, self.tabs.currentWidget())

         def tab_open_double_click(self, i):

             if i == -1:                                                                                 #NO tab Under the Click
                 self.add_new_tab()

         def add_new_tab(self,qurl = None,label = "Blank"):

             if qurl == None :
                 qurl = QUrl('http://localhost:5000/')
             browser = QWebView()
             browser.setUrl(qurl)

             i = self.tabs.addTab(browser,label)

             self.tabs.setCurrentIndex(i)

             #We will only update the url when it is of the current page only
             #Else we will not

             browser.urlChanged.connect(lambda qurl, browser = browser:
                                        self.update_urlbar(qurl,browser))

             browser.loadFinished.connect(lambda _, i = i, browser = browser:
                                          self.tabs.setTabText(i, browser.page().mainFrame().title()))

         def print_page(self):                                                                         #Print Page

             dlg = QPrintPreviewDialog()
             dlg.paintRequested.connect(self.browser.print_)
             dlg.exec_()

         def open_file(self):                                                                          #Open File Menu Bar

             filename = QFileDialog.getOpenFileName(self,"Open File","",
                            "Hypertext Markup Language (*.htm *.html);;"
                                                    "All files (*.*)")

             if filename:
                 with open(filename,"r") as f:
                     html = f.read()

                 self.tabs.currentWidget().setHtml(html)
                 self.urlbar.setText(filename)

         def save_file(self):                                                                           #save File Menu Bar
             filename = QFileDialog.getSaveFileName(self,"Save Page As","",
                                                    "Hypertext Markup Language (*.htm *.html);;"
                                                                                   "All files (*.*)")

             if filename:
                 html = self.browser.page().mainFrame().toHtml()
                 with open(filename,"w") as f:
                     f.write(html.encode('utf8'))


         def navigate_home(self):

             self.tabs.currentWidget().setUrl(QUrl("https://www.google.com"))

         def navigate_to_url(self):

             q = QUrl(set.urlbar.text())
             if q.scheme == "":
                 q.setScheme("http")
                 self.tabs.currentWidget().setUrl(q)

         def update_urlbar(self, q, browser = None):

            if browser != self.tabs.currentWidget():

                 # If Signal is not from the current tab ignore
                 return

            if q.scheme == "https":
                 self.httpsicon.setPixmap(QPixmap('lock.png'))
            else:
                 self.httpsicon.setPixmap(QPixmap('unlock.png'))

            self.urlbar.setText(q.toString())
            self.urlbar.setCursorPosition(0)

         def navigatePasha(self):

             self.tabs.currentWidget().setUrl(QUrl("https://futuresahead.blogspot.com"))

         def about(self):
             dlg = AboutDialog()
             dlg.exec_()

         def game(self):
             try:
                 #os.system('l' + ' &')
                 #l.main()
                 subprocess.Popen(['python', 'game.py'])
                 #subprocess.call('python l.py',shell=True)

             except sys.exit(0):
                 print("sys.exit was called but I'm proceeding anyway")
                 print("so I'll print this, etc, etc")

         def air(self):

             try:
                 #os.system('l' + ' &')
                 #l.main()
                 subprocess.Popen(['python', 'airhoc.py'])
                 #subprocess.call('python l.py',shell=True)

             except sys.exit(0):
                 print("sys.exit was called but I'm proceeding anyway")
                 print("so I'll print this, etc, etc")

         def calculate(self):

             subprocess.Popen(['python', 'calc.py'])

         def graph(self):
             '''fname = filedialog.askopenfilename(filetypes=(("Template files", "*.tplate"),
                                                           ("HTML files", "*.html;*.htm"),
                                                           ("All files", "*.*")))'''
             text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')

             if ok:
                df = pd.read_csv(text, index_col=0)
                plt.style.use('ggplot')
                ms = df.G3

                df1 = df[['G3', 'G2', 'G1']]
                ms.plot.hist(title='Histogram', alpha=0.5)
                df1.plot.hist(alpha=0.5)
                df.plot.scatter(x='G1', y='G3')
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.set_xlabel('Final Grade')
                ax.set_ylabel('First Grade')
                ax.set_zlabel('Daily Alcohol')
                ax.scatter(df.G1, df.G3, df['Dalc'], c='r', marker='o')
                plt.show()

app = QApplication(sys.argv)
app.setApplicationName("PrakharBrowser")
#app.setOrganiationName("Prakhar")
app.setOrganizationDomain("Prakhar.org")
window = MainWindow()
window.show()
app.exec()