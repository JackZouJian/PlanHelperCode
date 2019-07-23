import wx
import os,sys
import random
import threading

##############################################
#首页内部面板
class UserPanel(wx.Panel):
    def __init__(self,parent):
        super(UserPanel,self).__init__(parent,pos=(0,0),size=(575,490),
                                       style=wx.BORDER_SUNKEN | wx.CLIP_CHILDREN)

#首页界面面板类
class FirstHeadFrame(wx.Frame):
    def __init__(self):
        # self.MenuFont = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        wx.Frame.__init__(self, parent=None, size=(592, 550),
                          title="计划助手",
                          style=wx.MINIMIZE_BOX | wx.CAPTION |
                                wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.CLIP_CHILDREN)
        self.panel = wx.Panel(self)
        self.InitUI()
        self.Center()
        self.Bind(wx.EVT_CLOSE,self.OnClose)    #关闭窗体时
        self.OnAllClick()     #所有事件
    #
    #     # self.panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnErase)
    #     self.panel.Bind(wx.EVT_PAINT,self.OnPaint)
    # # def OnErase(self,e):
    # #     pass
    # def OnPaint(self,e):
    #     dc = wx.BufferedPaintDC(self)

#界面组件
    def InitUI(self):
        self.menuBar = wx.MenuBar()
        self.menuFirstHead = wx.Menu()  #首页
        self.itemShowAllPlan = self.menuFirstHead.Append(-1,"&显示所有计划")
        self.menuFirstHead.AppendSeparator()
        self.itemShowPlanInfo = self.menuFirstHead.Append(-1, "&显示计划信息")
        self.menuFirstHead.AppendSeparator()
        self.itemShowHabitInfo = self.menuFirstHead.Append(-1, "&显示习惯信息")
        self.menuFirstHead.AppendSeparator()
        self.itemPlanBat = self.menuFirstHead.Append(-1, "&计划打卡")
        self.menuFirstHead.AppendSeparator()
        self.itemHabitBat = self.menuFirstHead.Append(-1, "&习惯打卡")
        self.menuFirstHead.AppendSeparator()
        self.itemBill = self.menuFirstHead.Append(-1, "&账单")

        self.menuCreate = wx.Menu()     #创建
        self.itemCreatePlan = self.menuCreate.Append(-1, "&创建计划")
        self.menuCreate.AppendSeparator()
        self.itemCreateHabit = self.menuCreate.Append(-1,"&创建习惯")
        #
        self.menuPlan = wx.Menu()   #计划
        self.itemDayHabit = self.menuPlan.Append(-1,"&日常习惯")
        self.menuPlan.AppendSeparator()
        self.itemMyPlan = self.menuPlan.Append(-1,"&我的计划")
        #
        self.menuWriteBill = wx.Menu()      #记账
        self.itemInCome = self.menuWriteBill.Append(-1,"&收入")
        self.menuWriteBill.AppendSeparator()
        self.itemPayMent = self.menuWriteBill.Append(-1,"&支出")
        #
        self.menuMySlef = wx.Menu()
        self.itemSelfAccount = self.menuMySlef.Append(-1,"&个人账户")
        self.menuMySlef.AppendSeparator()
        self.itemSafetyCenter = self.menuMySlef.Append(-1,"&安全中心")
        self.menuMySlef.AppendSeparator()
        self.itemUserHelpr = self.menuMySlef.Append(-1,"&使用帮助")
        self.menuMySlef.AppendSeparator()
        self.itemAboutMe = self.menuMySlef.Append(-1,"&关于我们")

        self.menuBar.Append(self.menuFirstHead,"&首页")
        self.menuBar.Append(self.menuCreate,"&创建")
        self.menuBar.Append(self.menuPlan,"&计划")
        self.menuBar.Append(self.menuWriteBill,"&记账")
        self.menuBar.Append(self.menuMySlef, "&我的")

        self.SetMenuBar(self.menuBar)

        #面板列表
        self.ListPanel = []
        for itemPanel in range(0, 16):
            self.ListPanel.append(UserPanel(self.panel))
        # item组件列表
        self.itemList = [
            self.itemShowAllPlan, self.itemShowPlanInfo, self.itemShowHabitInfo, self.itemPlanBat,
            self.itemHabitBat, self.itemBill,
            self.itemCreatePlan, self.itemCreateHabit,
            self.itemDayHabit, self.itemMyPlan,
            self.itemInCome, self.itemPayMent,
            self.itemSelfAccount, self.itemSafetyCenter, self.itemUserHelpr, self.itemAboutMe
        ]
        #事件列表
        self.OnClickList = [
            self.OnClick0,self.OnClick1,self.OnClick2,
            self.OnClick3,self.OnClick4,self.OnClick5,
            self.OnClick6,self.OnClick7,
            self.OnClick8,self.OnClick9,
            self.OnClick10,self.OnClick11,
            self.OnClick12,self.OnClick13,self.OnClick14,self.OnClick15
        ]
        return

    #关闭
    def OnClose(self,e):
        dlg = wx.MessageDialog(self,u"确定退出?",u"提示",wx.YES_NO|wx.ICON_INFORMATION)
        if dlg.ShowModal() == wx.ID_YES:
            sys.exit()
        else:
            pass
    #显示当前面板，隐藏其他面吧
    def IsShowPanel(self,listpanel):
        for item in range(0, 16):
            if item==listpanel:
                self.ListPanel[item].Show(True)
            else:
                self.ListPanel[item].Show(False)
    # 给所有item添加事件
    def OnAllClick(self):
        for item in range(0, 16):
            self.Bind(wx.EVT_MENU, self.OnClickList[item], self.itemList[item])

    #显示所有计划
    def OnClick0(self,e):
        btn = wx.Button(self.ListPanel[0],-1,"asdfadf",(100,100))
        self.IsShowPanel(0)

    #显示计划信息
    def OnClick1(self,e):
        btn = wx.Button(self.ListPanel[1],-1,"sssssss")
        self.IsShowPanel(1)
    #显示习惯信息
    def OnClick2(self,e):
        btn = wx.Button(self.ListPanel[2],-1,"12312",(100,100))
        self.IsShowPanel(2)

    #习惯打卡
    def OnClick3(self,e):
        btn = wx.Button(self.ListPanel[3],-1,"ssss45346sss")
        self.IsShowPanel(3)

    #计划打卡
    def OnClick4(self, e):
        btn = wx.Button(self.ListPanel[4], -1, "fghfghh", (100, 100))
        self.IsShowPanel(4)

    #账单
    def OnClick5(self, e):
        btn = wx.Button(self.ListPanel[5], -1, "890ilu")
        self.IsShowPanel(5)

    # 创建计划
    def OnClick6(self, e):
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        panel = self.ListPanel[7]

        lblTitle = wx.StaticText(panel, -1, "创建计划", (215, 30))
        lblTitle.SetFont(lblTitleFont)

        lblPlanName = wx.StaticText(panel, -1, "计划名称:", (40, 83))
        lblPlanName.SetFont(lblFont)
        self.txtPlanName = wx.TextCtrl(panel, -1, "", (40, 112), (473, 25))

        lblPlanDays = wx.StaticText(panel, -1, "计划完成天数:", (40, 155))
        lblPlanDays.SetFont(lblFont)
        self.btn7 = wx.Button(panel, -1, "7天", (60, 184), (40, 40))
        self.btn21 = wx.Button(panel, -1, "21天", (120, 184), (40, 40))
        self.btn30 = wx.Button(panel, -1, "30天", (180, 184), (40, 40))
        self.btn100 = wx.Button(panel, -1, "100天", (240, 184), (40, 40))

        lblSelfDays = wx.StaticText(panel, -1, "自定义天数:===============", (40, 255))
        lblSelfDays.SetFont(lblFont)
        self.txtSelfDays = wx.TextCtrl(panel, -1, "7", (360, 255), (80, 25), wx.TE_CENTER)
        self.txtSelfDays.SetFont(lblFont)

        lblRelaxDays = wx.StaticText(panel, -1, "休息天数:=================", (40, 300))
        lblRelaxDays.SetFont(lblFont)
        self.txtRelaxDays = wx.TextCtrl(panel, -1, "2", (360, 300), (80, 25), wx.TE_CENTER)
        self.txtRelaxDays.SetFont(lblFont)

        lblFirstBatTime = wx.StaticText(panel, -1, "首次签到时间:", (40, 350))
        lblFirstBatTime.SetFont(lblFont)
        firstBatTimeList = ["今天", "明天"]
        self.rbxFirstBatTime = wx.RadioBox(panel, -1, pos=(80, 380), choices=firstBatTimeList)

        self.btnCreatePlan = wx.Button(panel, -1, "创建计划", (220, 440), (125, 30))
        self.btnCreatePlan.SetFont(lblFont)

        self.IsShowPanel(7)

    #创建习惯
    def OnClick7(self, e):
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        panel = self.ListPanel[6]

        lblTitle = wx.StaticText(panel,-1,"创建习惯",(215,30))
        lblTitle.SetFont(lblTitleFont)

        lblName = wx.StaticText(panel,-1,"给习惯命名:",(21,83))
        lblName.SetFont(lblFont)
        self.txtInputName = wx.TextCtrl(panel,-1,"",(165,80),(350,30))
        self.txtInputName.SetFont(lblFont)

        lblDayTime = wx.StaticText(panel,-1,"在一天什么时候:",(21,126))
        lblDayTime.SetFont(lblFont)
        rbxDayTimeList = ["任意时间  ","起床之后  ","晨间习惯  ","中午时分  "]
        self.rbxDayTime = wx.RadioBox(panel,-1,pos=(165,150),choices=rbxDayTimeList,style=wx.RA_SPECIFY_COLS)
        self.rbxDayTime.SetSelection(0)

        lblDayBat = wx.StaticText(panel, -1, "设置每日打卡次数:", (21, 215))
        lblDayBat.SetFont(lblFont)
        rbxDayBatList = ["每日 ","每周 "]
        self.rbxDayBat = wx.RadioBox(panel,-1,pos=(220,200),choices=rbxDayBatList)
        self.lblDayBatCount = wx.StaticText(panel, -1, "每日:", (390, 215))
        self.lblDayBatCount.SetFont(lblFont)
        self.txtInputDayBatCount = wx.TextCtrl(panel,-1,"1",(450,215),(50,25),wx.TE_CENTER)
        lblDayBatCountEnd = wx.StaticText(panel,-1,"次",(510,215))
        lblDayBatCountEnd.SetFont(lblFont)

        lblWeekTime = wx.StaticText(panel, -1, "在一周什么时候:", (21, 260))
        lblWeekTime.SetFont(lblFont)
        rbxWeekList = ["周一","周二","周三","周四","周五","周六","周日"]
        self.rbxWeek = wx.RadioBox(panel,-1,pos=(110,290),choices=rbxWeekList)
        self.rbxWeek.Disable()

        lblSpeak = wx.StaticText(panel, -1, "写一句激励自己的话:", (21, 360))
        lblSpeak.SetFont(lblFont)
        self.txtSpeak = wx.TextCtrl(panel,-1,"",(80,400),(430,25))

        btnFinish = wx.Button(panel,-1,"创建习惯",(220,440),(135,30))
        btnFinish.SetFont(lblFont)

        self.IsShowPanel(6)

    #日常习惯
    def OnClick8(self, e):
        btn = wx.Button(self.ListPanel[8], -1, "ghjrgkyjj", (100, 100))
        self.IsShowPanel(8)

    #我的计划
    def OnClick9(self, e):
        btn = wx.Button(self.ListPanel[9], -1, "sssssbzcafergss")
        self.IsShowPanel(9)

    #收入
    def OnClick10(self, e):
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        panel = self.ListPanel[10]

        lblTitle = wx.StaticText(panel, -1, "收入", (250, 30))
        lblTitle.SetFont(lblTitleFont)

        lblName = wx.StaticText(panel,-1,"收入名称:",(100,175))
        lblName.SetFont(lblFont)
        self.txtName = wx.TextCtrl(panel,-1,"",(270,175),(200,25))

        lblName = wx.StaticText(panel, -1, "收入金额(元):", (100, 250))
        lblName.SetFont(lblFont)
        self.txtName = wx.TextCtrl(panel, -1, "", (270, 250), (200, 25))

        self.btnSure = wx.Button(panel,-1,"确定",(210,360),(125,35))
        self.btnSure.SetFont(lblFont)

        self.IsShowPanel(10)
    #收入内部类
    class OnClick10InnerClass:
        def __init__(self):
            pass

    #支出
    def OnClick11(self, e):
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        panel = self.ListPanel[11]

        lblTitle = wx.StaticText(panel, -1, "支出", (250, 30))
        lblTitle.SetFont(lblTitleFont)

        lblName = wx.StaticText(panel, -1, "支出名称:", (100, 175))
        lblName.SetFont(lblFont)
        self.txtName = wx.TextCtrl(panel, -1, "", (270, 175), (200, 25))

        lblName = wx.StaticText(panel, -1, "支出金额(元):", (100, 250))
        lblName.SetFont(lblFont)
        self.txtName = wx.TextCtrl(panel, -1, "", (270, 250), (200, 25))

        self.btnSure = wx.Button(panel, -1, "确定", (210, 360), (125, 35))
        self.btnSure.SetFont(lblFont)

        self.IsShowPanel(11)
    #支出内部类
    class OnClick11InnerClass:
        def __init__(self):
            pass

    #个人账户
    def OnClick12(self, e):
        btn = wx.Button(self.ListPanel[12], -1, "asddsghdj56uhfghsfadf", (100, 100))
        self.IsShowPanel(12)

    #安全中心
    def OnClick13(self, e):
        btn = wx.Button(self.ListPanel[13], -1, "sssshcvbdfgssss")
        self.IsShowPanel(13)

    #使用帮助
    def OnClick14(self, e):
        btn = wx.Button(self.ListPanel[14], -1, "asdf 586iadf", (100, 100))
        self.IsShowPanel(14)

    #关于我们
    def OnClick15(self, e):
        btn = wx.Button(self.ListPanel[15], -1, "ssfjuyo86sssss")
        self.IsShowPanel(15)

