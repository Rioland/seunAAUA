from flask import Flask,request,redirect, url_for,make_response,Response
from flask import render_template as render
from werkzeug.utils import secure_filename
from functions import isNotEmpty
from database import * 
app = Flask(__name__)



# products=[
#   {
#   "id":1,
#   "name":"Amala",
#   "price":"1500",
#   "desc":"hgasjgdjhas asjhgdhasd jhasghdgas ",
#   "kg":2,
#   "image":"static/product/amala.webp",
#   "type":2
# },

#    {
#   "id":2,
#   "name":"Eforiro",
#   "price":"1500",
#   "desc":"hgasjgdjhas asjhgdhasd jhasghdgas ",
#   "kg":2,
#   "image":"static/product/eforiro.jpeg",
#   "type":2
# },

#   {
#   "id":3,
#   "name":"Frey DODO",
#   "price":"1500",
#   "desc":"hgasjgdjhas asjhgdhasd jhasghdgas ",
#   "kg":2,
#   "image":"static/product/frey_dodo.webp",
#   "type":1
# },

#    {
#   "id":3,
#   "name":"Ogbona",
#   "price":"1500",
#   "desc":"hgasjgdjhas asjhgdhasd jhasghdgas ",
#   "kg":2,
#   "image":"static/product/ogbona.webp",
#   "type":2
# }
# ]


# page routes
@app.route("/")
def index():
    product=getProductFromDb()
    return render("index.html",products=product)





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
         resp = make_response(redirect("/add-product"))
         resp.set_cookie('message', 'successfull',expires=2)
         return resp
      else:
         resp = make_response(redirect("/add-product",expires=2))
         resp.set_cookie('message', output,expires=2)
         return resp

     
    else:
      resp = make_response(redirect("/add-product"))
      resp.set_cookie('message', 'All fields are required',expires=2)
      return resp
  else:
      resp = make_response(redirect("/add-product"))
      resp.set_cookie('message', 'invalid method',expires=2)
      return resp

# end of api

  
@app.route("/about")
def about():
    return render("about.html")
  
@app.route("/cart")
def cart():
    return render("cart.html")
  
@app.route("/checkout")
def checkout():
    return render("checkout.html")


@app.route("/contact")
def contact():
    return render("contact.html")
  
@app.route("/shop")
def shop():
    return render("shop.html")
  
@app.route("/single-product")
def singlepage():
    return render("single-product.html")

@app.route("/news")
def news():
    return render("news.html")

@app.route("/single-news")
def singlenews():
    return render("single-news.html")

@app.route("/add-product")
def addProduct():
    message = request.cookies.get('message')
    # Response.set_cookie('message', None)
    return render("add-product.html",message=message)









if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)