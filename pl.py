#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from telethon.sync import TelegramClient,errors, connection
from os import remove as osremove
from Color import Color
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class MyBot:
    def __init__(self,name,api_id,api_hash):
        self.cli = TelegramClient(name,api_id,api_hash)
        self.name=name
        self.connect()
    def show(self):
        print(f'\n\t\t{Color.BLACK} {Color.BACKGROUND_RED}㉿ [   Plague Dr.  ] ㉿{Color.RESET}')
        print(Color.RED ,f'\t- Connected to {Color.YELLOW} {self.name} {Color.RED} session!')
        print('\t• Please select one of the following:\n', Color.RESET)
        self.inshow()
    def inshow(self):
        print(f'''{Color.CYAN}- - - - - - - - - - - - - - - - - - - - -
卐 show all chat && chat id: {Color.GREEN}[{Color.RESET} 1 {Color.GREEN}]{Color.CYAN}
卐 Send from restrict chat to any chat: {Color.GREEN}[{Color.RESET} 2 {Color.GREEN}]{Color.CYAN}
卐 forward msg: {Color.GREEN}[{Color.RESET} 3 {Color.GREEN}]{Color.CYAN}
卐 Forward without quotes {Color.GREEN}[{Color.RESET} 4 {Color.GREEN}]{Color.CYAN}
卐 ExiT : {Color.GREEN}[{Color.RESET} 0 {Color.GREEN}]{Color.CYAN}
''')
        cmd = input(f'{Color.GREEN}┌──({Color.CYAN}EnteR㉿plagueDr{Color.GREEN})-[{Color.RESET}~/pl{Color.GREEN}]\n└─${Color.RESET} ')
        switch(cmd,{
            '0':exit,
            '1':self.show_chats,
            '2':self.send_restrictchat_2anychat,
            '3':self.forwaed_msg,
            '4':self.nameless_forward
        },self.what)()
        self.inshow()
    def send_restrictchat_2anychat(self):
        restrictchat = checkchat(input('- enter restrict chat = '))
        anychat = checkchat(input('- enter any chat 2 send = '))
        print(f'{Color.RED}----    if you enter \'0\', it means \'None\'    ----',Color.RESET)
        end = getint('- enter end msg = ')
        end = None if end == 0 else end
        print(Color.DARK_GRAY,'\n\n----    wait!    ----\n',Color.RESET)
        try:
            for msg in self.cli.iter_messages(restrictchat,end):
                if msg.media:
                    media = self.cli.download_media(msg.media)
                    self.cli.send_file(anychat,media,caption=msg.raw_text)
                else:
                    self.cli.send_message(anychat,msg.raw_text)
        except ValueError:
            print(f'{Color.RED}- chat not found !',Color.RESET)
    def forwaed_msg(self):
        mainchat = checkchat(input('- enter main chat = '))
        anychat = checkchat(input('- enter any chat 2 send = '))
        print(f'{Color.RED}----    if you enter \'0\', it means \'None\'    ----',Color.RESET)
        end = getint('- enter end msg = ')
        end = None if end == 0 else end
        print(Color.DARK_GRAY,'\n\n----    wait!    ----\n',Color.RESET)
        try:
            for msg in self.cli.iter_messages(mainchat,end):
                msg.forward_to(anychat)
        except ValueError:
            print(f'{Color.RED}- chat not found !{Color.RESET}')
        except errors.rpcerrorlist.ChatForwardsRestrictedError:
            print(f'{Color.RED}- chat is restricted ! {Color.GRAY}please use \'Send from restrict chat to any chat\' !{Color.RESET}')
    def nameless_forward(self):
        mainchat = checkchat(input('- enter main chat = '))
        anychat = checkchat(input('- enter any chat 2 send = '))
        print(f'{Color.RED}----    if you enter \'0\', it means \'None\'    ----',Color.RESET)
        end = getint('- enter end msg = ')
        end = None if end == 0 else end
        print(Color.DARK_GRAY,'\n\n----    wait!    ----\n',Color.RESET)
        try:
            for msg in self.cli.iter_messages(mainchat,end):
                if msg.media:
                    self.cli.send_file(anychat,msg.media,caption=msg.raw_text)
                else:
                    self.cli.send_message(anychat,msg.raw_text)
        except ValueError:
            print(f'{Color.RED}- chat not found !{Color.RESET}')
        except errors.rpcerrorlist.ChatForwardsRestrictedError:
            print(f'{Color.RED}- chat is restricted ! {Color.GRAY}please use \'Send from restrict chat to any chat\' !{Color.RESET}')
    def connect(self):
        self.cli.connect()
        if not self.cli.is_user_authorized():
            self.login()
    def login(self):
        number = input('- enter phone = ')
        self.cli.send_code_request(number)
        code = input('- code = ')
        try:
            self.cli.sign_in(number, code)
        except errors.rpcerrorlist.SessionPasswordNeededError:
            password = input('enter pass = ')
            self.cli.sign_in(password=password)
    def show_chats(self):
        for dialog in self.cli.iter_dialogs():
            print(f'{Color.GREEN}[ {Color.BLUE}+ {Color.GREEN}]{Color.YELLOW}',dialog.name, f'{Color.GRAY} = {Color.MAGENTA}', dialog.id,f';{Color.RESET}')
    def what(self):
        print(Color.RED,'\n- 404 !\n',Color.RESET)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def switch(search, source: dict, default):
    return source.get(search, default)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def getint(msg: str, er: str = '- enter an integer !'):
    try:
        print(msg,end='')
        return int(input())
    except ValueError:
        print(er)
        return getint(msg,er)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class Color:
    RESET = '\x1b[0m'
    RED = '\x1b[91m'
    GRAY = '\x1b[90m'
    MAGENTA = '\x1b[35m'
    CYAN = '\x1b[96m'
    YELLOW = '\x1b[93m'
    BLUE = '\x1b[94m'
    BLACK = '\x1b[30m'
    GREEN = '\x1b[92m'
    LIGHT_GRAY = '\x1b[37m'
    DARK_GRAY = '\x1b[90m'
    LIGHT_RED = '\x1b[91m'
    LIGHT_GREEN = '\x1b[92m'
    LIGHT_YELLOW = '\x1b[93m'
    LIGHT_BLUE = '\x1b[94m'
    LIGHT_MAGENTA = '\x1b[95m'
    LIGHT_CYAN = '\x1b[96m'
    #
    BACKGROUND_RED = '\x1b[41m'
    BACKGROUND_GRAY = '\x1b[100m'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkchat(chat: str):
    if chat[0] == '-' or chat.isdigit():
        return int(chat)
    return chat
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
