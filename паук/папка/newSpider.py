import uiautomation as auto
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSplitter, QTextEdit, QTreeView, QVBoxLayout,
    QWidget)

# import pythoncom
# #button.clicked.connect(self.the_button_was_clicked)
# pythoncom.CoInitializeEx(0)  
class Spyder(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()       
        self.ui.setupUi(self)  
        self.show()
    def keyPressEvent(self, event):       
        key=event.key()
        if (key==82):
            self.ui.serchFunction()    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
       
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 760)
        MainWindow.setMaximumSize(QSize(960, 760))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 961, 761))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(127, 127, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(63, 63, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(0, 0, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(0, 0, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 127))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 127, 127))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
        self.splitter.setPalette(palette)
        self.splitter.setOrientation(Qt.Horizontal)
        self.gridLayoutWidget = QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeView = QTreeView(self.gridLayoutWidget)
        self.treeView.setObjectName(u"treeView")        
        self.treeView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.treeView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  
       

        self.verticalLayout.addWidget(self.treeView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.splitter.addWidget(self.gridLayoutWidget)
        self.gridLayoutWidget_3 = QWidget(self.splitter)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label = QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton_5 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.label_2 = QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pushButton_6 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.textEdit = QTextEdit(self.gridLayoutWidget_3)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(0, 10))
        self.textEdit.setMaximumSize(QSize(16777215, 30))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.pushButton_7 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.textEdit_2 = QTextEdit(self.gridLayoutWidget_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_2.addWidget(self.textEdit_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.gridLayoutWidget_3)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    # переменные и методы
        self.element=""
        self.nodes = {}
        #self.bind('<Control-r>', self.serchFunction)
        #self.treeView.bind("<ButtonRelease-1>", self.open_node)
        self.model = QStandardItemModel()
        self.treeView.setModel(self.model) 
        self.treeView.selectionModel().selectionChanged.connect(self.open_node)
        self.pushButton_4.clicked.connect(self.buttonGetMetodsFunction)
        self.pushButton_5.clicked.connect(self.buttonGetMetodsTwoFunction)
        self.pushButton_8.clicked.connect(self.clickFunction)
        self.pushButton_7.clicked.connect(self.invokeMetod)
        self.pushButton_6.clicked.connect(self.setTextMetod)
    def buttonGetMetodsFunction(self):
        #30045
        try:
            self.label.clear()
            self.label.setText(self.element.GetPropertyValue(30005))    
        except:
            self.label.clear()
            self.label.setText("Ошибка")    
    def buttonGetMetodsTwoFunction(self):
        #30045 label_2
        try:
            self.label_2.clear()
            self.label_2.setText(self.element.GetPropertyValue(30045))    
        except:
            self.label_2.clear()
            self.label_2.setText("Ошибка") 
    def clickFunction(self):         
        if self.element.Exists(): #проверка что элемент сущесвует
            try:            
                iEnable=self.element.GetPropertyValue(30010) #проверка что элемент активен
            except:
                auto.MessageBox("Ошибка выполнения","Внимание",0)  
            if iEnable:               
                self.element.Click()
    def invokeMetod(self):
        if self.element.Exists(): #проверка что элемент сущесвует
            try:            
                iEnable=self.element.GetPropertyValue(30010) #проверка что элемент активен
                if iEnable:               
                    self.element.GetInvokePattern().Invoke()
            except:
                auto.MessageBox("Ошибка выполнения","Внимание",0) 
            
    def setTextMetod(self):
        if self.element.Exists(): #проверка что элемент сущесвует
            try:            
                iEnable=self.element.GetPropertyValue(30010) #проверка что элемент активен
                if iEnable:  
                    print(self.textEdit.toPlainText())  
                    self.element.GetValuePattern().SetValue(self.textEdit.toPlainText())  
            except:
                auto.MessageBox("Ошибка выполнения","Внимание",0)              
    def open_node(self, selected):
        indexes = selected.indexes()
        if indexes:
            index = indexes[0]
            item = self.model.itemFromIndex(index)
            #selected_item = item.text()
            control = self.nodes[str(item)]
            self.element=control  
            print(self.element.GetPropertyValue(30003)) 
           
            self.textEdit_2.clear()
            self.textEdit_2.append("Свойства элемента")
            self.textEdit_2.append("```````````````````````````")
            self.textEdit_2.append(f"{control}")
            self.textEdit_2.append(f"GetPropertyValue")
            for k, v in auto.PropertyIdNames.items():
                value = control.GetPropertyValue(k)
                self.textEdit_2.append(f"{k}  {v}={value}, {type(value)}") 
            self.rowsSearh="```````````````код доступа````````````````\n"
            
            lists = []
            while control:
                lists.insert(0, control)
                control = control.GetParentControl()                
            self.rowsSearh="```````````````код доступа````````````````\n"
            lastControl=""
            for i, control in enumerate(lists): 
                print(i)
                lastControl=str(auto.ControlTypeNames[control.GetPropertyValue(30003)])
                if i>0: 
                    depth=  auto.LogControlNewdepth(control, i, False, False)  
                    if i==1:                       
                        self.rowsSearh  = self.rowsSearh + f"element{i}=auto.WindowControl(searchDepth={depth}, ClassName='{control.GetPropertyValue(30012)}', Name='{control.GetPropertyValue(30005)}')\nelement{i}.SetActive()\n"
                    elif i>1:
                        self.rowsSearh  = self.rowsSearh + f"element{i}=element{i-1}.{auto.ControlTypeNames[control.GetPropertyValue(30003)]}(ClassName='{control.GetPropertyValue(30012)}', Name='{control.GetPropertyValue(30005)}', AutomationId='{control.GetPropertyValue(30011)}')\n"
            self.textEdit_2.append(self.rowsSearh)
            if lastControl=="EditControl":
                self.textEdit_2.append(f"element{len(lists)-1}.GetValuePattern().SetValue('Ваш текст')")
            elif lastControl=="ButtonControl":
                self.textEdit_2.append(f"element{len(lists)-1}.GetInvokePattern().Invoke()")
    def serchFunction(self):         
        self.textEdit_2.clear()
        root = False
        focus = False
        cursor = False
        ancestor = True
        foreground = False
        showAllName = False
        depth = 0xFFFFFFFF
        showPid = False    
        auto.GetCursorPos()
        control = None
        if root:
            control = auto.GetRootControl()
        if focus:
            control = auto.GetFocusedControl()
        if cursor:
            control = auto.ControlFromCursor()
            if depth < 0:
                while depth < 0 and control:
                    control = control.GetParentControl()
                    depth += 1
                depth = 0xFFFFFFFF
        if ancestor:
            control = auto.ControlFromCursor()
            
            if control:
                lists = []
                while control:
                    lists.insert(0, control)
                    control = control.GetParentControl()
                    
                self.rowsSearh="```````````````код доступа````````````````\n"
                for i, control in enumerate(lists):  
                    depth=  auto.LogControlNewdepth(control, i, showAllName, showPid)   
                    NameControl= auto.LogControlNewSmal(control, i, showAllName, showPid) 
                    if self.rowsSearh=="":
                        self.rowsSearh=f"element{i}={auto.LogControlNew(control, i, showAllName, showPid)}\n"
                    else:
                        #if i==1:
                           #self.wa(control) 
                        self.rowsSearh=self.rowsSearh + f"element{i}={auto.LogControlNew(control, i, showAllName, showPid)}\n"
                    if i==0:
                        node = QStandardItem(f"id:{i}|{depth} {NameControl}")  
                        self.model.appendRow(node)
                        #node = self.tree.insert("", tk.END, text=f"id:{i}|{depth} {NameControl}", open=False)
                        self.nodes[str(node)] = control
                        continue
                    ch=QStandardItem(f"id:{i}|{depth} {NameControl}")
                    node.appendRow(ch)
                    node=ch                                  
                    #node = self.tree.insert(node, tk.END, text=f"id:{i}|{depth} {NameControl}", open=False)   
                    self.nodes[str(node)] = control
            else:
                print('IUIAutomation returns null element under cursor\n')     
    def wa(self,controlW, node="", icount=0):        
        if icount==0:            
            node = QStandardItem(f"{controlW.Name} {controlW.ControlTypeName}")            
            self.model.appendRow(node)
            self.nodes[str(node)] =controlW        
        else:            
            ch=QStandardItem(f"{controlW.Name} {controlW.ControlTypeName}")            
            node.appendRow(ch) 
            node=ch
            self.nodes[str(node)] =controlW        
        for control in controlW.GetChildren(): 
            
            icount+=1
            if len(control.GetChildren())>0:                 
                self.wa(control,node, icount)
            else:
                ch= QStandardItem(f"{controlW.Name} {controlW.ControlTypeName}") 
                print(ch)  
                self.nodes[str(ch)] =controlW         
                node.appendRow(ch)                 
    # переменные и методы   

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0443\u043a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Text Element", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"****", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Value Element", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"****", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Invoke", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Click", None))
    # retranslateUi
def fin():
    element1=auto.WindowControl(searchDepth=1, ClassName='#32770', Name='Выполнить')
    element1.SetActive()
    element2=element1.ComboBoxControl(ClassName='ComboBox', Name='Открыть:', AutomationId='12298')
    element3=element2.EditControl(ClassName='Edit', Name='Открыть:', AutomationId='1001')

    element3.GetValuePattern().SetValue('cmd')
    element1=auto.WindowControl(searchDepth=1, ClassName='#32770', Name='Выполнить')
    element1.SetActive()
    element2=element1.ButtonControl(ClassName='Button', Name='ОК', AutomationId='1')

    element2.GetInvokePattern().Invoke()
import sys
if __name__ == '__main__': 
    # fin()
    app = QApplication(sys.argv)
    Syderwindow = Spyder()
    sys.exit(app.exec())