#要求：有完整的界面，增删改查功能。人员信息包括编号、姓名、联系方式、住址、工作单位、职位。
#使用文本文档保存和读取。
import wx
import sys
import os
import threading

#人员信息类
class GetInfo:
    __number = "null" #编号
    __name = "null" #姓名
    __phone = "null" #联系方式
    __address = "null" #地址
    __workUnit = "null"  #工作单位
    __post = "null"  #职位
    def SetNumber(self,number):
        self.__number = number
        return
    def SetName(self,name):
        self.__name = name
        return
    def SetPhone(self,phone):
        self.__phone = phone
        return
    def SetAddress(self,address):
        self.__address = address
        return
    def SetWorkUnit(self,workUnit):
        self.__workUnit = workUnit
        return
    def SetPost(self,post):
        self.__post = post
        return

    def GetNumber(self):
        return self.__number
    def GetName(self):
        return self.__name
    def GetPhone(self):
        return self.__phone
    def GetAddress(self):
        return self.__address
    def GetWorkUnit(self):
        return self.__workUnit
    def GetPost(self):
        return self.__post

    def __init__(self,name,number,phone,address,workUnit,post):
        '''
        设置信息
        :param number: 编号
        :param name: 姓名
        :param phone: 联系方式
        :param address: 地址
        :param workUnit: 工作单位
        :param post:职位
        '''
        self.SetNumber(number)
        self.SetName(name)
        self.SetPhone(phone)
        self.SetAddress(address)
        self.SetWorkUnit(workUnit)
        self.SetPost(post)
    #获取信息
    def GetInfo(self):
        info = {
            'number':self.GetNumber(),
            'name':self.GetName(),
            'phone':self.GetPhone(),
            'address':self.GetAddress(),
            'workUnit':self.GetWorkUnit(),
            'post':self.GetPost()
        }
        return info

#单利
class Singleton(object):
    # 单利模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Frame, cls)
            cls.__instance = orig.__new__(cls, *args, **kwargs)
        return cls.__instance

#增删改查窗体父类
class OtherFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="通讯录增加界面", size=(300, 300), style=wx.CLOSE_BOX | wx.CAPTION)
        panel = wx.Panel(self)
        self.Center()
        # 姓名
        self.namelbl = wx.StaticText(parent=panel, id=-1, label="姓名:", size=(60, 30), pos=(40, 30), style=wx.TE_RIGHT)
        self.nameTxt = wx.TextCtrl(parent=panel, id=-1, value="", size=(120, 25), pos=(120, 25))
        self.isnameTxtlbl = wx.StaticText(parent=panel, id=-1, pos=(250, 30))
        # 编号
        self.numberlbl = wx.StaticText(parent=panel, id=-1, label="编号*:", size=(60, 30), pos=(40, 60), style=wx.TE_RIGHT)
        self.numberTxt = wx.TextCtrl(parent=panel, id=-1, value="", size=(120, 25), pos=(120, 55))
        self.isnumberTxtlbl = wx.StaticText(parent=panel,id=-1,pos=(250,60))
        # 联系方式
        self.phonelbl = wx.StaticText(parent=panel, id=-1, label="联系方式:", size=(60, 30), pos=(40, 90), style=wx.TE_RIGHT)
        self.phoneTxt = wx.TextCtrl(parent=panel, id=-1, value="", size=(120, 25), pos=(120, 85))
        self.isphoneTxtlbl = wx.StaticText(parent=panel, id=-1, pos=(250, 90))
        # 地址
        self.addresslbl = wx.StaticText(parent=panel, id=-1, label="地址:", size=(60, 30), pos=(40, 120), style=wx.TE_RIGHT)
        self.addressTxt = wx.TextCtrl(parent=panel, id=-1, value="", size=(120, 25), pos=(120, 115))
        self.isaddressTxtlbl = wx.StaticText(parent=panel, id=-1, pos=(250, 120))
        # 工作单位
        self.workUnitlbl = wx.StaticText(parent=panel, id=-1, label="工作单位:", size=(60, 30), pos=(40, 150), style=wx.TE_RIGHT)
        self.workUnitTxt = wx.TextCtrl(parent=panel, id=-1, value="", size=(120, 25), pos=(120, 145))
        self.isworkUnitTxtlbl = wx.StaticText(parent=panel, id=-1, pos=(250, 150))
        # 职位
        self.postlbl = wx.StaticText(parent=panel, id=-1, label="职位:", size=(60, 30), pos=(40, 180), style=wx.TE_RIGHT)
        self.postTxt = wx.TextCtrl(parent=panel, id=-1, value="", size=(120, 25), pos=(120, 175))
        self.ispostTxtlbl = wx.StaticText(parent=panel, id=-1, pos=(250, 180))
        # 确定按钮
        self.sureBtn = wx.Button(parent=panel, id=-1, label="确定添加", pos=(120, 210))

