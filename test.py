import json
from http.client import HTTPConnection, HTTPSConnection
from foxconn import interface


def case1(self):
        
        self.https.request("GET", "/#/login")
        req = self.https.getresponse()
        read = req.read().decode()
        bool = read.find("消防")
        res=bool>=0
        if res:
                print("Test Pass")
        else:
                print("Test Failed")
        self.assertEqual(res,True)
        #self.https.close()



def case2(self):
        
        maps = {'Content-Type': 'application/json'}
        data = {"name": "admin", "password": "HON123well", "platform": "0"}
        datasend = json.dumps(data)
        self.https.request("POST", "/central/user/login", headers=maps, body=datasend)
        req = self.https.getresponse()
        read = req.read().decode()
        req = json.loads(read)
        # print(req)
        bool = 0
        try:
            interface.token=req['result']['token']
            bool = True
            print("Test Pass")
        except TypeError:
            bool = False
            print("Test Failed")
        #self.https.close()
        self.assertEqual(bool,True)


def case3(self):

        maps = {'Content-Type': 'application/json','authorization':'Bearer '+interface.token}
        self.https.request("GET", "/topic?currentPage=1&pageSize=15&status=3", headers=maps)
        req = self.https.getresponse()
        read = req.read().decode()    
        #print(read)
        bool_check = read.find("8002")
        res=bool_check>=0
        if res:
                print("Test Pass")
        else:
                print("Test Failed")
        self.assertEqual(res,True)
        #self.https.close()
