import requests
import json

class RunMethod:
    # def __init__(self,method,url,data=None):
    #     self.res = self.run_main(method,url,data)

    def get_main(self, url):
        res = requests.get(url=url)
        return res.json()

    def post_main(self, url, data):
        res = requests.post(url=url, data=data)
        return res.json()

    def run_main(self, method,url, data=None, ):
        if method == 'post':
            res = self.post_main(url, data)
        else:
            res = self.get_main(url)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == '__main__':
    url = 'http://lemondream.chumanapp.com/api/recommend/get_home_page_zone_list'
    data = ''
    ru = RunMethod()
    print(ru.run_main('GET',url))
    # run = RunMethod('GET',url,data)
    # print(run.res)
