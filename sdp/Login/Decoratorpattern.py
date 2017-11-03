######### Author :  Noboni #########

from django.template import loader
from abc import ABC, abstractmethod
from django.http import HttpResponse
class Component(ABC):
    def operation(self):
        pass


class Decorator(Component,ABC):
    def __init__(self, component):
        self._component = component
    def operation(self):
        pass


class ConcreteDecoratorB(Decorator):
    def operation(self):
        p=self._component.operation()
        return HttpResponse(p)

class ConcreteDecoratorA(Decorator):
    def operation(self):
        k = self._component.operation()
        return k.render(self._component.context, self._component.request)


class ConcreteComponent(Component):
    def __init__(self, request,context,templatename):
        self.request=request
        self.context =context
        self.tempaltename =templatename
    def operation(self):
        return loader.get_template( self.tempaltename)