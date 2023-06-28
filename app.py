from flask import Flask
from flask import render_template as render

app = Flask(__name__)

@app.route("/")
def index():
    return render("index.html")
  
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
def single-news():
    return render("single-news.html")


if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)