#Importing libraries
from datetime import date, datetime
import os
from calendar import monthrange, day_name

#Creating a Databackup class
class DataBackup():
    def __init__(self, curr_date, f_date):
        self.curr_date = curr_date
        self.f_date = f_date

#method to check if the file is older than 5 days
    def checkFivedays(self, f_name):
        day_diff = self.curr_date - self.f_date
        if day_diff.days >= 5:
            return True
        else:
            return False

#method to check if the file is of last day of the month
    def checklastDay(self, f_name):
        if self.f_date.day == monthrange(self.f_date.year, self.f_date.month)[1]:
            return True
        else:
            return False

#method to check if the file is from last 4 saturdays
    def checkSat(self, f_name):
        if day_name[self.f_date.weekday()] == 'Saturday':
                return True
        else:
            return False

if __name__ == "__main__":
    #Taking current date
    #current_date = datetime.now()
    #Taking fake date for testing purpose
    current_date = datetime.strptime('2020-9-18', '%Y-%m-%d')
    #count of last 4 saturdays
    sat_code_count = 0
    sat_db_count = 0
    bucket_1 = 'bucket1/'
    bucket_2 = 'bucket2/'

    print('Iterating through Bucket 1 directory')
    #iterating through bucket1 dir
    for entry in os.listdir(bucket_1):
        start = entry.rfind('_') + 1
        end = entry.find('.')
        f_date = entry[start:end]

        #datetime of file
        file_date = datetime.strptime(f_date, '%Y-%m-%d')
        a = DataBackup(current_date, file_date)
        if a.checkFivedays(entry):
            if a.checkSat(entry) == False:
                if a.checklastDay(entry) == False:
                    print('Deleting the file: ',entry)
                    os.remove(bucket_1+entry)
            else:
                if sat_code_count > 4:
                    if a.checklastDay(entry) == False:
                        print('Deleting the file: ',entry)
                        os.remove(bucket_1+entry)
                else:
                    sat_code_count += 1

    #iterating through bucket2 dir
    print('Iterating through Bucket 2 directory')
    for entry in os.listdir(bucket_2):
        start = entry.rfind('_') + 1
        end = entry.find('.')
        f_date = entry[start:end]

        #datetime of file
        file_date = datetime.strptime(f_date, '%Y-%m-%d')
        a = DataBackup(current_date, file_date)
        if a.checkFivedays(entry):
            if a.checkSat(entry) == False:
                if a.checklastDay(entry) == False:
                    print('Deleting the file: ',entry)
                    os.remove(bucket_2+entry)
            else:
                if sat_db_count > 4:
                    if a.checklastDay(entry) == False:
                        print('Deleting the file: ',entry)
                        os.remove(bucket_2+entry)
                else:
                    sat_db_count += 1