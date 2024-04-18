import psycopg2
import json
import os

# Retrieve env variables
PG_DB_NAME=os.getenv('PG_DB_NAME')
PG_DB_USER=os.getenv('PG_DB_USER')
PG_HOST=os.getenv('PG_HOST')
PG_PASSWORD=os.getenv('PG_PASSWORD')

# Build connection to Postgres DB
conn = psycopg2.connect(f"dbname='{PG_DB_NAME}' user='{PG_DB_USER}' host='{PG_HOST}' password='{PG_PASSWORD}'")

# Create the function
def my_poc_function(action, product={}):

    if action == 'GET':
        with conn.cursor() as curs:
            curs.execute("""SELECT product_id, "name", description, CAST(cost_manufacture AS TEXT) FROM public.product_catalogue;""")
            many_rows = curs.fetchall()
            json_result = json.dumps(many_rows)
            
            print(json_result)
            return json_result

    elif action == 'POST':
        with conn.cursor() as curs:
            curs.execute(f"""
                         INSERT INTO public.product_catalogue (name, description, cost_manufacture) 
                         VALUES ('{product['name']}', '{product['description']}', '{product['cost_manufacture']}')
                         """)
            conn.commit()

            result = {
                "status":'Product inserted',
                "product": product
            }

            json_result = json.dumps(result)

            print(json_result)
            return json_result


# Add a product
product = {
    "name": 'Smart hat2', 
    "description": 'Special smart hat2', 
    "cost_manufacture": '125'
}
my_poc_function('POST',product)

# List all products
my_poc_function('GET')


    