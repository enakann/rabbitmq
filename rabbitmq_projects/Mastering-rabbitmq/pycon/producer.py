class Producer:
    def __init__(self,conn):
        self.conn=conn

    def send_message(self,msg,exch,rtg_key):
        chan=self.conn.channel()
        chan.basic_publish(exch,rtg_key,msg)
        chan.close()
