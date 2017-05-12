import logging
import random
from scrapy import signals
from scrapy.exceptions import NotConfigured

import tutorial.tor_controller as tor_controller

logger = logging.getLogger(__name__)

class TorRenewIdentity(object):

	def __init__(self, crawler, item_count):
		self.crawler = crawler
		self.item_count = self.randomize(item_count) 	# Randomize the item count to confound traffic analysis
		self._item_count = item_count 					# Also remember the given item count for future randomizations
		self.items_scraped = 0

		# Connect the extension object to signals
		self.crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)

	@staticmethod
	def randomize(item_count, min_factor=0.5, max_factor=1.5):
		'''Randomize the number of items scraped before changing identity. (A similar technique is applied to Scrapy's DOWNLOAD_DELAY setting).'''
		randomized_item_count = random.randint(int(min_factor*item_count), int(max_factor*item_count))
		logger.info("The crawler will scrape the following (randomized) number of items before changing identity (again): {}".format(randomized_item_count))
		return randomized_item_count

	@classmethod
	def from_crawler(cls, crawler):
		if not crawler.settings.getbool('TOR_RENEW_IDENTITY_ENABLED'):
			raise NotConfigured

		item_count = crawler.settings.getint('TOR_ITEMS_TO_SCRAPE_PER_IDENTITY', 50)

		return cls(crawler=crawler, item_count=item_count) 			# Instantiate the extension object

	def item_scraped(self, item, spider):
		'''When item_count items are scraped, pause the engine and change IP address.'''
		self.items_scraped += 1
		if self.items_scraped == self.item_count:
			logger.info("Scraped {item_count} items. Pausing engine while changing identity...".format(item_count=self.item_count))

			self.crawler.engine.pause()

			tor_controller.change_identity() 						# Change IP address (cf. https://stem.torproject.org/faq.html#how-do-i-request-a-new-identity-from-tor)
			self.items_scraped = 0 									# Reset the counter
			self.item_count = self.randomize(self._item_count)		# Generate a new random number of items to scrape before changing identity again
			
			self.crawler.engine.unpause()


