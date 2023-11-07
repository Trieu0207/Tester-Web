import json
from datetime import datetime
from flask_login import current_user, login_user
from numpy.testing import assert_equal

from saleapp import untils, models
from saleapp import app, db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def load_categories_to_terminal():
    data = untils.load_categories()
    for d in data:
        print(d.id)
        print(d.name)
        print("============")


def load_products_to_terminal(num):
    with app.app_context():
        if num.isdigit():
            data = untils.load_products(num, None)
        for d in data:
            print("=========================")
            print(d.name)
            print(d.price)
            print(d.image)
            print(d.active)
            print(d.quantity)
            print(d.category_id)
            print(d.created_date)


def test_load_categories():
    with app.app_context():
        data = untils.load_categories()
        assert data is None
        # print("\n")
        # for d in data:
        #     print(d.id)
        #     print(d.name)
        #     print("============")


def test_load_products():
    with app.app_context():
        data = untils.load_products(50, None)
        data2 = untils.load_products(cate_id= 2, name ="Batman")
        data3 = untils.load_products(cate_id= 2)
        data4 = untils.load_products(name="lập trình")
        data5 = untils.load_products(name = "None")
        for d in data5:
            print(d.id)
            print(d.name)
            print("============")



def test_load_all_products():
    with app.app_context():
        data = untils.load_all_products()
        assert data is not None

def test_load_all_product_is_query():
    with app.app_context():
        data = untils.load_all_products()
        assert type(data).__name__ == "Query"
        for d in data:
            print("=========================")
            print(d.name)
            print(d.price)
            print(d.image)
            print(d.active)
            print(d.quantity)
            print(d.category_id)
            print(d.created_date)
def test_active_load_products():
    with app.app_context():
        active_product = models.Product(name='Active product', category_id = 1, active = True)
        unactive_product = models.Product(name = 'UnActive product', category_id = 1, active = False)
        db.session.add_all([active_product, unactive_product])
        db.session.commit()
        products = untils.load_all_products()
        assert active_product in products.all()
        assert unactive_product not in products.all()
def test_add_product():
    with app.app_context():
        untils.add_product("Book1", "2", "ABC", "120", "mota 1",
                           "https://i.pinimg.com/564x/82/44/fc/8244fc27134978a867198b7c7fd6a228.jpg", "12000")
        data = untils.load_all_products()
        for d in data:
            print("=========================")
            print(d.name)
            print(d.price)
            print(d.image)
            print(d.active)
            print(d.quantity)
            print(d.category_id)
            print(d.created_date)
def test_delete_product_by_id():
    with app.app_context():
        product = models.Product(name='Test product', category_id=1, active=True)
        db.session.add(product)
        db.session.commit()
        name = "Test product"
        product = models.Product.query.filter(models.Product.name == name)
        id = product.id
        untils.delete_product_by_id(id)
        data = untils.get_product_by_id(id)
        assert data is None
        count_product_befor = models.Product.query.count()
        untils.delete_product_by_id(500)
        untils.delete_product_by_id(-20)
        count_product = models.Product.query.count()
        assert_equal(count_product_befor, count_product)
def test_delete_chi_tiet_nhap_sach_by_id():
    with app.app_context():
        untils.delete_chi_tiet_nhap_sach_by_id()

def test_delete_comment_by_id():
    with app.app_context():

        # # data = untils.delete_comment_by_id(-50)
        # untils.delete_comment_by_id(28)
        # # data2 = models.Comment.query.filter(models.Comment.product_id == 28)
        # # assert data2 is None
        # # assert data is not Exception
        untils.add_comment(content="comment_test_1", product_id=28)
        untils.add_comment(content="comment_test_2", product_id=28)
        data = models.Comment.query.filter(models.Comment.product_id == 28).all()
        assert_equal([], data)

def test_products_stats():
    # test case 1:
    with app.app_context():
        data = untils.products_stats(kw = "Batman", from_date = datetime(2023, 3, 1))
        assert data != []
        data = untils.products_stats(kw = "Batman",from_date = datetime(2023, 4, 1),
                                     to_date=datetime(2023, 10, 1))
        assert data != []
        data = untils.products_stats(kw = "Batman",from_date = datetime(2023, 4, 1),
                                     to_date=datetime(2022, 10, 1))
        assert data == []
        data = untils.products_stats(kw = "Batman")
        assert data != []
        data = untils.products_stats(kw = "Batman",to_date = datetime(2023, 10, 1))
        assert data != []
        data = untils.products_stats()
        assert data != []
        data = untils.products_stats(to_date = datetime(2023, 4, 30))
        assert data != []
        data = untils.products_stats(from_date = datetime(2023, 4, 1))
        assert data != []
        data = untils.products_stats(from_date = datetime(2023, 3, 1), to_date = datetime(2022, 10, 1))
        assert data == []
        data = untils.products_stats(from_date = datetime(2025, 4, 1), to_date = datetime(2022, 10, 1))
        assert data == []
        data = untils.products_stats(from_date = datetime(2023, 3, 1), to_date = datetime(2023, 4, 1))
        assert data != []

        # for d in data: print(d)
