# coding=utf-8
import requests,json
class Api():

    def __init__(self):
        self.url = 'http://data.zhugefang.com/Borough/Api/getCityareaList?city=zz'

    def parse(self):
        response = requests.get(self.url)
        res = response.text
        res_dict = json.loads(res)
        self.res_data= res_dict['data']

    def parse_data_area1(self):
        list_1 = []
        city_area1 = {}
        temp = {}
        for data in self.res_data:

            temp[data['name']] = str(data['id'])
            # list_1.extend(temp)
        print(temp)

        # city_area1['zz_city_area1'] = list_1
    def parse_data_area2(self):
        temp2 = {}
        for data in self.res_data:
            res_data_1 = data['list_cityarea2']
            for k in res_data_1.keys():
                temp2[k] = str(res_data_1[k]['id'])

        print(temp2)
    def data_to(self):
        pass

    def run(self):
        self.parse()
        self.parse_data_area1()
        self.parse_data_area2()

if __name__ == '__main__':

    api = Api()
    api.run()
