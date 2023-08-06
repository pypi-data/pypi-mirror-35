import os
import logging

from typing import List

from tulgey.utils.iputils import normalizeIPv6, isValidIPv6
from tulgey.utils.ssh import getSSHConnection, paramikoExecuteRead, writeDataToTmpFile, cleanTemp


def filterToAlive(ipsToPing: List[str]) -> List[str]:
    """
    Filter the given list of IPv6 IPs to live ones
    :param ipsToPing:
    :return:
    """
    sshClient = getSSHConnection()
    cleanTemp(sshClient)
    inputFilename: str = writeDataToTmpFile(sshClient, "\n".join(ipsToPing))

    ipCmd = """ip -6 addr show dev eth0 | grep 'inet6' | awk '{print $2}' | cut -d/ -f1 | grep -v fe80"""
    _, stdoutReader, _ = sshClient.exec_command(ipCmd)
    sourceIp: str = stdoutReader.read().strip().decode('utf-8')
    if not sourceIp or not isValidIPv6(sourceIp):
        raise Exception("Got invalid IP address from `ip -6`! %s" % repr(sourceIp))
    zmapCmd = "zmap --ipv6-target-file=%s --ipv6-source-ip=%s -M icmp6_echoscan -r %s" % (
        inputFilename, sourceIp, str(int(os.environ['SCANNING_SERVER_SCAN_RATE']) // 5))
    stdout, stderr = paramikoExecuteRead(sshClient, zmapCmd)
    if stderr and b"zmap: completed" not in stderr:
        #       raise Exception('Got "%s" in stderr' % stderr)
        logging.critical('Got "%s" in stderr' % stderr)

    alive: List[str] = []
    for line in stdout.splitlines():
        alive.append(normalizeIPv6(line.decode('utf-8')))
    return alive
