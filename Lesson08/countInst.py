class WebBrowser:
    connected = True
    num_web_browsers = 0

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
        WebBrowser.num_web_browsers += 1


print(WebBrowser.num_web_browsers)
chrome = WebBrowser('facebook.com')
firefox = WebBrowser('google.com')
print(WebBrowser.num_web_browsers)

