class DataProvider(object):
    def __init__(self):
        self.name = self.get_provider_name()
        self.version = self.get_provider_version()

        self.connection = self.establish_connection()

        self.templates = self.get_all_templates()

    def get_provider_name(self):
        raise NotImplementedError

    def get_provider_version(self):
        raise NotImplementedError

    def establish_connection(self):
        raise NotImplementedError

    def get_template_path(self):
        return 'editorial_staff/providers/{}/v{}'.format(
            self.name,
            self.version
        )

    def get_creation_header_template(self):
        return '{}/creation_header.html'.format(self.get_template_path())

    def get_creation_form_template(self):
        return '{}/creation_form.html'.format(self.get_template_path())

    def get_update_button_template(self):
        return '{}/update_button.html'.format(self.get_template_path())

    def get_update_progress_modal_template(self):
        return '{}/update_progress_modal.html'.format(self.get_template_path())

    def get_all_templates(self):
        return {
            'creation_header': self.get_creation_header_template(),
            'creation_form': self.get_creation_form_template(),
            'update_button': self.get_update_button_template(),
            'update_progress_modal': self.get_update_progress_modal_template(),
        }

    # Provider functions (must be extended for subclasses to work):
    def get_all_staffers(self, include_bots=False, include_deleted=False,
                         excluded_email_domains=[]):
        raise NotImplementedError

    def get_staffer(self, queried_email, excluded_email_domains=[]):
        raise NotImplementedError

    def format_staffer(self, user_data, exclude_email=False):
        raise NotImplementedError

    def post_new_staffer_message(self, options, staffer):
        raise NotImplementedError
