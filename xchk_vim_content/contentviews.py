from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class VimTextEditorView(ContentView):
     
    uid = 'vim_text_editor'
    template = 'xchk_vim_content/vim_text_editor.html'
    strat = Strategy(refusing_check=TrueCheck()),
                     accepting_check=Negation(TrueCheck()))
