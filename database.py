import mysql.connector as conn

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



# sql="""
# CREATE TABLE `product` (
#   `pid` INT NOT NULL,
#   `pname` VARCHAR(45) NOT NULL,
#   `price` VARCHAR(45) NULL,
#   `disc` VARCHAR(2000) NULL,
#   PRIMARY KEY (`pid`));
# """
# cusor=connection.cursor()
# cusor.execute(sql)
# print(cusor.execute(sql))



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
  query="SELECT  `fullname`, `phone_number`, `email`FROM `users` WHERE `email`=%s AND `password`=%s"
  cs.execute(query,val)
  data=cs.fetchall()
  if len(data)>0:
    return data
  else:
    return None


def addPoductTcart(productid):
  cs=connection.cursor()
  query="SELECT `pid`, `pname`, `price`, `disc`,`image`, `meal_type` FROM `product`"
  query1="INSERT INTO product(pname, price, disc,meal_type ,image) VALUES (%s, %s, %s, %s, %s)"
  cs.execute(query,productid)
  return True

def createUser(detail):
  cs=connection.cursor()
  query="INSERT INTO `users`(`fullname`, `phone_number`, `email`, `password`) VALUES (%s, %s, %s, %s)"
  cs.execute(query,detail)
  
  return True

# print(loginUser(("riolandadedamola@gmail.com","Rioland@1")))


