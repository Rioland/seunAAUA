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
  connection.close()
  return True


def getProductFromDb():
  cs=connection.cursor(dictionary=True)
  query="SELECT `pid`, `pname`, `price`, `disc`,`image`, `meal_type` FROM `product`"
  cs.execute(query)
  data=cs.fetchall()
  return data

print(getProductFromDb())


