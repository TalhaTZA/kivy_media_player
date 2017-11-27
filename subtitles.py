from kivy.network.urlrequest import UrlRequest


class Subtitles:

    def __init__(self,url):
        self.subtitles=[]
        req=UrlRequest(url, on_success=self.got_subtitles)
        
    
    def got_subtitles(self,req,result):
        print('xhr called')
        self.subtitles=result['captions']
        
    
    def next(self, secs):
        for sub in self.subtitles:
            ms = secs*1000 - 0
            st = 'startTime'
            d = 'duration'
            if ms >= sub[st] and ms <= sub[st] + sub[d]:
                return sub
        return None 