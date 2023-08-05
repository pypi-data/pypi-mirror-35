import json
from requests_html import HTMLSession


class FSHARE:
    """
    Get Fshare.vn link.
    If you have VIP account, you will receive premium download link.
    """
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password
        self.session = HTMLSession()
        self.URL_LOGIN = 'https://www.fshare.vn/site/login'
        self.error = {'error': ''}

    def get_token(self, res):
        """
        Get token of page
        :param res: Page html
        :return: Page token
        """
        token = res.xpath('//*[@name="_csrf-app"]')[0].attrs['value']
        return token

    def login(self):
        """
        Login to Fshare.vn
        :return: True if success, otherwise False
        """
        req = self.session.get(self.URL_LOGIN)
        token = self.get_token(req.html)
        data = {
            '_csrf-app': token,
            'LoginForm[email]': self.email,
            'LoginForm[password]': self.password,
            'LoginForm[rememberMe]': 1
        }
        login = self.session.post(url=self.URL_LOGIN, data=data)
        if login.url == self.URL_LOGIN:
            raise Exception("Login Failed!")
        else:
            pass

    def logout(self):
        """
        Log out
        :return: None
        """
        self.session.get(url='https://www.fshare.vn/site/logout')

    def is_exist(self, status_code):
        """
        Check if file is exist
        :param status_code: Page status code
        :return: True if exist, otherwise False
        """
        if status_code == 200:
            return True
        return False

    def get_link(self, url, password=None):
        """
        Get the download link
        :param url: URL need to download
        :param password: file password
        :return: download link if success, otherwise error message
        """
        req = self.session.get(url=url)
        if self.is_exist(req.status_code):
            url_title = req.html.xpath('//title/text()')[0]
            if url_title == 'Password required - Fshare':
                token = self.get_token(req.html)
                data = {
                    '_csrf-app': token,
                    'DownloadPasswordForm[password]': password
                }
                req = self.session.post(url=url,
                                        data=data)
            dl_token = self.get_token(req.html)
            linkcode = url.split("/")[-1]
            dl_data = {
                '_csrf-app': dl_token,
                'fcode5': '',
                'linkcode': linkcode,
                'withFcode5': 0,
            }
            req = self.session.post('https://www.fshare.vn/download/get',
                                    data=dl_data)
            try:
                link = req.json()
                if 'errors' in link:
                    return link['errors']
                return link['url']
            except json.decoder.JSONDecodeError:
                raise Exception('Get link failed')
        else:
            self.error['error'] = 'File not found'
            return self.error
