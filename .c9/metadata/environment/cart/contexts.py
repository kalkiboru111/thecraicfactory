{"filter":false,"title":"contexts.py","tooltip":"/cart/contexts.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":79},"action":"remove","lines":["from django.shortcuts import get_object_or_404","from posts.models import Post","","","def cart_contents(request):","    \"\"\"","    Ensures that the cart contents are available when rendering","    every page","    \"\"\"","    cart = request.session.get('cart', {})","","    cart_items = []","    total = 0","    post_count = 0","    ","    for id, quantity in cart.items():","        post = get_object_or_404(Post, pk=id)","        total += quantity * post.price","        post_count += quantity","        cart_items.append({'id': id, 'quantity': quantity, 'post': post})","    ","    return {'cart_items': cart_items, 'total': total, 'post_count': post_count}"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":85},"action":"insert","lines":["from django.shortcuts import get_object_or_404","from products.models import Product","","","def cart_contents(request):","    \"\"\"","    Ensures that the cart contents are available when rendering","    every page","    \"\"\"","    cart = request.session.get('cart', {})","","    cart_items = []","    total = 0","    product_count = 0","    ","    for id, quantity in cart.items():","        product = get_object_or_404(Product, pk=id)","        total += quantity * product.price","        product_count += quantity","        cart_items.append({'id': id, 'quantity': quantity, 'product': product})","    ","    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}"],"id":3}],[{"start":{"row":5,"column":4},"end":{"row":8,"column":7},"action":"remove","lines":["\"\"\"","    Ensures that the cart contents are available when rendering","    every page","    \"\"\""],"id":4},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["    "]},{"start":{"row":4,"column":27},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":84,"scrollleft":0,"selection":{"start":{"row":4,"column":27},"end":{"row":4,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/python"}},"timestamp":1570603135622,"hash":"b26297c2a64708332430acffae52bac4417c827b"}