from django.conf import settings
import importlib

class DRFSettings(object):

    def __init__(self):
        self.drf_settings = {
            "HIDE_DOCS": self.get_setting("HIDE_DOCS") or False,
            "APP_NAME": self.get_setting("APP_NAME") or settings.ROOT_URLCONF.split(".")[0],
        }
        # 获取用户settings中的ERROR_CODE
        error_code = self.get_setting("ERROR_CODE") or False
        if error_code:
            ins = importlib.import_module(error_code)
            # 获取翻译
            translate = getattr(ins, "translate", None)
            self.drf_settings['translate'] = translate

    def get_setting(self, name):
        try:
            return settings.DRF_DOCS[name]
        except:
            return None

    @property
    def settings(self):
        return self.drf_settings