#增加类
class AddFrame(OtherFrame,Singleton):
    def __init__(self):
        super(AddFrame, self).__init__()
        self.path = os.getcwd()  # 获取当前路径
        #如果当前文件不存在则创建
        if not os.path.exists(self.path + "\info.txt"):
            try:
                self.CreateTxt("info")  # 创建信息文件
            except:
                wx.MessageBox("文件创建失败!","错误")
        self.sureBtn.SetLabel("确定添加")
        self.Bind(event=wx.EVT_BUTTON,handler=self.AgetInfo,source=self.sureBtn)
        self.Bind(wx.EVT_TEXT, self.txtfun, self.numberTxt)
#写入信息,获取事件
    def AgetInfo(self,e):
        try:
            name = self.nameTxt.GetValue()  #获取姓名
            number = self.numberTxt.GetValue()  #获取编号
            phone = self.phoneTxt.GetValue()    #联系方式
            address = self.addressTxt.GetValue()    #地址
            workUnit = self.workUnitTxt.GetValue()  #工作单位
            post = self.postTxt.GetValue()  #职位
            if (name != "")and(number != "")and(phone != "")and(address != "")and(workUnit != "")and(post != ""):
                try:
                    info = str(GetInfo(name,number,phone,address,workUnit,post).GetInfo())   #获取信息
                    infoappendtxt = open(self.path + "\info.txt","a",encoding='utf-8')  #打开文件
                    infoappendtxt.write(info + "\n")    #写入文件
                    wx.MessageBox(message="添加成功!", caption="提示")
                    infoappendtxt.close()
                except:
                    wx.MessageBox(message="添加失败!", caption="错误")
                finally:
                    pass
            else:
                wx.MessageBox(message="请填入完整信息!",caption="提示")
        except:
            pass
        finally:
            self.nameTxt.SetValue("")
            self.numberTxt.SetValue("")
            self.phoneTxt.SetValue("")
            self.addressTxt.SetValue("")
            self.workUnitTxt.SetValue("")
            self.postTxt.SetValue("")

    def TxtEvent(self):
        self.count = -1
        try:
            self.inforeadtxt = open(self.path + "\info.txt", 'r', encoding="utf-8")  # 打开文件
        except:
            pass
        istrue = False
        try:
            lines = self.inforeadtxt.readlines()
            for line in lines:  # 逐行读取
                line = eval(line)  # 字符串转为字典
                try:
                    if str(line["number"]) != self.numberTxt.GetValue():  # 如果编号相等
                        try:
                            self.isnumberTxtlbl.SetLabel("true")
                        except:
                            self.isnumberTxtlbl.SetLabel("false")
                    else:
                        self.isnumberTxtlbl.SetLabel("false")
                        istrue = True
                        break
                except:
                    self.isnumberTxtlbl.SetLabel("false")
                finally:
                    self.count += 1

        except:
            self.isnumberTxtlbl.SetLabel("false")
        finally:
            if self.isnumberTxtlbl.GetLabel() == "true":
                self.nameTxt.Enable()
                self.phoneTxt.Enable()
                self.addressTxt.Enable()
                self.workUnitTxt.Enable()
                self.postTxt.Enable()
                self.sureBtn.Enable()
            if istrue:
                self.sureBtn.Disable()
                self.nameTxt.Disable()
                self.phoneTxt.Disable()
                self.addressTxt.Disable()
                self.workUnitTxt.Disable()
                self.postTxt.Disable()
                self.isnumberTxtlbl.SetLabel("false")


    #文本事件线程
    def txtfun(self, event):
        try:
            self.twork = threading.Thread(target=self.TxtEvent)
            self.twork.start()
        except:
            pass
        finally:
            pass
        return

