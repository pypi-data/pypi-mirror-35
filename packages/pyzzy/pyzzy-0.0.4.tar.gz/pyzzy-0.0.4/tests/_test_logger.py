import pyzzy as pz
import commons


CWD = pz.set_working_directory(__file__)

conf = CWD + "/configurations/logging.json"

conf = pz.load_yaml(conf)
pz.init_logging(conf, raise_exceptions=True)

dvpt_logger = pz.getLogger("development")
main_logger = pz.getLogger(__name__)
root_logger = pz.getLogger()


def test_logger():

    print(" development logger ".center(55, "-"))
    commons.use_logger(dvpt_logger)
    commons.logger_infos(dvpt_logger)

    print(" __main__ logger ".center(55, "-"))
    commons.use_logger(main_logger)
    commons.logger_infos(main_logger)

    print(" root logger ".center(55, "-"))
    commons.use_logger(root_logger)
    commons.logger_infos(root_logger)


def use_warnings():
    import warnings
    print(" warnings.warn ".center(55, "-"))
    warnings.warn("Message from 'warnings' module")


if __name__ == "__main__":
    test_logger()
    use_warnings()
