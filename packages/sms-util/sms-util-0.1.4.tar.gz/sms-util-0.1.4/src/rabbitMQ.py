# coding:utf8
import sys
import pika
import pika.exceptions
from ConfParse import ConfParser

class rabbitMQ(object):
    def __init__(self,callback=None):
        conf = ConfParser()
        host = conf.get("rabbimq","host")
        self.port = conf.get("rabbimq", "port")
        username = conf.get("rabbimq", "username")
        password = conf.get("rabbimq", "password")
        self.user_pwd = pika.PlainCredentials(username, password)
        self.parameters = pika.ConnectionParameters(host=host, credentials=self.user_pwd, heartbeat=0)

        # 定义交换机，设置类型为direct
        # self.channel = self.s_conn.channel()
        self.callback = callback
    def __enter__(self):
        pass
    def send_msg(self,queue_name,body,exchange=''):
        try:
            self.s_conn = pika.BlockingConnection(self.parameters)  # 创建连接
            self.channel = self.s_conn.channel()
        except pika.exceptions.ConnectionClosed:
            self.s_conn = pika.BlockingConnection(self.parameters)
            self.channel = self.s_conn.channel()
        except :
            self.s_conn = pika.BlockingConnection(self.parameters)
            self.channel = self.s_conn.channel()
        if exchange:
            self.channel.exchange_declare(exchange=exchange, exchange_type='direct')
        self.channel.queue_declare(queue=queue_name)  # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
        self.channel.basic_publish(exchange=exchange,  # 交换机
                           routing_key=queue_name,  # 路由键，写明将消息发往哪个队列，本例是将消息发往队列hello
                           body=body)  # 生产者要发送的消息
        self.s_conn.close()
    def receive_msg(self,routings,exchange=''):
        try:
            self.s_conn = pika.BlockingConnection(self.parameters)  # 创建连接
            self.channel = self.s_conn.channel()
        except pika.exceptions.ConnectionClosed:
            self.s_conn = pika.BlockingConnection(self.parameters)
            self.channel = self.s_conn.channel()
        except Exception as e:
            self.s_conn = pika.BlockingConnection(self.parameters)
            channel = self.s_conn.channel()
        if exchange:
            self.channel.exchange_declare(exchange=exchange, exchange_type='direct')
        for routing in routings:
            self.channel.queue_declare(queue=routing)  # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
            self.channel.queue_bind(exchange=exchange,
                           queue=routing,
                           routing_key=routing)
            self.channel.basic_consume(self.__callback, queue=routing, no_ack=False)
        try:
            self.channel.start_consuming()
        except:
            print sys.exc_info()
        self.s_conn.close()

    def __callback(self,ch, method, properties, body):
        # print " [x] Received %r" % (body,)
        # print method.routing_key
        # print method.exchange
        try:
            if self.callback:
                self.callback(method.routing_key,body)
            #回复ack
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except:
            print sys.exc_info()


    def __exit__(self, exc_type, exc_val, exc_tb):
        print "exit rabbit mq"

