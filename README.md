Prerequisites

    Python installed on your system.
    Google Chrome browser installed.

Instructions

    Clone or download the repository to your local machine.
    Ensure Python is installed on your system.
    Modify the name list in the script to include the URLs you want to open.
    Run the script by executing python open_links.py in your terminal or command prompt.

Code Explanation

    import webbrowser: Importing the webbrowser module to interact with the web browser.
    name: List containing URLs to be opened.
    chrome(text): Function definition to open URLs in Google Chrome.
    chrome_path: Path to the Google Chrome executable.
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path)): Registering Google Chrome as the default browser.
    webbrowser.get('chrome').open(text): Opening the URLs in Google Chrome.
    Looping through each URL in the name list and opening them in Google Chrome using the chrome() function.

Note

    Ensure Google Chrome is installed in the specified path or update the chrome_path variable accordingly.
    Make sure the URLs in the name list are correctly formatted.
    Customize the script to include additional URLs or modify it to suit your specific requirements.