#创建文件
    def CreateTxt(self,name):
        try:
            path = os.getcwd()  # 获取当前路径
            full_path = str(path + "\\" + name + ".txt")
            txt = open(full_path,"w",encoding="utf-8")    #如果文件不存在则创建
            # txt.write("\t\t\t\t\t\t\t人员信息\n")
        except:
            pass
        return txt

#删除类
class DelFrame(OtherFrame,Singleton):
    def __init__(self):
        super(DelFrame, self).__init__()
        self.sureBtn.Disable()
        self.path = os.getcwd()  # 获取当前路径
        self.SetTitle("通讯录删除界面")
        self.sureBtn.SetLabel("确定删除")
        self.phoneTxt.Disable()
        self.addressTxt.Disable()
        self.workUnitTxt.Disable()
        self.nameTxt.Disable()
        self.postTxt.Disable()
        self.Bind(event=wx.EVT_BUTTON,handler=self.fun,source=self.sureBtn)
        self.Bind(wx.EVT_TEXT,self.txtfun,self.numberTxt)

    def DelInfo(self):
        self.inforeadtxt = open(self.path + "\info.txt", 'r', encoding="utf-8") #打开文件
        try:
            # lines[self.count - 1] 需要删除的元素
            lines = list(self.inforeadtxt.readlines())
            lines.remove(lines[self.count]) #删除
            self.numberTxt.SetValue("删除成功")
            self.infowtxt = open(self.path + "\info.txt", 'w', encoding="utf-8")  # 打开文件
            self.infowtxt.write("")
            for line in range(0,len(lines)+1): # 重新写入文件
                self.infowritetxt = open(self.path + "\info.txt", 'a+', encoding="utf-8")  # 打开文件
                self.infowritetxt.write(str(lines[line]))
        except:
            pass
        return

    def fun(self, event):
        try:
            self.twork = threading.Thread(target=self.DelInfo)
            self.twork.start()
        except:
            pass
        finally:
            pass
        return

    def TxtEvent(self):
        self.count = -1
        self.inforeadtxt = open(self.path + "\info.txt", 'r', encoding="utf-8")  # 打开文件
        istrue = False
        try:
            lines = self.inforeadtxt.readlines()
            for line in lines:  # 逐行读取
                line = eval(line)  # 字符串转为字典
                try:
                    if str(line["number"]) == self.numberTxt.GetValue():  # 如果编号相等
                        try:
                            self.nameTxt.SetValue(line["name"])
                            self.phoneTxt.SetValue(line["phone"])
                            self.addressTxt.SetValue(line["address"])
                            self.workUnitTxt.SetValue(line["workUnit"])
                            self.postTxt.SetValue(line["post"])
                            self.isnumberTxtlbl.SetLabel("true")
                            istrue = True
                            break
                        except:
                            self.isnumberTxtlbl.SetLabel("false")
                except:
                    self.isnumberTxtlbl.SetLabel("false")
                finally:
                    self.count += 1 #获取要删除元素的位置

        except:
            self.isnumberTxtlbl.SetLabel("false")
        finally:
            try:
                if not istrue:
                    self.sureBtn.Disable()
                    self.isnumberTxtlbl.SetLabel("false")
                    self.nameTxt.SetValue("查无此人!")
                    self.phoneTxt.SetValue("查无此人!")
                    self.addressTxt.SetValue("查无此人!")
                    self.workUnitTxt.SetValue("查无此人!")
                    self.postTxt.SetValue("查无此人!")
                else:
                    self.sureBtn.Enable()
            except:
                pass
        # 文本事件线程

    def txtfun(self, event):
        try:
            self.twork = threading.Thread(target=self.TxtEvent)
            self.twork.start()
        except:
            pass
        finally:
            pass
        return

