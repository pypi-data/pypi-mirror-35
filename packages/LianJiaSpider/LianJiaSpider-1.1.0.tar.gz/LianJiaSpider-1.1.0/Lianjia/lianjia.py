import execjs
import requests
import time
import set
import tqdm
import json
import sqlite3
import numpy
import math


class Lianjia():
    def __init__(self, city):
        self.city_id = set.city[city]['city_id']
        self.city=city
    def GetAuthorization(self, dict):

        jsstr = set.js
        ctx = execjs.compile(jsstr)
        authorization = ctx.call('getMd5', dict)
        return authorization

    def GetDistrictInfo(self,max_lat, min_lat, max_lng, min_lng):
        """
        :str max_lat:
        最大经度 六位小数str型max_lat='40.074766'

        :str min_lat:
        最小经度 六位小数str型min_lat='39.609408'

        :str max_lng:
        最大纬度 六位小数str型max_lng='40.074766'

        :str min_lng:
        最小纬度 六位小数str型min_lng='39.609408'

        :str city_id:
        北京:110000  上海:310000

        #获取上海的各个区域，例如浦东，长宁，徐汇

        :return: list

        [{'id': 310115, 'name': '浦东', 'longitude': 121.60653130552, 'latitude': 31.208001618509, 'border': '121.54148868942,31.347913060234', 'unit_price': 58193, 'count': 18866},
        {'id': 310112, 'name': '闵行', 'longitude': 121.40817118429, 'latitude': 31.091185835136, 'border': '121.34040533465,31.037672798655;121.34022400061,31.022622576909;121.33932297393,31.020472421859;121.35006370183,31.020640362869', 'unit_price': 51866, 'count': 9024},
        {'id': 310113, 'name': '宝山', 'longitude': 121.42883034102, 'latitude': 31.369477510376, 'border': '121.37795619808,','unit_price': 18486, 'count': 76}]
        .........

        """

        time_13 = int(round(time.time() * 1000))
        authorization = Lianjia(self.city).GetAuthorization(
            {'group_type': 'district', 'city_id': self.city_id, 'max_lat': max_lat, 'min_lat': min_lat,
             'max_lng': max_lng, 'min_lng': min_lng, 'request_ts': time_13})

        url = set.url % (
            self.city_id, 'district', max_lat, min_lat, max_lng, min_lng, '%7B%7D', time_13, authorization, time_13)
        print(url)
        with requests.Session() as sess:
            ret = sess.get(url=url, headers=set.headers, cookies=set.cookies)
            print(ret.text)

            house_json = json.loads(ret.text[43:-1])

            if house_json['errno'] == 0:

                return house_json['data']['list'].values()

            else:
                return None

    def GetCommunityInfo(self,max_lat, min_lat, max_lng, min_lng):

        """
        :str max_lat:
        最大经度 六位小数str型max_lat='40.074766'

        :str min_lat:
        最小经度 六位小数str型min_lat='39.609408'

        :str max_lng:
        最大纬度 六位小数str型max_lng='40.074766'

        :str min_lng:
        最小纬度 六位小数str型min_lng='39.609408'

        :str city_id:
        北京:110000  上海:310000


        #获取区域内在售小区的信息#例如上海市的陈湾小区ID地理位置平均价格在售套数

        :return: list

        [{'id': '5011000012693', 'name': '陈湾小区', 'longitude': 121.455211, 'latitude': 30.966981, 'unit_price': 24407, 'count': 9}]


        """

        time_13 = int(round(time.time() * 1000))
        authorization = Lianjia(city).GetAuthorization(
            {'group_type': 'community', 'city_id': self.city_id, 'max_lat': max_lat, 'min_lat': min_lat,
             'max_lng': max_lng, 'min_lng': min_lng, 'request_ts': time_13})

        url = set.url % (
            self.city_id, 'community', max_lat, min_lat, max_lng, min_lng, '%7B%7D', time_13, authorization, time_13)

        with requests.Session() as sess:
            ret = sess.get(url=url, headers=set.headers, cookies=set.cookies)
            house_json = json.loads(ret.text[43:-1])

            if house_json['errno'] == 0:
                data_list = []
                if type(house_json['data']['list']) is dict:
                    for x in house_json['data']['list']:
                        data_list.append(house_json['data']['list'][x])
                    return data_list
                else:
                    return house_json['data']['list']

            else:
                return None

    def GetHousingInfo(self,id, count):

        ll = []
        for page in range(1, math.ceil(count / 10) + 1):
            time_13 = int(round(time.time() * 1000))
            jsstr = set.js
            ctx = execjs.compile(jsstr)
            authorization = ctx.call('getMd5',
                                     {'filters': "{}", 'id': id, 'order': 0, 'page': page, 'request_ts': time_13})
            ###############-----拼接请求url-----#################
            url = set.url_fang % (id, page, '%7B%7D', time_13, authorization, time_13)

            with requests.Session() as sess:
                ret = sess.get(url=url, headers=set.headers, cookies=set.cookies)
                house_json = json.loads(ret.text[42:-1])

                for x in house_json['data']['ershoufang_info']['list']:
                    ll.append(house_json['data']['ershoufang_info']['list'][x])

        return ll





