#encoding:utf-8
import datetime
import threading
import time

from tgasdk.sdk import TGAnalytics, BatchConsumer, LoggingConsumer, AsyncBatchConsumer

# tga = TGAnalytics(AsyncBatchConsumer("server_uri","appid"))
# tga = TGAnalytics(AsyncBatchConsumer("http://test:44444/logagent_count_test","quanjie-python-sdk",max_batch_size=300,queue_size=10000))
tga = TGAnalytics(LoggingConsumer("F:/home/sdk/log",log_size=1))


properties = {
    #"#time":'2018-01-12 20:46:56',
    "custome":datetime.datetime.now(),
    "#ip":"192.168.1.1",
    "Product_Name":"a",
    '#os':'windows',
    "today":datetime.date.today(),
    "nullkey":None,
    "#safwue8382f83":"#测试"

}
for i in range(2):
    tga.track('dis'+str(i),None,"shopping",properties)


# super_properties = {
#     "server_version":"1.2.3",
#     "server_name":"A1001"
# }
# tga.set_super_properties(super_properties)
#
# distinct_id = "ABCDEF123456"
# account_id = "TA10001"
# properties = {
#     "Product_Name":"礼包",
#     "Price":60
# }
#
#
# # 上传事件，事件中将会带有公共事件属性以及该事件本身的属性
# tga.track(distinct_id,account_id,"Payment",properties)
#
# tga.clear_super_properties()
# tga.track(distinct_id,account_id,"Payment",properties)

tga.close()






