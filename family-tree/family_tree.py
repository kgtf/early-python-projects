from turtle import *
from tkinter import *
class FamilyTree:
    '''Draws a Family Tree'''
    def __init__(self, master, family={0:"Not Known"}, level=0):
        ''' FamilyTree(master, family={0:"Not Known"}, level=0)
        Draws a family tree with a depth of level
        family -> a dictionary. Keys are 0 for self, 1 for dad, 2 for mom
        Ex. 12 -> mom's dad, 212, dad's mom's dad
        Level is how deep the family tree can go. 0 is just self, 1 is parents,
        2 is grandparents, etc.
        CAN ONLY GO FROM LEVEL 0-4 WILL SET LEVEL TO 0 IF GIVEN ANYTHING ELSE
        master is for GoodByeFrame'''
        # initalize variables
        # create two turtles
        self.mom_side = Turtle()
        self.dad_side = Turtle()
        self.wn = Screen()       # set up the window and its attributes
        self.master = master
        bgcolor('lightgray')
        
        # set background color
        self.bgColor = 'lightgray'
        
        # set speed
        self.mom_side.speed(0)
        self.dad_side.speed(0)
        # set size
        self.mom_side.pensize(2)
        self.dad_side.pensize(2)
        # set color
        self.mom_sideFontColor = 'blue'
        self.dad_sideFontColor = 'blue'
        self.mom_sideDrawColor = 'red'
        self.dad_sideDrawColor = 'orange'

        self.mom_side.color(self.mom_sideDrawColor)
        self.dad_side.color(self.dad_sideDrawColor)
        
        
        self.family = family
        self.keys = family.keys()
        # level can only be from 0 to 4 
        if level < 0 or level > 4:
            level = 0
        self.level = level

        # make a done button which deletes the current screen
        # draw button
        self.dad_side.color('black')
        self.dad_side.setheading(90)
        self.dad_side.penup()
        self.dad_side.fd(200)
        self.dad_side.rt(90)
        self.dad_side.fd(20)
        self.dad_side.lt(180)
        self.dad_side.pendown()
        self.dad_side.fillcolor('blue')
        self.dad_side.begin_fill()
        for side in [60, 40, 60, 40]:
            self.dad_side.fd(side)
            self.dad_side.rt(90)
        self.dad_side.end_fill()
        # write done 
        self.dad_side.penup()
        self.dad_side.fd(30)
        self.dad_side.rt(90)
        self.dad_side.fd(10)
        self.dad_side.color("magenta")
        self.dad_side.write("Done", font=('Arial', 20, 'underline'), align = 'center')
        self.dad_side.color(self.dad_sideDrawColor)
        
        # go back to original position
        self.dad_side.goto(0, 0)
        self.dad_side.setheading(0)
        self.dad_side.pendown()
        
        self.draw_tree() # draw the family tree
        # listen for if clicked on 
        self.wn.onscreenclick(self.done_button, 1)
        self.wn.listen()

            
        self.wn.mainloop()

    def done_button(self, x, y):
        ''' uses bye method for turtle screen to
        erase everything'''
        if x >= -40 and x <= 20 and y >= 200 and y <= 240:
            self.wn.bye()
            GoodByeFrame(self.master)

    def get_member(self, key):
        '''FamilyTree.get_member(key) -> str
        key -> int which represents which family member to get from family dict
        Keys are 0 for self, 1 for dad, 2 for mom Ex. 12 -> mom's dad;
        21 -> dad's mom's dad
        Returns "Not Known" if entry is not in dict or person is not known'''
        if key not in self.keys:
            return "Not Known"
        else:
            return self.family[key]

    def turn_turtle(self, t, parent):
        '''FamilyTree.turn_turtle(t, parent)
        t -> turtle object, mom_side or dad_side
        parent -> 1 if mom and 2 if dad
        if t is mom_side, turns right if father and left if mother
        if t is dad_side, turns left if father and right if mother'''
        if t == self.mom_side: # if turtle for mom side
            if parent == 1: # if mom
                t.lt(45) # turn left
            else: # if dad 
                t.rt(45) # turn right
        else:  # if turtle for dad side
            if parent == 1: # if mom    
                t.rt(45) # turn right
            else: # if dad
                t.lt(45) # turn left

    def draw_y(self, t, mom, dad, textOnly, centerY=None):
        '''FamilyTree.draw_y(t, side, mom, dad, textOnly, centerY )
        makes turtle t draw a y in whichever direction it is facing
        t -> the turtle which draws the y
        mom -> str the mom's name
        dad -> str the dad's name
        textOnly -> true if only text and not drawing else false
        centerY -> not necessary, str, the name where the 3 lines of the y meet
        will put mom on left and dad on right if turtle is mom_side and vice versa for dad_side'''
        if t == self.mom_side:  # if mom side
            leftY = mom
            rightY = dad
            drawColor = self.mom_sideDrawColor
            fontColor = self.mom_sideFontColor
        else:  # else dad side
            leftY = dad
            rightY = mom
            drawColor = self.dad_sideDrawColor
            fontColor = self.dad_sideFontColor
        t.fd(45)
        # write the name in the center if is given
        if not centerY == None:
            t.penup()
            t.lt(90)
            t.fd(10)
            t.color(fontColor)
            if t == self.mom_side:
                t.write(centerY, align = 'right', font=('Arial', 10, 'bold'))
            else:
                t.write(centerY, font=('Arial', 10, 'bold'))
            t.color(drawColor)
            t.bk(10)
            t.rt(90)
            if textOnly == False:
                t.pendown()
        t.fd(30)
        t.lt(45)
        t.fd(75)
        t.rt(135)
        t.penup()
        t.fd(15)
        # name for left branch
        t.color(fontColor)
        t.write(leftY, font=('Arial', 10, 'bold'))
        t.color(drawColor)
        t.bk(15)
        t.lt(135)
        t.bk(75)
        t.rt(90)
        if  textOnly == False:
            t.pendown()
        t.fd(75)
        t.lt(135)
        t.penup()
        t.fd(15)
        # name for right branch
        t.color(fontColor) 
        t.write(rightY, font=('Arial', 10, 'bold'))
        t.color(drawColor)
        t.bk(15)
        t.rt(135)
        t.bk(75)
        t.left(45)
        if textOnly == False:
            t.pendown()
        
    def draw_tree(self):
        '''FamilyTree.draw_tree()
        draws a family tree with depth level using mom_side and dad_side turtles and
        uses the names in the family dictionary'''        
        # write self name
        self.mom_side.color('purple')
        self.mom_side.write(self.get_member(0), font = ('Arial', 10, 'bold'), align = 'center')
        self.mom_side.color(self.mom_sideDrawColor)
        self.mom_side.rt(180)

        count = 0 # for determining if textOnly or not
        
        if self.level > 0:
            for t in [self.mom_side, self.dad_side, self.mom_side, self.dad_side]:
                count += 1 # increase count every time
                
                # to know if dad or mom
                if t == self.mom_side:
                    x = 1
                else:
                    x = 2

                # to know if textOnly or not 
                if count == 3 or count == 4:
                    t.penup()
                    textOnly = True
                else:
                    textOnly = False

                
                if self.level == 1: # if only up to level 1
                    t.fd(75)
                    if t == self.mom_side:
                        t.color(self.mom_sideFontColor)
                        t.write(self.get_member(x), font = ('Arial', 10, 'bold'))
                        t.color(self.mom_sideDrawColor)
                    else:
                        t.color(self.dad_sideFontColor)
                        t.write(self.get_member(x), font = ('Arial', 10, 'bold'))
                        t.color(self.dad_sideDrawColor)
                    t.goto(0, 0)
                        
                elif self.level >= 2: # else 2 or greater
                    self.draw_y(t, self.get_member(int(str(x) + '1')), self.get_member(int(str(x) + '2')), textOnly, self.get_member(int(str(x)))) # grand parents
                    
                    if self.level == 2: # if only up to level 2 go back to 0, 0
                        t.penup()
                        t.goto(0, 0)
                        t.pendown()
                        
                    else: 
                        self.turn_turtle(t, 2) # turn for grandfather's parents
                        
                    if self.level == 3: # if only up to great grandparents  
                        t.fd(75)
                        t.lt(45)
                        t.fd(75)
                        if t == self.mom_side:
                            t.color(self.mom_sideFontColor)
                            t.write(self.get_member(int(str(x) + '22')), font = ('Arial', 10, 'bold'))
                            t.color(self.mom_sideDrawColor)
                        else:
                            t.color(self.dad_sideFontColor)
                            t.write(self.get_member(int(str(x) + '22')), font = ('Arial', 10, 'bold'))
                            t.color(self.dad_sideDrawColor)
                            
                        t.bk(75)
                        t.rt(90)
                        t.fd(75)
                        if t == self.mom_side:
                            t.color(self.mom_sideFontColor)
                            t.write(self.get_member(int(str(x) + '21')), font = ('Arial', 10, 'bold'))
                            t.color(self.mom_sideDrawColor)
                        else:
                            t.color(self.dad_sideFontColor)
                            t.write(self.get_member(int(str(x) + '21')), font = ('Arial', 10, 'bold'))
                            t.color(self.dad_sideDrawColor)
                        t.penup()
                        t.goto(0, 0)
                        if t == self.mom_side:
                            t.setheading(180)
                        else:
                            t.setheading(0)
                    
                    elif self.level >= 4:
                        self.draw_y(t, self.get_member(int(str(x) + '21')), self.get_member(int(str(x) + '22')), textOnly) # parents of grandfather
                        self.turn_turtle(t, 2) # turn for great grandfather's side (grandfather)
                        if t == self.dad_side:
                            self.draw_y(t, self.get_member(int(str(x) + '221')), '', textOnly) # parents of great grandfather (grandfather)
                            t.lt(45)
                            t.fd(75)
                            t.penup()
                            t.fd(15)
                            t.color(self.dad_sideFontColor)
                            t.write(self.get_member(int(str(x) + '222')), font= ('Arial', 10, 'bold'))
                            t.color(self.dad_sideDrawColor)
                            t.bk(90)
                            if not textOnly:
                                t.pendown()
                            t.rt(45)
                        else:
                            self.draw_y(t, self.get_member(int(str(x) + '221')), self.get_member(int(str(x) + '222')), textOnly) # parents of great grandfather (grandfather)
            
                        # get in position for great grandmother's parents(grandfather)
                        t.bk(75)
                        # move a little less right so doesn't interfere with rest of family tree
                        if t == self.mom_side:
                            t.lt(90)
                        else:
                            t.rt(90)
                        t.color(self.bgColor)
                        t.fd(75)
                        t.bk(75)
                        if t == self.mom_side:
                            t.color(self.mom_sideDrawColor)
                            t.rt(5)
                        else:
                            t.color(self.dad_sideDrawColor)
                            t.lt(5)
                        self.draw_y(t, self.get_member(int(str(x) + '211')), self.get_member(int(str(x) + '212')), textOnly) # parents of great grandmother (grandfather)
                        t.penup()
                        t.goto(0, 0)
                        # get correct orientation
                        if t == self.mom_side:
                            t.setheading(180)
                        else:
                            t.setheading(0)


                    if self.level >= 3:  
                        # get in position for parents of grandmother
                        t.fd(75)
                        self.turn_turtle(t, 1)
                        if not textOnly:
                            t.pendown() # start drawing again
                        
                        self.draw_y(t, self.get_member(int(str(x) + '11')), self.get_member(int(str(x) + '12')), textOnly) # parents of grandmother

                        if self.level == 3:
                            t.penup()
                            t.goto(0, 0)
                            if t == self.mom_side:
                                t.setheading(180)
                            else:
                                t.setheading(0)
                                
                        if self.level >= 4:
                            
                            # turn for great grandfather's side (grandmother)
                            self.turn_turtle(t, 2)
                            t.color(self.bgColor)
                            t.fd(75)
                            t.bk(75)
                            if t == self.mom_side:
                                t.lt(5)
                                t.color(self.mom_sideDrawColor)
                            else:
                                t.rt(5)
                                t.color(self.dad_sideDrawColor)
                            
                            
                            self.draw_y(t, self.get_member(int(str(x) + '121')), self.get_member(int(str(x) + '122')), textOnly) # parents of great grandfather (grandmother)
                            # get in position for great grandmother's parents 
                            t.bk(75)
                            if t == self.mom_side:
                                t.lt(85)
                            else:
                                t.rt(85)
            
                            if t == self.mom_side:
                                self.draw_y(t, self.get_member(int(str(x) + '111')), self.get_member(int(str(x) + '112')),textOnly) # parents of great grandmother (grandmother)
                            
                            else:
                                self.draw_y(t, '', self.get_member(int(str(x) + '112')), textOnly)
                                t.rt(45)
                                t.penup()
                                t.fd(90)
                                t.color(self.dad_sideFontColor)
                                t.write(self.get_member(int(str(x) + '111')), font = ('Arial', 10, 'bold'))
                                t.color(self.dad_sideDrawColor)
                            
                            t.penup()
                            t.goto(0, 0)
                            if t == self.mom_side:
                                t.setheading(180)
                            else:
                                t.setheading(0)
        # hide turtles
        self.mom_side.hideturtle()
        self.dad_side.hideturtle()



