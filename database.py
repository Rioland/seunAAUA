import mysql.connector as conn
# import smtplib
from email.mime.text import MIMEText
# import MySQLdb as conn

# connection = conn.connect(
#   host= os.getenv("HOST"),
#   user=os.getenv("USERNAME"),
#   passwd= os.getenv("PASSWORD"),
#   db= os.getenv("DATABASE"),
#   autocommit = True,
#   ssl_mode = "VERIFY_IDENTITY",
#   ssl      = {
#     "ca": "/etc/ssl/cert.pem"
#   }
# )

HOST="db4free.net "
USERNAME="acoinclub"
PASSWORD="Rioland@1"
DATABASE="acoinclub"
# HOST="aws.connect.psdb.cloud"
# USERNAME="nr07orm4dvw1vn44rmfo"
# PASSWORD="pscale_pw_KWMqULDaH1a1Lr6DUnJU1NcQ9BZFUqb5zpnC4bH8nMF"
# DATABASE="seunaaua"



connection = conn.connect(
  host =HOST,
  user =USERNAME,
  passwd =PASSWORD,
  db=DATABASE,
  autocommit = True,
)




def addPoductToDB(detail):
  cs=connection.cursor()
  query="INSERT INTO product(pname, price, disc,meal_type ,image) VALUES (%s, %s, %s, %s, %s)"
  cs.execute(query,detail)
  return True


def getProductFromDb():
  cs=connection.cursor(dictionary=True)
  query="SELECT `pid`, `pname`, `price`, `disc`,`image`, `meal_type` FROM `product`"
  cs.execute(query)
  data=cs.fetchall()
  return data
  
def loginUser(val):
  cs=connection.cursor(dictionary=True)
  query="SELECT uid, fullname, phone_number,email FROM users WHERE email=%s AND password=%s"
  cs.execute(query,val)
  data=cs.fetchall()
  if len(data)>0:
    return data
  else:
    return None



def createUser(detail):
  cs=connection.cursor()
  query="INSERT INTO `users`(`fullname`, `phone_number`, `email`, `password`) VALUES (%s, %s, %s, %s)"
  cs.execute(query,detail)
  
  return True

# print(loginUser(("riolandadedamola@gmail.com","Rioland@1")))



def getCartCount(userid):
  cs=connection.cursor(dictionary=True)
  query=f"SELECT * FROM cart WHERE uid='{userid}'"
  cs.execute(query)
  data=cs.fetchall()
  if len(data)>0:
    return len(data)
  else:
    return None





def getCarts(userid):
  cs=connection.cursor(dictionary=True)
  query=f"SELECT product.pname, product.price,product.image,product.pid, cart.cid, cart.uid,cart.qty, (product.price * cart.qty)as total FROM cart INNER JOIN product ON product.pid=cart.pid WHERE cart.uid='{userid}'"
  cs.execute(query)
  data=cs.fetchall()
  print(data)
  if len(data)>0:
    return data
  else:
    return None





def addTocart(pid,uid):
  try:
    cs=connection.cursor()
    query=f"SELECT pid,uid FROM `cart` WHERE `pid`='{pid}'"
    cs.execute(query)
    data=cs.fetchall()
    # print(data)
    
    if len(data) >0:

      query2=f"UPDATE cart SET qty=qty+1 WHERE pid={pid}"
      cs.execute(query2)
      print("update")
    else:
      hj=(uid,pid,"1")
      query3=f"INSERT INTO cart(uid, pid,qty) VALUES ('{uid}','{pid}','1')"
      cs.execute(query3)
      print("set new")
    return True
  except OSError:
     print(OSError)
     return False
    

def addTOOther(pid,uid):
  orderId=generateUnid(10)
  try:
    cs=connection.cursor()
    query=f"SELECT pid,uid FROM `cart` WHERE `pid`='{pid}'"
    cs.execute(query)
    data=cs.fetchall()
    # print(data)
    
    if len(data) >0:
      query2=f"UPDATE cart SET qty=qty+1 WHERE pid={pid}"
      cs.execute(query2)
      print("update")
    else:
      hj=(uid,pid,"1")
      query3=f"INSERT INTO cart(uid, pid,qty) VALUES ('{uid}','{pid}','1')"
      cs.execute(query3)
      print("set new")
    return True
  except OSError:
     print(OSError)
     return False
    


def updateCartQTY(data={}):
  cs=connection.cursor()
  query2=f"UPDATE cart SET qty={data['qty']} WHERE cid={data['cid']}"
  cs.execute(query2)
  return True;
  





def placeOrder(order):
  cs=connection.cursor(dictionary=True)
  query="INSERT INTO orders( uid, trackingID, email, name, reference, trans, trxref, address, someText,phone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  cs.execute(query,order)
  query2=f"SELECT pid,uid,qty FROM `cart` WHERE `uid`='{order[0]}'"
  cs.execute(query2)
  cart=cs.fetchall()
  print(cart)
  for rows in cart:
    uid=rows["uid"]
    pid=rows["pid"]
    qty=rows["qty"]
    tid=order[1]
    q3=f"INSERT INTO `orders_details` (`uid`, `pid`, `qty`, `trackingID`) VALUES ({uid},{pid},{qty},{tid})"
    cs.execute(q3)
    
  query3=f"DELETE FROM `cart` WHERE `uid`='{order[0]}'"
  cs.execute(query3)


