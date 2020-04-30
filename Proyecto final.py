import PySimpleGUI as sg
import re
class ITEM:
    def __init__(self,name,category,location,quantity,atribute):
        self.name=name
        self.category=category
        self.location=location
        self.quantity=quantity
        self.atribute=atribute
    def getName(self):
        return self.name
    def getCategory(self):
        return self.category
    def getLocation(self):
        return self.location
    def getQuantity(self):
        return self.quantity
    def getAtribute(self):
        return self.atribute
    def print(self):
        return '\nName: '+self.name+'\nCategory: '+self.category+'\nLocation: '+self.location+' \nQuantity: '+self.quantity+'\nAtribute: '+self.atribute
    def printcsv(self):
        return ('\n'+self.name+','+self.category+','+
              self.location+','+self.quantity+','+self.atribute)
    
def IsUserAndPass(userfile,user,password):
    file=open(userfile,'r')
    for line in file:
        if line != '\n':
            first,last=line.split(":")
            if(first==user and password==last):
                return True
        
    return False
def IsUser(userfile,user):
    file=open(userfile,'r')
    for line in file:
        if line != '\n':
            
            first,last=line.split(":")
            if(first==user):
                return True
        
    return False
def IsEmpty(pathfile):
    file=open(pathfile,'r')
    for line in file:
        if line != '\n':
            return False
        
    return True
def ItemSearch(item,itemlist):
    i=1
    for i in range(len(itemlist)):
            if(item.getName()==itemlist[i].getName()):
                return True
    return False
def ItemSearchandReturn(item,itemlist,keyword):#hacer que busque sin ser exacto
    i=1
    final=''
    if (keyword=='Category'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getCategory()):
                    final=final+itemlist[i].print()
    if (keyword=='Name'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getName()):
                    final=final+itemlist[i].print()
    if (keyword=='Location'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getLocation()):
                     final=final+itemlist[i].print()
    if (keyword=='Quantity'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getQuantity()):
                     final=final+itemlist[i].print()
    if (keyword=='Atribute'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getAtribute()):
                     final=final+itemlist[i].print()
    return final
sg.theme('DarkAmber')

#Welcome Screen Layout
wslayout = [[sg.Text('\n\n\nWelcome to Inventory Plus',size=(30,0), justification='center',
            font=("Times", 35))],[sg.Button('Press here to continue', size=(19, 1),pad=((195, 10), 3),font='Helvetica 14')],
            [sg.Text('',size=(10,10))]]

#User Screen Layout
uslayout=[[sg.Text('\n\n\nUser Sign-In',size=(20, 0), justification='center', font=("Times", 35))],[sg.Text('User:\t',
         font=("Times",25)),sg.Input(size=(30,100),key='User')],[sg.Text('Password: ',font=("Times",25)),sg.Input(size=(30,100),key='Pass')],
         [sg.Button('Enter', size=(10, 1),pad=((150, 10), 3),font='Helvetica 14',key='Enter')],[sg.Text('',size=(10,10))]]
#File Choose Layout
fclayout=[[sg.Text('\n\n\nChoose files: ',size=(30,0), font=("Times", 35),key='text')],
          [sg.Text('Users File: ', size=(15, 1),font=("Times",15)), sg.Input(key='UF'), sg.FileBrowse()],
          [sg.Text('Inventory File:', size=(15, 1),font=("Times",15)), sg.Input(key='IF'), sg.FileBrowse()],
          [sg.Submit(pad=((195, 10), 3),key='Submit'), sg.Cancel()],[sg.Text('',size=(10,10))]]

welcomescreen = sg.Window('Inventory Plus', wslayout)    

wsevent, wsvalues = welcomescreen.read()    
welcomescreen.close()

pathfile='PathFile.txt'
if(IsEmpty(pathfile)):
    filechoosescreen = sg.Window('Inventory Plus', fclayout)    
    fcevent, fcvalues = filechoosescreen.read()
    path=open(pathfile,'a')
    path.write(fcvalues['UF'])
    path.write("\n")
    path.write(fcvalues['IF'])
    path.close()
    if fcevent=='Submit':
        filechoosescreen .close()
ufname,ufnamefinal,ifname,ifnamefinal='','','',''
fp=open(pathfile)
for i, line in enumerate(fp):
    if line!='\n':
        if i == 0:
            ufname=line.split("/")
            ufnamefinal=ufname[len(ufname)-1]
            ufnamefinal = re.sub('\n$', '', ufnamefinal)
        elif i == 1:
            ifname=line.split("/")
            ifnamefinal=ifname[len(ifname)-1]
cond=False
path=open(ufnamefinal,'r')
for line in path:
    if line!='\n':
        cond=True
if cond:
    userwelcome=sg.Window('Inventory Plus',uslayout)
    while True:
        usevent, usvalues = userwelcome.read()
        if usevent=='Enter' and IsUserAndPass(ufnamefinal,usvalues['User'],usvalues['Pass'])!=True:
            userwelcome['text'].update('\n\n\nEnter a valid user and password')
            userwelcome['User'].update('')
            userwelcome['Pass'].update('')
        if usevent=='Enter' and IsUserAndPass(ufnamefinal,usvalues['User'],usvalues['Pass'])==True:
            sg.popup('Logged In Succesfully!')
            break
    userwelcome.close()
