import wx
import os,sys
import random,time
import threading

#单利
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(UserPanel,cls)
            cls.__instance = orig.__new__(cls,*args,**kwargs)
        return cls.__instance
#首页内部面板
class UserPanel(wx.Panel,Singleton):
    def __init__(self,parent,act):
        super(UserPanel,self).__init__(parent,pos=(0,0),size=(575,490),
                                       style=wx.BORDER_SUNKEN | wx.CLIP_CHILDREN)

#显示所计划#
class Panel0(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel0, self).__init__(parent,act)
        self.act = act
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "显示所有计划", (180, 30))
        lblTitle.SetFont(lblTitleFont)

        btnShow = wx.Button(self, -1, "刷新", (420, 30))
        btnShow.SetFont(lblFont)

        lblPlan = wx.StaticText(self, -1, "计划", (255, 80))
        lblPlan.SetFont(lblFont)
        self.txtPlan = wx.TextCtrl(self, -1, "", (1, 110), (570, 150), wx.TE_MULTILINE | wx.TE_READONLY)

        lblHabit = wx.StaticText(self, -1, "习惯", (255, 270))
        lblHabit.SetFont(lblFont)
        self.txtHabit = wx.TextCtrl(self, -1, "", (1, 300), (570, 150), wx.TE_MULTILINE | wx.TE_READONLY)

        self.Bind(wx.EVT_BUTTON,self.BtnClick,btnShow)
    def BtnClick(self,e):
        self.txtPlan.SetValue("")
        self.txtHabit.SetValue("")
        planCount = 0
        habitCount = 0
        try:
            path = "C:\\PlanHelper\\" + self.act + "\\"  # 获取路径
        except:pass
        #显示计划
        try:
            PlanRead = open(path + "plan\\execute.txt",'r',encoding="utf-8")#读取计划
            planLines = PlanRead.readlines()#读取
            for line in planLines:
                planCount = planCount + 1
                line = eval(line)
                self.txtPlan.AppendText(str(planCount)+"\n")
                txtPlan = str("创建时间为:"+line['创建时间']+"\n计划名称:"+line['计划名称']+\
                              "\n执行天数:"+line['自定义天数']+"\t休息天数:"+line['休息天数']+\
                              "\n首次打卡时间为:"+line['首次打卡时间']+"\n是否打卡:"+str(line['是否打卡'])+\
                              "\n打卡时间:"+line['打卡时间'])+"\n\n"
                self.txtPlan.AppendText(txtPlan)
        except:pass
        #显示习惯
        try:
            HabitRead = open(path + "habit\\execute.txt",'r',encoding="utf-8")#读取习惯
            habitLines = HabitRead.readlines()#读取
            for line in habitLines:
                habitCount = habitCount + 1
                line = eval(line)
                self.txtHabit.AppendText(str(habitCount)+"\n")
                if line['每日每周']=='每日':
                    txtHabit = str("创建时间为:"+line['创建时间']+"\n习惯名称:"+line['习惯名称']+\
                                  "\n在什么时候:"+line['在一天什么时候']+"\n打卡时间:"+line['每日每周']+\
                                  "\n打卡次数:"+line['打卡次数']+"\n是否打卡:"+str(line['是否打卡'])+\
                                   "\n激励自己的话:"+line['激励自己的话']+"\n打卡时间:"+line['打卡时间'])+"\n\n"
                elif line['每日每周']=='每周':
                    txtHabit = str("创建时间为:" + line['创建时间'] + "\n习惯名称:" + line['习惯名称'] + \
                                   "\n在一天什么时候执行:" + line['在一天什么时候'] + "\n打卡时间:" + line['每日每周'] + \
                                   "\n打卡次数:" + line['打卡次数']+ "\t在一周什么时候执行:"+line['在一周什么时候'] +\
                                   "\n是否打卡:" + str(line['是否打卡']) + "\n激励自己的话:"+line['激励自己的话']+\
                                   "\n打卡时间:"+line['打卡时间']) + "\n\n"
                self.txtHabit.AppendText(txtHabit)
        except:pass
#显示计划信息#
class Panel1(UserPanel,Singleton):
    def __init__(self,parent,act):
        self.act = act
        self.planCount = 0  # 计划个数
        super(Panel1, self).__init__(parent, act)
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "显示计划信息", (200, 30))
        lblTitle.SetFont(lblTitleFont)

        btnShow = wx.Button(self, -1, "刷新", (420, 30))
        btnShow.SetFont(lblFont)

        try:
            self.path = "C:\\PlanHelper\\" + self.act + "\\plan\\"  # 获取路径
            self.list = []
        except:
            pass

        PlanBatRead = open(self.path + "execute.txt", 'r', encoding="utf-8")  # 读取计划
        planBatLines = PlanBatRead.readlines()  # 读取
        for line in planBatLines:
            self.planCount = self.planCount + 1  # 计划个数
            count = self.planCount
            line = eval(line)
            self.list.append(str(str(count)+ "--创建时间:"+ line['创建时间'] + "====计划名称: " + line['计划名称'] + "====是否打卡: " + str(line['是否打卡'])))
        self.listBox = wx.ListBox(self, -1, (1, 100), (570, 380), self.list, wx.LB_SINGLE)

        self.Bind(wx.EVT_BUTTON, self.BtnClick, btnShow)

    def BtnClick(self,e):
        try:
            list1 = []
            self.planCount = 0  # 计划个数
            self.listBox.Clear()
            PlanBatRead = open(self.path + "execute.txt", 'r', encoding="utf-8")  # 读取计划
            planBatLines = PlanBatRead.readlines()  # 读取
            for line in planBatLines:
                self.planCount = self.planCount + 1  # 计划个数
                count = self.planCount
                line = eval(line)
                list1.append(str(str(count)+ "--创建时间:"+ line['创建时间'] + "====计划名称: " + line['计划名称'] + "====是否打卡: " + str(line['是否打卡'])))
            self.listBox.Set(list1)#重新设置列表框
        except:pass
