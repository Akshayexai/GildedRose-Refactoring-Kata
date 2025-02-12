# # -*- coding: utf-8 -*-
# import unittest

# from gilded_rose import Item, GildedRose


# class GildedRoseTest(unittest.TestCase):
#     def test_foo(self):
#         items = [Item("foo", 0, 0)]
#         gilded_rose = GildedRose(items)
#         gilded_rose.update_quality()
#         self.assertEqual("fixme", items[0].name)

        
# if __name__ == '__main__':
#     unittest.main()

# ===========================================================================================================


# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_regular_item(self):
        items = [Item("foo", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_conjured_item(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)  # Degrades by 2 instead of 1
        self.assertEqual(2, items[0].sell_in)

    def test_conjured_item_past_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)  # Degrades by 4 instead of 2
        self.assertEqual(-1, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