class MakeFamilyTreeFrame(Frame):
    '''creates a Make Family Tree Frame window'''
 
    def __init__(self,master):
        '''MakeFamilyTreeFrame()
        creates a new MakeFamilyTreeFrame'''
        Frame.__init__(self,master, bg = 'blue')  # set up as a Tk frame
        self.grid()  # place the frame in the root window
        self.widgets = []
        self.master = master

        # create a text display for instructions
        self.InstrMessageBox = Label(self,text="Select up to which generation of your family you know:", fg='magenta', bg='blue', font = ("Arial", 18, "bold"))
        self.InstrMessageBox.grid(row=1,column=0)
        self.widgets.append(self.InstrMessageBox)

        # create a drop down box to select generation
        self.generList = [
            "Self",
            "Parents",
            "Grandparents",
            "Great-Grandparents",
            ]
        self.gener = StringVar()
        self.gener.set(self.generList[0])
        self.generMenu = OptionMenu(self, self.gener, *self.generList)
        self.generMenu.grid()
        self.widgets.append(self.generMenu)
        self.generMenu.config(font=('Arial', 15, 'bold'), bg='blue', fg='blue')

        self.menu = root.nametowidget(self.generMenu.menuname)
        self.menu.config(font=('Arial', 13, 'normal'), bg='orange')  # Set the dropdown menu's font

        # create a button that user clicks when ready to move on
        self.dButtonGener = Button(self, text = "Done", command = self.get_family_names)
        self.dButtonGener.grid()
        self.widgets.append(self.dButtonGener)


    def get_family_names(self):
        '''MakeFamilyTreeFrame.get_family_names
        asks user if know up to parents grandparents etc.
        then asks user to enter names'''
        # destroy all the widgets
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()
        
        self.generNum = self.generList.index(self.gener.get())      
        self.dirLabel1 = Label(self, text = "Enter the names below.", bg='blue', font=('Arial', 15, 'bold'), fg='orange')
        self.dirLabel2 = Label(self, text = "Leave any you don't know blank.", bg='blue', font=('Arial', 15, 'bold'), fg='orange')
        self.dirLabel1.grid(row=0, column=0)
        self.dirLabel2.grid(row=1, column=0)
        self.widgets.append(self.dirLabel1)
        self.widgets.append(self.dirLabel2)
        
        # if know self or greater
        if self.generNum >= 0:
            self.selfEntry = Entry(self, bg='blue', fg='white', border=4)
            
            self.selfEntryLabel = Label(self, text='You', bg='blue', font=('Arial', 13, 'bold'))
            self.selfEntryLabel.grid(row=2, column=0)
            
            self.selfEntry.grid(row=2, column=1)
                        
            self.widgets.append(self.selfEntry)
            self.widgets.append(self.selfEntryLabel)

        # if know parents of greater
        if self.generNum >= 1:
            self.momEntry = Entry(self, bg='blue', fg='white', border=4)
            self.dadEntry = Entry(self, bg='blue', fg='white', border=4)
            
            self.momEntry.grid(row=3, column=1)
            self.dadEntry.grid(row=4, column=1)
            
            self.momEntryLabel = Label(self, text='Mother', bg='blue', font=('Arial', 13, 'bold'))
            self.momEntryLabel.grid(row=3, column=0)
            self.dadEntryLabel = Label(self, text='Father', bg='blue', font=('Arial', 13, 'bold'))
            self.dadEntryLabel.grid(row=4, column=0)

            self.widgets.append(self.momEntry)
            self.widgets.append(self.dadEntry)
            self.widgets.append(self.momEntryLabel)
            self.widgets.append(self.dadEntryLabel)

        # if know grandparents or greater
        if self.generNum >= 2:
            # dad's parents
            self.dad_dadEntry = Entry(self, bg='blue', fg='white', border=4)
            self.dad_momEntry = Entry(self, bg='blue', fg='white', border=4)
            
            self.dad_dadEntry.grid(row=5, column=1)
            self.dad_momEntry.grid(row=6, column=1)

            self.dad_dadEntryLabel = Label(self, text='Grandfather (father)', bg='blue', font=('Arial', 13, 'bold'))
            self.dad_dadEntryLabel.grid(row=5, column=0)
            self.dad_momEntryLabel = Label(self, text='Grandmother (father)', bg='blue', font=('Arial', 13, 'bold'))
            self.dad_momEntryLabel.grid(row=6, column=0)
                        
            self.widgets.append(self.dad_dadEntry)
            self.widgets.append(self.dad_momEntry)
            self.widgets.append(self.dad_dadEntryLabel)
            self.widgets.append(self.dad_momEntryLabel)

            # mom's parents
            
            self.mom_dadEntry = Entry(self, bg='blue', fg='white', border=4)
            self.mom_momEntry = Entry(self, bg='blue', fg='white', border=4)
            
            self.mom_dadEntry.grid(row=7, column=1)
            self.mom_momEntry.grid(row=8, column=1)

            self.mom_dadEntryLabel = Label(self, text='Grandfather (mother)', bg='blue', font=('Arial', 13, 'bold'))
            self.mom_dadEntryLabel.grid(row=7, column=0)
            self.mom_momEntryLabel = Label(self, text='Grandmother (mother)', bg='blue', font=('Arial', 13, 'bold'))
            self.mom_momEntryLabel.grid(row=8, column=0)
            
            self.widgets.append(self.mom_dadEntry)
            self.widgets.append(self.mom_momEntry)
            self.widgets.append(self.mom_dadEntryLabel)
            self.widgets.append(self.mom_momEntryLabel)

        # if know great-grandparents
        if self.generNum >= 3:
            # dad's dad's parents
            self.dad_dad_dadEntry = Entry(self, bg='blue', fg='white', border=4)
            self.dad_dad_momEntry = Entry(self, bg='blue', fg='white', border=4)
            
            self.dad_dad_dadEntry.grid(row=9, column = 1)
            self.dad_dad_momEntry.grid(row=10, column = 1)

            self.dad_dad_dadEntryLabel = Label(self, text="Great-Grandfather (Father's Father's Father)", bg='blue', font=('Arial', 13, 'bold'))
            self.dad_dad_dadEntryLabel.grid(row=9, column=0)
            self.dad_dad_momEntryLabel = Label(self, text="Great-Grandmother (Father's Father's Mother)", bg='blue', font=('Arial', 13, 'bold'))
            self.dad_dad_momEntryLabel.grid(row=10, column=0)
                        
            self.widgets.append(self.dad_dad_dadEntry)
            self.widgets.append(self.dad_dad_momEntry)
            self.widgets.append(self.dad_dad_dadEntryLabel)
            self.widgets.append(self.dad_dad_momEntryLabel)
            
            # dad's mom's parents
            self.dad_mom_dadEntry = Entry(self, bg='blue', fg='white', border=4)
            self.dad_mom_momEntry = Entry(self, bg='blue', fg='white', border=4)
            
            self.dad_mom_dadEntry.grid(row=11, column=1)
            self.dad_mom_momEntry.grid(row=12, column=1)

            self.dad_mom_dadEntryLabel = Label(self, text="Great-Grandfather (Father's Mother's Father)", bg='blue', font=('Arial', 13, 'bold'))
            self.dad_mom_dadEntryLabel.grid(row=11, column=0)
            self.dad_mom_momEntryLabel = Label(self, text="Great-Grandmother (Father's Mother's Mother)", bg='blue', font=('Arial', 13, 'bold'))
            self.dad_mom_momEntryLabel.grid(row=12, column=0)
            
            self.widgets.append(self.dad_mom_dadEntry)
            self.widgets.append(self.dad_mom_momEntry)
            self.widgets.append(self.dad_mom_dadEntryLabel)
            self.widgets.append(self.dad_mom_momEntryLabel)

            # mom's dad's parents
            self.mom_dad_dadEntry = Entry(self, bg='blue', fg='white', border=4)
            self.mom_dad_momEntry = Entry(self, bg='blue', fg='white', border=4)
            
            self.mom_dad_dadEntry.grid(row=13, column=1)
            self.mom_dad_momEntry.grid(row=14, column=1)

            self.mom_dad_dadEntryLabel = Label(self, text="Great-Grandfather (Mother's Father's Father)", bg='blue', font=('Arial', 13, 'bold'))
            self.mom_dad_dadEntryLabel.grid(row=13, column=0)
            self.mom_dad_momEntryLabel = Label(self, text="Great-Grandmother (Mother's Father's Mother)", bg='blue', font=('Arial', 13, 'bold'))
            self.mom_dad_momEntryLabel.grid(row=14, column=0)
            
            self.widgets.append(self.mom_dad_dadEntry)
            self.widgets.append(self.mom_dad_momEntry)
            self.widgets.append(self.mom_dad_dadEntryLabel)
            self.widgets.append(self.mom_dad_momEntryLabel)

            # mom's mom's parents
            self.mom_mom_dadEntry = Entry(self, bg='blue', fg='white', border=4)
            self.mom_mom_momEntry = Entry(self, bg='blue', fg='white', border=4)
            
            self.mom_mom_dadEntry.grid(row=15, column=1)
            self.mom_mom_momEntry.grid(row=16, column=1)

            self.mom_mom_dadEntryLabel = Label(self, text="Great-Grandfather(Mother's Mother's Father)", bg='blue', font=('Arial', 13, 'bold'))
            self.mom_mom_dadEntryLabel.grid(row=15, column=0)
            self.mom_mom_momEntryLabel = Label(self, text="Great-Grandmother (Mother's Mother's Mother)", bg='blue', font=('Arial', 13, 'bold'))
            self.mom_mom_momEntryLabel.grid(row=16, column=0)
            
            self.widgets.append(self.mom_mom_dadEntry)
            self.widgets.append(self.mom_mom_momEntry)
            self.widgets.append(self.mom_mom_dadEntryLabel)
            self.widgets.append(self.mom_mom_momEntryLabel)

        self.dButtonNames = Button(self, text = "Done", command = self.create_family_dict)
        self.widgets.append(self.dButtonNames)
        self.dButtonNames.grid(row=18, column = 0, columnspan = 2)
        

    def create_family_dict(self):
        '''MakeFamilyTreeFrame.create_dict() -> dict
        creates dictionary of family names gathered in get_family_names method
        as specified in FamilyTree class
        Calls draw_tree method when finished'''
        # create dictionary for family
        self.familyDict = {}

        # add items
        if self.generNum >= 0:
            self.familyDict[0] = self.selfEntry.get()
        
        if self.generNum >= 1:
            self.familyDict[1] = self.momEntry.get()
            self.familyDict[2] = self.dadEntry.get()

        if self.generNum >= 2:
            self.familyDict[22] = self.dad_dadEntry.get()
            self.familyDict[21] = self.dad_momEntry.get()
            self.familyDict[12] = self.mom_dadEntry.get()
            self.familyDict[11] = self.mom_momEntry.get()

        if self.generNum >= 3:            
            self.familyDict[222] = self.dad_dad_dadEntry.get()
            self.familyDict[221] = self.dad_dad_momEntry.get()
            self.familyDict[212] = self.dad_mom_dadEntry.get()
            self.familyDict[211] = self.dad_mom_momEntry.get()
            self.familyDict[122] = self.mom_dad_dadEntry.get()
            self.familyDict[121] = self.mom_dad_momEntry.get()
            self.familyDict[112] = self.mom_mom_dadEntry.get()
            self.familyDict[111] = self.mom_mom_momEntry.get()

        self.draw_tree()

    def draw_tree(self):
        '''MakeFamilyTreeFrame.draw_tree()
        draws family tree'''
        # destory all widgets
        for widget in self.widgets:
            widget.destroy()
            
        FamilyTree(self.master, self.familyDict, self.generNum)


