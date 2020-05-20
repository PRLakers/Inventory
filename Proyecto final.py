import PySimpleGUI as sg
import re
import csv
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
        return '\nName: '+self.name+'\nCategory: '+self.category+'\nLocation: '+self.location+' \nQuantity: '+self.quantity+'\nAttribute: '+self.atribute
    def printcsv(self):
        return (self.name+','+self.category+','+
              self.location+','+self.quantity+','+self.atribute)
    def printdelete(self):
        return '\nName: ///'+self.name+'///'+'\nCategory: '+self.category+'\nLocation: '+self.location+' \nQuantity: '+self.quantity+'\nAttribute: '+self.atribute
class USER:
    def __init__(self,user,password,role):
        self.user=user
        self.password=password
        self.role=role
    def getUser(self):
        return self.user
    def getPassword(self):
        return self.password
    def getRole(self):
        return self.role
    def print(self):
        return '\nUsername: '+self.user+'\nPassword: '+self.password+'\nRole: '+self.role
    def printtxt(self):
        return ('\n'+self.user+':'+self.password+':'+self.role)
    def printdelete(self):
        return '\nUser: ///'+self.user+'///'
def userSearch(user, userlist):
    i=1
    for i in range(len(userlist)):
            if(user.getUser()==userlist[i].getUser()):
                return True
    return False
def UserSearchandReturn(user,userlist,keyword):#hacer que busque sin ser exacto
    i=1
    final=''
    if (keyword=='User'):
        for i in range(len(userlist)):
                if(user==userlist[i].getUser()):
                    final=final+userlist[i].print()
    if (keyword=='Password'):
        for i in range(len(userlist)):
                if(user==userlist[i].getPassword()):
                    final=final+userlist[i].print()
    if (keyword=='Role'):
        for i in range(len(userlist)):
                if(user==userlist[i].getRole()):
                     final=final+userlist[i].print()
    return final
def UserSearchandReturnDelete(user,userlist):#hacer que busque sin ser exacto
    i=1
    final=''
    for i in range(len(userlist)):
            if(user==userlist[i].getUser()):
                final=final+userlist[i].printdelete()
        
    return final
def IsUserAndPass(userfile,user,password):
    file=open(userfile,'r')
    for line in file:
        if line != '\n':
            first,last,role=line.split(":")
            if(first==user and password==last):
                return True
        
    return False
def IsUser(userfile,user):
    file=open(userfile,'r')
    for line in file:
        if line != '\n':
            
            first,last,role=line.split(":")
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
def ItemSearchandReturnDelete(item,itemlist,keyword):#hacer que busque sin ser exacto
    i=1
    final=''
    if (keyword=='Category'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getCategory()):
                    final=final+itemlist[i].printdelete()
    if (keyword=='Name'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getName()):
                    final=final+itemlist[i].printdelete()
    if (keyword=='Location'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getLocation()):
                     final=final+itemlist[i].printdelete()
    if (keyword=='Quantity'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getQuantity()):
                     final=final+itemlist[i].printdelete()
    if (keyword=='Atribute'):
        for i in range(len(itemlist)):
                if(item==itemlist[i].getAtribute()):
                     final=final+itemlist[i].printdelete()
    return final
sg.theme('DarkAmber')

#Welcome Screen Layout
red_x_base64=b'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'

#Welcome Screen Layout
wslayout = [[sg.Text('\n\n\nWelcome to Inventory Plus',size=(30,0), justification='center',
            font=("Times", 35))],[sg.Text('\t\t\tPowered by Python', size=(42,0),font=("Times",15),justification='center')],[sg.Button('Press here to continue', size=(19, 1),pad=((195, 10), 3),font='Helvetica 14')],
            [sg.Text('',size=(10,10))],[sg.Button('',image_data=red_x_base64)]]

