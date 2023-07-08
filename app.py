from flask import Flask,request,redirect, url_for,make_response,session,jsonify
from flask import render_template as render
from werkzeug.utils import secure_filename
from functions import isNotEmpty,generateUnid
from database import * 
import json
from flask_redmail import RedMail
from flask_mail import Mail, Message
from datetime import datetime, timedelta 
app = Flask(__name__)
app.secret_key = "rioland123456"
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'Okeseunbaby98@gamil.com'
app.config['MAIL_PASSWORD'] = 'Oluwaseyi22*'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)





# page routes
@app.route("/")
def index():
  user=None
  cartCount=0
  if "USER" in session:
    user=session["USER"]
    nn=user[0]['uid']
    print(nn)
    cartCount=getCartCount(nn)
  product=getProductFromDb()
  return render("index.html",products=product,user=user,cartCount=cartCount)




# *****************************************************
# api routes

@app.route("/save-product", methods=['POST'])
def saveProduct():
  if request.method == 'POST':

    if isNotEmpty(request.form['pname']) and isNotEmpty(request.form['price']) and isNotEmpty(request.form['desc']) and isNotEmpty(request.form['meal_type']):
      
      file = request.files['image']
      filelocation=f"static/product/{secure_filename(file.filename)}"
      file.save(filelocation)
      prod=(request.form['pname'],request.form['price'],
                           request.form['desc'],request.form['meal_type'],filelocation)
      output=addPoductToDB(prod)
      if output==True:
        resp = redirect(url_for("addProduct"))
        session['message']='successfull'
             # resp.set_cookie('message', 'successfull')
        return resp
      else:
         resp = redirect(url_for("addProduct"))
         session['message']='something went wrong'
         return resp

     
    else:
      resp =redirect(url_for( "addProduct" ))
      session['message']='all fields are required'
      return resp
  else:
    
      resp = redirect(url_for("addProduct"))
      session['message']= 'invalid method'
      return resp


@app.route("/register", methods=['POST'])
def register():
  if request.method == 'POST':
    if isNotEmpty(request.form['fname']) and isNotEmpty(request.form['email']) and isNotEmpty(request.form['password']) and isNotEmpty(request.form['phone_number']):
      prod=(request.form['fname'],request.form['phone_number'],request.form['email'],request.form['password'])
      output=createUser(prod)
      if output==True:
         resp = make_response(redirect("/login"))
         resp.set_cookie('message', 'successfull',expires=2)
         return resp
      else:
         resp = make_response(redirect("/signup",expires=2))
         resp.set_cookie('message', output,expires=2)
         return resp
      

    
    else:
       resp = make_response(redirect("/signup"))
       resp.set_cookie('message', 'All fields are required',expires=2)
       return resp
  else:
      resp = make_response(redirect("/signup"))
      resp.set_cookie('message', 'invalid method',expires=2)
      return resp
  

@app.route("/auth", methods=['POST'])
def auth():
  if request.method == 'POST':
    if isNotEmpty(request.form['email']) and isNotEmpty(request.form['password']):
      prod=(request.form['email'],request.form['password'])
      output=loginUser(prod)
      print(output)
      if output!=None:
         resp = redirect(url_for("index"))
         session['USER'] = output
         return resp
      else:
        session['message'] = "invalid login details"
        resp = redirect(url_for("login"))
        return resp
    else:
       resp =redirect(url_for("login"))
       session['message'] = "All fields are required"
       return resp
  else:
      resp = redirect(url_for("login"))
      session['message'] = "Invalid method"
      return resp
  




@app.route("/addtocart/<cartid>",methods=["GET","POST"])
def addToCart(cartid):
  user=None
  if "USER" in session:
    user=session["USER"]
    uid=user[0]['uid']
    pn=addTocart(cartid,uid)
    resp={
      "error":False,
      "message":"item Added to cart",
      "data":""
    }
    return jsonify(resp)
  else:
    resp={
      "error":True,
      "message":"Something went wrong",
      "data":[]
    }
    return jsonify(resp)
      # resp = redirect(url_for("login"))
      # session['message']="please login"
      # return resp
  
  
