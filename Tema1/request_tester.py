import threading, time, urllib.request, random

sites = [
    "https://dog.ceo/dog-api/",
    "https://thecatapi.com/docs.html",
    "https://http.cat/",
    "https://clearbit.com/docs",
    "https://randomfox.ca/floof/",
    "https://developers.google.com/earth-engine/",
    "http://apiv3.iucnredlist.org/api/v3/docs",
    "http://google.com/",
    "http://youtube.com/"
]

class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        start = time.perf_counter()
        urllib.request.urlopen("http://localhost:8080/location?url={}".format(random.choice(sites)))
        duration = time.perf_counter() - start
        print("[{}] Done in {} seconds.".format(self.name, duration))

paralel_requests = 5
series_requests = 10

for i in range(series_requests):
    threads = []

    for j in range(paralel_requests):
        threads.append(MyThread(str(j)))
        threads[-1].start()
    
    for j, thread in enumerate(threads):
        thread.join()