#显示习惯信息#
class Panel2(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel2, self).__init__(parent,act)
        self.act = act
        self.habitCount = 0
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "显示习惯信息", (180, 30))
        lblTitle.SetFont(lblTitleFont)

        btnShow = wx.Button(self, -1, "刷新", (420, 30))
        btnShow.SetFont(lblFont)

        try:
            self.path = "C:\\PlanHelper\\" + self.act + "\\habit\\"  # 获取路径
            self.list = []
        except:
            pass
        try:
            HabitBatRead = open(self.path + "execute.txt", 'r', encoding="utf-8")  # 读取习惯
            habitBatLines = HabitBatRead.readlines()  # 读取
            for line in habitBatLines:
                self.habitCount = self.habitCount + 1  # 加
                count = self.habitCount
                line = eval(line)
                self.list.append(str(str(count) + "--创建时间"+line['创建时间'] +"====习惯名称: " + line['习惯名称'] + "====是否打卡: " + str(line['是否打卡'])))
            self.listBox = wx.ListBox(self, -1, (1, 100), (570, 380), self.list, wx.LB_SINGLE)
        except:
            pass
        self.Bind(wx.EVT_BUTTON, self.BtnClick, btnShow)
    def BtnClick(self,e):
        self.habitCount = 0  # 习惯个数
        list1 = []
        self.listBox.Clear()
        HabitBatRead = open(self.path + "execute.txt", 'r', encoding="utf-8")  # 读取计划
        habitBatLines = HabitBatRead.readlines()  # 读取
        for line in habitBatLines:
            self.habitCount = self.habitCount + 1#加
            count = self.habitCount
            line = eval(line)
            list1.append(str(str(count) + "--创建时间:"+line['创建时间'] +"====习惯名称: " + line['习惯名称'] + "====是否打卡: " + str(line['是否打卡'])))
        self.listBox.Set(list1)
#计划打卡  未实现打卡
class Panel3(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel3, self).__init__(parent,act)
        self.act = act
        self.planCount = 0  # 计划个数
        self.getNowTime = str(time.strftime("%Y-%m-%d", time.localtime(time.time())))  # 获取当前时间
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "计划打卡", (200, 30))
        lblTitle.SetFont(lblTitleFont)

        # btnShow = wx.Button(self, -1, "刷新", (420, 30))
        # btnShow.SetFont(lblFont)

        try:
            self.path = "C:\\PlanHelper\\" + self.act + "\\plan\\"  # 获取路径
            self.list = []
        except:pass

        PlanBatRead = open(self.path + "finish.txt", 'r', encoding="utf-8")  # 读取计划
        self.planBatLines = PlanBatRead.readlines()  # 读取
        for line in self.planBatLines:
            self.planCount = self.planCount + 1  # 计划个数
            count = self.planCount
            line = eval(line)
            self.list.append(str(str(count) + "--计划名称: " + line['计划名称'] + "=====是否打卡: " + str(line['是否打卡'])))
        self.listBox = wx.ListBox(self, -1, (1, 100), (570, 380), self.list, wx.LB_SINGLE)

        self.Bind(wx.EVT_LISTBOX_DCLICK,self.ListClick,self.listBox)
        # self.Bind(wx.EVT_BUTTON, self.BtnClick, btnShow)
    # def BtnClick(self,e):
    #     try:
    #         self.planCount = 0
    #         try:
    #             self.path = "C:\\PlanHelper\\" + self.act + "\\plan\\"  # 获取路径
    #             self.list = []
    #         except:
    #             pass
    #
    #         PlanBatRead = open(self.path + "finish.txt", 'r', encoding="utf-8")  # 读取计划
    #         self.planBatLines = PlanBatRead.readlines()  # 读取
    #         for line in self.planBatLines:
    #             self.planCount = self.planCount + 1  # 计划个数
    #             count = self.planCount
    #             line = eval(line)
    #             self.list.append(str(str(count) + "--计划名称: " + line['计划名称'] + "=====是否打卡: " + str(line['是否打卡'])))
    #         self.listBox = wx.ListBox(self, -1, (1, 100), (570, 380), self.list, wx.LB_SINGLE)
    #         self.Bind(wx.EVT_LISTBOX_DCLICK, self.ListClick, self.listBox)
    #     except:pass
    #未实现
    def ListClick(self,e):
        # try:
        self.planCount = 0  # 计划个数
        clickCount = str(int(self.listBox.GetSelection()) + 1)  # 获取当前点击按钮的编号
        PlanBatRead = open(self.path + "finish.txt",'r',encoding="utf-8")
        planBatLines = PlanBatRead.readlines()
        listPlanBatLines = list(planBatLines)
        for line in planBatLines:
            line = eval(line)
            self.planCount = self.planCount + 1  # 计划个数
            count = str(self.planCount)
            if clickCount == count: #判断是否点击的是同一个按钮
                mdg = wx.MessageDialog(self,"是否打卡?","打卡",wx.YES_NO)
                if mdg.ShowModal() == wx.ID_YES:#如果打卡
                    list1 = list(line.values())
                    if list1[6] != self.getNowTime:#如果打卡时间！=当前时间,就打卡
                        listL = []
                        line['是否打卡'] = True  # 设置
                        line['打卡时间'] = self.getNowTime  # 设置
                        PlanBatFinishWrite = open(self.path + "finish.txt", 'a+', encoding="utf-8")  # 写入计划
                        PlanBatFinishWrite.write(str(line) + "\n")  # 重新写入

                        PlanBatFinishRead = open(self.path + "finish.txt", 'r', encoding="utf-8")  # 读取计划
                        PlanReadLines = PlanBatFinishRead.readlines()  # 读取
                        listL.append(str(str(count) + "--计划名称: " + line['计划名称'] + "=====是否打卡: " + str(line['是否打卡'])))
                        self.listBox.InsertItems(listL, int(clickCount))  # 插入
                        self.listBox.Delete(int(clickCount) - 1)
        # except:pass
