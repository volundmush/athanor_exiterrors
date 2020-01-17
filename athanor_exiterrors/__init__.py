def load(settings):
    settings.CMDSETS["CHARACTER"].extend(["athanor_exiterrors.exit_errors.ExitErrorCmdSet"])
