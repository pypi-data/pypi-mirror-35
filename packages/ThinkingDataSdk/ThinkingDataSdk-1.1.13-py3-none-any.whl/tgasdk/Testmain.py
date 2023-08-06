#encoding:utf-8
import datetime
import threading
import time

from tgasdk.sdk import TGAnalytics, BatchConsumer, LoggingConsumer, AsyncBatchConsumer

tga = TGAnalytics(BatchConsumer("server_uri","appid"))
# tga = TGAnalytics(AsyncBatchConsumer("http://test:44444/logagent","quanjie-python-sdk"))
tga = TGAnalytics(LoggingConsumer("F:/home/sdk/log"))


properties = {
    "#time":datetime.datetime.now() - datetime.timedelta(days=1),
    "custome":datetime.datetime.now(),
    # "#ip":"192.168.1.1",
    "Product_Name":"a",
    '#os':'windows',
    "today":datetime.date.today(),
    "nullkey":None,
    "#safwue8382f83":"#测试"

}
i = 1
tga.user_set('dis'+str(i),None)
tga.track('dis'+str(i),None,"shopping",properties.copy())



start = time.time()
print(start)
# for i in range(100000):
#     tga.track('dis'+str(i),None,"shopping",properties)
tga.close()
end = time.time()
print(end)
print("diff:",end - start)







