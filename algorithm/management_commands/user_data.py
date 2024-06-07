import panda as pd
from ..models import Property, PropertyPrice, PropertyMedia, PropertyLocation, PropertyContact, PropertyExtraInfo
from django.core.management.base import BaseCommand

class ImportDataCommand(BaseCommand):
    help = 'Imports real estate data and user interaction data into the system.'

    def handle(self, *args, **options):
        data = pd.read_csv('../dataset.csv')
        
        for index, row in data.iterrows():
            property = Property.objects.create(
                property_title=row['property_title'],
                property_description=row['property_description'],
                property_status=row['property_status'],
            )
            
            
        