#习惯打卡  未实现打卡
class Panel4(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel4, self).__init__(parent,act)
        self.act = act
        self.habitCount = 0 #习惯个数
        self.getNowTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))  # 获取当前时间
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "习惯打卡", (200, 30))
        lblTitle.SetFont(lblTitleFont)

        # btnShow = wx.Button(self, -1, "刷新", (420, 30))
        # btnShow.SetFont(lblFont)

        try:
            self.path = "C:\\PlanHelper\\" + self.act + "\\habit\\"  # 获取路径
            self.list = []
        except:pass
        try:
            HabitBatRead = open(self.path + "finish.txt", 'r', encoding="utf-8")  # 读取习惯
            habitBatLines = HabitBatRead.readlines()  # 读取
            for line in habitBatLines:
                self.habitCount = self.habitCount + 1#加
                count = self.habitCount
                line = eval(line)
                self.list.append(str(str(count) +"--习惯名称: " + line['习惯名称'] + "=====是否打卡: " + str(line['是否打卡'])))
            self.listBox = wx.ListBox(self, -1, (1, 100), (570, 380), self.list, wx.LB_SINGLE)
        except:pass

        # self.Bind(wx.EVT_BUTTON, self.BtnClick, btnShow)
        self.Bind(wx.EVT_LISTBOX_DCLICK,self.ListClick,self.listBox)
    # def BtnClick(self,e):
    #     self.habitCount = 0  # 习惯个数
    #     list1 = []
    #     self.listBox.Clear()
    #     HabitBatRead = open(self.path + "finish.txt", 'r', encoding="utf-8")  # 读取计划
    #     habitBatLines = HabitBatRead.readlines()  # 读取
    #     for line in habitBatLines:
    #         self.habitCount = self.habitCount + 1#加
    #         count = self.habitCount
    #         line = eval(line)
    #         list1.append(str(str(count) +"--习惯名称: " + line['习惯名称'] + "=====是否打卡: " + str(line['是否打卡'])))
    #     self.listBox.Set(list1)
    #未实现
    def ListClick(self,e):
        self.habitCount = 0  # 计划个数
        clickCount = str(int(self.listBox.GetSelection()) + 1)  # 获取当前点击按钮的编号
        HabitBatRead = open(self.path + "finish.txt", 'r', encoding="utf-8")  # 读取习惯
        habitBatLines = HabitBatRead.readlines()
        for line in habitBatLines:
            line = eval(line)
            self.habitCount = self.habitCount + 1  # 计划个数
            count1 = str(self.habitCount)
            if clickCount == count1:  # 判断是否点击的是同一个按钮
                mdg = wx.MessageDialog(self, "是否打卡?", "打卡", wx.YES_NO)
                if mdg.ShowModal() == wx.ID_YES:  # 如果打卡
                    list1 = list(line.values())
                    if list1[6] != self.getNowTime:  # 如果打卡时间！=当前时间,就打卡
                        listL = []
                        line['是否打卡'] = True  # 设置
                        line['打卡时间'] = self.getNowTime  # 设置
                        HabitBatFinishWrite = open(self.path + "finish.txt", 'a+', encoding="utf-8")  # 写入计划
                        HabitBatFinishWrite.write(str(line) + "\n")  # 重新写入

                        HabitBatFinishRead = open(self.path + "finish.txt", 'r', encoding="utf-8")  # 读取计划
                        HabitReadLines = HabitBatFinishRead.readlines()  # 读取
                        listL.append(str(str(count1) + "--习惯名称: " + line['习惯名称'] + "=====是否打卡: " + str(line['是否打卡'])))
                        self.listBox.InsertItems(listL, int(clickCount))  # 插入
                        self.listBox.Delete(int(clickCount) - 1)

#账单#
class Panel5(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel5, self).__init__(parent, act)
        self.act = act
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblTitle = wx.StaticText(self, -1, "账单", (245, 30))
        lblTitle.SetFont(lblTitleFont)

        btnShow = wx.Button(self,-1,"刷新",(380,30))
        btnShow.SetFont(lblFont)

        lblIn = wx.StaticText(self, -1, "收入", (255, 80))
        lblIn.SetFont(lblFont)
        self.txtIn = wx.TextCtrl(self, -1, "", (1, 110), (570, 150), wx.TE_MULTILINE|wx.TE_READONLY)

        lblOut = wx.StaticText(self, -1, "支出", (255, 270))
        lblOut.SetFont(lblFont)
        self.txtOut = wx.TextCtrl(self, -1, "", (1, 300), (570, 150), wx.TE_MULTILINE|wx.TE_READONLY)

        self.Bind(wx.EVT_BUTTON,self.BtnClick,btnShow)
    def BtnClick(self,e):
        self.txtIn.SetValue("")
        self.txtOut.SetValue("")
        # 添加事件
        try:
            path = "C:\\PlanHelper\\" + self.act + "\\bill\\"  # 获取路径
        except:pass
        try:
            inComeRead = open(path + "billIn.txt", "r", encoding="utf-8")  # 读取收入
            inlines = inComeRead.readlines()
            for line in inlines:  # 逐行读取
                line = eval(line)  # 字符串转为字典
                txtShowIn = str(line['当前时间'] + "\t你 " + line['收入名称'] + "\t收入 " + line['收入金额'] + "元") + "\n"
                self.txtIn.AppendText(txtShowIn)
        except:
            pass
        try:
            outMoneyRead = open(path + "billOut.txt", "r", encoding="utf-8")  # 读取支出
            outlines = outMoneyRead.readlines()
            for line in outlines:  # 逐行读取
                line = eval(line)  # 字符串转为字典
                txtShowOut = str(line['当前时间'] + "\t你 " + line['支出名称'] + "\t支出 " + line['支出金额'] + "元") + "\n"
                self.txtOut.AppendText(txtShowOut)
        except:
            pass
