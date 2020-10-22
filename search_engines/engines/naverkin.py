from ..engine import SearchEngine
from ..config import PROXY, TIMEOUT, FAKE_USER_AGENT


class Naverkin(SearchEngine):
    '''Searches kin.naver.com'''
    def __init__(self, proxy=PROXY, timeout=TIMEOUT):
        super(Naverkin, self).__init__(proxy, timeout)
        self._base_url = 'https://kin.naver.com'
        self.set_headers({'User-Agent':FAKE_USER_AGENT})

    def _selectors(self, element):
        '''Returns the appropriate CSS selector.'''
        selectors = {
            'url': 'a[href]',
            'title': 'a',
            'text': 'dd:nth-child(3)',
            'links': 'ul.basic1 > li',
            'next': '.s_paging a:last-child'
        }
        return selectors[element]
    
    def _first_page(self):
        '''Returns the initial page and query.'''
        url = u'{}/search/list.nhn?sort=date&query={}&section=kin'.format(self._base_url, self._query)
        return {'url':url, 'data':None}
    
    def _next_page(self, tags):
        '''Returns the next page URL and post data (if any)'''
        selector = self._selectors('next')
        next_page = self._get_tag_item(tags.select_one(selector), 'href')
        url = None
        if next_page:
            url = (self._base_url + next_page) 
        return {'url':url, 'data':None}