#修改类
class UpDataFrame(OtherFrame,Singleton):
    def __init__(self):
        super(UpDataFrame, self).__init__()
        self.sureBtn.Disable()
        self.SetTitle("通讯录修改界面")
        self.sureBtn.SetLabel("确定修改")
        self.nameTxt.Disable()
        self.phoneTxt.Disable()
        self.addressTxt.Disable()
        self.workUnitTxt.Disable()
        self.postTxt.Disable()
        self.path = os.getcwd()  # 获取当前路径
        self.Bind(event=wx.EVT_BUTTON, handler=self.fun, source=self.sureBtn)
        self.Bind(wx.EVT_TEXT,self.txtfun,self.numberTxt)

    def UpdataInfo(self):
        self.inforeadtxt = open(self.path + "\info.txt", 'r', encoding="utf-8") #打开文件
        try:
            lines = self.inforeadtxt.readlines()
            for line in lines:  # 逐行读取
                line = eval(line)  # 字符串转为字典
                try:
                    if str(line["number"]) == self.numberTxt.GetValue():  # 如果编号相等
                        try:
                            dictline = {
                                "number":line["number"],
                                "name":self.nameTxt.GetValue(),
                                "phone":self.phoneTxt.GetValue(),
                                "address":self.addressTxt.GetValue(),
                                "workUnit":self.workUnitTxt.GetValue(),
                                "post":self.postTxt.GetValue()
                            }
                            lines.remove(lines[self.count])    #删除元素
                            lines.insert(self.count,str(dictline)+"\n")   #插入元素
                            self.numberTxt.SetValue("修改成功")
                            self.isnumberTxtlbl.SetLabel("true")
                            istrue = True
                            break
                        except:
                            self.isnumberTxtlbl.SetLabel("false")
                except:
                    self.isnumberTxtlbl.SetLabel("false")
                finally:
                    pass
            self.infowtxt = open(self.path + "\info.txt", 'w', encoding="utf-8")  # 打开文件
            self.infowtxt.write("")
            for line in range(0,len(lines)+1):  # 重新写入文件
                self.infowritetxt = open(self.path + "\info.txt", 'a+', encoding="utf-8")  # 打开文件
                self.infowritetxt.write(str(lines[line]))
        except:
            pass
        return
#修改事件线程
    def fun(self, event):
        try:
            self.twork = threading.Thread(target=self.UpdataInfo)
            self.twork.start()
        except:
            pass
        finally:
            pass
        return

    def TxtEvent(self):
        self.count = -1
        try:
            self.inforeadtxt = open(self.path + "\info.txt", 'r', encoding="utf-8")  # 打开文件
        except:
            pass
        istrue = False
        try:
            lines = self.inforeadtxt.readlines()
            for line in lines:  # 逐行读取
                line = eval(line)  # 字符串转为字典
                try:
                    if str(line["number"]) == self.numberTxt.GetValue():  # 如果编号相等
                        try:
                            self.nameTxt.SetValue(line["name"])
                            self.phoneTxt.SetValue(line["phone"])
                            self.addressTxt.SetValue(line["address"])
                            self.workUnitTxt.SetValue(line["workUnit"])
                            self.postTxt.SetValue(line["post"])
                            self.isnumberTxtlbl.SetLabel("true")
                            istrue = True
                            break
                        except:
                            self.isnumberTxtlbl.SetLabel("false")
                except:
                    self.isnumberTxtlbl.SetLabel("false")
                finally:
                    self.count += 1

        except:
            self.isnumberTxtlbl.SetLabel("false")
        finally:
            if self.isnumberTxtlbl.GetLabel() == "true":
                self.nameTxt.Enable()
                self.phoneTxt.Enable()
                self.addressTxt.Enable()
                self.workUnitTxt.Enable()
                self.postTxt.Enable()
                self.sureBtn.Enable()
            if not istrue:
                self.sureBtn.Disable()
                self.nameTxt.Disable()
                self.phoneTxt.Disable()
                self.addressTxt.Disable()
                self.workUnitTxt.Disable()
                self.postTxt.Disable()
                self.isnumberTxtlbl.SetLabel("false")
                self.nameTxt.SetValue("查无此人!")
                self.phoneTxt.SetValue("查无此人!")
                self.addressTxt.SetValue("查无此人!")
                self.workUnitTxt.SetValue("查无此人!")
                self.postTxt.SetValue("查无此人!")
    #文本事件线程
    def txtfun(self, event):
        try:
            self.twork = threading.Thread(target=self.TxtEvent)
            self.twork.start()
        except:
            pass
        finally:
            pass
        return

