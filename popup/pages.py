from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Group

class Introduction(Page):
    pass

class TestMobile(Page):
    def is_displayed(self):
        # Here, we'll obtain the type of user we've
        user_agent = self.request.META['HTTP_USER_AGENT']
        # Default value
        self.participant.vars['MobilePhones'] = False
        # The default is changed if the player is mobile
        for substring in ['Mobi', 'Android']:
            if substring in user_agent:
                self.participant.vars['MobilePhones'] = True
        return self.participant.vars['MobilePhones']

class Decide(Page):
    
    form_model = 'player'
    form_fields = ['price']
    
    
   
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    template_name = 'popup/MyWaitPage.html'



class Results(Page):
    pass


page_sequence = [TestMobile, Introduction, Decide, ResultsWaitPage, Results]
