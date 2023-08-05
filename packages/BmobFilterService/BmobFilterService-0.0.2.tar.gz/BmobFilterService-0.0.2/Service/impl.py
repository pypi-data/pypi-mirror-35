import json
import logging

from requests import Session

from Service.service_interface import DBInterface


class Bmob(DBInterface):
    def __init__(self, table_name, application_id, rest_api_key):
        self.table_name = table_name
        self.application_id = application_id
        self.rest_api_key = rest_api_key
        self.headers = {
            "X-Bmob-Application-Id": self.application_id,
            "X-Bmob-REST-API-Key": self.rest_api_key,
            "Content-Type": "application/json"
        }
        self.s = Session()
        self.s.headers = self.headers
        self.logger = logging.getLogger(__name__)
        self.base_url = "https://api.bmob.cn/1/classes/{}".format(self.table_name)

    def insert(self, item):
        # item["images"] = json.dumps(item["images"])
        # item["tags"] = ','.join(item["tags"])
        try:
            post_data = {
                "title": item["title"],
                "type": "text",
                "content": "<h2>hello word</h2>",
                "url": item["url"],
                "version": "1"
            }
            resp = self.s.post(self.base_url, data=json.dumps(dict(post_data)))
            self.logger.info(resp.text)
        except Exception as e:
            self.logger.error("Bomb insert http error %s ", e, exc_info=True)

    def update(self, objectId):
        try:
            post_data = {
                "title": "quantity的游戏 更新测试",
                "type": "text",
                "content": "<h2>hello word</h2>",
                "show": True
            }
            resp = self.s.put("{}/{}".format(self.base_url, objectId), data=json.dumps(post_data))
            self.logger.info(resp.text)
        except Exception as e:
            self.logger.error("Bomb insert http error %s ", e, exc_info=True)

    def save(self, item):
        self.insert(item)
        pass

    def get_info_by_url(self, url):
        where = {"url": url}
        where = json.dumps(dict(where))
        payload = {'where': where}
        try:
            # post_data = {
            #     "title": "quantity的游戏 普罗米修斯",
            #     "type": "text",
            #     "content": "<h2>hello word</h2>",
            #     "show": True
            # }
            resp = self.s.get(self.base_url, params=payload)
            self.logger.info(resp.text)
            if len(resp.json()['results']) > 0:
                return resp.json()
        except Exception as e:
            self.logger.error("Bomb insert http error %s ", e, exc_info=True)

    def is_exist_url(self, url, title="def"):
        if self.get_info_by_url(url):
            return True
        else:
            item = {
                "title": title,
                "url": url
            }
            self.insert(item)
            return False

# bm = Bmob("CubeSpiderFilter", "eccd0a711b9b4a0bac2ce174abd9a29c", "0424ed5234ddc8a5461aaca091a94c92")
# bm.is_exist_url("testfgfgfg")