#User Screen Layout
uslayout=[[sg.Text('\n\n\nUser Sign-In',size=(20, 0), justification='center', font=("Times", 35),key='text')],[sg.Text('User:\t',
         font=("Times",25)),sg.Input(size=(30,100),key='User')],[sg.Text('Password: ',font=("Times",25)),sg.Input(size=(30,100),key='Pass')],
         [sg.Button('Enter', size=(10, 1),pad=((150, 10), 3),font='Helvetica 14',key='Enter')],[sg.Text('',size=(10,10))]]
#File Choose Layout
fclayout=[[sg.Text('\n\n\nChoose files: ',size=(30,0), font=("Times", 35),key='text')],
          [sg.Text('Users File (.txt): ', size=(20, 1),font=("Times",15)), sg.Input(key='UF'), sg.FileBrowse()],
          [sg.Text('Inventory File (.csv):', size=(20, 1),font=("Times",15)), sg.Input(key='IF'), sg.FileBrowse()],
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
    if fcevent=='Cancel':
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
fp.close()
cond=False
path=open(ufnamefinal,'r')
for i, line in enumerate(path):
    if line!='\n' and i>0:
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
            ['Users', ['Add User...','Delete User...','Update User...']],['Settings',['Choose File...']]]

#Main Screen Layout
fp=open(ifnamefinal,'r')
inventorylist11=[]
for i, line in enumerate(fp):
    if line!='\n' and i>0:
        name,category,location,quantity,atribute=line.split(',')
        item=ITEM(name,category,location,quantity,atribute)
        inventorylist11.append(item)#Anadi a list
fp.close()
fp=open(ufnamefinal, 'r')
userlist11=[]
for i, line in enumerate(fp):
    if line!='\n' and i>0:
        user,password,role=line.split(':')
        user=USER(user,password,role)
        userlist11.append(user)
fp.close()
mslayout=[[sg.Menu(menu_def,key='Menu')],[sg.Text('\nDashboard\n',size=(50,0),justification='center',font=("Times",45)
)],[sg.Text("\t\t"),
sg.Frame("Number of Items",[[sg.Text(str(len(inventorylist11)),size=(20,0),justification='center',font=("Times",40),key='numofitem')]],font=("Times",20)),sg.Text("\t\t"),
sg.Frame("Number of Users",[[sg.Text(str(len(userlist11)),size=(20,0),justification='center',font=("Times",40),key='numofuser')]],font=("Times",20))],
[sg.Text("\n\n")],
[sg.Text("\n\n\t\t"),
sg.Frame("User Path File",[[sg.Text(ufnamefinal,size=(20,0),justification='center',font=("Times",40),key='userpath')]],font=("Times",20)),sg.Text("\t\t"),
sg.Frame("Inventory Path File",[[sg.Text(ifnamefinal,size=(20,0),justification='center',font=("Times",40),key='inventorypath')]],font=("Times",20))],
[sg.Text('',size=(10,5))],
[sg.Button('Exit', size=(15, 1),pad=((450, 10), 3),font='Helvetica 14',key="Exit"),sg.Button("Refresh",size=(15, 1),pad=((10, 10), 3),font='Helvetica 14',key="Refresh")],[sg.Text('',size=(10,10))]]

mainscreen=sg.Window('Inventory Plus',mslayout)

#Search Screen Layout
sslayout= [[sg.Text('\nSearch Item',size=(20, 0),font=("Times", 35),key='Title')],
           [sg.InputCombo(('Category', 'Name','Location','Quantity','Atribute'), size=(20, 1),key='combovalue'),
            sg.Input(key='searchvalue')],[sg.Submit(pad=((320, 10), 3),key='Submit'), sg.Cancel(key='Cancel')],
            [sg.Multiline(default_text='This is the default Text should you decide not to type anything',
            size=(70, 20),key='textbox')],[sg.Text('',size=(5,5))]]
