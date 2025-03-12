# coreui/templatetags/slots.py

from django.template import Node

def parse_slots(nodelist, context):
    slots = {"default": nodelist.render(context)}
    # Extend this to parse named slots if needed
    return slots
