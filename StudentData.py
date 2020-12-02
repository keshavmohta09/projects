import pandas as pd
while True:
    choice = input("Press 'r' for read the data\nPress 'u' for update the data\nPress 'w' for write new data\nPress 'd' for delete the data\n:-> ")
    if choice=='r':
        df = pd.read_csv('studentdata.csv')
        spcfc = input('Press 1 for print specific data else press any key for print complete data : ')
        if spcfc=='1':
            prspcfc = input('Press 1 for any one column only\nPress 2 for any two columns\nPress 3 for any three columns\nPress 4 for selected student data\nPress any key for print no. of students data\n:-> ')
            if prspcfc=='1':
                clm = input('Enter the column name : ')
                try:
                    print(df[clm])
                except Exception as e:
                    print(e)

            elif prspcfc=='2':
                clm1 = input('Enter the 1st column : ')
                clm2 = input('Enter the 2nd column : ')
                try:
                    print(df[[clm1,clm2]])
                except Exception as e:
                    print(e)

            elif prspcfc=='3':
                clm1 = input('Enter the 1st column name : ')
                clm2 = input('Enter the 2nd column name : ')
                clm3 = input('Enter the 3rd column name : ')
                try:
                    print(df[[clm1,clm2,clm3]])
                except Exception as e:
                    print(e)

            elif prspcfc=='4':
                name = input('Enter the name of student : ')
                try:
                    data = df[df['Name']==name]
                    print(data)
                except Exception as e:
                    print(e)

            else:
                n = input('Enter the number of students : ')
                try:
                    print(df.head(int(n)))
                except Exception as e:
                    print(e)

        else:
            print(df)
        break

    elif choice=='u':
        try:
            df = pd.read_csv('studentdata.csv')
            name = input('Enter the full name of student : ')
            change = input('Press 1 for name/2 for class/3 for phone_no/4 for email : ')
            dict_d = {'1':'Name','2':'Class','3':'Phone_no','4':'Email'}
            row = list(df[df['Name']==name].index)
            clm = [dict_d[change]]
            df.loc[row,clm] = input(f'Type {dict_d[change]}: ')
            df.to_csv('studentdata.csv',index=False)
        except Exception as e:
            print(e)
        print('Data updated successfully')
        break

    elif choice=='w':
        inp = input('Enter the no. of students: ')
        lines = []
        try:
            df = pd.read_csv('studentdata.csv')
            for i in range(int(inp)):
                name = input('Enter the name of student : ')
                clas = input('Enter the class with year and branch : ')
                phone = input('Enter the contact number : ')
                email = input('Enter email : ')
                df.loc[len(df)] = [name,clas,phone,email]
            df.to_csv('studentdata.csv',index=False)
            print('\nData updated successfully\n')
        except Exception as e:
            print(e)
        break

    elif choice=='d':
        try:
            name = input('Enter the name of student : ')
            df = pd.read_csv('studentdata.csv')
            indx = list(df[df['Name']==name].index)
            df.drop(indx[0],axis=0,inplace=True)
            df.to_csv('studentdata.csv',index=False)
            print('Data deleted successfully')
        except Exception as e:
            print('Data not found')
        break

    else:
        ask = input("Press 'e' for exit else press any key : ")
        if ask=='e':
            exit()