import time
import pexpect
import subprocess
import sys
import re

class BluetoothctlError(Exception):
    """This exception is raised, when bluetoothctl fails to start."""
    pass


class Bluetoothctl:
    def __init__(self):
        out = subprocess.check_output("sudo rfkill unblock bluetooth", shell = True)
        self.child = pexpect.spawn("bluetoothctl", echo = False)
        print("bluetoothctl")

    def get_output(self, command, pause = 0):
        """Run a command in bluetoothctl prompt, return output as a list of lines."""
        self.child.send(command + "\n")
        time.sleep(pause)
        start_failed = self.child.expect(["bluetooth", pexpect.EOF])

        if start_failed:
            raise BluetoothctlError("Bluetoothctl failed after running " + command)

        return self.child.before.split("\r\n")

    def make_discoverable(self):
        """Make device discoverable."""
        try:
            out = self.get_output("discoverable on")
            print("discoverable on")
        except BluetoothctlError as e:
            print(e)
            return None


    def power_on(self):
        """Start agent"""
        try:
            out = self.get_output("power on")
            print("power on")
        except BluetoothctlError as e:
            print(e)
            return None


    def pairable_on(self):
        """Start agent"""
        try:
            out = self.get_output("pairable on")
            print("pairable on")
        except BluetoothctlError as e:
            print(e)
            return None

    def agent_noinputnooutput(self):
        """Start agent"""
        try:
            out = self.get_output("agent NoInputNoOutput")
            print("agent Registered Successfully")
        except BluetoothctlError as e:
            print(e)
            return None

    def default_agent(self):
        """Start default agent"""
        try:
            out = self.get_output("default-agent")
            print("set as default agent")
        except BluetoothctlError as e:
            print(e)
            return None

if __name__ == "__main__":
    print("Init bluetooth...")
    bl = Bluetoothctl()
    bl.power_on()
    bl.make_discoverable()
    bl.pairable_on()
    bl.agent_noinputnooutput()
    bl.default_agent()