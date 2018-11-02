class Consumer:
    def __init__(self,conn):
        self.conn=conn
    def get_message(self,queue):
        chan=self.conn.channel()
        frame,_,body=chan.basic_get(queue)
        if frame:
            chan.basic_ack(frame.delivery_tag)
        return body
