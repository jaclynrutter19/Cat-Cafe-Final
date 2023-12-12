# Sample Flask application for a Foster Cat Relationship database, snapshot of Foster_Cat_Relationships
# Citation: Original code is reformatted by the bsg_people example and flask tutorial https://github.com/osu-cs340-ecampus/flask-starter-app/tree/master/bsg_people_app

from flask import Flask, render_template, json, redirect
#import database.db_connector as db
#db_connection = db.connect_to_database()
from flask_mysqldb import MySQL
from flask import request
import os



app = Flask(__name__)

# database connection
# Template:
# app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
# app.config["MYSQL_USER"] = "cs340_OSUusername"
# app.config["MYSQL_PASSWORD"] = "XXXX" | last 4 digits of OSU id
# app.config["MYSQL_DB"] = "cs340_OSUusername"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "cs340_"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Routes

# HOME PAGE
@app.route("/")
def home():
    return render_template("main.j2")

# CATS PAGE

# route to display cats page
@app.route("/cats", methods=["POST", "GET"])
def cats():
    if request.method == "GET":
        # Select all data from cats table
        query = "SELECT * FROM Cats" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        data = cur.fetchall()
    
        return render_template("cats.j2", cats=data)
    
    if request.method == "POST":
        
        if request.form.get("Add_Cat"):
            # Grab form input
            name = request.form["name"]
            date_of_birth = request.form["dob"]
            weight = request.form["weight"]
            color = request.form["color"]
            sex = request.form["sex"]
            adoptable = request.form["adoptable"]
            last_vet_check = request.form["vet"]
            
            # INSERT values
            query = "INSERT INTO Cats (name, date_of_birth, weight, color, sex, adoptable, last_vet_check) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, date_of_birth, weight, color, sex, adoptable, last_vet_check))
            mysql.connection.commit()

        # redirect to cat page
        return redirect("/cats")

# route to DELETE cat
@app.route("/delete_cat/<int:cat_id>")
def delete_cat(cat_id):
    # query to delete the cat with our passed cat id
    query = "DELETE FROM Cats WHERE cat_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (cat_id,))
    mysql.connection.commit()

    # redirect to cat page
    return redirect("/cats")

