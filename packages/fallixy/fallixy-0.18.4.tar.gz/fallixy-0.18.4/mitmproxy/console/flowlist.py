from __future__ import absolute_import, print_function, division

import urwid

import netlib.http.url
from mitmproxy import exceptions
from mitmproxy.console import common
from mitmproxy.console import signals
from mitmproxy.flow import export

import time
import re
import json
import urlparse

def _mkhelp():
    text = []
    keys = [
        ("A", "accept all intercepted flows"),
        ("a", "accept this intercepted flow"),
        ("b", "save request/response body"),
        ("C", "export flow to clipboard"),
        ("d", "delete flow"),
        ("D", "duplicate flow"),
        ("e", "toggle eventlog"),
        ("E", "export flow to file"),
        ("f", "filter view"),
        ("F", "toggle follow flow list"),
        ("L", "load saved flows"),
        ("m", "toggle flow mark"),
        ("M", "toggle marked flow view"),
        ("n", "create a new request"),
        ("N", "add filter to remove Noise"),
        ("r", "replay request"),
        ("R", "repeat this 64 times with incrementing id"),
        ("S", "server replay request/s"),
        ("u", "toggle listed flows markings"),
        ("U", "unmark all marked flows"),
        ("v", "remove all filters"),
        ("V", "revert changes to request"),
        ("w", "save flows "),
        ("W", "stream flows to file"),
        ("X", "kill and delete flow, even if it's mid-intercept"),
        ("z", "clear flow list or eventlog"),
        ("tab", "tab between eventlog and flow list"),
        ("enter", "view flow"),
        ("|", "run script on this flow"),
        ("f1", "toggle authenticion to fail/pass"),
        ("f2", "toggle authorization to fail/pass"),
        ("f3", "toggle payu salt leak to fail/pass"),
        ("f4", "toggle otp leak to fail/pass")
    ]
    text.extend(common.format_keyvals(keys, key="key", val="text", indent=4))
    return text
help_context = _mkhelp()

footer = [
    ('heading_key', "?"), ":help ",
]


class LogBufferBox(urwid.ListBox):

    def __init__(self, master):
        self.master = master
        urwid.ListBox.__init__(self, master.logbuffer)

    def keypress(self, size, key):
        key = common.shortcuts(key)
        if key == "z":
            self.master.clear_events()
            key = None
        elif key == "G":
            self.set_focus(len(self.master.logbuffer) - 1)
        elif key == "g":
            self.set_focus(0)
        return urwid.ListBox.keypress(self, size, key)


class BodyPile(urwid.Pile):

    def __init__(self, master):
        h = urwid.Text("Event log")
        h = urwid.Padding(h, align="left", width=("relative", 100))

        self.inactive_header = urwid.AttrWrap(h, "heading_inactive")
        self.active_header = urwid.AttrWrap(h, "heading")

        urwid.Pile.__init__(
            self,
            [
                FlowListBox(master),
                urwid.Frame(
                    LogBufferBox(master),
                    header = self.inactive_header
                )
            ]
        )
        self.master = master

    def keypress(self, size, key):
        if key == "tab":
            self.focus_position = (
                self.focus_position + 1) % len(self.widget_list)
            if self.focus_position == 1:
                self.widget_list[1].header = self.active_header
            else:
                self.widget_list[1].header = self.inactive_header
            key = None
        elif key == "e":
            self.master.toggle_eventlog()
            key = None

        # This is essentially a copypasta from urwid.Pile's keypress handler.
        # So much for "closed for modification, but open for extension".
        item_rows = None
        if len(size) == 2:
            item_rows = self.get_item_rows(size, focus = True)
        i = self.widget_list.index(self.focus_item)
        tsize = self.get_item_size(size, i, True, item_rows)
        return self.focus_item.keypress(tsize, key)


