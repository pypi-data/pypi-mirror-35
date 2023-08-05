
import inspect
import threading
from kervi.spine import Spine
from kervi.core.utility.component import KerviComponent

ACTION_STOPPED = "stopped"
ACTION_RUNNING = "running"
ACTION_SUCCESS = "success"
ACTION_FAILED = "failed"
ACTION_PENDING = "pending"

class _LinkedAction(object):
    def __init__(self, action_id):
        self._action_id = action_id
        self.spine = Spine()
        self.spine.register_event_handler("actionDone", self._action_done, action_id)
        self.spine.register_event_handler("actionStarted", self._action_started, action_id)
        self.spine.register_query_handler("getComponentRoutes", self._get_component_bus_routes)
        self._state = ACTION_STOPPED
        self._action_event = None
        self._action_lock = threading.Lock()
        self._process_locked = False
        self._is_running = False
        self._last_result = None

    
    def _get_component_bus_routes(self):
        return {
            "id": None,
            "routes": [
                {
                    "id": self._action_id,
                    "direction": "in",
                    "topic_type": "event",
                    "topic": "actionStarted"
                },
                {
                    "id": self._action_id,
                    "direction": "in",
                    "topic_type": "event",
                    "topic": "actionDone"
                },
                {
                    "id": self._action_id,
                    "direction": "out",
                    "topic_type": "command",
                    "topic": "kervi_action_" + self._action_id
                }
            ],
        }

    def _action_done(self, id, state, result):
        if self._state == ACTION_RUNNING:
            self._state = state

        self._last_result = result
        if self._action_event:
            self._action_event.set()

        if self._process_locked:
            self._process_locked = False
            self._action_lock.release()
        self._is_running = False

    def _action_started(self, id):
        self._state = ACTION_RUNNING
        self._last_result = None
        self._is_running = True
        if self._action_lock.acquire(False):
            self._process_locked = True

    @property
    def is_running(self):
        return self._is_running

    @property
    def state(self):
        """Returns the running state of the action."""
        return self._state

    def interrupt(self, *args, **kwargs):
        self.spine.send_command("kervi_action_interrupt_" + self._action_id, *args, **kwargs)

    def execute(self, *args, **kwargs):
        """Executes the action."""
        timeout = kwargs.pop("timeout", -1)
        run_async = kwargs.pop("run_async", False)
        self._is_running = True
        result = None
        if self._action_lock.acquire(False):
            self._state = ACTION_PENDING
            self._action_event = threading.Event()
            self.spine.send_command("kervi_action_" + self._action_id, *args, **kwargs)

            if not run_async:
                if self._action_event.wait(timeout):
                    self._state = ACTION_FAILED
                    raise TimeoutError("Timeout in call to action: " + self._action_id)
                self._action_event = None
                result = self._last_result
            else:
                self._action_lock.release()

        else:
            if not self._action_lock.acquire(True, timeout):
                return None
            self._action_lock.release()
            return result

    def __call__(self, *args, **kwargs):
        self.execute(*args, **kwargs)

class _ActionThread(threading.Thread):
    def __init__(self, action, args, kwargs):
        super().__init__()
        self._action = action
        self.deamon = True
        self._args = args
        self._kwargs = kwargs
        self.result = None

    def run(self):
        self.result = self._action._execute(*self._args, **self._kwargs)

class _ActionInterrupt():
    def __init__(self, interrupt):
        self._interrupt = interrupt
        argspec = inspect.getargspec(interrupt)
        self._keywords = argspec.keywords != None

    def __call__(self, *args, **kwargs):
        if self._keywords:
            self._interrupt(*args, **kwargs)
        else:
            self._interrupt(*args)