#创建计划#
class Panel6(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel6, self).__init__(parent,act)
        self.act = act
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "创建计划", (215, 30))
        lblTitle.SetFont(lblTitleFont)

        lblPlanName = wx.StaticText(self, -1, "计划名称:", (40, 83))
        lblPlanName.SetFont(lblFont)
        self.txtPlanName = wx.TextCtrl(self, -1, "自定义名称", (40, 112), (473, 25))

        lblPlanDays = wx.StaticText(self, -1, "计划完成天数:", (40, 155))
        lblPlanDays.SetFont(lblFont)
        self.btn7 = wx.Button(self, -1, "7天", (60, 184), (40, 40))
        self.btn21 = wx.Button(self, -1, "21天", (120, 184), (40, 40))
        self.btn30 = wx.Button(self, -1, "30天", (180, 184), (40, 40))
        self.btn100 = wx.Button(self, -1, "100天", (240, 184), (40, 40))

        lblSelfDays = wx.StaticText(self, -1, "自定义天数:===============", (40, 255))
        lblSelfDays.SetFont(lblFont)
        self.txtSelfDays = wx.TextCtrl(self, -1, "7", (360, 255), (80, 25), wx.TE_CENTER)
        self.txtSelfDays.SetFont(lblFont)

        lblRelaxDays = wx.StaticText(self, -1, "休息天数:=================", (40, 300))
        lblRelaxDays.SetFont(lblFont)
        self.txtRelaxDays = wx.TextCtrl(self, -1, "2", (360, 300), (80, 25), wx.TE_CENTER)
        self.txtRelaxDays.SetFont(lblFont)

        lblFirstBatTime = wx.StaticText(self, -1, "首次签到时间:", (40, 350))
        lblFirstBatTime.SetFont(lblFont)
        firstBatTimeList = ["今天", "明天"]
        self.rbxFirstBatTime = wx.RadioBox(self, -1, pos=(80, 380), choices=firstBatTimeList)
        self.rbxFirstBatTime.SetSelection(0)

        self.btnCreatePlan = wx.Button(self, -1, "创建计划", (220, 440), (125, 30))
        self.btnCreatePlan.SetFont(lblFont)

        self.Bind(wx.EVT_BUTTON, self.OnClick6Btn1, self.btn7)
        self.Bind(wx.EVT_BUTTON, self.OnClick6Btn2, self.btn21)
        self.Bind(wx.EVT_BUTTON, self.OnClick6Btn3, self.btn30)
        self.Bind(wx.EVT_BUTTON, self.OnClick6Btn4, self.btn100)
        self.Bind(wx.EVT_BUTTON, self.OnClick6BtnCreate, self.btnCreatePlan)

    def OnClick6BtnCreate(self, e):
        try:
            path = "C:\\PlanHelper\\" + self.act + "\\plan\\"  # 获取路径
            # print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
            getRbxIndex = str(self.rbxFirstBatTime.GetSelection())
            # print(getRbxIndex)
            getNowTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))  # 获取当前时间
            getPlanName = self.txtPlanName.GetValue()  # 获取计划名称
            getSelfDays = self.txtSelfDays.GetValue()  # 获取自定义天数
            getRelaxDays = self.txtRelaxDays.GetValue()  # 获取休息天数
            getFirstBatTime = str(getRbxIndex)  # 获取首次签到
            if getFirstBatTime == "0":
                firstBatTimerbx = str(getNowTime)  # 获取首次签到时间
            elif getFirstBatTime == "1":
                day = str(int(time.strftime("%d", time.localtime(time.time()))) + 1)
                firstBatTimerbx = str(time.strftime("%Y-%m", time.localtime(time.time()))) + "-" + day
            else:
                pass
            # 写入计划
            # 创建时间-计划名称-自定义天数-休息天数-第一次打卡-是否打卡-打卡时间
            planDict = str({"创建时间": getNowTime, "计划名称": getPlanName, "自定义天数": getSelfDays, "休息天数": getRelaxDays,
                            "首次打卡时间": firstBatTimerbx, "是否打卡": False,"打卡时间":""}) + "\n"
            planWrite = open(path + "execute.txt", "a+", encoding="utf-8")
            planWrite.write(planDict)
            planDict1 = str({"创建时间": getNowTime, "计划名称": getPlanName, "自定义天数": getSelfDays, "休息天数": getRelaxDays,
                            "首次打卡时间": firstBatTimerbx, "是否打卡": False,"打卡时间":""}) + "\n"
            planfinishWrite = open(path + "finish.txt", "a+", encoding="utf-8")
            planfinishWrite.write(planDict1)
            wx.MessageBox("创建成功!", "提示")
        except:
            pass

    def OnClick6Btn1(self, e):
        self.txtSelfDays.SetValue("7")
        self.txtRelaxDays.SetValue("2")

    def OnClick6Btn2(self, e):
        self.txtSelfDays.SetValue("21")
        self.txtRelaxDays.SetValue("5")

    def OnClick6Btn3(self, e):
        self.txtSelfDays.SetValue("30")
        self.txtRelaxDays.SetValue("6")

    def OnClick6Btn4(self, e):
        self.txtSelfDays.SetValue("100")
        self.txtRelaxDays.SetValue("20")
