import mysql.connector as sql
import datetime


E = "employee"
e = "employee_entry"
V = "vehicle"
v = "vehicle_entry"
Vi = "visitor"
vi = "visitor_entry"
R = "residential"
r = "residential_entry"
pwd = "MasterSQL"


def valErrHandle(n):
    while True:
        try:
            i = int(input(n))
            break
        except ValueError:
            print("\nONLY 'INTEGRAL' VALUES ARE ACCEPTABLE IN THIS FIELD!")

    return i


def nullCon(n):
    while True:
        i = input(n)
        if i:
            break
        else:
            print("\nKINDLY ENTER SOME VALUE...THE FIELD CANNOT BE EMPTY!")

    return i


def readCon(a, b):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=a)
    cur = data.cursor()
    cur.execute(f"SELECT * FROM {b}")
    dat = cur.fetchall()
    data.close()

    if not dat:
        print("\nNO RECORDS FOUND AT THE MOMENT!")
        return False
    else:
        print()
        for i in dat:
            print(i)
        return True


def inpCheck(a, b, c):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=a)
    cur = data.cursor()
    cur.execute(f"SELECT * FROM {b}")
    dat = cur.fetchall()
    data.close()

    while True:
        n = valErrHandle("-> ")

        flag = False
        for i in dat:
            for j in i:
                if j == n:
                    flag = True

        if flag:
            break
        else:
            print(f"\nNO RECORD WAS FOUND WITH THE ENTERED {c}! PLEASE TRY AGAIN...")

    return n


def databasesCr():
    mycon = sql.connect(host='localhost', user='root', passwd=pwd)
    mycursor = mycon.cursor()
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {E}")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {V}")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {Vi}")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {R}")
    mycon.commit()
    mycon.close()


def empCr():
    mycon = sql.connect(host='localhost', user='root', passwd=pwd, database=E)
    cur = mycon.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {e}(NAME VARCHAR(30) NOT NULL, EMP_CODE INT PRIMARY KEY,"
                "DATE_TIME DATETIME NOT NULL, DEPARTMENT VARCHAR(30))")
    mycon.commit()
    mycon.close()


def vehCr():
    mycon = sql.connect(host='localhost', user='root', passwd=pwd, database=V)
    cur = mycon.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {v}(VEHICLE_NUMBER INT PRIMARY KEY, DRIVER_NAME VARCHAR(30) "
                "NOT NULL, DATE_TIME DATETIME NOT NULL, MATERIAL VARCHAR(30))")
    mycon.commit()
    mycon.close()


def visCr():
    mycon = sql.connect(host='localhost', user='root', passwd=pwd, database=Vi)
    cur = mycon.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {vi}(NAME VARCHAR(30) NOT NULL, DATE_TIME DATETIME NOT NULL,"
                "MOBILE_NUMBER BIGINT PRIMARY KEY, REASON VARCHAR(90))")
    mycon.commit()
    mycon.close()


def resCr():
    mycon = sql.connect(host='localhost', user='root', passwd=pwd, database=R)
    cur = mycon.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {r}(NAME VARCHAR(30) NOT NULL, DATE_TIME DATETIME NOT NULL, "
                "HOUSE_NUMBER INT PRIMARY KEY)")
    mycon.commit()
    mycon.close()


def date_time():
    return datetime.datetime.now()


def empIns(N, C, DT, D):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=E)
    cur = data.cursor()
    q = f"INSERT INTO {e}(NAME, EMP_CODE, DATE_TIME, DEPARTMENT) VALUES(%s, %s, %s, %s)"
    val = (N, C, DT, D)
    cur.execute(q, val)
    data.commit()
    data.close()


def vehIns(VN, DN, DT, M):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=V)
    cur = data.cursor()
    q = f"INSERT INTO {v}(VEHICLE_NUMBER, DRIVER_NAME, DATE_TIME, MATERIAL) VALUES(%s, %s, %s, %s)"
    val = (VN, DN, DT, M)
    cur.execute(q, val)
    data.commit()
    data.close()


