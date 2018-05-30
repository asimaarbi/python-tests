
#record = int(input("Enter the members to add :"))

memb_data={}


for i in range(2):

    a = input("Member name :")
    if a in memb_data:
        print("Member Already Existed")

    else:
        Name = a
        Age = input("Enter the {} age :".split().format(Name))
        Grade = input("Enter the {} grade :".format(Name))
        Nam_key =  Name[0]
        Age_value = Age[0]
        Grade_value = Grade[0]
        memb_data[a] = {Age_value,Grade_value}

print(memb_data)