# route to EDIT cat
@app.route("/edit_cat/<int:cat_id>", methods=["POST", "GET"])
def edit_cat(cat_id):
    
    if request.method == "GET":
        #mySQL will grab the information based on the given ID
        query = "SELECT * FROM Cats WHERE cat_id = %s" % (cat_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("edit_cat.j2", cats=data)
    
    if request.method == "POST":
        if request.form.get("Edit_Cat"):
            # Grab form input
            name = request.form["name"]
            date_of_birth = request.form["dob"]
            weight = request.form["weight"]
            color = request.form["color"]
            sex = request.form["sex"]
            adoptable = request.form["adoptable"]
            last_vet_check = request.form["vet"]


            query = "UPDATE Cats SET Cats.name = %s, Cats.date_of_birth = %s, Cats.weight = %s, Cats.color = %s, Cats.sex = %s, Cats.adoptable = %s, Cats.last_vet_check = %s WHERE cat_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, date_of_birth, weight, color, sex, adoptable, last_vet_check, cat_id))
            mysql.connection.commit()


            return redirect("/cats")

# FOSTER PARENTS
@app.route("/foster_parents", methods=["POST", "GET"])
def foster_parents():
    if request.method == "GET":
        # Select all data from cats table
        query = "SELECT * FROM Foster_Parents" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        data = cur.fetchall()
    
        return render_template("foster_parents.j2", foster_parents=data)

    if request.method == "POST":
        
        if request.form.get("Add_Parent"):
            # Grab form input
            fname = request.form["fname"]
            lname = request.form["lname"]
            email = request.form["email"]
            phone = request.form["phone"]
            
            # INSERT values
            query = "INSERT INTO Foster_Parents (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (fname, lname, email, phone))
            mysql.connection.commit()
        
        # redirect to cat page
        return redirect("/foster_parents")

# route to DELETE foster_parent
@app.route("/delete_foster_parent/<int:foster_parent_id>")
def delete_foster_parent(foster_parent_id):
    # query to delete the cat with our passed cat id
    query = "DELETE FROM Foster_Parents WHERE foster_parent_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (foster_parent_id,))
    mysql.connection.commit()

     # redirect to foster_parents page
    return redirect("/foster_parents")

@app.route("/edit_parent/<int:foster_parent_id>", methods=["POST", "GET"])
def edit_parent(foster_parent_id):
    if request.method == "GET":
        query = "SELECT * FROM Foster_Parents WHERE foster_parent_id = '%s';"
        cur = mysql.connection.cursor()
        cur.execute(query, (foster_parent_id,))
        mysql.connection.commit()
        data = cur.fetchall()
        return render_template("/edit_foster_parent.j2", parents=data)
    if request.method == "POST":
        if request.form.get("edit_parent"):
            # Grab form input
            fname = request.form["fname"]
            lname = request.form["lname"]
            email = request.form["email"]
            phone = request.form["phone"]

            query = "UPDATE Foster_Parents SET Foster_Parents.first_name = %s, Foster_Parents.last_name = %s, Foster_Parents.email = %s, Foster_Parents.phone = %s WHERE foster_parent_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (fname, lname, email, phone, foster_parent_id))
            mysql.connection.commit()

            return redirect("/foster_parents")
    


# route for foster cat relationships page
@app.route("/foster_cat_relationships", methods=["POST", "GET"])
def relationships():
    if request.method == "GET":
        # Select all data from cafe transactions table
        query = "SELECT * FROM Foster_Cat_Relationships" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query = "SELECT Foster_Cat_Relationships.relationship_id As RelationshipID, Cats.name as Cat, concat(Foster_Parents.first_name, ' ', Foster_Parents.last_name) AS FosterParent FROM Foster_Cat_Relationships JOIN Cats on Foster_Cat_Relationships.cat_id=Cats.cat_id JOIN Foster_Parents ON Foster_Cat_Relationships.foster_parent_id=Foster_Parents.foster_parent_id ORDER BY relationship_id" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        all_data = cur.fetchall()

        query = "SELECT * FROM Cats" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        cat_data = cur.fetchall()

        query = "SELECT * FROM Foster_Parents" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        parent_data = cur.fetchall()
    
        return render_template("foster_cat_relationships.j2", relationships=data, cats=cat_data, parents=parent_data, all=all_data)
    
    if request.method == "POST":
        if request.form.get("Add_Relationship"):
            # Grab form input
            parent_id = request.form["foster_parent_id"]
            cat_id = request.form["cat_id"]

            # INSERT values
            query = "INSERT INTO Foster_Cat_Relationships (foster_parent_id, cat_id) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (parent_id, cat_id))
            mysql.connection.commit()

        # redirect to cafe transactions page
        return redirect("/foster_cat_relationships")
   

# route for delete functionality, deleting a foster cat relationship from Foster_Cat_Relationships,
# we want to pass the 'id' value of that foster cat relationship on button click (see HTML) via the route
@app.route("/delete_relationship/<int:relationship_id>")
def delete_relationship(relationship_id):
    # mySQL query to delete the foster cat relationship with our passed id
    query = "DELETE FROM Foster_Cat_Relationships WHERE relationship_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (relationship_id,))
    mysql.connection.commit()

    # redirect back to foster cat relationships page
    return redirect("/foster_cat_relationships")


# route for edit functionality, updating the attributes of a foster cat relationship in Foster_Cat_Relationships
# similar to our delete route, we want to the pass the 'id' value of that foster cat relationship on button click (see HTML) via the route
@app.route("/edit_foster_cat_relationship/<int:relationship_id>", methods=["POST", "GET"])
def edit_foster_cat_relationship(relationship_id):
    if request.method == "GET":
        # mySQL query to grab the info of the foster cat relationship with our passed id
        query = "SELECT * FROM Foster_Cat_Relationships WHERE relationship_id = %s" % (relationship_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query = "SELECT Foster_Cat_Relationships.relationship_id As RelationshipID, Cats.name as Cat, concat(Foster_Parents.first_name, ' ', Foster_Parents.last_name) AS FosterParent FROM Foster_Cat_Relationships JOIN Cats on Foster_Cat_Relationships.cat_id=Cats.cat_id JOIN Foster_Parents ON Foster_Cat_Relationships.foster_parent_id=Foster_Parents.foster_parent_id WHERE relationship_id = %s" % (relationship_id)
        cur = mysql.connect.cursor()
        cur.execute(query)
        all_data = cur.fetchall()

        query = "SELECT * FROM Cats" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        cat_data = cur.fetchall()

        query = "SELECT * FROM Foster_Parents" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        parent_data = cur.fetchall()

        # render edit_foster_cat_ page passing our query data and cat/foster data to the edit_foster_cat template
        return render_template("edit_foster_cat_relationship.j2", relationships=data, all=all_data, cats=cat_data, parents=parent_data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit foster cat relationship' button
        if request.form.get("Edit_Foster_Cat_Relationship"):
            # grab user form inputs
            cat_id = request.form["cat_id"]
            foster_parent_id = request.form["foster_parent_id"]

            query = "UPDATE Foster_Cat_Relationships SET Foster_Cat_Relationships.cat_id = %s, Foster_Cat_Relationships.foster_parent_id = %s WHERE relationship_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (cat_id, foster_parent_id, relationship_id))
            mysql.connection.commit()

            # redirect back to foster cat relationships page after we execute the update query
            return redirect("/foster_cat_relationships")

# Route to display employees page
@app.route("/employees", methods=["POST", "GET"])
def employees():
    if request.method == "GET":
        # Select all data from employees table
        query = "SELECT * FROM Employees" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        data = cur.fetchall()
    
        return render_template("employees.j2", employees=data)
    
    if request.method == "POST":
        
        if request.form.get("Add_Employee"):
            # Grab form input
            first_name = request.form["fname"]
            last_name = request.form["lname"]
            email = request.form["email"]
            phone = request.form["phone"]
            hourly_salary = request.form["salary"]
            
            # INSERT values
            query = "INSERT INTO Employees (first_name, last_name, email, phone, hourly_salary) VALUES (%s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email, phone, hourly_salary))
            mysql.connection.commit()

        # redirect to employee page
        return redirect("/employees")

# route to DELETE employee
@app.route("/delete_employee/<int:employee_id>")
def delete_employee(employee_id):
    # query to delete the employee with our passed employee id
    query = "DELETE FROM Employees WHERE employee_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (employee_id,))
    mysql.connection.commit()

    # redirect to employees page
    return redirect("/employees")


# route to EDIT employee
@app.route("/edit_employee/<int:employee_id>", methods=["POST", "GET"])
def edit_employee(employee_id):
    
    if request.method == "GET":
        #mySQL will grab the information based on the given ID
        query = "SELECT * FROM Employees WHERE employee_id = %s" % (employee_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("edit_employee.j2", employees=data)
    
    if request.method == "POST":
        if request.form.get("Edit_Employee"):
            # Grab form input
            first_name = request.form["fname"]
            last_name = request.form["lname"]
            email = request.form["email"]
            phone = request.form["phone"]
            hourly_salary = request.form["salary"]

            query = "UPDATE Employees SET Employees.first_name = %s, Employees.last_name = %s, Employees.email = %s, Employees.phone = %s, Employees.hourly_salary = %s WHERE employee_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email, phone, hourly_salary, employee_id))
            mysql.connection.commit()

            return redirect("/employees")

# route to display customers page
@app.route("/customers", methods=["POST", "GET"])
def customers():
    if request.method == "GET":
        # Select all data from customers table
        query = "SELECT * FROM Customers" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        data = cur.fetchall()
    
        return render_template("customers.j2", customers=data)
    
    if request.method == "POST":
        
        if request.form.get("Add_Customer"):
            # Grab form input
            first_name = request.form["fname"]
            last_name = request.form["lname"]
            email = request.form["email"]
            phone = request.form["phone"]
            
            # INSERT values
            query = "INSERT INTO Customers (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email, phone))
            mysql.connection.commit()

        # redirect to customers page
        return redirect("/customers")

# route to DELETE customer
@app.route("/delete_customer/<int:customer_id>")
def delete_customer(customer_id):
    # query to delete the customer with our passed customer id
    query = "DELETE FROM Customers WHERE customer_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (customer_id,))
    mysql.connection.commit()

    # redirect to customers page
    return redirect("/customers")



# route to EDIT customer
@app.route("/edit_customer/<int:customer_id>", methods=["POST", "GET"])
def edit_customer(customer_id):
    
    if request.method == "GET":
        #mySQL will grab the information based on the given ID
        query = "SELECT * FROM Customers WHERE customer_id = %s" % (customer_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("edit_customer.j2", customers=data)
    
    if request.method == "POST":
        if request.form.get("Edit_Customer"):
            # Grab form input
            first_name = request.form["fname"]
            last_name = request.form["lname"]
            email = request.form["email"]
            phone = request.form["phone"]


            query = "UPDATE Customers SET Customers.first_name = %s, Customers.last_name = %s, Customers.email = %s, Customers.phone = %s WHERE customer_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email, phone, customer_id))
            mysql.connection.commit()

            return redirect("/customers")


# CAFE PRODUCTS ENTITY

# route to display cafe products page
@app.route("/cafe_products", methods=["POST", "GET"])
def cafe_products():
    if request.method == "GET":
        # Select all data from cafe products table
        query = "SELECT * FROM Cafe_Products" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        data = cur.fetchall()
    
        return render_template("cafe_products.j2", cafe_products=data)
    
    if request.method == "POST":
        
        if request.form.get("Add_Cafe_Product"):
            # Grab form input
            name = request.form["name"]
            price = request.form["price"]
            quantity = request.form["quantity"]
            product_type = request.form["product-type"]
            
            # INSERT values
            query = "INSERT INTO Cafe_Products (name, price, quantity, product_type) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, price, quantity, product_type))
            mysql.connection.commit()

        # redirect to cafe products page
        return redirect("/cafe_products")

# route to DELETE cafe product
@app.route("/delete_cafe_product/<int:product_id>")
def delete_cafe_product(product_id):
    # query to delete the cafe product with our passed cafe product id
    query = "DELETE FROM Cafe_Products WHERE product_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (product_id,))
    mysql.connection.commit()

    # redirect to cafe products page
    return redirect("/cafe_products")


# route to EDIT cafe product
@app.route("/edit_cafe_product/<int:product_id>", methods=["POST", "GET"])
def edit_cafe_product(product_id):
    
    if request.method == "GET":
        #mySQL will grab the information based on the given ID
        query = "SELECT * FROM Cafe_Products WHERE product_id = %s" % (product_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("edit_cafe_product.j2", cafe_products=data)
    
    if request.method == "POST":
        if request.form.get("edit_cafe_product"):
            # Grab form input
            name = request.form["name"]
            price = request.form["price"]
            quantity = request.form["quantity"]
            product_type = request.form["product_type"]


            query = "UPDATE Cafe_Products SET Cafe_Products.name = %s, Cafe_Products.price = %s, Cafe_Products.quantity = %s, Cafe_Products.product_type = %s  WHERE product_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, price, quantity, product_type, product_id))
            mysql.connection.commit()


            return redirect("/cafe_products")




# ADOPTIONS ENTITY


# route to display adoptions page
@app.route("/adoptions", methods=["POST", "GET"])

def adoptions():

    if request.method == "GET":
        # Select all data from adoptions table
        query = "SELECT * FROM Adoptions" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query = "SELECT Adoptions.adoption_id as id, Adoptions.date AS Date, concat(Customers.last_name,' ', Customers.first_name) As Customer, concat(Employees.first_name, ' ', Employees.last_name) AS Employee, concat(Foster_Parents.first_name, ' ', Foster_Parents.last_name) AS Parent, Cats.name AS Cat FROM Adoptions JOIN Customers on Adoptions.customer_id = Customers.customer_id JOIN Employees on Adoptions.employee_id = Employees.employee_id JOIN Foster_Parents on Adoptions.foster_parent_id = Foster_Parents.foster_parent_id JOIN Cats on Adoptions.cat_id = Cats.cat_id ORDER BY id ASC;" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        all_data = cur.fetchall()

        query = "SELECT * FROM Customers" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        cus_data = cur.fetchall()

        query = "SELECT * FROM Cats" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        cat_data = cur.fetchall()

        query = "SELECT * FROM Foster_Parents" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        parent_data = cur.fetchall()

        query = "SELECT * FROM Employees" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        emp_data = cur.fetchall()

        return render_template("adoptions.j2", adoptions=data, customers = cus_data, cats=cat_data, parents = parent_data, employees=emp_data, all = all_data)
    
    if request.method == "POST":
        
        if request.form.get("Add_Adoption"):
            # Grab form input
            customer_id = request.form["customer_id"]
            cat_id = request.form["cat_id"]
            foster_parent_id = request.form["foster_parent_id"]
            employee_id = request.form["employee_id"]
            date = request.form["adoption_date"]
            
            # INSERT values
            query = "INSERT INTO Adoptions (customer_id, cat_id, foster_parent_id, employee_id, date) VALUES (%s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (customer_id, cat_id, foster_parent_id, employee_id, date))
            mysql.connection.commit()

        # redirect to adoptions page
        return redirect("/adoptions")

# route to DELETE adoption
@app.route("/delete_adoption/<int:adoption_id>")
def delete_adoption(adoption_id):
    # query to delete the adoption with our passed adoption id
    query = "DELETE FROM Adoptions WHERE adoption_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (adoption_id,))
    mysql.connection.commit()

    # redirect to adoptions page
    return redirect("/adoptions")

# route to EDIT adoptions
@app.route("/edit_adoption/<int:adoption_id>", methods=["POST", "GET"])
def edit_adoption(adoption_id):
    
    if request.method == "GET":
        #mySQL will grab the information based on the given ID
        query = "SELECT * FROM Adoptions WHERE adoption_id = %s" % (adoption_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
    
        query = "SELECT Adoptions.adoption_id as id, Adoptions.date AS Date, concat(Customers.first_name,' ', Customers.last_name) As Customer, concat(Employees.first_name, ' ', Employees.last_name) AS Employee, concat(Foster_Parents.first_name, ' ', Foster_Parents.last_name) AS Parent, Cats.name AS Cat FROM Adoptions JOIN Customers on Adoptions.customer_id = Customers.customer_id JOIN Employees on Adoptions.employee_id = Employees.employee_id JOIN Foster_Parents on Adoptions.foster_parent_id = Foster_Parents.foster_parent_id JOIN Cats on Adoptions.cat_id = Cats.cat_id WHERE adoption_id = %s ORDER BY id ASC;"  % (adoption_id)
        cur = mysql.connect.cursor()
        cur.execute(query)
        all_data = cur.fetchall()

        query = "SELECT * FROM Customers" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        cus_data = cur.fetchall()

        query = "SELECT * FROM Cats" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        cat_data = cur.fetchall()

        query = "SELECT * FROM Foster_Parents" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        parent_data = cur.fetchall()

        query = "SELECT * FROM Employees" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        emp_data = cur.fetchall()

        return render_template("edit_adoption.j2", adoptions=data, all = all_data, employees = emp_data, parents=parent_data, cats = cat_data, customers=cus_data)
    
    if request.method == "POST":
        if request.form.get("Edit_Adoption"):
            # Grab form input
            customer_id = request.form["customer_id"]
            cat_id = request.form["cat_id"]
            foster_parent_id = request.form["foster_parent_id"]
            employee_id = request.form["employee_id"]
            date = request.form["date"]


            query = "UPDATE Adoptions SET Adoptions.customer_id = %s, Adoptions.cat_id = %s, Adoptions.foster_parent_id = %s, Adoptions.employee_id = %s, Adoptions.date = %s WHERE adoption_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (customer_id, cat_id, foster_parent_id, employee_id, date, adoption_id))
            mysql.connection.commit()


            return redirect("/adoptions")

# CAFE TRANSACTIONS ENTITY


# route to display cafe transactions page
@app.route("/cafe_transactions", methods=["POST", "GET"])
def cafe_transactions():
    if request.method == "GET":
        # Select all data from cafe transactions table
        query = "SELECT * FROM Cafe_Transactions" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query = "SELECT * FROM Customers" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        cus_data = cur.fetchall()

        query = "SELECT * FROM Employees" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        emp_data = cur.fetchall()

        query = "SELECT Cafe_Transactions.transaction_id as id, Cafe_Transactions.order_date as Date,  concat(Customers.first_name, ' ', Customers.last_name) as Customer, concat(Employees.first_name, ' ', Employees.last_name) as Employee, Cafe_Transactions.total_price as Total FROM Cafe_Transactions JOIN Employees ON Cafe_Transactions.employee_id = Employees.employee_id JOIN Customers ON Cafe_Transactions.customer_id = Customers.customer_id ORDER BY transaction_id" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        all_data = cur.fetchall()
    
        return render_template("cafe_transactions.j2", cafe_transactions=data, all = all_data, customers = cus_data, employees=emp_data)
    
    if request.method == "POST":
        
        if request.form.get("Add_Cafe_Transaction"):
            # Grab form input
            customer_id = request.form["customer_id"]
            employee_id = request.form["employee_id"]
            order_date = request.form["date"]
            total_price = request.form["total_price"]
            
            # INSERT values
            query = "INSERT INTO Cafe_Transactions (customer_id, employee_id, order_date, total_price) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (customer_id, employee_id, order_date, total_price))
            mysql.connection.commit()

        # redirect to cafe transactions page
        return redirect("/cafe_transactions")

# route to DELETE cafe transaction
@app.route("/delete_cafe_transaction/<int:transaction_id>")
def delete_cafe_transaction(transaction_id):
    # query to delete the cafe transaction with our passed transaction id
    query = "DELETE FROM Cafe_Transactions WHERE transaction_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (transaction_id,))
    mysql.connection.commit()

    # redirect to cafe transactions page
    return redirect("/cafe_transactions")


# route to EDIT cafe transaction
@app.route("/edit_cafe_transaction/<int:transaction_id>", methods=["POST", "GET"])
def edit_cafe_transaction(transaction_id):
    
    if request.method == "GET":
        #mySQL will grab the information based on the given ID
        query = "SELECT * FROM Cafe_Transactions WHERE transaction_id = %s" % (transaction_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query = "SELECT * FROM Customers" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        cus_data = cur.fetchall()

        query = "SELECT * FROM Employees" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        emp_data = cur.fetchall()

        query = "SELECT Cafe_Transactions.transaction_id as id, Cafe_Transactions.order_date as Date,  concat(Customers.first_name, ' ', Customers.last_name) as Customer, concat(Employees.first_name, ' ', Employees.last_name) as Employee, Cafe_Transactions.total_price as Total FROM Cafe_Transactions JOIN Employees ON Cafe_Transactions.employee_id = Employees.employee_id JOIN Customers ON Cafe_Transactions.customer_id = Customers.customer_id WHERE transaction_id = %s ORDER BY transaction_id" % (transaction_id)
        cur = mysql.connect.cursor()
        cur.execute(query)
        all_data = cur.fetchall()
        return render_template("edit_cafe_transaction.j2", cafe_transactions=data, customers = cus_data, employees=emp_data, all=all_data)
    
    if request.method == "POST":
        if request.form.get("Edit_Transaction"):
            # Grab form input
            customer_id = request.form["customer_id"]
            employee_id = request.form["employee_id"]
            order_date = request.form["date"]
            total_price = request.form["total_price"]


            query = "UPDATE Cafe_Transactions SET Cafe_Transactions.customer_id = %s, Cafe_Transactions.employee_id = %s, Cafe_Transactions.order_date = %s, Cafe_Transactions.total_price = %s WHERE transaction_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (customer_id, employee_id, order_date, total_price, transaction_id))
            mysql.connection.commit()


        return redirect("/cafe_transactions")

# PRODUCT ORDERS ENTITY

# route to display product orders entities page
@app.route("/product_orders", methods=["POST", "GET"])
def product_orders():
    if request.method == "GET":
        # Select all data from product orders table
        query = "SELECT * FROM Product_Orders" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query = "SELECT Product_Orders.product_order_id as id, Product_Orders.transaction_id AS TransactionID, Cafe_Products.name AS Product, Product_Orders.quantity, Cafe_Transactions.order_date as Date FROM Product_Orders JOIN Cafe_Products on Product_Orders.product_id = Cafe_Products.product_id JOIN Cafe_Transactions ON Product_Orders.transaction_id = Cafe_Transactions.transaction_id;" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        all_data = cur.fetchall()

        query = "SELECT * FROM Cafe_Transactions" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        trans_data = cur.fetchall()

        query = "SELECT * FROM Cafe_Products" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        prod_data = cur.fetchall()
    
        return render_template("product_orders.j2", product_orders=data, products=prod_data, transactions=trans_data, all=all_data)
    
    if request.method == "POST":
        
        if request.form.get("Add_Product_Order"):
            # Grab form input
            transaction_id = request.form["transaction_id"]
            product_id = request.form["product_id"]
            quantity = request.form["quantity"]
            
            # INSERT values
            query = "INSERT INTO Product_Orders (transaction_id, product_id, quantity) VALUES (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (transaction_id, product_id, quantity))
            mysql.connection.commit()

        # redirect to product orders page
        return redirect("/product_orders")

# route to DELETE product order
@app.route("/delete_product_order/<int:product_order_id>")
def delete_product_order(product_order_id):
    # query to delete product order with our passed product order id
    query = "DELETE FROM Product_Orders WHERE product_order_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (product_order_id,))
    mysql.connection.commit()

    # redirect to product orders page
    return redirect("/product_orders")

# route to EDIT product order
@app.route("/edit_product_order/<int:product_order_id>", methods=["POST", "GET"])
def edit_product_order(product_order_id):
    
    if request.method == "GET":
        #mySQL will grab the information based on the given ID
        query = "SELECT * FROM Product_Orders WHERE product_order_id = %s" % (product_order_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query = "SELECT Product_Orders.product_order_id as id, Product_Orders.transaction_id AS TransactionID, Cafe_Products.name AS Product, Product_Orders.quantity, Cafe_Transactions.order_date as Date FROM Product_Orders JOIN Cafe_Products on Product_Orders.product_id = Cafe_Products.product_id JOIN Cafe_Transactions ON Product_Orders.transaction_id = Cafe_Transactions.transaction_id WHERE product_order_id = %s;"  % (product_order_id)
        cur = mysql.connect.cursor()
        cur.execute(query)
        all_data = cur.fetchall()

        query = "SELECT * FROM Cafe_Transactions" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        trans_data = cur.fetchall()

        query = "SELECT * FROM Cafe_Products" 
        cur = mysql.connect.cursor()
        cur.execute(query)
        prod_data = cur.fetchall()

        return render_template("edit_product_order.j2", product_orders=data, all=all_data, transactions=trans_data, products=prod_data)
    

    
    if request.method == "POST":
        if request.form.get("Edit_Product_Order"):
            # Grab form input
            transaction_id = request.form["transaction-id"]
            product_id = request.form["product_id"]
            quantity = request.form["quantity"]


            query = "UPDATE Product_Orders SET Product_Orders.transaction_id = %s, Product_Orders.product_id = %s, Product_Orders.quantity = %s WHERE product_order_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (transaction_id, product_id, quantity, product_order_id))
            mysql.connection.commit()


            return redirect("/product_orders")


# route to display foster cat relationships page

# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 30242)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 