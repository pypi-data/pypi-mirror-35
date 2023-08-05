from qlib.data import dbobj, Cache
from qlib.file import ensure_path

from concurrent.futures.thread import  ThreadPoolExecutor
from termcolor import colored
from functools import partial

import importlib
import base64
import pickle
import json
import os
import sys
import logging

DEFAULT_BASE_DIR = os.path.expanduser("~/DefaultApiDir/plugins")
MODULES_PATH = os.path.join(DEFAULT_BASE_DIR, 'Plugins')
ensure_path(DEFAULT_BASE_DIR)
ensure_path(MODULES_PATH)


class OO:pass
class Repo(dbobj):pass

def load(name):
    try:
        return importlib.import_module("Plugins.%s" % name)
    except ModuleNotFoundError as e:
        files = os.listdir(MODULES_PATH)
        if (name + ".bash") in files:
            def _run(*args, **kargs):
                res = os.popen('bash %s {}'.format(" ".join(['"%s"' % i for i in args])) % os.path.join(MODULES_PATH, name + ".bash")).read()
                return res
            OO.run = _run
            return OO
        return str(e)
    


class BaseApi:
    BASE_REPO = None
    BASE_DIR = DEFAULT_BASE_DIR
    MODULES_PATH = os.path.join(BASE_DIR, 'Plugins')
    REPO_DB = os.path.join(BASE_DIR, 'repo.db')
    REPO_NOW_USE = os.path.join(BASE_DIR, 'repo.now')
    exes = ThreadPoolExecutor(max_workers=40)

    def __init__(self, name, loop=None, callback=None):
        assert self.__class__.BASE_REPO is not None
        self.name = name
        self.loop = loop
        self.__callback = callback
        self.Permission = None
        self._Obj = self.load(self.name)
        if hasattr(self._Obj, 'Permission'):
            self.Permission = self._Obj.Permission


    def set_callback(self, callback):
        self.__callback = callback

    def set_repo(self, name,url, path):
        c = Cache(self.__class__.REPO_DB)
        if path.endswith("/"):
            path = path[:-1]
        r = Repo(name=name, url=url, path=path)
        os.popen("cd %s && git init || git remote add %s  %s" % (r.path.strip(), r.name.strip(), r.url.strip()))
        r.save(c)

    def update(self, repo_name):
        c = Cache(self.__class__.REPO_DB)
        r = c.query_one(Repo, name=repo_name)
        if not r:
            r = c.query_one(Repo)
        
        if r:
            return os.popen("cd %s && pwd &&  git fetch --all && git reset --hard %s/master" % (r.path.strip(), r.name)).read()
        else:
            base_repo = self.__class__.BASE_REPO
            assert base_repo is not None
            self.set_repo('origin', base_repo, self.__class__.MODULES_PATH)
            res = self.update(repo_name)
            return "rebuild... " + res

    def switch_repo(self, repo_name):
        c = Cache(self.__class__.REPO_DB)
        r = c.query_one(Repo, name=repo_name)
        with open(self.__class__.REPO_NOW_USE, 'w') as fp:
            fp.write(r.path.strip())
    
    def use_repo(self):
        if os.path.exists(self.__class__.REPO_NOW_USE):
            with open(self.__class__.REPO_NOW_USE) as fp:
                N = fp.read()
                dname = os.path.dirname(N)
                mname = os.path.basename(N)
                if dname not in sys.path:
                    sys.path += [dname]
                return mname
        else:
            dname = os.path.dirname(self.__class__.MODULES_PATH)
            mname = os.path.basename(self.__class__.MODULES_PATH)
            if dname not in sys.path:
                sys.path += [dname]
            return mname


    def cat(self, file):
        c = Cache(self.__class__.REPO_DB)
        r = c.query_one(Repo, name=self.use_repo())
        if r:
            files = os.listdir(r.path)
            for f in fils:
                if file in f:
                    with open(os.path.join(r.path, f)) as fp:
                        return fp.read()
            return "no file: %s" % file
        return "no current repo"


    def load(self, name):
        mname = self.use_repo()
        try:
            return importlib.import_module("%s.%s" % (mname, name))
        except ModuleNotFoundError as e:
            files = os.listdir(self.__class__.MODULES_PATH)
            if (name + ".bash") in files:
                def _run(*args, **kargs):
                    res = os.popen('bash %s {}'.format(" ".join(['"%s"' % i for i in args])) % os.path.join(self.__class__.MODULES_PATH, name + ".bash")).read()
                    return res
                OO.run = _run
                return OO
            return str(e)
        

    def run(self, *args, **kargs):
        if self.name == 'repo-set':
            name = kargs.get('name','').strip()
            path = kargs.get('path','').strip()
            url = kargs.get('url','').strip()

            if not 'https://github' in url:
                return url + " Not valid"
            if not os.path.exists(path):
                return path + " Not found"
            if ' ' in name:
                return name + " Not valid"

            self.set_repo(name, url, path)
            return "repo set : name=%s url=%s path=%s " % (name, url, path)
        elif self.name == 'repo-use':
            repo = kargs.get('name')
            self.switch_repo(repo)
            return 'switch to : %s' % wargs[1]
        elif self.name == 'repo-ls':
            c = Cache(self.__class__.REPO_DB)
            rs = c.query(Repo)
            _d = [r.get_dict() for r in rs]
            now = self.use_repo()
            _d.insert(0, now)
            return json.dumps(_d)
            
        elif self.name == 'repo-help':
            c = Cache(self.__class__.REPO_DB)
            r = c.query_one(Repo, name=wargs[0])
            if r:
                res = self.update(r.name)
                return res
            return """suport:
                    Was sagst du?
                        curl http://xxxx -d module=repo-ls                      # ls all repo, and now repo
                        curl http://xxxx -d module=repo-help
                        curl http://xxxx -d module=repo-set -d name="xxx-name" -d url="https://xxxx" -d path="/xxx/xxx/xx" # set repo
                        curl http://xxxx -d module=repo-use -d name="xxx-name"  # switch repo
                        curl http://xxxx -d module=repo-update                  # this will update use now repo

                    """
                
        elif self.name == 'repo-update':
            res = self.update("")
            return res
        else:
            if isinstance(self._Obj, str):
                return self._Obj
            if not self.loop:
                logging.warn("loop is None.")
            
            fff = partial(self._Obj.run, *args, **kargs)
            if 'loop' in self._Obj.run.__code__.co_varnames:
                logging.info("patch with loop")
                
                fff = partial(fff, loop=self.loop)

                
            

            futu = self.__class__.exes.submit(fff)
            if hasattr(self._Obj, 'callback'):
                self.__callback = self._Obj.callback
            futu.add_done_callback(self.callback)

    def _callback(self, r):
        print(colored("[+]",'green'), r)

    def callback(self, result):
        raise NotImplementedError("Not implement!!")



