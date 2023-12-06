from rest_framework import serializers

from call_center.models import Agent, Queue


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = '__all__'


class QueueSerializer(serializers.ModelSerializer):
    agents = serializers.PrimaryKeyRelatedField(
            queryset=Agent.objects.all(),
            many=True,
            required=False,
        )

    class Meta:
        model = Queue
        fields = (
            'id',
            'name',
            'skill',
            'agents',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        agents = representation.get('agents')

        if agents:
            return representation
        else:
            return {'id': representation['id'],
                    'name': representation['name'],
                    'skill': representation['skill'],
                    'agents': 'В данный момент нет активных агентов',}