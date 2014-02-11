"""
    Copyright (c) 2013 Joshua Machol
    MIT, see LICENSE for more details.
"""

import unittest
from scrapedota import scrape_heroes

class TestScrape(unittest.TestCase):

    def setUp(self):
        pass

    def test_scrape_hero(self):
        heroes = scrape_heroes(3)
        for h in heroes:
            self.assertTrue(h.img_url and h.img_url != '')
            self.assertTrue(h.portrait_img_url and h.portrait_img_url != '')
            self.assertTrue(h.name and h.name != '')
            self.assertTrue(h.lore and h.lore != '')
            self.assertTrue(h.atk_type and h.atk_type != '')
            self.assertTrue(h.primary_attribute and h.primary_attribute != '')
            self.assertTrue(h.roles and h.roles != '')
            self.assertTrue(h.int and h.int != '')
            self.assertTrue(h.agi and h.agi != '')
            self.assertTrue(h.str and h.str != '')
            self.assertTrue(h.dmg and h.dmg != '')
            self.assertTrue(h.move_spd and h.move_spd != '')
            self.assertTrue(h.armor and h.armor != '')
            self.assertTrue(h.sight_range and h.sight_range != '')
            self.assertTrue(h.atk_range and h.atk_range != '')
            self.assertTrue(h.missile_spd and h.missile_spd != '')
            for a in h.abilities:
                self.assertTrue(a.img_url and a.img_url != '')
                self.assertTrue(a.name and a.name != '')
                self.assertTrue(a.description and a.description != '')
                for d in a.details:
                    self.assertTrue(d.name and d.name != '')
                    self.assertTrue(d.detail and d.detail != '')


if __name__ == '__main__':
    unittest.main()