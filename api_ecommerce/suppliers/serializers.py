from rest_framework.serializers import ModelSerializer

from suppliers.models import SupplierModel

class SupplierSerializer(ModelSerializer):
    class Meta:
        model = SupplierModel
        fields = '__all__'