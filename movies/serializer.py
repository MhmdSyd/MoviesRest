from rest_framework import serializers
from .models import MoviesRest

class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MoviesRest 
        fields = [
            'show_id',
            'title',
            'year',
            'rating',
        ]
