import asyncio
import logging
from databot.botframe import BotFrame,call_wrap,BotControl
import collections
from databot.config import config
import  databot.queue  as queue


class RouteRule(object):
    __slots__ = ['output_q', 'type_list', 'share']

    def __init__(self, output_q, types_list, share):
        self.output_q = output_q
        self.type_list = types_list
        self.share = share

    def is_match(self, o):
        for t in self.type_list:
            if isinstance(o, t):
                return True

        return False

    def is_share(self):
        return self.share

    def __eq__(self, other):
        return False

    def __lt__(self, other):

        if self.share == False:
            return True
        else:
            return False


class RouteTable(object):
    __slots__ = ['rules']

    def __init__(self):
        self.rules = queue.PriorityQueue()

    def add_rules(self, r):
        self.rules.put(r)

    async def route(self, msg):
        matched_q = []
        for r in self.rules.queue:
            if r.is_match(msg):
                matched_q.append(r.output_q)

                # use wait api ,it maybe blocked(wait) in a q. then block other q speed
                await  r.output_q.put(msg)
                if not r.is_share():
                    break

    pass


class Route(object):

    def __init__(self, *args, route_type=object, share=True, join=False):

        self.in_table = RouteTable()
        self.out_table = RouteTable()
        self.args = args
        if isinstance(route_type, list):
            self.route_type = route_type
        else:
            self.route_type = [route_type]

        self.share = share
        self.joined = join
        self.start_q=None
        self.output_q=None


        if hasattr(self, 'route_type') and not isinstance(self.route_type, list):
            self.route_type = [self.route_type]

    async def start_q_put(self,data):


        is_signal= isinstance(data,BotControl)

        matched = self.type_match(data, self.route_type)


        if self.share == True or is_signal:
                await self.output_q.put(data)
        else:
                if not matched:
                    await self.output_q.put(data)
                else:
                    pass


        if matched or is_signal:
            for q in self.start_q:
                await q.put(data)
            # if isinstance(self.start_q,list):
            #     for q in self.start_q:
            #         await q.put(data)
            # else:
            #     await self.start_q.put(data)

    async def __call__(self, data):

        if isinstance(data,list):
            for d in data:
                await self.start_q_put(data)
        else:
            await self.start_q_put(data)

        return



    def make_route_bot(self, iq, oq):
        raise NotImplementedError()


    @classmethod
    def type_match(cls, msg, type_list):
        for t in type_list:
            if isinstance(msg, t):
                return True

        return False




# main pipe
class Pipe(Route):

    # |
    # |
    # |
    # |

    def __init__(self, *args):
        q_o = queue.GodQueue()

        # get this pip own inside bot
        self.start_index = len(BotFrame.bots)
        self.q_start = q_o
        self.joined = False

        for func in args:
            q_i = q_o
            if func == args[-1]:
                q_o = queue.NullQueue()

            else:
                if config.replay_mode:
                    q_o=queue.CachedQueue()
                else:
                    q_o = queue.DataQueue()

            bis=BotFrame.make_bot(q_i, q_o, func)
            for b in bis:
                b.flow='main'


            if isinstance(func, Route):
                if hasattr(func, 'joined') and func.joined:
                    self.joined = True

        self.end_index = len(BotFrame.bots)
        for i in range(self.start_index, self.end_index):
            BotFrame.bots[i].pipeline = str(self)
        self.q_end = q_o

        if self.joined or config.joined_network:
            self.check_joined_node()

    @classmethod
    def get_reader_id_by_q(cls,q):
        ids=[]
        for b in BotFrame.bots:
            if cls.included(q,b.iq):
                ids.append(b.id)

        return ids

    import sys
    pickle_name = sys.modules['__main__'].__file__ + 'palyback.pk'
    @classmethod
    def  save_for_replay(cls):
        '''it will save cached data for pay back'''

        #1. get output queue of the nearest closed node in main pipe
        #2.save the data
        max_id=-1
        bot=None
        for b in BotFrame.bots:
            if b.flow=='main' and b.stoped==True:
                if b.id > max_id:
                    bot=b
                    max_id=b.id
        if bot is None:
            pass

        obj={}
        obj['botid']=max_id

        to_dump=[]
        for q in bot.oq:
            #iid=get_writor_botid(q)
            iid=[max_id]
            oid=cls.get_reader_id_by_q(q)
            to_dump.append((iid,oid,q.cache))

        obj['data'] =to_dump

        import pickle
        with open(cls.pickle_name,'wb') as f:
            pickle.dump(obj,f)

    @classmethod
    def get_q_by_bot_id_list(cls, iid, oid):
        q_of_writer=set()
        q_of_reader=set()

        for i in iid:
            for q in BotFrame.get_botinfo_by_id(i).oq:
                q_of_writer.add(q)
        for i in oid:
            for q in BotFrame.get_botinfo_by_id(i).iq:
                q_of_reader.add(q)


        r=q_of_writer&q_of_reader
        return r.pop()

    @classmethod
    def restore_for_replay(cls):
        ''''''
        #1. load data to queue
        #2. set all pre-node to closed

        import os.path
        if not os.path.isfile(cls.pickle_name):
            return

        import pickle
        with open(cls.pickle_name,'rb') as f:
            obj=pickle.load(f)

        botid=obj['botid']
        for b in BotFrame.bots:
            if b.id<=botid:
                b.stoped=True
        for data in obj['data']:
            (iid,oid,cache)=data
            q=cls.get_q_by_bot_id_list(iid, oid)
            q.load_cache(cache)

        return





    @classmethod
    def included(self,iq,oq):
        if not isinstance(iq,list):
            iq=[iq]
        if not isinstance(oq,list):
            oq=[oq]

        for q in iq:
            for _oq in oq:
                if q is _oq:
                    return True
        return False
    def check_joined_node(self):
        for i in range(self.start_index, self.end_index):
            bot = BotFrame.bots[i]
            count = 0
            for j in range(self.start_index, self.end_index):

                for q in BotFrame.bots[j].oq:
                    if self.included(bot.iq, q):
                    #if bot.iq is q:
                        count += 1
                        bot.parents.append(BotFrame.bots[j])



    def finished(self):
        for i in range(self.start_index, self.end_index):
            fu = BotFrame.bots[i].futr
            if not fu.done() and not fu.cancelled():
                return False
        return True

    def __call__(self, list):
        pass

    def __repr__(self):
        return 'Pip_' + str(id(self))


