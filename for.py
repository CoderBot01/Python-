words = ['praveen' , 'kabilan', 'Thambi' , 'sachin' , 'indra']
for i in words:
    print(i,len(i))

    #for loop helps to take and process each and every element in the series
users = {
    'saran':'active',
    'karthi':'inactive',
    'sasi':'active',
    'alagar':'inactive'
}
for user,rt in users.copy().items():
    if rt == 'active':
        print(user + ' velapolappu illathavanuga')
    elif rt == 'inactive': 
        print(user + ' pulithis')
         