class Action(KerviComponent):
    """The Action class is used by the action decorator. A function or method that is marked with @actions os converted to an Action class"""
    def __init__(self, handler, action_id, name=None):
        super().__init__(action_id, "KerviAction", name)
        self.action_id = action_id
        self._handler = handler
        argspec = inspect.getargspec(handler)
        self._keywords = argspec.keywords != None
        #print("kw", self.action_id, self._keywords, argspec, handler)
        self.spine = Spine()
        self.spine.register_command_handler("kervi_action_" + action_id, self._handle_command)
        self.spine.register_command_handler("kervi_action_interrupt_" + action_id, self.interrupt)
        self._state = ACTION_STOPPED
        self._action_lock = threading.Lock()
        self._last_result = None
        self._is_running = False
        self._interrupt = None

        self._ui_parameters = {
            "link_to_header": False,
            "label_icon": None,
            "label": self.name,
            "label_size":0,
            "flat": False,
            "inline": False,
            "is_input":True,
            "value_size":3,
            "width":0,
            "height":0
        }

        self._ui_parameters["type"] = "button"
        self._ui_parameters["on_text"] = "On"
        self._ui_parameters["off_text"] = "Off"
        self._ui_parameters["on_icon"] = None
        self._ui_parameters["off_icon"] = None
        self._ui_parameters["button_icon"] = None
        self._ui_parameters["button_text"] = self.name,
        self._ui_parameters["button_width"] = None
        self._ui_parameters["button_height"] = None,
        self._ui_parameters["input_size"] = 0
        self._ui_parameters["action_parameters"] = []
        #self._ui_parameters["run_command"] = "kervi_action_" + action_id
        #self._ui_parameters["interrupt_command"] = "kervi_action_interrupt_" + action_id
        self._ui_parameters["interrupt_parameters"] = []
        self._ui_parameters["interrupt_enabled"] = False

    def _execute(self, *args, **kwargs):
        kwargs.pop("injected", None) # signaling from zmq bus
        self._state = ACTION_RUNNING
        self._is_running = True
        result = None
        try:
            if self._keywords:
                result = self._handler(*args, **kwargs)
            else:
                result = self._handler(*args)
            self._state = ACTION_SUCCESS

        except Exception as e:
            print("action failed:", self.action_id, e)
            self._state = ACTION_FAILED
        self.spine.trigger_event("actionDone", self.action_id, self._state, result)
        self._last_result = result
        self._action_lock.release()
        self._is_running = False
        return result

    def __call__(self, *args, **kwargs):
        return self.execute(*args, **kwargs)

    def _handle_command(self, *args, **kwargs):
        if self._action_lock.acquire(False):
            self.spine.trigger_event("actionStarted", self.action_id)
            thread = _ActionThread(self, args, kwargs)
            thread.start()

    def execute(self, *args, **kwargs):
        """ 
            Executes the action and returns the result. 
            You dont have to call this function directly as the class is callable (implements __call__)
            you just call the @action marked function as normal.

            @action
            def my_action(p1)
                print(p1)

            my_action("x")

            :Keyword Arguments:

            * *link_to_header* (``str``) -- Link this action to the header of the panel.
         """

        timeout = kwargs.pop("timeout", -1)
        execute_async = kwargs.pop("run_async", False)
        result = None
        if self._action_lock.acquire(False):
            try:
                self.spine.trigger_event("actionStarted", self.action_id)
                if timeout == -1 and not execute_async:
                    result = self._execute(*args, **kwargs)
                else:
                    thread = _ActionThread(self, args, kwargs)
                    thread.start()
                    if not execute_async:
                        thread.join(timeout)
                        if thread.is_alive():
                            result = None
                            raise TimeoutError("Timeout in call to action: " + self.action_id)
                        else:
                            result = thread.result
                    else:
                        result = thread
                return result
            finally:
                pass
            #    self._action_lock.release()
        else:
            if not self._action_lock.acquire(True, timeout):
                return None
            self._action_lock.release()
            return self._last_result

    def interrupt(self, *args, **kwargs):
        print("interrupt; ", self.action_id)
        if self._interrupt:
            self._interrupt(*args, **kwargs)

    @property
    def is_running(self):
        """"Is true if the action is executing. You can use it together with the timeout parameter in the call to execute"""
        return self._is_running

    @property
    def state(self):
        return self._state

    def _get_info(self, **kwargs):
        return {
            "runCommand":"kervi_action_" + self.action_id,
            "interruptCommand":"kervi_action_interrupt_" + self.action_id,
            "running":self._is_running
        }

    def _get_bus_routes(self):
        result = [
            {
                "id": None,
                "direction": "in",
                "topic_type": "command",
                "topic": "kervi_action_" + self.action_id
            },
            {
                "id": None,
                "direction": "in",
                "topic_type": "command",
                "topic": "kervi_action_interrupt_" + self.action_id
            }
        ]
        return result

    def link_to_dashboard(self, dashboard_id=None, panel_id=None, **kwargs):
        r"""
        Links this action to a dashboard panel.

        :param dashboard_id:
            Id of the dashboard to link to.
        :type dashboard_id: str
        
        :param panel_id:
            Id of the panel on the dashboard to link to.
        :type panel_id: str
        


        :Keyword Arguments:
            
            * *link_to_header* (``str``) -- Link this acton to the header of the panel.

            * *label_icon* (``str``) -- Icon that should be displayed together with label.

            * *label* (``str``) -- Label text, default value is the name of the action.

            * *flat* (``bool``) -- Flat look and feel.

            * *inline* (``bool``) -- Display button and label in its actual size
                If you set inline to true the size parameter is ignored.
                The action will only occupy as much space as the label and input takes.

            * *input_size* (``int``) -- width of the slider as a percentage of the total container it sits in.

            * *value_size* (``int``) -- width of the value area as a percentage of the total container it sits in.

            * *type* (``string``) -- if value should be displayes as a 'switch' (default) or 'push' for push button.

            * *on_text* (``string``) -- Text to display when switch is on.
            * *off_text* (``string``) -- Text to display when switch is off.
            * *on_icon* (``string``) -- Icon to display when switch is on.
            * *off_icon* (``string``) -- Icon to display when switch is off.

            * *button_icon* (``string``) -- Icon to display on button.
            * *button_text* (``string``) -- Text to display on button, default is name.

            * *action_parameters* (``list``) -- List of parameters to pass to the action.
            
            * *interrupt_enabled* (``bool``) -- If true the button will send interrupt to action on off. Default true if an interrupt is specified for the action.
            * *interrupt_parameters* (``list``) -- List of parameters to pass to the interrupt function of the action.
            
        """
        KerviComponent.link_to_dashboard(
            self,
            dashboard_id,
            panel_id,
            **kwargs
        )


    def set_interrupt(self, method=None, **kwargs):
        """
            Decorator that turns a function or controller method into an action interrupt.

        """
        
        def action_wrap(f):
            action_id = kwargs.get("action_id", f.__name__)
            name = kwargs.get("name", action_id)
            if not "." in f.__qualname__:
                self._interrupt = _ActionInterrupt(f)
                self._ui_parameters["interrupt_enabled"] = True
                return self._interrupt
            else:
                Actions.add_unbound_interrupt(f.__qualname__, self)
                return f
        
        if method:
            return action_wrap(method)
        else:
            return action_wrap