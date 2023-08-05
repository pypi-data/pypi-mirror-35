# -*- coding: utf-8  -*-
#StoryBot IRC lib

import datetime, logging, socket
try:
    import urllib, urllib2
except ImportError:
    import urllib.request

class IRC:
    def __init__(self):
        self.ver = "1.4.1"

    def away(self, msg = None):
        if msg != None:
            self.send("AWAY :%s\r\n" % msg)
        else:
            self.send("AWAY\r\n")

    def ban(self, chan, user):
        self.mode(chan, "+b", user)

    def connect(self, server, port = 6667, user = None, password = None, identname = "StoryBot", realname = "StoryBot", ipv6 = False, chan = None):
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.identname = identname
        self.realname = realname
        if ipv6:
            self.socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        else:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server, port))
        if user != None:
            self.send("NICK %s\r\n" % user)
            self.send("USER %s %s bla :%s\r\n" % (identname, server, realname))
            if password != None:
                self.ns_identify(password)
        if chan != None:
            self.join(chan)

    def cs(self, msg):
        self.privmsg("ChanServ", msg)

    def cs_access(self, chan, user, template):
        self.cs("ACCESS %s add %s %s" % (chan, user, template))

    def cs_access_del(self, chan, user):
        self.cs("ACCESS %s del %s" % (chan, user))

    def cs_akick(self, chan, user, reason = None):
        if reason != None:
            self.cs("AKICK %s add %s %s" % (chan, user, reason))
        else:
            self.cs("AKICK %s add %s" % (chan, user))

    def cs_akick_del(self, chan, user):
        self.cs("AKICK %s del %s" % (chan, user))

    def cs_deop(self, chan, user = None):
        if user != None:
            self.cs("DEOP %s %s" % (chan, user))
        else:
            self.cs("DEOP %s" % chan)

    def cs_devoice(self, chan, user = None):
        if user != None:
            self.cs("DEVOICE %s %s" % (chan, user))
        else:
            self.cs("DEVOICE %s" % chan)

    def cs_flags(self, chan, user, flags):
        self.cs("FLAGS %s %s %s" % (chan, user, flags))

    def cs_invite(self, chan):
        self.cs("INVITE %s" % chan)

    def cs_op(self, chan, user = None):
        if user != None:
            self.cs("OP %s %s" % (chan, user))
        else:
            self.cs("OP %s" % chan)

    def cs_quiet(self, chan, user):
        self.cs("QUIET %s %s" % (chan, user))

    def cs_topic(self, chan, topic):
        self.cs("TOPIC %s %s" % (chan, topic))

    def cs_topicappend(self, chan, topic):
        self.cs("TOPICAPPEND %s %s" % (chan, topic))

    def cs_topicprepend(self, chan, topic):
        self.cs("TOPICPREPEND %s %s" % (chan, topic))

    def cs_topicswap(self, chan, search, replace):
        self.cs("TOPICSWAP %s %s:[%s]" % (chan, search, replace))

    def cs_voice(self, chan, user = None):
        if user != None:
            self.cs("VOICE %s %s" % (chan, user))
        else:
            self.cs("VOICE %s" % chan)

    def cs_unban(self, chan, user):
        self.cs("UNBAN %s %s" % (chan, user))

    def cs_unquiet(self, chan, user):
        self.cs("UNQUIET %s %s" % (chan, user))

    def deop(self, chan, user):
        self.mode(chan, "-o", user)

    def devoice(self, chan, user):
        self.mode(chan, "-v", user)

    def disconnect(self):
        self.socket.close()

    def get_identname(self):
        return self.identname

    def get_port(self):
        return self.port

    def get_realname(self):
        return self.realname

    def get_server(self):
        return self.server

    def get_user(self):
        return self.user

    def get_ver(self):
        return self.ver

    def identify(self, password, user = None):
        ns_identify(password, user)

    def invite(self, user, chan):
        self.send("INVITE %s %s\r\n" % (user, chan))

    def join(self, chan, key = None):
        if key != None:
            self.send("JOIN %s %s\r\n" % (chan, key))
        else:
            self.send("JOIN %s\r\n" % chan)

    def kick(self, chan, user, text = None):
        if text != None:
            self.send("KICK %s %s :%s\r\n" % (chan, user, text))
        else:
            self.send("KICK %s %s\r\n" % (chan, user))

    def kickban(self, chan, user, text = None):
        self.kick(chan, user, text)
        self.mode(chan, "+b", user)

    def memo(self, user, text):
        self.send("PRIVMSG MemoServ :send %s %s\r\n" % (user, text))

    def mode(self, chan, flags, user = None):
        if user != None:
            self.send("MODE %s %s %s\r\n" % (chan, flags, user))
        else:
            self.send("MODE %s %s\r\n" % (chan, flags))

    def msg(self):
        return " ".join(self.text2[3:])

    def names(self, chan):
        self.send("NAMES %s\r\n" % chan)

    def nick(self, name):
        self.send("NICK %s\r\n" % name)

    def notice(self, chan, text):
        self.send("NOTICE %s :%s\r\n" % (chan, text))

    def ns(self, msg):
        self.privmsg("NickServ", msg)

    def ns_identify(self, password, user = None):
        if user == None:
            self.ns("identify %s" % password)
        else:
            self.ns("identify %s %s" % (user, password))

    def ns_info(self, user):
        self.ns("info %s" % user)

    def ns_release(self, nick, password = None):
        if password == None:
            self.ns("release %s" % nick)
        else:
            self.ns("release %s %s" % (nick, password))

    def op(self, chan, user):
        self.mode(chan, "+o", user)

    def part(self, chan, text = None):
        if text != None:
            self.send("PART %s :%s\r\n" % (chan, text))
        else:
            self.send("PART %s\r\n" % chan)

    def pong(self, server):
        self.send("PONG %s\r\n" % server)

    def privmsg(self, chan, text):
        self.send("PRIVMSG %s :%s\r\n" % (chan, text))

    def quiet(self, chan, user):
        self.mode(chan, "+q", user)

    def quit_irc(self, msg = None):
        if msg != None:
            self.send("QUIT :%s\r\n" % msg)
        else:
            self.send("QUIT\r\n")

    def recv(self, n = 2048):
        self.rep = self.text = self.socket.recv(n).decode("utf-8")
        self.rep2 = self.text2 = self.text.split()
        self.chan_msg = self.text2[2]
        self.command = self.text2[3].lower()
        self.pm = not self.text2[2].startswith("#")
        return self.text

    def send(self, text):
        self.socket.send(bytes(text, "utf-8"))

    def status(self):
        self.privmsg("NickServ", "status")
        return " ".join(self.recv().split()[3:]).strip(":")

    def topic(self, chan, text):
        self.send("TOPIC %s :%s\r\n" % (chan, text))

    def unban(self, chan, user):
        self.mode(chan, "-b", user)

    def unquiet(self, chan, user):
        self.mode(chan, "-q", user)

    def update(self):
        ver = self.get_ver()
        try:
            ver_update = urllib2.urlopen(urllib2.Request("https://skygen.alwaysdata.net/StoryBotUpdate.txt")).read()
        except TypeError:
            ver_update = urllib.request.urlopen(urllib.request.Request("https://skygen.alwaysdata.net/StoryBotUpdate.txt")).read()
        return [ver != ver_update, ver_update]

    def ver(self):
        return self.get_ver()

    def voice(self, chan, user):
        self.mode(chan, "+v", user)

    def whois(self, name):
        self.send("WHOIS %s\r\n" % name)

class Logs:
    def __init__(self, file_name = "IRCLogs_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".log"):
        logging.basicConfig(format = "[%(asctime)s] %(message)s", datefmt = "%Y/%m/%d %H:%M:%S", filename = file_name, level = logging.INFO)

    def log(self, msg):
        logging.info(msg)

    def privmsg(self, chan, user, msg):
        logging.info("(%s) <%s> %s" % (chan, user, msg))
