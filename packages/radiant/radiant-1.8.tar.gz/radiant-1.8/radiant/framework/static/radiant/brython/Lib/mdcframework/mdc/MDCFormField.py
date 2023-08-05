"""
Brython MDCComponent: MDCFormField
==================================


"""

from .core import MDCTemplate
from browser import html

########################################################################
class MDCFormField(MDCTemplate):
    """"""
    NAME = 'formField', 'MDCFormField'

    MDC_optionals = {
        'end': 'mdc-form-field--align-end',
    }


    #----------------------------------------------------------------------
    def __new__(self, **kwargs):
        """"""
        self.element = self.render({}, kwargs)

        self.element.style = {'width': '100%',
                              'min-height': '48px',
                              # 'margin-bottom': '8px',
                              }

        return self.element



    #----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
            <div class="mdc-form-field {end}"></div>
        """
        return cls.render_html(code, context)





########################################################################
class MDCForm(MDCTemplate):
    """"""

    #----------------------------------------------------------------------
    def __new__(self, separator=None, formfield=None, formfield_style={}, **kwargs):
        """"""
        self.separator = separator
        self.formfield = formfield
        self.formfield_style = formfield_style
        self.element = self.render(locals(), kwargs)
        return self.element

    #----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
            <form></form>
        """
        return cls.render_html(code, context)



    #----------------------------------------------------------------------
    @classmethod
    def __genericElement__(cls, parent, Element, extern_label, *args, **kwargs):
        """"""
        if cls.formfield:
            formfield =  cls.formfield.clone()
        else:
            formfield = MDCFormField(style=cls.formfield_style)

        if cls.formfield_style:
            formfield = MDCFormField(style=cls.formfield_style)

        if 'formfield' in kwargs:
            formfield = kwargs['formfield']



        el = Element(*args, **kwargs)
        formfield <= el
        if extern_label:
            formfield <= __formLabel__(id_=el.mdc.get_id(), label=args[0])
        if kwargs.get('helper_text', False):
            # print(kwargs.get('helper_text_persistent'))
            formfield <= __formHelper__(id_=el.mdc.get_id(), label=kwargs.get('helper_text'), persistent=kwargs.get('helper_text_persistent', True))
        # cls.element <= formfield
        parent <= formfield

        if cls.separator:
            # cls.element <= cls.separator.clone()
            parent <= cls.separator.clone()

        return el, formfield


    #----------------------------------------------------------------------
    @classmethod
    def Checkbox(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(element, MDCCheckbox, True, *args, **kwargs)
        return el


    #----------------------------------------------------------------------
    @classmethod
    def Radio(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(element, MDCRadio, True, *args, **kwargs)
        return el


    #----------------------------------------------------------------------
    @classmethod
    def Select(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(element, MDCSelect, False, *args, **kwargs)
        return el


    #----------------------------------------------------------------------
    @classmethod
    def Slider(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(element, MDCSlider, False, *args, **kwargs)
        return el


    #----------------------------------------------------------------------
    @classmethod
    def Switch(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(element, MDCSwitch, True, *args, **kwargs)
        return el


    #----------------------------------------------------------------------
    @classmethod
    def TextField(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(element, MDCTextField, False, *args, **kwargs)
        element.style = {'display': 'flow-root'}
        el.style = {'margin-top': 'unset'}
        return el


    #----------------------------------------------------------------------
    @classmethod
    def TextAreaField(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(element, MDCTextAreaField, False, *args, **kwargs)
        element.style = {'display': 'flow-root'}
        el.style = {'margin-top': '8px'}
        return el




########################################################################
class __formLabel__(MDCTemplate):
    """"""

    #----------------------------------------------------------------------
    def __new__(self, id_, label):
        """"""
        code = """
            <label for="{id_}">{label}</label>
            """.format(id_=id_, label=label)
        return self.render_str(code)


########################################################################
class __formHelper__(MDCTemplate):
    """"""

    #----------------------------------------------------------------------
    def __new__(self, id_, label, persistent=True):
        """"""
        if persistent:
            persistent = 'mdc-text-field-helper-text--persistent'
        else:
            persistent = ''
        code = """
            <p id="{id_}" class="mdc-text-field-helper-text {persistent}" aria-hidden="true">
              {label}
            </p>
            """.format(id_=id_, label=label, persistent=persistent)
        return self.render_str(code)




########################################################################
class MDCCheckbox(MDCTemplate):
    """"""
    NAME = 'checkbox', 'MDCCheckbox'

    MDC_optionals = {

        'disabled': 'mdc-checkbox--disabled',
        'checked': 'checked',

    }


    #----------------------------------------------------------------------
    def __new__(self, label, name='', value='', checked=False, disabled=False, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        # self.element.need_label = True
        return self.element




    #----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        code = """
              <div class="mdc-checkbox">
                <input type="checkbox"
                       id="{id}"
                        name="{name}"
                        value="{value}"
                       class="mdc-checkbox__native-control"
                       {input_disabled}
                       {checked}
                       />
                <div class="mdc-checkbox__background">
                  <svg class="mdc-checkbox__checkmark"
                       viewBox="0 0 24 24">
                    <path class="mdc-checkbox__checkmark-path"
                          fill="none"
                          stroke="white"
                          d="M1.73,12.91 8.1,19.28 22.79,4.59"/>
                  </svg>
                  <div class="mdc-checkbox__mixedmark"></div>
                </div>
              </div>
        """
        return cls.render_html(code, context)


########################################################################
class MDCRadio(MDCTemplate):
    """"""
    NAME = 'radio', 'MDCRadio'

    MDC_optionals = {

        'disabled': 'mdc-radio--disabled',
        'checked': 'checked',

    }


    #----------------------------------------------------------------------
    def __new__(self, label, name='', checked=False, disabled=False, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        # self.element.need_label = True
        return self.element


    #----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        code = """
            <div class="mdc-radio {disabled}">
              <input class="mdc-radio__native-control" type="radio" id="{id}" name="{name}" {input_disabled} {checked}>
              <div class="mdc-radio__background">
                <div class="mdc-radio__outer-circle"></div>
                <div class="mdc-radio__inner-circle"></div>
              </div>
            </div>
        """
        return cls.render_html(code, context)


########################################################################
class MDCSelect(MDCTemplate):
    """"""
    NAME = 'select', 'MDCSelect'

    MDC_optionals = {

        'disabled': 'mdc-select--disabled',
        'box': 'mdc-select--box',

    }


    #----------------------------------------------------------------------
    def __new__(self, label, options=[], selected=None, disabled=False, box=False, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        # self.element.need_label = False

        if options:
            self.add_options(self.element, options, selected)

        return self.element


    #----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        code = """
            <div class="mdc-select {box} {disabled}" style="width: 100%">
              <select class="mdc-select__native-control" {input_disabled}>

              </select>
              <label class="mdc-floating-label">{label}</label>
              <div class="mdc-line-ripple"></div>
            </div>
        """
        return cls.render_html(code, context)



    #----------------------------------------------------------------------
    @classmethod
    def __getitem__(self, name):
        """"""
        if name is 'options_placeholder':
            return self.element.select('.mdc-select__native-control')[0]
        elif name is 'label':
            return self.element.select('.mdc-floating-label')[0]



    #----------------------------------------------------------------------
    @classmethod
    def add_option(cls, element, label, value, selected=False, disabled=False):
        """"""
        option = html.OPTION(label, value=value, selected=selected, disabled=disabled)
        cls['options_placeholder'] <= option
        return option


    #----------------------------------------------------------------------
    @classmethod
    def add_options(cls, element, options, selected=None):
        """"""
        if selected is None:
            cls.add_option(element, '', '', selected=True)
        else:
            cls['label'].class_name += ' mdc-floating-label--float-above'

        for option in options:
            cls.add_option(element, *option, option[1] == selected)


########################################################################
class MDCSlider(MDCTemplate):
    """"""
    NAME = 'slider', 'MDCSlider'

    MDC_optionals = {

        'disabled': 'aria-disabled="true"',
        # 'box': 'mdc-select--box',

    }


    #----------------------------------------------------------------------
    def __new__(self, label, min=0, max=100, step=1, valuenow=0, discrete=False, continuous=False, disabled=False, markers=False, **kwargs):
        """"""

        if not discrete and not continuous:
            continuous = True

        self.element = self.render(locals(), kwargs)
        # self.element.need_label = False

        return self.element


    #----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        if context['markers']:
            context['display_marker'] = 'mdc-slider--display-markers'
            context['marker_container'] = '<div class="mdc-slider__track-marker-container"></div>'
        else:
            context['display_marker'] = ''
            context['marker_container'] = ''


        if context.get('continuous'):
            code = """
                <div class="mdc-slider" tabindex="0" role="slider"
                     aria-valuemin="{min}" aria-valuemax="{max}" data-step="{step}" aria-valuenow={valuenow}"
                     aria-label="Select Value"
                     {disabled}>
                  <div class="mdc-slider__track-container">
                    <div class="mdc-slider__track"></div>
                  </div>
                  <div class="mdc-slider__thumb-container">
                    <svg class="mdc-slider__thumb" width="21" height="21">
                      <circle cx="10.5" cy="10.5" r="7.875"></circle>
                    </svg>
                    <div class="mdc-slider__focus-ring"></div>
                  </div>
                </div>
            """
        elif context.get('discrete'):
            code = """
                <div class="mdc-slider mdc-slider--discrete {display_marker}" tabindex="0" role="slider"
                     aria-valuemin="{min}" aria-valuemax="{max}" data-step="{step}" aria-valuenow="{valuenow}"
                     aria-label="Select Value">
                  <div class="mdc-slider__track-container">
                    <div class="mdc-slider__track"></div>
                    {marker_container}
                  </div>
                  <div class="mdc-slider__thumb-container">
                    <div class="mdc-slider__pin">
                      <span class="mdc-slider__pin-value-marker"></span>
                    </div>
                    <svg class="mdc-slider__thumb" width="21" height="21">
                      <circle cx="10.5" cy="10.5" r="7.875"></circle>
                    </svg>
                    <div class="mdc-slider__focus-ring"></div>
                  </div>
                </div>
            """


        return cls.render_html(code, context)


########################################################################
class MDCSwitch(MDCTemplate):
    """"""
    NAME = 'switch', 'MDCSwitch'

    MDC_optionals = {

        'disabled': 'disabled',
        # 'box': 'mdc-select--box',

    }


    #----------------------------------------------------------------------
    def __new__(self, label, disabled=False, **kwargs):
        """"""

        self.element = self.render(locals(), kwargs)
        return self.element


    #----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        code = """
            <div class="mdc-switch">
              <input type="checkbox" id="{id}" class="mdc-switch__native-control" role="switch" {disabled}>
              <div class="mdc-switch__background">
                <div class="mdc-switch__knob"></div>
              </div>
            </div>
        """
        return cls.render_html(code, context)


########################################################################
class MDCTextField(MDCTemplate):
    """"""
    NAME = 'textField', 'MDCTextField'

    MDC_optionals = {

        'disabled': 'mdc-text-field--disabled',
        'dense': 'mdc-text-field--dense',
        # 'box': 'mdc-select--box',
        # 'fullwidth': 'mdc-text-field--fullwidth',

        'value': 'value="{value}"',


    }


    #----------------------------------------------------------------------
    def __new__(self, label, value=False, type='text', leading_icon=False, trailing_icon=False, helper_text=False, helper_text_persistent=True, outlined=False, box=False, dense=False, disabled=False, fullwidth=False, **kwargs):
        """"""

        self.element = self.render(locals(), kwargs)
        return self.element


    #----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        if context['value']:
            context['upgraded'] = 'mdc-text-field--upgraded'
        else:
            context['upgraded'] = ''

        if context['helper_text']:
            context['helper_text'] = 'aria-controls="username-helper-text" aria-describedby="username-helper-text"'
        else:
            context['helper_text'] = ''

        if context['leading_icon']:
            context['icon'] = '<i class="material-icons mdc-text-field__icon" tabindex="0" role="button">{icon}</i>'.format(icon=context['leading_icon'])
            context['leading_icon'] = 'mdc-text-field--with-leading-icon'

        elif context['trailing_icon']:
            context['icon'] = '<i class="material-icons mdc-text-field__icon" tabindex="0" role="button">{icon}</i>'.format(icon=context['trailing_icon'])
            context['trailing_icon'] = 'mdc-text-field--with-trailing-icon'

        else:
            context['leading_icon'] = ''
            context['trailing_icon'] = ''
            context['icon'] = ''



        if not context.get('fullwidth'):
            if context.get('outlined'):
                code = """
                    <div class="mdc-text-field mdc-text-field--outlined {disabled} {upgraded} {dense} {leading_icon} {trailing_icon}">
                      {icon}
                      <input type="{type}" id="{id}" class="mdc-text-field__input" {input_disabled} {value} {helper_text}>
                      <label class="mdc-floating-label" for="{id}">{label}</label>
                        <div class="mdc-notched-outline">
                          <svg><path class="mdc-notched-outline__path"/></svg>
                        </div>
                        <div class="mdc-notched-outline__idle"></div>
                    </div>
                """
            elif context.get('box'):
                code = """
                    <div class="mdc-text-field mdc-text-field--box {disabled} {upgraded} {dense} {leading_icon} {trailing_icon}">
                      {icon}
                      <input type="{type}" id="{id}" class="mdc-text-field__input" {input_disabled} {value} {helper_text}>
                      <label class="mdc-floating-label" for="{id}">{label}</label>
                      <div class="mdc-line-ripple"></div>
                    </div>
                """
            else:
                code = """
                    <div class="mdc-text-field {disabled} {upgraded} {dense}">
                      <input type="{type}" id="{id}" class="mdc-text-field__input" {input_disabled} {value} {helper_text}>
                      <label class="mdc-floating-label" for="{id}">{label}</label>
                      <div class="mdc-line-ripple"></div>
                    </div>
                """
        else:
            code = """
            <div class="mdc-text-field mdc-text-field--fullwidth {upgraded} {dense}">
              <input class="mdc-text-field__input" id="{id}" type="{type}" {value}
                     placeholder="{label}" aria-label="{label}" {helper_text}>
            </div>
            """



        return cls.render_html(code, context)





########################################################################
class MDCTextAreaField(MDCTemplate):
    """"""
    NAME = 'textField', 'MDCTextField'

    MDC_optionals = {

        'disabled': 'mdc-text-field--disabled',
        # 'dense': 'mdc-text-field--dense',
        # 'box': 'mdc-select--box',
        'fullwidth': 'mdc-text-field--fullwidth',

        # 'value': 'value="{value}"',


    }


    #----------------------------------------------------------------------
    def __new__(self, label, value='', rows='2', cols='40', helper_text=False, helper_text_persistent=True, dense=False, disabled=False, fullwidth=False, **kwargs):
        """"""

        self.element = self.render(locals(), kwargs)
        return self.element



    #----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        if context['helper_text']:
            context['helper_text'] = 'aria-controls="username-helper-text" aria-describedby="username-helper-text"'
        else:
            context['helper_text'] = ''

        code = """
            <div class="mdc-text-field mdc-text-field--textarea {fullwidth} {dense} {disabled}">
              <textarea id="{id}" class="mdc-text-field__input" rows="{rows}" cols="{cols}" {helper_text} {input_disabled}>{value}</textarea>
              <label for="{id}" class="mdc-floating-label">{label}</label>
            </div>
        """


        return cls.render_html(code, context)