def SaveCityBorderIntoDB(city):  # 读取某市各个区域轮廓
    ret = Lianjia(city).GetDistrictInfo(max_lat=set.city[city]['max_lat'], min_lat=set.city[city]['min_lat'],
                          max_lng=set.city[city]['max_lng'], min_lng=set.city[city]['min_lng'],)
    conn = sqlite3.connect('district.db')  # 链接数据库
    cursor = conn.cursor()
    try:
        sql = '''create table %s (
                    id int PRIMARY KEY ,
                    name text,
                    longitude text,
                    latitude text,
                    border text,
                    unit_price int,
                    count int
                    )''' % city
        cursor.execute(sql)
    except:
        print('数据表已存在')

    pbar = tqdm.tqdm(ret)
    for x in pbar:
        sql = ''' 
            insert into %s
            (id, name, longitude,latitude,border,unit_price,count)
            values
            (:id, :name, :longitude, :latitude, :border, :unit_price, :count)
            ''' % city
        try:
            cursor.execute(sql, x)
            conn.commit()
            pbar.set_description(x['name'] + '已导入')
        except:
            pbar.set_description(x['name'] + '已存在')

    cursor.close()
    # for x in numpy.arange(121.118774, 121.944122, 0.1):
    #     for y in numpy.arange(30.820294, 31.487821, 0.1):
    #         print((round(y,6), round(y - 0.1,6), round(x,6), round(x - 0.1,6)))
    #         print(requlianjia(round(y,6), round(y - 0.1,6), round(x,6), round(x - 0.1,6)))




def HoleCityDown(city):  # 爬取小区套数平均价格
    with sqlite3.connect('district.db') as conn:
        c = conn.cursor()
        c.execute('SELECT border,name FROM %s' % city)
        area_list = c.fetchall()
    lat = []
    lng = []
    conn = sqlite3.connect('LianJia_area.db')
    cursor = conn.cursor()
    try:
        sql = '''create table %s (
                        id int PRIMARY KEY ,
                        district text,
                        name text,
                        longitude text,
                        latitude text,
                        unit_price int,
                        count int
                        )
            ''' % city
        cursor.execute(sql)
    except:
        pass
    for x in area_list:
        district = x[1]
        for y in x[0].split(';'):
            lng.append(float(y.split(',')[0]))
            lat.append(float(y.split(',')[1]))
        li = []
        step = 0.02
        for x in numpy.arange(min(lng), max(lng), step):
            for y in numpy.arange(min(lat), max(lat), step):
                li.append((round(y, 6), round(y - step, 6), round(x, 6), round(x - step, 6)))
        pbar = tqdm.tqdm(li)
        for x in pbar:

            ret = Lianjia(city).GetCommunityInfo(x[0], x[1], x[2], x[3])

            if ret is not None:
                for z in ret:
                    try:
                        sql = ''' insert into %s
                                 (id, name, district,longitude,latitude,unit_price,count)
                                 values
                                 (:id, :name, :district,:longitude, :latitude, :unit_price, :count)
                                 ''' % city
                        z.update({'district': district})
                        cursor.execute(sql, z)
                        conn.commit()

                        pbar.set_description(district + z['name'] + '已导入')
                    except:

                        pbar.set_description(district + z['name'] + '住房已存在')


def GetCompleteHousingInfo(city):
    # 爬取所有小区内每个住房信息
    with sqlite3.connect('DetailInfo.db') as conn1:
        cursor1 = conn1.cursor()
        try:
            sql = set.sql_CreateDetailInfo % city
            cursor1.execute(sql)



        except:
            pass

    with sqlite3.connect('LianJia_area.db') as conn:
        c = conn.cursor()
        c.execute('SELECT id,count FROM %s' % city)
        area_list = c.fetchall()
    pbar = tqdm.tqdm(area_list)
    for x in pbar:
        ret = Lianjia(city).GetHousingInfo(x[0], x[1])
        with sqlite3.connect('DetailInfo.db') as conn:
            cursor = conn.cursor()
            for y in ret:
                try:
                    sql = set.sql_InsertDetailInfo % city
                    y['house_video_info'] = str(y['house_video_info'])
                    y['tags'] = str(y['tags'])
                    cursor.execute(sql, y)
                    conn.commit()
                    pbar.set_description(y['title'] + '已导入')
                except:
                    pbar.set_description(y['title'] + '已存在')


if __name__ == '__main__':
    city = '厦门'
    #SaveCityBorderIntoDB(city)  # 下载城市区域数据
    #HoleCityDown(city)  # 下载区域住房数据
    GetCompleteHousingInfo(city)#获取详细在售房屋