#注册界面
class RegisterFrame(wx.Frame):
    def __init__(self):
        self.TitleFont = wx.Font(28, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.LblFont = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.TxtFont = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        wx.Frame.__init__(self, parent=None, size=(498, 379),
                          title="计划助手注册",
                          style=wx.MINIMIZE_BOX | wx.CAPTION |
                                wx.CLOSE_BOX | wx.STAY_ON_TOP)
        self.panel = wx.Panel(self)
        self.InitUI()
        self.Center()
        self.Bind(wx.EVT_TEXT,self.pwdOneFun,self.txtOnePwd)
        self.Bind(wx.EVT_TEXT,self.pwdTwoFun,self.txtTwoPwd)
        self.Bind(wx.EVT_BUTTON,self.OnRegBtn,self.btnSureRegister)

#界面组件
    def InitUI(self):
        lblTitle = wx.StaticText(self.panel, -1, "注册", (220, 32))
        lblTitle.SetFont(self.TitleFont)
        lblOnePwd = wx.StaticText(self.panel, -1, "密码:", (107, 107))
        lblOnePwd.SetFont(self.LblFont)
        self.txtOnePwd = wx.TextCtrl(self.panel, -1, "", (171, 104), (206, 31),wx.TE_PASSWORD)
        self.txtOnePwd.SetFont(self.TxtFont)
        lblTwoPwd = wx.StaticText(self.panel, -1, "确认密码:", (65, 162))
        lblTwoPwd.SetFont(self.LblFont)
        self.txtTwoPwd = wx.TextCtrl(self.panel, -1, "", (171, 160), (206, 31),wx.TE_PASSWORD)
        self.txtTwoPwd.SetFont(self.TxtFont)

        self.lblPwdSureOne = wx.StaticText(self.panel,-1,"",(385,106))
        self.lblPwdSureTwo = wx.StaticText(self.panel, -1, "", (385, 164))

        self.btnSureRegister = wx.Button(self.panel, -1, "确定注册", (107, 250), (270, 54))
        self.btnSureRegister.SetDefault()
        self.btnSureRegister.SetFont(self.TitleFont)
        self.btnSureRegister.Disable()
#注册按钮事件
    def OnRegBtn(self,e):
        """"""
        self.Mkdir()
    # 创建目录
    # 在C:\PlanHelper中创建一个与账号相同的目录
    def Mkdir(self):
        try:
            self.Path = "C:\\PlanHelper\\"
            self.FilePath = str(self.Path+str(self.accountNumber)+"\\")
        except:
            pass
        try:
            self.isExists = os.path.exists(self.FilePath)  # 判断目录是否存在
            if not self.isExists:
                os.mkdir(self.FilePath)  # 不存在则创建

                """1.一个名为‘actpwd’的文件用来存放账号、密码"""
                try:
                    actpwdtxtFile = str(self.FilePath + "actpwd.txt")
                    actpwdTxt = open(actpwdtxtFile, "w", encoding="utf-8")
                    actpwdDict = {str(self.accountNumber):str(self.txtTwoPwd.GetValue())}
                    actpwdTxt.write(str(actpwdDict))
                except:
                    pass

                """2.一个名为‘uid’的文件用来存放UID"""
                uidtxtFile = str(self.FilePath+"uid.txt")
                uidTxt = open(uidtxtFile,"w",encoding="utf-8")
                uidDict = {"uid":str(self.uidNumber)}
                uidTxt.write(str(uidDict))

                """3.一个名为‘plan’的目录用来存放创建好的计划"""
                self.isPlan = os.path.exists(self.FilePath + "plan\\")
                if not self.isPlan:
                    os.mkdir(self.FilePath + "plan\\")  # 不存在则创建
                else:
                    pass
                #	1.创建‘execute’的文件用来存放创建好的计划
                PlanexecutetxtFile = str(self.FilePath + "plan\\" + "execute.txt")
                PlanexecuteTxt = open(PlanexecutetxtFile, "w", encoding="utf-8")
                #	2.创建‘finish’的文件用存放打卡完成的计划
                PlanfinishtxtFile = str(self.FilePath + "plan\\" + "finish.txt")
                PlanfinishTxt = open(PlanfinishtxtFile, "w", encoding="utf-8")
                #	3.创建‘over’的文件用存放已经完成的计划
                PlanovertxtFile = str(self.FilePath + "plan\\" + "over.txt")
                PlanoverTxt = open(PlanovertxtFile, "w", encoding="utf-8")

                """4.一个名为‘habit’的目录用来存放创建好的习惯"""
                self.isHabit = os.path.exists(self.FilePath + "habit\\")
                if not self.isHabit:
                    os.mkdir(self.FilePath + "habit\\")  # 不存在则创建
                else:
                    pass
                #	1.创建‘execute’的文件存放执行中的习惯
                HabitexecutetxtFile = str(self.FilePath + "habit\\" + "execute.txt")
                HabitexecuteTxt = open(HabitexecutetxtFile, "w", encoding="utf-8")
                #	2.创建‘finish’的文件存放打卡完成的习惯
                HabitfinishtxtFile = str(self.FilePath + "habit\\" + "finish.txt")
                HabitfinishTxt = open(HabitfinishtxtFile, "w", encoding="utf-8")

                """5.一个名为‘bill’的目录用来存放创建好的账单"""
                self.isBill = os.path.exists(self.FilePath + "bill\\")
                if not self.isBill:
                    os.mkdir(self.FilePath + "bill\\")  # 不存在则创建
                else:
                    pass
                #	1.创建‘1 ~ 12’的文件存放不同的账单
                for num in range(1,13):
                    BilltxtFile = str(self.FilePath + "bill\\" + "bill"+str(num)+".txt")
                    BillTxt = open(BilltxtFile, "w", encoding="utf-8")

            else:
                pass
        except:
            pass

        try:
            wx.MessageBox("账号:"+str(self.accountNumber)+"\nUID:"+
                          str(self.uidNumber)+"\n请记下账号与UID!\n","信息",
                          style=wx.OK)
            self.txtOnePwd.SetValue("")
            self.txtTwoPwd.SetValue("")
            self.lblPwdSureOne.SetLabel("")
            self.lblPwdSureTwo.SetLabel("")
            wx.MessageBox("请退出!", "信息",style=wx.OK)
        except:
            pass

#1执行密码文本事件线程
    def pwdOneFun(self,event):
        try:
            pwdWork = threading.Thread(target=self.OnePwdIpt)
            pwdWork.start()
        except:
            pass
#1密码判断方法
    def OnePwdIpt(self):
        try:
            self.getOnePwd = str(self.txtOnePwd.GetValue())
            if self.getOnePwd.isalnum() and 15>=len(self.getOnePwd)>=10:    #是否为数字和字母的组合
                self.lblPwdSureOne.SetLabel("true")
            else:
                self.lblPwdSureOne.SetLabel("false")
        except:
            pass
# 2执行密码文本事件线程
    def pwdTwoFun(self, event):
        try:
            pwdWork = threading.Thread(target=self.TwoPwdIpt)
            pwdWork.start()
        except:
            pass
#2密码判断方法
    def TwoPwdIpt(self):
        try:
            #账号生成
            actOne = random.randint(10000,99999)
            actTwo = random.randint(10000,99999)
            #uid生成
            uidOne = random.randint(100,999)
            uidTwo = random.randint(1000,9999)
        except:
            pass
        try:
            self.getTwoPwd = str(self.txtTwoPwd.GetValue())
            if self.getOnePwd == self.getTwoPwd:
                self.lblPwdSureTwo.SetLabel("true")
            else:
                self.lblPwdSureTwo.SetLabel("false")
        except:
            pass
        try:
            if str(self.lblPwdSureOne.GetLabel())=="true" and str(self.lblPwdSureTwo.GetLabel())=="true":
                self.btnSureRegister.Enable()
                # 使用两个随机的5位数生成账号
                self.accountNumber = actOne * actTwo
                # 使用一个3位的随机数和一个4位的随机数生成UID
                self.uidNumber = uidOne * uidTwo
            else:
                self.btnSureRegister.Disable()
        except:
            pass

#登录界面面板类
class LoginFrame(wx.Frame):
    def __init__(self):
        self.TitleFont = wx.Font(28, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.LblFont = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.TxtFont = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        wx.Frame.__init__(self,parent=None,size=(488,379),
                          title="计划助手登录",
                          style=wx.MINIMIZE_BOX | wx.CAPTION |
                                wx.CLOSE_BOX | wx.STAY_ON_TOP)
        self.panel = wx.Panel(self)
        self.InitUI()
        self.Rbx()
        self.Bind(wx.EVT_BUTTON,self.OnRegisger,self.btnRegister)
        self.Bind(wx.EVT_BUTTON,self.OnBtnLogin,self.btnLogin)
        self.Bind(wx.EVT_BUTTON,self.OnLostPwd,self.btnLostPwd)

    #添加组件
    def InitUI(self):
        lblTitle = wx.StaticText(self.panel,-1,"计划助手",(166,32))
        lblTitle.SetFont(self.TitleFont)
        lblAccount = wx.StaticText(self.panel,-1,"账号:",(87,107))
        lblAccount.SetFont(self.LblFont)
        self.txtAccount = wx.TextCtrl(self.panel,-1,"",(151,104),(226,31))
        self.txtAccount.SetFont(self.TxtFont)
        lblPassword = wx.StaticText(self.panel, -1, "密码:", (87, 162))
        lblPassword.SetFont(self.LblFont)
        self.txtPassword = wx.TextCtrl(self.panel, -1, "",(151,160),(226,31),wx.TE_PASSWORD)
        self.txtPassword.SetFont(self.TxtFont)

        self.rabtnList = ["从不记住","记住密码"]
        self.rabtnBox = wx.RadioBox(self.panel, -1,pos=(150,193),choices=self.rabtnList,style=wx.RA_SPECIFY_COLS)
        self.rabtnBox.SetSelection(0)

        self.btnLostPwd = wx.Button(self.panel,-1,"忘记密码",(310,209),(65,25))
        self.btnLogin = wx.Button(self.panel,-1,"登录",(107,250),(270,54))
        self.btnLogin.SetDefault()
        self.btnLogin.SetFont(self.TitleFont)
        # self.btnLogin.Disable()
        self.btnRegister = wx.Button(self.panel,-1,"注册",(5,309),(63,25))
        return
    #单选按钮
    def Rbx(self):
        try:
            rememberPWD = str("C:\\PlanHelper\\remblog.txt")
            rememberPwdTxt = open(rememberPWD, "r", encoding="utf-8")
            line = eval(str(rememberPwdTxt.readline()))
            for isTrue,actpwd in line.items():
                if isTrue:
                    #设置单选按钮初始值
                    # self.rabtnBox.SetSelection(self.rabtnBox.FindString("记住密码"))
                    self.rabtnBox.SetSelection(1)
                    for act,pwd in actpwd.items():
                        self.txtAccount.SetValue(str(act))
                        self.txtPassword.SetValue(str(pwd))
                else:
                    # 设置单选按钮初始值
                    self.rabtnBox.SetSelection(0)
                    # self.rabtnBox.SetSelection(self.rabtnBox.FindString("从不记住"))

        except:pass
    #忘记密码按钮
    def OnLostPwd(self,e):
        try:
            self.path = "C:\\PlanHelper\\"
            self.dlgAct = wx.TextEntryDialog(self,"请输入你的账号!","找回密码")
            if self.dlgAct.ShowModal() == wx.ID_OK:
                self.actNum = self.dlgAct.GetValue()
                if self.actNum == "":
                    wx.MessageBox("输入不能为空!","错误")
                else:
                    self.actPath = str(self.path + self.actNum +"\\")
                    isActDir = os.path.exists(self.actPath)  # 判断目录(账号是否正确)是否存在
                    if isActDir:
                        self.dlgUid = wx.TextEntryDialog(self, "请输入你的UID!", "找回密码")
                        if self.dlgUid.ShowModal() == wx.ID_OK:
                            self.uidNum = self.dlgUid.GetValue()
                            if self.uidNum == "":
                                wx.MessageBox("输入不能为空!","错误")
                            else:
                                #获取uid
                                self.uidTxtRead = open(self.actPath + "uid.txt", 'r', encoding="utf-8")
                                self.uidDict = eval(str(self.uidTxtRead.readline()))
                                for uidName,uid in self.uidDict.items():
                                    if self.uidNum == str(uid):
                                        actpwdtxtRead = open(self.actPath + "actpwd.txt", 'r', encoding="utf-8")
                                        line = eval(str(actpwdtxtRead.readline()))
                                        for act,pwd in line.items():
                                            password = str(pwd)
                                        wx.MessageBox("密码为:"+password,"找回密码")
                                    else:
                                        wx.MessageBox("UID错误!", "错误")
                    else:
                        wx.MessageBox("账号错误!", "错误")

        except:
            pass
    #登录按钮事件
    def OnBtnLogin(self,e):
        """"""
        try:
            self.Path = "C:\\PlanHelper\\"+str(self.txtAccount.GetValue())+"\\"  #获取路径
            self.isActDir = os.path.exists(self.Path)    #判断目录是否存在
            if self.txtAccount.GetValue()=="" or self.txtPassword.GetValue()=="":
                wx.MessageBox("账号或密码不能为空!\n请重新输入!", "错误", wx.OK)
                self.txtPassword.SetValue("")
                self.txtAccount.SetValue("")
            else:
                if not self.isActDir:    #如果目录不存在(账号错误),则提示错误
                    wx.MessageBox("账号或密码错误!\n请重新输入!","错误",wx.OK)
                    self.txtPassword.SetValue("")
                    self.txtAccount.SetValue("")
                else:
                    """获取到actpwd文件中的账号和密码并判断"""
                    try:
                        #打开文件
                        actpwxTxtRead = open(self.Path+"\\actpwd.txt",'r',encoding="utf-8")
                        line = eval(str(actpwxTxtRead.readline())) #字符串转为字典
                        for act,pwd in line.items():
                            self.actNum = str(act)   #获取账号
                            self.pwdNum = str(pwd)   #获取密码
                        if self.actNum == self.txtAccount.GetValue() and \
                            self.pwdNum == self.txtPassword.GetValue():
                            """显示首页界面"""
                            FirstHeadFrame().Show(True)
                            self.Show(False)
                            try:
                                rbxIndex = str(self.rabtnBox.GetSelection()) #获取单选按钮编号

                                if rbxIndex == "0":
                                    try:# 创建密码文件
                                        path = str("C:\\PlanHelper\\remblog.txt")
                                        rememberPWD = path
                                        rememberPwdTxt = open(rememberPWD, "w", encoding="utf-8")
                                        rememberPwdTxt.write("")  # 账号密码存入文件
                                        self.rabtnBox.SetSelection(0)
                                    except:pass
                                elif rbxIndex == "1": #记住密码
                                    try:  # 创建密码文件
                                        path = str("C:\\PlanHelper\\remblog.txt")
                                        rememberPWD = path
                                        rememberPwdTxt = open(rememberPWD, "w", encoding="utf-8")
                                        rebPwdList = {"true":{str(self.actNum):str(self.pwdNum)}}  # 获取账号密码
                                        rememberPwdTxt.write(str(rebPwdList))  # 账号密码存入文件
                                        self.rabtnBox.SetSelection(1)
                                    except:
                                        pass
                                else:
                                    pass
                            except:
                                pass
                        else:
                            wx.MessageBox("账号或密码错误!","错误")

                    except:
                        pass
        except:
            pass
    #创建目录
    def Mkdir(self,dirname):
        try:
            isExists = os.path.exists(dirname) #判断目录是否存在
            if not isExists:
                os.mkdir(dirname)   #不存在则创建
            else:
                pass
        except:
            pass
    #注册按钮事件
    def OnRegisger(self,e):
        try:
            frame = RegisterFrame()
            frame.Show()
            #在C盘下创建 PlanHelper 总目录
            try:
                self.Mkdir("C:\\PlanHelper\\")
            except:
                pass
        except:
            pass

def main():
    app = wx.App()
    frame = LoginFrame()
    frame.Show()
    frame.Center()
    app.MainLoop()

if __name__ == '__main__':
    main()