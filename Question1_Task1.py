import os, csv #Operating System and Comma Separated Values (Allow to read csv files)
csv_D=r'C:\Study\WINT01 Bachelor of IT\First Year Sem2\HIT137 Software now\Assignment 2' #Change this to your file location 

#It will create another text file and posted within the folder of your selected folder of the script you have created above
output_file = 'output.txt'

with open(output_file, 'w', encoding='utf-8') as txt_file: 
    for csv_filename in os.listdir(csv_D):
        if csv_filename.endswith('.csv'):
            csv_path=os.path.join(csv_D, csv_filename)
            with open(csv_path, 'r', encoding='utf-8') as csv_file:
                reader=csv.reader(csv_file) 
                for row in reader:
                    txt_file.write(' '.join(row)+'\n')