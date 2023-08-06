# coding=utf-8
import easygui as eg

def buttonbox(msg='', choices=[], title=''):
    eg.buttonbox(msg, title, choices)

def choicebox(msg='', choices=[], title=''):
    choicebox(msg, title, choices)

def enterbox(msg='', title=''):
    eg.enterbox(msg, title)

def fileopenbox(msg='', title=''):
    eg.fileopenbox(msg, title)[0]

def indexbox(msg='', choices=[], title=''):
    eg.indexbox(msg, title, choices)

def msgbox(msg='', image=None):
    eg.msgbox(msg, image=image)

def multchoicebox(msg='', choices=[], title=''):
    eg.multchoicebox(msg, title, choices)

def multpasswordbox(msg='', title=''):
    eg.multchoicebox(msg, title)

def passwordbox(msg='', title=''):
    eg.passwordbox(msg, title)

def textbox(msg='', text='', title='', codebox=False):
    eg.textbox(msg, title, text, codebox)

def ynbox(msg='', choices=[], title=''):
    eg.ynbox(msg, title, choices)

def codebox(msg='', text='', title=''):
    eg.codebox(msg, title, text)
