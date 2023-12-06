from rest_framework import serializers

from call_center.models import Agent, Queue


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = '__all__'


class QueueSerializer(serializers.ModelSerializer):
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.all(),
        write_only=True
    )
    agent_name = serializers.StringRelatedField(
        source='agent',
        read_only=True
    )

    class Meta:
        model = Queue
        fields = (
            'id',
            'name',
            'skill',
            'agent',
            'agent_name'
        )

