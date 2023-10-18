from rest_framework import serializers
from.models import EmpolyeData

class EmployeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmpolyeData
        fields = ['firstName', 'lastName', 'eMail', 'phoneNumber']

    def create(self, validated_data):
        print(" i am in create method ")
        print(validated_data)
        name = validated_data['firstName']
        lname = validated_data['lastName']
        pnumber = validated_data['phoneNumber']
        email = validated_data['eMail']
        print(name, lname, pnumber, email)
        
        user = EmpolyeData.objects.create(firstName =name, lastName = lname, phoneNumber = pnumber, eMail = email)
        user.save()

        return user