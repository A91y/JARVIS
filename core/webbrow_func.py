import webbrowser


# Registering chrome as Default browser
webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser(
                        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                    )

if __name__ == "__main__":

    # a = webbrowser.get()
    # print(a.__dir__())
    '''
    name: Text, 
    klass: Optional[Callable[[], BaseBrowser]], 
    instance: BaseBrowser=...,
    preferred: bool=...
    '''
    # webbrowser.open('google.com')
    # webbrowser.get('chrome').open('google.com')
