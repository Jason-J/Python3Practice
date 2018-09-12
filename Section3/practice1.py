#coding=utf-8
class ContactList(list):
    def search(self, name):
        matching_contacts=[]
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts
class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class Supplier(Contact):
    def order(self,order):
        print ("if this were a real system we would send "
               "{}order to"
               "{}".format(order,self.name))

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

#多态
class AudioFile:
    '媒体播放器'
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print ("playing {} as mp3".format(self.filename))
class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print ("playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print ("playing {} as ogg".format(self.filename))


class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("invalid file format ")
        self.filename = filename
    def play(self):
        print ("playing {} as flac".format(self.filename))