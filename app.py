from flask import Flask
from flask import render_template as render

app = Flask(__name__)



products=[
  {
  "id":1,
  "name":"Amala",
  "price":"1500",
  "desc":"hgasjgdjhas asjhgdhasd jhasghdgas ",
  "kg":2,
  "image":"static/product/amala.webp",
  "type":2
},

   {
  "id":2,
  "name":"Eforiro",
  "price":"1500",
  "desc":"hgasjgdjhas asjhgdhasd jhasghdgas ",
  "kg":2,
  "image":"static/product/eforiro.jpeg",
  "type":2
},

  {
  "id":3,
  "name":"Frey DODO",
  "price":"1500",
  "desc":"hgasjgdjhas asjhgdhasd jhasghdgas ",
  "kg":2,
  "image":"static/product/frey_dodo.webp",
  "type":1
},

   {
  "id":3,
  "name":"Ogbona",
  "price":"1500",
  "desc":"hgasjgdjhas asjhgdhasd jhasghdgas ",
  "kg":2,
  "image":"static/product/ogbona.webp",
  "type":2
}
]







@app.route("/")
def index():
    return render("index.html",products=products)
  
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


if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)