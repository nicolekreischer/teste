# External libraries
import hydralit_components as hc

# Internal libraries
from page_2.pg2_guide2 import run_guide2

def run_page2():

    guides_auto = [
            {'icon':"bi bi-file-earmark-arrow-up",'label':"Upload spreadsheet to add data"}
        ]    
    over_theme_auto = {'txc_inactive': '#262730','menu_background':'#F0F2F6','txc_active':'white','option_active':'#4073ca'}
    guide_auto = hc.option_bar(option_definition = guides_auto,override_theme = over_theme_auto, horizontal_orientation=True, key="page2")


    run_guide2()
