from django import template
from mongoengine import connect

from ..models import Author, Quote

connect(db='database', host="mongodb+srv://olesyashevchuk0402:JeJ6Bb00zAnOUTRL@cluster0.ki8cwf1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

register = template.Library()

def tags(note_tags):
    return ', '.join([str(name) for name in note_tags.all()])


register.filter('tags', tags)