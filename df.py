#!/usr/bin/env python

from __future__ import with_statement
import contextlib
import os
import sys
import smtplib

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

mensaje = "PO Desarrollo\n\n"
mensaje += "Filesystem   Montado en         Uso%  \n"
with contextlib.closing(open('/etc/mtab')) as fp:
        for m in fp:
                fs_spec, fs_file, fs_vfstype, fs_mntops, fs_freq, fs_passno = m.split()
                if fs_spec.startswith('/'):
                        r = os.statvfs(fs_file)
                        block_usage_pct = 100.0 - (float(r.f_bavail) / float(r.f_blocks) * 100)
                        inode_usage_pct = 100.0 - (float(r.f_favail) / float(r.f_files) * 100)
                        mensaje += "%-12s %-16s %5d\n" % (fs_spec, fs_file, block_usage_pct)

sendemail(from_addr    = 'xxx@xxx.com',
          to_addr_list = ['xxx@xxx.com'],
          cc_addr_list = [''],
          subject      = 'ESPACIO PO DES',
          message      = mensaje,
          login        = '',
          password     = '')
