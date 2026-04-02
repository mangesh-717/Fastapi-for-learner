# Initialize APIRouter
from fastapi import APIRouter, HTTPException , FastAPI
from pydantic import BaseModel

from datetime import datetime, timedelta


from fastapi import FastAPI, Request, File, UploadFile, Form, HTTPException


from fastapi import FastAPI, Request, UploadFile, File, Depends, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
# from some_module import get_db, crud, schemas, models

app = FastAPI()

@app.api_route('/products', methods=['GET', 'POST', 'PUT', 'DELETE'])
async def manage_products(
    request: Request,
    file: UploadFile = File(None),
    name: str = Form(None),
    description: str = Form(None)
):
    if request.method == 'GET':
        # Handle GET request
        return {"message": "Products fetched successfully"}

    elif request.method == 'POST':
        # Handle POST request
        # if file and name and description:
        # contents = await file.read()
        # Process the uploaded file and form data
        return {
                "message": "Product created successfully",
                "filename": file,
                "name": name,
                "description": description
            }

    elif request.method == 'PUT':
        # Handle PUT request
        form = await request.form()
        product_id = form.get('product_id')
        name = form.get('name')
        description = form.get('description')
        # if file:
        #     filename = file.filename
        #     # Save the file and update other fields
        #     with open(f'uploads/{filename}', 'wb') as f:
        #         f.write(file.file.read())
        #     crud.update_product(db, product_id=product_id, name=name, description=description, filename=filename)
        # else:
            # crud.update_product(db, product_id=product_id, name=name, description=description)
        return {"message": f"{file.filename} ++++ {product_id}+ {name}+{description}+....Product updated successfully"}

    elif request.method == 'DELETE':
        # Handle DELETE request
        form = await request.form()
        filename = form.get('filename')
        # if filename:
        #     crud.delete_product_by_filename(db, filename)
        return {"message": f"{filename}Product deleted successfully"}
        # else:
        #     raise HTTPException(status_code=400, detail="Filename required")

# # Placeholder CRUD operations and database models
# class crud:
#     @staticmethod
#     def get_products(db):
#         # Fetch products from the database
#         return db.query(models.Product).all()

#     @staticmethod
#     def create_product(db, name, description, filename):
#         # Insert new product into the database
#         new_product = models.Product(name=name, description=description, filename=filename)
#         db.add(new_product)
#         db.commit()

#     @staticmethod
#     def update_product(db, product_id, name, description, filename=None):
#         # Update existing product in the database
#         product = db.query(models.Product).filter(models.Product.id == product_id).first()
#         if product:
#             product.name = name
#             product.description = description
#             if filename:
#                 product.filename = filename
#             db.commit()

#     @staticmethod
#     def delete_product_by_filename(db, filename):
#         # Delete product from the database by filename
#         product = db.query(models.Product).filter(models.Product.filename == filename).first()
#         if product:
#             db.delete(product)
#             db.commit()

# class models:
#     class Product:
#         id = 1
#         name = ''
#         description = ''
#         filename = ''

# class schemas:
#     class Product:
#         id: int
#         name: str
#         description: str
#         filename: str

# class get_db:
#     pass
