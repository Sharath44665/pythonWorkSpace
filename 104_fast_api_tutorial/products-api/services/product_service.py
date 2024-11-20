from typing import List
from config.prisma_config import prisma
from schemas.product_schema import Product as ProductSchema, ProductCreate, ProductUpdate

class ProductService:
    async def getProducts(self) -> List[ProductSchema]: # arrow marks means, its going to return List[ProductSchema] for the respective function
        products = await prisma.product.find_many()
        return [ProductSchema(** prod.model_dump()) for prod in products]


    async def createProduct(self, product: ProductUpdate) -> ProductSchema:
        createdProduct = await prisma.product.create(data=product.model_dump())
        return ProductSchema(**createdProduct.model_dump())
    
   

    async def getProductById(self, id:str) -> ProductSchema:
        singleProd = await prisma.product.find_unique(where={'id':id})
        if not singleProd:
            return None
        return ProductSchema(**singleProd.model_dump())

    async def updateProduct(self, id: str, product: ProductUpdate) -> ProductSchema:
        updatedProd = await prisma.product.update(where={'id':id}, data=product.model_dump())
        return ProductSchema(**updatedProd.model_dump())


    async def deleteProuct(self, id:str) -> ProductSchema:
        deletedProd = await prisma.product.delete(where={"id":id})
        return ProductSchema(**deletedProd.model_dump())
    
    async def getOnCategory(self, category:str) -> List[ProductSchema]:
        getProds = await prisma.product.find_many(where={ 'category':{"contains": category}})
        # print(getProds)
        return [ProductSchema(**myval.model_dump()) for myval in getProds]