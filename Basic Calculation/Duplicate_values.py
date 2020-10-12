#Importing libraries
import pandas as pd


def matching_index(source):
    """This function is used to get index of duplicate values of column"""
    df = pd.DataFrame(source,columns=['column_'+str(i)  for i in range(0,len(source[0]))])
    for col in df.columns:
        df[col+'_duplicate'] = df.duplicated(subset=[col],keep=False)
    df.insert(0, 'ID', range(0, 0 + len(df)))
    final=pd.DataFrame(columns=df.columns)
    for col in df.columns: 
        temp = df[df[col]==True]
        if temp.empty:
            pass
        else:
            final = final.append(temp)
    lst = final['ID'].unique().tolist()
    return lst



if '__main__'==__name__:
    source = [
("username1","phone_number1", "email1"), ("usernameX","phone_number1", "emailX"), ("usernameZ","phone_numberZ", "email1Z"), ("usernameY","phone_numberY", "emailX"),
]
    lst = matching_index(source)




