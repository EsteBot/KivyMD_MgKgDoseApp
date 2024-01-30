from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

class Tabs(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class Ket_Dom_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
    
    # functions for KETDOM dosing tab  
    def generate_dose_vol(self):
        try:
            dose_t1 = float(self.root.ids.dose_input_t1.text)
            vol = float(self.root.ids.end_vol_input.text)
            max_wgt = float(round((vol*1000),5))
            mg_amt = round((dose_t1*vol),5)
            g_amt = round((mg_amt/1000),5)
            self.root.ids.end_weight_output.color = 0.08, 0.96, .93
            self.root.ids.end_weight_output.text = str(f'Dosable Weight = {max_wgt}g')
            self.root.ids.mg_weight_1.color = 0.08, 0.96, .93
            self.root.ids.mg_weight_1.text = str(f'Mg Weight = {mg_amt}Mg')
            self.root.ids.g_weight_1.color = 0.08, 0.96, .93
            self.root.ids.g_weight_1.text = str(f'g Weight = {g_amt}g')
            self.root.ids.vol_err_msg.text = str("")
            if dose_t1 <= 0 or vol <= 0:
                print(dose_t1, vol)
                self.root.ids.vol_err_msg.text = str("dose and/or vol value(s) must be > 0")
                self.root.ids.egg_question_text1.text = str('')
                self.root.ids.egg_answer_text1.text = str('')
                self.root.ids.end_weight_output.text = str('')
                self.root.ids.mg_weight_1.text = str('')
                self.root.ids.g_weight_1.text = str('')
        except ValueError:
            self.root.ids.vol_err_msg.text = str("dose and/or vol value(s) must be a numerical value")
            self.root.ids.end_weight_output.text = str('')
            self.root.ids.mg_weight_1.text = str('')
            self.root.ids.g_weight_1.text = str('')

    def end_vol_reset_func(self):
        self.release_count = 0
        self.root.ids.egg_question_text1.text = str('')
        self.root.ids.egg_answer_text1.text = str('')
        self.root.ids.dose_input_t1.color =  1,1,1
        self.root.ids.dose_input_t1.text = str('')
        self.root.ids.end_vol_input.color =  1,1,1
        self.root.ids.end_vol_input.text = str('')
        self.root.ids.end_weight_output.color =  1,1,1, 0.3
        self.root.ids.end_weight_output.text = str('Dosable Weight (g)')
        self.root.ids.mg_weight_1.color =  1,1,1, 0.3
        self.root.ids.mg_weight_1.text = str('Drug Weight (Mg)')
        self.root.ids.g_weight_1.color =  1,1,1, 0.3
        self.root.ids.g_weight_1.text = str('Drug Weight (g)')
        self.root.ids.vol_err_msg.text = str('')

    release_count = 0
    def egg_button_on_release1(self):
        if self.release_count == 0:
            self.egg_question1()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer1()
            self.release_count = 0
            return 

    def egg_question1(self):
        self.root.ids.egg_question_text1.color = [.6, 0, 1]
        self.root.ids.egg_question_text1.text = str("Why did the\nneuron cross\nthe microscope?")


    def egg_answer1(self):
        self.root.ids.egg_answer_text1.color = [.6, 0, 1]
        self.root.ids.egg_answer_text1.text = str("To get to\nthe other slide!!!")

    # functions for KETDOM ratio tab
    def generate_dose_weight(self):
        try:
            dose_t2 = float(self.root.ids.dose_input_t2.text)
            tot_weight = float(self.root.ids.weight_input.text)
            tot_vol = float(round((tot_weight/1000),5))
            mg_amt = round(((dose_t2*tot_weight/1000)),5)
            g_amt = round((mg_amt/1000),5)
            self.root.ids.end_vol_output.color = 0.08, 0.96, .93
            self.root.ids.end_vol_output.text = str(f'Dilution Volume = {tot_vol}mL')
            self.root.ids.mg_weight_2.color = 0.08, 0.96, .93
            self.root.ids.mg_weight_2.text = str(f'Mg Weight = {mg_amt}Mg')
            self.root.ids.g_weight_2.color = 0.08, 0.96, .93
            self.root.ids.g_weight_2.text = str(f'g Weight = {g_amt}g')
            self.root.ids.weight_err_msg.text = str("")
            if dose_t2 <= 0 or tot_weight <= 0:
                self.root.ids.weight_err_msg.text = str("dose and/or weight value(s) must be > 0")
                self.root.ids.dose_input_t2.text = str('')
                self.root.ids.weight_input.text = str('')
                self.root.ids.end_vol_output.text = str('')
                self.root.ids.egg_question_text1.text = str('')
                self.root.ids.egg_answer_text1.text = str('')
        except ValueError:
            self.root.ids.weight_err_msg.text = str("dose and/or weight value(s) must be a numerical value")
            self.root.ids.end_vol_output.text = str('')
            self.root.ids.mg_weight_2.text = str('')
            self.root.ids.g_weight_2.text = str('')


    release_count = 0
    def egg_button_on_release2(self):
        if self.release_count == 0:
            self.egg_question2()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer2()
            self.release_count = 0
            return 

    def egg_question2(self):
        self.root.ids.egg_question_text2.color = [.6, 0, 1]
        self.root.ids.egg_question_text2.text = str("How did the\nbiologist impress\ntheir date?")

    def egg_answer2(self):
        self.root.ids.egg_answer_text2.color = [.6, 0, 1]
        self.root.ids.egg_answer_text2.text = str("With designer\ngenes!!!")

    def tot_weight_reset_func(self):
        self.release_count = 0
        self.root.ids.egg_question_text2.text = str('')
        self.root.ids.egg_answer_text2.text = str('')
        self.root.ids.dose_input_t2.color =  1,1,1
        self.root.ids.dose_input_t2.text = str('')
        self.root.ids.weight_input.color =  1,1,1
        self.root.ids.weight_input.text = str('')
        self.root.ids.end_vol_output.color =  1,1,1, 0.3
        self.root.ids.end_vol_output.text = str('Dilution Volume (mL)')
        self.root.ids.mg_weight_2.color =  1,1,1, 0.3
        self.root.ids.mg_weight_2.text = str('Drug Weight (Mg)')
        self.root.ids.g_weight_2.color =  1,1,1, 0.3
        self.root.ids.g_weight_2.text = str('Drug Weight (g)')
        self.root.ids.weight_err_msg.text = str('')

    # function to control switching between tabs
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = tab_text


Ket_Dom_App().run()