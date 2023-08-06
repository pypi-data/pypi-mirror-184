"""class for the range test module settings"""


from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QCheckBox, QFormLayout, QDialogButtonBox, QLineEdit, QLabel

from meshtastic.__init__ import BROADCAST_ADDR
from meshtastic.__main__ import setPref
from meshtastic_flasher.util import zero_if_blank


class RangeTestForm(QDialog):
    """range test module settings form"""

    def __init__(self, parent=None):
        """constructor"""
        super(RangeTestForm, self).__init__(parent)

        self.parent = parent
        self.main = parent.main

        width = 500
        height = 200
        self.setMinimumSize(width, height)
        self.setWindowTitle(self.main.text('range_test_module_settings'))

        self.port = None
        self.interface = None
        self.prefs = None

        # Create widgets
        self.range_test_about = QLabel(self.main.doc_url('range_test_module_about'))
        self.range_test_about.setOpenExternalLinks(True)
        self.range_test_about.setTextFormat(QtCore.Qt.RichText)
        self.range_test_about.setToolTip(self.main.tooltip('module_link'))
        self.range_test_module_enabled = QCheckBox()
        self.range_test_module_enabled.setToolTip(self.main.description('range_test_module_enabled'))
        self.range_test_module_save = QCheckBox()
        self.range_test_module_save.setToolTip(self.main.description('range_test_module_save'))
        self.range_test_module_sender = QLineEdit()
        self.range_test_module_sender.setToolTip(self.main.description('range_test_module_sender'))

        # Add a button box
        self.button_box = QDialogButtonBox()
        self.button_box.setStandardButtons(QDialogButtonBox.Save)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        # create form
        form_layout = QFormLayout()
        form_layout.addRow(self.main.label("range_test_module_about"), self.range_test_about)
        form_layout.addRow(self.main.label("range_test_module_enabled"), self.range_test_module_enabled)
        form_layout.addRow(self.main.label("range_test_module_save"), self.range_test_module_save)
        form_layout.addRow(self.main.label("range_test_module_sender"), self.range_test_module_sender)
        form_layout.addRow("", self.button_box)
        self.setLayout(form_layout)


    def run(self, port=None, interface=None):
        """load the form"""
        self.port = port
        self.interface = interface
        if self.port:
            print(f'using port:{self.port}')
            self.get_values()
            self.show()


    def get_values(self):
        """Get values from device"""
        try:
            if self.interface:
                self.prefs = self.interface.getNode(BROADCAST_ADDR).radioConfig.preferences

                if self.prefs.range_test_module_enabled and self.prefs.range_test_module_enabled is True:
                    self.range_test_module_enabled.setChecked(True)

                if self.prefs.range_test_module_save and self.prefs.range_test_module_save is True:
                    self.range_test_module_save.setChecked(True)

                if self.prefs.range_test_module_sender:
                    self.range_test_module_sender.setText(f'{self.prefs.range_test_module_sender}')
                else:
                    self.range_test_module_sender.setText("0")

        except Exception as e:
            print(f'Exception:{e}')


    def write_values(self):
        """Write values to device"""
        try:
            if self.interface:
                print("Writing preferences to device")
                prefs = self.interface.getNode(BROADCAST_ADDR).radioConfig.preferences
                setPref(prefs, 'range_test_module_enabled', f'{self.range_test_module_enabled.isChecked()}')
                setPref(prefs, 'range_test_module_save', f'{self.range_test_module_save.isChecked()}')
                setPref(prefs, 'range_test_module_sender', zero_if_blank(self.range_test_module_sender.text()))
                self.interface.getNode(BROADCAST_ADDR).writeConfig()

        except Exception as e:
            print(f'Exception:{e}')


    def reject(self):
        """Cancel without saving"""
        print('CANCEL button was clicked')
        self.parent.my_close()


    def accept(self):
        """Close the form"""
        print('SAVE button was clicked')
        self.write_values()
