
# example rXEjcaulT60
# no es uuid, es como las de youtube
import random
def gen_id() -> str:
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=11))

def gen_short_id() -> str:
    return ''.join(random.choices('abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ0123456789', k=5))