searchscreen=sg.Window('Inventory Plus',sslayout)
#AddScreenLayout
aslayout=[[sg.Text('\n\n\nAdd Item',size=(20, 0), justification='center', font=("Times", 35),key='Title')],
         [sg.Text('Item Name'),sg.Input(key='ITEMNAME')],[sg.Text('Category'),sg.Input(key='CATEGORY')],
         [sg.Text('Location'),sg.Input(key='LOCATION')],[sg.Text('Quantity'),sg.Input(key='QUANTITY')],
          [sg.Text('Attribute'),sg.Input(key='ATRIBUTE')],[sg.Submit(pad=((195, 10), 3),key='Submit'), sg.Cancel()]
          ,[sg.Text('',size=(10,10))]]
addscreen=sg.Window('Inventory Plus',aslayout)
#DeleteScreenLayout
emptylist=[]
dslayout=[[sg.Text('\nSearch Item to Delete',size=(20, 0),font=("Times", 35),key='Title')],
           [sg.InputCombo(('Category', 'Name','Location','Quantity','Attribute'), size=(20, 1),key='combovalue'),
            sg.Input(key='searchvalue'),sg.Submit(pad=((10, 10), 3),key='Submit')],
            [sg.Multiline(default_text='This is the default Text should you decide not to type anything',
            size=(70, 20),key='textbox')],[sg.Frame('Choose Item to Delete',[[sg.Listbox(values=emptylist, 
            size=(20, 12), key='-LIST-', enable_events=True)]]),
            sg.Button('Delete', size=(10, 1),pad=((10, 10), 3),font=('Helvetica',14),key='Delete'),sg.Button('Exit',
            key='Exit', size=(10, 1),font=('Helvetica',14))],
            [sg.Text('',size=(5,5))]]
deletescreen=sg.Window('Inventory Plus',dslayout)
#Update Screen Layout
uslayout=[[sg.Text('\nSearch Item to Update',size=(20, 0),font=("Times", 35),key='Title')],
           [sg.InputCombo(('Category', 'Name','Location','Quantity','Attribute'), size=(20, 1),key='combovalue'),
            sg.Input(key='searchvalue'),sg.Submit(pad=((10, 10), 3),key='Submit')],
            [sg.Multiline(default_text='This is the default Text should you decide not to type anything',
            size=(70, 20),key='textbox')],[sg.Frame('Choose Item to Update',[[sg.Listbox(values=emptylist, 
            size=(20, 12), key='-LIST-', enable_events=True)]]),sg.Frame('Enter Fields',layout=[
            [sg.Text('Item Name'),sg.Input(key='ITEMNAME')],
            [sg.Text('Category '),sg.Input(key='CATEGORY')],
            [sg.Text('Location '),sg.Input(key='LOCATION')],
            [sg.Text('Quantity '),sg.Input(key='QUANTITY')],
            [sg.Text('Attribute '),sg.Input(key='ATRIBUTE')]])],
            [sg.Button('Update', size=(10, 1),pad=((250, 10), 3),font=('Helvetica',14),key='Update'),sg.Button('Exit',
            key='Exit', size=(10, 1),font=('Helvetica',14))],
            [sg.Text('',size=(5,5))]]
updatescreen=sg.Window('Inventory Plus',uslayout)
#Setting Layout
fclayout1=[[sg.Text('\n\n\nChoose files: ',size=(30,0), font=("Times", 35),key='text')],
          [sg.Text('Users File (.txt): ', size=(20, 1),font=("Times",15)), sg.Input(key='UF'), sg.FileBrowse()],
          [sg.Text('Inventory File (.csv):', size=(20, 1),font=("Times",15)), sg.Input(key='IF'), sg.FileBrowse()],
          [sg.Submit(pad=((195, 10), 3),key='Submit'), sg.Cancel(key='Cancel')],[sg.Text('',size=(10,10))]]
