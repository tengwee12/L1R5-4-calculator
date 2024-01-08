import csv
import tkinter
from tkinter import *
from tkinter import filedialog
root = Tk()


def contains_num(strings):
    answer = False
    for i in strings:
        if i.isnumeric() == True:
            answer = True
        else:
            pass
    return answer


def PROCESS():
    infile = open(target_file_name,"r")
    lines = csv.reader(infile,delimiter= " ")
    ##RAW TEXT1.txt
    print("")

    infile2 = open(reference_file_name,"r")                                            #cross reference to raw file data and actual name can be added to presentation
    lines2 = csv.reader(infile2,delimiter = " ")

    main_ref = []

    for i in lines2:
        tmp = []
        for j in i:
            if j == "":
                pass
            else:
                tmp.append(j)   #tmp is raw form of reference array
                
        tmp2 = []
        name = ""
        for k in range(1,len(tmp)):
            if contains_num(tmp[k]) == False:    #filter out true name with IC number
                if k == 1:
                    name += tmp[k]
                else:
                    name += " "
                    name += tmp[k]
            else:
                tmp2.append(tmp[k]) #[NRIC,Name] --> tmp2 is revised array with only name and IC number
                break
        tmp2.append(name)
            
        #print(name)
        main_ref.append(tmp2)

    main_ref_nd = []

    for i in main_ref:
        if i in main_ref_nd:
            pass
        else:
            main_ref_nd.append(i)  #Creates a new array identical but without the duplicates, this new array will be the reference array

    print(main_ref_nd) 

    main = []
    for i in lines:
        sub = []
        for j in i:
            if j == "":
                pass
            else:
                sub.append(j)
        main.append(sub)    #gets abridged version of text in csv file, without preprocessing to add name and sub code
    global students    
    students = []       #Students is the raw array in which the actual O level calculation part will work on, includes ALL student information
    for i in main:  #i represents individual student, each round of for loop only works for one individual student 
        #print(i)
        global std
        std = []
        PTR = 0
        particulars = []
        while i[PTR][0] != "0" and i[PTR][0] != "2":
            particulars.append(i[PTR])
            PTR += 1        #Pointer ends up in exact position where the results part starts 
            
        P1 = []                         #P1 is the revised version of particulars that processes and gets only name and IC
        
        P1.append(particulars[len(particulars)-1][0:9])     #Appending only the NRIC element to particular since it is the consistent element 

        for h in main_ref_nd:
            if h[0] == P1[0]:
                P1.append(h[1])         # Finds match for NRIC in the reference array, then inserts the correct name into P1
            else:
                pass

        std.append(P1)                                  #P1 now is inserted as two elements, Name and NRIC, which is compatible with other code(otp array), as it only
                                                        #two elements
        for k in range(PTR,len(i)-1): #takes out main subject codes and inserts them into individual student std information array
            finding(i[k])                  #uses the find function to get appropriate matching subject name to the 
        if len(std) < 4:                   #original subject code in raw file snippet/ finding function has been expanded 
            pass                           #to resolve conflict as some subjects like higher art and HCL have no whitespace between them
        else:                              #to get discrete subject elements, expanded also to do remaining process and add operations 
            students.append(std)           #originally intended for this block of code  

def finding(inputs):
    slist = [["1128","EL"],["2272","CombHum"],["2273","CombHum"],
             ["2274","CombHum"],["4047","A Math"],["4048","E Math"],["6091","Phy"]
             ,["6092","Chem"],["6093","Bio"],["1116","HCL"],["2174","P.Hist"],["2065","P.Lit",],["2236","P.Geog"],
             ["2272","CombHum"],["2273","CombHum"],["6085","Music"],["6086","Higher Music"],["6087","F&N"]
             ,["6123","Art"],["6124","Higher Art"],["7155","Computing"],["1133","MSP"],["1166","CSP"],["3261","Jap"]]
             
    if len(inputs) > 7:
        #print(inputs)
        for i in slist:
            if i[0] == inputs[1:5]:
                if inputs[5].isnumeric() == False:      #Weeds out people who did not take the exam, therefore getting non numeric "X" as result
                    pass
                else:
                    std.append([i[1],int(inputs[5])])
        for i in slist:
            if i[0] == inputs[8:12]:
                if inputs[12].isnumeric() == False:
                    pass
                else:
                    std.append([i[1],int(inputs[12])])
    else:
        #print(inputs)
        for i in slist:
            if i[0] == inputs[1:5]:
                if inputs[5].isnumeric() == False:
                    pass
                else:
                    std.append([i[1],int(inputs[5])])
                break
                                             

