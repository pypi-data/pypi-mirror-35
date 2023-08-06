import json
import datetime
import random
from django.utils import timezone
from logging import Handler


class DBHandler(Handler, object):
    """
    This handler will add logs to a database model defined in settings.py
    If log message (pre-format) is a json string, it will try to apply the array onto the log event object
    """

    model_name = None
    expiry = None

    def __init__(self, model="", expiry=0):
        super(DBHandler, self).__init__()
        self.model_name = model
        self.expiry = int(expiry)

    def emit(self, record):
        # big try block here to exit silently if exception occurred
        try:
            # instantiate the model
            model = self.get_model(self.model_name)

            log_entry = model(level=record.levelname, message=self.format(record))

            # test if msg is json and apply to log record object
            try:
                data = json.loads(record.msg)
                for key, value in data.items():
                    if hasattr(log_entry, key):
                        try:
                            setattr(log_entry, key, value)
                        except:
                            pass
            except:
                pass

            log_entry.save()

            # in 20% of time, check and delete expired logs
            if self.expiry and random.randint(1, 5) == 1:
                model.objects.filter(time__lt=timezone.now() - datetime.timedelta(seconds=self.expiry)).delete()
        except:
            pass

    def get_model(self, name):
        names = name.split('.')
        mod = __import__('.'.join(names[:-1]), fromlist=names[-1:])
        return getattr(mod, names[-1])