def visIns(N, DT, MN, R):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=Vi)
    cur = data.cursor()
    q = f"INSERT INTO {vi}(NAME, DATE_TIME, MOBILE_NUMBER, REASON) VALUES(%s, %s, %s, %s)"
    val = (N, DT, MN, R)
    cur.execute(q, val)
    data.commit()
    data.close()


def resIns(N, DT, H):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=R)
    cur = data.cursor()
    q = f"INSERT INTO {r}(NAME, DATE_TIME, HOUSE_NUMBER) VALUES(%s, %s, %s)"
    val = (N, DT, H)
    cur.execute(q, val)
    data.commit()
    data.close()


def empUp(emp_Sr):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=E)
    cur = data.cursor()
    print("\nWHAT DO YOU WANT TO CHANGE?\n PRESS 1 FOR NAME\n PRESS 2 FOR EMPLOYEE CODE\n PRESS 3 FOR DEPARTMENT\n "
          "PRESS 4 FOR CHANGING A WHOLE INDIVIDUAL RECORD")

    i = valErrHandle("-> ")
    if i == 1:
        n = nullCon("\nEnter Name: ")
        cur.execute(f"UPDATE {e} SET NAME='{n}' WHERE EMP_CODE={emp_Sr}")
        data.commit()
        print(f"\nNAME CHANGED TO '{n}'")
    elif i == 2:
        n1 = valErrHandle("\nEnter Employee Code: ")
        cur.execute(f"UPDATE {e} SET EMP_CODE={n1} WHERE EMP_CODE={emp_Sr}")
        data.commit()
        print(f"\nEMPLOYEE CODE CHANGED TO '{n1}'")
    elif i == 3:
        n2 = nullCon("\nEnter Department: ")
        cur.execute(f"UPDATE {e} SET DEPARTMENT='{n2}' WHERE EMP_CODE={emp_Sr}")
        data.commit()
        print(f"\nDEPARTMENT CHANGED TO '{n2}'")
    elif i == 4:
        n3 = nullCon("\nEnter Name: ")
        n4 = valErrHandle("Enter Employee Code: ")
        n5 = nullCon("Enter Department: ")
        cur.execute(f"UPDATE {e} SET NAME='{n3}', EMP_CODE={n4}, DEPARTMENT='{n5}' WHERE EMP_CODE={emp_Sr}")
        data.commit()
        print(f"\nNAME CHANGED TO '{n3}'\nEMPLOYEE CODE CHANGED TO '{n4}'\nDEPARTMENT CHANGED TO '{n5}'")
    else:
        data.close()
        print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
        empUp(emp_Sr)

    data.close()
    interface_1()


def vehUp(veh_Sr):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=V)
    cur = data.cursor()
    print("\nWHAT DO YOU WANT TO CHANGE?\n PRESS 1 FOR VEHICLE NUMBER"
          "\n PRESS 2 FOR DRIVER NAME\n PRESS 3 FOR MATERIAL\n PRESS 4 FOR CHANGING A WHOLE INDIVIDUAL RECORD")

    i = valErrHandle("-> ")
    if i == 1:
        n = valErrHandle("\nEnter Vehicle Number: ")
        cur.execute(f"UPDATE {v} SET VECHICLE_NUMBER={n} WHERE VECHICLE_NUMBER={veh_Sr}")
        data.commit()
        print(f"\nVEHICLE NUMBER CHANGED TO '{n}'")
    elif i == 2:
        n1 = nullCon("\nEnter Driver Name: ")
        cur.execute(f"UPDATE {v} SET DRIVER_NAME='{n1}' WHERE VECHICLE_NUMBER={veh_Sr}")
        data.commit()
        print(f"\nDRIVER NAME CHANGED TO '{n1}'")
    elif i == 3:
        n2 = nullCon("\nEnter Material: ")
        cur.execute(f"UPDATE {V} SET MATERIAL='{n2}' WHERE VECHICLE_NUMBER={veh_Sr}")
        data.commit()
        print(f"\nMATERIAL CHANGED TO '{n2}'")
    elif i == 4:
        n3 = valErrHandle("\nEnter Vehicle Number: ")
        n4 = nullCon("Enter Driver Name: ")
        n5 = nullCon("Enter Material: ")
        cur.execute(f"UPDATE {v} SET VECHICLE_NUMBER={n3}, DRIVER_NAME='{n4}', MATERIAL='{n5}'"
                    "WHERE VECHICLE_NUMBER={veh_Sr}")
        data.commit()
        print(f"\nVEHICLE NUMBER CHANGED TO '{n3}'\nDRIVER NAME CHANGED TO '{n4}'\nMATERIAL CHANGED TO '{n5}'")
    else:
        data.close()
        print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
        vehUp(veh_Sr)

    data.close()
    interface_1()


