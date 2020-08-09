from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('vim',
                'Vim',
                [(VimTextEditorView,[])],
                "git@github.com:v-nys/vim-modeloplossingen.git")
