import Tkinter as tk
import Database as DB
import Widgets as wd

class NewVisit:
    'App for creating a new student in the database'
    #################   CONSTRUCTOR   #################
    def __init__(self, db):
        '''
        Initialize a gui for the insertion of students infomation'
        INPUT: db - the databse
        '''
        #create a root container
        self.root = tk.Tk()
        self.root.title("New Visit")

        #upper parts : display crucial infomation

        #Labels: to the left of the window
        idL = wd.LabelWidget(self.root, 0, 0, "'Picture'")
        dateL = wd.LabelWidget(self.root, 0, 4, "Get Student Name")
        startL = wd.LabelWidget(self.root, 1, 0, "Button for New")



        #lower part, display long text
        #Visit NOTE
        noteL = wd.LabelWidget(self.root, 0, 5, "Visit Note")
        noteL.grid(columnspan=2)
        noteE = wd.TextWidget(self.root, 0, 6, 150, 10, "Insert Note")
        noteE.grid(columnspan = 2)
        oldNote = noteE.getVal() #store the old note for comparision later


        #Log display to the gui
        log = wd.LabelWidget(self.root, 0, 14, "Status", 30)
        log.config(width = 100)
        #having the log display to span 2 columns
        log.grid(columnspan = 2)


        def ins():
            'method to call for the Submit button'
            if idE.getVal() not in db.idList():
                log.set("ID not found. Please insert student first!")
            else:
                #Checking if any of the entry fields is empty
                nt = "" if oldNote == noteE.getVal() else noteE.getVal()

                comm = "" if oldComments == comments.getVal() else comments.getVal()

                obs = "" if oldObservations == observations.getVal() else observations.getVal()

                rec = "" if oldRecommendations == observations.getVal() else recommendations.getVal()
                try:
                    #interaction witht the Database object
                    db.insVisit(idE.getVal(), dateE.getVal(), startE.getVal(), showVar.get(), TopicE.getVal(), nt, comm, obs, rec)
                    #report that the insertion is success
                    log.set("Success")
                except Exception, value:
                    #If insertion fail, report to the Log display
                    log.set(value)

        #A Submit button
        submit = tk.Button(self.root, text="Submit", command = ins)
        submit.grid(column = 0, row=13, columnspan=2)

        #make the window appears
        self.root.mainloop()



if __name__ == "__main__":
    #connecting with the database
    db = DB.Database('database/cup.db')
    new = NewVisit(db)