class MenuFrame(Frame):
    ''' creates a Menu Frame window '''

    def __init__(self, master):
        '''MenuFrame(master)
        creates a MenuFrame window'''
        Frame.__init__(self, master, bg = 'blue') # set up the Frame
        self.grid()
        self.master = master
        self.widgets = [] # list containing all of the widgets
        self.create_menu()
        

    def UserFamilyTree(self):
        '''MenuFrame.UserFamilyTree()
        uses MakeFamilyTreeFrame class'''
        self.destroy() # just clear frame for MakeFamilyTreeFrame
        MakeFamilyTreeFrame(root)

    def quit(self):
        '''MenuFrame.quit()
        closes window'''
        self.destroy()
        GoodByeFrame(self.master)

    def create_menu(self):
        '''MenuFrame.create_menu()
        creates the menu in which the user selects
        what they want to do'''
        # give user directions on what to do 
        self.welcomeLabel1 = Label(self, text="Hi, click one of the button below to ", font=("Arial", 25, "bold"), fg = 'gray', bg = 'blue')
        self.welcomeLabel2 = Label(self, text="enter your own family's names and see", font=("Arial", 25, "bold"), fg = 'gray', bg = 'blue')
        self.welcomeLabel3 = Label(self, text="your own family tree drawn in real time!", font=("Arial", 25, "bold"), fg = 'gray', bg = 'blue')
        
        # place labels in frame
        self.welcomeLabel1.grid(row=0, column=0)
        self.welcomeLabel2.grid(row=1, column=0)
        self.welcomeLabel3.grid(row=2, column=0)
        
        # add labels to list of widgets
        self.widgets.append(self.welcomeLabel1)
        self.widgets.append(self.welcomeLabel2)
        self.widgets.append(self.welcomeLabel3)

        # create buttons for user and my family tree
        self.userTreeButton = Button(self, text="Create Your Own Tree", command=self.UserFamilyTree, activeforeground='blue', font=('Arial', 20, 'normal'), fg='magenta')

        # place button in frame
        self.userTreeButton.grid(row=4, column=0)

        # add buttons to list of widgets
        self.widgets.append(self.userTreeButton)

        # create button for quitting program
        self.quitButton = Button(self, text="Quit", command=self.quit, activeforeground='blue', font=('Arial', 20, 'normal'), fg = 'red')
        self.quitButton.grid(row=5, column=0)
        self.widgets.append(self.quitButton)


class GoodByeFrame(Frame):
    ''' creates a good bye frame'''
    
    def __init__(self, master):
        '''GoodByeFrame(master)
        creates a GoodByeFrame'''
        Frame.__init__(self, master, bg='blue')
        self.grid()

        self.goodByeLabel = Label(self, text = "GOODBYE!!", font=("Arial", 30, "bold"), bg = 'lightblue')
        self.goodByeLabel.grid(row=0, column=0)

        master.after(5000, master.destroy)
    

root = Tk()
root['bg'] = 'blue'
MenuFrame(root)
root.mainloop()