def visUp(vis_Sr):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=Vi)
    cur = data.cursor()
    print("\nWHAT DO YOU WANT TO CHANGE?\n PRESS 1 FOR NAME\n PRESS 2 FOR MOBILE_NUMBER\n PRESS 3 FOR REASON\n "
          "PRESS 4 FOR CHANGING A WHOLE INDIVIDUAL RECORD")

    i = valErrHandle("-> ")
    if i == 1:
        n = nullCon("\nEnter Name: ")
        cur.execute(f"UPDATE {vi} SET NAME='{n}' WHERE MOBILE_NUMBER={vis_Sr}")
        data.commit()
        print(f"\nNAME CHANGED TO '{n}'")
    elif i == 2:
        n1 = valErrHandle("\nEnter Mobile Number: ")
        cur.execute(f"UPDATE {vi} SET MOBILE_NUMBER={n1} WHERE MOBILE_NUMBER={vis_Sr}")
        data.commit()
        print(f"\nMOBILE NUMBER CHANGED TO '{n1}'")
    elif i == 3:
        n2 = nullCon("\nEnter Reason: ")
        cur.execute(f"UPDATE {vi} SET REASON='{n2}' WHERE MOBILE_NUMBER={vis_Sr}")
        data.commit()
        print(f"\nREASON CHANGED TO'{n2}'")
    elif i == 4:
        n3 = nullCon("\nEnter Name: ")
        n4 = valErrHandle("Enter Mobile Number: ")
        n5 = nullCon("Enter Reason: ")
        cur.execute(f"UPDATE {vi} SET NAME='{n3}', MOBILE_NUMBER={n4}, REASON='{n5}' WHERE MOBILE_NUMBER={vis_Sr}")
        data.commit()
        print(f"\nNAME CHANGED TO '{n3}'\nMOBILE NUMBER CHANGED TO '{n4}'\nREASON CHANGED TO '{n5}'")
    else:
        data.close()
        print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
        visUp(vis_Sr)

    data.close()
    interface_1()


def resUp(res_Sr):
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=R)
    cur = data.cursor()
    print("\nWHAT DO YOU WANT TO CHANGE?\n PRESS 1 FOR NAME"
          "\n PRESS 2 FOR HOUSE NUMBER\n PRESS 3 FOR CHANGING A WHOLE INDIVIDUAL RECORD")

    i = valErrHandle("-> ")
    if i == 1:
        n = nullCon("\nEnter Name: ")
        cur.execute(f"UPDATE {r} SET NAME='{n}' WHERE HOUSE_NUMBER={res_Sr}")
        data.commit()
        print(f"\nNAME CHANGED TO '{n}'")
    elif i == 2:
        n1 = valErrHandle("\nEnter House Number: ")
        cur.execute(f"UPDATE {r} SET HOUSE_NUMBER='{n1}' WHERE HOUSE_NUMBER={res_Sr}")
        data.commit()
        print(f"\nHOUSE NUMBER CHANGED TO '{n1}'")
    elif i == 3:
        n2 = nullCon("\nEnter Name: ")
        n3 = valErrHandle("\nEnter House Number: ")
        cur.execute(f"UPDATE {r} SET NAME='{n2}', HOUSE_NUMBER='{n3}' WHERE HOUSE_NUMBER={res_Sr}")
        data.commit()
        print(f"\nNAME CHANGED TO '{n2}'\nHOUSE NUMBER CHANGED TO '{n3}'")
    else:
        data.close()
        print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
        resUp(res_Sr)

    data.close()
    interface_1()


