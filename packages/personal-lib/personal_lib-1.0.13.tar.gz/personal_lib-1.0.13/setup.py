from setuptools import setup

setup(name='personal_lib',
      version='1.0.13',
      description="personal library 1.0.13：\n 1. add ThreadSafeDB to db_utils.py \n 2. add params try_times to function get_trade_days which is in common_utils.py",
      long_description = "a personal library",
      packages=['personal_lib', 'personal_lib/utils'],
      package_data={'': ['*.txt']},
      install_requires=['pandas>=1.1.4', 'yagmail>=0.14.261', 'paramiko>=2.7.2', 'pymysql>=1.0.2','requests','dbutils'],
      python_requires='>=3.7',
      )
