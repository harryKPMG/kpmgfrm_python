# !/usr/bin/env python
# -*- coding:utf-8 -*-


__author__ = 'afli'

class Staff:
    '''Represents any staff in KPMG firm.'''
    population=0
    def __init__(self,name,gender,level,salary):#initialization of class
        self.name=name
        self.gender=gender
        self.lvl=level
        self.salary=salary
        Staff.population+=1
        print 'Initialized Staff: %s'%self.name

    def nm(self):#print object's name
        print 'My Name is:%s'%self.name

    def level(self):#print object's level
        print 'I am a %s staff'%self.lvl

    def show(self):#show object's main info
        print 'Name:%s Gender:%s Level:%s Salary:%d'%(self.name,self.gender,self.lvl,self.salary),

class Consultant(Staff):
    '''Represents any consultant.'''
    def __init__(self,name,gender,level,salary,activity):#initialization of class
        Staff.__init__(self,name,gender,level,salary)
        self.act=activity
        print 'Initialized Consultant: %s'%self.name

    def nm(self):#print object's name
        Staff.nm(self)

    def level(self):#print object's level
        Staff.level(self)

    def show(self):#show object's main info
        Staff.show(self)
        print 'Activity:%s'%self.act

    def activity(self):#print object's activity
        print self.name,"'s activity is %s"%self.act
        return self.act


class Manager(Staff):
    '''Represents any manager.'''
    def __init__(self,name,gender,level,salary,qualification):#initialization of class
        Staff.__init__(self,name,gender,level,salary)
        self.q=qualification
        print 'Initialized Manager: %s'%self.name

    def nm(self):#print object's name
        Staff.nm(self)

    def level(self):#print object's level
        Staff.level(self)

    def show(self):#show object's main info
        Staff.show(self)
        print 'Qualification:%s'%self.q

    def qualification(self):#print object's qualification
        print self.name,"'s qualification is %s"%self.q


class SeniorManager(Staff):
    '''Represents any senior manager.'''
    def __init__(self,name,gender,level,salary,project):#initialization of class
        Staff.__init__(self,name,gender,level,salary)
        self.prj=project
        print 'Initialized Senior Manager: %s'%self.name

    def nm(self):#print object's name
        Staff.nm(self)

    def level(self):#print object's level
        Staff.level(self)

    def show(self):#show object's main info
        Staff.show(self)
        print 'Project:%s'%self.prj

    def project(self):#print object's project
        print self.name,"'s project is %s"%self.prj


class Partner(Staff):
    '''Represents any partner.'''
    def __init__(self,name,gender,level,salary,lob):#initialization of class
        Staff.__init__(self,name,gender,level,salary)
        self.lob=lob
        print 'Initialized Partner: %s'%self.name

    def nm(self):#print object's name
        Staff.nm(self)

    def level(self):#print object's level
        Staff.level(self)

    def show(self):#show object's main info
        Staff.show(self)
        print 'LOB:%s'%self.lob

    def biz(self):#print object's lob
        print self.name,"'s line of business is %s"%self.lob


#end of definition

print 'There are',Staff.population,'employees in the firm.'
c=Consultant('Messi','Male','A level',10000,'football')
m=Manager('Rooney','Male','C level',20000,'FRM')
s=SeniorManager('Maya','Female','D level',30000,'XXBank IMA')
p=Partner('Ronaldo','Male','E level',40000,'Market Risk')
print 'There are',Staff.population,'employees in the firm.'

FRM=[c,m,s,p]
for i in FRM:
    i.nm()
    i.level()
    i.show()

c.activity()
m.qualification()
s.project()
p.biz()
print Staff.__doc__