def empRead():
    flag = readCon(E, e)

    while flag:
        print("\nIF YOU WANT TO UPDATE ANY RECORD, PRESS 'Y' ELSE PRESS 'N'")
        rr = input("-> ")
        if rr.lower() == 'y':
            print("\nENTER THE EMPLOYEE CODE OF THE EMPLOYEE WHOSE RECORD IS TO BE UPDATED")
            i = inpCheck(E, e, "EMPLOYEE CODE")
            empUp(i)
            break
        elif rr.lower() == 'n':
            interface_1()
            break
        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
    else:
        interface_1()


def vehRead():
    flag = readCon(V, v)

    while flag:
        print("\nIF YOU WANT TO UPDATE ANY RECORD, PRESS 'Y' ELSE PRESS 'N'")
        rr = input("-> ")
        if rr.lower() == 'y':
            print("\nENTER THE VEHICLE NUMBER OF THE VEHICLE WHOSE RECORD IS TO BE UPDATED")
            i = inpCheck(V, v, "VEHICLE NUMBER")
            vehUp(i)
            break
        elif rr.lower() == 'n':
            interface_1()
            break
        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
    else:
        interface_1()


def visRead():
    flag = readCon(Vi, vi)

    while flag:
        print("\nIF YOU WANT TO UPDATE ANY RECORD, PRESS 'Y' ELSE PRESS 'N'")
        rr = input("-> ")
        if rr.lower() == 'y':
            print("\nENTER THE MOBILE NUMBER OF THE VISITOR WHOSE RECORD IS TO BE UPDATED")
            i = inpCheck(Vi, vi, "MOBILE NUMBER")
            visUp(i)
            break
        elif rr.lower() == 'n':
            interface_1()
            break
        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
    else:
        interface_1()


def resRead():
    flag = readCon(R, r)

    while flag:
        print("\nIF YOU WANT TO UPDATE ANY RECORD, PRESS 'Y' ELSE PRESS 'N'")
        rr = input("-> ")
        if rr.lower() == 'y':
            print("\nENTER THE HOUSE NUMBER OF THE RESIDENT WHOSE RECORD IS TO BE UPDATED")
            i = inpCheck(R, r, "HOUSE NUMBER")
            resUp(i)
            break
        elif rr.lower() == 'n':
            interface_1()
            break
        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
    else:
        interface_1()


def empDel():
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=E)
    cur = data.cursor()
    print("\nKINDLY ENTER THE EMPLOYEE CODE CORRESPONDING TO THE EMPLOYEE'S RECORD TO BE DELETED")
    i = inpCheck(E, e, "EMPLOYEE CODE")
    cur.execute(f"DELETE FROM {e} WHERE EMP_CODE = {i}")
    data.commit()
    data.close()
    print(f"\nTHE RECORD CORRESPONDING TO THE EMPLOYEE CODE '{i}' HAS BEEN SUCCESSFULLY DELETED FROM THE EMPLOYEE TABLE")


def vehDel():
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=V)
    cur = data.cursor()
    print("\nKINDLY ENTER THE VEHICLE NUMBER CORRESPONDING TO THE VEHICLE'S RECORD TO BE DELETED")
    i = inpCheck(V, v, "VEHICLE NUMBER")
    cur.execute(f"DELETE FROM {v} WHERE VEHICLE_NUMBER = {i}")
    data.commit()
    data.close()
    print(f"\nTHE RECORD CORRESPONDING TO THE VEHICLE NUMBER '{i}' HAS BEEN SUCCESSFULLY DELETED FROM THE VEHICLE TABLE")


