from .create_window import create_main_window
from .tab_view_manager import create_tabs

root = create_main_window()
root_tabs = create_tabs(root)
