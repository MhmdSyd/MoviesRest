from .models import MoviesRest
from rest_framework import serializers

class MoviesSerializers(serializers.ModelSerializer):

    class Meta:
        model = MoviesRest
        fields = ['id',
            'show_id',
            'title',
            'rating','year', 'count', 'poster', 'genre'
        ]
        read_only_fields = ('id','genre')
        
        extra_kwargs = {
            'year':{'write_only':True},
            'count':{'write_only':True},
            'poster':{'write_only':True},
        }
