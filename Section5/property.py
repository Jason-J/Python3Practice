#coding=-utf8
class Person(object):
    def __init__(self, name, sex= True):
        self.name = name
        self._sex = sex
    def _set_sex(self, sex):
        print("sss")
        if not isinstance(sex, bool):
            raise Exception("Invalid bool")

    def _get_sex(self):
        return self._sex
    sex = property(_get_sex, _set_sex)


class Color(object):
    def __init__(self, rbg_value, name):
        self.rbg_value = rbg_value
        self._name = name
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name
    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)

class Silly:
    @property
    def silly(self):
        print("you are get silly")
        return self._silly
    @silly.setter
    def silly(self, value):
        print("you are set silly {}".format(value))
        self._silly = value
    @silly.deleter
    def silly(self):
        print("you are delete silly")
        del self._silly


from urllib.request import  urlopen
import  time
class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        starTime = time.time()
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        print("use time total :{}".format(time.time() - starTime))
        return self._content


//新上传的代码