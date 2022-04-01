import pandas as pd
# res=pd.read_csv('C:\\Users\\user\\PycharmProjects\\reciperecognation\\static\\recipe dataset.csv', index_col=0)
# print(res)


df = pd.read_csv("C:\\Users\\user\\PycharmProjects\\reciperecognation\\static\\recipedataset _ orginal.csv", usecols = ['TranslatedIngredients'])
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
for i in inclist:


    d1 = i.split("-")
    # d2 = i.split("(")

    # print(d1)
    # print(d1[0].replace('/',""))
    d2= d1[0].replace("/","").replace("teaspoon","").replace("tablespoon","").replace("cup","").replace(" ","").replace("Water","").replace("to","").replace("kg","").replace("s","").replace("cup","").replace("gram","").replace("inch","").replace("pinch","").replace("नमक","")


    d3=d2.split("(")
    # print(d3[0])

    v=d3[0]
    print(v)
    # v1= []
    # for x in v:
    #
    #     if x not in v1:
    #         v1.append(x)
    #
    # for x in v1:
    #     print(v1)

    # v=list(d3)
    # print(v)
    # x=[]
    # r=len(d3)
    # print(r)
    # for i in range(len(d3)):
    #     print(i)
    # ny=[]
    # ny.append(d3[0])
    # print("====",ny)
    # # k=len(d3[0])
    # #
    # unique_list = []
    #
    # for x in ny:
    #     if x  in unique_list:
    #         pass
    #     else:
    #         unique_list.append(x)
    #     print("**********************************************************************************************",unique_list)








