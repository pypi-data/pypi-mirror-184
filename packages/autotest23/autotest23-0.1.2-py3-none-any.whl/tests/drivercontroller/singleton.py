from subprocess import run


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def some_business_logic(self):
        run(['pytest', '--json-report', '--json-report-file=tests/report/report1.json', '--json-report-indent=4'], shell=True)