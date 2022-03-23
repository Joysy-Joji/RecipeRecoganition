import pandas as pd
# res=pd.read_csv('C:\\Users\\user\\PycharmProjects\\reciperecognation\\static\\recipe dataset.csv', index_col=0)
# print(res)


df = pd.read_csv("C:\\Users\\user\\PycharmProjects\\reciperecognation\\static\\recipe dataset.csv", usecols = ['TranslatedIngredients'])
data=df.TranslatedIngredients
# print(data)
inclist=[]
for i in data:
    # print(i.split(","))
    try:
        d1=i.split(",")
        for inc in d1:
            result = ''.join([i for i in inc if not i.isdigit()])
            inclist.append(result)
    except:
        pass
print(inclist)