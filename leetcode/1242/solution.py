# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import threading
import queue

class Solution:

    
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        q = queue.Queue()
        visited = {startUrl}
        visitedLock = threading.Lock()
        q.put(startUrl)
        threads = []
        startHostname = startUrl.split("/")[2]
        num_workers = 6

        for i in range(num_workers):
            thread = threading.Thread(target = self.getNextUrlsAndAppendToQueue, args = (visited,visitedLock,q,htmlParser,startHostname, ))
            thread.start()
            threads.append(thread)

        q.join()

        for i in range(num_workers): 
            q.put(None)
        for thread in threads:
            thread.join()
        return list(visited)


    def getNextUrlsAndAppendToQueue(self, visited, visitedLock, q, htmlParser, startHostname):
        while True:
            url = q.get()
            if url is None:
                return
        
            nextUrls = htmlParser.getUrls(url)

            for next_url in nextUrls:
                if next_url.split("/")[2] == startHostname:
                    with visitedLock:
                        if next_url not in visited:
                            q.put(next_url)
                            visited.add(next_url)
            q.task_done()
        
