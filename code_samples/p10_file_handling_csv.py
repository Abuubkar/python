import csv
""""csv = comma seperated files"""
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
sales = ['10', '8', '19', '12', '25']

with open('csv_files/sales.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',') # delimiter must be of 1 character
    csv_writer.writerow(weekdays)
    csv_writer.writerow(sales)