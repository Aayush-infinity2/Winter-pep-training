from rest_framework import serializers
from .models import Students

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields = ['id','name','age','course']


    def validate_age(self, value):
        if value <= 5:
            raise serializers.ValidationError("Age must be greater than 5")
        return value    

#searilization : converts datas such as django models into json or xml


