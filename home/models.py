from django.db import models, connection 

# Create your models here.
class Sakila:
    def countries():
        with connection.cursor() as cursor:
            cursor.execute('select country_id, country from country')
            countries = cursor.fetchall()
            return countries
    def categories():
        with connection.cursor() as cursor:
            cursor.execute('select category_id, name from category')
            categories = cursor.fetchall()
            return categories
        
    
    # 根據國家編號 讀取城市資料
    def cities(id=1):
        with connection.cursor() as cursor:
            cursor.execute(f"select city_id, city from sakila.city where country_id = {id}")
            cities= cursor.fetchall()
            return cities