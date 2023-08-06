import os
from time import sleep, time
from user_exception import UserException as Ux
import mtaf_logging
from android_zpath import set_zpath_tag, expand_zpath, replace_zpaths
from android_actions import AndroidActions
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import threading
import json
from filters import get_filter
from PIL import Image as PIL_Image, ImageTk
from xml_to_csv import xml_to_csv
from parse_ids import parse_ids_with_zpaths, parse_zpaths
import errno
import importlib
from operator import xor
from time import strftime, localtime
import traceback
from Tkinter import *
import tk_simple_dialog
from ttk import Combobox
from mtaf.trace import Trace


mtaf_logging.disable_console()
log = mtaf_logging.get_logger('mtaf.inspector')
android_actions = AndroidActions()
re_dumpsys = re.compile('(?ms).*mCurrentFocus=\S+\s+\S+\s+([^/]+)/([^}]+)')
re_apk = re.compile('(?ms).*Packages:.*?versionName=([^\n]+)')
btn_default_bg = '#d9d9d9'
btn_select_bg = '#d97979'
from Queue import Queue


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as _e:
        if _e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


class AutoIncrementer(object):
    # useful for keeping track of row and column assignments when building a GUI;
    # permits adding a widget in the middle of a group without having to reassign
    # the rows or columns in widgets that follow the added widget
    #
    # To Use:
    # - create an instance of AutoIncrementer
    # - to start a named row or column counter, give it an appropriate class member name
    #   and it will be automatically created, returning a zero value
    # - each time the value of the counter is used, it will be incremented by 1
    # - to set the value of the counter, just assign to it
    # - to skip rows or columns, use the "+=" operator
    #
    # Example:
    #   ai = AutoIncrementer()
    #   btn = Button(...)
    #   btn.grid(row=0, column=ai.btn_col)
    #   btn2 = Button(...)
    #   btn2.grid(row=0, column=ai.btn_col)
    #   btn3 = Button(...)
    #   # skip a couple of columns
    #   ai.btn_col += 2
    #   btn3.grid(row=0, column=ai.btn_col)

    def __init__(self):
        self.__dict__['counts'] = {}

    def __setattr__(self, name, value):
        self.__dict__['counts'][name] = value

    def __getattr__(self, name):
        if name not in self.__dict__['counts']:
            self.__dict__['counts'][name] = 0
        prev_count = self.__dict__['counts'][name]
        self.__dict__['counts'][name] += 1
        # print "AutoIncrementer returning %s for name %s" % (prev_count, name)
        return prev_count



class MyDialog(tk_simple_dialog.Dialog):

    list = None
    devices = None

    def body(self, master):

        Label(master, text="Select Device:").grid(row=0)

        self.devices = master.master.master.devices
        self.list = Listbox(master, height=len(self.devices))
        for key in self.devices:
            self.list.insert(END, "%s: %s" % (key, self.devices[key]))
        self.list.grid(row=1)
        return self.list  # initial focus

    def apply(self):
        key = self.list.curselection()[0]
        self.devices = {0: self.devices[key]}


