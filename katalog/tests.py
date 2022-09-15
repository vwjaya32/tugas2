from django.test import TestCase
from katalog.models import CatalogItem

# Create your tests here.
class testing(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name="FantechTHORX16",
                                   item_price=149000,
                                   item_stock=100,
                                   description="Mouse Pilihan No.1 di Asia tenggara dan JEPANG",
                                   rating=9,
                                   item_url="https://www.tokopedia.com/fantechstore/fantech-thor-ii-x16-mouse-gaming-pixart",)
        
    # Unit testing
    def test_object(self):
        fantech = CatalogItem.objects.get(item_name="FantechTHORX16",
                                          item_price=149000,
                                          item_stock=100,
                                          description="Mouse Pilihan No.1 di Asia tenggara dan JEPANG",
                                          rating=9,
                                          item_url="https://www.tokopedia.com/fantechstore/fantech-thor-ii-x16-mouse-gaming-pixart",)
        
        # Functional Testing
        self.assertEqual(fantech.item_name, "FantechTHORX16")
        self.assertEqual(fantech.item_price, 149000)
        self.assertEqual(fantech.item_stock, 100)
        self.assertEqual(fantech.description, "Mouse Pilihan No.1 di Asia tenggara dan JEPANG")
        self.assertEqual(fantech.rating, 9)
        self.assertEqual(fantech.item_url, "https://www.tokopedia.com/fantechstore/fantech-thor-ii-x16-mouse-gaming-pixart")

# Acknowledgement, Ide dari Risa Lestari - 2106655274
        

        
