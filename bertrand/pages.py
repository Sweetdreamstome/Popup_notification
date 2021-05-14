from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Group
#from tkinter import *
#from PIL import ImageTk,Image
#from tkinter import messagebox
#from selenium import webdriver

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
    '''
    def before_next_page(self):
        driver=webdriver.Chrome("C:/Users/fredi/Desktop/python/e2labup/pop_up/chromedriver.exe")
        driver.maximize_window()
        location="C:/Users/fredi/Desktop/python/e2labup/pop_up/testmehtml.html"
        driver.get(location)
        
        button=driver.find_element_by_name('alert')
        button.click()
        driver.close
    '''
    #def before_next_page(self):
        
        #Aquí tengo que poner 3 minutos o más
        
        #self.group.popupmsg("Hola")
        #mainloop()

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [TestMobile, Introduction, Decide, ResultsWaitPage, Results]
