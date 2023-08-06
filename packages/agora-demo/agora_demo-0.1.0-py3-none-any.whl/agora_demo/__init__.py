
from agora_demo.core.dataset_manager import DatasetManager
from agora_demo.core.configuration import ConfigurationManager
import os

config = ConfigurationManager()
dsm = [None]


def setup():
	"""Interact with the Configuration Manager"""
	config.bootstrap(config_filepath="configuration.ini")
	dsm[0] = DatasetManager(config)

def apply_transform(transform_function = None):
	"""Interact with the Dataset Manager. If transform function is not provided, then default transform function of removing one row is used."""
	def remove_first_row(df):
		if len(df.index) > 0:
			df = df.iloc[1:]
		return df
	if not transform_function:
		transform_function = remove_first_row
	dsm[0].transform_data(transform_function)
