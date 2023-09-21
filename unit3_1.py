def linearSearchProduct(productList, targetProduct):
    indices = []

    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)
    
    return indices

products = ["shoes", "boat", "loafer", "sandal", "shoes"]
target = "shoes"
target2 = "apples"
result = linearSearchProduct(products, target)
print(result)