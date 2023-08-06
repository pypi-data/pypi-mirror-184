"""class for the settings"""


from PySide6.QtWidgets import QTabWidget, QMainWindow, QMessageBox

import meshtastic.serial_interface

from meshtastic_flasher.admin_form import AdminForm
from meshtastic_flasher.wifi_and_mqtt_form import Wifi_and_MQTT_Form
from meshtastic_flasher.user_form import UserForm
from meshtastic_flasher.position_form import PositionForm
from meshtastic_flasher.power_form import PowerForm
from meshtastic_flasher.radio_form import RadioForm
from meshtastic_flasher.channel_settings import ChannelSettings
from meshtastic_flasher.plugin_settings import PluginSettings


class Settings(QMainWindow):
    """settings"""

    def __init__(self, parent=None):
        """constructor"""
        super(Settings, self).__init__(parent)

        self.port = None
        self.interface = None

        self.parent = parent
        self.main = parent

        width = 800
        height = 700
        self.setMinimumSize(width, height)
        self.setWindowTitle(self.main.text('settings'))

        # self.admin_form = AdminForm(self)
        # self.wifi_and_mqtt_form = Wifi_and_MQTT_Form(self)
        # self.user_form = UserForm(self)
        # self.position_form = PositionForm(self)
        # self.power_form = PowerForm(self)
        self.radio_form = RadioForm(self)
        # self.plugin_settings = PluginSettings(self)
        # self.channel_settings = ChannelSettings(self)

        self.tabs = QTabWidget()

        self.setStyleSheet("""
QTabWidget::pane {
    position: absolute;
    top: 1em;
}
QTabWidget::tab-bar {
    alignment: center;
}
QTabWidget::tab {
}
QTabBar::tab:selected {
    margin-left: 2px;
    margin-right: 2px;
}
QTabBar::tab:first:selected {
    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */
}
QTabBar::tab:last:selected {
    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
}
QTabBar::tab:only-one {
    margin: 0; /* if there is only one tab, we don't want overlapping margins */
}
""")
        self.tabs.blockSignals(True) # just for not showing initial message
        self.tabs.currentChanged.connect(self.on_change_tabs)

        self.tabs.setTabPosition(QTabWidget.North)

        # self.tabs.addTab(self.user_form, self.main.text('user'))
        # self.tabs.addTab(self.wifi_and_mqtt_form, "Wifi/MQTT")
        # self.tabs.addTab(self.position_form, self.main.text('position'))
        # self.tabs.addTab(self.power_form, self.main.text('power'))
        self.tabs.addTab(self.radio_form, self.main.text('radio'))
        # self.tabs.addTab(self.plugin_settings, self.main.text('modules'))
        # self.tabs.addTab(self.channel_settings, self.main.text('channels'))
        # self.tabs.addTab(self.admin_form, self.main.text('admin'))

        self.setCentralWidget(self.tabs)

        self.tabs.blockSignals(False) # now listen the currentChanged signal


    def on_change_tabs(self, i):
        """On change of each tab """
        print(f'on_change_tabs:{i}')
        # if i == 0:
        #     print('user run()')
        #     self.user_form.run(port=self.port, interface=self.interface)
        # elif i == 1:
        #     print('wifi_and_mqtt_form run()')
        #     self.wifi_and_mqtt_form.run(port=self.port, interface=self.interface)
        # elif i == 2:
        #     print('position run()')
        #     self.position_form.run(port=self.port, interface=self.interface)
        # elif i == 3:
        #     print('power run()')
        #     self.power_form.run(port=self.port, interface=self.interface)
        # elif i == 4:
        print('radio run()')
        self.radio_form.run(port=self.port, interface=self.interface)
        # elif i == 5:
        #     print('plugin settings run()')
        #     self.plugin_settings.run(port=self.port, interface=self.interface)
        # elif i == 6:
        #     print('channel settings run()')
        #     self.channel_settings.run(port=self.port, interface=self.interface)
        # elif i == 7:
        #     print('admin form run()')
        #     self.admin_form.run(port=self.port, interface=self.interface)


    def my_close(self):
        """Close this window"""
        if self.port:
            self.port = None
        if self.interface:
            self.interface.close()
            self.interface = None # so any saved values are re-read upon next form use
        self.close()


    # pylint: disable=unused-argument
    def closeEvent(self, event):
        """On close of the Settings window"""
        print('closed Settings')
        self.my_close()


    def confirm_use_fake_device(self):
        """Prompt the user to confirm if they want to use a 'fake' device.
           Returns True if user answered Yes, otherwise returns False
        """
        want_to_proceed = False
        confirm_msg = self.main.text('confirm_use_fake_device')
        reply = QMessageBox.question(self, self.main.text('question'), confirm_msg, QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            want_to_proceed = True
            print("User confirmed they want to use a fake device")
        else:
            print("User does not want to use a fake device")
        return want_to_proceed


    def run(self):
        """load the form"""
        print('in settings')
        if self.interface is None:
            try:
                self.interface = meshtastic.serial_interface.SerialInterface(devPath=self.port)
                self.port = self.interface.devPath
                print(f'self.port:{self.port}:')
            except Exception as e:
                print(f'Exception:{e}')
            except SystemExit:
                pass
        if self.interface:
            self.show()
            self.radio_form.run(port=self.port, interface=self.interface)
        else:
            QMessageBox.warning(self, self.main.text('warning'), self.main.text('warning_problem_connecting'))
            if self.confirm_use_fake_device():
                self.show()
                self.radio_form.run(port=None, interface=None)
            else:
                print("closing")
                self.my_close()
