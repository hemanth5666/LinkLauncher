import webbrowser
name=["https://www.linkedin.com/feed/?midToken=AQELmdRZG4KjSg&midSig=0uD66pm3AQOaE1&trk=eml-jobs_jymbii_digest-header-0-home_glimmer&trkEmail=eml-jobs_jymbii_digest-header-0-home_glimmer-null-fyb1ye~lexy8ozw~ju-null-null&eid=fyb1ye-lexy8ozw-ju",
      "https://www.hackerrank.com/hemanth2004?hr_r=1",
      "https://leetcode.com/accounts/login/",
      "https://github.com/hemanth5666"]

def chrome(text):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(text)
  
for i in name:
    chrome(i)
