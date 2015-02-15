# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class StandardItem(unittest.TestCase):

    def test_sellin_drops_by_one_when_sellin_above_0(self):
        items = [Item("+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    def test_quality_drops_by_one_when_sellin_above_0(self):
        items = [Item("+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].quality)

    def test_quality_drops_by_two_when_sellin_below_0(self):
        items = [Item("+5 Dexterity Vest", sell_in=-10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(18, items[0].quality)

    def test_quality_doesnt_decrease_if_zero(self):
        items = [Item("+5 Dexterity Vest", sell_in=10, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)


class AgedBrie(unittest.TestCase):

    def test_sellin_drops_by_one_when_sellin_above_0(self):
        items = [Item("Aged Brie", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    def test_quality_increases_by_one_when_sellin_above_0(self):
        items = [Item("Aged Brie", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)

    def test_quality_increases_by_two_when_sellin_below_0(self):
        items = [Item("Aged Brie", sell_in=-10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(22, items[0].quality)

    def test_quality_doesnt_increase_if_fifty(self):
        items = [Item("Aged Brie", sell_in=10, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)


class Sulfuras(unittest.TestCase):

    def test_sellin_doesnt_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(10, items[0].sell_in)

    def test_quality_doesnt_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(20, items[0].quality)


class BackstagePasses(unittest.TestCase):

    def test_sellin_drops_by_one_when_sellin_above_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",
                      sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    def test_quality_increases_by_one_when_sellin_above_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",
                      sell_in=11, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)

    def test_quality_increases_by_two_when_sellin_between_5_and_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",
                      sell_in=10, quality=20),
                 Item("Backstage passes to a TAFKAL80ETC concert",
                      sell_in=6, quality=20),
                 ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(22, items[0].quality)
        self.assertEquals(22, items[1].quality)

    def test_quality_increases_by_three_when_sellin_between_0_and_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",
                      sell_in=5, quality=20),
                 Item("Backstage passes to a TAFKAL80ETC concert",
                      sell_in=1, quality=20),
                 ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(23, items[0].quality)
        self.assertEquals(23, items[1].quality)

    def test_quality_drops_to_0_after_sellin(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",
                      sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_quality_doesnt_increase_if_fifty(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",
                      sell_in=10, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)


if __name__ == '__main__':
    unittest.main()