@app.route("/update-cart-qty",methods=["POST"])
def updateCartQty():
  data=json.loads(request.data)
  print(data)
  respon=updateCartQTY(data)
  return jsonify({"error":"false","data":respon})








@app.route("/place-oder",methods=["POST"])
def updateUserOthers():
  data=json.loads(request.data)
  user=None
  if "USER" in session:
    user=session["USER"]
    uid=user[0]['uid']
    trackid=generateUnid(10)
    order=(uid,trackid,data['remail'],data['rname'],data['reference'],data['trans'],data['trxref'],data['raddress'],data['sometext'],data['phone'])
    print(order)
    placeOrder(order)
    return jsonify({"error":False,"message":"success"})
  else:
    return jsonify({"error":True,"message":"something went wrong contact suport"})
    
  
  
  
# end of api


# ********************************************
@app.route("/sendmail",methods=["GET"])
def sendFlaskEmail():
  try:
    msg = Message(
                    'Hello',
                    sender ='seunAAUA',
                    recipients = ['riolandadedamola@gmail.com']
                   )
    msg.body = '<h1>Hello Flask message sent from Flask-Mail</h1>'
    msg.html="<h1>Hello Flask message sent from Flask-Mail</h1>"
    
    mail.send(msg)
    return "ok let me text it"
  except Exception as e:
    print(e)
    return "llllll"













@app.route("/about")
def about():
  user=None
  cartCount=0
  if "USER" in session:
    user=session.get("USER")
    # USER = request.cookies.get('USER')
    cartCount=getCartCount(user[0]['uid'])
  return render("about.html",user=user,cartCount=cartCount)




@app.route("/cart")
def cart():
    user=None
    if "USER" in session:
      user=session.get("USER")
      cartCount=getCartCount(user[0]['uid'])
      mycart=getCarts(user[0]['uid'])
      subt=0
      for v in mycart:
        subt+=v['total']

      shipping=1500
      

      
      return render("cart.html",user=user,cartCount=cartCount,cartList=mycart,subt=subt,shipping=shipping)
    else:
      resp = redirect(url_for("login"))
      session['message']="please login"
      return resp




  
@app.route("/checkout")
def checkout():
    user=None
    if "USER" in session:
      user=session.get("USER")
      cartCount=getCartCount(user[0]['uid'])
      cartList=getCarts(user[0]['uid'])
      total=0
      for v in cartList:
        total+=v['total']
      shipping=1500
      
      return render("checkout.html",user=user,cartCount=cartCount,cartList=cartList,total=total,shipping=shipping)
    else:
      resp = redirect(url_for("login"))
      session['message']="please login"
      return resp
    


@app.route("/login")
def login():
  message=None
  if "message" in session:
    message=session["message"]
    session["message"]=""
  if "USER" in session:
    return redirect(url_for("index"))
  else:  
    return render("login.html",message=message)


@app.route("/signup")
def signUp():
  message=None
  if "message" in session:
    message=session["message"]
    session["message"]=""
  if "USER" in session:
    return redirect(url_for("index"))
  else:  
    # return render("login.html",message=message)
    return render("signup.html",message=message)


@app.route("/contact")
def contact():
  user=None
  cartCount=0
  if "USER" in session:
    user=session["USER"]
    cartCount=getCartCount(user[0]['uid'])
  return render("contact.html",user=user,cartCount=cartCount)
  
@app.route("/shop")
def shop():
  user=None
  cartCount=0
  if "USER" in session:
    user=session["USER"]
    cartCount=getCartCount(user[0]['uid'])
  return render("shop.html",user=user,cartCount=cartCount)
  


@app.route("/add-product")
def addProduct():
  message=None
  if "message" in session:
    message=session["message"]
    session["message"]=""
  
  return render("add-product.html",message=message)


  


@app.route("/logout")
def logout():
  for key in list(session.keys()):
     session.pop(key)
  user=None
  if "USER" in session:
    user=session["USER"]
  return redirect(url_for("login",user=user))








if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)