#查找类
class FindFrame(OtherFrame,Singleton):
    def __init__(self):
        super(FindFrame, self).__init__()
        self.path = os.getcwd()  # 获取当前路径
        self.SetTitle("通讯录查找界面")
        self.sureBtn.SetLabel("确定查找")
        self.nameTxt.Disable()
        self.phoneTxt.Disable()
        self.addressTxt.Disable()
        self.workUnitTxt.Disable()
        self.postTxt.Disable()
        self.Bind(wx.EVT_BUTTON,self.fun,self.sureBtn)

    def FindInfo(self):
        self.inforeadtxt = open(self.path + "\info.txt", 'r', encoding="utf-8") #打开文件
        istrue = False
        try:
            lines = self.inforeadtxt.readlines()
            for line in lines:  # 逐行读取
                line = eval(line)   #字符串转为字典
                try:
                    if str(line["number"]) == self.numberTxt.GetValue():    #如果编号相等
                        try:
                            self.nameTxt.SetValue(line["name"])
                            self.phoneTxt.SetValue(line["phone"])
                            self.addressTxt.SetValue(line["address"])
                            self.workUnitTxt.SetValue(line["workUnit"])
                            self.postTxt.SetValue(line["post"])
                            istrue = True
                            break
                        except:
                            wx.MessageBox("查找错误!", "错误")
                except:
                    wx.MessageBox("查找错误!", "错误")
        except:
            wx.MessageBox("查找错误!", "错误")
        finally:
            if not istrue:
                self.nameTxt.SetValue("查无此人!")
                self.phoneTxt.SetValue("查无此人!")
                self.addressTxt.SetValue("查无此人!")
                self.workUnitTxt.SetValue("查无此人!")
                self.postTxt.SetValue("查无此人!")

    def fun(self, event):
        try:
            self.twork = threading.Thread(target=self.FindInfo)
            self.twork.start()
        except:
            pass
        finally:
            pass
        return

#窗体类
class Frame(wx.Frame):
    def __init__(self):
        self.font = wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.btnFont = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.width = 400
        self.height = 400
        wx.Frame.__init__(self,parent=None,id=-1,title="通讯录系统",size=(self.width,self.height),style=wx.MINIMIZE_BOX|wx.CAPTION)
        self.Center()
        panel = wx.Panel(self)

        optionTxt = wx.StaticText(parent=panel,id=-1,label="欢迎进入通讯录系统 !",size=(150,30),pos=((self.width-150)/2,10))
        selectTxt = wx.StaticText(parent=panel,id=-1,label="请选择:",pos=(self.width/2-80,50))
        selectTxt.SetFont(self.font)
        self.addBtn = wx.Button(parent=panel,id=-1,label="添加联系人",size=(130,40),pos=((self.width-140)/2,120))
        self.addBtn.SetFont(self.btnFont)
        findBtn = wx.Button(parent=panel, id=-1, label="查找联系人", size=(130, 40), pos=((self.width - 140) / 2, 160))
        findBtn.SetFont(self.btnFont)
        updateBtn = wx.Button(parent=panel, id=-1, label="修改联系人", size=(130, 40), pos=((self.width - 140) / 2, 200))
        updateBtn.SetFont(self.btnFont)
        delBtn = wx.Button(parent=panel, id=-1, label="删除联系人", size=(130, 40), pos=((self.width - 140) / 2, 240))
        delBtn.SetFont(self.btnFont)
        exitBtn = wx.Button(parent=panel, id=-1, label="退出系统", size=(130, 40), pos=((self.width - 140) / 2, 280))
        exitBtn.SetFont(self.btnFont)

        self.Bind(event=wx.EVT_BUTTON, handler=self.addFrame, source=self.addBtn)  # 增加
        self.Bind(event=wx.EVT_BUTTON, handler=self.delFrame, source=delBtn)  # 删除
        self.Bind(event=wx.EVT_BUTTON, handler=self.updateFrame, source=updateBtn)  # 修改
        self.Bind(event=wx.EVT_BUTTON, handler=self.findFrame, source=findBtn)  # 查找
        self.Bind(event=wx.EVT_BUTTON,handler=self.exit,source=exitBtn) #退出系统

    def addFrame(self,e):
        frame = AddFrame()
        frame.Show()
        return
    def delFrame(self,e):
        DelFrame().Show()
        return
    def updateFrame(self,e):
        UpDataFrame().Show()
        return
    def findFrame(self,e):
        FindFrame().Show()
        return
    def exit(self,e):
        sys.exit()
        return

def main():
    ''''''
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()
    return

if __name__ == '__main__':
    main()