from django import template
from django.template.base import VariableNode
from django.contrib.auth import get_user_model

from photos.models import Like


register = template.Library()

@register.filter(name = 'did_like')     #name생략가능
def did_like(photo, user):     #최대두개 최소한개의 인자를 받음
    return photo.like_set.filter(user = user).exists()

@register.filter(name = 'count_like')
def count_like(photo):
    return photo.like_set.all().count()

@register.simple_tag
def helloworld(*args, **kwargs):
    msg = []
    msg.append(','.join([str(a) for a in args]))

    msg.append('<ul>')
    for k,v in kwargs.items():
        msg.append('<li>{}:{}</li>'.format(k,v))
    msg.append('</ul>')
    return ''.join(msg)

@register.tag(name = 'addnim')
def add_nim(parser,token):      #token = 템플릿태그 자체
    nodelist = parser.parse(('endaddnim','end_add_nim'))     #태그를 닫을때까지 파싱을 해라, 두가지 다 가능
    parser.delete_first_token()
    return NimNode(nodelist)

class NimNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.user_class = get_user_model()

    def render(self, context):
        output = []

        for node in self.nodelist:
            if not isinstance(node, VariableNode):
                output.append(node.render(context))
                continue

            obj = node.filter_expression.resolve(context)       #template노드에 있는 컨텍스트객체를 가져오겠다
            if not isinstance(obj, self.user_class):
                output.append(node.render(context))
                continue

            output.append('{}님'.format(node.render(context)))

        return ''.join(output)
