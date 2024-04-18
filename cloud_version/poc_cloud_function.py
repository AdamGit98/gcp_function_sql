import functions_framework
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

@functions_framework.http
def hello_http(request):
    
    # Prepare input
    request_method = request.method
    request_json = request.get_json(silent=True)
    
    # Identify GET request and act accordingly
    if request_method == 'GET':
        with conn.cursor() as curs:
            curs.execute("""SELECT product_id, "name", description, CAST(cost_manufacture AS TEXT) FROM public.product_catalogue;""")
            many_rows = curs.fetchall()
            response = json.dumps(many_rows)

    # Identify POST request and act accordingly
    elif request_method == 'POST' and request_json and request_json.get('product', False):
        received_product = request_json['product']
        with conn.cursor() as curs:
            curs.execute(f"""
                         INSERT INTO public.product_catalogue (name, description, cost_manufacture) 
                         VALUES ('{received_product['name']}', '{received_product['description']}', '{received_product['cost_manufacture']}')
                         """)
            conn.commit()
            result = {"status":'Product inserted', "product": received_product}
            response = json.dumps(result)

    # If input is not adequate for our 2 methods return message
    else:
        raise RuntimeError("Your request could not be processed") 

    return response