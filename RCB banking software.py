# Banking-Software
A simple software coded by me for school project at 11th standard @ age-16. Its a compact banking software created by using python and mysql-connector. It allows users to create account, make transcation and avail loan.
#PROJECT RCB

#LIBRARY USED IN THE PROGRAM
import mysql.connector as sqltor
import random
import stdiomask
import os
from datetime import datetime
from tabulate import tabulate

#FUNCTIONS
def date():
    dates=datetime.date(datetime.now())
    return dates
def time():
    times=datetime.time(datetime.now())
    return times

def clear():
    clr=os.system('cls')
    return clr

print('''                                                                                                BCDBANKMANAGEMENT
======================================================================================================================================================

RCBG BANK WELCOMES YOU!!!!!!!!!!!!

RCB BANK PROVIDES CUSTOMERS A NEW EXPERIENCE IN BANKING BY MAKING TRANSACTIONS SECURELY AND EASILY.
CUSTOMERS DATA IS STORED IN DATABASES SAFELY.  YOU CAN ACCESS IT FROM ANY PART OF THE WORLD.
WE ARE PROVIDING GREAT INTERESTS ON YOUR DEPOSITS.  IF ANY MALPRACTICES FOUND, THEY WOULD BE PUNISHED UNDER SECTION 1344.
TRANSACTION DETAILS, WITHDRAW, DEPOSITS WILL BE PRESERVED PRIVATELY. WE ARE SERVING PEOPLE FOR THEIR LIVES MORE THAN 4 DECADES AND SUCCEEDED IN IT. 

======================================================================================================================================================= ''')     
clear()



#CONNECTION AND CREATION OF DATABASE
a=sqltor.connect(host='localhost',user='root',passwd='vivek')
b=a.cursor()
b.execute('''create  database if not exists bank''')
b.execute('''use bank''')
b.execute('''create table if not exists employee
(Admin_id integer primary key,
Password varchar(20),
Name varchar(20),
Age integer ,
Mobile_number varchar(10),
Work_experience integer)''')
b.execute('''create table if not exists bank_creating
(Account integer primary key,
Password varchar(20),
Name varchar(50),
Age integer ,
type varchar(2),
Amount integer,
loan_name varchar(20) default null)''')
b.execute('''create table if not exists bank_transfer
(Account integer,
Password varchar(20),
type char(2),
date_of_trans date,
time_of_trans time,
Amount integer)''')

