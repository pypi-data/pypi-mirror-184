from alphatools.base_trading_app import BaseTradingApp
import configparser


class BackTestingApp(BaseTradingApp):
    def __init__(self, config_file):
        """

        :param config_file:
        """
        super.__init__()
        cfg_parser = configparser.ConfigParser()
        cfg_parser.read(config_file)
        print(cfg_parser.sections())

    def run(self):
        pass