#创建习惯#
class Panel7(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel7, self).__init__(parent,act)
        self.act = act
        try:
            lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
            lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

            lblTitle = wx.StaticText(self,-1,"创建习惯",(215,30))
            lblTitle.SetFont(lblTitleFont)

            lblName = wx.StaticText(self,-1,"给习惯命名:",(21,83))
            lblName.SetFont(lblFont)
            self.txtInputName = wx.TextCtrl(self,-1,"自定义习惯",(165,80),(350,30))
            self.txtInputName.SetFont(lblFont)

            lblDayTime = wx.StaticText(self,-1,"在一天什么时候:",(21,126))
            lblDayTime.SetFont(lblFont)
            rbxDayTimeList = ["任意时间  ","起床之后  ","晨间习惯  ","中午时分  ","傍晚时分  "]
            self.rbxDayTime = wx.RadioBox(self,-1,pos=(145,150),choices=rbxDayTimeList,style=wx.RA_SPECIFY_COLS)
            self.rbxDayTime.SetSelection(0)

            lblDayBat = wx.StaticText(self, -1, "设置每日打卡次数:", (21, 215))
            lblDayBat.SetFont(lblFont)
            rbxDayBatList = ["每日 ","每周 "]
            self.rbxDayBat = wx.RadioBox(self,-1,pos=(220,200),choices=rbxDayBatList)
            self.lblDayBatCount = wx.StaticText(self, -1, "每日:", (390, 215))
            self.lblDayBatCount.SetFont(lblFont)
            self.txtInputDayBatCount = wx.TextCtrl(self,-1,"1",(450,215),(50,25),wx.TE_CENTER)
            lblDayBatCountEnd = wx.StaticText(self,-1,"次",(510,215))
            lblDayBatCountEnd.SetFont(lblFont)

            lblWeekTime = wx.StaticText(self, -1, "在一周什么时候:", (21, 260))
            lblWeekTime.SetFont(lblFont)
            rbxWeekList = ["周一","周二","周三","周四","周五","周六","周日"]
            self.rbxWeek = wx.RadioBox(self,-1,pos=(110,290),choices=rbxWeekList)
            self.rbxWeek.Disable()

            lblSpeak = wx.StaticText(self, -1, "写一句激励自己的话:", (21, 360))
            lblSpeak.SetFont(lblFont)
            self.txtSpeak = wx.TextCtrl(self,-1,"",(80,400),(430,25))

            self.btnCreateHabit = wx.Button(self,-1,"创建习惯",(220,440),(135,30))
            self.btnCreateHabit.SetFont(lblFont)

            self.Bind(wx.EVT_BUTTON,self.OnClick7BtnCreate,self.btnCreateHabit)
            self.Bind(wx.EVT_RADIOBOX,self.OnRadioBtn,self.rbxDayBat)
        except:
            pass
    def OnClick7BtnCreate(self,e):
        try:
            path = "C:\\PlanHelper\\"+ self.act +"\\habit\\"
            getDayTimeIndex = self.rbxDayTime.GetSelection()#获取一天时间段
            getNowTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))  # 获取当前时间
            getHabitName = self.txtInputName.GetValue()#获取习惯名称
            getDayTimerbx = str(getDayTimeIndex)#在一天什么时候
            if getDayTimerbx == "0":
                txt1 = "任意时间"
            elif getDayTimerbx == "1":
                txt1 = "起床之后"
            elif getDayTimerbx == "2":
                txt1 = "晨间习惯"
            elif getDayTimerbx == "3":
                txt1 = "中午时分"
            elif getDayTimerbx == "4":
                txt1 = "傍晚时分"
            else:pass
            getDayBatCountrbx = str(self.rbxDayBat.GetSelection())  # 设置每日打卡次数
            if getDayBatCountrbx == "0":
                txt2 = "每日"
            elif getDayBatCountrbx == "1":
                txt2 = "每周"
            else:pass
            getDayBatCounttxt = int(self.txtInputDayBatCount.GetValue())#获取打卡次数
            if getDayBatCountrbx == "0":
                self.lblDayBatCount.SetLabel("每日:")
                self.rbxWeek.Disable()
                if getDayBatCounttxt < 1 or getDayBatCounttxt > 1:
                    self.txtInputDayBatCount.SetValue("1")
            if getDayBatCountrbx == "1":
                self.lblDayBatCount.SetLabel("每周:")
                self.rbxWeek.Enable()
                if getDayBatCounttxt < 1:
                    self.txtInputDayBatCount.SetValue("1")
                elif getDayBatCounttxt > 7:
                    self.txtInputDayBatCount.SetValue("7")
            #在一周什么时候
            getWeek = str(self.rbxWeek.GetSelection())
            if getWeek == "0":
                txt3 = "周一"
            elif getWeek == "1":
                txt3 = "周二"
            elif getWeek == "2":
                txt3 = "周三"
            elif getWeek == "3":
                txt3 = "周四"
            elif getWeek == "4":
                txt3 = "周五"
            elif getWeek == "5":
                txt3 = "周六"
            elif getWeek == "6":
                txt3 = "周日"
            else:pass
            #获取激励自己的话
            getSpeak = str(self.txtSpeak.GetValue())
            #创建时间-习惯名称-在一天什么时候-每日每周-打卡次数为1-在一周什么时候-激励自己的话-是否打卡
            habitDict = str({"创建时间":getNowTime,"习惯名称":getHabitName,"在一天什么时候":txt1,"每日每周":txt2,
                             "打卡次数":self.txtInputDayBatCount.GetValue(),"在一周什么时候":txt3,
                             "激励自己的话":getSpeak,"是否打卡":False,"打卡时间":""})+"\n"
            habitWrite = open(path+"execute.txt","a+",encoding="utf-8")
            habitWrite.write(habitDict)

            habitDict1 = str({"创建时间": getNowTime, "习惯名称": getHabitName, "在一天什么时候": txt1, "每日每周": txt2,
                             "打卡次数": self.txtInputDayBatCount.GetValue(), "在一周什么时候": txt3, "激励自己的话": getSpeak,
                             "是否打卡": False,"打卡时间:":""}) + "\n"
            habitfinishWrite = open(path + "finish.txt", "a+", encoding="utf-8")
            habitfinishWrite.write(habitDict1)
            wx.MessageBox("创建成功!","提示")
        except:
            pass
    def OnRadioBtn(self,e):
        try:#设置每日打卡次数
            getDayBatCountrbx = str(self.rbxDayBat.GetSelection())  # 设置每日打卡次数
            if getDayBatCountrbx == "0":
                self.lblDayBatCount.SetLabel("每日:")
                self.rbxWeek.Disable()
                if self.txtInputDayBatCount.GetValue() < "1" or self.txtInputDayBatCount.GetValue() > "1":
                    self.txtInputDayBatCount.SetValue("1")
            if getDayBatCountrbx == "1":
                self.lblDayBatCount.SetLabel("每周:")
                self.rbxWeek.Enable()
                if self.txtInputDayBatCount.GetValue() < "1" or self.txtInputDayBatCount.GetValue() > "1":
                    self.txtInputDayBatCount.SetValue("1")

        except:
            pass
