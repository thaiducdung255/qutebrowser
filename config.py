# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401

config: ConfigAPI = config  # noqa: F821 pylint: disable=E0602,C0103,E0601
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103,E0601

config.load_autoconfig()


def unbind(keys):
    for key in keys:
        config.unbind(key)


def bind(bind_dict, mode="normal"):
    for mode, bindings in bind_dict.items():
        for lhs, rhs in bindings.items():
            config.bind(lhs, rhs, mode)


# unbind mappings
unbind_keys = [
    "j",
    "k",
    "l",
    "<Control-Tab>",
    "<Control-Shift-Tab>",
    "R",
    "<Control-v>",
]
unbind(unbind_keys)

# command bindings
normal_bindings = {
    "<Control-Space>": "zoom-in",
    "<Control-Shift-Space>": "zoom-out",
    "E": "tab-next",
    "N": "tab-prev",
    "n": "scroll down",
    "e": "scroll up",
    "h": "scroll left",
    "i": "scroll right",
    "m": "scroll-page 0 0.7",
    "M": "scroll-page 0 -1",
    "d": "devtools",
    "a": "hint inputs",
    "y": "hint links yank",
    "Y": "yank",
    "l": "hint images",
    "<Return>": "cmd-set-text :",
    "t": "cmd-set-text -s :tab-select",
    "fd": "hint links download",
    "<Control-h>": "tab-focus 1",
    "<Control-n>": "tab-focus 2",
    "<Control-e>": "tab-focus 3",
    "<Control-i>": "tab-focus 4",
    "<Control-o>": "tab-focus 5",
    "<Control-j>": "tab-focus 6",
    "<Control-l>": "tab-focus 7",
    "<Control-u>": "tab-focus 8",
    "<Control-y>": "tab-focus 9",
    "<Control-;>": "tab-focus 10",
    "r": "reload -f",
    "R": "restart",
    "<Control-Shift-e>": "tab-move +",
    "<Control-Shift-n>": "tab-move -",
    "H": "back",
    "I": "forward",
    "S": "bookmark-add",
    "q": "tab-close",
    "F": "hint all tab",
    "gh": "history",
    "gb": "bookmark-list --jump",
    "gs": "view-source",
    "<Tab>": "search-next",
    "<Shift-Tab>": "search-prev",
    "k": "mode-enter passthrough",
    "D": "tab-clone",
    "<Control-t>": "open -p",
}

# insert bindings
insert_bindings = {}

# passthrough bindings
passthrough_bindings = {"<ESC>": "mode-leave"}

# caret bindings
caret_bindings = {
    "gf": "move-to-end-of-line",
    "ga": "move-to-start-of-line",
    "ge": "move-to-end-of-prev-block",
    "gn": "move-to-end-of-next-block",
    "n": "move-to-next-line",
    "e": "move-to-prev-line",
    "i": "move-to-next-char",
    "m": "scroll down",
    "M": "scroll up",
    "I": "scroll right",
}

bindings = {
    "normal": normal_bindings,
    "caret": caret_bindings,
    "insert": insert_bindings,
    "passthrough": passthrough_bindings,
}

bind(bindings)

c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
}
c.url.default_page = "https://www.google.com"
c.url.start_pages = ["https://www.google.com"]
c.hints.chars = "arstdhneioqwfpgjluy;zxcvbkm."
c.hints.find_implementation = "javascript"
c.hints.uppercase = True
c.scrolling.smooth = True
c.scrolling.bar = "always"
c.search.ignore_case = "smart"
c.downloads.remove_finished = 3
c.fonts.default_size = "11pt"
c.fonts.default_family = "FiraCodeNerdFontMono-Regular"
c.tabs.max_width = 300
c.content.cookies.accept = "all"
c.content.blocking.method = "both"
c.auto_save.session = True
c.input.mode_override = "normal"
c.tabs.title.format = "{perc} {current_title:.30}"
c.window.title_format = "qutebrowser"