class BaseArgs:

    def __init__(self, handle, tp=None):
        self.handle = handle
        self.args = []
        self.kargs = dict()
        self._tp = tp
        self.parse()


    def get_parameter(self):
        raise NotImplementedError("")

    def get_parameter_keys(self):
        raise NotImplementedError("")

    def finish(self,D):
        raise NotImplementedError("")

    def parse(self):    
        tp = self.get_parameter("type")
        args = self.get_parameter('args')
        self.module = self.get_parameter('module')
        self.type = tp
        self.kwargs = {}

        keys = self.get_parameter_keys()
        for k in keys:
            if k in ['type', 'args', 'module']:
                continue
            self.kwargs[k] = self.get_parameter(k)

        if tp == 'base64':
            if isinstance(args, str):
                args = args.encode('utf8', 'ignore')
            args = json.loads(base64.b64decode(args))
            if isinstance(args, (list, tuple,)):
                self.args = args
            else:
                self.kargs = args
        elif tp =='json':
            args = json.loads(args)
            if isinstance(args, (list, tuple,)):
                self.args = args
            else:
                self.kargs = args
        else:
            self.args = [args]

    def after_dealwith(self, data):
        b_data = {'res':None, 'type':'json'}
        
        if isinstance(data, str) or isinstance(data, (list, dict, tuple, )):
            b_data['res'] = data
        elif isinstance(data, (int,float,bool,)):
            b_data['res'] = data
        else:
            b_data['res'] = base64.b64encode(pickle.dumps(data))
            b_data['type'] = 'pickle'

        D = json.dumps(b_data)
        self.finish(D)
            

