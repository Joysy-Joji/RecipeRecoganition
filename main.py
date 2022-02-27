from flask import Flask,render_template,request
from DBConnection import Db
app=Flask(__name__)
staticpath="C:\\Users\\user\\PycharmProjects\\reciperecognation\\static\\"

@app.route('/admin_index')
def admin_index():
    return render_template('admin/admin_index.html')

@app.route('/store_index')
def store_index():
    return render_template('store/store_index.html')

@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/login_post',methods=['post'])
def login_post():
    name=request.form['textfield']
    password=request.form['textfield2']
    db=Db()
    qry="select * from login where username='"+name+"' and password='"+password+"'"
    res=db.selectOne(qry)
    if res!=None:
        if res['type']=='admin':
            return adminhome()
        elif res['type']=='store':
            return storehome()
        else:
            return '''<script> alert('User not allowed'); window.location='/' </script>'''
    else:
        return '''<script> alert('Invalid username or password'); window.location='/' </script>'''
        
            
    



@app.route('/adminhome')
def adminhome():
    return render_template('admin/adminhome.html')


@app.route('/storehome')
def storehome():
    return render_template('store/store_index.html')



@app.route('/deleteVegetables/<id>')
def deleteVegetables(id):
    db=Db()
    qry="delete from vegetable where veg_id='"+str(id)+"'"
    res=db.delete(qry)
    return 'ok'

@app.route('/SearchVegetables',methods=['post'])
def SearchVegetables():
    n=request.form['textfield']
    db = Db()
    qry = "select * from vegetable where name like '%"+n+"%' "
    res = db.select(qry)
    return render_template('admin/ViewVegetables.html', data=res)





@app.route('/AddVegetables')
def AddVegetables():
   return render_template('admin/AddVegetables.html')


@app.route('/AddVegetables_post',methods=['post'])
def AddVegetables_post():
    name = request.form['textfield']
    color = request.form['textfield2']
    shape = request.form['textfield3']
    size = request.form['textfield4']
    texture = request.form['textfield5']
    image = request.files['file']
    import datetime
    dt=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    image.save(staticpath+"veg\\"+dt+".jpg")
    path="/static/veg"+dt+".jpg"
    db=Db()
    qry="insert into vegetable(name,color,shape,size,texture,image)values('"+name+"','"+color+"','"+shape+"','"+size+"','"+texture+"','"+path+"')"
    res=db.insert(qry)
    return 'ok'

@app.route('/EditVegetables/<id>')
def EditVegetables(id):
    db=Db()
    qry="select * from vegetable where veg_id='"+str(id)+"'"
    res=db.selectOne(qry)
    return render_template('admin/EditVegetables.html',data=res)
@app.route('/EditVegetables_post',methods=['post'])
def EditVegetables_post():
    id = request.form['id']
    veg_name = request.form['textfield']
    veg_color = request.form['textfield2']
    veg_shape = request.form['textfield3']
    veg_size = request.form['textfield4']
    veg_texture = request.form['textfield5']
    image = request.files['file']
    import datetime
    dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    image.save(staticpath + "veg\\" + dt + ".jpg")
    path = "/static/veg" + dt + ".jpg"
    db = Db()
    qry = "update vegetable set name='" + veg_name + "', color='" + veg_color + "',shape='" + veg_shape + "',size='" + veg_size + "',texture='" + veg_texture + "',image='" + path + "' where veg_id='"+str(id)+"' "
    res = db.update(qry)
    return 'ok'







@app.route('/EditProduct/<id>')
def EditProduct(id):
    db=Db()
    qry="select * from product where product_id='"+str(id)+"'"
    res=db.selectOne(qry)
    return render_template('store/EditProduct.html',data=res)
