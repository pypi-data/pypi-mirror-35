# encoding: utf-8

from uiutil.tk_names import ttk
from stateutil.switch import Switch as _Switch
from stateutil.persist import Persist
from ..helper.arguments import pop_kwarg, raise_on_positional_args
from .observable_base_widget import BaseWidget


class Switch(BaseWidget,
             _Switch):

    WIDGET = ttk.Checkbutton
    STYLE = u"TCheckbutton"
    VAR_TYPE = u'boolean_var'
    VAR_PARAM = u'variable'
    VAR_IS_OPTIONAL = False
    DEFAULT_VALUE = _Switch.ON

    def __init__(self,
                 # switch_state=_Switch.ON,
                 # link=None,
                 # persist=None,
                 # trace=None,
                 # take_focus=None,
                 *args,
                 **kwargs):
        """
        Note: link/persist and trace are bit strange in this widget.
        A link/persist is always used, even if one is not provided.
        This is because we want to observe it and use
        notifications to update the state (ON or OFF), in order to
        have access ot the _Switch methods.
         
        Trace is still available, calling the traced function
        on notification of the link changing
        
        :param switch_state: Switch.ON or Switch.Off
        :param link: a Persist object
        :param trace: function to call on value change
        :param take_focus: used to set takefocus in the kwargs.
                           Does not override takefocus if already
                           in kwargs.
        :param args: invalid. positional args are poison in BaseWidget!
        :param kwargs: keyword arguments to the underlying widget
        """

        raise_on_positional_args(self, args)
        switch_state = pop_kwarg(kwargs, u'switch_state', self.ON)
        #take_focus = pop_kwarg(kwargs, u'take_focus')

        if switch_state not in [self.ON, self.OFF]:
            raise ValueError(u'Switch state should be one of Switch.ON or Switch.OFF! ({v}).'.format(v=switch_state))

        # f take_focus is not None and u'takefocus' not in kwargs:
        #     kwargs.update({u'takefocus': take_focus})

        super(Switch, self).__init__(value=switch_state,
                                     onvalue=self.ON,
                                     offvalue=self.OFF,
                                     **kwargs)

    def __update_state(self):
        self._state = self.value

    def _switch_on_action(self):
        # Synchronise self.state & self._var as with trace above
        self.value = self._state

    def _switch_off_action(self):
        # Synchronise self.state & self._var as with trace above
        self.value = self._state