#收入#
class Panel8(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel8, self).__init__(parent,act)
        self.act = act
        try:
            lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
            lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

            lblTitle = wx.StaticText(self, -1, "收入", (250, 30))
            lblTitle.SetFont(lblTitleFont)

            lblName = wx.StaticText(self, -1, "收入名称:", (100, 175))
            lblName.SetFont(lblFont)
            self.txtInName = wx.TextCtrl(self, -1, "", (270, 175), (200, 25))

            lblName = wx.StaticText(self, -1, "收入金额(元):", (100, 250))
            lblName.SetFont(lblFont)
            self.txtInMoney = wx.TextCtrl(self, -1, "", (270, 250), (200, 25))

            self.btnSureIn = wx.Button(self, -1, "确定", (210, 360), (125, 35))
            self.btnSureIn.SetFont(lblFont)

            self.Bind(wx.EVT_BUTTON, self.OnInCome, self.btnSureIn)
        except:
            pass
    def OnInCome(self, e):
        try:
            path = "C:\\PlanHelper\\" + self.act + "\\bill\\"  # 获取路径
            getNowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 获取当前时间
            getInName = str(self.txtInName.GetValue())  # 获取收入名称
            getInMoney = str(self.txtInMoney.GetValue())  # 获取收入金额
            InComeDict = str({"当前时间": getNowTime, "收入名称": getInName, "收入金额": getInMoney}) + "\n"
            # 写入
            try:
                if getInName != "" and getInMoney != "":
                    if getInMoney.isdigit():
                        InComeWrite = open(path + "billIn.txt", "a+", encoding="utf-8")
                        InComeWrite.write(InComeDict)
                        wx.MessageBox("写入成功!", "提示")
                        self.txtInName.SetValue("")
                        self.txtInMoney.SetValue("")
                    else:
                        wx.MessageBox("写入失败!\n金额必须为数字!", "提示")
                else:
                    wx.MessageBox("写入失败!\n不能为空!", "提示")
            except:
                pass
        except:
            pass
#支出#
class Panel9(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel9, self).__init__(parent,act)
        self.act = act
        try:
            lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
            lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

            lblTitle = wx.StaticText(self, -1, "支出", (250, 30))
            lblTitle.SetFont(lblTitleFont)

            lblName = wx.StaticText(self, -1, "支出名称:", (100, 175))
            lblName.SetFont(lblFont)
            self.txtOutName = wx.TextCtrl(self, -1, "", (270, 175), (200, 25))

            lblName = wx.StaticText(self, -1, "支出金额(元):", (100, 250))
            lblName.SetFont(lblFont)
            self.txtOutMoney = wx.TextCtrl(self, -1, "", (270, 250), (200, 25))

            self.btnSureOut = wx.Button(self, -1, "确定", (210, 360), (125, 35))
            self.btnSureOut.SetFont(lblFont)

            self.Bind(wx.EVT_BUTTON, self.OnOutMoney, self.btnSureOut)
        except:
            pass

    def OnOutMoney(self, e):
        try:
            path = "C:\\PlanHelper\\" + self.act + "\\bill\\"  # 获取路径
            getNowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 获取当前时间
            getOutName = str(self.txtOutName.GetValue())  # 获取支出名称
            getOutMoney = str(self.txtOutMoney.GetValue())  # 获取支出金额
            OutMoneyDict = str({"当前时间": getNowTime, "支出名称": getOutName, "支出金额": getOutMoney}) + "\n"
            # 写入
            try:
                if getOutName != "" and getOutMoney != "":
                    if getOutMoney.isdigit():
                        OutMoneyWrite = open(path + "billOut.txt", "a+", encoding="utf-8")
                        OutMoneyWrite.write(OutMoneyDict)
                        wx.MessageBox("写入成功!", "提示")
                        self.txtOutName.SetValue("")
                        self.txtOutMoney.SetValue("")
                    else:
                        wx.MessageBox("写入失败!\n金额必须为数字!", "提示")
                else:
                    wx.MessageBox("写入失败!\n不能为空!", "提示")
            except:
                pass
        except:
            pass