def visDel():
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=Vi)
    cur = data.cursor()
    print("\nKINDLY ENTER THE MOBILE NUMBER CORRESPONDING TO THE VISITOR'S RECORD TO BE DELETED")
    i = inpCheck(Vi, vi, "MOBILE NUMBER")
    cur.execute(f"DELETE FROM {vi} WHERE MOBILE_NUMBER = {i}")
    data.commit()
    data.close()
    print(f"\nTHE RECORD CORRESPONDING TO THE MOBILE NUMBER '{i}' HAS BEEN SUCCESSFULLY DELETED FROM THE VISITOR TABLE")


def resDel():
    data = sql.connect(host='localhost', user='root', passwd=pwd, database=R)
    cur = data.cursor()
    print("\nKINDLY ENTER THE HOUSE NUMBER CORRESPONDING TO THE RESIDENT'S RECORD TO BE DELETED")
    i = inpCheck(R, r, "HOUSE NUMBER")
    cur.execute(f"DELETE FROM {r} WHERE HOUSE_NUMBER = {i}")
    data.commit()
    data.close()
    print(f"\nTHE RECORD CORRESPONDING TO THE HOUSE NUMBER '{i}' HAS BEEN SUCCESSFULLY DELETED FROM THE RESIDENT TABLE")


def empClear():
    print("\nARE YOU SURE YOU WANT TO CLEAR THE EMPLOYEE TABLE?")
    while True:
        q = input("'Y' OR 'N'\n-> ")
        if q.lower() == 'y':
            data = sql.connect(host='localhost', user='root', passwd=pwd, database=E)
            cur = data.cursor()
            cur.execute(f"TRUNCATE TABLE {e}")
            data.commit()
            data.close()
            print("\nALL THE EMPLOYEES' RECORDS HAVE BEEN OBLITERATED FROM THE EMPLOYEE TABLE")
            break
        elif q.lower() == 'n':
            break
        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")


def vehClear():
    print("\nARE YOU SURE YOU WANT TO CLEAR THE VEHICLE TABLE?")
    while True:
        q = input("'Y' OR 'N'\n-> ")
        if q.lower() == 'y':
            data = sql.connect(host='localhost', user='root', passwd=pwd, database=V)
            cur = data.cursor()
            cur.execute(f"TRUNCATE TABLE {v}")
            data.commit()
            data.close()
            print("\nALL THE VEHICLES' RECORDS HAVE BEEN OBLITERATED FROM THE VEHICLE TABLE")
            break
        elif q.lower() == 'n':
            break
        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")


def visClear():
    print(f"\nARE YOU SURE YOU WANT TO CLEAR THE VISITOR TABLE?")
    while True:
        q = input("'Y' OR 'N'\n-> ")
        if q.lower() == 'y':
            data = sql.connect(host='localhost', user='root', passwd=pwd, database=Vi)
            cur = data.cursor()
            cur.execute(f"TRUNCATE TABLE {vi}")
            data.commit()
            data.close()
            print("\nALL THE VISITORS' RECORDS HAVE BEEN OBLITERATED FROM THE VISITOR TABLE")
            break
        elif q.lower() == 'n':
            break
        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")


def resClear():
    print(f"\nARE YOU SURE YOU WANT TO CLEAR THE RESIDENT TABLE?")
    while True:
        q = input("'Y' OR 'N'\n-> ")
        if q.lower() == 'y':
            data = sql.connect(host='localhost', user='root', passwd=pwd, database=R)
            cur = data.cursor()
            cur.execute(f"TRUNCATE TABLE {r}")
            data.commit()
            data.close()
            print("\nALL THE RESIDENTS' RECORDS HAVE BEEN OBLITERATED FROM THE RESIDENT TABLE")
            break
        elif q.lower() == 'n':
            break
        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")


def exitCode():
    print("\nWELL THEN...\nGOODBYE!\n")
    exit()


def interface_1():
    print("\n|============================ INDUSTRIAL GATE MANAGEMENT SYSTEM ============================|")
    print(" PRESS 1 TO ENTER RECORDS IN THE SYSTEM")
    print(" PRESS 2 TO READ AND UPDATE RECORDS FROM THE SYSTEM")
    print(" PRESS 3 TO DELETE RECORDS FROM THE SYSTEM")
    print(" PRESS 4 TO EXIT")
    i = input("-> ")

    interface_2(i)


