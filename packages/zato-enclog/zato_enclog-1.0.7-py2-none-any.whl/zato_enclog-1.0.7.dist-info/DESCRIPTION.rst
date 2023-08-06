
===========
zato-enclog
===========

* Encrypted logger which stores everything using Fernet keys (AES128). Safe to use in environments
  that cannot store Personally Identifiable Information (PII) in clear text, such as HIPAA-compliant applications.

* Comes with a command line tool that is used to decrypt logs, including both open and tail -f functionality.

* Learn more about Fernet: https://cryptography.io/en/latest/fernet/

::

  # stdlib
  import logging

  # Zato
  from zato.enclog import EncryptedLogFormatter, genkey

  level = logging.INFO
  format = '%(levelname)s - %(message)s'

  key = genkey()
  formatter = EncryptedLogFormatter(key, format)

  handler = logging.StreamHandler()
  handler.setFormatter(formatter)

  logger = logging.getLogger('')
  logger.addHandler(handler)
  logger.setLevel(level)

  logger.info(b'{"user":"Jane Xi"}')

  # Shows the following
  INFO - gAAAAABWYa17oiDoSMVjF8JM9DWzB3dtEvenW9laKqgsFl4d4ksbLCkoJzTyrI3nXKYVOcC03dhJ_BwfWlBN3CdGxJZAwMmfUbUzLHkqw2JeTzdgtz0YEGU=


