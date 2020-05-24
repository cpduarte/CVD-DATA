import pandas as pd

#-------- Import CSV data from GitHub
try:
    cvd_data = pd.read_csv('https://raw.githubusercontent.com/cpduarte/CVD-DATA/master/us_cvd_daily.csv')
except:
    print('Error: Connection failed!')
    exit()
date = pd.to_datetime(cvd_data.date.max(), format='%Y%m%d')
print(f"""
============================================================
US COVID-19 STATISTICS | UPDATED IN  {date}

1: Summary US Results    3: Complete US States Table
2: Search by State       X: Quit / Step Back

============================================================
""")
cvd_data = cvd_data[['state','total','negative','positive','death']]
quit = False
while quit != True:
    option = input('Type Menu Option > ')
    if option == '1':
        tmp = cvd_data[['total','negative','positive','death']].sum()
        print(f"\nTotal US COVID-19 Results\n\n{tmp}\n")
    elif option == '2':
        exit = False
        while exit != True:
            state = input("Type State, eg. 'UT' > ")
            res = cvd_data[cvd_data.state == state.upper()]
            if state.lower() == 'x':
                exit = True
                break
            elif res.empty:
                print("Invalid input! Type an abbreviation like 'TX' or 'X' to back menu.")
            else:
                print(f"\n  {res} \n")
    elif option == '3':
        print(f"\n  {cvd_data} \n")
    elif option.lower() == 'x':
        print('Thank you for your visit, see you...')
        quit = True
    else:
        print(f"'{option}' is not a valid menu option!")
