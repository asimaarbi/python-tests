"""
memberdetail = {"Omer" :{"Age" : "25", "Place" : "Cant","occupation" : "Bataien"},
                 "Shahid" :{"Age" : "26", "Place" : "Cant","occupation" : "Bataien"},
                  "Bilal" :{"Age" : "30", "Place" : "Cant","occupation" : "Bataien"},
                }
a = str(input("Member name :"))
if a in memberdetail:
    print("Member Already Existed")
"""

#record = int(input("Enter the members to add :"))

memb_data={}

for i in range(0,1):

    a = input("Member name :")
    if a in memb_data:
        print("Member Already Existed")
    else:
        Name = a
        Age = input("Enter the {} age :".format(Name,))
        Grade = input("Enter the {} grade :".format(Name))
        Nam_key =  Name[0]
        Age_value = Age[0]
        Grade_value = Grade[0]
        memb_data[a] = {Age_value,Grade_value}

print(memb_data)