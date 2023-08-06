import time
import traceback
from multiprocessing.managers import BaseManager
from multiprocessing.managers import BaseProxy
from .common.protocol import DEFAULT_SIMPLE_AGENT_NAME
from .common.protocol import DEFAULT_UNIQUE_KEY_AGENT_NAME
from loguru import logger

class RegisterManager:

	def __init__(self, host, port, authkey):
		logger.debug(f'client factory init host={host}, port={port}')
		BaseManager.register(DEFAULT_SIMPLE_AGENT_NAME)
		BaseManager.register(DEFAULT_UNIQUE_KEY_AGENT_NAME)
		self._address = (host, port)
		self._auth_key = authkey
		self._m = BaseManager(address=self._address, authkey=self._auth_key)
		self.rebind()

	def get_simple_topic(self):
		return self._simple_topic

	def get_unique_key_topic(self):
		return self._unique_key_topic

	def rebind(self):
		# 由于reconnect的时候也会用到，所以单独抽出来了
		self._m.connect()
		self._unique_key_topic = getattr(self._m, DEFAULT_UNIQUE_KEY_AGENT_NAME)()
		self._simple_topic = getattr(self._m, DEFAULT_SIMPLE_AGENT_NAME)()

	def reconnect(self, max_retry_times=10):
		for times in range(max_retry_times):
			try:
				if self._address in BaseProxy._address_to_local:
					if getattr(BaseProxy._address_to_local[self._address][0], 'connection', False):
						del BaseProxy._address_to_local[self._address][0].connection
						logger.warning('Delete connection success')
					self.rebind()
					logger.warning(f'RegisterManager reconnect success, times = {times}')
					return True
			except Exception as e:
				retry_after = 1 * times
				logger.error(f'reconnect error: {e}, times = {times}, retry after {retry_after} seconds')
				time.sleep(retry_after)
		return False