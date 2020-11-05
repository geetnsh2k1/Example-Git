from django import template
from home.models import Like, Product
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag(name='like')
def like(pname, username):
    user = User.objects.get(username=username)
    
    product = Product.objects.get(name=pname)
    try:
        like = Like.objects.filter(product=product, user=user)
        if len(like) == 0:
            return 'Likes'
        else:
            return 'Unlike'
    except Exception as e:
        print(e)

@register.simple_tag(name='counter')
def counter(pname):
    product = Product.objects.get(name=pname)
    like = Like.objects.get(product=product)
    return like.count