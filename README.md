# tacacs_log_parser

## Authentication Log
```2020-07-08 08:58:11 +0000|!|192.168.179.252|!|admin|!|tty66|!|192.168.179.1|!|shell login succeeded
2020-07-08 09:39:19 +0000|!|192.168.179.252|!|admin|!|tty66|!|192.168.179.1|!|shell login succeeded
2020-07-08 09:39:19 +0000|!|192.168.179.252|!|admin|!|tty66|!|192.168.179.1|!|shell login failed
```

## Accounting Log 
```2020-07-08 08:42:51 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=25|!|timezone=BST|!|service=shell|!|start_time=1594197717|!|priv-lvl=15|!|cmd=configure terminal <cr>
2020-07-08 08:43:04 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=26|!|timezone=BST|!|service=shell|!|start_time=1594197730|!|priv-lvl=15|!|cmd=aaa new-model <cr>
2020-07-08 08:44:36 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=27|!|timezone=BST|!|service=shell|!|start_time=1594197822|!|priv-lvl=15|!|cmd=aaa group server tacacs+ ROUTER <cr>
2020-07-08 08:45:47 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=28|!|timezone=BST|!|service=shell|!|start_time=1594197893|!|priv-lvl=15|!|cmd=aaa group server tacacs+ ROUTER <cr>
2020-07-08 08:47:01 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=29|!|timezone=BST|!|service=shell|!|start_time=1594197968|!|priv-lvl=0|!|cmd=exit <cr>
2020-07-08 08:47:14 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=30|!|timezone=BST|!|service=shell|!|start_time=1594197981|!|priv-lvl=15|!|cmd=aaa new-model <cr>
2020-07-08 08:47:42 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=31|!|timezone=BST|!|service=shell|!|start_time=1594198008|!|priv-lvl=15|!|cmd=tacacs-server host 192.168.179.129 key bin boot dev etc home initrd.img initrd.img.old lib lib64 lost+found media mnt opt proc root run sbin snap srv sys tmp usr var vmlinuz vmlinuz.old
2020-07-08 08:48:19 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=32|!|timezone=BST|!|service=shell|!|start_time=1594198046|!|priv-lvl=15|!|cmd=aaa authentication login default group ROUTER local <cr>
2020-07-08 08:49:50 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=33|!|timezone=BST|!|service=shell|!|start_time=1594198136|!|priv-lvl=15|!|cmd=aaa authentication enable default group ROUTER enable <cr>
2020-07-08 08:50:20 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=34|!|timezone=BST|!|service=shell|!|start_time=1594198167|!|priv-lvl=15|!|cmd=aaa accounting exec default start-stop group ROUTER <cr>
2020-07-08 08:51:05 +0000|!|192.168.179.252|!||!|tty0|!|async|!|stop|!|task_id=35|!|timezone=BST|!|service=shell|!|start_time=1594198212|!|priv-lvl=15|!|cmd=aaa accounting commands 0 default start-stop group ROUTER <cr>

```
