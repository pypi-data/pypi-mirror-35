import paramiko
import logging
import time
import json
import os
import string

from random import choice
from typing import Tuple, Optional


def makeTmpFile(sshClient: paramiko.SSHClient) -> bytes:
    _, stdoutReader, stderrReader = sshClient.exec_command("mktemp")
    stderr: bytes = stderrReader.read()
    if stderr:
        logging.warning("Got %s in stderr, exiting..." % stderr)
        exit(1)
    stdout: bytes = stdoutReader.read()
    logging.info("Got temp file: %s" % stdout.strip())
    return stdout.strip()


def paramikoExecuteRead(sshClient: paramiko.SSHClient, cmdStr: str, skipStdout: bool = False, _sync: bool = True) -> Tuple[bytes, bytes]:
    # We can't rely on fabric or paramiko (for god knows what reason), so we run our command in the background,
    # monitor the pid, and then read the output from temp files once we're done
    stderrFile: bytes = makeTmpFile(sshClient)
    stdoutFile: bytes = makeTmpFile(sshClient)

    screenName = ''.join([choice(string.ascii_lowercase) for _ in range(10)])

    if skipStdout:
        screenCmd = "screen -dm -S %s bash -c '%s 2> %s'; screen -S %s -Q echo '$PID'" % \
                    (screenName, cmdStr, stderrFile.decode('utf-8'), screenName)
    else:
        screenCmd = "screen -dm -S %s bash -c '%s > %s 2> %s'; screen -S %s -Q echo '$PID'" % \
                    (screenName, cmdStr, stdoutFile.decode('utf-8'), stderrFile.decode('utf-8'), screenName)

    _, stdout, stderr = sshClient.exec_command(screenCmd, timeout=10)

    pid = stdout.readline()
    if not pid:
        raise Exception("No pid found!!! cmd: %s" % screenCmd)

    while pidIsAlive(sshClient, pid):
        time.sleep(1)

    # Sleep one last time to make sure the files have been flushed
    time.sleep(10)
    if _sync:
        paramikoExecuteRead(sshClient, "sync", skipStdout=True, _sync=False)

    return readRemoteFile(sshClient, stdoutFile), readRemoteFile(sshClient, stderrFile)


def pidIsAlive(sshClient: paramiko.SSHClient, pid: str) -> bool:
    chan = sshClient.get_transport().open_session()
    chan.exec_command("kill -0 %s" % pid)
    return chan.recv_exit_status() == 0


def readRemoteFile(sshClient: paramiko.SSHClient, filename: bytes) -> bytes:
    sftpClient: paramiko.SFTP = sshClient.open_sftp()
    with sftpClient.open(filename.decode("utf-8"), "r") as f:
        return f.read()

def getSSHConnection() -> paramiko.SSHClient:
    hostList, username = os.environ["SCANNING_SERVER_IPS"], os.environ["SCANNING_SERVER_USER"]
    host = choice(json.loads(hostList))
    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        sshClient.connect(hostname=host, username=username,
                          password=os.environ["SCANNING_SERVER_PASSWORD"], port=2222)
        logging.info("Connected to host=%s" % host)
        return sshClient
    except paramiko.ssh_exception.SSHException as e:
        logging.info("Failed to connect to host=%s" % host)
        raise e

def writeDataToTmpFile(sshClient: paramiko.SSHClient, data: str) -> str:
    filename: bytes = makeTmpFile(sshClient)
    sftpClient: paramiko.SFTP = sshClient.open_sftp()
    with sftpClient.open(filename.decode('utf-8'), 'w') as f:
        f.write(data)
    return filename.decode("utf-8")

def cleanTemp(sshClient: paramiko.SSHClient) -> None:
    """ I'm a lazy/bad programmer so I just call this periodically to wipe out any old files in /tmp """
    sftpClient: paramiko.SFTP = sshClient.open_sftp()
    for fd in sftpClient.listdir("/tmp"):
        fp = "/tmp/" + fd
        try:
            lstats = sftpClient.lstat(fp)
            check = str(lstats).split()[0]
            if 'd' not in check:
                # Then it is a file so just check the date
                if lstats.st_mtime < time.time() - (3 * 60 * 60):
                    logging.info("Removing %s" % str(fp))
                    sftpClient.remove(fp)
        except FileNotFoundError:
            pass
