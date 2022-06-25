# pystripe

# PyStripe - Python library for Stripe payment API 
Python is a python library of functions to consume [Stripe](https://stripe.com/) APIs.

## Requirements :

### Python version:
```
Python 3 or higher
```

### Extensions required :
```
stripe
flask/url_for
```

## How to

Create a object passing the password for authentication.

Example :

```
from external.pyStripe import Stripe

myStripe = Stripe("my_password")

```

Set the list of products accordingly on what was set on Stripe website

Example :

```

Products = {'product10usd': {'name': '$10 product','price': 10,},'product10usd': {'name': '$20 product','price': 20,}}

```

Call the method GetChecjoutFormUrl passing the list and product ID used as parameter. It will return the url form for payment on stripe services, then use a redirect method to call the url.

Example :

```

checkout_url = myStripe.GetCheckoutFormUrl(Products, <product_id>)

return redirect(checkout_url)    


```

### Available methods

- GetCheckoutFormUrl : Get the URL for the payment form on stripe platform