filechoosescreen1 = sg.Window('Inventory Plus', fclayout1)
#DeleteUser
deleteUser=[[sg.Text('\nSearch User to Delete',size=(20, 0),font=("Times", 35),key='Title')],
           [sg.Text('User',font=("Times",14)),
            sg.Input(key='searchvalue'),sg.Submit(pad=((10, 10), 3),key='Submit')],
            [sg.Multiline(default_text='This is the default Text should you decide not to type anything',
            size=(70, 10),key='textbox')],[sg.Frame('Choose User to Delete',[[sg.Listbox(values=emptylist, 
            size=(20, 12), key='-LIST-', enable_events=True)]]),
            sg.Button('Delete', size=(10, 1),pad=((10, 10), 3),font=('Helvetica',14),key='Delete'),sg.Button('Exit',
            key='Exit', size=(10, 1),font=('Helvetica',14))],
            [sg.Text('',size=(5,5))]]
deleteUser=sg.Window('Inventory Plus',deleteUser)
#UpdateUser
updateUser=[[sg.Text('\nSearch User to Update',size=(20, 0),font=("Times", 35),key='Title')],
           [sg.Text('User',font=("Times",14)),
            sg.Input(key='searchvalue'),sg.Submit(pad=((10, 10), 3),key='Submit')],
            [sg.Multiline(default_text='This is the default Text should you decide not to type anything',
            size=(70, 10),key='textbox')],[sg.Frame('Choose Item to Update',[[sg.Listbox(values=emptylist, 
            size=(20, 12), key='-LIST-', enable_events=True)]]),sg.Frame('Enter Fields',layout=[
            [sg.Text('User\t'),sg.Input(key='USER')],
            [sg.Text('Password '),sg.Input(key='PASSWORD')],
            [sg.Text('Role\t'),sg.Input(key='ROLE')],
            [sg.Button('Update', size=(10, 1),pad=((75, 10), 3),font=('Helvetica',14),key='Update'),sg.Button('Exit',
            key='Exit', size=(10, 1),font=('Helvetica',14))],
            [sg.Text('',size=(5,5))]])]]
updateUser=sg.Window('Inventory Plus',updateUser)
                
#Adduser
addUser=[[sg.Text('\n\n\nAdd User',size=(20, 0), justification='center', font=("Times", 35),key='Title')],
         [sg.Text('User\t'),sg.Input(key='USER')],[sg.Text('Password'),sg.Input(key='PASSWORD')],
         [sg.Text('Role\t'),sg.Input(key='ROLE')],[sg.Submit(pad=((195, 10), 3),key='Submit'), sg.Cancel()]
        ,[sg.Text('',size=(10,10))]]
