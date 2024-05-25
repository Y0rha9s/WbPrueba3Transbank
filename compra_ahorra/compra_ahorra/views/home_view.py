from django.shortcuts import render
import requests

def cart(request):

    control = { 'image' : 'img/tecnologia/ps5 normal.jpg',
                'product': 'Ps5 con disco + 1 dual sense',
                'description': '',
                'price' : 590000,
                'quantity': 1
                }
    gabinete = {'image' : 'img/rtx4090.jpg',
                'product': 'RTX 4090',
                'description': 'Zotac 24GB vram',    
                'price' : 962190,
                'quantity': 1
                }
    notebook = {'image' : 'img/mouse logitwch.webp',
                'product': 'Mouse optico logitech',
                'description': 'G502 hero',    
                'price' : 35140,
                'quantity': 1
                }

    products = [control, gabinete, notebook]
    total = control.get('price') + gabinete.get('price') + notebook.get('price')

    return render(request, 'home2.html', {'products' : products, 'total': total})  