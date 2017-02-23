from django.contrib import admin

# Register your models here.
from .models import SubwayModel

class SubwayModelAdmin(admin.ModelAdmin):
    fields=[
        'date',
        'station',
        'line_number',
        'population0',
        'population1',
        'population2',
        'population3',
        'population4',
        'population5',
        'population6',
        'population7',
        'population8',
        'population9',
        'population10',
        'population11',
        'population12',
        'population13',
        'population14',
        'population15',
        'population16',
        'population17',
        'population18',
        'population19',
        'population20',
        'population21',
        'population22',
        'population23',
        ]

    readonly_fields=['date',
            'station',
            'line_number',
            'population0',
            'population1',
            'population2',
            'population3',
            'population4',
            'population5',
            'population6',
            'population7',
            'population8',
            'population9',
            'population10',
            'population11',
            'population12',
            'population13',
            'population14',
            'population15',
            'population16',
            'population17',
            'population18',
            'population19',
            'population20',
            'population21',
            'population22',
            'population23',]

    class Meta:
        model=SubwayModel

admin.site.register(SubwayModel, SubwayModelAdmin)
