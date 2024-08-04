from django.db import models, connection
from django.db.utils import DatabaseError
# Create your models here.

class Category:
    def all():
        # Step2 SQL語法
        sql = "SELECT * FROM category"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                turple_categories = cursor.fetchall()
                # print(turple_categories)
                # 將 turple 轉成 list
                categories = [{"id": category[0],"name":category[1]} for category in turple_categories]
                # print(categories)
                return categories
        except DatabaseError as e:
            print(f"讀取資料錯誤: { e }")
            return None
        
    def single(id):
        # Step2 SQL語法
        sql = "select * from category where category_id=%s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql,(id, ))
                categories = cursor.fetchone()
                return categories
        except DatabaseError as e:
            print(f"讀單筆資料有誤: { e }")
            return None

    def create(category_name):
        # step2 SQL INSERT
        sql = 'INSERT INTO category (name) VALUES (%s)'
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql,(category_name, ))
                connection.commit()
                return cursor.rowcount
        except DatabaseError as e:
            print(f"資料新增失敗: { e }")
            return None

    def update(id, category_name):
        # step2 SQL update
        sql = "UPDATE category SET name=%s WHERE category_id=%s"
        try:
            # step3 cursor 執行 SQL
            with connection .cursor() as cursor:
                cursor.execute(sql, (category_name, id))
                connection.commit()
                return cursor.rowcount
        except DatabaseError as e:
            print(f"資料修改失敗: { e }")
            return None

    def delete(id):
        # step2 SQL delete
        sql = "DELETE FROM category WHERE category_id=%s "
        try:
            # step3 cursor 執行 SQL
            with connection.cursor() as cursor:
                cursor.execute(sql,(id, )) 
                connection.commit()
                return cursor.rowcount
        except DatabaseError as e:
            print(f"資料刪除失敗: { e }")
            
        