addUser=sg.Window('Inventory Plus',addUser)
final=True
while True:
    msevent,msvalues=mainscreen.read()
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
    fp.close()
    fp=open(ifnamefinal,'r')
    inventorylist=[]
    for i, line in enumerate(fp):
        if line!='\n' and i>0:
            name,category,location,quantity,atribute=line.split(',')
            item=ITEM(name,category,location,quantity,atribute)
            inventorylist.append(item)#Anadi a list
    fp.close()
    fp=open(ufnamefinal, 'r')
    userlist1=[]
    for i, line in enumerate(fp):
        if line!='\n' and i>0:
            user,password,role=line.split(':')
            user=USER(user,password,role)
            userlist1.append(user)
    mainscreen['numofitem'].update(len(inventorylist))
    mainscreen['numofuser'].update(len(userlist1))
    mainscreen['inventorypath'].update(ifnamefinal)
    mainscreen['userpath'].update(ufnamefinal)
    if msevent=='Add...':
        addscreen.UnHide()
        while True:
            asevent,asvalues=addscreen.read()
            if asevent=='Submit':
                item=ITEM(asvalues['ITEMNAME'],asvalues['CATEGORY'],asvalues['LOCATION'],asvalues['QUANTITY'],asvalues['ATRIBUTE'])
                if (ItemSearch(item,inventorylist)==False):
                    fp=open(ifnamefinal,'a')
                    fp.write('\n'+item.printcsv())#Anadi a csv
                    fp.close()
                    sg.popup('Added Succesfully!')
                    addscreen.Hide()
                    addscreen['ITEMNAME'].update('')
                    addscreen['CATEGORY'].update('')
                    addscreen['LOCATION'].update('')
                    addscreen['QUANTITY'].update('')
                    addscreen['ATRIBUTE'].update('')
                    break
                else:
                   addscreen['Title'].update('\n\n\nPlease Enter A New Item')
                   addscreen['ITEMNAME'].update('')
                   addscreen['CATEGORY'].update('')
                   addscreen['LOCATION'].update('')
                   addscreen['QUANTITY'].update('')
                   addscreen['ATRIBUTE'].update('')
            if asevent=='Cancel':
                addscreen.Hide()
                addscreen['ITEMNAME'].update('')
                addscreen['CATEGORY'].update('')
                addscreen['LOCATION'].update('')
                addscreen['QUANTITY'].update('')
                addscreen['ATRIBUTE'].update('')
                break
    elif msevent=='Delete...':#un Search pero con la opcion de escoger y un buton de delete
        deletescreen.UnHide()
        while True:
            dsevent,dsvalues=deletescreen.read()
            if dsevent=='Submit':
                deletescreen['textbox'].update(ItemSearchandReturnDelete(dsvalues['searchvalue'],inventorylist,dsvalues['combovalue']))
                deletecombo=ItemSearchandReturnDelete(dsvalues['searchvalue'],inventorylist,dsvalues['combovalue'])
                deletecombo=deletecombo.split('///')
                cbox=[]
                for i in range(len(deletecombo)):
                    if i % 2 != 0:
                        cbox.append(deletecombo[i])
                deletescreen['-LIST-'].update(cbox)
            if dsevent=='Exit':
                deletescreen.Hide()
                deletescreen['searchvalue'].update('')
                deletescreen['textbox'].update([])
                deletescreen['-LIST-'].update([])
                break
            if dsevent=='Delete':
                inventorylist1=[]
                fp=open(ifnamefinal,'r')
                for i, line in enumerate(fp):
                    if line!='\n' and i>0:
                         name,category,location,quantity,atribute=line.split(',')
                         item=ITEM(name,category,location,quantity,atribute)
                         inventorylist1.append(item)
                         if item.getName()==dsvalues['-LIST-'][0]:
                             inventorylist1.remove(item)
                fp.close()
                fp1=open(ifnamefinal,'w')
                fp1.write('Name,Category,Location,Quantity,Atribute\n')
                i=1
                for i in range(len(inventorylist1)):
                    fp1.write(inventorylist1[i].printcsv())
                fp1.close()
                sg.popup('Deleted Succesfully!')
                deletescreen.Hide()
                deletescreen['searchvalue'].update('')
                deletescreen['textbox'].update([])
                deletescreen['-LIST-'].update([])
                break
    elif msevent=='Update...':
         updatescreen.UnHide()
         while True:
            usevent,usvalues=updatescreen.read()
            if usevent=='Submit':
                updatescreen['textbox'].update(ItemSearchandReturnDelete(usvalues['searchvalue'],inventorylist,usvalues['combovalue']))
                updatecombo=ItemSearchandReturnDelete(usvalues['searchvalue'],inventorylist,usvalues['combovalue'])
                updatecombo=updatecombo.split('///')
                ubox=[]
                for i in range(len(updatecombo)):
                    if i % 2 != 0:
                        ubox.append(updatecombo[i])
                updatescreen['-LIST-'].update(ubox)
            if usevent=='Exit':
                updatescreen.Hide()
                updatescreen['searchvalue'].update('')
                updatescreen['ITEMNAME'].update('')
                updatescreen['CATEGORY'].update('')
                updatescreen['LOCATION'].update('')
                updatescreen['QUANTITY'].update('')
                updatescreen['ATRIBUTE'].update('')
                updatescreen['textbox'].update([])
                updatescreen['-LIST-'].update([])
                break
            if usevent=='Update': 
                inventorylist1=[]
                fp=open(ifnamefinal,'r')
                for i, line in enumerate(fp):
                    if line!='\n' and i>0:
                         name,category,location,quantity,atribute=line.split(',')
                         item=ITEM(name,category,location,quantity,atribute)
                         inventorylist1.append(item)
                         if item.getName()==usvalues['-LIST-'][0]:
                             inventorylist1.remove(item)
                fp.close()
                fp1=open(ifnamefinal,'w')
                fp1.write('Name,Category,Location,Quantity,Atribute\n')
                i=1
                for i in range(len(inventorylist1)):
                    fp1.write(inventorylist1[i].printcsv())
                item=ITEM(usvalues['ITEMNAME'],usvalues['CATEGORY'],usvalues['LOCATION'],usvalues['QUANTITY'],usvalues['ATRIBUTE'])
                fp1.write("\n"+item.printcsv())
                fp1.close()
                sg.popup('Updated Succesfully!')
                updatescreen.UnHide()
                updatescreen['searchvalue'].update('')
                updatescreen['ITEMNAME'].update('')
                updatescreen['CATEGORY'].update('')
                updatescreen['LOCATION'].update('')
                updatescreen['QUANTITY'].update('')
                updatescreen['ATRIBUTE'].update('')
                updatescreen['textbox'].update([])
                updatescreen['-LIST-'].update([])
                break
    elif msevent=='Search...':
        searchscreen.UnHide()
        while True:
            ssevent,ssvalues=searchscreen.read()
            if ssevent=='Submit':
                searchscreen['textbox'].update(ItemSearchandReturn(ssvalues['searchvalue'],inventorylist,ssvalues['combovalue']))
            if ssevent=='Cancel':
                searchscreen.Hide()
                searchscreen['searchvalue'].update('')
                searchscreen['textbox'].update([])
                break
    elif msevent=='Choose File...':
        filechoosescreen1.UnHide()
        while True: 
            pathfile = 'PathFile.txt'    
            fcevent, fcvalues = filechoosescreen1.read()
            if fcevent=='Submit':
                path=open(pathfile,'w')
                path.write(fcvalues['UF'])
                path.write("\n")
                path.write(fcvalues['IF'])
                path.close()
                filechoosescreen1.Hide()
                break 
            if fcevent=='Cancel':
                filechoosescreen1.Hide()
                break
    elif msevent=='Add User...':
        addUser.UnHide()
        while True:
            asevent1,asvalues1=addUser.read()
            if asevent1=='Submit':
                user2=USER(asvalues1['USER'],asvalues1['PASSWORD'],asvalues1['ROLE'])
                if (userSearch(user2,userlist1)==False):
                    userlist1.append(user2)
                    fp=open(ufnamefinal,'a')
                    fp.write(user2.printtxt())
                    fp.close()
                    sg.popup('User added succesfully!')
                    addUser.Hide()
                    addUser['USER'].update('')
                    addUser['PASSWORD'].update('')
                    addUser['ROLE'].update('')
                    break
                else:
                    addUser['Title'].update('\n\n\nEnter new user')
                    addUser['USER'].update('')
                    addUser['PASSWORD'].update('')
                    addUser['ROLE'].update('')
            if asevent1=='Cancel':
                addUser.Hide()
                addUser['USER'].update('')
                addUser['PASSWORD'].update('')
                addUser['ROLE'].update('')
                break
    elif msevent=='Delete User...':
        deleteUser.UnHide()
        while True:
            dsevent1,dsvalues1=deleteUser.read()
            if dsevent1=='Submit':
                fp=open(ufnamefinal, 'r')
                userlist2=[]
                for i, line in enumerate(fp):
                    if line!='\n' and i>0:
                        user,password,role=line.split(':')
                        user=USER(user,password,role)
                        userlist2.append(user)
                fp.close()
                deleteUser['textbox'].update(UserSearchandReturnDelete(dsvalues1['searchvalue'],userlist2))
                deletecombo=UserSearchandReturnDelete(dsvalues1['searchvalue'],userlist2)
                deletecombo=deletecombo.split('///')
                cbox=[]
                for i in range(len(deletecombo)):
                    if i % 2 != 0:
                        cbox.append(deletecombo[i])
                deleteUser['-LIST-'].update(cbox)
            if dsevent1=='Exit':
                deleteUser.Hide()
                deleteUser['searchvalue'].update('')
                deleteUser['textbox'].update([])
                deleteUser['-LIST-'].update([])
                break
            if dsevent1=='Delete':
                userListDelete1=[]
                fp1=open(ufnamefinal,'r')
                for i, line in enumerate(fp1):
                    if line!='\n' and i>0:
                            user,password,role=line.split(':')
                            userDelete=USER(user,password,role)
                            userListDelete1.append(userDelete)
                            if userDelete.getUser()==dsvalues1['-LIST-'][0]:
                                userListDelete1.remove(userDelete)
                fp1.close()
                fp2=open(ufnamefinal,'w')
                fp2.write('User:Password:Role\n')
                i=1
                for i in range(len(userListDelete1)):
                    fp2.write(userListDelete1[i].printtxt())
                fp2.close()
                sg.popup('Deleted User Succesfully!')
                deleteUser.Hide()
                deleteUser['searchvalue'].update('')
                deleteUser['textbox'].update([])
                deleteUser['-LIST-'].update([])
                break
    elif msevent=='Update User...':
        updateUser.UnHide()
        while True:
            usevent1,usvalues1=updateUser.read()
            if usevent1=='Submit':
                fp=open(ufnamefinal, 'r')
                userlist2=[]
                for i, line in enumerate(fp):
                    if line!='\n' and i>0:
                        user,password,role=line.split(':')
                        user=USER(user,password,role)
                        userlist2.append(user)
                fp.close()
                updateUser['textbox'].update(UserSearchandReturnDelete(usvalues1['searchvalue'],userlist2))
                updatecombo=UserSearchandReturnDelete(usvalues1['searchvalue'],userlist2)
                updatecombo=updatecombo.split('///')
                ubox=[]
                for i in range(len(updatecombo)):
                    if i % 2 != 0:
                        ubox.append(updatecombo[i])
                
                updateUser['-LIST-'].update(ubox)
            if usevent1=='Exit':
                updateUser.Hide()
                updateUser['searchvalue'].update('')
                updateUser['USER'].update('')
                updateUser['PASSWORD'].update('')
                updateUser['ROLE'].update('')
                updateUser['textbox'].update([])
                updateUser['-LIST-'].update([])
                break
            if usevent1=='Update': 
                userUpdateList=[]
                fp=open(ufnamefinal,'r')
                for i, line in enumerate(fp):
                    if line!='\n' and i>0:
                         user,password,role=line.split(':')
                         user2=USER(user,password,role)
                         userUpdateList.append(user2)
                         if user2.getUser()==usvalues1['-LIST-'][0]:
                             userUpdateList.remove(user2)
                fp.close()
                fp3=open(ufnamefinal,'w')
                fp3.write('User:Password:Role\n')
                i=1
                for i in range(len(userUpdateList)):
                    fp3.write(userUpdateList[i].printtxt())
                user2=USER(usvalues1['USER'],usvalues1['PASSWORD'],usvalues1['ROLE'])
                fp3.write(user2.printtxt())
                fp3.close()
                sg.popup('Updated User Succesfully!')
                updateUser.Hide()
                updateUser['searchvalue'].update('')
                updateUser['USER'].update('')
                updateUser['PASSWORD'].update('')
                updateUser['ROLE'].update('')
                updateUser['textbox'].update([])
                updateUser['-LIST-'].update([])
                break
    elif msevent=='Exit':
        mainscreen.close()
        break
    elif msevent=='Refresh':
        print("")







