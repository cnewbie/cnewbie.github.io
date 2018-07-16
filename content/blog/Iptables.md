Title: Iptables Firewall
Tags: iptables,linux
lang: zh
Summary: Iptables 配置
Date: 2017-06-30
Modified: 2018-07-16

---
title: Iptables 防火墙配置

---

-----------------------------

# filter,nat,mangle 规则表

## filter表

数据包过滤,根据规则决定是否放行数据包（DROP,ACCEPT,REJECT,LOG）

三条规则链

- INPUT 进入本地的包
- FORWARD 不是本地产生且负责转发的包
- OUTPUT 本地产生的包

## nat表

修改数据包ip地址、端口等信息（SNAT,DNAT,MASQUERADE,REDIRECT）

三条规则链

- PREROUTING 改变进入数据包的目的地址
- OUTPUT 改变本地产生包的目的地址
- POSTROUTING 改变发出数据包的源地址

## mangle表

修改数据包的TOS，TTL及数据包的Mark

五个规则链 PREROUTING，POSTROUTING，INPUT，OUTPUT，FORWARD

## raw表

决定数据包是否被状态跟踪机制处理

两条规则链 OUTPUT,PREROUTING

四种状态

- NEW 开始一个连接
- RELATED 某个已经建立的连接所建立的新连接
- ESTABLISHED 发送后接到应答的数据包
- INVALID 无法识别的数据包

# 规则链和规则

在处理各种数据包时，根据防火墙规则的不同时机，iptables供涉及5种默认规则链：

- INPUT 当接收到防火墙本机地址的数据包（入站）时,应用此链中的规则。。
- OUTPUT 当防火墙本机向外发送数据包（出站）时，应用此链中的规则。
- FORWARD 当接收到需要通过防火墙发送给其他地址的数据包（转发）时，应用此链中的规则。
- PREROUTING 在对数据包作路由选择之前，应用此链中的规则，如DNAT。
- POSTROUTING 在对数据包作路由选择之后，应用此链中的规则，如SNAT。


```
-->PREROUTING-->[ROUTE]-->FORWARD-->POSTROUTING-->
     mangle        |       mangle        ^ mangle
      nat          |       filter        |  nat
                   |                     |
                   |                     |
                   v                     |
                 INPUT                 OUTPUT
                   | mangle              ^ mangle
                   | filter              |  nat
                   v ------>local------->| filter
```

防火墙处理数据包的方式（规则）：

- ACCEPT：允许数据包通过
- DROP：直接丢弃数据包，不给任何回应信息
- REJECT：拒绝数据包通过，必要时会给数据发送端一个响应的信息。
- SNAT：源地址转换。在进入路由层面的route之前，重新改写源地址，目标地址不变，并在本机建立NAT表项，当数据返回时，根据NAT表将目的地址数据改写为数据发送出去时候的源地址，并发送给主机。解决内网用户用同一个公网地址上网的问题。
- MASQUERADE，是SNAT的一种特殊形式，适用于像adsl这种临时会变的ip上
- DNAT:目标地址转换。和SNAT相反，IP包经过route之后、出本地的网络栈之前，重新修改目标地址，源地址不变，在本机建立NAT表项，当数据返回时，根据NAT表将源地址修改为数据发送过来时的目标地址，并发给远程主机。可以隐藏后端服务器的真实地址。
- REDIRECT：是DNAT的一种特殊形式，将网络包转发到本地host上（不管IP头部指定的目标地址是啥），方便在本机做端口转发。
- LOG：在/var/log/messages文件中记录日志信息，然后将数据包传递给下一条规则

除去最后一个LOG，前3条规则匹配数据包后，该数据包不会再往下继续匹配了，所以编写的规则顺序极其关键。

Linux数据包路由原理

![数据包流程](/images/2017-packetflow.jpg)

# iptables编写规则
![命令格式](/images/2017-iptables.png)

- [-t 表名]：该规则所操作的哪个表，可以使用filter、nat等，如果没有指定则默认为filter
- -A：新增一条规则，到该规则链列表的最后一行
- -I：插入一条规则，原本该位置上的规则会往后顺序移动，没有指定编号则为1
- -D：从规则链中删除一条规则，要么输入完整的规则，或者指定规则编号加以删除
- -R：替换某条规则，规则替换不会改变顺序，而且必须指定编号。
- -P：设置某条规则链的默认动作
- -nL：-L、-n，查看当前运行的防火墙规则列表
- chain名：指定规则表的哪个链，如INPUT、OUPUT、FORWARD、PREROUTING等
- [规则编号]：插入、删除、替换规则时用，--line-numbers显示号码
- [-i|o 网卡名称]：i是指定数据包从哪块网卡进入，o是指定数据包从哪块网卡输出
- [-p 协议类型]：可以指定规则应用的协议，包含tcp、udp和icmp等
- [-s 源IP地址]：源主机的IP地址或子网地址
- [--sport 源端口号]：数据包的IP的源端口号
- [-d目标IP地址]：目标主机的IP地址或子网地址
- [--dport目标端口号]：数据包的IP的目标端口号
- -m：extend matches，这个选项用于提供更多的匹配参数，如：
  - -m state –state ESTABLISHED,RELATED
  - -m tcp –dport 22
  - -m multiport –dports 80,8080
  - -m icmp –icmp-type 8
- <-j 动作>：处理数据包的动作，包括ACCEPT、DROP、REJECT等

# iptables常用实例备查

```bash
iptables -P INPUT DROP
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
```

限制

`iptables -I INPUT 1 -m state --state RELATED,ESTABLISHED -j ACCEPT`

把这条语句插在input链的最前面（第一条），对状态为ESTABLISHED,RELATED的连接放行

`iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT`

开放指定端口

`iptables -I INPUT 2 -i lo -j ACCEPT`

允许loopback，本地回环是主机内部发送和接收

删除

`iptables -D chain  number`

丢弃非法连接

```bash
iptables -A INPUT -m state –state INVALID -j DROP
iptables -A OUTPUT -m state –state INVALID -j DROP
iptables-A FORWARD -m state –state INVALID -j DROP
```

日志

`iptables -R INPUT 1 -p tcp --dport 22 -m limit --limit 3/minute --limit-burst 8 -j LOG`

Dos

```bash
iptables -N syn-flood   (如果您的防火墙默认配置有“ :syn-flood - [0:0] ”则不许要该项，因为重复了)
iptables -A INPUT -p tcp --syn -j syn-flood
iptables -I syn-flood -p tcp -m limit --limit 2/s --limit-burst 5 -j RETURN
iptables -A syn-flood -j REJECT
# 防止DOS太多连接进来,可以允许外网网卡每个IP最多15个初始连接,超过的丢弃

# 需要iptables v1.4.19以上版本：iptables -V
iptables -A INPUT -p tcp --syn -i eth0 --dport 80 -m connlimit --connlimit-above 20 --connlimit-mask 24 -j DROP

#用Iptables抵御DDOS (参数与上相同)
iptables -A INPUT -p tcp --syn -m limit --limit 5/s --limit-burst 10 -j ACCEPT
iptables -A FORWARD -p tcp --syn -m limit --limit 1/s -j ACCEPT
iptables -A FORWARD -p icmp -m limit --limit 2/s --limit-burst 10 -j ACCEPT
iptables -A INPUT -p icmp --icmp-type 0 -s ! 172.29.73.0/24 -j DROP
```

# 引用

[Seanlook](http://seanlook.com/2014/02/23/iptables-understand/)