class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    """
    def __init__(self, parent, *_args):
        Frame.__init__(self, parent, *_args)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)

        self.rowconfigure(0, weight=1)
        vscrollbar.grid(sticky='ns', row=0, column=1)

        canvas = Canvas(self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set)

        canvas.grid(sticky='nsew', row=0, column=0)

        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
            if interior.winfo_reqheight() != canvas.winfo_height():
                # update the canvas's height to fit the inner frame
                canvas.config(height=interior.winfo_reqheight())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


class ScrolledLogwin(Frame):
    def __init__(self, parent, height=20, label=None):
        Frame.__init__(self, parent)
        self.log_q = Queue()
        self.parent = parent
        row = 0
        if label is not None:
            self.label = Label(self, text=label)
            self.label.grid(row=row, column=0, columnspan=2, sticky='ew')
            row += 1
        self.txt = Text(self, height=height)
        self.scrollback = 5000
        self.txt.configure(state=DISABLED)
        self.sb = Scrollbar(self, command=self.txt.yview)
        self.txt["yscrollcommand"] = self.sb.set
        self.txt.grid(row=row, column=0, sticky='nsew', padx=2, pady=2)
        self.sb.grid(row=row, column=1, sticky='ns', padx=2, pady=2)
        self.rowconfigure(row, weight=1)
        self.print_buf = ''
        self.read_q()

    def write(self, _txt):
        self.log_q.put(_txt)

    def read_q(self):
        while not self.log_q.empty():
            _txt = self.log_q.get()
            # old_stdout.write(">>%s<<" % _txt)
            log.debug("write: _txt = [%s], len=%d" % (repr(_txt), len(_txt)))
            if len(_txt) > 0 and _txt[-1] == '\n':
                eol = True
            else:
                eol = False
            lines = _txt.strip().split('\n')
            self.txt.configure(state=NORMAL)
            for line in lines[:-1]:
                self.txt.insert('end', line + '\n')
            if len(lines):
                self.txt.insert('end', lines[-1])
            if eol:
                self.txt.insert('end', '\n')
            # self.delete('0.0', 'end - %d lines' % self.scrollback)
            self.txt.see('end')
            # self.update_idletasks()
            self.txt.configure(state=DISABLED)
        self.after(100, self.read_q)


class MenuItem(object):
    def __init__(self, label, action, uses_appium):
        self.label = label
        self.action = action
        self.uses_appium = uses_appium


class MyMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        self.items = {}

    def add_submenu(self, label, menu_items):
        if label in self.items:
            submenu = self.items[label]["menu"]
        else:
            submenu = MyMenu(self)
            self.add_cascade(label=label, menu=submenu)
            self.items[label] = {"menu": submenu, "uses_appium": []}
        for i, item in enumerate(menu_items):
            submenu.add_command(label=item.label, command=item.action)
            self.items[label]["uses_appium"].append(item.uses_appium)

    def enable_items(self, appium_open):
        for label in self.items:
            for i in range(len(self.items[label]["uses_appium"])):
                uses_appium = self.items[label]["uses_appium"][i]
                if appium_open and (uses_appium is True or uses_appium is None):
                    self.items[label]["menu"].entryconfig(i + 1, state=NORMAL)
                elif (not appium_open) and (uses_appium is False or uses_appium is None):
                    self.items[label]["menu"].entryconfig(i + 1, state=NORMAL)
                else:
                    self.items[label]["menu"].entryconfig(i + 1, state=DISABLED)


class AttrFrame(Frame):
    index = None


class BottomFrame(Frame):
    mk_canvas = None


class ButtonFrame(Frame):
    find_frame = None


old_stdout = sys.stdout


class Inspector(Frame):
    menu_cmd_labels = {}

    def __init__(self, parent, gui_cfg):
        Frame.__init__(self, parent, bg="brown")
        self.parent = parent
        self.cfg = gui_cfg
        parent.bind_all("<Button-4>", self.mouse_btn)
        parent.bind_all("<Button-5>", self.mouse_btn)
        self.appium_btns = []
        self.appium_is_open = False
        self.automation_name = None
        self.clickable_element = None
        self.cwin = None
        self.cwin_x = None
        self.cwin_y = None
        self.devices = []
        self.drag_polygon = None
        self.drag_polygon_x1 = None
        self.drag_polygon_x2 = None
        self.drag_polygon_y1 = None
        self.drag_polygon_y2 = None
        self.elem_index = None
        self.elem_indices = []
        self.elems = []
        self.exec_text = StringVar()
        self.find_button = None
        self.find_by_var = None
        self.find_value_var = None
        self.frame_element = None
        self.id_frame_btns = {}
        self.id_frame = None
        self.id_label = None
        self.ids = None
        self.ids = None
        self.im_canvas = None
        self.im_height = None
        self.im_width = None
        self.keycode_name = None
        self.locator_by_values = ['uia_text', 'zpath', 'xpath', 'id', '-android uiautomator']
        self.locators = {}
        self.log_frame = None
        self.menu = None
        self.new_drag_polygon_x1 = None
        self.new_drag_polygon_y1 = None
        self.parent_element = None
        self.polygons = []
        self.rec_file = os.path.join(self.cfg['tmp_dir'], 'inspector_recording.txt')
        self.loc_file = os.path.join(self.cfg['tmp_dir'], 'inspector_locators.json')
        self.rec_frame = None
        self.scroll_elem1_var = StringVar()
        self.scroll_elem2_var = StringVar()
        self.swipe_ms_var = StringVar()
        self.swipe_y1_var = StringVar()
        self.swipe_y2_var = StringVar()
        self.tap_x_var = StringVar()
        self.tap_y_var = StringVar()
        self.text_to_send = None
        self.top_frames = []
        self.use_parent = None
        self.views = {}
        self.within_frame = None
        self.worker_thread = None
        self.zpath_frame_btns = {}
        self.zpath_frame = None
        self.zpath_label = None
        self.zpaths = None

        try:
            with open(self.loc_file, 'r') as f:
                self.locators = json.loads(f.read())
        except (IOError, ValueError):
            pass

        self.btn_frame = self.create_btn_frame()
        self.top_frames.append(self.btn_frame)
        self.top_frames.append(self.create_exec_frame())
        self.top_frames.append(self.create_log_frame())
        self.bottom_frame = self.create_bottom_frame()
        self.top_frames.append(self.bottom_frame)
        self.populate_top_frames()

        sys.stdout = self.log_frame

        self.grid_columnconfigure(0, weight=1)
        self.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')
        for btn in self.appium_btns:
            btn.configure(state=DISABLED)
        self.user_cmds = {
            'Get Current Activity': lambda: self.do_cmd(self.get_current_activity),
            'Restart Appium': lambda: self.do_cmd(self.restart_appium),
            "Get Screenshot Appium": self.get_screenshot_appium,
            "Get Screenshot ADB": self.get_screenshot_adb,
            "Rotate Image": self.rotate_image,
            "Open Appium": lambda: self.do_cmd(self.open_appium),
            "Open Appium (UIAutomator2)": lambda: self.do_cmd(lambda: self.open_appium(automation_name="UIAutomator2")),
            "Get Focused App": lambda: self.do_cmd(self.get_focused_app),
            "Close Appium": lambda: self.do_cmd(self.close_appium)
        }
        self.create_menus(parent)

    def populate_top_frames(self):
        top_frame_row = 0
        for top_frame in self.top_frames:
            if hasattr(top_frame, 'expand_y') and top_frame.expand_y is True:
                self.grid_rowconfigure(top_frame_row, weight=1)
            top_frame.grid_forget()
            top_frame.grid(row=top_frame_row, column=0, padx=4, pady=2, sticky='news')
            top_frame_row += 1

    def record(self, txt):
        self.rec_frame.write(txt + '\n')
        timestamp = strftime('%m_%d_%y-%H_%M_%S', localtime())
        with open(self.rec_file, 'a') as f:
            f.write('%s %s\n' % (timestamp, txt.encode('utf-8')))

    def check_thread(self):
        if self.worker_thread is None:
            return
        # there is a worker thread;
        # if it has died, set to None and enable buttons
        # if it is still alive, call "after" to check again in 100 ms
        if self.worker_thread.is_alive():
            self.after(100, self.check_thread)
            return
        else:
            log.debug("worker thread done: %s" % self.worker_thread.name)
            self.worker_thread = None
            # if do_cmd thread is done, re-enable the menubar dropdowns
            for i in range(len(self.menu.items)):
                self.menu.entryconfig(i + 1, state=NORMAL)
            if self.appium_is_open:
                for btn in self.appium_btns:
                    btn.configure(state=NORMAL)
            # depending on self.appium_is_enabled value, enable/disable dropdown menu items
            self.menu.enable_items(self.appium_is_open)

    def create_bottom_frame(self):
        bottom_frame = BottomFrame(self, bg="tan")
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.mk_canvas = Button(bottom_frame, text="Screenshot", bg=btn_default_bg, command=self.create_cwin)
        bottom_frame.mk_canvas.grid(row=0, column=0, sticky='e', padx=2, pady=2)
        # self.appium_btns.append(bottom_frame.mk_canvas)
        bottom_frame.Quit = Button(bottom_frame, text="Quit", bg=btn_default_bg, command=self.close_appium_and_quit)
        bottom_frame.Quit.grid(row=0, column=1, sticky='e', padx=2, pady=2)
        # bottom_frame.grid(row=self.top_frame_row, column=0, padx=4, pady=4, sticky='news')
        # self.top_frame_row += 1
        return bottom_frame

    def elem_selected(self, elems):
        if self.drag_polygon is None:
            return True
        bw = self.cwin.canvas_borderwidth
        dx1 = min(self.drag_polygon_x1 - bw, self.drag_polygon_x2 - bw)
        dx2 = max(self.drag_polygon_x1 - bw, self.drag_polygon_x2 - bw)
        dy1 = min(self.drag_polygon_y1 - bw, self.drag_polygon_y2 - bw)
        dy2 = max(self.drag_polygon_y1 - bw, self.drag_polygon_y2 - bw)
        for elem in elems:
            x1 = int(elem['x1']) * self.cwin.scale
            x2 = int(elem['x2']) * self.cwin.scale
            y1 = int(elem['y1']) * self.cwin.scale
            y2 = int(elem['y2']) * self.cwin.scale
            if x1 >= dx1 and x2 <= dx2 and y1 >= dy1 and y2 <= dy2:
                return True
        return False

    @Trace(log)
    def create_cwin(self, reuse_image=False):
        #
        # handle problem with unwanted call when button is apparently disabled but still bound to the command.
        # just doing the cget synchronizes the "set disabled" action so the "if" statement returns false;
        # without this a double click on the button causes an exception in "self.cwin_x = self.cwin.winfo_x()"
        # because create_cwin() is called again before the first cwin is rendered
        @Trace(log)
        def disable_screenshot_button():
            if self.bottom_frame.mk_canvas.cget('state') == DISABLED:
                raise Ux("bogus double call to create_cwin()")
            self.bottom_frame.mk_canvas.configure(command=None)
            self.bottom_frame.mk_canvas.configure(state=DISABLED)

        def get_screenshot():
            if self.appium_is_open:
                self.user_cmds['Get Screenshot Appium']()
                self.get_xml_appium()
            else:
                self.user_cmds['Get Screenshot ADB']()
                self.get_xml_adb()

        @Trace(log)
        def enable_screenshot_button():
            self.bottom_frame.mk_canvas.configure(state=NORMAL, command=self.create_cwin)

        @Trace(log)
        def destroy_existing_cwin():
            if self.cwin is not None:
                if self.drag_polygon is not None:
                    self.im_canvas.delete(self.drag_polygon)
                    self.drag_polygon = None
                try:
                    self.cwin_x = self.cwin.winfo_x()
                    self.cwin_y = self.cwin.winfo_y()
                    self.destroy_loc_frames()
                    self.cwin.destroy()
                except TclError:
                    pass
                self.cwin = None

        @Trace(log)
        def create_new_cwin():
            self.cwin = Toplevel(self.parent, bg='tan')
            self.cwin.protocol("WM_DELETE_WINDOW", self.on_canvas_closing)
            image = PIL_Image.open(os.path.join(self.cfg['tmp_dir'], 'inspector.png'))
            self.cwin.scale = 600.0 / max(image.height, image.width)
            self.im_width = int(image.width * self.cwin.scale)
            self.im_height = int(image.height * self.cwin.scale)
            small = image.resize((self.im_width, self.im_height))
            self.cwin.minsize(width=self.im_width, height=self.im_height)
            self.cwin.canvas_borderwidth = 8
            self.im_canvas = Canvas(self.cwin, height=self.im_height, width=self.im_width, bg='darkgrey',
                                    borderwidth=self.cwin.canvas_borderwidth)
            self.im_canvas.photo = ImageTk.PhotoImage(small)
            self.im_canvas.create_image(self.im_width/2 + self.cwin.canvas_borderwidth,
                                        self.im_height/2 + self.cwin.canvas_borderwidth,
                                        image=self.im_canvas.photo)
            self.im_canvas.grid(column=0, row=0)
            self.im_canvas.bind('<Button-1>', self.mouse_btn)
            self.im_canvas.bind('<Button-2>', self.mouse_btn)
            self.im_canvas.bind('<Button-3>', self.mouse_btn)
            self.im_canvas.bind('<Button-4>', self.mouse_btn)
            self.im_canvas.bind('<Button-5>', self.mouse_btn)
            self.im_canvas.bind('<B1-Motion>', self.mouse_btn)
            self.im_canvas.bind('<ButtonRelease-1>', self.mouse_btn)
            self.cwin.btn_frame = Frame(self.cwin)
            self.cwin.btn_frame.rotate = Button(self.cwin.btn_frame, text="rotate image", bg=btn_default_bg,
                                                command=self.user_cmds['Rotate Image'])
            self.cwin.btn_frame.rotate.grid(row=0, column=0)
            self.cwin.btn_frame.grid(row=1, column=0)
            self.cwin.invert_selection = IntVar()
            self.cwin.invert_selection.set(0)
            self.cwin.btn_frame.invert = Checkbutton(self.cwin.btn_frame, text='Invert Selection',
                                                     variable=self.cwin.invert_selection,
                                                     command=self.create_loc_frames)
            self.cwin.btn_frame.invert.grid(row=0, column=1, padx=2, pady=2, sticky='ew')
            self.cwin.rowconfigure(0, weight=1)
            self.create_loc_frames()
            if self.cwin_x is None:
                self.cwin_x = self.parent.winfo_x() + 20
            if self.cwin_y is None:
                self.cwin_y = self.parent.winfo_y() + 20
            width = self.im_canvas.winfo_reqwidth() + self.id_frame.winfo_reqwidth() + self.zpath_frame.winfo_reqwidth()
            height = self.im_canvas.winfo_reqheight() + self.cwin.btn_frame.winfo_reqheight()
            self.cwin.geometry('%dx%d+%d+%d' % (width, height, self.cwin_x, self.cwin_y - 28))
            self.cwin.minsize(width=width, height=height)

        try:
            disable_screenshot_button()
            if reuse_image:
                enable_screenshot_button()
            else:
                get_screenshot()
            destroy_existing_cwin()
            create_new_cwin()
        except Ux as _e:
            print "error creating screenshot window: %s" % _e
            # traceback.print_exc()
        finally:
            enable_screenshot_button()

    @Trace(log)
    def destroy_loc_frames(self):
        if self.id_frame is not None:
            for _id in self.id_frame_btns:
                self.id_frame_btns[_id].grid_forget()
            self.id_frame_btns = {}
            self.id_frame.grid_forget()
            self.id_frame = None
        if self.zpath_frame is not None:
            for zpath in self.zpath_frame_btns:
                self.zpath_frame_btns[zpath].grid_forget()
            self.zpath_frame_btns = {}
            self.zpath_frame.grid_forget()
            self.zpath_frame = None

    @Trace(log)
    def create_loc_frames(self):
        while len(self.polygons):
            self.im_canvas.delete(self.polygons.pop())
        self.destroy_loc_frames()
        self.id_frame = VerticalScrolledFrame(self.cwin)
        self.id_frame_btns = {}
        self.id_frame.grid(column=1, row=0, sticky='n')
        self.zpath_frame = VerticalScrolledFrame(self.cwin)
        self.zpath_frame_btns = {}
        self.zpath_frame.grid(column=2, row=0, sticky='n')
        csv_fullpath = os.path.join(self.cfg['tmp_dir'], 'inspector.csv')
        row = 0
        self.ids = parse_ids_with_zpaths(csv_fullpath)
        self.id_label = Label(self.id_frame.interior, text='IDs', width=30, bg='brown')
        self.id_label.grid(column=0, row=0, stick='ew')
        row += 1
        for _id in self.ids:
            if xor(self.cwin.invert_selection.get(), self.elem_selected(self.ids[_id]['geoms'])):
                self.id_frame_btns[_id] = Button(self.id_frame.interior, text=_id, command=self.get_id_outline_fn(_id),
                                                 bg=btn_default_bg, activebackground=btn_default_bg)
                self.id_frame_btns[_id].grid(row=row, column=0, sticky='w')
                row += 1
        row = 0
        self.zpaths = parse_zpaths(csv_fullpath)
        self.zpath_label = Label(self.zpath_frame.interior, text='zpaths', width=10, bg='brown')
        self.zpath_label.grid(column=0, row=0, sticky='ew')
        row += 1
        zpath_keys = self.zpaths.keys()
        for zpath_key in sorted(zpath_keys):
            if xor(self.cwin.invert_selection.get(), self.elem_selected(self.zpaths[zpath_key]['geoms'])):
                self.zpath_frame_btns[zpath_key] = Button(self.zpath_frame.interior, text=zpath_key,
                                                          command=self.get_zpath_outline_fn(zpath_key),
                                                          bg=btn_default_bg, activebackground=btn_default_bg)
                self.zpath_frame_btns[zpath_key].grid(row=row, column=0, sticky='w')
                row += 1
        self.id_frame.update()
        self.zpath_frame.update()
        self.cwin.update()

    def scale(self, dim):
        return dim * self.cwin.scale + self.cwin.canvas_borderwidth

    def descale(self, dim):
        return int((dim - self.cwin.canvas_borderwidth) / self.cwin.scale)

    def xy_within_zpath(self, x, y, key):
        geom = self.zpaths[key]['geoms'][0]
        x1 = self.scale(geom['x1'])
        x2 = self.scale(geom['x2'])
        y1 = self.scale(geom['y1'])
        y2 = self.scale(geom['y2'])
        return x1 <= x <= x2 and y1 <= y <= y2

    def zpath_area(self, key):
        geom = self.zpaths[key]['geoms'][0]
        return (geom['x2'] - geom['x1']) * (geom['y2'] - geom['y1'])

    def select_smallest(self, x, y):
        clicked_zpaths = []
        for key in self.zpaths.keys():
            if self.xy_within_zpath(x, y, key):
                clicked_zpaths.append(key)
        if len(clicked_zpaths) == 0:
            return None
        else:
            return min(clicked_zpaths, key=self.zpath_area)

    def mouse_btn(self, event):
        # (event.type, event.num) values: (4,1)=press, 6=motion, 5=release, (4,3)=right-press
        # print "type,num = %s(%s),%s(%s)   x = %d,  y = %d" % (event.type, type(event.type),
        #                                     event.num, type(event.num), event.x, event.y)
        if event.type == '4':
            if event.num == 1:
                self.new_drag_polygon_x1 = event.x
                self.new_drag_polygon_y1 = event.y
            elif event.num == 3:
                if self.drag_polygon is not None:
                    self.im_canvas.delete(self.drag_polygon)
                    self.drag_polygon = None
                    self.create_loc_frames()
            elif event.num == 4 or event.num == 5:
                locked = False
                w = event.widget
                while True:
                    if w == self.im_canvas:
                        locked = True
                        break
                    if hasattr(w, 'master'):
                        w = w.master
                    if w == self or w == self.parent:
                        break
                if not locked:
                    w = event.widget
                    while True:
                        if hasattr(w, 'yview_scroll'):
                            if event.num == 4:
                                w.yview_scroll(-1, UNITS)
                            else:
                                w.yview_scroll(1, UNITS)
                            break
                        if hasattr(w, 'master'):
                            w = w.master
                        else:
                            break
        elif event.type == '5':
            x1 = self.new_drag_polygon_x1
            y1 = self.new_drag_polygon_y1
            x2 = event.x
            y2 = event.y
            if x2 != x1 and y2 != y1:
                self.create_loc_frames()
            else:
                # click/release with no drag, select and outline smallest element and put its zpath in the value
                # combobox
                print "clicked: (image) %s,%s  (device) %s,%s" % (x1, y1, self.descale(x1), self.descale(y1))
                zpath_key = self.select_smallest(x1, y1)
                if zpath_key is None:
                    print "No element reported at location: (image) %s,%s  (device) %s,%s" % (
                        x1, y1, self.descale(x1), self.descale(y1))
                else:
                    self.get_zpath_outline_fn(zpath_key)()
        elif event.type == '6':
            x1 = self.new_drag_polygon_x1
            y1 = self.new_drag_polygon_y1
            x2 = event.x
            y2 = event.y
            if x2 != x1 and y2 != y1:
                if self.drag_polygon is not None:
                    self.im_canvas.delete(self.drag_polygon)
                    self.drag_polygon = None
                self.drag_polygon_x1 = self.new_drag_polygon_x1
                self.drag_polygon_y1 = self.new_drag_polygon_y1
                self.drag_polygon_x2 = x2
                self.drag_polygon_y2 = y2
                self.drag_polygon = self.im_canvas.create_polygon(x1, y1, x1, y2, x2, y2, x2, y1, outline='blue',
                                                                  fill='', width=2)

        return 'break'

    def get_id_outline_fn(self, id_name):
        def f():
            self.outline_elems(id_name, loc_type='id')
            self.find_by_var.set('id')
            self.find_value_var.set(id_name)
        return f

    def get_zpath_outline_fn(self, zpath):
        def f():
            self.outline_elems(zpath, loc_type='zpath')
            self.find_by_var.set('zpath')
            self.find_value_var.set(zpath)
        return f

    def on_canvas_closing(self):
        self.im_canvas = None
        self.id_frame_btns = {}
        self.id_frame = None
        self.zpath_frame_btns = {}
        self.zpath_frame = None
        self.drag_polygon = None
        self.cwin.destroy()
        # self.bottom_frame.mk_canvas.configure(state=NORMAL)

    def create_log_frame(self):
        pw = PanedWindow(self, orient=VERTICAL, bg='brown')
        self.log_frame = ScrolledLogwin(pw, height=self.cfg['log_window_height'], label='standard output')
        self.log_frame.grid_columnconfigure(0, weight=1)
        pw.add(self.log_frame, stretch='always')
        rec_frame = ScrolledLogwin(pw, height=self.cfg['log_window_height'], label='recorded text')
        self.rec_frame = rec_frame
        rec_frame.grid_columnconfigure(0, weight=1)
        pw.add(rec_frame, stretch='always')
        pw.expand_y = True
        return pw

    @staticmethod
    def defocus(event):
        event.widget.selection_clear()

    def create_exec_frame(self):
        exec_frame = Frame(self, bg="brown")
        exec_frame.btn = Button(exec_frame, text="exec:", command=lambda: self.do_cmd(self.exec_code),
                                bg=btn_default_bg, state=NORMAL)
        exec_frame.btn.grid(row=0, column=0)
        exec_frame.entry = Entry(exec_frame, textvariable=self.exec_text)
        exec_frame.entry.grid(row=0, column=1, sticky='news')
        exec_frame.columnconfigure(1, weight=1)
        # exec_frame.grid(row=self.top_frame_row, column=0, padx=4, pady=4, sticky='news')
        # self.top_frame_row += 1
        return exec_frame

    def exec_code(self):
        text = self.exec_text.get()
        try:
            exec text
        except Exception as _e:
            print "exec raised exception: %s" % _e

    def callback(self, *_args):
        self.find_button.configure(bg=btn_select_bg, activebackground=btn_select_bg)

    def create_btn_frame(self):
        ai = AutoIncrementer()
        btn_frame = ButtonFrame(self, bg="brown")

        btn_frame.find_frame = Frame(btn_frame, bg='tan')
        btn_frame.find_frame.grid(row=ai.bf_row, column=0, sticky='ew', padx=2, pady=2)
        btn = Button(btn_frame.find_frame, text="find elements:", bg=btn_default_bg,
                     command=lambda: self.do_cmd(self.find_elements), state=DISABLED)
        self.find_button = btn
        self.appium_btns.append(btn)
        btn.grid(row=0, column=ai.ffr, padx=2, pady=2, sticky='n')

        self.find_by_var = StringVar()
        self.find_by_var.set(self.locator_by_values[0])
        btn_frame.find_frame.by = Combobox(btn_frame.find_frame, width=16, state='readonly', takefocus=False,
                                           values=self.locator_by_values, textvariable=self.find_by_var)
        self.appium_btns.append(btn_frame.find_frame.by)
        btn_frame.find_frame.by.bind('<<ComboboxSelected>>', self.update_find_widgets)
        btn_frame.find_frame.by.bind("<FocusIn>", self.defocus)
        btn_frame.find_frame.by.grid(row=0, column=ai.ffr, padx=2, pady=2, sticky='n')

        btn_frame.find_frame.cbs = Frame(btn_frame.find_frame, bg='tan')
        btn_frame.find_frame.cbs.grid(row=0, column=ai.ffr, padx=2, pady=2, sticky='n')

        btn_frame.find_frame.loc = Frame(btn_frame.find_frame)
        btn_frame.find_frame.loc.grid_columnconfigure(0, weight=1)
        loc_column = ai.ffr
        btn_frame.find_frame.loc.grid(row=0, column=loc_column, padx=2, pady=2, sticky='new')
        btn_frame.find_frame.grid_columnconfigure(loc_column, weight=1)

        self.use_parent = IntVar()
        self.use_parent.set(0)
        btn_frame.find_frame.cbs.use_parent = Checkbutton(btn_frame.find_frame.cbs, text='from Parent',
                                                          variable=self.use_parent, state=DISABLED)
        btn_frame.find_frame.cbs.use_parent.grid(row=0, column=0, padx=2, pady=2, sticky='ew')

        self.within_frame = IntVar()
        self.within_frame.set(0)
        btn_frame.find_frame.cbs.within_frame = Checkbutton(btn_frame.find_frame.cbs, text='within frame',
                                                        variable=self.within_frame, state=DISABLED)
        btn_frame.find_frame.cbs.within_frame.grid(row=1, column=0, padx=2, pady=2, sticky='ew')

        self.find_value_var = StringVar()
        self.find_value_var.trace('w', self.callback)
        btn_frame.find_frame.loc.value = Combobox(btn_frame.find_frame.loc, width=60,
                                                  values=self.get_filtered_locator_keys(),
                                                  textvariable=self.find_value_var)
        self.appium_btns.append(btn_frame.find_frame.loc.value)
        btn_frame.find_frame.loc.value.bind('<<ComboboxSelected>>', self.update_find_frame)
        btn_frame.find_frame.loc.value.bind("<FocusIn>", self.defocus)
        btn_frame.find_frame.loc.hsb = Scrollbar(btn_frame.find_frame.loc, orient=HORIZONTAL,
                                                 command=btn_frame.find_frame.loc.value.xview)
        btn_frame.find_frame.loc.value["xscrollcommand"] = btn_frame.find_frame.loc.hsb.set
        btn_frame.find_frame.loc.value.grid(row=0, column=0, padx=2, pady=0, sticky='ew')
        btn_frame.find_frame.loc.hsb.grid(row=1, column=0, sticky='ew')

        btn_frame.attr_frame = AttrFrame(btn_frame, bg='tan')
        btn_frame.attr_frame.grid(row=ai.bf_row, column=0, sticky='ew', padx=2, pady=2)
        btn_frame.attr_frame.index_label = Label(btn_frame.attr_frame, text="select elem:", bg="tan")
        self.appium_btns.append(btn_frame.attr_frame.index_label)
        btn_frame.attr_frame.index_label.grid(row=0, column=ai.atf_r1, padx=2, pady=2, sticky='e')
        self.elem_index = StringVar()
        self.elem_index.set('')
        btn_frame.attr_frame.index = Combobox(btn_frame.attr_frame, width=6, values=[], textvariable=self.elem_index)
        self.appium_btns.append(btn_frame.attr_frame.index)
        btn_frame.attr_frame.index.grid(row=0, column=ai.atf_r1, padx=2, pady=2, sticky='e')
        btn = Button(btn_frame.attr_frame, text="get elem attributes", bg=btn_default_bg, command=self.get_elem_attrs,
                     state=DISABLED, padx=1)
        self.appium_btns.append(btn)
        btn.grid(row=0, column=ai.atf_r1, padx=2, pady=2)
        btn = Button(btn_frame.attr_frame, text="get elem color", bg=btn_default_bg, command=self.get_elem_color,
                     state=DISABLED, padx=1)
        self.appium_btns.append(btn)
        btn.grid(row=0, column=ai.atf_r1, padx=2, pady=2)
        btn = Button(btn_frame.attr_frame, text="click elem", bg=btn_default_bg, command=self.click_element,
                     state=DISABLED, padx=1)
        self.appium_btns.append(btn)
        btn.grid(row=0, column=ai.atf_r1, padx=2, pady=2)
        btn = Button(btn_frame.attr_frame, text="set parent", bg=btn_default_bg, command=self.set_parent,
                     state=DISABLED, padx=1)
        self.appium_btns.append(btn)
        btn.grid(row=0, column=ai.atf_r1, padx=2, pady=2)
        btn = Button(btn_frame.attr_frame, text="set frame", bg=btn_default_bg, command=self.set_frame,
                     state=DISABLED, padx=1)
        self.appium_btns.append(btn)
        btn.grid(row=0, column=ai.atf_r1, padx=2, pady=2)
        btn = Button(btn_frame.attr_frame, text="clear elem", bg=btn_default_bg, command=self.clear_element,
                     state=DISABLED, padx=1)
        self.appium_btns.append(btn)
        btn.grid(row=1, column=ai.atf_r2, padx=2, pady=2)
        btn = Button(btn_frame.attr_frame, text="input text", bg=btn_default_bg, command=self.input_text,
                     state=DISABLED, padx=1)
        self.appium_btns.append(btn)
        btn.grid(row=1, column=ai.atf_r2, padx=2, pady=2)
        frame = Frame(btn_frame.attr_frame, bg='tan')
        frame.columnconfigure(0, weight=1)
        self.text_to_send = StringVar()
        entry = Entry(frame, textvariable=self.text_to_send, state=DISABLED)
        self.appium_btns.append(entry)
        entry.grid(row=0, column=0, sticky='ew')
        btn = Button(frame, text='X', command=self.clear_text_to_send, padx=0, pady=0)
        btn.grid(row=0, column=1)
        self.appium_btns.append(btn)
        frame.grid(row=1, column=ai.atf_r2, padx=2, pady=2, columnspan=3, sticky='ew')
        btn = Button(btn_frame.attr_frame, text="input ENTER", bg=btn_default_bg, command=self.input_enter,
                     state=DISABLED, padx=1)
        self.appium_btns.append(btn)
        ai.atf_r2 += 2
        btn.grid(row=1, column=ai.atf_r2, columnspan=2, padx=2, pady=2, sticky='w')

        btn_frame.xy_frame = Frame(btn_frame, bg='tan')
        btn_frame.xy_frame.grid(row=ai.bf_row, column=0, sticky='ew', padx=2, pady=2)

        btn_frame.xy_frame.tap_frame = Frame(btn_frame.xy_frame, bg='tan')
        btn_frame.xy_frame.tap_frame.grid(row=0, column=ai.xyf, sticky='w', padx=2, pady=2)

        btn = Button(btn_frame.xy_frame.tap_frame, text="tap:", bg=btn_default_bg, command=self.tap_xy, state=DISABLED)
        self.appium_btns.append(btn)
        btn.grid(row=0, column=ai.tap, padx=2, pady=2, sticky='w')

        lbl = Label(btn_frame.xy_frame.tap_frame, text="x:", bg='tan')
        self.appium_btns.append(lbl)
        lbl.grid(row=0, column=ai.tap)
        x_entry = Entry(btn_frame.xy_frame.tap_frame, width=4, textvariable=self.tap_x_var)
        self.appium_btns.append(x_entry)
        x_entry.grid(row=0, column=ai.tap, padx=2, pady=2, sticky='w')

        lbl = Label(btn_frame.xy_frame.tap_frame, text="y:", bg='tan')
        self.appium_btns.append(lbl)
        lbl.grid(row=0, column=ai.tap)
        y_entry = Entry(btn_frame.xy_frame.tap_frame, width=4, textvariable=self.tap_y_var)
        self.appium_btns.append(y_entry)
        y_entry.grid(row=0, column=ai.tap, padx=2, pady=2, sticky='w')

        btn_frame.xy_frame.swipe_frame = Frame(btn_frame.xy_frame, bg='tan')
        btn_frame.xy_frame.swipe_frame.grid(row=0, column=ai.xyf, sticky='w', padx=60, pady=2)

        btn = Button(btn_frame.xy_frame.swipe_frame, text="swipe:", bg=btn_default_bg, command=self.swipe,
                     state=DISABLED)
        self.appium_btns.append(btn)
        btn.grid(row=0, column=ai.swp, padx=2, pady=2, sticky='w')

        lbl = Label(btn_frame.xy_frame.swipe_frame, text="x:", bg='tan')
        self.appium_btns.append(lbl)
        lbl.grid(row=0, column=ai.swp)
        entry = Entry(btn_frame.xy_frame.swipe_frame, width=4, textvariable=self.swipe_y1_var)
        self.appium_btns.append(entry)
        entry.grid(row=0, column=ai.swp, padx=2, pady=2, sticky='w')

        lbl = Label(btn_frame.xy_frame.swipe_frame, text="y:", bg='tan')
        self.appium_btns.append(lbl)
        lbl.grid(row=0, column=ai.swp)
        entry = Entry(btn_frame.xy_frame.swipe_frame, width=4, textvariable=self.swipe_y2_var)
        self.appium_btns.append(entry)
        entry.grid(row=0, column=ai.swp, padx=2, pady=2, sticky='w')

        lbl = Label(btn_frame.xy_frame.swipe_frame, text="ms:", bg='tan')
        self.appium_btns.append(lbl)
        lbl.grid(row=0, column=ai.swp)
        entry = Entry(btn_frame.xy_frame.swipe_frame, width=4, textvariable=self.swipe_ms_var)
        self.swipe_ms_var.set(100)
        self.appium_btns.append(entry)
        entry.grid(row=0, column=ai.swp, padx=2, pady=2, sticky='w')
        btn_frame.xy_frame.scroll_frame = Frame(btn_frame.xy_frame, bg='tan')
        btn_frame.xy_frame.scroll_frame.grid(row=0, column=ai.xyf, sticky='w', padx=2, pady=2)

        btn = Button(btn_frame.xy_frame.scroll_frame, text="scroll:", bg=btn_default_bg, command=self.scroll,
                     state=DISABLED)
        self.appium_btns.append(btn)
        btn.grid(row=0, column=ai.scrl, padx=2, pady=2, sticky='w')

        lbl = Label(btn_frame.xy_frame.scroll_frame, text="elem1:", bg='tan')
        self.appium_btns.append(lbl)
        lbl.grid(row=0, column=ai.scrl)
        btn_frame.xy_frame.scroll_frame.elem1 = Combobox(btn_frame.xy_frame.scroll_frame, width=6, values=[],
                                                         textvariable=self.scroll_elem1_var)
        self.appium_btns.append(btn_frame.xy_frame.scroll_frame.elem1)
        btn_frame.xy_frame.scroll_frame.elem1.grid(row=0, column=ai.scrl, padx=2, pady=2, sticky='w')

        lbl = Label(btn_frame.xy_frame.scroll_frame, text="elem2:", bg='tan')
        self.appium_btns.append(lbl)
        lbl.grid(row=0, column=ai.scrl)
        btn_frame.xy_frame.scroll_frame.elem2 = Combobox(btn_frame.xy_frame.scroll_frame, width=6, values=[],
                                                         textvariable=self.scroll_elem2_var)
        self.appium_btns.append(btn_frame.xy_frame.scroll_frame.elem2)
        btn_frame.xy_frame.scroll_frame.elem2.grid(row=0, column=ai.scrl, padx=2, pady=2, sticky='w')

        btn_frame.grid_columnconfigure(0, weight=1)
        return btn_frame

    def clear_text_to_send(self):
        self.text_to_send.set('')

    def update_find_frame(self, event):
        value = self.find_value_var.get().split(':', 1)[1]
        self.find_value_var.set(value)
        if value in self.locators:
            self.find_by_var.set(self.locators[value]["by"])
            self.update_find_widgets(None)
            if self.parent_element is not None:
                self.use_parent.set(self.locators[self.find_value_var.get()]["use_parent"])
            else:
                self.use_parent.set(0)

    def make_menu_items(self, menu_items):
        return [MenuItem(item['label'], self.user_cmds[item['label']], item['uses_appium']) for item in menu_items]

    def create_menus(self, parent):
        menu_items = {
            'Appium Actions': [
                {'label': 'Get Current Activity', 'uses_appium': True},
                {'label': 'Restart Appium', 'uses_appium': True}
            ],
            'ADB Actions': [
                {'label': 'Get Focused App', 'uses_appium': False}
            ],
            'Appium Session': [
                {'label':'Open Appium', 'uses_appium': False},
                {'label':'Open Appium (UIAutomator2)', 'uses_appium': False},
                {'label':'Close Appium', 'uses_appium': True}
            ]
        }
        self.menu = MyMenu(parent)
        for menu_label in menu_items:
            self.menu.add_submenu(menu_label, self.make_menu_items(menu_items[menu_label]))
        # depending on self.appium_is_enabled value, enable/disable dropdown menu items
        self.menu.enable_items(self.appium_is_open)
        parent.config(menu=self.menu)

    def do_cmd(self, cmd):
        if self.worker_thread is not None:
            print "worker thread busy: %s" % cmd.__name__
        else:
            for btn in self.appium_btns:
                btn.configure(state=DISABLED)
            # disable the menubar dropdowns while thread is running
            for i in range(len(self.menu.items)):
                    self.menu.entryconfig(i + 1, state=DISABLED)
            pass
            self.update_idletasks()
            # sleep(5)
            self.worker_thread = threading.Thread(target=cmd, name=cmd.__name__)
            self.worker_thread.start()
            log.debug("worker thread started: %s" % cmd.__name__)
            self.after(100, self.check_thread)

    def close_appium_and_quit(self):
        if self.appium_is_open:
            print "trying to close appium"
            self.close_appium()
        try:
            os.mkdir(os.path.dirname(self.loc_file))
        except OSError:
            pass
        with open(self.loc_file, 'w') as f:
            f.write(json.dumps(self.locators, sort_keys=True, indent=4, separators=(',', ': ')))
        self.parent.destroy()

    def tap_xy(self):
        try:
            x = int(self.tap_x_var.get())
            y = int(self.tap_y_var.get())
        except (ValueError, TypeError):
            print "Can't execute tap with x='%s', y='%s'" % (self.tap_x_var.get(), self.tap_y_var.get())
        else:
            print "Executing tap([(%d, %d)])..." % (x, y),
            android_actions.tap([(x, y)])
            print "Done"

    def swipe(self):
        try:
            y1 = int(self.swipe_y1_var.get())
            y2 = int(self.swipe_y2_var.get())
            ms = int(self.swipe_ms_var.get())
        except (ValueError, TypeError):
            print "Can't execute swipe with y1='%s', y2='%s'" % (self.swipe_y1_var.get(), self.swipe_y2_var.get())
        else:
            print "Executing swipe([(300, %d, 300, %d, %d)])..." % (y1, y2, ms),
            android_actions.swipe(300, y1, 300, y2, ms)
            print "Done"

    def scroll(self):
        try:
            elem1 = int(self.scroll_elem1_var.get())
            elem2 = int(self.scroll_elem2_var.get())
        except (ValueError, TypeError):
            print "Can't execute scroll with elem1='%s', elem2='%s'" % (self.scroll_elem1_var.get(),
                                                                             self.scroll_elem1_var.get())
        else:
            print "Executing scroll from elem %s to elem %s..." % (elem1, elem2)
            android_actions.short_press_scroll(self.elems[elem1], self.elems[elem2])
            print "Done"

    def update_find_widgets(self, event):
        find_by = self.find_by_var.get()
        if (find_by == 'id') and self.parent_element is not None:
            self.btn_frame.find_frame.cbs.use_parent.configure(state=NORMAL)
        else:
            self.btn_frame.find_frame.cbs.use_parent.configure(state=DISABLED)
            self.use_parent.set(0)
        if find_by[-11:] == 'locator_all' and self.frame_element is not None:
            self.btn_frame.find_frame.cbs.within_frame.configure(state=NORMAL)
        else:
            self.btn_frame.find_frame.cbs.within_frame.configure(state=DISABLED)

    def find_elements_by_locator_name(self, locator):
        by = locator['by']
        value = locator['value']
        elems = []
        try:
            if by[-3:] == 'all':
                view_name = by[:-12]
                # self.record("finding elements in view %s using locator %s" % (view_name, value))
                elems = getattr(self.views[view_name].all, value)
            else:
                view_name = by[:-8]
                # self.record("finding elements in view %s using locator %s" % (view_name, value))
                elems = [getattr(self.views[view_name], value)]
        except Ux as _e:
            print _e.message
        if self.within_frame.get():
            return filter(get_filter('within_frame', frame=self.frame_element), elems)
        else:
            if elems == [None]:
                return []
            return elems

    def find_elements_with_driver(self, locator):
        by = locator['by']
        value = locator['value']
        if by == 'zpath':
            value = expand_zpath(value)
            by = 'xpath'
            print "xpath = %s" % value
        elif by == 'uia_text':
            by = '-android uiautomator'
            value = 'new UiSelector().text("%s")' % value
        if self.use_parent.get():
            return self.parent_element.find_elements(by, value)
        else:
            return android_actions.driver.find_elements(by, value)

    def get_filtered_locator_keys(self):
        sorted_keys = sorted(self.locators.keys(), key=lambda x: self.locators[x]['time'], reverse=True)
        filtered_keys = filter(lambda x: self.locators[x]['by'] in self.locator_by_values, sorted_keys)
        return ["%s:%s" % (self.locators[key]['by'], key) for key in filtered_keys]

    def update_locator_list(self, locator=None):
        self.btn_frame.find_frame.by.configure(values=self.locator_by_values)
        # - find_elements passes in a locator value, which is added to self.locators
        # - a plugin that adds values to self.locator_by_values will need to call this method with no locator argument
        # - the find element "by" combobox will be updated and the "value" combobox locator list will be filtered,
        #   according  to the current value of self.locator_by_values
        if locator is not None:
            if locator['value'] in self.locators.keys():
                self.locators[locator['value']]['time'] = time()
            else:
                self.locators[locator['value']] = {"by": locator['by'], "use_parent": locator['use_parent'],
                                                   "time": time()}
        sorted_keys = sorted(self.locators.keys(), key=lambda x: self.locators[x]['time'], reverse=True)
        # only keep 50 locators
        for key in sorted_keys[50:]:
            del self.locators[key]
            sorted_keys.pop()
        self.btn_frame.find_frame.loc.value.configure(value=self.get_filtered_locator_keys())

    def find_elements(self):
        print "finding elements...",
        self.find_button.configure(bg=btn_default_bg)
        locator = {
            'by': self.find_by_var.get(),
            'value': self.find_value_var.get(),
            'use_parent': self.use_parent.get()
        }
        self.record("finding elements with locator %s" % locator)
        self.update_locator_list(locator)
        if locator['by'][-7:] == 'locator' or locator['by'][-11:] == 'locator_all':
            self.elems = self.find_elements_by_locator_name(locator)
        else:
            try:
                self.elems = self.find_elements_with_driver(locator)
            except WebDriverException as _e:
                print str(_e).strip()
                return
            # keep frame element setting if using "by" value ending in '*_locator'
            self.frame_element = None
            self.within_frame.set(0)
        _msg = "%s element%s found" % (len(self.elems), '' if len(self.elems) == 1 else 's')
        print _msg
        self.record(_msg)
        elem_indices = [str(i) for i in range(len(self.elems))]
        self.btn_frame.attr_frame.index.configure(values=elem_indices)
        self.btn_frame.xy_frame.scroll_frame.elem1.configure(values=elem_indices)
        self.btn_frame.xy_frame.scroll_frame.elem2.configure(values=elem_indices)
        self.scroll_elem1_var.set('')
        self.scroll_elem2_var.set('')
        if len(elem_indices):
            self.elem_index.set('0')
        else:
            self.elem_index.set('')
        self.parent_element = None
        self.btn_frame.find_frame.cbs.use_parent.configure(state=DISABLED)
        self.use_parent.set(0)
        self.update_find_widgets(None)

    def get_elem_attrs(self):
        text_index = self.elem_index.get()
        if text_index == '':
            return
        index = int(text_index)
        elem = self.elems[index]
        self.record('getting element %d attributes' % index)
        print "\nattributes for element %d" % index
        print "  %10s: %s" % ("location_in_view", elem.location_in_view)
        print "  %10s: %s" % ("location", elem.location)
        print "  %10s: %s" % ("size", elem.size)
        for attr in ['name', 'contentDescription', 'text', 'className', 'resourceId', 'enabled', 'checkable', 'checked',
                     'clickable', 'focusable', 'focused', 'longClickable', 'scrollable', 'selected', 'displayed']:
            try:
                _msg = "  %10s: %s" % (attr, elem.get_attribute(attr))
            except NoSuchElementException:
                _msg = "NoSuchElementException running elem.get_attribute(%s)" % attr
                log.debug(_msg)
            print _msg
            self.record(_msg)
        self.draw_outlines([{
            "x1": int(elem.location['x']),
            "y1": int(elem.location['y']),
            "x2": int(elem.location['x']) + int(elem.size['width']),
            "y2": int(elem.location['y']) + int(elem.size['height'])
        }])

    def outline_elems(self, locator_name, loc_type=None):
        if hasattr(self, 'im_canvas') and self.im_canvas is not None:
            if loc_type == 'zpath':
                locator = self.zpaths[locator_name]
                geoms = locator['geoms']
                for _id in self.id_frame_btns:
                    btn = self.id_frame_btns[_id]
                    if locator['id'] == _id:
                        btn.configure(bg=btn_select_bg, activebackground=btn_select_bg)
                    else:
                        btn.configure(bg=btn_default_bg, activebackground=btn_default_bg)
                for zpath in self.zpath_frame_btns:
                    btn = self.zpath_frame_btns[zpath]
                    if zpath == locator_name:
                        btn.configure(bg=btn_select_bg, activebackground=btn_select_bg)
                    else:
                        btn.configure(bg=btn_default_bg, activebackground=btn_default_bg)
            else:
                locator = self.ids[locator_name]
                geoms = locator['geoms']
                if len(locator['zpath']) > 1:
                    print "id %s matched %d elements" % (locator_name, len(locator['zpath']))
                for zpath in self.zpath_frame_btns:
                    btn = self.zpath_frame_btns[zpath]
                    if zpath in locator['zpath']:
                        btn.configure(bg=btn_select_bg, activebackground=btn_select_bg)
                    else:
                        btn.configure(bg=btn_default_bg, activebackground=btn_default_bg)
                for _id in self.id_frame_btns:
                    btn = self.id_frame_btns[_id]
                    if _id == locator_name:
                        btn.configure(bg=btn_select_bg, activebackground=btn_select_bg)
                    else:
                        btn.configure(bg=btn_default_bg, activebackground=btn_default_bg)
            self.draw_outlines(geoms)

    def draw_outlines(self, geoms):
        if self.im_canvas is not None:
            while len(self.polygons):
                self.im_canvas.delete(self.polygons.pop())
            for geom in geoms:
                x1 = self.scale(geom["x1"]) + 2
                y1 = self.scale(geom["y1"]) + 2
                y2 = self.scale(geom["y2"]) - 1
                x2 = self.scale(geom["x2"]) - 1
                # print "calling create_polygon(%d, %d, %d, %d, %d, %d, %d, %d)" %
                #            (x1, y1, x1, y2, x2, y2, x2, y1)
                self.polygons.append(self.im_canvas.create_polygon(x1, y1, x1, y2, x2, y2, x2, y1, outline='red',
                                                                   fill='', width=2))

    def get_elem_color(self):
        text_index = self.elem_index.get()
        if text_index == '':
            return
        index = int(text_index)
        elem = self.elems[index]
        android_actions.get_screenshot_as_file('inspector.png')
        color = android_actions.get_element_color_and_count_using_folder(self.cfg['tmp_dir'], 'inspector', elem,
                                                                         cropped_suffix='', color_list_index=0)
        print "first color and count: %s" % color
        self.record("first color and count: %s" % color)
        color = android_actions.get_element_color_and_count_using_folder(self.cfg['tmp_dir'], 'inspector', elem,
                                                                         cropped_suffix='', color_list_index=1)
        print "second color and count: %s" % color
        self.record("second color and count: %s" % color)
        color = android_actions.get_element_color_and_count_using_folder(self.cfg['tmp_dir'], 'inspector', elem,
                                                                         cropped_suffix='', color_list_index=2)
        self.record("third color and count: %s" % color)

    def click_element(self):
        text_index = self.elem_index.get()
        if text_index == '':
            return
        index = int(text_index)
        self.record('clicking element %d' % index)
        self.elems[index].click()

    def clear_element(self):
        text_index = self.elem_index.get()
        if text_index == '':
            return
        index = int(text_index)
        self.record('clearing element %d' % index)
        self.elems[index].clear()

    def set_parent(self):
        text_index = self.elem_index.get()
        if text_index == '':
            return
        index = int(text_index)
        self.record('setting element %d as parent' % index)
        self.parent_element = self.elems[index]
        self.update_find_widgets(None)

    def set_frame(self):
        text_index = self.elem_index.get()
        if text_index == '':
            return
        index = int(text_index)
        self.record('setting element %d as frame' % index)
        self.frame_element = self.elems[index]
        self.update_find_widgets(None)

    def input_text(self):
        text_index = self.elem_index.get()
        if text_index == '':
            return
        index = int(text_index)
        text = self.text_to_send.get()
        self.record('sending "%s" to element %d' % (text, index))
        try:
            elem = self.elems[index].clear()
            terms = text.split('\\n')
            while len(terms):
                value = terms.pop(0)
                if len(value):
                    elem.set_value(value)
                if len(terms):
                    elem.send_keys('\n')
        except BaseException as _e:
            print "got exception %s" % _e
        self.update_find_widgets(None)

    def input_enter(self):
        text_index = self.elem_index.get()
        if text_index == '':
            return
        index = int(text_index)
        self.record('sending \\n to element %d' % index)
        try:
            self.elems[index].send_keys('\n')
        except BaseException as _e:
            print "got exception %s" % _e
        self.update_find_widgets(None)

    def open_appium(self, max_attempts=1, retry_seconds=5, automation_name="Appium"):
        attempts = 0
        print "Opening Appium (%s)..." % automation_name,
        while attempts < max_attempts:
            try:
                if attempts > 0:
                    print "\n(retrying) Opening Appium...",
                self.update_idletasks()
                android_actions.open_appium(automation_name=automation_name)
                self.appium_is_open = True
                self.automation_name = automation_name
                self.update_find_widgets(None)
                print "Done"
                break
            except BaseException as _e:
                print "Error trying to open Appium: %s" % _e
            finally:
                attempts += 1
            if attempts < max_attempts:
                sleep(retry_seconds)
        else:
            print "attempted to open_appium %d time(s)\n" % attempts

    def close_appium(self):
        print "Closing Appium...",
        try:
            android_actions.close_appium()
            self.appium_is_open = False
            self.automation_name = None
            print "Done"
        except Ux as e:
            print e

    @staticmethod
    def log_action(spud_serial, action):
        (reply, elapsed, groups) = spud_serial.do_action(action)
        lines = reply.split('\n')
        log.debug('cmd: %s\nelapsed: [%5.3f s]  \necho: "%s"\n' %
                  (action['cmd'], elapsed, repr(lines[0].encode('string_escape'))))
        for line in lines[1:]:
            log.debug(' '*7 + line.encode('string_escape'))

    def restart_appium(self):
        print "--> Restarting Appium"
        if not self.appium_is_open:
            raise Ux("called restart_appium when appium was not open")
        # calling close_appium will set self.automation_name to none, so save it
        automation_name = self.automation_name
        self.close_appium()
        self.open_appium(automation_name=automation_name)
        print "--> Done"

    def get_focused_app(self, quiet=False):
        if not quiet:
            print "Getting Focused App...",
        package = 'Unknown'
        activity = 'Unknown'
        apk = 'Unknown'
        self.devices = android_actions.adb.get_devices()
        if len(self.devices) > 0:
            if len(self.devices) > 1:
                id = MyDialog(self)
                print "MyDialog returned %s" % id
                android_actions.adb.set_target_by_id(id)
            output = android_actions.adb.run_cmd('shell dumpsys window windows')
            if re_dumpsys.match(output):
                (package, rest) = re_dumpsys.match(output).groups()
                activity = rest[(len(package) + 1):]
                output = android_actions.adb.run_cmd('shell dumpsys package %s' % package)
                if re_apk.match(output):
                    apk = re_apk.match(output).group(1)
        if not quiet:
            print
            print "Package: " + package
            print "Activity: " + activity
            print "apk: " + apk
            print "Done"
        return package

    def get_xml_appium(self):
        print "Getting XML and CSV...",
        xml = android_actions.driver.page_source
        xml_fullpath = os.path.join(self.cfg['tmp_dir'], 'inspector.xml')
        csv_fullpath = os.path.join(self.cfg['tmp_dir'], 'inspector.csv')
        log.info("saving xml %s" % xml_fullpath)
        with open(xml_fullpath, 'w') as _f:
            _f.write(xml.encode('utf8'))
        xml_to_csv(xml_fullpath, csv_fullpath)
        print "Done"

    def get_xml_adb(self):
        print "Getting XML and CSV..."
        xml_path = os.path.join(self.cfg['tmp_dir'], 'inspector.xml')
        csv_path = os.path.join(self.cfg['tmp_dir'], 'inspector.csv')
        try:
            os.remove(xml_path)
            os.remove(csv_path)
        except OSError:
            pass
        android_actions.adb.run_cmd('shell rm /sdcard/window_dump.xml')
        android_actions.adb.run_cmd('shell uiautomator dump')
        android_actions.adb.run_cmd('pull /sdcard/window_dump.xml')
        log.info("saving xml %s" % xml_path)
        try:
            os.rename('window_dump.xml', xml_path)
        except OSError as e:
            raise Ux("No xml file found, is Android device connected?")
        else:
            xml_to_csv(xml_path, csv_path)

        print "Done"

    def get_screenshot_appium(self):
        print "Getting Screenshot using Appium...",
        img_path = os.path.join(self.cfg['tmp_dir'], 'inspector.png')
        log.debug("saving screenshot to %s" % img_path)
        android_actions.get_screenshot_as_file(img_path)
        print "Done"

    def get_screenshot_adb(self):
        print "Getting Screenshot using ADB...",
        devices = android_actions.adb.get_devices()
        if len(devices) == 0:
            print "no device found"
        else:
            print "%d devices found" % len(devices)
            img_path = os.path.join(self.cfg['tmp_dir'], 'inspector.png')
            try:
                os.remove(img_path)
            except OSError:
                pass
            android_actions.adb.run_cmd('shell rm /sdcard/screencap.png')
            android_actions.adb.run_cmd('shell screencap -p /sdcard/screencap.png')
            android_actions.adb.run_cmd('pull /sdcard/screencap.png')
            log.debug("saving screenshot to %s" % img_path)
            try:
                os.rename('screencap.png', img_path)
            except OSError as _e:
                print "Error"
                if _e.errno == errno.ENOENT:
                    raise Ux("ADB did not supply screenshot image")
                else:
                    raise Ux("could not rename 'screencap.png': %s" % _e)
            print "Done"

    def rotate_image(self):
        print "Rotating screenshot...",
        img_path = os.path.join(self.cfg['tmp_dir'], 'inspector.png')
        im = PIL_Image.open(img_path)
        im = im.rotate(-90, expand=True)
        im.save(img_path)
        self.create_cwin(reuse_image=True)
        print "Done"

    def __del__(self):
        print "Closing Appium...",
        self.update_idletasks()
        self.after(500, android_actions.close_appium)
        sleep(1)
        print "Done"

    @staticmethod
    def get_current_activity():
        print "current activity: " + android_actions.driver.current_activity

    def set_zpath_tag(self, abbrev, zpath):
        set_zpath_tag(abbrev, zpath)


def run_inspector(cfg):
    root = Tk()
    root.wm_title("Appium test utility")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    if 'zpath_tags_all' in cfg:
        replace_zpaths(cfg['zpath_tags_all'])
    if 'zpath_tags_new' in cfg:
        for tag in cfg['zpath_tags_new']:
            set_zpath_tag(tag, cfg['zpath_tags_new'][tag])
    gui_cfg = {
        'tmp_dir': cfg.get('tmp_dir', './tmp'),
        'log_window_height': cfg.get('log_window_height', 20)
    }
    try:
        os.makedirs(gui_cfg['tmp_dir'])
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(cfg['tmp_dir']):
            pass
        else:
            raise

    _app = Inspector(root, gui_cfg)
    package = _app.get_focused_app(quiet=True)
    # can load a plugin here based on the Inspector app's "package" attribute, set during the call to get_focused_app()
    if package != 'Unknown':
        try:
            if 'plugin_dir' in cfg:
                path = cfg['plugin_dir'].rsplit('/', 1)[0]
                sys.path.insert(0, path)
            import inspector_plugins
            module_name = '.' + '_'.join(package.split('.'))
            module = importlib.import_module(module_name, 'inspector_plugins')
            module_class = getattr(module, 'Plugin')
            instance = module_class()
            instance.install_plugin(_app)
        except ImportError as e:
            tb = sys.exc_info()[2]
            path, line_no = traceback.extract_tb(tb)[-1][:2]
            print "no plugin loaded for package %s\n  -->[%s:%s] %s" % (package, path, line_no, e)
        else:
            print "plugin loaded for package %s" % package
    root.protocol("WM_DELETE_WINDOW", _app.close_appium_and_quit)
    _app.mainloop()
