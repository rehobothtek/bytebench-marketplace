"""Add a small set of gadget catalogue starters without overwriting stock.

The names/specification categories are informed by current Nigerian retail
catalogues. Prices and quantities remain starter values: review both in admin
before treating an item as live inventory.
"""

from decimal import Decimal

from django.core.management.base import BaseCommand

from shop.models import Product


CATALOGUE = [
    {
        'name': 'Samsung Galaxy A17, 128GB', 'category': 'phone',
        'spec': '128GB · 6GB RAM · 5G', 'price': '252000', 'compare_at_price': '280000',
        'stock_quantity': 6, 'emoji': '📱', 'is_featured': True, 'is_bestseller': True,
    },
    {
        'name': 'Xiaomi Redmi 15C, 128GB', 'category': 'phone',
        'spec': '128GB · 4GB RAM · 6.9-inch display', 'price': '170000', 'compare_at_price': '200000',
        'stock_quantity': 8, 'emoji': '📱', 'is_featured': True, 'is_bestseller': True,
    },
    {
        'name': 'Infinix Smart 20, 64GB', 'category': 'phone',
        'spec': '64GB · 4GB RAM · 5,000mAh battery', 'price': '156000', 'compare_at_price': '170000',
        'stock_quantity': 10, 'emoji': '📱', 'is_featured': False, 'is_bestseller': True,
    },
    {
        'name': 'POCO C85, 256GB', 'category': 'phone',
        'spec': '256GB · 8GB RAM · 6.9-inch display', 'price': '206000', 'compare_at_price': '230000',
        'stock_quantity': 5, 'emoji': '📱', 'is_featured': True, 'is_bestseller': False,
    },
    {
        'name': 'Samsung Galaxy A26 5G, 256GB', 'category': 'phone',
        'spec': '256GB · 8GB RAM · 5G', 'price': '359000', 'compare_at_price': '400000',
        'stock_quantity': 4, 'emoji': '📱', 'is_featured': False, 'is_bestseller': False,
    },
    {
        'name': 'Dell Latitude 7490', 'category': 'laptop',
        'condition': 'uk', 'spec': 'Core i5 · 8GB RAM · 256GB SSD', 'price': '419000', 'compare_at_price': '465000',
        'stock_quantity': 3, 'emoji': '💻', 'is_featured': True, 'is_bestseller': True,
    },
    {
        'name': 'ASUS TUF Gaming F16', 'category': 'laptop',
        'spec': 'Core 7 · 16GB RAM · 1TB SSD · RTX 4050', 'price': '1546700', 'compare_at_price': '1864363',
        'stock_quantity': 2, 'emoji': '🎮', 'is_featured': False, 'is_bestseller': False,
    },
    {
        'name': 'Oraimo SpaceBuds Neo', 'category': 'accessory',
        'spec': 'True wireless · Spatial audio · Black', 'price': '13500', 'compare_at_price': '43200',
        'stock_quantity': 15, 'emoji': '🎧', 'is_featured': True, 'is_bestseller': True,
    },
    {
        'name': 'Oraimo MagPower 15', 'category': 'accessory',
        'spec': '10,000mAh · 15W magnetic wireless charging', 'price': '37900', 'compare_at_price': '42220',
        'stock_quantity': 9, 'emoji': '🔋', 'is_featured': False, 'is_bestseller': True,
    },
    {
        'name': 'Oraimo PowerCube 20 Chic', 'category': 'accessory',
        'spec': '20W GaN charger · USB-C cable included', 'price': '12900', 'compare_at_price': '14330',
        'stock_quantity': 16, 'emoji': '🔌', 'is_featured': False, 'is_bestseller': True,
    },
    {
        'name': 'Oraimo PowerTrans USB-C Hub', 'category': 'accessory',
        'spec': '7-in-1 hub · 4K HDMI · USB-C', 'price': '23900', 'compare_at_price': '26600',
        'stock_quantity': 7, 'emoji': '🧩', 'is_featured': False, 'is_bestseller': False,
    },
    {
        'name': 'Oraimo Watch 6N', 'category': 'accessory',
        'spec': '1.83-inch display · Smartwatch · Black', 'price': '13500', 'compare_at_price': '43200',
        'stock_quantity': 12, 'emoji': '⌚', 'is_featured': False, 'is_bestseller': True,
    },
    {
        'name': 'Soundcore R50i Wireless Earbuds', 'category': 'accessory',
        'spec': 'Water-resistant · Gaming mode · Black', 'price': '21800', 'compare_at_price': '25500',
        'stock_quantity': 10, 'emoji': '🎧', 'is_featured': False, 'is_bestseller': False,
    },
    {
        'name': 'Xiaomi 20,000mAh Power Bank', 'category': 'accessory',
        'spec': '22.5W fast charge · Integrated cable', 'price': '32400', 'compare_at_price': '36000',
        'stock_quantity': 10, 'emoji': '🔋', 'is_featured': False, 'is_bestseller': True,
    },
    {
        'name': 'Havit Dual-Fan Laptop Cooling Stand', 'category': 'accessory',
        'spec': 'Foldable · Ergonomic riser · Dual fan', 'price': '37000', 'compare_at_price': '40000',
        'stock_quantity': 5, 'emoji': '❄️', 'is_featured': False, 'is_bestseller': False,
    },
]


class Command(BaseCommand):
    help = 'Add current phone, laptop and accessory starter products without changing existing products.'

    def handle(self, *args, **options):
        added = 0
        for raw_product in CATALOGUE:
            product = raw_product.copy()
            product['price'] = Decimal(product['price'])
            product['compare_at_price'] = Decimal(product['compare_at_price'])
            product.setdefault('condition', 'new')
            _, created = Product.objects.get_or_create(name=product['name'], defaults=product)
            added += int(created)
        self.stdout.write(self.style.SUCCESS(f'Catalogue update complete: {added} product(s) added.'))
