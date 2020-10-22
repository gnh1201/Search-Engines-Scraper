from ..engine import SearchEngine
from ..config import PROXY, TIMEOUT, FAKE_USER_AGENT


class Naverblog(SearchEngine):
    '''Searches search.naver.com'''
    def __init__(self, proxy=PROXY, timeout=TIMEOUT):
        super(Naverblog, self).__init__(proxy, timeout)
        self._base_url = 'https://search.naver.com/search.naver'
        self.set_headers({'User-Agent':FAKE_USER_AGENT})
    
    def _selectors(self, element):
        '''Returns the appropriate CSS selector.'''
        selectors = {
            'url': 'a.sh_blog_title[href]',
            'title': 'a.sh_blog_title',
            'text': 'dd.sh_blog_passage',
            'links': '#elThumbnailResultArea > li',
            'next': 'a.next'
        }
        return selectors[element]
    
    def _first_page(self):
        '''Returns the initial page and query.'''
        url = u'{}?where=post&query={}'.format(self._base_url, self._query)
        return {'url':url, 'data':None}
    
    def _next_page(self, tags):
        '''Returns the next page URL and post data (if any)'''
        selector = self._selectors('next')
        next_page = self._get_tag_item(tags.select_one(selector), 'href')
        url = None
        if next_page:
            url = (self._base_url + next_page) 
        return {'url':url, 'data':None}
