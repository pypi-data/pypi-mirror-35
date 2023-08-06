#!/usr/bin/env python3

import os
import time
import shutil
import signal

import yaml
import sass
import pyinotify

from colorama import init, Fore, Style
from jsmin import jsmin
from csscompressor import compress

VERSION = '1.4.7'


class Kyk(object):
    """Kyk

    Build JS
    - if min: minify in place, append _minifed
    - concat to destfile

    Build SASS:
    - compile SASS file
    - concat to destfile

    Build partial js not yet implemented completely
    """

    def __init__(self, folder, debug):
        self._folder = folder
        self._debug = debug
        init()
        self._load_config()
        signal.signal(signal.SIGINT, self.teardown)

    def teardown(self, signal, frame):
        if type(self.notifier) == pyinotify.ThreadedNotifier:
            print('stopping watching')
            self.notifier.stop()

    def _load_config(self, reloading=False):
        cfgfile = os.path.normpath(os.path.join(self._folder, 'kyk.yaml'))
        if not os.path.isfile(cfgfile) and reloading:
            time.sleep(1)  # wait for it to appear (ftp program maybe?)
        if not os.path.isfile(cfgfile):
            raise Exception('no config file "{}" found!'.format(cfgfile))

        with open(cfgfile, 'r', encoding='utf-8') as f:
            dat = f.read()

        self._cfg = yaml.load(dat)

        self._js = {}
        self._css = {}
        self._jswatchlist = []
        self._listen_events = []
        self._timestamp_file = None

        if 'watch_path' in self._cfg.keys():
            self._folder = self._cfg['watch_path']

        # no overwriting of command line debug, if config file does not hold debug: True we do not want to disable --debug
        if not self._debug:
            self._debug = 'debug' in self._cfg.keys() and self._cfg['debug']

        self._version = self._cfg['version']
        self._listen_events = self._cfg['events']
        if 'timestamp_file' in self._cfg.keys():
            self._timestamp_file = self._cfg['timestamp_file']

        for minfile in self._cfg.keys():
            if minfile.endswith('.js'):
                jsfile = self._cfg[minfile]
                minify = False

                for jsfile in self._cfg[minfile]:
                    if jsfile.startswith('min:'):
                        minify = True
                        jsfile = jsfile.split('min:')[1].strip()
                    if minfile not in self._js.keys():
                        self._js[minfile] = []

                    self._js[minfile].append({'file': os.path.abspath(jsfile), 'minify': minify})
                    self._jswatchlist.append(os.path.abspath(jsfile))
            elif minfile.endswith('.css'):
                self._css[minfile] = self._cfg[minfile]

        print('Kyk version: {}'.format(VERSION))
        print('config version: {}'.format(self._version))

    def oneshot(self):
        print('oneshot')
        self.build_js()
        self.build_sass()

    def watch_forever(self):
        print('listening on:')
        print(self._listen_events)

        # first run, build everything
        self.build_js()
        self.build_sass()

        # now only changed files
        self.wm = pyinotify.WatchManager()
        self.notifier = pyinotify.ThreadedNotifier(self.wm, default_proc_fun=self.handler)
        self.wm.add_watch(self._folder, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
        # self.notifier.loop()
        self.notifier.start()
        signal.pause()

    def reload(self):
        self.notifier.stop()
        self._load_config(True)
        self.watch_forever()

    def handler(self, event):
        # catch every scss file change, we can do this here because we are limited by the watchpath
        if getattr(event, 'pathname'):
            if event.pathname.endswith('.scss'):
                if event.maskname in self._listen_events:
                    print('{} changed!'.format(event.pathname))
                    self.build_sass()

            # catch only changes to our configured jsfiles
            elif event.pathname in self._jswatchlist:
                if event.maskname in self._listen_events:
                    print('{} changed!'.format(event.pathname))
                    self.build_js()

            elif event.pathname.endswith('kyk.yaml'):
                print('kyk config changed, reloading')
                self.reload()

    def build_js(self):
        """minify everything, then concat everything
        """
        print('building js...')
        for minfile in self._js.keys():
            with open(minfile, 'w', encoding='utf-8') as f:
                for jsfile in self._js[minfile]:
                    if jsfile['minify'] and not self._debug:
                        self.minify_js(jsfile['file'])

                    out = self._load_js(jsfile['file'], load_minified=jsfile['minify'])

                    f.write(out + "\n")

        print('finished')
        self._update_timestamp()

    def concat_js(self, destfile):
        print('building {}...'.format(destfile))
        with open(destfile, 'w', encoding='utf-8') as f:
            for jsfile in self._js[destfile]:
                if self._debug:
                    f.write('{}\n'.format(self._load_js(jsfile['file'])))
                f.write(self._load_js(jsfile['file']) + ';')
        print('finished')

    def minify_js(self, jsfile=None):
        """Minify JS in place, append _minified
        """
        out = jsmin(self._load_js(jsfile, load_minified=False))

        with open('{}_minified'.format(jsfile), 'w', encoding='utf-8') as f:
            f.write(out)

    def build_partial_js(self, changed):
        print('building partial js...')

        for minfile in self._js:
            for jsfile in self._js[minfile]:
                if changed == jsfile['file']:
                    if jsfile['minify'] and not self._debug:
                        self.minify_js(jsfile['file'])
                    self.concat_js(minfile)
        print('finished')

    def _load_js(self, jsfile, load_minified=True):
        """Load js from file, load _minifed if exists and we want to have it (we do not want it if we minify anew)
        """
        if load_minified and os.path.isfile('{}_minified'.format(jsfile)):
            jsfile = '{}_minified'.format(jsfile)

        if not os.path.isfile(jsfile):
            print(Fore.RED + 'File {} not found!'.format(jsfile))
            print(Style.RESET_ALL)

            return ''
        else:
            with open(jsfile, 'r', encoding='utf-8') as f:
                out = f.read()

            return out

    def _update_timestamp(self):
        try:
            if self._timestamp_file:
                with open(self._timestamp_file, 'w') as f:
                    f.write('{}'.format(int(time.time())))
                print('timestamp file updated')
        except Exception as e:
            print(Fore.RED + 'Error updating timestamp file: {}'.format(e))
            print(Style.RESET_ALL)

    def build_sass(self):
            print('building sass...')
            for minfile in self._css.keys():
                try:
                    # tmp minfile name for writing
                    minfile_name = os.path.basename(minfile)
                    tmp_minfile_name = 'kyk_{}'.format(minfile_name)

                    tmp_minfile = minfile.replace(minfile_name, tmp_minfile_name)
                    # only scss source map file
                    mapfile = tmp_minfile.replace('.css', '.css.map')
                    smapfile = tmp_minfile.replace('.css', '.smap.css')  # this holds the css and the source comments
                    with open(tmp_minfile, 'w', encoding='utf-8') as f, open(mapfile, 'w', encoding='utf-8') as smf, open(smapfile, 'w', encoding='utf-8') as sma:
                        for sassfile in self._css[minfile]:
                            if sassfile.endswith('.scss'):
                                ost = 'compressed'
                                if self._debug:
                                    ost = 'expanded'
                                sc, sm = sass.compile(filename=sassfile, source_comments=True, source_map_filename=mapfile, output_style=ost)
                                sc_clean = sass.compile(filename=sassfile, source_comments=False, output_style=ost)  # without source comments

                                f.write(sc_clean)
                                smf.write(sm)
                                sma.write(sc)
                            else:
                                sc = open(sassfile, 'r', encoding='utf-8').read()
                                if not self._debug:
                                    sc = compress(sc)
                                f.write(sc)

                    shutil.copy(tmp_minfile, minfile)
                    shutil.copy(mapfile, minfile.replace('.css', '.css.map'))
                    shutil.copy(smapfile, minfile.replace('.css', '.smap.css'))
                except sass.CompileError as e:
                    print(Fore.RED + 'SASS Error: {}'.format(e))
                    print(Style.RESET_ALL)

                    # in debug mode we break things on purpose here
                    if self._debug:
                        shutil.copy(tmp_minfile, minfile)
                        shutil.copy(mapfile, minfile.replace('.css', '.css.map'))
                        shutil.copy(smapfile, minfile.replace('.css', '.smap.css'))
            print('finished')
            self._update_timestamp()