def test_add_receipt():
    with app.app_context():
        # test case 1
        data = untils.add_receipt(cart= None)
        assert data is not None
        # test case 2
def test_count_product():
    with app.app_context():
        data = untils.count_product(category_id=1, kw=None)
        data2 = untils.count_product(category_id=-1, kw=None)
        data3 = untils.count_product(category_id=None, kw="lập trình")
        data4 = untils.count_product(category_id=None, kw="!##$%$%^")
        data5 = untils.count_product(category_id=None, kw=None)
        print(data, data2, data3, data4, data5)
def test_count_cart():
    #test case 1
    data = untils.count_cart(cart=None)
    assert data['total_quantity'] == 0 and data['total_amount'] == 0

    # test case 2
    cart = {
        "1":{
            "id": 3,
            "quantity": -2,
            "price": 100000
        }
    }
    data = untils.count_cart(cart)
    assert data['total_quantity'] == 0 and data['total_amount'] == 0

    # test case 3
    cart = {
        "1":{
            "id": 3,
            "quantity": 5,
            "price": 100000
        }
    }
    data = untils.count_cart(cart)
    assert data['total_amount'] > 0 and data['total_quantity'] > 0
    # test case 4
    cart = {
        "1": {
            "id": 3,
            "quantity": 0,
            "price": 100000
        }
    }
    data = untils.count_cart(cart)
    assert data['total_amount'] == 0 and data['total_quantity'] == 0
def test_minus_product_quality():
    with app.app_context():
        data = untils.minus_product_quality(id=2, value=-50)
        data2 = untils.minus_product_quality(id = -2, value= 5)
def test_add_user():
    with app.app_context():
        # untils.add_user(name = "Nguyen Van A", username = "user_test", password = "1", diachi = "hcm")
        data = models.User.query.filter(models.User.username.__eq__("user_test"))
        e = None
        try:
            untils.add_user(name="Nguyen Van A", username="user_test", password="1", diachi="hcm")
        except: e = Exception
        assert e != None
def add_receipt():
    with app.app_context():
        user_test = models.User.query.get(2)
        receipt = models.Receipt(payment=0)
        user_receipt = models.UserReceipt(user=user_test, receipt=receipt)
        data4 = untils.get_all_receipt_not_pay(id=receipt.id)
        product = models.Product.query.get(5)
        d = models.ReceiptDetail(receipt=receipt,
                                 product_id=product.id,
                                 quantity=2,
                                 unit_price=product.price)
        db.session.add(d)
        db.session.add(receipt)
        db.session.add(user_receipt)
        db.session.commit()
def test_get_all_receipt_not_pay():
    with app.app_context():
        data = untils.get_all_receipt_not_pay(id = -50)
        data2 = untils.get_all_receipt_not_pay(id = 3)
        data3 = untils.get_all_receipt_not_pay(id=2)
        print(data2, data3)
        # add_receipt()
        last_receipt = db.session.query(models.Receipt).order_by(models.Receipt.id.desc()).first()
        data4 = untils.get_all_receipt_not_pay(id = last_receipt.id)
        print(data4)
def test_add_product():
    with app.app_context():
        data = untils.add_product(name="book_test", category="thieu nhi", author="LeMinhKhue",
                                  quantity=300, mota="nhapsach",
                                  avatar=None, price=-150000)
        print(data)
def test_check_login():
    with app.app_context():
        data = untils.check_login(None, None)
        assert data is None
        data = untils.check_login(username="test_user_1", password="1")
        assert data is None
        data = untils.check_login(username="hoang1", password="1")
        assert data is not None
        data = untils.check_login(username="hoang1", password="123abc")
        assert data is None
def test_category_month_stats():
   with app.app_context():
       data = untils.category_month_stats(month=0)
       data2 = untils.category_month_stats(month=13)
       data3 = untils.category_month_stats(month= -2)
       assert data == {} and data2 == {} and data3 == {}
       data4 = untils.category_month_stats(month= 4)
       assert data4 != {}
def test_product_count_month_stats():
    with app.app_context():
        data = untils.product_count_month_stats(0)
        data2 = untils.product_count_month_stats(13)
        data3 = untils.product_count_month_stats(-5)
        assert data == {} and data2 == {} and data3 == {}
        data4 = untils.product_count_month_stats(4)
        assert data4 != {}
        print("\n")
        for d in data4:
            print(d)
if __name__ == '__main__':
    load_products_to_terminal("50")