class ConnectionItem(urwid.WidgetWrap):
    PHONE_NUMBER = "7259361414"
    EMAIL = "mkagenius@gmail.com"
    def is_mobile_number(self, s):
        re_phone = re.compile(r'(\d{10})')
        if re_phone.match(s):
            return True
        return False

    def is_email(self, s):
        re_email =  re.compile(r'([^@\/=\?]+(?:@|%40)[^@\/=\?]+\.[^@\/=\?\ ]+)')
        if re_email.match(s):
            return True
        return False

    def decrement_id(self, id):
        return str(int(id) - 1)

    def update_json(self, jsn, kk, vv):
        try:
            jsn = json.loads(jsn)
            for k, v in jsn.iteritem():
                if type(v) == dict:
                    jsn[k] = json.loads(self.update_json(json.dumps(v), kk, vv))
                elif k == kk:
                    jsn[k] = vv

            return json.dumps(jsn)
        except:
            if type(jsn) == dict:
                return json.dumps(jsn)
            return jsn

    def __init__(self, master, state, flow, focus):
        self.master, self.state, self.flow = master, state, flow
        self.f = focus
        w = self.get_text()
        urwid.WidgetWrap.__init__(self, w)

    def get_text(self):
        cols, _ = self.master.ui.get_cols_rows()
        return common.format_flow(
            self.flow,
            self.f,
            hostheader=self.master.options.showhost,
        )

    def selectable(self):
        return True

    def save_flows_prompt(self, k):
        if k == "l":
            signals.status_prompt_path.send(
                prompt = "Save listed flows to",
                callback = self.master.save_flows
            )
        elif k == "h":
            signals.status_prompt_path.send(
                prompt = "Save listed flows to (as har)",
                callback = self.master.save_flows_as_har
            )
        elif k == "r":
            signals.status_prompt_path.send(
                prompt="Save listed flows as a report",
                callback=self.master.save_flows_as_report
            )
        elif k == "s":
            signals.status_prompt_path.send(
                prompt="Save listed flows as a Swagger file",
                callback=self.master.save_flows_as_swagger
            )
        else:
            signals.status_prompt_path.send(
                prompt = "Save this flow to",
                callback = self.master.save_one_flow,
                args = (self.flow,)
            )

    def server_replay_prompt(self, k):
        a = self.master.addons.get("serverplayback")
        if k == "a":
            a.load([i.copy() for i in self.master.state.view])
        elif k == "t":
            a.load([self.flow.copy()])
        signals.update_settings.send(self)

    def mouse_event(self, size, event, button, col, row, focus):
        if event == "mouse press" and button == 1:
            if self.flow.request:
                self.master.view_flow(self.flow)
                return True


    def remove_auth(self, headers):
        """
        remove the authorization related headers, keep the rest
        :param headers: input
        :return: headers not containing any authorizations
        """
        if 'authorization' in headers:
            headers.set_all('authorization', [])
        if 'Authorization' in headers:
            headers.set_all('Authorization', [])
        if 'X-Authorization' in headers:
            headers.set_all('X-Authorization', [])
        if 'X-Auth' in headers:
            headers.set_all('X-Auth', [])
        if 'X-auth' in headers:
            headers.set_all('X-auth', [])
        if 'Cookie' in headers:
            headers.set_all('Cookie', [])
        if 'cookie' in headers:
            headers.set_all('cookie', [])
        return headers

    def revert_to_original(self):
        if not self.flow.modified():
                signals.status_message.send(message="Flow not modified.")
                return
        self.state.revert(self.flow)
        signals.flowlist_change.send(self)
        signals.status_message.send(message="Reverted.")

    def test_authentication(self, f):
        """
        Test authentication for this flow
        :param f:
        :return: whether authentication is required or not
        """
        if not f.response:
            if "backup" not in f.get_state() or "response" not in f.get_state()["backup"]:
                return 0

        #self.flow.backup()
        prev_response = f.response
        signals.status_message.send(message="Testing authentication.")
        prev_headers = f.request.headers
        f.request.headers = self.remove_auth(f.request.headers)
        if prev_headers == f.request.headers:
            f.authentication = 1
            return 1
        r = self.master.replay_request(f)
        return 3

    def test_payu_salt_leak(self, f):
        """
        Look for PayU specific salt in flow response or request data
        :param f:
        :return: whether found salt or not
        """
        signals.status_message.send(message="Testing payu salt leak.")
        # f.request.headers = self.remove_auth(f.request.headers)
        found_salt = False
        if f.request.content:
            post_str = f.request.content
            post_dict = dict(urlparse.parse_qsl(post_str))
            found_salt = common.salt_leakage(post_dict, f.request.url)

        if f.response.content:
            found_salt = common.salt_leakage_in_response(f.response.content)

        if found_salt: 
            return 2 # bug found
        return 1 # no bug

    def test_otp_leak(self, f):
        """
        Test if OTP is being sent back in the response of generate otp call
        :param f:
        :return: 2 if OTP is leaked else return 1
        """
        prev_response = f.response
        signals.status_message.send(message="Testing otp leak")
        # f.request.headers = self.remove_auth(f.request.headers)
        content_type = ""
        if "content-type" in f.response.headers:
            content_type = f.response.headers["content-type"]
        elif "Content-Type" in f.response.headers:
            content_type = f.response.headers["Content-Type"]
        
        if "json" in content_type.lower() and common.resp_body_contains_otp(f.response.content, content_type):
            return 2
        else:
            return 1 # since so far only json leaked the salt

    def get_content_type(self, headers):
        content_type = ""
        if "content-type" in headers:
            content_type = headers["content-type"]
        elif "Content-Type" in headers:
            content_type = headers["Content-Type"]
        return content_type

    def edit_url(self, regex, url):
        """
        Swap existing phone number and email to see if Authorization is properly implemented for this API or not
        :param regex:
        :param url:
        :return: new URL with new phone number and email address
        """
        ret = ""

        ss = regex.finditer(url)

        prev = 0
        for i in ss:
            
            if i.group(1):
                # phone num 
                # Todo: this is regex is not good enough to detect phone number
                span_tup = i.span(1)
                ret += url[prev:span_tup[0]]
                ret += str(self.PHONE_NUMBER)
            if i.group(2):
                # email
                span_tup = i.span(2)
                ret += url[prev:span_tup[0]]
                ret += str(self.EMAIL)
            if i.group(3):
                # user id
                span_tup = i.span(3)  
                ret += url[prev:span_tup[0]]    
                ret += str(int(url[span_tup[0]:span_tup[1]]) - 1)
                
            prev = span_tup[1]

        ret += url[prev:]

        return ret
    def manipulate_user_id(self, k, v):
        if "user_id" in k or "userid" in k or "_id" in k or "profileid" in k or "cartid" in k:
            v = self.decrement_id(v)
        if "phone" in k or "mobile" in k or self.is_mobile_number(v):
            v = self.PHONE_NUMBER
        if "email" in k or self.is_email(v):
            v = self.EMAIL
        return v

    def edit_body(self, body, content_type):
        """
        Edit user id, phone or email to see if API still works, meaning authorization is not working
        :param body:
        :return:
        """

        if "json" in content_type:
            req_dict = common.flatten(body)
            req_keys = req_dict.keys()
            for kk in req_keys:
                k = kk.lower()
                if "user_id" in k or "userid" in k or "_id" in k or "profileid" in k or "cartid" in k:
                    body = self.update_json(body, kk, self.decrement_id(req_dict[kk]))
                if "phone" in k or "mobile" in k or self.is_mobile_number(req_dict[kk]):
                    body = self.update_json(body, kk, self.PHONE_NUMBER)
                if "email" in k or self.is_email(req_dict[kk]):
                    body = self.update_json(body, kk, self.EMAIL)
            return body

        if "multipart" in content_type:
            # TODO: edit params
            return body
        elif "form" in content_type:
            parts = body.split("&")
            ret = ""
            for p in parts:
                if '=' not in p:
                    continue
                [kk, v] = p.split('=',1)
                k = kk.lower()

                v = self.manipulate_user_id(k, v)

                ret += kk + "=" + v + "&"
            return ret

        return body

    def edit_headers(self, headers):
        dict = headers
        for kk, v in headers.iteritems():
            k = kk.lower()
            v = self.manipulate_user_id(k, v)
            dict[kk] = v

        return dict

    def test_authorization(self, f):
        """
        Test authorization by replacing user identity to a different user while keeping auth headers same
        :param f:
        :return: 2 if auth is broken, else 1, 3 is yellow intermediate stage
        """
        if not f.response:
            if "backup" not in f.get_state() or "response" not in f.get_state()["backup"]:
                return 0
        #self.flow.backup()
        prev_response = f.response
        signals.status_message.send(message="Testing authorization.")

        f.request.url = self.edit_url(common.re_phone_or_email_or_userid, f.request.url)

        # edit url, body or header whichever contains user id or email
        f.request.content = self.edit_body(f.request.content, self.get_content_type(f.request.headers))

        f.request.headers = self.edit_headers(f.request.headers)

        signals.status_message.send(message="Edited url: " + f.request.url)
        r = self.master.replay_request(f)
        return 3

    def gather_authentication_result(self, f):
        if f.authentication > 0:
            return f.authentication
        if "backup" not in f.get_state():
            signals.status_message.send(message="No backup found..maybe you checked result too fast.")
            return 0
        backup_flow = f.get_state()["backup"]
        if f.response and f.response.content == backup_flow["response"]["content"]:
            return 2 # auth broken
        else:
            return 1

        return 0



    def is_different_data(self, new_resp, old_resp):
        """
        This compares new response data with the original response data and decides if they are same or new data got fetched
        :param new_resp:
        :param old_resp:
        :return: True if data leaked and False if not
        """
        content_type = self.get_content_type(new_resp.headers)

        if "json" in content_type:
            old_resp_dict = common.flatten(old_resp["content"])
            new_resp_dict = common.flatten(new_resp.content)

            keys_old = old_resp_dict.keys()
            keys_new = new_resp_dict.keys()

            cnt = 0
            match_cnt = 0
            value_match_cnt = 0
            for k in keys_old:
                cnt += 1
                if k in keys_new:
                    match_cnt+=1
                    if old_resp_dict[k] == new_resp_dict[k]:
                        value_match_cnt += 1

            if value_match_cnt == match_cnt:
                return False # even same values

            if match_cnt / (cnt * 1.0) * 100.0 > 90.0 :
                return True # different values, almost same keys

            return False
        else:
            if "error" in new_resp.content.lower(): # anything better than error keyword?
                return False # if error happened then its not a data leak
            return True # if error not happened then its a data leak

    def is_request_same(self, f1, f2):

        # z = common.flatten(f1)
        # if "url" in z:
        #     signals.status_message.send(message="Found url key.")
        # else:
        #     signals.status_message.send(message="NOT found url key.")
        if f1["request"]["content"] != f2.request.content:
            return False
        # if f1["response"]["url"] != f2.request.url:
        #     return False
        for k,v in f1["request"]["headers"]:
            if k not in f2.request.headers or f2.request.headers[k] != v:
                return False
        signals.status_message.send(message="Request is same.")
        return True


    def gather_authorization_result(self, f):
        """
        This function gathers all the authorization tests done so far on the flow
        :param f:
        :return: 2 if data leak, else 1
        """
        if "backup" not in f.get_state():
            signals.status_message.send(message="No backup found..maybe you checked result too fast.")
            return 0
        backup_flow = f.get_state()["backup"]

        # TODO if request is unchanged, return no data leak
        if self.is_request_same(backup_flow, f):
            return 1

        ## TODO test if response contains data different than this but some user data
        if f.response and f.response.status_code >= 200 and f.response.status_code < 300:
            if f.response.content == backup_flow["response"]["content"]:
                return 1 # authorization is done via cookies or something
            elif self.is_different_data(f.response, backup_flow["response"]): # same type of data content came back, but not exact
                return 2
            else:
                return 1
        else:
            return 1

        return 0

    def keypress(self, xxx_todo_changeme, key):
        (maxcol,) = xxx_todo_changeme
        key = common.shortcuts(key)

        # Test keys are number 1 to 6, flow must me marked before run test on it.
        if key == "1":
            for f in self.state.flows:
                if f.marked:
                    f.authentication = self.test_authentication(f)
                    signals.flowlist_change.send(self)

        if key == "2":
            for f in self.state.flows:
                if f.marked:
                    f.authentication = self.gather_authentication_result(f)
                    signals.flowlist_change.send(self)

        if key == "3":
            cnt = 1
            for f in self.state.flows:
                if f.marked:
                    f.authorization = self.test_authorization(f)
                    signals.flowlist_change.send(self)

        if key == "4":
            for f in self.state.flows:
                if f.marked:
                    f.authorization = self.gather_authorization_result(f)
                    signals.flowlist_change.send(self)

        # payu salt in req or resp
        if key == "5":
            for f in self.state.flows:
                if f.marked:
                    f.payu_salt_leak = self.test_payu_salt_leak(f)
                    signals.flowlist_change.send(self) 

        # otp in resp
        if key == "6":
            for f in self.state.flows:
                if f.marked:
                    f.otp_leak = self.test_otp_leak(f)
                    signals.flowlist_change.send(self)


        if key == "R":
            self.master.repeater(self.flow)
            signals.status_message.send(message="Repeating request 64 times")
            signals.flowlist_change.send(self)
        if key == "a":
            self.flow.accept_intercept(self.master)
            signals.flowlist_change.send(self)
        elif key == "d":
            if self.flow.killable:
                self.flow.kill(self.master)
            self.state.delete_flow(self.flow)
            signals.flowlist_change.send(self)
        elif key == "D":
            f = self.master.duplicate_flow(self.flow)
            self.master.state.set_focus_flow(f)
            signals.flowlist_change.send(self)
        elif key == "f1":
            self.flow.authentication += 1
            self.flow.authentication %= 3
            signals.flowlist_change.send(self)
        elif key == "f2":
            self.flow.authorization += 1
            self.flow.authorization %= 3
            signals.flowlist_change.send(self)
        elif key == "f3":
            self.flow.payu_salt_leak += 1
            self.flow.payu_salt_leak %= 3
            signals.flowlist_change.send(self)
        elif key == "f4":
            self.flow.otp_leak += 1
            self.flow.otp_leak %= 3
            signals.flowlist_change.send(self)
        elif key == "u":
            for f in self.master.state.view:
                f.marked = not f.marked
            signals.flowlist_change.send(self)
        elif key == "m":
            self.flow.marked = not self.flow.marked
            signals.flowlist_change.send(self)
        elif key == "M":
            if self.state.mark_filter:
                self.state.disable_marked_filter()
            else:
                self.state.enable_marked_filter()
            signals.flowlist_change.send(self)
        elif key == "N":

            self.state.set_view_filter("!(.gif) & !(.js) & !(.css) & !(.ttf) & !(.png) & !(.svg) & !(gstatic) & !(.ico) & !(.jpg) & !(.jpeg) & !(.woff) & !(.woff2) & !(fbcdn) & !(google) & !(facebook)")
            signals.flowlist_change.send(self)
        elif key == "v":
            self.state.set_view_filter("")
            signals.flowlist_change.send(self)
        elif key == "r":
            try:
                self.master.replay_request(self.flow)
            except exceptions.ReplayException as e:
                signals.add_log("Replay error: %s" % e, "warn")
            signals.flowlist_change.send(self)
        elif key == "S":
            def stop_server_playback(response):
                if response == "y":
                    self.master.options.server_replay = []
            a = self.master.addons.get("serverplayback")
            if a.count():
                signals.status_prompt_onekey.send(
                    prompt = "Stop current server replay?",
                    keys = (
                        ("yes", "y"),
                        ("no", "n"),
                    ),
                    callback = stop_server_playback,
                )
            else:
                signals.status_prompt_onekey.send(
                    prompt = "Server Replay",
                    keys = (
                        ("all flows", "a"),
                        ("this flow", "t"),
                    ),
                    callback = self.server_replay_prompt,
                )
        elif key == "U":
            for f in self.state.flows:
                f.marked = False
            signals.flowlist_change.send(self)
        elif key == "V":
            if not self.flow.modified():
                signals.status_message.send(message="Flow not modified.")
                return
            self.state.revert(self.flow)
            signals.flowlist_change.send(self)
            signals.status_message.send(message="Reverted.")
        elif key == "w":
            signals.status_prompt_onekey.send(
                self,
                prompt = "Save",
                keys = (("listed flows as swagger", "s"),
                    ("listed flows as report", "r"),
                    ("listed flows as har", "h"),
                    ("listed flows", "l"),
                    ("this flow", "t"),
                ),
                callback = self.save_flows_prompt,
            )
        elif key == "X":
            if self.flow.killable:
                self.flow.kill(self.master)
        elif key == "z":
            # create a copy since used in for loop
            copy_of_state_view = self.state.view[:]
            for f in copy_of_state_view:
                signals.add_log("Len of state.view %d " % len(self.state.view), level="info")
                if f.killable:
                    f.kill(self.master)
                self.state.delete_flow(f)
            signals.flowlist_change.send(self)
        elif key == "enter":
            if self.flow.request:
                self.flow = common.add_key_log(self.flow, "enter")
                signals.flowlist_change.send(self)
                self.master.view_flow(self.flow)
        elif key == "|":
            signals.status_prompt_path.send(
                prompt = "Send flow to script",
                callback = self.master.run_script_once,
                args = (self.flow,)
            )
        elif key == "E":
            signals.status_prompt_onekey.send(
                self,
                prompt = "Export to file",
                keys = [(e[0], e[1]) for e in export.EXPORTERS],
                callback = common.export_to_clip_or_file,
                args = (None, self.flow, common.ask_save_path)
            )
        elif key == "C":
            signals.status_prompt_onekey.send(
                self,
                prompt = "Export to clipboard",
                keys = [(e[0], e[1]) for e in export.EXPORTERS],
                callback = common.export_to_clip_or_file,
                args = (None, self.flow, common.copy_to_clipboard_or_prompt)
            )
        elif key == "b":
            common.ask_save_body(None, self.flow)
        else:
            return key


