from __future__ import absolute_import

from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('email',
                  'first_name',
                  'last_name',
                  'is_active',
                  'is_staff',
                  'date_joined',
        )