# No read inpute
class Loop(Route):



    def make_route_bot(self, iq, oq):
        self.input = self.args[0]
        self.joined = True
        self.share=False
        self.start_q=[iq]
        self.output_q =oq


    async def __call__(self, data):
        if isinstance(data,BotControl):
            await self.output_q.put(data)
            return
        for i in self.input:
            await self.output_q.put(i)




#note drivedn by data
class Timer(Route):
    def __init__(self, delay=1, max_time=None, until=None):

        # \|/
        #  |
        #  |

        self.delay = delay
        self.max_time = max_time
        self.until = until

    def make_route_bot(self, iq, oq):
        self.start_q=[None]
        self.output_q=oq


    async def __call__(self, data):

        await self.output_q.put(data)








class Branch(Route):

    def is_last_one(self, list, item):
        if item == list[-1]:
            return True
        else:
            return False

    def make_route_bot(self, iq, oq):


        self.output_q = oq
        q_o = queue.DataQueue()
        self.start_q=[q_o]
        for func in self.args:
            q_i = q_o
            if self.is_last_one(self.args, func):
                if self.joined:
                    q_o = oq
                else:
                    q_o = queue.NullQueue()
            else:
                q_o = queue.DataQueue()



            BotFrame.make_bot(q_i, q_o, func)



class Return(Branch):


    def make_route_bot(self, iq, oq):
        self.share=False
        self.joined=True

        super().make_route_bot(iq,oq)


# 无法知道该类是被那里使用。更复杂实现是需要控制所有route初始化的顺序，需要外层初始化结束，建in,out队列传递到内侧
# make bot时候，对route只需要建立队列关系，而不需要，使用for循环来处理call
class Fork(Route):

    # |
    # | x
    # |/
    # |\
    # | x


    def make_route_bot(self, iq, oq):
        if self.joined:
            q_o = oq
        else:
            q_o = queue.NullQueue()

        self.start_q = []
        self.output_q = oq

        #parallel in sub network not in node
        for func in self.args:
            q_i = asyncio.Queue()
            self.start_q.append(q_i)
            BotFrame.make_bot(q_i, q_o, func)


class Join(Fork):
    def make_route_bot(self, iq, oq):
        self.share = False
        self.joined=True
        self.route_type=[object]

        super().make_route_bot(iq,oq)




#方案1，放入一个等待结构，超时后需要将任务杀死
#方案2 随机处理，在出口处，汇总合并数据，
class BlockedJoin(Route):

    # |
    # | x
    # |/
    # |\
    # | x


    def make_route_bot(self, iq,oq):

        self.start_q = []
        self.tmp_output_q=[]
        self.output_q=oq
        self.share = False
        self.joined=True
        self.route_type=[object]

        self.start_index = len(BotFrame.bots)
        for func in self.args:

            i_q = asyncio.Queue(maxsize=1)
            o_q = queue.DataQueue()
            self.start_q.append(i_q)
            self.tmp_output_q.append(o_q)
            BotFrame.make_bot(i_q, o_q, func)

        self.end_index = len(BotFrame.bots)


    def check(self):
        for i in range(self.start_index, self.end_index):
            bot = BotFrame.bots[i]
            if not bot.idle:
                return False
        for q in self.start_q:
            if not q.empty():
                return False
        return True

    async def compeleted(self):
        while True:
            s=self.check()

            if s:
                return True
            await asyncio.sleep(2)


    async def put_batch_q(self,data,qlist):

        tasks=[]
        for q in qlist:
            task=q.put(data)
            tasks.append(task)

        await asyncio.gather(*tasks)

    async def gut_batch_q(self, qlist):

        tasks = []
        for q in qlist:
            #TODO need get all extension
            task = q.get()
            tasks.append(task)

        r=await asyncio.gather(*tasks)
        return tuple(r)



    async def __call__(self, data):


            await self.put_batch_q(data,self.start_q)
            r=await self.gut_batch_q(self.tmp_output_q)
            await self.output_q.put(r)










###########short name ############

F = Fork
J = Join
P = Pipe
B = Branch
T = Timer
L = Loop



