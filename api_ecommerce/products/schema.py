import graphene
from products.models import ProductModel

from products.types import ProductType

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product_by_id = graphene.Field(ProductType, id=graphene.String(required=True))

    def resolve_all_products(root, info, name=None):
        return ProductModel.objects.all()
    
    def resolve_product_by_id(root, info, id):
        try:
            return ProductModel.objects.get(id=id)
        except:
            return None
        
schema = graphene.Schema(query=Query)