def interface_2(i):
    # CODE TO ENTER DATA INTO THE DATABASE
    if i == '1':
        print("\n PRESS 1 FOR EMPLOYEE ENTRY")
        print(" PRESS 2 FOR VEHICLE ENTRY")
        print(" PRESS 3 FOR RESIDENTIAL ENTRY")
        print(" PRESS 4 FOR VISITOR ENTRY")
        print(" PRESS 5 TO GO BACK TO MAIN MENU")
        print(" PRESS 6 TO EXIT")

        i1 = input("-> ")
        if i1 == '1':
            flag = True
            while flag:
                n = nullCon("Enter Name of the Employee: ")
                c = valErrHandle("Enter the Employee Code: ")
                dt = date_time()
                d = nullCon("Enter Department of the Employee: ")
                empIns(n, c, dt, d)
                print(f"\nRECORD SUCCESSFULLY ENTERED OF EMPLOYEE:-\nNAME: {n}      EMPLOYEE CODE: {c}")
                print("\nIF YOU WISH TO ENTER ANOTHER EMPLOYEE RECORD, THEN PRESS 'Y', ELSE PRESS 'N'")
                while True:
                    q = input("-> ")
                    if q.lower() == 'y':
                        break
                    elif q.lower() == 'n':
                        flag = False
                        break
                    else:
                        print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")

            interface_1()

        elif i1 == '2':
            flag = True
            while flag:
                vn = valErrHandle("Enter Vehicle Number: ")
                dn = nullCon("Enter Driver's Name: ")
                dt = date_time()
                ma = nullCon("Enter Material Name: ")
                vehIns(vn, dn, dt, ma)
                print(f"\nRECORD SUCCESSFULLY ENTERED OF VEHICLE:-\nDRIVER'S NAME: {dn}      VEHICLE NUMBER: {vn}")
                print("\nIF YOU WISH TO ENTER ANOTHER VEHICLE RECORD, THEN PRESS 'Y', ELSE PRESS 'N'")
                while True:
                    q = input("-> ")
                    if q.lower() == 'y':
                        break
                    elif q.lower() == 'n':
                        flag = False
                        break
                    else:
                        print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")

            interface_1()

        elif i1 == '3':
            flag = True
            while flag:
                rn = nullCon("Enter Name of the Resident: ")
                dt = date_time()
                hn = valErrHandle("Enter House Number: ")
                resIns(rn, dt, hn)
                print(f"\nRECORD SUCCESSFULLY ENTERED OF RESIDENT:-\nNAME: {rn}      HOUSE NUMBER: {hn}")
                print("\nIF YOU WISH TO ENTER ANOTHER RESIDENTIAL RECORD, THEN PRESS 'Y', ELSE PRESS 'N'")
                while True:
                    q = input("-> ")
                    if q.lower() == 'y':
                        break
                    elif q.lower() == 'n':
                        flag = False
                        break
                    else:
                        print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")

            interface_1()

        elif i1 == '4':
            flag = True
            while flag:
                vn = nullCon("Enter Name of the visitor: ")
                dt = date_time()
                vm = valErrHandle("Enter Mobile Number of the visitor: ")
                vr = nullCon("Enter Reason of visiting the area: ")
                visIns(vn, dt, vm, vr)
                print(f"\nRECORD SUCCESSFULLY ENTERED OF VISITOR:-\nNAME: {vn}      REASON: {vr}")
                print("\nIF YOU WISH TO ENTER ANOTHER VISITOR RECORD, THEN PRESS 'Y', ELSE PRESS 'N'")
                while True:
                    q = input("-> ")
                    if q.lower() == 'y':
                        break
                    elif q.lower() == 'n':
                        flag = False
                        break
                    else:
                        print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")

            interface_1()

        elif i1 == '5':
            interface_1()

        elif i1 == '6':
            exitCode()

        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
            interface_2(i)

    # CODE TO READ THE ENTERED DATA
    elif i == '2':
        print("\n PRESS 1 TO RETRIEVE EMPLOYEES' DATA")
        print(" PRESS 2 TO RETRIEVE VEHICLES' DATA")
        print(" PRESS 3 TO RETRIEVE RESIDENTIAL DATA")
        print(" PRESS 4 TO RETRIEVE VISITORS' DATA")
        print(" PRESS 5 TO GO TO MAIN MENU")
        print(" PRESS 6 TO EXIT")

        i1 = input("-> ")
        if i1 == '1':
            empRead()

        elif i1 == '2':
            vehRead()

        elif i1 == '3':
            resRead()

        elif i1 == '4':
            visRead()

        elif i1 == '5':
            interface_1()

        elif i1 == '6':
            exitCode()

        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
            interface_2(i)

    # CODE TO DELETE RECORDS
    elif i == '3':
        print("\n PRESS 1 FOR DELETING ALL THE CONTENTS OF A TABLE")
        print(" PRESS 2 FOR DELETING A PARTICULAR RECORD")
        print(" PRESS 3 TO GO TO MAIN MENU")
        print(" PRESS 4 TO EXIT")

        i1 = input("-> ")
        if i1 == '1':
            while True:
                print("\nSPECIFY THE TABLE YOU WISH TO CLEAR")
                print(" PRESS 1 FOR EMPLOYEE TABLE")
                print(" PRESS 2 FOR VEHICLE TABLE")
                print(" PRESS 3 FOR RESIDENT TABLE")
                print(" PRESS 4 FOR VISITOR TABLE")
                print(" PRESS 5 TO GO TO MAIN MENU")
                print(" PRESS 6 TO EXIT")

                i2 = input("->")
                if i2 == '1':
                    empClear()
                    break

                elif i2 == '2':
                    vehClear()
                    break

                elif i2 == '3':
                    resClear()
                    break

                elif i2 == '4':
                    visClear()
                    break

                elif i2 == '5':
                    interface_1()
                    break

                elif i2 == '6':
                    exitCode()

                else:
                    print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")

            while True:
                print("\nIF YOU WISH TO DELETE ANYTHING ELSE, THEN PRESS 'Y', ELSE PRESS 'N'")
                q = input("-> ")
                if q.lower() == 'y':
                    interface_2(i)
                    break
                elif q.lower() == 'n':
                    interface_1()
                    break
                else:
                    print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")

        elif i1 == '2':
            while True:
                print("\nSPECIFY THE TABLE YOU WISH TO DELETE A RECORD FROM")
                print(" PRESS 1 FOR EMPLOYEE TABLE")
                print(" PRESS 2 FOR VEHICLE TABLE")
                print(" PRESS 3 FOR RESIDENT TABLE")
                print(" PRESS 4 FOR VISITOR TABLE")
                print(" PRESS 5 TO GO TO MAIN MENU")
                print(" PRESS 6 TO EXIT")

                i2 = input("-> ")
                if i2 == '1':
                    empDel()
                    break

                elif i2 == '2':
                    vehDel()
                    break

                elif i2 == '3':
                    resDel()
                    break

                elif i2 == '4':
                    visDel()
                    break

                elif i2 == '5':
                    interface_1()
                    break

                elif i2 == '6':
                    exitCode()

                else:
                    print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")

            while True:
                print("\nIF YOU WISH TO DELETE ANYTHING ELSE, THEN PRESS 'Y', ELSE PRESS 'N'")
                q = input("-> ")
                if q.lower() == 'y':
                    interface_2(i)
                    break
                elif q.lower() == 'n':
                    interface_1()
                    break
                else:
                    print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")

        elif i1 == '3':
            interface_1()

        elif i1 == '4':
            exitCode()

        else:
            print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
            interface_2(i)

    elif i == '4':
        exitCode()

    else:
        print("\nKINDLY ENTER THE APPROPRIATE CHOICE...")
        interface_1()


# __main__:-
databasesCr()
empCr()
vehCr()
visCr()
resCr()
interface_1()