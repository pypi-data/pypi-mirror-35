#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import socket
import sys
from logging.handlers import (DatagramHandler, RotatingFileHandler,
                              SMTPHandler, SysLogHandler)

BRIEF_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
PRECISE_FORMATTER = logging.Formatter(
    '%(asctime)s %(process)d %(levelname)s %(module)s %(message)s')

logging.getLogger().addHandler(logging.NullHandler())
logging.getLogger().setLevel(logging.DEBUG)


def __create_and_add_handler(hander_class, formatter, level, *args, **kwargs):
    handler = hander_class(*args, **kwargs)
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logging.getLogger().addHandler(handler)
    return handler


def remove_handler(handler):
    """删除日志handler

    :param handler: handler实例

    """
    root_logger = logging.getLogger()
    if handler in root_logger.handlers:
        root_logger.removeHandler(handler)


def add_stream_handler(level=logging.DEBUG, stream=sys.stderr):
    """增加流式log handler

    :param level: 指定输出日志等级
    :param stream: 输出流

    :returns: 生成的handler

    """
    handler = __create_and_add_handler(logging.StreamHandler, BRIEF_FORMATTER,
                                       level, stream)
    return handler


def add_file_handler(appname="app", log_path='.', level=logging.INFO):
    """增加文件handler

    :param appname: 应用名，用于创建独立的日志文件夹名
    :param log_path: 存放日志文件夹的路径
    :param level: 指定输出日志等级

    :returns: 生成的handler

    """
    foldername = '%s_logs' % appname
    log_dir = "/".join([log_path, foldername])
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    filepath = "%s/%s.log" % (log_dir, appname)
    filelog_handler = __create_and_add_handler(
        RotatingFileHandler,
        BRIEF_FORMATTER,
        level,
        filepath,
        maxBytes=5 * 1024 * 1024,
        backupCount=100,
        encoding='utf-8')
    return filelog_handler


def add_syslog_handler(
        address='/dev/log',  # remote: use ('localhost', logging.handlers.SYSLOG_UDP_PORT)
        socktype=socket.SOCK_DGRAM,
        level=logging.WARNING):
    """增加syslog日志

    :param address: syslog服务器地址(host, port) 或者文件路径
    :param socktype: 指定socket传输类型
    :param level: 输出日志等级

    :returns: 生成的handler

    """
    handler = __create_and_add_handler(
        SysLogHandler,
        PRECISE_FORMATTER,
        level,
        address=address,
        socktype=socktype)
    return handler


def add_udp_handler(host, port, level):
    """启用udp handler

    :param host: udp服务主机名
    :param port: udp服务端口号

    :returns: 生成的handler

    """
    handler = __create_and_add_handler(DatagramHandler, BRIEF_FORMATTER, level,
                                       host, port)
    return handler


def add_smtp_handler(mailhost,
                     fromaddr,
                     toaddrs,
                     subject,
                     credentials=None,
                     level=logging.CRITICAL,
                     secure=None):
    """启用日志邮件通知

    :param mailhost: 邮件服务器主机名
    :param fromaddr: 邮件发送方地址
    :param toaddrs: 邮件接收方地址
    :param subject: 主题
    :param credentials: 认证信息
    :param level: 输出日志等级
    :param secure: 安全协议

    :returns: 生成的handler

    """
    handler = __create_and_add_handler(SMTPHandler, BRIEF_FORMATTER, level,
                                       mailhost, fromaddr, toaddrs, subject,
                                       credentials, secure)
    return handler


if __name__ == '__main__':
    stream_handler = add_stream_handler()
    add_syslog_handler()
    logging.warning(1)
    remove_handler(stream_handler)
    logging.info(2)