#个人账户#
class Panel10(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel10, self).__init__(parent,act)
        self.act = act
        path = "C:\\PlanHelper\\" + self.act + "\\"  # 获取路径
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "个人账户", (215, 30))
        lblTitle.SetFont(lblTitleFont)

        lblaccount = wx.StaticText(self,-1,"账号:",(120,130))
        lblaccount.SetFont(lblFont)
        self.txtaccount = wx.TextCtrl(self,-1,"",(210,130),(150,25),wx.TE_READONLY)

        lblName = wx.StaticText(self, -1, "昵称:", (120, 180))
        lblName.SetFont(lblFont)
        self.txtName = wx.TextCtrl(self, -1, "", (210, 180), (150, 25))
        self.txtName.Disable()
        self.cbxName = wx.CheckBox(self,-1,"修改",(380,185))

        lblWrite = wx.StaticText(self, -1, "签名:", (120, 230))
        lblWrite.SetFont(lblFont)
        self.txtWrite = wx.TextCtrl(self, -1, "", (200, 230), (260, 25))
        self.txtWrite.Disable()
        self.cbxWrite = wx.CheckBox(self, -1, "修改", (480, 235))

        self.btnSave = wx.Button(self,-1,"保存",(220,300))
        self.btnSave.SetFont(lblFont)
        #昵称，签名
        selfActTxt = open(path + "self.txt", 'r', encoding="utf-8")  # 个人账户
        selfLine = eval(selfActTxt.readline())
        for name,write in selfLine.items():
            self.getTxtName = str(name)#昵称
            self.getTxtWrite = str(write)#签名
            self.txtName.SetValue(str(name))
            self.txtWrite.SetValue(str(write))
        #账号
        account = open(path+"actpwd.txt", "r", encoding="utf-8")
        line = eval(str(account.readline()))
        for act,pwd in line.items():
            self.txtaccount.SetValue(str(act))#获取账号
        self.Bind(wx.EVT_BUTTON,self.BtnSaveClick,self.btnSave)
        self.Bind(wx.EVT_CHECKBOX,self.CbxName,self.cbxName)
        self.Bind(wx.EVT_CHECKBOX,self.CbxWrite,self.cbxWrite)
    def BtnSaveClick(self,e):
        path = "C:\\PlanHelper\\" + self.act + "\\self.txt"  # 获取路径
        selfFile = open(path,'w',encoding="utf-8")
        txtname = str(self.txtName.GetValue())
        txtwrite = str(self.txtWrite.GetValue())
        selfDict = str({str(txtname):str(txtwrite)})
        selfFile.write(selfDict)
        wx.MessageBox("保存成功!","提示")

        self.txtName.Disable()
        self.txtWrite.Disable()
        self.cbxName.SetValue(False)
        self.cbxWrite.SetValue(False)
    def CbxName(self,e):
        cbn = e.GetEventObject()
        if cbn.GetValue():
            self.txtName.Enable()
        else:
            self.txtName.Disable()
    def CbxWrite(self,e):
        cbw = e.GetEventObject()
        if cbw.GetValue():
            self.txtWrite.Enable()
        else:
            self.txtWrite.Disable()
#安全中心#
class Panel11(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel11, self).__init__(parent,act)
        self.act = act
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "安全中心", (215, 30))
        lblTitle.SetFont(lblTitleFont)

        lblold= wx.StaticText(self, -1, "旧密码:", (120, 130))
        lblold.SetFont(lblFont)
        self.txtold = wx.TextCtrl(self, -1, "", (210, 130), (200, 25),wx.TE_PASSWORD)

        lblNew = wx.StaticText(self, -1, "新密码:", (120, 180))
        lblNew.SetFont(lblFont)
        self.txtNew = wx.TextCtrl(self, -1, "", (210, 180), (200, 25),wx.TE_PASSWORD)

        lblSureNew = wx.StaticText(self, -1, "确认新密码:", (75, 230))
        lblSureNew.SetFont(lblFont)
        self.txtSureNew = wx.TextCtrl(self, -1, "", (210, 230), (200, 25),wx.TE_PASSWORD)

        self.btnUpdate = wx.Button(self, -1, "确定修改", (240, 280))
        self.Bind(wx.EVT_BUTTON,self.BtnSurePwd,self.btnUpdate)
    def BtnSurePwd(self,e):
        path = "C:\\PlanHelper\\" + self.act + "\\actpwd.txt"  # 获取路径
        actpwd = open(path, "r", encoding="utf-8")#账号密码
        line = eval(str(actpwd.readline()))
        for act, pwd in line.items():
            self.actNum = str(act)#获取旧帐号
            self.pwdNum = str(pwd)#获取旧密码
        if self.txtold !="" and self.txtNew != "" and self.txtSureNew !="":
            if self.pwdNum == str(self.txtold.GetValue()):#旧密码相同
                if str(self.txtNew.GetValue()).isalnum() and len(str(self.txtNew.GetValue())) >= 10 and \
                        str(self.txtSureNew.GetValue()).isalnum() and len(str(self.txtSureNew.GetValue())) >= 10:#判断新密码是否为数字和字母组合
                    if str(self.txtNew.GetValue()) == str(self.txtSureNew.GetValue()):#如果新密码相同
                        actpwd = open(path, "w", encoding="utf-8")
                        newActPwdDict = str({str(self.actNum):str(self.txtSureNew.GetValue())})
                        actpwd.write(newActPwdDict)#写入新密码
                        wx.MessageBox("修改成功!","提示")
                        self.txtold.SetValue("")
                        self.txtNew.SetValue("")
                        self.txtSureNew.SetValue("")
                    else:
                        wx.MessageBox("新密码不相同!","错误")
                        self.txtold.SetValue("")
                        self.txtNew.SetValue("")
                        self.txtSureNew.SetValue("")
                else:
                    wx.MessageBox("密码为数字或字母组合\n长度大于10!","错误")
                    self.txtold.SetValue("")
                    self.txtNew.SetValue("")
                    self.txtSureNew.SetValue("")
            else:
                wx.MessageBox("密码输入错误!","错误")
                self.txtold.SetValue("")
                self.txtNew.SetValue("")
                self.txtSureNew.SetValue("")
        else:
            wx.MessageBox("密码不能为空!","错误")
#使用帮助#
class Panel12(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel12, self).__init__(parent,act)
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "使用帮助", (215, 30))
        lblTitle.SetFont(lblTitleFont)

        txt = wx.TextCtrl(self, -1, "", (1, 110), (570, 350), wx.TE_MULTILINE |
                                 wx.TE_READONLY|wx.TE_CENTER)
        txt.SetValue("无")
#关于我们#
class Panel13(UserPanel,Singleton):
    def __init__(self,parent,act):
        super(Panel13, self).__init__(parent,act)
        lblTitleFont = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        lblFont = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        lblTitle = wx.StaticText(self, -1, "关于我们", (215, 30))
        lblTitle.SetFont(lblTitleFont)

        txt = wx.TextCtrl(self, -1, "", (1, 110), (570, 350), wx.TE_MULTILINE |
                          wx.TE_READONLY | wx.TE_CENTER)
        txt.SetValue("作者:jack邹建\n心得:闲着没事儿干--写着玩儿的")