#Top Menu
menu_def = [['Inventory Management', ['Add...', 'Delete...', 'Update...', 'Search...']],            
            ['Users', ['Add User...','Delete User...','Update User...']],['Settings']] 

#Main Screen Layout
#Empujar exit button si ponen algo
mslayout=[[sg.Menu(menu_def,key='Menu')],[sg.Text('\n\nDashboard',size=(50,10),font=("Times",25),
justification='center')],[sg.Button('Exit',pad=(300,5),size=(10,1),key='Exit')]]

mainscreen=sg.Window('Inventory Plus',mslayout)
#msevent,msvalues=mainscreen.read()


#Search Screen Layout
sslayout= [[sg.Text('\nSearch Item',size=(20, 0),font=("Times", 35),key='Title')],
           [sg.InputCombo(('Category', 'Name','Location','Quantity','Atribute'), size=(20, 1),key='combovalue'),
            sg.Input(key='searchvalue')],[sg.Submit(pad=((320, 10), 3),key='Submit'), sg.Cancel(key='Cancel')],
            [sg.Multiline(default_text='This is the default Text should you decide not to type anything',
            size=(70, 40),key='textbox')],[sg.Text('',size=(5,5))]]

#AddScreenLayout
aslayout=[[sg.Text('\n\n\nAdd Item',size=(20, 0), justification='center', font=("Times", 35),key='Title')],
         [sg.Text('Item Name'),sg.Input(key='ITEMNAME')],[sg.Text('Category'),sg.Input(key='CATEGORY')],
         [sg.Text('Location'),sg.Input(key='LOCATION')],[sg.Text('Quantity'),sg.Input(key='QUANTITY')],
          [sg.Text('Atribute'),sg.Input(key='ATRIBUTE')],[sg.Submit(pad=((195, 10), 3),key='Submit'), sg.Cancel()]
          ,[sg.Text('',size=(10,10))]]
addscreen=sg.Window('Inventory Plus',aslayout)
final=True
while True:
    msevent,msvalues=mainscreen.read()
    fp=open(ifnamefinal,'r')
    inventorylist=[]
    for i, line in enumerate(fp):
        if line!='\n' and i>0:
            name,category,location,quantity,atribute=line.split(',')
            item=ITEM(name,category,location,quantity,atribute)
            inventorylist.append(item)#Anadi a list
    fp.close()
    #addscreen=sg.Window('Inventory Plus',aslayout)
    if msevent=='Add...':#hay que darle dos veces
        #addscreen=sg.Window('Inventory Plus',aslayout)
        while final:
            asevent,asvalues=addscreen.read()
            if asevent=='Submit':
                item=ITEM(asvalues['ITEMNAME'],asvalues['CATEGORY'],asvalues['LOCATION'],asvalues['QUANTITY'],asvalues['ATRIBUTE'])
                if (ItemSearch(item,inventorylist)==False):
                    inventorylist.append(item)#Anadi a list
                    fp=open(ifnamefinal,'a')
                    fp.write(item.printcsv())#Anadi a csv
                    fp.close()
                    sg.popup('Added Succesfully!')
                    addscreen.close()
                    final=False
                    break
                else:
                   addscreen['Title'].update('\n\n\nPlease Enter A New Item')
                   addscreen['ITEMNAME'].update('')
                   addscreen['CATEGORY'].update('')
                   addscreen['LOCATION'].update('')
                   addscreen['QUANTITY'].update('')
                   addscreen['ATRIBUTE'].update('')
            if asevent=='Cancel':
                addscreen.close()
                final=False
                break
    elif msevent=='Delete...':#un Search pero con la opcion de escoger y un buton de delete
        print('')
    elif msevent=='Update...':#un Search y un Add combinados
        print('')
    elif msevent=='Search...':
        searchscreen=sg.Window('Inventory Plus',sslayout)
        while True:
            ssevent,ssvalues=searchscreen.read()
            if ssevent=='Submit':
                searchscreen['textbox'].update(ItemSearchandReturn(ssvalues['searchvalue'],inventorylist,ssvalues['combovalue']))
            if ssevent=='Cancel':
                searchscreen.close()
                break
    elif msevent=='Settings':
        fclayout=[[sg.Text('\n\n\nChoose files: ',size=(30,0), font=("Times", 35),key='text')],
              [sg.Text('Users File: ', size=(15, 1),font=("Times",15)), sg.Input(key='UF'), sg.FileBrowse()],
              [sg.Text('Inventory File:', size=(15, 1),font=("Times",15)), sg.Input(key='IF'), sg.FileBrowse()],
              [sg.Submit(pad=((195, 10), 3),key='Submit'), sg.Cancel()],[sg.Text('',size=(10,10))]]
        print('')
    elif msevent=='Add User...':#mismo que el add pero otro csv y campos:user,pass,role
        print('')
    elif msevent=='Delete User...':#mismo que el delete pero otros csv
        print('')
    elif msevent=='Update User...':#similar al update pero otros csv
        print('')
    elif msevent=='Exit':
        mainscreen.close()
        break
    #si nos da tiempo hacemos lo algo con el campo de roles en users
