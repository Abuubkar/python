"""
a => Append                :: if file is not present will create file
w => Write                 :: if file is not present will create file
r => Read                  :: if file is not present will give error
x => w + r and create file :: if file is present will give error
b => binary mode
"""

# ========================= Writing to file
filename = "text_files\programming.txt"
try:
    with open(filename, "w") as f:                    # Closes file on its own
        f.write("Now the file has more content!")
        x =10
except FileNotFoundError as err:
    print('File:- '+ filename + "Not Found")
   
# ========================= Writing multiple lines
with open("text_files\programming.txt", 'a') as f:
    web_browsers = ['Firefox\n', 'Chrome\n', 'Edge\n']
    f.writelines(web_browsers)
 
# open and read the file after the appending:
f = open(filename, "r")                           # Need Closes file on our own
print(f.read())
f.close()