ValidSub1 = [["EL","HCL"],      #List of valid subjects that the student can be counted for for each subject in each band of L1R5
            ["CombHum","H.Art","H.Music","MSP","BHSI","CSP"],
            ["E Math","A Math","Bio","Chem","Phy"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","P.Lit","P.Geog","P.Hist","CSP"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap","CSP"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap","CSP"]]

ValidSub2 = [["EL","HCL"],       #List of valid subjects that the student can be counted for for each subject in each band of L1R5
            ["P.Lit","P.Geog","P.Hist","CombHum","A Math","E Math","H.Art","H.Music","Phy","Chem","Bio","MSP","BHSI","CSP"],
            ["P.Lit","P.Geog","P.Hist","CombHum","A Math","E Math","H.Art","H.Music","Phy","Chem","Bio","MSP","BHSI","CSP"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap","CSP"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap","CSP"]]

def L1R5Calc(student,choice):#Calculates the L1R5 score for each student put into function parameters as 2d list 
    otp = []
    otp.append(student[0][0])   #otp is the final "presentation" array, as such elements of P1 can be added in individually to be separate
    otp.append(student[0][1])   #elements for better viewing and data manipulation in the resulting csv file.
    
    if choice == 1:
        ValidSub = ValidSub1
    else:
        ValidSub = ValidSub2
    std_temp = student[1:]
    L1R5 = 0
    std = []    #valid subjects for l1r5 component that student actually takes
    for g in ValidSub[0]:
        for n in range(len(std_temp)):
            if std_temp[n][0] == g:
                std.append(std_temp[n])
    best = std[0]
    for m in std:
        if m[1] < best[1]:    #Gets the subject in the valid subjects where the student in question scored the 
            best = m          #best in for L1 since got special concession rule for HCL and CL, best is one complete
    if best[0] == "HCL":      #subject unit as and such is "final" meaning that it is directly added to L1R5, being "final"
        for f in std_temp:    #also means that it is subject to presentation, as such it is added to otp array
            if f[0] == "CL":
                std_temp.remove(f)
    print(std)
    print(best)
    L1R5 += best[1]
    otp.append(best[0])        
    otp.append(best[1])     #Adding to otp "presentation" array as before the main loop to calculate, a preliminary calculation is
    std_temp.remove(best)   #done for the l1r5 due to potential CL/HCL conflict, need to add that step to final presentation
                            #as well as the L1R5
    for i in ValidSub[1:]:
        std = []
        for j in i:
            for k in range(len(std_temp)):
                if std_temp[k][0] == j:
                    std.append(std_temp[k])
                else:
                    pass
        print(std)
        if len(std) == 0:
            break
        else:
            best = std[0]
            for m in std:
                if m[1] < best[1]:    #Gets the subject in the valid subjects where the student in question scored the best in
                    best = m
            print(best)
            L1R5 += best[1]
            otp.append(best[0])
            otp.append(best[1])
            std_temp.remove(best)   #remove the counted subject from the main list of subjects for the remainder of L1R5 to prevent multiple counts
    if choice == 1:
        print(student[0][1] + " has a L1R5 of " + str(L1R5)) #Final output message
    else:
        print(student[0][1] + " has a L1R4 of " + str(L1R5)) #Final output message
    print("\t")
    print("\t")
    otp.append(L1R5)
    if len(otp) < 4:
        return []
    else:
        return otp

##for i in students:
##    print(i)
##    print("")
##    L1R5Calc(i)




ValidSubA = [["EL"],       #List of valid subjects that the student can be counted for for each subject in each band of L1R5
            ["P.Lit","P.Geog","P.Hist","CombHum","H.Art","H.Music","Art","Music"],
            ["P.Lit","P.Geog","P.Hist","CombHum","H.Art","H.Music","Art","Music","E Math","A Math","CL","HCL"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap"]]

ValidSubB = [["EL"],       #List of valid subjects that the student can be counted for for each subject in each band of L1R5
            ["E Math","A Math"],
            ["P.Lit","P.Geog","P.Hist","CombHum","H.Art","H.Music","Art","Music"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap"]]

ValidSubC = [["EL"],       #List of valid subjects that the student can be counted for for each subject in each band of L1R5
            ["E Math","A Math"],
            ["Phy","Chem","Bio"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap"]]

ValidSubD = [["EL"],       #List of valid subjects that the student can be counted for for each subject in each band of L1R5
            ["E Math","A Math"],
            ["Phy","Chem","Bio","Art","H.Art"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap"],
            ["E Math","A Math","Bio","Chem","Phy","CombHum","H.Art","H.Music","MSP","BHSI","EL","HCL","CL","P.Lit","P.Geog","P.Hist","Art","Music","Jap"]]

def ELR2B2Calc(student,choice): #Calculates the ELR2B2 score for each student put into function parameters as 2d list 
    if choice == "A":
        ValidSub = ValidSubA
    elif choice == "B":
        ValidSub = ValidSubB
    elif choice == "C":
        ValidSub = ValidSubC
    elif choice == "D":
        ValidSub = ValidSubD
        
    otp = []
    otp.append(student[0][0])
    otp.append(student[0][1])
    
    std_temp = student[1:]  #Only the subjects and results part of the student information, therefore omitting the name, to be slowly eliminated based on best result
    ELR2B2 = 0
    std = []    #Counting only the subjects that is valid for the band, and is also taken by the student, must show subject name and results
    init_compare = ["HCL","CL"]
    for g in init_compare:
        for n in range(len(std_temp)):
            if std_temp[n][0] == g:
                std.append(std_temp[n])
    if len(std) < 2 :
        pass
    else:
        worst = std[0]
        print(std)
        for w in std:
            if w[1] > worst[1]: #Gets the worst out of the std array containing student results for only HCl and Cl to remove out of main array containing student results
                worst = w
        print(worst)
        print( worst[0] + " will be removed as it is the worst out of HCl and CL")
        print("\t")
        std_temp.remove(worst)  #Special Move for ELR2B2 calculation, best out of CL and HCl remains in the std_temp list to be evaluated, as impossible to evaluate both
                                #at the same time

    for i in ValidSub:
        print(std_temp)
        std = []    #Counting only the subjects that is valid for the band, and is also taken by the student, must show subject name and results
        for j in i:
            for k in range(len(std_temp)):
                if std_temp[k][0] == j:
                    std.append(std_temp[k])
                else:
                    pass
        print(std)
        if len(std) == 0:
            return []
        best = std[0]
        for m in std:
            if m[1] < best[1]:    #Gets the subject in the valid subjects where the student in question scored the best in
                best = m
        print(best)
        otp.append(best[0])
        otp.append(best[1])
        ELR2B2 += best[1]
        std_temp.remove(best)   #remove the counted subject from the main list of subjects for the remainder of L1R5 to prevent multiple counts
    print(student[0][1] + " has a ELR2B2 of " + str(ELR2B2)) #Final output message
    print("\t")
    print("\t")
    otp.append(ELR2B2)
    if len(otp) < 4:
        return []
    else:
        return otp



def output(final_output):
    from csv import writer
    for p in final_output:
        with open("output.csv",'a+',newline ='') as write_obj:
            print(p)
            csv_writer = writer(write_obj)
            csv_writer.writerow(p)


def target_file_clicked():
    file_path = filedialog.askopenfilename()
    global target_file_name
    target_file_name = ""
    for i in range(len(file_path)):
        if file_path[i] == "/":
            target_file_name = ""
        else:
            target_file_name += file_path[i]
    print(target_file_name)
    target_file_button["state"] = DISABLED
    l1r5.pack()
    l1r4.pack()
    elr2b2A.pack()
    elr2b2B.pack()
    elr2b2C.pack()
    elr2b2D.pack()
    return PROCESS()


def reference_file_clicked():
    file_path = filedialog.askopenfilename()
    global reference_file_name
    reference_file_nam
    e = ""
    for i in range(len(file_path)):
        if file_path[i] == "/":
            reference_file_name = ""
        else:
            reference_file_name += file_path[i]
    print(reference_file_name)
    reference_file_button["state"] = DISABLED
    global target_file_button
    target_file_button = Button(root,text="SELECT TARGET FILE",command=target_file_clicked,padx=100)
    target_file_button.pack()


def executeL1R5():
    final_output = []
    final_output.append(["NRIC","Name","Scores","","","","","","","","","","","","L1R5"])
    for i in students:
        final_output.append(L1R5Calc(i,1))
    for h in final_output:
        if h == []:
            final_output.remove(h)
    output(final_output)
        
def executeL1R4():
    final_output = []
    final_output.append(["NRIC","Name","Scores","","","","","","","","","","L1R4"])
    for i in students:
        final_output.append(L1R5Calc(i,2))
    for h in final_output:
        if h == []:
            final_output.remove(h)
    output(final_output)
    
def executeELR2B2A():
    final_output = []
    final_output.append(["NRIC","Name","Scores","","","","","","","","","","ELR2B2"])
    for i in students:
        print(i)
        final_output.append(ELR2B2Calc(i,"A"))
    for h in final_output:
        if h == []:
            final_output.remove(h)
    output(final_output)
        
def executeELR2B2B():
    final_output = []
    final_output.append(["NRIC","Name","Scores","","","","","","","","","","ELR2B2"])
    for i in students:
        print(i)
        final_output.append(ELR2B2Calc(i,"B"))
    for h in final_output:
        if h == []:
            final_output.remove(h)
    output(final_output)
    
def executeELR2B2C():
    final_output = []
    final_output.append(["NRIC","Name","Scores","","","","","","","","","","ELR2B2"])
    for i in students:
        print(i)
        final_output.append(ELR2B2Calc(i,"B"))
    for h in final_output:
        if h == []:
            final_output.remove(h)
    output(final_output)
    
def executeELR2B2D():
    final_output = []
    final_output.append(["NRIC","Name","Scores","","","","","","","","","","ELR2B2"])
    for i in students:
        print(i)
        final_output.append(ELR2B2Calc(i,"D"))
    for h in final_output:
        if h == []:
            final_output.remove(h)
    output(final_output)

reference_file_button = Button(root,text="SELECT REFERENCE FILE",command=reference_file_clicked,padx=100)
reference_file_button.pack()

l1r5 = Button(root,text="L1R5 Calculation",command=executeL1R5)
l1r4 = Button(root,text="L1R4 Calculation",command=executeL1R4)
elr2b2A = Button(root,text="ELR2B2 Category A",command=executeELR2B2A)
elr2b2B = Button(root,text="ELR2B2 Category B",command=executeELR2B2B)
elr2b2C = Button(root,text="ELR2B2 Category C",command=executeELR2B2C)
elr2b2D = Button(root,text="ELR2B2 Category D",command=executeELR2B2D)



root.mainloop() 

##print("1.L1R5")
##print("2.L1R4")
##print("3.L1R2B2")
##
##print("")
##
##choice_calc = input("CALCULATION FOR WHICH METRIC: ")
##final_output = []
##if choice_calc != "3":
##    for i in students:
##        print(i)
##        print("")
##        final_output.append(L1R5Calc(i,int(choice_calc)))
##        
##elif choice_calc == "3":
##    print("")
##    print("A: CAT A")
##    print("B: CAT B")
##    print("C: CAT C")
##    print("D: CAT D")
##    elr2b2_choice = input("ENTER CHOICE FOR TYPE OF L1R2B2 TO CALCULATE: " )
##    for i in students:
##        print(i)
##        print("")
##        final_output.append(ELR2B2Calc(i,elr2b2_choice))
##
##from csv import writer
##
##opfile = input("PLEASE GIVE THE NAME OF THE OUTPUT FILE : ")
##for p in final_output:
##    with open(str(opfile) + ".csv",'a+',newline ='') as write_obj:
##        print(p)
##        csv_writer = writer(write_obj)
##        csv_writer.writerow(p)

       
   


        
            