@app.route('/EditProduct_post',methods=['post'])
def EditProduct_post():
    id = request.form['id']
    product_name = request.form['textfield']
    product_price = request.form['textfield2']
    prodcut_stock = request.form['textfield3']
    product_madedate = request.form['textfield4']

    image = request.files['file']
    import datetime
    dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    image.save(staticpath + "store\\" + dt + ".jpg")
    path = "/static/store" + dt + ".jpg"
    db = Db()
    qry = "update product set name='" + product_name + "', price='" + product_price + "',stock='" + prodcut_stock + "',made_date='" + product_madedate + "',image='" + path + "' where product_id='"+str(id)+"' "
    res = db.update(qry)
    return 'ok'




@app.route('/EditRecipe/<id>')
def EditRecipe(id):
    db=Db()
    qry="select * from recipe where recipe_id='"+str(id)+"'"
    res=db.selectOne(qry)
    return render_template('admin/edit_recipe.html',data=res)
@app.route('/EditRecipe_post',methods=['post'])
def EditRecipe_post():
    id = request.form['id']
    recipe_name = request.form['textfield']
    recipe_description = request.form['textarea']
    recipe_ingredients = request.form['textarea2']

    image = request.files['file']
    import datetime
    dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    image.save(staticpath + "recipe\\" + dt + ".jpg")
    path = "/static/recipe" + dt + ".jpg"
    db = Db()
    qry = "update recipe set name='" + recipe_name + "', description='" + recipe_description + "',ingredients='" + recipe_ingredients + "'where recipe_id='"+str(id)+"' "

    res = db.update(qry)

    return 'ok'




@app.route('/Reply')
def Reply():
    return render_template('admin/Reply.html')
@app.route('/Reply_post',methods=['post'])
def Reply_post():
    reply = request.form['textarea']
    db = Db()
    qry = "insert into complaint(reply)values('" + reply + "')"
    res = db.insert(qry)

    return 'ok'



@app.route('/deleteRecipe/<id>')
def deleteRecipe(id):
    db = Db()
    qry = "delete from recipe where recipe_id='" + str(id) + "'"
    res = db.delete(qry)
    return 'ok'

@app.route('/SearchRecipe',methods=['post'])
def SearchRecipe():
    n=request.form['textfield']
    db = Db()
    qry = "select * from recipe where name like '%"+n+"%'"
    res = db.select(qry)
    return render_template('admin/ViewRecipe.html', data=res)


@app.route('/UploadRecipe')
def UploadRecipe():
    return render_template('admin/UploadRecipe.html')
@app.route('/UploadRecipe_post',methods=['post'])
def UploadRecipe_post():
    name = request.form['textfield']
    description = request.form['textarea']
    ingredients = request.form['textarea']
    image = request.files['file']
    import datetime
    dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    image.save(staticpath + "recipe\\" + dt + ".jpg")
    path = "/static/recipe" + dt + ".jpg"
    db = Db()
    qry = "insert into recipe(name,description,ingredients,image)values('" + name + "','" + description + "','" + ingredients + "','"+ path + "')"
    res = db.insert(qry)
    return 'ok'

@app.route('/SearchComplaints',methods=['post'])
def SearchComplaints():
    n = request.form['textfield']
    m = request.form['textfield2']
    db = Db()
    qry = "select * from complaint where date between '"+n+"' and '"+m+"'"
    res = db.select(qry)
    return render_template('admin/ViewComplaints.html', data=res)

@app.route('/ViewComplaints')
def ViewComplaints():
    db = Db()
    qry = "select * from complaint"
    res = db.select(qry)
    return render_template('admin/ViewComplaints.html',data=res)

@app.route('/ViewComplaints_post',methods=['post'])
def ViewComplaints_post():
    return 'ok'


@app.route('/ViewRecipe')
def ViewRecipe():
    db = Db()
    qry = "select * from recipe"
    res = db.select(qry)
    return render_template('admin/ViewRecipe.html', data=res)


@app.route('/ViewRecipe_post',methods=['post'])
def ViewRecipe_post():
    name = request.form['textfield']
    return 'ok'


@app.route('/SearchStore',methods=['post'])
def SearchStore():
    n=request.form['textfield']
    a = request.form['textfield2']
    db = Db()
    qry = "select * from storeregister where name like '%"+n+"%' and place like '%"+a+"%'"
    res = db.select(qry)
    return render_template('admin/ViewStore.html', data=res)

