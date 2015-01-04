
# vim: set ts=4 sw=4 expandtab:

from puremvc.patterns.command import SimpleCommand

from libtimesheet.model.TimeProxy import TimeProxy

from libtimesheet.view.DialogMediator import DialogMediator
from libtimesheet.view.MenuMediator import MenuMediator
from libtimesheet.view.DatePickerMediator import DatePickerMediator
from libtimesheet.view.TimeGridMediator import TimeGridMediator
from libtimesheet.view.SummaryMediator import SummaryMediator

class StartupCommand(SimpleCommand):
    def execute(self,note):
        self.facade.registerProxy(TimeProxy())

        mainPanel = note.getBody()
        self.facade.registerMediator(DialogMediator(mainPanel))
        self.facade.registerMediator(MenuMediator(mainPanel.menuBar))
        self.facade.registerMediator(TimeGridMediator(mainPanel.timeGrid))
        self.facade.registerMediator(SummaryMediator(mainPanel.summary))

        # This one must be registered last, or at least after TimeGridMediator
        # Fires DATE_SELECTED notification, which is used in TimeGridMediator
        self.facade.registerMediator(DatePickerMediator(mainPanel.datePicker))
