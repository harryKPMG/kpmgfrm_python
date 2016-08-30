#!/user/bin/python
# _*_ coding: utf-8 _*_
__author__ = 'philipshen'

class kpmgStaff:
#定义一个Kpmg员工信息的母类
    count=0 #计数变量
    def __init__(self,staffID,staffName,department,staffFunction):

        self.id=int(staffID)  #员工号,整数
        self.name=str(staffName) #姓名，字符串
        self.department=str(department) #部门，字符串
        self.function=str(staffFunction) #职能，字符串

        kpmgStaff.count= kpmgStaff.count+1 #统计Kpmg员工数量

class Consulant(kpmgStaff):
#定义一个Kpmg职能为Consulant的员工信息的子类
    member=[] #定义该职能员工姓名列表
    def __init__(self,staffID,staffName,department,task):
        kpmgStaff.__init__(self,staffID,staffName,department,'Consulant')#母类初始化，写死职能
        self.task=str(task)#定义子类特有属性：工作任务，字符串
        Consulant.member.append(staffName)

    @staticmethod
    def getCount():#统计该职能员工数量
        return len(Consulant.member)

class Partner(kpmgStaff):
#定义一个Kpmg职能为Partner的员工信息的子类
    member=[] #定义该职能员工姓名列表
    def __init__(self,staffID,staffName,department,project):
        kpmgStaff.__init__(self,staffID,staffName,department,'Partner')#母类初始化，写死职能
        self.myProject=list(project)#定义子类特有属性：手中的项目，字符串
        Partner.member.append(staffName)

    @staticmethod
    def getCount():#统计该职能员工数量
        return len(Partner.member)

class Manager(kpmgStaff):
#定义一个Kpmg职能为Manager的员工信息的子类
    member=[] #定义该职能员工姓名列表
    def __init__(self,staffID,staffName,department,boy):
        kpmgStaff.__init__(self,staffID,staffName,department,'Manager')#母类初始化，写死职能
        self.myBoy=list(boy)#定义子类特有属性：手下的小朋友列表，列表
        Manager.member.append(staffName)

    @staticmethod
    def getCount():#统计该职能员工数量
        return len(Manager.member)

    def getMyboy(self):#返回手下小朋友的姓名列表
        myboyMember=[]
        for i in range(0,len(self.myBoy)):
            myboyMember.append(self.myBoy[i].name)
        return myboyMember

class SeniorManager(kpmgStaff):
#定义一个Kpmg职能为SeniorManager的员工信息的子类
    member=[] #定义该职能员工姓名列表
    def __init__(self,staffID,staffName,department,myManager):
        kpmgStaff.__init__(self,staffID,staffName,department,'SeniorManager')#母类初始化，写死职能
        self.myManager=list(myManager)#定义子类特有属性：手下的经理列表，列表
        SeniorManager.member.append(staffName)

    @staticmethod
    def getCount():#统计该职能员工数量
        return len(SeniorManager.member)

    def getMyManager(self):#返回手下Manager的姓名列表
        myManagerMember=[]
        for i in range(0,len(self.myManager)):
            myManagerMember.append(self.myManager[i].name)
        return myManagerMember
#example:

jinx=Consulant(83007055,'Jinx','FRM','social')
curtis=Consulant(82254677,'Curtis','FRM','modelTest')
rose=Consulant(82659901,'Rose','FRM','dataProcing')
kate=Consulant(87655637,'Kate','FRM','projectManagement')
jack=Consulant(86602637,'Jack','FRM','dataProcessing')
marry=Consulant(83459900,'Marry','FRM','Riskfactors')
hanasaki=Consulant(89902501,'Hanasaki','FRM','modelDevelopment')
mizuhara=Consulant(83297546,'Mizuhara','FRM','dataProcing')

enzo=Manager(87920328,'Enzo','FRM',[curtis,kate,mizuhara])
friedlich=Manager(84410028,'Friedlich','FRM',[curtis,jinx,hanasaki])
alessandro=Manager(82016773,'Alessandro','FRM',[jack,rose,curtis,marry,jack])

linda=SeniorManager(83321900,'Linda','FRM',[enzo])
chrisoph=SeniorManager(87223456,'Christoph','FRM',[alessandro,friedlich])

david=Partner(87756731,'David','FRM',['ccbRisk','ccbValuation','cmbValidation'])


print 'The total number of staff of KPMG is',kpmgStaff.count

print 'The total number of Consulant is',Consulant.getCount()
print 'The total number of Manager is',Manager.getCount()
print 'The total number of SeniorManager is',SeniorManager.getCount()
print 'The total number of Partner is',Partner.getCount()

print 'The member of Consulant are',Consulant.member
print 'The member of Manager are',Manager.member
print 'The member of SeniorManager are',SeniorManager.member
print 'The member of Partner are',Partner.member

print'Enzo has',Manager.getMyboy(enzo),'to assign task'
print'Alessandro has',Manager.getMyboy(alessandro),'to assign task'
print'friedlich has',Manager.getMyboy(friedlich),'to assign task'

print'Linda has',SeniorManager.getMyManager(linda),'to work together'
print'christoph has',SeniorManager.getMyManager(chrisoph),'to work together'
print'David has',david.myProject, 'to focus on'




