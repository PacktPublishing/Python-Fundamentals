class WebBrowser:
    connected = True
    counter_web_browsers = 0

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
        WebBrowser.counter_web_browsers += 1


print(WebBrowser.counter_web_browsers)
chrome = WebBrowser('facebook.com')
firefox = WebBrowser('google.com')
print(WebBrowser.counter_web_browsers)
safari = WebBrowser('twitter.com')
print(WebBrowser.counter_web_browsers)