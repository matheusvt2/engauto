from rest_framework import serializers

from .models import History
# class HistorySerializer(serializers.HyperlinkedModelSerializer):

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ('id','job', 'server','server_user', 'script', 'terminal', 'exectime', 'terminal_error', 'returncode')