#首页界面面板类
class FirstHeadFrame(wx.Frame,Singleton):
    def __init__(self,act):
        # self.MenuFont = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        wx.Frame.__init__(self, parent=None, size=(592, 550),
                          title="计划助手",
                          style=wx.MINIMIZE_BOX | wx.CAPTION |
                                wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.CLIP_CHILDREN)
        self.panel = wx.Panel(self)
        self.InitUI()
        self.actNum = act
        self.Center()
        self.ListPanel = [
            Panel0(self.panel,self.actNum),Panel1(self.panel,self.actNum),Panel2(self.panel,self.actNum),Panel3(self.panel,self.actNum),
            Panel4(self.panel, self.actNum),Panel5(self.panel,self.actNum),Panel6(self.panel,self.actNum),Panel7(self.panel,self.actNum),
            Panel8(self.panel, self.actNum),Panel9(self.panel,self.actNum),Panel10(self.panel,self.actNum),Panel11(self.panel,self.actNum),
            Panel12(self.panel, self.actNum),Panel13(self.panel,self.actNum)
        ]
        for item in range(0,14):
            self.ListPanel[item].Show(False)
        self.ListPanel[0].Show(True)
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
        self.menuBar.Append(self.menuWriteBill,"&记账")
        self.menuBar.Append(self.menuMySlef, "&我的")

        self.SetMenuBar(self.menuBar)

        try:

            # item组件列表
            self.itemList = [
                self.itemShowAllPlan, self.itemShowPlanInfo, self.itemShowHabitInfo, self.itemPlanBat,
                self.itemHabitBat, self.itemBill,
                self.itemCreatePlan, self.itemCreateHabit,
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
                self.OnClick12,self.OnClick13
            ]
        except:
            pass
        return
    def IsShowPanel(self,num):
        for item in range(0,14):
            if item == num:
                self.ListPanel[item].Show(True)
            else:
                self.ListPanel[item].Show(False)
    #关闭
    def OnClose(self,e):
        dlg = wx.MessageDialog(self,u"确定退出?",u"提示",wx.YES_NO|wx.ICON_INFORMATION)
        if dlg.ShowModal() == wx.ID_YES:
            sys.exit()
        else:
            pass
    # 给所有item添加事件
    def OnAllClick(self):
        for item in range(0, 14):
            self.Bind(wx.EVT_MENU, self.OnClickList[item], self.itemList[item])

    #显示所有计划
    def OnClick0(self,e):
        self.IsShowPanel(0)
    #显示计划信息
    def OnClick1(self,e):
        self.IsShowPanel(1)
    #显示习惯信息
    def OnClick2(self,e):
        self.IsShowPanel(2)
    #习惯打卡
    def OnClick3(self,e):
        self.IsShowPanel(3)
    #计划打卡
    def OnClick4(self, e):
        self.IsShowPanel(4)
    #账单
    def OnClick5(self, e):
        self.IsShowPanel(5)
    # 创建计划
    def OnClick6(self, e):
        self.IsShowPanel(6)
    #创建习惯
    def OnClick7(self,e):
        self.IsShowPanel(7)
    #收入
    def OnClick8(self, e):
        self.IsShowPanel(8)
    #支出
    def OnClick9(self, e):
        self.IsShowPanel(9)
    #个人账户
    def OnClick10(self, e):
        self.IsShowPanel(10)
    #安全中心
    def OnClick11(self, e):
        self.IsShowPanel(11)
    #使用帮助
    def OnClick12(self, e):
        self.IsShowPanel(12)
    #关于我们
    def OnClick13(self, e):
        self.IsShowPanel(13)
#注册界面
class RegisterFrame(wx.Frame,Singleton):
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

                '''4.一个名为‘self’的文件存放个人账户信息'''
                selftxtFile = str(self.FilePath + "self.txt")
                selfTxt = open(selftxtFile, "w", encoding="utf-8")
                selfTxt.write(str({str(self.accountNumber):"写点儿什么..."}))

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
                #收入
                self.isBill = os.path.exists(self.FilePath + "bill\\")
                if not self.isBill:
                    os.mkdir(self.FilePath + "bill\\")  # 不存在则创建
                else:
                    pass
                #收入
                BillInFile = str(self.FilePath + "bill\\" + "billIn.txt")
                BillInTxt = open(BillInFile, "w", encoding="utf-8")
                #支出
                BillOutFile = str(self.FilePath + "bill\\" + "billOut.txt")
                BillOutTxt = open(BillOutFile, "w", encoding="utf-8")


            else:
                pass
        except:
            pass

        try:
            wx.MessageBox("账号:"+str(self.accountNumber)+"\nUID:"+
                          str(self.uidNumber)+"\n请记下账号与UID!\n","信息",
                          style=wx.OK)
            mgd = wx.MessageDialog(self,"退出","创建成功",wx.OK)
            if mgd.ShowModal() == wx.ID_OK:
                self.Show(False)

            self.txtOnePwd.SetValue("")
            self.txtTwoPwd.SetValue("")
            self.lblPwdSureOne.SetLabel("")
            self.lblPwdSureTwo.SetLabel("")

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
class LoginFrame(wx.Frame,Singleton):
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
        # try:
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
                #打开文件
                actpwxTxtRead = open(self.Path+"\\actpwd.txt",'r',encoding="utf-8")
                line = eval(str(actpwxTxtRead.readline())) #字符串转为字典
                for act,pwd in line.items():
                    self.actNum = str(act)   #获取账号
                    self.pwdNum = str(pwd)   #获取密码
                if self.actNum == self.txtAccount.GetValue() and \
                    self.pwdNum == self.txtPassword.GetValue():
                    """显示首页界面"""
                    FirstHeadFrame(act=self.actNum).Show(True)
                    self.Show(False)
                    self.txtAccount.SetValue("")
                    self.txtPassword.SetValue("")
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
        # except:
        #     pass
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