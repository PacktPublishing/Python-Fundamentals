class WebBrowser:
    connected = True

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False


chrome = WebBrowser('facebook.com')
firefox = WebBrowser('google.com')

print(chrome.__dict__)
print(firefox.__dict__)

# check class attribtes
print(chrome.connected)
print(firefox.connected)
# change attribute for instance only
WebBrowser.connected = False
print(chrome.__dict__)
print(firefox.__dict__)
print('firefox connected:', firefox.connected)
print('chrome connected:', chrome.connected)
# change attribute for all instances




