import pygame

class Renderer:
    objects = []

    @staticmethod
    def add_object(obj):
        Renderer.objects.append(obj)

    @staticmethod
    def render_all():
        for obj in Renderer.objects:
            obj.draw()