@app.route('/ViewStore')
def ViewStore():
    db = Db()
    qry = "select * from storeregister order by store_id desc"
    res = db.select(qry)
    print(qry)
    return render_template('admin/ViewStore.html',data=res)
@app.route('/ViewStore_post',methods=['post'])
def ViewStore_post():
    name = request.form['textfield']
    address = request.form['textfield2']
    return 'ok'


@app.route('/ViewVegetables')
def ViewVegetables():
    db=Db()
    qry="select * from vegetable"
    res=db.select(qry)
    print(res)
    return render_template('admin/ViewVegetables.html',data=res)





@app.route('/ViewVegetables_post',methods=['post'])
def ViewVegetables_post():
    name = request.form['textfield']
    return 'ok'



@app.route('/AcceptStore')
def AcceptStore():
    return 'ok'
@app.route('/RejectStore/<id>')
def RejectStore(id):
    db = Db()
    qry = "delete from storeregister where store_id='" + str(id) + "'"
    res = db.delete(qry)
    return 'ok'

@app.route('/Storeregistration')
def Storeregistration():
    return render_template('store/Storeregistration.html')


@app.route('/Storeregistration_post',methods=['post'])
def Storeregistration_post():
    type="store"
    name = request.form['textfield']
    place = request.form['textfield2']
    post = request.form['textfield3']
    pin = request.form['textfield4']
    mobilenumber = request.form['textfield5']
    email = request.form['textfield6']
    password = request.form['textfield7']
    image = request.files['file']
    import datetime
    dt=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    image.save(staticpath+"store\\"+dt+".jpg")
    path="/static/store/"+dt+".jpg"
    db=Db()
    q="insert into login(username,password,type)values('"+name+"','"+password+"','"+type+"')"
    lid = db.insert(q)
    qry="insert into storeregister(name,place,post,pin,mobilenumber,email,password,image,login_id)values('"+name+"','"+place+"','"+post+"','"+pin+"','"+mobilenumber+"','"+email+"','"+password+"','"+path+"','"+str(lid)+"')"
    res=db.insert(qry)

    # return render_template('store/store_index.html')
    return '''<script> alert('Registered Succusfully '); window.location='/storehome'</script>'''

@app.route('/deleteProduct/<id>')
def deleteProduct(id):
    db = Db()
    qry = "delete from product where product_id='" + str(id) + "'"
    res = db.delete(qry)

    return render_template('store/ViewProduct.html')




@app.route('/AddProduct')
def AddProduct():
    return render_template('store/AddProduct.html')
@app.route('/AddProduct_post',methods=['post'])
def AddProduct_post():
    name = request.form['textfield']

    price = request.form['textfield2']
    stock = request.form['textfield3']
    made_date = request.form['textfield4']
    image = request.files['file']
    import datetime
    dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    image.save(staticpath + "store\\" + dt + ".jpg")
    path = "/static/store/"+ dt + ".jpg"
    db = Db()
    qry = "insert into product(name,price,stock,made_date,image)values('" + name + "','" + price + "','" + stock + "','" + made_date + "','" + path + "')"
    res = db.insert(qry)
    return '''<script> alert('Added Succusfully '); window.location='/storehome'</script>'''



@app.route('/SearchProduct',methods=['post'])
def SearchProduct():
    n=request.form['textfield']
    db = Db()
    qry = "select * from product where name like '%"+n+"%'"
    res = db.select(qry)

    return render_template('store/ViewProduct.html', data=res)

@app.route('/ViewProduct')
def ViewProduct():
    db=Db()
    qry="select * from product"
    res=db.select(qry)
   
    return render_template('store/ViewProduct.html',data=res)





@app.route('/ViewProduct_post',methods=['post'])
def ViewProduct_post():
    name = request.form['textfield']
    return 'ok'













if __name__=='__main__':
   app.run(debug=True)