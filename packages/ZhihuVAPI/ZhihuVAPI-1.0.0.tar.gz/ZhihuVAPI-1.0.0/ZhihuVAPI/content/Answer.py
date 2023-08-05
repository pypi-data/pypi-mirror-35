from .Ancestry import Content
from ..util.urls import urls
from ..util import zhihu


class Answer(Content):
    """知乎的答案对象"""

    def __init__(self, id):
        super().__init__(id, '答案', 'answer')
        if 2 == 1:  # 单纯为了编辑器能智能提示
            self.thumbnail = ""
            self.is_collapsed = ""
            self.created_time = ""
            self.updated_time = ""
            self.extras = ""
            self.is_copyable = ""
            self.thanks_count = ""
            self.is_mine = ""
            self.is_sticky = ""
            self.sticky_info = ""
            self.collaboration_status = ""
            self.has_publishing_draft = ""
            self.editable_content = ""
            self.relevant_info = ""
            self.reward_info = ""

    def init(self, id=''):
        responseJSON = zhihu.json(f'https://www.zhihu.com/api/v4/answers/{self.id}')
        self.load(responseJSON)

    def load(self, JSON):
        super(Answer, self).load(JSON)
        if JSON.get('question'):
            from .Question import Question
            self.question = Question(JSON.get('question'))
        for v in ['thumbnail', 'is_collapsed', 'created_time', 'updated_time', 'extras', 'is_copyable', 'thanks_count', 'is_mine', 'is_sticky', 'sticky_info', 'collaboration_status', 'has_publishing_draft', 'editable_content', 'relevant_info', 'reward_info']:
            if JSON.get(v) != None:
                setattr(self, v, JSON.get(v))

        datas = {
            'is_favoriting': JSON.get('relationship', {}).get('is_favorited'),
            'is_nohelping': JSON.get('relationship', {}).get('is_nothelp'),
            'is_thanking': JSON.get('relationship', {}).get('is_thanked'),
            'is_voting': JSON.get('relationship', {}).get('voting')

        }
        for k, v in datas.items():
            if v != None:
                setattr(self, k, v)

    @zhihu.log_attr
    def block(self):
        """对{name}的回答不感兴趣 """
        url = urls(self, 'block')()
        responseJSON = zhihu.jsonp(url[0], url[1])
        return self

    # @zhihu.iter_factory('voters')
    # def voters(x):
    #     """获取{name}的回答的点赞列表 """
    #     from .People import People
    #     return People(x)

    @zhihu.log_attr
    def down(self):
        '''反对{name}的回答'''
        url = urls(self, 'vote')('down')
        responseJSON = zhihu.jsonp(url[0], url[1])

    @zhihu.log_attr
    def undown(self):
        '''取消对{name}的回答的反对'''
        url = urls(self, 'vote')('undown')
        responseJSON = zhihu.jsonp(url[0], url[1])