class FlowListWalker(urwid.ListWalker):

    def __init__(self, master, state):
        self.master, self.state = master, state
        signals.flowlist_change.connect(self.sig_flowlist_change)

    def sig_flowlist_change(self, sender):
        self._modified()

    def get_focus(self):
        f, i = self.state.get_focus()
        f = ConnectionItem(self.master, self.state, f, True) if f else None
        return f, i

    def set_focus(self, focus):
        ret = self.state.set_focus(focus)
        return ret

    def get_next(self, pos):
        f, i = self.state.get_next(pos)
        f = ConnectionItem(self.master, self.state, f, False) if f else None
        return f, i

    def get_prev(self, pos):
        f, i = self.state.get_prev(pos)
        f = ConnectionItem(self.master, self.state, f, False) if f else None
        return f, i


class FlowListBox(urwid.ListBox):

    def __init__(self, master):
        # type: (mitmproxy.console.master.ConsoleMaster) -> None
        self.master = master
        super(FlowListBox, self).__init__(FlowListWalker(master, master.state))

    def get_method_raw(self, k):
        if k:
            self.get_url(k)

    def get_method(self, k):
        if k == "e":
            signals.status_prompt.send(
                self,
                prompt = "Method",
                text = "",
                callback = self.get_method_raw
            )
        else:
            method = ""
            for i in common.METHOD_OPTIONS:
                if i[1] == k:
                    method = i[0].upper()
            
            self.get_url(method)

    def get_url(self, method):
        signals.status_prompt.send(
            prompt = "URL",
            text = "http://www.example.com/",
            callback = self.new_request,
            args = (method,)
        )

    def new_request(self, url, method):
        parts = netlib.http.url.parse(str(url))
        if not parts:
            signals.status_message.send(message="Invalid Url")
            return
        scheme, host, port, path = parts
        f = self.master.create_request(method, scheme, host, port, path)
        self.master.state.set_focus_flow(f)
        signals.flowlist_change.send(self)

    def keypress(self, size, key):
        key = common.shortcuts(key)
        if key == "A":
            self.master.accept_all()
            signals.flowlist_change.send(self)
        elif key == "e":
            self.master.toggle_eventlog()
        elif key == "g":
            self.master.state.set_focus(0)
            signals.flowlist_change.send(self)
        elif key == "G":
            self.master.state.set_focus(self.master.state.flow_count())
            signals.flowlist_change.send(self)
        elif key == "f":
            signals.status_prompt.send(
                prompt = "Filter View",
                text = self.master.state.filter_txt,
                callback = self.master.set_view_filter
            )
        elif key == "L":
            signals.status_prompt_path.send(
                self,
                prompt = "Load flows",
                callback = self.master.load_flows_callback
            )
        elif key == "n":
            signals.status_prompt_onekey.send(
                prompt = "Method",
                keys = common.METHOD_OPTIONS,
                callback = self.get_method
            )
        elif key == "F":
            self.master.toggle_follow_flows()
        elif key == "W":
            if self.master.options.outfile:
                self.master.options.outfile = None
            else:
                signals.status_prompt_path.send(
                    self,
                    prompt="Stream flows to",
                    callback= lambda path: self.master.options.update(outfile=(path, "ab"))
                )
        else:
            return urwid.ListBox.keypress(self, size, key)
