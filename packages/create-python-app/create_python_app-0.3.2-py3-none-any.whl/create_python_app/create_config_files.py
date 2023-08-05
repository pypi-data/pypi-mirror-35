from create_python_app.path_utils import *

_logging_config_name= "logging.json"
_logging_config_content= f"""\
{{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {{
        "simple": {{
            "format": "%(levelname)s - %(asctime)s - %(name)s:%(lineno)d - %(message)s"
        }}
    }},

    "handlers": {{
        "console": {{
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }},

        "info_file_handler": {{
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "info.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }},

        "error_file_handler": {{
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": "errors.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }}
    }},
    "loggers": {{
        "my_module": {{
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": "no"
        }}
    }},

    "root": {{
        "level": "DEBUG",
        "handlers": ["console", "info_file_handler", "error_file_handler"]
    }}
}}
"""
_sys_config_name= "sys.json"
_sys_config_content= f"""{{}}"""

def create_config_files(base_dir, **kwargs):
    config_dir = create_dir(base_dir, "config")
    create_file(base_dir, config_dir, _logging_config_name, content=_logging_config_content)
    create_file(base_dir, config_dir, _sys_config_name, content=_sys_config_content)