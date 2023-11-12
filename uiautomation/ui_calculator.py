#!python3
# -*- coding: utf-8 -*-
# works on windows XP, 7, 8, 8.1 and 10
import os
import sys
import time
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # not required after 'pip install uiautomation'
import uiautomation as auto

auto.uiautomation.DEBUG_EXIST_DISAPPEAR = True  # set it to False and try again, default is False
auto.uiautomation.DEBUG_SEARCH_TIME = True  # set it to False and try again, default is False
auto.uiautomation.TIME_OUT_SECOND = 10  # global time out

#Калькулятор
'''
-выбрать окно
-проверить кнопку МС
-нажать на комбинацю цифр
-поместиь в M+
-ввести новую комбинацию клавишь + MC
'''
#получаем кнопку 2MC
def get_MC():
    element1=auto.WindowControl(searchDepth=1, 
                                ClassName='ApplicationFrameWindow', 
                                Name='Calculator')
    element1.SetActive()
    element2=element1.WindowControl(ClassName='Windows.UI.Core.CoreWindow', 
                                    Name='Calculator', AutomationId='')
    element3=element2.CustomControl(ClassName='', 
                                    Name='', AutomationId='NavView')
    element4=element3.GroupControl(ClassName='LandmarkTarget', 
                                Name='', AutomationId='')
    element5=element4.GroupControl(ClassName='NamedContainerAutomationPeer', 
                                Name='Memory controls', AutomationId='MemoryPanel')
    element6=element5.ButtonControl(ClassName='Button', 
                                    Name='Clear all memory', AutomationId='ClearMemoryButton')

    if element6.Exists(1):
        print('кнопка существует')
    else:
        print('кнопка НЕ существует')
    if element6.IsEnabled:
        print('кнопка активна')
    else:
        print('кнопка НЕ активна')
    if element6.IsOffscreen:
        print('кнопка вне экрана')
    else:
        print('кнопка в области видимости экрана')

    return element6
#получаем кнопку 2
def get_two():
    element1=auto.WindowControl(searchDepth=1, ClassName='ApplicationFrameWindow', Name='Calculator')
    element1.SetActive()
    element2=element1.WindowControl(ClassName='Windows.UI.Core.CoreWindow', Name='Calculator', AutomationId='')
    element3=element2.CustomControl(ClassName='', Name='', AutomationId='NavView')
    element4=element3.GroupControl(ClassName='LandmarkTarget', Name='', AutomationId='')
    element5=element4.GroupControl(ClassName='NamedContainerAutomationPeer', Name='Number pad', AutomationId='NumberPad')
    element6=element5.ButtonControl(ClassName='Button', Name='Two', AutomationId='num2Button')

    return element6
#полчаем кнопку M+
def get_M_plus():
    element1=auto.WindowControl(searchDepth=1, ClassName='ApplicationFrameWindow', Name='Calculator')
    element1.SetActive()
    element2=element1.WindowControl(ClassName='Windows.UI.Core.CoreWindow', Name='Calculator', AutomationId='')
    element3=element2.CustomControl(ClassName='', Name='', AutomationId='NavView')
    element4=element3.GroupControl(ClassName='LandmarkTarget', Name='', AutomationId='')
    element5=element4.GroupControl(ClassName='NamedContainerAutomationPeer', Name='Memory controls', AutomationId='MemoryPanel')
    element6=element5.ButtonControl(ClassName='Button', Name='Memory add', AutomationId='MemPlus')

    return element6
#получаем кнопку СЕ
def get_CE():
    element1=auto.WindowControl(searchDepth=1, ClassName='ApplicationFrameWindow', Name='Calculator')
    element1.SetActive()
    element2=element1.WindowControl(ClassName='Windows.UI.Core.CoreWindow', Name='Calculator', AutomationId='')
    element3=element2.CustomControl(ClassName='', Name='', AutomationId='NavView')
    element4=element3.GroupControl(ClassName='LandmarkTarget', Name='', AutomationId='')
    element5=element4.GroupControl(ClassName='NamedContainerAutomationPeer', Name='Display controls', AutomationId='DisplayControls')
    element6=element5.ButtonControl(ClassName='Button', Name='Clear entry', AutomationId='clearEntryButton')
    return element6
#получаем кнопку +
def get_plus():
    element1=auto.WindowControl(searchDepth=1, ClassName='ApplicationFrameWindow', Name='Calculator')
    element1.SetActive()
    element2=element1.WindowControl(ClassName='Windows.UI.Core.CoreWindow', Name='Calculator', AutomationId='')
    element3=element2.CustomControl(ClassName='', Name='', AutomationId='NavView')
    element4=element3.GroupControl(ClassName='LandmarkTarget', Name='', AutomationId='')
    element5=element4.GroupControl(ClassName='NamedContainerAutomationPeer', Name='Standard operators', AutomationId='StandardOperators')
    element6=element5.ButtonControl(ClassName='Button', Name='Plus', AutomationId='plusButton')
    return element6
#получаем кнопку MR
def get_MR():

    element1=auto.WindowControl(searchDepth=1, ClassName='ApplicationFrameWindow', Name='Calculator')
    element1.SetActive()
    element2=element1.WindowControl(ClassName='Windows.UI.Core.CoreWindow', Name='Calculator', AutomationId='')
    element3=element2.CustomControl(ClassName='', Name='', AutomationId='NavView')
    element4=element3.GroupControl(ClassName='LandmarkTarget', Name='', AutomationId='')
    element5=element4.GroupControl(ClassName='NamedContainerAutomationPeer', Name='Memory controls', AutomationId='MemoryPanel')
    element6=element5.ButtonControl(ClassName='Button', Name='Memory recall', AutomationId='MemRecall')
    return element6
#получаем кнопку =
def get_equal():
    element1=auto.WindowControl(searchDepth=1, ClassName='ApplicationFrameWindow', Name='Calculator')
    element1.SetActive()
    element2=element1.WindowControl(ClassName='Windows.UI.Core.CoreWindow', Name='Calculator', AutomationId='')
    element3=element2.CustomControl(ClassName='', Name='', AutomationId='NavView')
    element4=element3.GroupControl(ClassName='LandmarkTarget', Name='', AutomationId='')
    element5=element4.GroupControl(ClassName='NamedContainerAutomationPeer', Name='Standard operators', AutomationId='StandardOperators')
    element6=element5.ButtonControl(ClassName='Button', Name='Equals', AutomationId='equalButton')
    return element6


#нажимаем двойку
get_two().GetInvokePattern().Invoke()
#нажимаем М+
get_M_plus().GetInvokePattern().Invoke()
#нажимаем CE+
get_CE().GetInvokePattern().Invoke()
#нажимаем двойку
get_two().GetInvokePattern().Invoke()
#нажимаем двойку
get_two().GetInvokePattern().Invoke()
#нажимаем +
get_plus().GetInvokePattern().Invoke()
#нажимаем +
get_MR().GetInvokePattern().Invoke()
#нажимаем =
get_equal().GetInvokePattern().Invoke()
#нажимаем MC
get_MC().GetInvokePattern().Invoke()
