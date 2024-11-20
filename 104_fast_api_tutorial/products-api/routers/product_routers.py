from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from services.product_service import ProductService
from schemas.product_schema import ProductCreate, ProductUpdate, Product

import logging 

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/all", response_model=List[Product], status_code= status.HTTP_200_OK)
async def getProducts(productService: ProductService = Depends()):
    products = await productService.getProducts()
    if not products:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Products are empty")
        
    return products

@router.post("/create", response_model=ProductCreate, status_code= status.HTTP_201_CREATED)
async def createProduct(product: ProductCreate , productService: ProductService = Depends()):
    createdProducts = await productService.createProduct(product)
    logger.info(f"successfully added {createdProducts}")
    return createdProducts


@router.get("/id/{id}", response_model=Product, status_code=status.HTTP_200_OK)
async def getProductById(id: str, productService: ProductService = Depends()):
    foundProduct =await productService.getProductById(id=id)
    if not foundProduct:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Product not found")
    return foundProduct


@router.put("/u/{id}", response_model=ProductCreate, status_code= status.HTTP_200_OK)
async def updateProduct(id: str, updatedProduct: ProductUpdate, productService: ProductService = Depends()):
    existingProd = await productService.getProductById(id=id)
    if not existingProd:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Products are empty")
    updatedProd = await productService.updateProduct(id=id, product=updatedProduct)
    logger.info("updated succesfully")
    return updatedProd


@router.delete("/d/{id}")
async def deleteMyProduct(id:str, productService: ProductService = Depends()):
    deleteProd = await productService.deleteProuct(id=id)
    logger.info("product deleted succesfully...")
    return deleteProd



@router.get("search/{category}", response_model=List[Product], status_code=status.HTTP_200_OK)
async def getOnSearch(category:str,  productService: ProductService = Depends()):
    getBySearchProds = await productService.getOnCategory(category=category)
    if not getBySearchProds:
        logger.error("hey, nothing found")
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="not found in search")
    logger.info(f"products are availabale in this {category} category")
    return getBySearchProds