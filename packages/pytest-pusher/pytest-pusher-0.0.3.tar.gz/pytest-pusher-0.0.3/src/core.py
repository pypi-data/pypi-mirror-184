import os
from minio import Minio
from loguru import logger


pod_name = os.getenv('POD_NAME')
logger.add(f'{pod_name}/log.log')


def get_all_abs_path(source_dir):
    path_list = []
    for fpathe, dirs, fs in os.walk(source_dir):
        for f in fs:
            p = os.path.join(fpathe, f)
            path_list.append(p)
    return path_list


def pytest_addoption(parser, pluginmanager):
    mygroup = parser.getgroup("pusher")
    mygroup.addoption(
        "--host",
        # default='middleware-minio.tink:9000',
        default='tink.test:32703',
        dest='host',
        help='minio host'
    )
    mygroup.addoption(
        "--user",
        default='admin',
        dest='user',
        help='minio access key'
    )
    mygroup.addoption(
        "--password",
        default='changeme',
        dest='password',
        help='minio secret key'
    )

def pytest_unconfigure(config):
    try:
        host = config.getoption("host")
        user = config.getoption("user")
        password = config.getoption("password")
        allure_report_dir = config.getoption("allure_report_dir")

        os.system(
            f'allure generate --clean {allure_report_dir} -o {pod_name}/html > {pod_name}/log.log')

        minioClient = Minio(
            host,
            access_key=user,
            secret_key=password,
            secure=False
        )

        objs = get_all_abs_path(f'{pod_name}')
        for obj in objs:
            minioClient.fput_object('test', obj, obj)
        logger.info('push report to minio')

    except Exception as err:
        logger.debug(err)

