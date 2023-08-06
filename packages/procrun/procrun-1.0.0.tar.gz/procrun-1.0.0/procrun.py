import os, signal, six, threading, time, traceback


__version__ = "1.0.0"


class ProcessRunnerMixin:

    @staticmethod
    def sleep_for_a_thousand_years(why):
        print("sleep for 1,000 years: " + why)
        return time.sleep(3600*24*365*1000)

    def record_pid(_, procname):
        fname = os.path.join(_.name, procname+'.pid')
        with open(fname, 'w') as f:  f.write(str(os.getpid()))

    def kill(_, procname):
        os.system("kill `cat %s/%s.pid` 2>/dev/null" % (_.name, procname))

    def stop(_):     os.system("kill -USR1 `cat %s/node.pid`" % _.name)

    def restart(_):  _.start(), _.stop()

    def _suicide(_): os.killpg(os.getpgid(os.getpid()),9)

    def _launch_jobs(_, lines):
        if isinstance(lines, six.string_types): lines = lines.split('\n')
        for cmd in (x.strip() for x in lines):
            if not cmd or cmd[0]=='#':
                continue
            prefix, cmd = [ x.strip() for x in cmd.split(':', 1) ]
            def system_loop(prefix, cmd):
                oldcmd = cmd
                if cmd.startswith('@'): cmd = 'python -um ' + cmd[1:]
                cmd += ' 1>>%s/logs/%s.out' % (_.name, prefix)
                cmd += ' 2>>%s/logs/%s.err' % (_.name, prefix)
                while 1:
                    print("%s: SPAWN %s" % (prefix, oldcmd))
                    ret = os.system(cmd)
                    print("%s: RET = %s" % (prefix, ret))
                    time.sleep(1)
            threading.Thread(target=system_loop, args=(prefix,cmd,)).start()
            time.sleep(0.05)

    def launch_jobs(_, text):
        "feel free to override me!"
        _._launch_jobs(text)

    def start(_, jobs='jobs'):
        try:
            signal.signal(signal.SIGUSR1, lambda*a: _._suicide())
            _.record_pid('node')
            _.launch_jobs(jobs)
            time.sleep(0.25)
            _.sleep_for_a_thousand_years('all processed launched')
        except:
            traceback.print_exc() # goes to stderr
            _._suicide()

    pass # end class ProcessRunnerMixin
