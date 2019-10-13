{"filter":false,"title":"views.py","tooltip":"/checkout/views.py","undoManager":{"mark":78,"position":78,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":3},{"start":{"row":0,"column":0},"end":{"row":60,"column":145},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404, reverse, redirect","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .forms import MakePaymentForm, OrderForm","from .models import OrderLineItem","from django.conf import settings","from django.utils import timezone","from products.models import Product","import stripe","","# Create your views here.","stripe.api_key = settings.STRIPE_SECRET","","","@login_required()","def checkout(request):","    if request.method == \"POST\":","        order_form = OrderForm(request.POST)","        payment_form = MakePaymentForm(request.POST)","","        if order_form.is_valid() and payment_form.is_valid():","            order = order_form.save(commit=False)","            order.date = timezone.now()","            order.save()","","            cart = request.session.get('cart', {})","            total = 0","            for id, quantity in cart.items():","                product = get_object_or_404(Product, pk=id)","                total += quantity * product.price","                order_line_item = OrderLineItem(","                    order=order,","                    product=product,","                    quantity=quantity","                )","                order_line_item.save()","            ","            try:","                customer = stripe.Charge.create(","                    amount=int(total * 100),","                    currency=\"EUR\",","                    description=request.user.email,","                    card=payment_form.cleaned_data['stripe_id']","                )","            except stripe.error.CardError:","                messages.error(request, \"Your card was declined!\")","            ","            if customer.paid:","                messages.error(request, \"You have successfully paid\")","                request.session['cart'] = {}","                return redirect(reverse('products'))","            else:","                messages.error(request, \"Unable to take payment\")","        else:","            print(payment_form.errors)","            messages.error(request, \"We were unable to take a payment with that card!\")","    else:","        payment_form = MakePaymentForm()","        order_form = OrderForm()","    ","    return render(request, \"checkout.html\", {\"order_form\": order_form, \"payment_form\": payment_form, \"publishable\": settings.STRIPE_PUBLISHABLE})"]}],[{"start":{"row":50,"column":41},"end":{"row":50,"column":49},"action":"remove","lines":["products"],"id":4},{"start":{"row":50,"column":41},"end":{"row":50,"column":42},"action":"insert","lines":["p"]},{"start":{"row":50,"column":42},"end":{"row":50,"column":43},"action":"insert","lines":["o"]},{"start":{"row":50,"column":43},"end":{"row":50,"column":44},"action":"insert","lines":["s"]},{"start":{"row":50,"column":44},"end":{"row":50,"column":45},"action":"insert","lines":["t"]},{"start":{"row":50,"column":45},"end":{"row":50,"column":46},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":11},"action":"remove","lines":["produc"],"id":5},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["p"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["o"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["s"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["t"],"id":6}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":32},"action":"remove","lines":["roduct"],"id":7},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["o"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["s"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"insert","lines":["p"],"id":8},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"insert","lines":["o"]},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["s"]},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"remove","lines":["t"],"id":9},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"remove","lines":["s"]},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"remove","lines":["o"]},{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"remove","lines":["p"]},{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"remove","lines":["t"]},{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"remove","lines":["c"]},{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"remove","lines":["u"]},{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"remove","lines":["d"]},{"start":{"row":28,"column":18},"end":{"row":28,"column":19},"action":"remove","lines":["o"]}],[{"start":{"row":28,"column":17},"end":{"row":28,"column":18},"action":"remove","lines":["r"],"id":10}],[{"start":{"row":28,"column":17},"end":{"row":28,"column":18},"action":"insert","lines":["o"],"id":11},{"start":{"row":28,"column":18},"end":{"row":28,"column":19},"action":"insert","lines":["s"]},{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":41},"end":{"row":28,"column":48},"action":"remove","lines":["Product"],"id":12},{"start":{"row":28,"column":41},"end":{"row":28,"column":42},"action":"insert","lines":["P"]},{"start":{"row":28,"column":42},"end":{"row":28,"column":43},"action":"insert","lines":["o"]},{"start":{"row":28,"column":43},"end":{"row":28,"column":44},"action":"insert","lines":["s"]},{"start":{"row":28,"column":44},"end":{"row":28,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":29,"column":36},"end":{"row":29,"column":42},"action":"remove","lines":["produc"],"id":13},{"start":{"row":29,"column":36},"end":{"row":29,"column":37},"action":"insert","lines":["p"]},{"start":{"row":29,"column":37},"end":{"row":29,"column":38},"action":"insert","lines":["o"]},{"start":{"row":29,"column":38},"end":{"row":29,"column":39},"action":"insert","lines":["s"]}],[{"start":{"row":32,"column":26},"end":{"row":32,"column":27},"action":"insert","lines":["p"],"id":14},{"start":{"row":32,"column":27},"end":{"row":32,"column":28},"action":"insert","lines":["o"]},{"start":{"row":32,"column":28},"end":{"row":32,"column":29},"action":"insert","lines":["s"]},{"start":{"row":32,"column":29},"end":{"row":32,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":32,"column":29},"end":{"row":32,"column":30},"action":"remove","lines":["t"],"id":15},{"start":{"row":32,"column":28},"end":{"row":32,"column":29},"action":"remove","lines":["s"]},{"start":{"row":32,"column":27},"end":{"row":32,"column":28},"action":"remove","lines":["o"]},{"start":{"row":32,"column":26},"end":{"row":32,"column":27},"action":"remove","lines":["p"]}],[{"start":{"row":32,"column":25},"end":{"row":32,"column":26},"action":"remove","lines":["c"],"id":16},{"start":{"row":32,"column":24},"end":{"row":32,"column":25},"action":"remove","lines":["u"]},{"start":{"row":32,"column":23},"end":{"row":32,"column":24},"action":"remove","lines":["d"]},{"start":{"row":32,"column":22},"end":{"row":32,"column":23},"action":"remove","lines":["o"]},{"start":{"row":32,"column":21},"end":{"row":32,"column":22},"action":"remove","lines":["r"]}],[{"start":{"row":32,"column":21},"end":{"row":32,"column":22},"action":"insert","lines":["o"],"id":17},{"start":{"row":32,"column":22},"end":{"row":32,"column":23},"action":"insert","lines":["s"]},{"start":{"row":32,"column":23},"end":{"row":32,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":32,"column":23},"end":{"row":32,"column":24},"action":"remove","lines":["t"],"id":18}],[{"start":{"row":32,"column":25},"end":{"row":32,"column":32},"action":"remove","lines":["product"],"id":19},{"start":{"row":32,"column":25},"end":{"row":32,"column":26},"action":"insert","lines":["p"]},{"start":{"row":32,"column":26},"end":{"row":32,"column":27},"action":"insert","lines":["o"]},{"start":{"row":32,"column":27},"end":{"row":32,"column":28},"action":"insert","lines":["s"]},{"start":{"row":32,"column":28},"end":{"row":32,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":10},"action":"remove","lines":["posts"],"id":20},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["p"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["r"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["o"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["d"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["u"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["c"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["t"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":32},"action":"remove","lines":["Post"],"id":21},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["P"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["r"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["o"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["d"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["u"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["c"]},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":16},"end":{"row":28,"column":20},"action":"remove","lines":["post"],"id":22},{"start":{"row":28,"column":16},"end":{"row":28,"column":17},"action":"insert","lines":["p"]},{"start":{"row":28,"column":17},"end":{"row":28,"column":18},"action":"insert","lines":["r"]},{"start":{"row":28,"column":18},"end":{"row":28,"column":19},"action":"insert","lines":["o"]},{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":["d"]},{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":["u"]},{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":["c"]},{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":44},"end":{"row":28,"column":48},"action":"remove","lines":["Post"],"id":23},{"start":{"row":28,"column":44},"end":{"row":28,"column":45},"action":"insert","lines":["P"]},{"start":{"row":28,"column":45},"end":{"row":28,"column":46},"action":"insert","lines":["r"]},{"start":{"row":28,"column":46},"end":{"row":28,"column":47},"action":"insert","lines":["o"]},{"start":{"row":28,"column":47},"end":{"row":28,"column":48},"action":"insert","lines":["d"]},{"start":{"row":28,"column":48},"end":{"row":28,"column":49},"action":"insert","lines":["u"]},{"start":{"row":28,"column":49},"end":{"row":28,"column":50},"action":"insert","lines":["c"]},{"start":{"row":28,"column":50},"end":{"row":28,"column":51},"action":"insert","lines":["t"]}],[{"start":{"row":29,"column":36},"end":{"row":29,"column":40},"action":"remove","lines":["post"],"id":24},{"start":{"row":29,"column":36},"end":{"row":29,"column":37},"action":"insert","lines":["p"]},{"start":{"row":29,"column":37},"end":{"row":29,"column":38},"action":"insert","lines":["r"]},{"start":{"row":29,"column":38},"end":{"row":29,"column":39},"action":"insert","lines":["o"]},{"start":{"row":29,"column":39},"end":{"row":29,"column":40},"action":"insert","lines":["d"]},{"start":{"row":29,"column":40},"end":{"row":29,"column":41},"action":"insert","lines":["u"]},{"start":{"row":29,"column":41},"end":{"row":29,"column":42},"action":"insert","lines":["c"]},{"start":{"row":29,"column":42},"end":{"row":29,"column":43},"action":"insert","lines":["t"]}],[{"start":{"row":32,"column":20},"end":{"row":32,"column":24},"action":"remove","lines":["post"],"id":25},{"start":{"row":32,"column":20},"end":{"row":32,"column":21},"action":"insert","lines":["p"]},{"start":{"row":32,"column":21},"end":{"row":32,"column":22},"action":"insert","lines":["r"]},{"start":{"row":32,"column":22},"end":{"row":32,"column":23},"action":"insert","lines":["o"]},{"start":{"row":32,"column":23},"end":{"row":32,"column":24},"action":"insert","lines":["d"]},{"start":{"row":32,"column":24},"end":{"row":32,"column":25},"action":"insert","lines":["u"]},{"start":{"row":32,"column":25},"end":{"row":32,"column":26},"action":"insert","lines":["c"]},{"start":{"row":32,"column":26},"end":{"row":32,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":32,"column":28},"end":{"row":32,"column":32},"action":"remove","lines":["post"],"id":26},{"start":{"row":32,"column":28},"end":{"row":32,"column":29},"action":"insert","lines":["p"]},{"start":{"row":32,"column":29},"end":{"row":32,"column":30},"action":"insert","lines":["r"]},{"start":{"row":32,"column":30},"end":{"row":32,"column":31},"action":"insert","lines":["o"]},{"start":{"row":32,"column":31},"end":{"row":32,"column":32},"action":"insert","lines":["d"]},{"start":{"row":32,"column":32},"end":{"row":32,"column":33},"action":"insert","lines":["u"]},{"start":{"row":32,"column":33},"end":{"row":32,"column":34},"action":"insert","lines":["c"]},{"start":{"row":32,"column":34},"end":{"row":32,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":50,"column":41},"end":{"row":50,"column":46},"action":"remove","lines":["posts"],"id":27},{"start":{"row":50,"column":41},"end":{"row":50,"column":42},"action":"insert","lines":["p"]},{"start":{"row":50,"column":42},"end":{"row":50,"column":43},"action":"insert","lines":["r"]},{"start":{"row":50,"column":43},"end":{"row":50,"column":44},"action":"insert","lines":["o"]},{"start":{"row":50,"column":44},"end":{"row":50,"column":45},"action":"insert","lines":["d"]},{"start":{"row":50,"column":45},"end":{"row":50,"column":46},"action":"insert","lines":["u"]},{"start":{"row":50,"column":46},"end":{"row":50,"column":47},"action":"insert","lines":["c"]},{"start":{"row":50,"column":47},"end":{"row":50,"column":48},"action":"insert","lines":["t"]},{"start":{"row":50,"column":48},"end":{"row":50,"column":49},"action":"insert","lines":["s"]}],[{"start":{"row":52,"column":41},"end":{"row":52,"column":63},"action":"remove","lines":["Unable to take payment"],"id":28},{"start":{"row":52,"column":41},"end":{"row":52,"column":42},"action":"insert","lines":["Y"]},{"start":{"row":52,"column":42},"end":{"row":52,"column":43},"action":"insert","lines":["o"]},{"start":{"row":52,"column":43},"end":{"row":52,"column":44},"action":"insert","lines":["u"]},{"start":{"row":52,"column":44},"end":{"row":52,"column":45},"action":"insert","lines":["r"]}],[{"start":{"row":52,"column":45},"end":{"row":52,"column":46},"action":"insert","lines":[" "],"id":29},{"start":{"row":52,"column":46},"end":{"row":52,"column":47},"action":"insert","lines":["m"]},{"start":{"row":52,"column":47},"end":{"row":52,"column":48},"action":"insert","lines":["o"]},{"start":{"row":52,"column":48},"end":{"row":52,"column":49},"action":"insert","lines":["n"]},{"start":{"row":52,"column":49},"end":{"row":52,"column":50},"action":"insert","lines":["e"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"insert","lines":["y"]}],[{"start":{"row":52,"column":51},"end":{"row":52,"column":52},"action":"insert","lines":[" "],"id":30},{"start":{"row":52,"column":52},"end":{"row":52,"column":53},"action":"insert","lines":["i"]},{"start":{"row":52,"column":53},"end":{"row":52,"column":54},"action":"insert","lines":["s"]}],[{"start":{"row":52,"column":54},"end":{"row":52,"column":55},"action":"insert","lines":[" "],"id":31},{"start":{"row":52,"column":55},"end":{"row":52,"column":56},"action":"insert","lines":["n"]},{"start":{"row":52,"column":56},"end":{"row":52,"column":57},"action":"insert","lines":["o"]}],[{"start":{"row":52,"column":57},"end":{"row":52,"column":58},"action":"insert","lines":[" "],"id":32},{"start":{"row":52,"column":58},"end":{"row":52,"column":59},"action":"insert","lines":["g"]},{"start":{"row":52,"column":59},"end":{"row":52,"column":60},"action":"insert","lines":["o"]},{"start":{"row":52,"column":60},"end":{"row":52,"column":61},"action":"insert","lines":["o"]},{"start":{"row":52,"column":61},"end":{"row":52,"column":62},"action":"insert","lines":["d"]}],[{"start":{"row":52,"column":62},"end":{"row":52,"column":63},"action":"insert","lines":[" "],"id":33},{"start":{"row":52,"column":63},"end":{"row":52,"column":64},"action":"insert","lines":["h"]},{"start":{"row":52,"column":64},"end":{"row":52,"column":65},"action":"insert","lines":["e"]},{"start":{"row":52,"column":65},"end":{"row":52,"column":66},"action":"insert","lines":["r"]},{"start":{"row":52,"column":66},"end":{"row":52,"column":67},"action":"insert","lines":["e"]},{"start":{"row":52,"column":67},"end":{"row":52,"column":68},"action":"insert","lines":["."]},{"start":{"row":52,"column":68},"end":{"row":52,"column":69},"action":"insert","lines":["."]},{"start":{"row":52,"column":69},"end":{"row":52,"column":70},"action":"insert","lines":["."]}],[{"start":{"row":52,"column":70},"end":{"row":52,"column":71},"action":"insert","lines":[" "],"id":34},{"start":{"row":52,"column":71},"end":{"row":52,"column":72},"action":"insert","lines":["n"]},{"start":{"row":52,"column":72},"end":{"row":52,"column":73},"action":"insert","lines":["o"]},{"start":{"row":52,"column":73},"end":{"row":52,"column":74},"action":"insert","lines":["r"]}],[{"start":{"row":52,"column":74},"end":{"row":52,"column":75},"action":"insert","lines":[" "],"id":35}],[{"start":{"row":52,"column":74},"end":{"row":52,"column":75},"action":"remove","lines":[" "],"id":36},{"start":{"row":52,"column":73},"end":{"row":52,"column":74},"action":"remove","lines":["r"]}],[{"start":{"row":52,"column":73},"end":{"row":52,"column":74},"action":"insert","lines":[","],"id":37}],[{"start":{"row":52,"column":74},"end":{"row":52,"column":75},"action":"insert","lines":[" "],"id":38},{"start":{"row":52,"column":75},"end":{"row":52,"column":76},"action":"insert","lines":["r"]},{"start":{"row":52,"column":76},"end":{"row":52,"column":77},"action":"insert","lines":["e"]},{"start":{"row":52,"column":77},"end":{"row":52,"column":78},"action":"insert","lines":["a"]},{"start":{"row":52,"column":78},"end":{"row":52,"column":79},"action":"insert","lines":["l"]},{"start":{"row":52,"column":79},"end":{"row":52,"column":80},"action":"insert","lines":["l"]},{"start":{"row":52,"column":80},"end":{"row":52,"column":81},"action":"insert","lines":["y"]},{"start":{"row":52,"column":81},"end":{"row":52,"column":82},"action":"insert","lines":["."]},{"start":{"row":52,"column":82},"end":{"row":52,"column":83},"action":"insert","lines":["."]},{"start":{"row":52,"column":83},"end":{"row":52,"column":84},"action":"insert","lines":["."]}],[{"start":{"row":55,"column":37},"end":{"row":55,"column":79},"action":"remove","lines":["We were unable to take a payment with that"],"id":39}],[{"start":{"row":55,"column":38},"end":{"row":55,"column":42},"action":"remove","lines":["card"],"id":40},{"start":{"row":55,"column":37},"end":{"row":55,"column":38},"action":"remove","lines":[" "]}],[{"start":{"row":55,"column":37},"end":{"row":55,"column":38},"action":"insert","lines":["I"],"id":41},{"start":{"row":55,"column":38},"end":{"row":55,"column":39},"action":"insert","lines":["s"]}],[{"start":{"row":55,"column":39},"end":{"row":55,"column":40},"action":"insert","lines":[" "],"id":42},{"start":{"row":55,"column":40},"end":{"row":55,"column":41},"action":"insert","lines":["t"]},{"start":{"row":55,"column":41},"end":{"row":55,"column":42},"action":"insert","lines":["h"]},{"start":{"row":55,"column":42},"end":{"row":55,"column":43},"action":"insert","lines":["a"]},{"start":{"row":55,"column":43},"end":{"row":55,"column":44},"action":"insert","lines":["t"]}],[{"start":{"row":55,"column":44},"end":{"row":55,"column":45},"action":"insert","lines":[" "],"id":43},{"start":{"row":55,"column":45},"end":{"row":55,"column":46},"action":"insert","lines":["a"]}],[{"start":{"row":55,"column":46},"end":{"row":55,"column":47},"action":"insert","lines":[" "],"id":44},{"start":{"row":55,"column":47},"end":{"row":55,"column":48},"action":"insert","lines":["D"]},{"start":{"row":55,"column":48},"end":{"row":55,"column":49},"action":"insert","lines":["i"]},{"start":{"row":55,"column":49},"end":{"row":55,"column":50},"action":"insert","lines":["s"]},{"start":{"row":55,"column":50},"end":{"row":55,"column":51},"action":"insert","lines":["c"]},{"start":{"row":55,"column":51},"end":{"row":55,"column":52},"action":"insert","lines":["o"]},{"start":{"row":55,"column":52},"end":{"row":55,"column":53},"action":"insert","lines":["v"]},{"start":{"row":55,"column":53},"end":{"row":55,"column":54},"action":"insert","lines":["e"]},{"start":{"row":55,"column":54},"end":{"row":55,"column":55},"action":"insert","lines":["r"]}],[{"start":{"row":55,"column":55},"end":{"row":55,"column":56},"action":"insert","lines":[" "],"id":45},{"start":{"row":55,"column":56},"end":{"row":55,"column":57},"action":"insert","lines":["C"]},{"start":{"row":55,"column":57},"end":{"row":55,"column":58},"action":"insert","lines":["a"]},{"start":{"row":55,"column":58},"end":{"row":55,"column":59},"action":"insert","lines":["r"]},{"start":{"row":55,"column":59},"end":{"row":55,"column":60},"action":"insert","lines":["d"]}],[{"start":{"row":55,"column":60},"end":{"row":55,"column":61},"action":"insert","lines":[" "],"id":46},{"start":{"row":55,"column":61},"end":{"row":55,"column":62},"action":"insert","lines":["b"]},{"start":{"row":55,"column":62},"end":{"row":55,"column":63},"action":"insert","lines":["y"]}],[{"start":{"row":55,"column":63},"end":{"row":55,"column":64},"action":"insert","lines":[" "],"id":47},{"start":{"row":55,"column":64},"end":{"row":55,"column":65},"action":"insert","lines":["a"]},{"start":{"row":55,"column":65},"end":{"row":55,"column":66},"action":"insert","lines":["n"]},{"start":{"row":55,"column":66},"end":{"row":55,"column":67},"action":"insert","lines":["y"]}],[{"start":{"row":55,"column":67},"end":{"row":55,"column":68},"action":"insert","lines":[" "],"id":48},{"start":{"row":55,"column":68},"end":{"row":55,"column":69},"action":"insert","lines":["c"]},{"start":{"row":55,"column":69},"end":{"row":55,"column":70},"action":"insert","lines":["h"]},{"start":{"row":55,"column":70},"end":{"row":55,"column":71},"action":"insert","lines":["a"]},{"start":{"row":55,"column":71},"end":{"row":55,"column":72},"action":"insert","lines":["n"]},{"start":{"row":55,"column":72},"end":{"row":55,"column":73},"action":"insert","lines":["c"]},{"start":{"row":55,"column":73},"end":{"row":55,"column":74},"action":"insert","lines":["e"]},{"start":{"row":55,"column":74},"end":{"row":55,"column":75},"action":"insert","lines":["?"]}],[{"start":{"row":55,"column":75},"end":{"row":55,"column":76},"action":"remove","lines":["!"],"id":49}],[{"start":{"row":55,"column":37},"end":{"row":55,"column":74},"action":"remove","lines":["Is that a Discover Card by any chance"],"id":50},{"start":{"row":55,"column":37},"end":{"row":55,"column":38},"action":"insert","lines":["Y"]},{"start":{"row":55,"column":38},"end":{"row":55,"column":39},"action":"insert","lines":["U"]}],[{"start":{"row":55,"column":38},"end":{"row":55,"column":39},"action":"remove","lines":["U"],"id":51}],[{"start":{"row":55,"column":38},"end":{"row":55,"column":39},"action":"insert","lines":["o"],"id":52},{"start":{"row":55,"column":39},"end":{"row":55,"column":40},"action":"insert","lines":["u"]}],[{"start":{"row":55,"column":39},"end":{"row":55,"column":40},"action":"remove","lines":["u"],"id":53},{"start":{"row":55,"column":38},"end":{"row":55,"column":39},"action":"remove","lines":["o"]},{"start":{"row":55,"column":37},"end":{"row":55,"column":38},"action":"remove","lines":["Y"]}],[{"start":{"row":55,"column":37},"end":{"row":55,"column":38},"action":"insert","lines":["Y"],"id":54},{"start":{"row":55,"column":38},"end":{"row":55,"column":39},"action":"insert","lines":["o"]},{"start":{"row":55,"column":39},"end":{"row":55,"column":40},"action":"insert","lines":["u"]},{"start":{"row":55,"column":40},"end":{"row":55,"column":41},"action":"insert","lines":["r"]}],[{"start":{"row":55,"column":41},"end":{"row":55,"column":42},"action":"insert","lines":[" "],"id":55}],[{"start":{"row":55,"column":41},"end":{"row":55,"column":42},"action":"remove","lines":[" "],"id":56},{"start":{"row":55,"column":40},"end":{"row":55,"column":41},"action":"remove","lines":["r"]},{"start":{"row":55,"column":39},"end":{"row":55,"column":40},"action":"remove","lines":["u"]},{"start":{"row":55,"column":38},"end":{"row":55,"column":39},"action":"remove","lines":["o"]},{"start":{"row":55,"column":37},"end":{"row":55,"column":38},"action":"remove","lines":["Y"]}],[{"start":{"row":55,"column":37},"end":{"row":55,"column":38},"action":"insert","lines":["H"],"id":57},{"start":{"row":55,"column":38},"end":{"row":55,"column":39},"action":"insert","lines":["o"]},{"start":{"row":55,"column":39},"end":{"row":55,"column":40},"action":"insert","lines":["w"]}],[{"start":{"row":55,"column":40},"end":{"row":55,"column":41},"action":"insert","lines":[" "],"id":58},{"start":{"row":55,"column":41},"end":{"row":55,"column":42},"action":"insert","lines":["m"]},{"start":{"row":55,"column":42},"end":{"row":55,"column":43},"action":"insert","lines":["a"]},{"start":{"row":55,"column":43},"end":{"row":55,"column":44},"action":"insert","lines":["n"]},{"start":{"row":55,"column":44},"end":{"row":55,"column":45},"action":"insert","lines":["y"]}],[{"start":{"row":55,"column":45},"end":{"row":55,"column":46},"action":"insert","lines":[" "],"id":59},{"start":{"row":55,"column":46},"end":{"row":55,"column":47},"action":"insert","lines":["l"]},{"start":{"row":55,"column":47},"end":{"row":55,"column":48},"action":"insert","lines":["i"]},{"start":{"row":55,"column":48},"end":{"row":55,"column":49},"action":"insert","lines":["n"]},{"start":{"row":55,"column":49},"end":{"row":55,"column":50},"action":"insert","lines":["e"]},{"start":{"row":55,"column":50},"end":{"row":55,"column":51},"action":"insert","lines":["s"]}],[{"start":{"row":55,"column":51},"end":{"row":55,"column":52},"action":"insert","lines":[" "],"id":60},{"start":{"row":55,"column":52},"end":{"row":55,"column":53},"action":"insert","lines":["h"]},{"start":{"row":55,"column":53},"end":{"row":55,"column":54},"action":"insert","lines":["a"]},{"start":{"row":55,"column":54},"end":{"row":55,"column":55},"action":"insert","lines":["v"]},{"start":{"row":55,"column":55},"end":{"row":55,"column":56},"action":"insert","lines":["e"]}],[{"start":{"row":55,"column":56},"end":{"row":55,"column":57},"action":"insert","lines":[" "],"id":61},{"start":{"row":55,"column":57},"end":{"row":55,"column":58},"action":"insert","lines":["y"]},{"start":{"row":55,"column":58},"end":{"row":55,"column":59},"action":"insert","lines":["o"]},{"start":{"row":55,"column":59},"end":{"row":55,"column":60},"action":"insert","lines":["u"]}],[{"start":{"row":55,"column":60},"end":{"row":55,"column":61},"action":"insert","lines":[" "],"id":62},{"start":{"row":55,"column":61},"end":{"row":55,"column":62},"action":"insert","lines":["c"]},{"start":{"row":55,"column":62},"end":{"row":55,"column":63},"action":"insert","lines":["u"]},{"start":{"row":55,"column":63},"end":{"row":55,"column":64},"action":"insert","lines":["t"]}],[{"start":{"row":55,"column":64},"end":{"row":55,"column":65},"action":"insert","lines":[" "],"id":63},{"start":{"row":55,"column":65},"end":{"row":55,"column":66},"action":"insert","lines":["w"]},{"start":{"row":55,"column":66},"end":{"row":55,"column":67},"action":"insert","lines":["i"]},{"start":{"row":55,"column":67},"end":{"row":55,"column":68},"action":"insert","lines":["t"]},{"start":{"row":55,"column":68},"end":{"row":55,"column":69},"action":"insert","lines":["h"]}],[{"start":{"row":55,"column":69},"end":{"row":55,"column":70},"action":"insert","lines":[" "],"id":64},{"start":{"row":55,"column":70},"end":{"row":55,"column":71},"action":"insert","lines":["t"]},{"start":{"row":55,"column":71},"end":{"row":55,"column":72},"action":"insert","lines":["h"]},{"start":{"row":55,"column":72},"end":{"row":55,"column":73},"action":"insert","lines":["a"]},{"start":{"row":55,"column":73},"end":{"row":55,"column":74},"action":"insert","lines":["t"]}],[{"start":{"row":55,"column":75},"end":{"row":55,"column":76},"action":"insert","lines":[" "],"id":65}],[{"start":{"row":55,"column":75},"end":{"row":55,"column":76},"action":"remove","lines":[" "],"id":66}],[{"start":{"row":55,"column":75},"end":{"row":55,"column":76},"action":"insert","lines":[" "],"id":67},{"start":{"row":55,"column":76},"end":{"row":55,"column":77},"action":"insert","lines":["Y"]},{"start":{"row":55,"column":77},"end":{"row":55,"column":78},"action":"insert","lines":["o"]},{"start":{"row":55,"column":78},"end":{"row":55,"column":79},"action":"insert","lines":["u"]},{"start":{"row":55,"column":79},"end":{"row":55,"column":80},"action":"insert","lines":["r"]}],[{"start":{"row":55,"column":80},"end":{"row":55,"column":81},"action":"insert","lines":[" "],"id":68},{"start":{"row":55,"column":81},"end":{"row":55,"column":82},"action":"insert","lines":["c"]},{"start":{"row":55,"column":82},"end":{"row":55,"column":83},"action":"insert","lines":["a"]},{"start":{"row":55,"column":83},"end":{"row":55,"column":84},"action":"insert","lines":["r"]},{"start":{"row":55,"column":84},"end":{"row":55,"column":85},"action":"insert","lines":["d"]}],[{"start":{"row":55,"column":85},"end":{"row":55,"column":86},"action":"insert","lines":[" "],"id":69},{"start":{"row":55,"column":86},"end":{"row":55,"column":87},"action":"insert","lines":["a"]},{"start":{"row":55,"column":87},"end":{"row":55,"column":88},"action":"insert","lines":["i"]},{"start":{"row":55,"column":88},"end":{"row":55,"column":89},"action":"insert","lines":["n"]},{"start":{"row":55,"column":89},"end":{"row":55,"column":90},"action":"insert","lines":["'"]},{"start":{"row":55,"column":90},"end":{"row":55,"column":91},"action":"insert","lines":["t"]}],[{"start":{"row":55,"column":91},"end":{"row":55,"column":92},"action":"insert","lines":[" "],"id":70},{"start":{"row":55,"column":92},"end":{"row":55,"column":93},"action":"insert","lines":["w"]},{"start":{"row":55,"column":93},"end":{"row":55,"column":94},"action":"insert","lines":["o"]},{"start":{"row":55,"column":94},"end":{"row":55,"column":95},"action":"insert","lines":["r"]},{"start":{"row":55,"column":95},"end":{"row":55,"column":96},"action":"insert","lines":["k"]},{"start":{"row":55,"column":96},"end":{"row":55,"column":97},"action":"insert","lines":["i"]},{"start":{"row":55,"column":97},"end":{"row":55,"column":98},"action":"insert","lines":["n"]},{"start":{"row":55,"column":98},"end":{"row":55,"column":99},"action":"insert","lines":["g"]}],[{"start":{"row":55,"column":98},"end":{"row":55,"column":99},"action":"remove","lines":["g"],"id":71}],[{"start":{"row":55,"column":98},"end":{"row":55,"column":99},"action":"insert","lines":["'"],"id":72}],[{"start":{"row":55,"column":99},"end":{"row":55,"column":100},"action":"insert","lines":[" "],"id":73},{"start":{"row":55,"column":100},"end":{"row":55,"column":101},"action":"insert","lines":["b"]},{"start":{"row":55,"column":101},"end":{"row":55,"column":102},"action":"insert","lines":["r"]},{"start":{"row":55,"column":102},"end":{"row":55,"column":103},"action":"insert","lines":["o"]}],[{"start":{"row":55,"column":102},"end":{"row":55,"column":103},"action":"remove","lines":["o"],"id":74}],[{"start":{"row":55,"column":102},"end":{"row":55,"column":103},"action":"insert","lines":["u"],"id":75}],[{"start":{"row":55,"column":103},"end":{"row":55,"column":104},"action":"insert","lines":["h"],"id":76}],[{"start":{"row":55,"column":103},"end":{"row":55,"column":104},"action":"remove","lines":["h"],"id":77}],[{"start":{"row":55,"column":103},"end":{"row":55,"column":104},"action":"insert","lines":["h"],"id":78}],[{"start":{"row":28,"column":59},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":79},{"start":{"row":29,"column":0},"end":{"row":29,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"insert","lines":["]"],"id":81},{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"insert","lines":["]"]}],[{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"remove","lines":["]"],"id":82},{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"remove","lines":["]"]},{"start":{"row":29,"column":12},"end":{"row":29,"column":16},"action":"remove","lines":["    "]},{"start":{"row":29,"column":8},"end":{"row":29,"column":12},"action":"remove","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":29,"column":8},"action":"remove","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "]},{"start":{"row":28,"column":59},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":398.5,"scrollleft":0,"selection":{"start":{"row":28,"column":59},"end":{"row":28,"column":59},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":23,"state":"start","mode":"ace/mode/python"}},"timestamp":1570910620908,"hash":"ec4e68477ef3346ac02b4fd9d06a3f1fd10fc476"}