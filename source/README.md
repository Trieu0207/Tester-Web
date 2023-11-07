#How to install app

0. Clone this git and open it on python IDE. Go to \saleapp\models.py and run it to create table first
1. Next, you must install mysql powershell. We recommend that you should install mysql workbench.
2. After you install mysql workbench, you need to create a schema name it "quanlybansach" and set charset="utf8mb4"
3. In mysql workbench, you must import database by using script in folder: \SQL 
4. Open python IDE, in "_init.py_", you have to change username and password: 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{username}:{password}@localhost/quanlybansach?charset=utf8mb4'
5. We done, run "index.py" and enjoy
