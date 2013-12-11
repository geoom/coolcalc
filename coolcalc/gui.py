# -*- coding: utf-8 *-*
import wx, os
import calculator
import analyzer
import validator
 
class MainWindow(wx.Frame):

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title, size=(400,100))
                  
        file_menu 	= wx.Menu() 

        about_item 	= file_menu.Append(wx.ID_ABOUT, "&About","info about this app")
        exir_item 	= file_menu.Append(wx.ID_EXIT,"&Exit"," finish the program")
         
        menu_bar 	= wx.MenuBar()
        menu_bar.Append(file_menu,"&File")       
        self.SetMenuBar(menu_bar) 
         
        self.Bind(wx.EVT_MENU, self.OnAbout, about_item)
        self.Bind(wx.EVT_MENU, self.OnExit, exir_item)
         
        lblOperation 	= wx.StaticText(self, label='Enter an arithmetic operation:')
        self.txtResult 		= wx.TextCtrl(self, style=wx.TE_MULTILINE)

        action_container 	= wx.BoxSizer(wx.HORIZONTAL)
        self.txtOperation 	= wx.TextCtrl(self, value='', size=(140, -1))
        self.btnCalculate		= wx.Button(self, -1, "Calculate")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btnCalculate)
        action_container.Add(self.txtOperation, 0, wx.EXPAND)
        action_container.Add(self.btnCalculate, 0, wx.EXPAND)

        main_container = wx.BoxSizer(wx.VERTICAL)
        main_container.Add(lblOperation, 0, wx.EXPAND)
        main_container.Add(action_container, 0, wx.EXPAND)
        main_container.Add(self.txtResult, 1, wx.EXPAND)
 
        self.SetSizer(main_container)
         
        self.Centre(True)
        self.Show(True)
     

    def OnClick(self,event):
    	expression = self.txtOperation.GetValue()

    	cool_cal 	= calculator.Calculator(
							analyzer.ExpresionAnalyser(),
							validator.ValidatorArithmeticExpression())

    	try:
    		result = cool_cal.calculate(expression)
    		self.txtResult.SetValue(result)
    	except SyntaxError:
    		self.txtResult.SetValue("Invalid expression: the expression cannot be calculated")
    	except ZeroDivisionError:
    		 self.txtResult.SetValue("Division by Zero: operation not allowed")
    	except ValueError:
    		self.txtResult.SetValue("result isnt integer: operation not allowed")

    def OnAbout(self,e):
        dlg = wx.MessageDialog( self, "This is an simple calculator of arithmetics operations", "About", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
 
    def OnExit(self,e):
        self.Close(True)
