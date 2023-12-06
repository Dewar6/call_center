from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from call_center.models import Agent, Queue
from call_center.serializers import AgentSerializer, QueueSerializer


class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        agent_id = data.get('agent', None)

        if Queue.objects.filter(agent_id=agent_id).exists():
            return Response(
                {'detail': 'Этот агент уже участвует в другой очереди'}
            )

        return super().create(request, *args, **kwargs)


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

