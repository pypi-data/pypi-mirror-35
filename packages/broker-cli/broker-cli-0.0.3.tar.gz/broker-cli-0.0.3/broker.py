#!/usr/bin/env python

import subprocess, re, os, sys, json



from optparse import OptionParser





def cli():
    payload = {}
    options = {}
    ssh_options = []
    if len(sys.argv) == 1:
        print('use me like: broker my.server.tld')
        sys.exit()

    if '-4' in sys.argv:
            ssh_options.append('-4')
            sys.argv.remove('-4')
    if '-6' in sys.argv:
            ssh_options.append('-6')
            sys.argv.remove('-6')
    if '-C' in sys.argv:
            ssh_options.append('-C')
            sys.argv.remove('-C')
    if '-p' in sys.argv:
            ssh_options.append('-p')
            i = sys.argv.index('-p')
            sys.argv.remove('-p')
            ssh_options.append(sys.argv[i])
            sys.argv.remove(sys.argv[i])

    if len(sys.argv) >= 2:
        if '@' in sys.argv[1]:
            server = sys.argv[1]
        else:
            server = 'broker@%s' % sys.argv[1]
    if len(sys.argv) >= 3:
        payload['project'] = sys.argv[2]
    if len(sys.argv) >= 4:
        payload['options'] = options
        payload['command'] = sys.argv[3]
    if len(sys.argv) >= 6:
        for i in range(3,len(sys.argv)):
            if sys.argv[i].startswith('--'):
                options[sys.argv[i].replace('--','')] = None
        for i in options:
            options[i] = sys.argv[sys.argv.index('--'+i)+1]
        payload['options'] = options

    #subprocess.call(['ssh', ' '.join(ssh_options), 'broker@%s' % server, json.dumps(payload)])
    #print 'ssh %s broker@%s \'%s\'' % (' '.join(ssh_options), server, json.dumps(payload))
    cmd= 'ssh %s %s \'%s\'' % (' '.join(ssh_options), server, json.dumps(payload))
    subprocess.call(cmd, shell=True)