#MENU
while(1):
    clear()
    print('LOGIN AS')
    print('1.BANK OFFICER\n2.BANK CUSTOMER\n3.EXIT')
    cho=int(input('ENTER YOUR CHOICE: '))
    if cho==2:
        while(1):
            clear()
            print('\t\tMENU\n1.NEW CUSTOMER\n2.EXISTING CUSTOMER\n3.EXIT')
            ch=int(input('ENTER YOUR CHOICE: '))
            if ch==1:
                def insert():
                    account=random.randrange(1000,9999)
                    print('YOUR ACCOUNT NUMBER IS: ',account)
                    pin=stdiomask.getpass('ENTER YOUR PASSWORD: ')
                    name=input('ENTER YOUR NAME : ')
                    age=int(input('ENTER YOUR AGE : '))
                    actype=input('ENTER THE TYPE[C/S]: ')
                    loan='NULL'
                    if actype.lower() =='s' or 'c':
                        amount=int(input('ENTER THE AMOUNT YOU WANT TO DEPOSIT INITIALLY: '))
                        if amount>=1000:
                            b.execute('''insert into bank_creating values(%s,%s,%s,%s,%s,%s,%s);''', (account,pin,name,age,actype,amount,loan))
                            print('ACCOUNT SUCCESSFULLY CREATED')
                        else:
                            print('THE MINIMUM AMOUNT IS 1000 YOU HAVE GIVEN LESS THAN THAT')
                    else:
                        print('WRONG INPUT ')
                    a.commit()
                
                insert()
                input()
                break
            elif ch==2:
                b.execute('''select*from bank_creating;''')
                data=b.fetchall()
                c=int(input('ENTER YOUR ACCOUNT NUMBER: '))
                d=stdiomask.getpass('ENTER YOUR PASSWORD: ')
                input()
                for i in data :
                    if i[0]==c:
                        if i[1]==d:
                            def modify():
                                print ('1.PIN\n2.NAME\n3.AGE\n4.TYPE OF ACCOUNT ')
                                Ch=int(input('ENTER YOUR CHOICE: '))
                                if Ch==1:
                                    b.execute('select * from bank_creating')
                                    Data=b.fetchall()
                                    d=int(input('ÉNTER YOUR ACCOUNT NUMBER: '))
                                    e=stdiomask.getpass('ENTER YOUR OLD PASSWORD: ')
                                    for i in Data:
                                        if i[0]==d:
                                            f=stdiomask.getpass('ENTER YOUR NEW PASSWORD: ')
                                            g=input('DO YOU WANT TO CHANGE PASSWORD [y/n]: ')
                                            if g.lower()=='y':
                                                b.execute('''update bank_creating set Password='{}' where Account={} '''.format(f,d))
                                                print('SUCESSFULLY MODIFIED')
                                            elif g.lower()=='n':
                                                print('PROCESS CANCELLED')
                                    input()
                                elif Ch==2:
                                    b.execute('select*from bank_creating')
                                    data=b.fetchall()
                                    d=int(input('ENTER YOUR ACCOUNT NUMBER: '))
                                    A=input('ENTER YOUR OLD NAME: ')
                                    for i in data:
                                        if i[0]==d:
                                            B=input('ENTER YOUR NEW NAME: ')
                                            g=input('DO YOU WANT TO CHANGE NAME [y/n]: ')
                                            if g.lower()=='y':
                                                b.execute('''update bank_creating set Name='{}' where Account={} '''.format(B,d))
                                                print('SUCESSFULLY MODIFIED')
                                            elif g.lower()=='n':
                                                print('PROCESS CANCELLED')
                                    input()
                                elif Ch==3:
                                    b.execute('select*from bank_creating')
                                    data=b.fetchall()
                                    d=int(input('ENTER YOUR ACCOUNT NUMBER: '))
                                    A=int(input('ENTER YOUR OLD AGE: '))
                                    for i in data:
                                        if i[0]==d:
                                            B=int(input('ENTER YOUR NEW AGE: '))
                                            g=input('DO YOU WANT TO CHANGE AGE [y/n]: ')
                                            if g.lower()=='y':
                                                b.execute('''update bank_creating set Age={} where Account={}'''.format(B,d))
                                                print('SUCESSFULY MODIFIED')
                                            elif g.lower()=='n':
                                                print('PROCESS CANCELLED')
                                    input()
                                elif Ch==4:
                                    b.execute('select*from bank_creating')
                                    data=b.fetchall()
                                    d=int(input('ENTER YOUR ACCOUNT NUMBER: '))
                                    A=input('ENTER YOUR CURRENT TYPE OF YOUR ACCOUNT: ')
                                    for i in data:
                                        if i[0]==d:
                                            B=input('ENTER YOUR NEW TYPE OF YOUR ACCOUNT: ')
                                            g=input('DO YOU WANT TO CHANGE THE TYPE OF YOUR ACCOUNT [y/n]: ')
                                            if g.lower()=='y':
                                                b.execute('''update bank_creating set type='{}' where Account={} '''.format(B,d))
                                                print('SUCESSFULLY MODIFIED')
                                            elif g.lower()=='n':
                                                print('PROCESS CANCELLED')
                                    input()
                            def withdraw():
                                D=stdiomask.getpass('ENTER PASSWORD : ')
                                A=int(input('ENTER THE AMOUNT YOU WANT TO WITHDRAW: '))
                                z=date()
                                x=time()
                                types='W'
                                b.execute('select * from bank_creating')
                                da=b.fetchall()
                                for i in da:
                                    if i[0]==c:
                                        if i[5]>A:
                                            b.execute('''update bank_creating set Amount=Amount-{}'''.format(A))
                                            print('SUCESSFULLY WITHDRAW AMOUNT')
                                            print('YOUR CURRENT BALANCE IS :',i[5]-A)
                                            b.execute('''insert into bank_transfer values(%s,%s,%s,%s,%s,%s)''',(c,D,types,z,x,A))
                                          
                                        elif i[5]==1000:
                                            print('''YOU CAN'T WITHDRAW BECAUSE YOU HAVE REACHED THE MINIMUM AMOUNT''')
                                        else:
                                            print('AVAILABLE BALANCE',i[5])
                                            print('YOU HAVE EXCEEDED YOUR CURRENT BALANCE')
                                input()

                                        
                                a.commit()
                            def deposit():
                                D=stdiomask.getpass('ENTER PASSWORD: ')
                                A=int(input('ENTER THE AMOUNT YOUR WANT TO DEPOSIT: '))
                                types='D'
                                z=date()
                                x=time()
                                b.execute('select * from bank_creating')
                                dataas=b.fetchall()
                                for i in dataas:
                                    if i[0]==c:
                                        b.execute('''update bank_creating set Amount=Amount+{}'''.format(A))
                                        print('SUCESSFULLY DEPOSITED YOUR AMOUNT')
                                        print('YOUR CURRENT BALANCE IS :',i[5]+A)
                                        b.execute('''insert into bank_transfer values(%s,%s,%s,%s,%s,%s)''',(c,D,types,z,x,A))
                                input()          
                                a.commit()
                            def customer():
                                b.execute('''select Account,Name,Age,type,Amount,loan_name from bank_creating''')
                                dataa=b.fetchall()
                                c=[i for i in dataa]
                                h=["ACCOUNT","PASSWORD","NAME","AGE","ACC. TYPE","AMOUNT","LOAN NAME"]
                                print(tabulate(c,h,tablefmt="grid"))
                                
                                a.commit()
                                input()
                            def trans():
                                b.execute('''select * from bank_transfer''')
                                dat=b.fetchall()
                                t=[j for j in dat]
                                h=["ACCOUNT","PASSWORD","TYPE","DATE OF TRANSACTION","TIME OF TRANSACTION","AMOUNT"]
                                print(tabulate(t,h,tablefmt="grid"))
                                a.commit()
                                input()
                            def LOAN():
                                b.execute('''select * from bank_creating''')
                                data=b.fetchall()
                                A=int(input('ENTER YOUR ACCOUNT NUMBER: '))
                                B=stdiomask.getpass('ENTER YOUR PASSWORD: ')
                                for i in data:
                                    if i[0]==A:
                                        if i[6]=='NULL':
                                            print('''MENU for loan
                         1. AGRICULTURE LOAN
                         2. HOME LOAN
                         3. PERSONAL LOAN
                         4. BUSINESS LOAN
                         5. EDUCATION LOAN
                         6. VENTURE CAPITAL
                         7. EXIT''')
                                            ch=int(input('ENTER YOUR LOAN TYPE: '))
                                            def loan(a=100000,i=7,t=5):
                                                a= float(a)
                                                i= float(i)
                                                t= float(t)
                                                interestCalculation = i / 100
                                                numberOfPayments = t*12
                                                monthlyRepaymentCost = a * interestCalculation * (1+interestCalculation) * numberOfPayments / ((1+interestCalculation) * numberOfPayments - 1)
                                                totalCharge = (monthlyRepaymentCost * numberOfPayments) - a
                                                print("You  borrowed ₹." + str(a) + " over " + str(t) + " years, with an interest rate of " + str(i) + "%!")
                                                print("Your monthly repayment will be ₹.%.2f " % monthlyRepaymentCost)
                                                print("The total charge on this loan will be ₹.%.2f " % totalCharge)
                                            if ch==1:
                                                a= input("How much do you want to borrow? \n")
                                                i= 7
                                                t=10
                                                print('Agriculture loan rate is',i,'\ntime of repay is',t,'years')
                                                bz='agricultural loan'
                                                b.execute('update bank_creating set loan_name=(%s) where Account=(%s)',(bz,A))
                                                b.execute('update bank_creating set Amount=(%s) where Account=(%s)',(a-monthyRepaymentCost,A))
                                                input()
                                            elif ch==2:
                                                a= input("How much do you want to borrow? \n")
                                                i= 6.8
                                                t=5
                                                print('Home loan rate is',i,'\ntime of repay is',t,'years')
                                                bz='home loan'
                                                b.execute('update bank_creating set loan_name=(%s) where Account=(%s)',(bz,A))
                                                b.execute('update bank_creating set Amount=Amount+(%s) where Account=(%s)',(a-monthyRepaymentCost,A))
                                                input()
                                            elif ch==3:
                                                a= input("How much do you want to borrow? \n")
                                                i= 9
                                                t=7
                                                print('Personal loan rate is',i,'\ntime of repay is',t,'years')
                                                bz='personal loan'
                                                b.execute('update bank_creating set loan_name=(%s) where Account=(%s)',(bz,A))
                                                b.execute('update bank_creating set Amount=Amount+(%s) where Account=(%s)',(a-monthyRepaymentCost,A))
                                                input()
                                            elif ch==4:
                                                a= input("How much do you want to borrow? \n")
                                                i= 16
                                                t=10
                                                print('Business loan rate is',i,'\ntime of repay is',t,'years')
                                                bz='business loan'
                                                b.execute('update bank_creating set loan_name=(%s) where Account=(%s)',(bz,A))
                                                b.execute('update bank_creating set Amount=Amount+(%s) where Account=(%s)',( a-monthyRepaymentCost ,A))
                                                input()
                                            elif ch==5:
                                                a= input("How much do you want to borrow? \n")
                                                i= 5
                                                t=3
                                                print('Educational loan rate is',i,'\ntime of repay is',t,'years')
                                                bz='educational loan'
                                                b.execute('update bank_creating set loan_name=(%s) where Account=(%s)',(bz,A))
                                                b.execute('update bank_creating set Amount=Amount+(%s) where Account=(%s)',(a-monthyRepaymentCost,A))
                                                input()
                                            elif ch==6:
                                                a= input("How much do you want to borrow? \n")
                                                i= 30
                                                t=20
                                                print('Venturecap loan rate is',i,'\ntime of repay is',t,'years')
                                                bz='venturecap loan'
                                                b.execute('update bank_creating set loan_name=(%s) where Account=(%s)',(bz,A))
                                                b.execute('update bank_creating set Amount=Amount+(%s) where Account=(%s)',(a-monthyRepaymentCost,A))
                                                input()
                                            elif ch==7:
                                                break
                                            loan(a,i,t)
                                        else:
                                            print('YOU ARE ALREADY IN ',i[6])
                                input()

                            while (1):
                                clear()
                                print('1.MODIFY\n2.WITHDRAW\n3.DEPOSIT\n4.VIEW YOUR PROFILE\n5.TRANSACTION DETAILS\n6.APPLY FOR LOAN\n7.EXIT')
                                CH=int(input('ENTER YOUR CHOICE: '))
                                if CH==1:
                                    modify()
                                elif CH==2:
                                    withdraw()
                                elif CH==3:
                                    deposit()
                                elif CH==4:
                                    customer()
                                elif CH==5:
                                    trans()
                                elif CH==6:
                                    LOAN()
                                elif CH==7:
                                    break
            elif ch==3:
                break

    elif cho==1:
        while(1):
            clear()
            print('1.NEW OFFICER\n2.EXISTING OFFICER\n3.EXIT')
            ch=int(input('ENTER YOUR CHOICE: '))
            if ch==1:
                def insert():
                    A=random.randrange(10000,99999)
                    print('YOUR ADMIN ID IS : ',A)
                    B=stdiomask.getpass('ENTER YOUR PASSWORD: ')
                    c=input('ENTER YOUR NAME: ')
                    d=int(input('ENTER YOUR AGE: '))
                    e=input('ENTER YOUR MOBILE NUMBER: ')
                    f=int(input('ENTER YOUR WORK EXPERIENCE: '))
                    if d>18:
                        b.execute('''insert into employee values(%s,%s,%s,%s,%s,%s)''',(A,B,c,d,e,f))
                        print('SUCCESSFULLY ENTERED DETAILS')
                    else:
                        print('''AGE ABOVE 18 IS ONLY VALID''')
                    a.commit()
                insert()
                input()
                break

            elif ch==2:
                b.execute('select*from employee')
                Data=b.fetchall()
                A=int(input('ENTER YOUR ADMIN ID: '))
                B=stdiomask.getpass('ENTER YOUR PASSWORD: ')
                input()
                for i in Data:
                    if i[0]==A:
                        if i[1]==B:
                            def customers():
                                b.execute('select Account,Name,Age,type,Amount,loan_name from bank_creating')
                                d=b.fetchall()
                                A=int(input('ENTER ACCOUNT NUMBER TO BE SEARCHED: '))
                                for i in d:
                                    if i[0]==A:
                                        h=["ACCOUNT","NAME","AGE","ACC. TYPE","AMOUNT","LOAN NAME"]
                                        print(tabulate(i,h,tablefmt="grid"))
                                input()
                                a.commit()
                                
                            def employe():
                                b.execute('Admin_id,Name,Age,Mobile_number,Work_experience  from employee')
                                dat=b.fetchall()
                                z=[i for i in dat ]
                                h=["ADMIN ID","NAME","AGE","MOBILE_NUMBER","WORK_EXPERIENCE"]
                                print(tabulate(z,h,tablefmt="grid"))
                                a.commit()
                                input()
                            def modify():
                                print ('1.PASSWORD\n2.NAME\n3.AGE\n4.MOBILE NUMBER ')
                                Ch=int(input('ENTER YOUR CHOICE: '))
                                if Ch==1:
                                    b.execute('select * from employee')
                                    Data=b.fetchall()
                                    e=stdiomask.getpass('ENTER YOUR OLD PASSWORD: ')
                                    d=int(input('ÉNTER YOUR ADMIN ID: '))
                                    for i in Data:
                                        if i[0]==d:
                                            f=stdiomask.getpass('ENTER YOUR NEW PASSWORD: ')
                                            g=input('DO YOU WANT TO CHANGE PASSWORD [y/n]: ')
                                            if g.lower()=='y':
                                                b.execute('''update employee set Password='{}' where Admin_id={} '''.format(f,d))
                                                print('SUCESSFULLY MODIFIED')
                                            elif g.lower()=='n':
                                                print('PROCESS CANCELLED')
                                    input()
                                elif Ch==2:
                                    b.execute('select * from employee')
                                    Data=b.fetchall()
                                    d=int(input('ÉNTER YOUR ADMIN ID: '))
                                    A=input('ENTER YOUR OLD NAME: ')
                                    for i in Data:
                                        if i[0]==d:
                                            B=input('ENTER YOUR NEW NAME: ')
                                            g=input('DO YOU WANT TO CHANGE NAME [y/n]: ')
                                            if g.lower()=='y':
                                                b.execute('''update employee set Name='{}' where Admin_id={}'''.format(B,d))
                                                print('SUCESSFULLY MODIFIED')
                                            elif g.lower()=='n':
                                                print('PROCESS CANCELLED')
                                    input()
                                elif Ch==3:
                                    b.execute('select * from employee')
                                    Data=b.fetchall()
                                    d=int(input('ENTER YOUR ADMIN ID: '))
                                    A=int(input('ENTER YOUR OLD AGE: '))
                                    for i in Data:
                                        if i[0]==d:
                                            B=int(input('ENTER YOUR NEW AGE : '))
                                            g=input('DO YOU WANT TO CHANGE AGE [y/n]: ')
                                            if g.lower()=='y':
                                                b.execute('''update employee set Age={} where Admin_id={}'''.format(B,d))
                                                print('SUCESSFULLY MODIFIED')
                                            elif g.lower()=='n':
                                                print('PROCESSS CANCELLED')
                                    input()
                                elif Ch==4:
                                    b.execute('select * from employee')
                                    Data=b.fetchall()
                                    d=int(input('ÉNTER YOUR ADMIN ID: '))
                                    A=input('ENTER YOUR OLD MOBILE NUMBER: ')
                                    for i in Data:
                                        if i[0]==d:
                                            B=input('ENTER YOUR NEW MOBILE NUMBER: ')
                                            g=input('DO YOU WANT TO CHANGE MOBILE NUMBER [y/n]: ')
                                            if g.lower()=='y':
                                                b.execute('''update employee set Mobile_number='{}' where Admin_id={} '''.format(B,d))
                                                print('SUCESSFULLY MODIFIED')
                                            elif g.lower()=='n':
                                                print('PROCESS CANCELLED')
                                    input()
                                a.commit()
                                
                            def profile():
                                b.execute('select Admin_id,Name,Age,Mobile_experience from employee')
                                data=b.fetchall()
                                h=['ADMIN ID','NAME','AGE','MOBILE NUMBER','WORK EXPERIENCE']
                                v=[i for i in data]
                                print(tabulate(v,h,tablefmt = "grid"))    
                                input()
                                a.commit()
                            def sanction():
                                b.execute('select * from bank_creating')
                                d=b.fetchall()
                                D='NULL'
                                A=int(input('ENTER ACCOUNT NUMBER: '))
                                for i in d:
                                    if i[0]==A:
                                        b.execute('''update bank_creating set loan_name='{}' where Account={}'''.format(D,A))
                                        print('SUCESSFULLY FINSISHED CUSTOMER LOAN')
                                input()
                                a.commit()
                                
                            while(1):
                                clear()
                                print('1.DETAILS OF ALL EMPLOYEE\n2.DETAILS OF CUSTOMER\n3.FINISHING LOAN OF CUSTOMER\n4.MODIFY YOUR PERSONAL DETAILS\n5.PROFILE\n6.EXIT')
                                CH=int(input('ENTER YOUR CHOICE: '))
                                if CH==1:
                                    employe()
                                elif CH==2:
                                    customers()
                                elif CH==3:
                                    sanction()
                                elif CH==4:
                                    modify()
                                elif CH==5:
                                    profile()
                                elif CH==6:
                                    break
            
            else:
                break
    elif cho==3:
        break
        input()
