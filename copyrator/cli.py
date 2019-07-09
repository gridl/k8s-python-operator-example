from argparse import ArgumentParser
from os import getenv

import kubernetes

from copyrator.load_crd import load_crd
from copyrator.operator import handle


try:
    kubernetes = kubernetes.config.load_incluster_config()
except kubernetes.config.config_exception.ConfigException:
    raise RuntimeError(
        'Не удалось прочитать конфигурацию кластера kubernetes.'
    )


def main():
    """
    Точка входа в приложения.
    Здесь происходит считывание настроек приложения из командной строки,
    переменных окружения и CRD, после чего запускается получение и обработка
    событий kubernetes.
    """
    parser = ArgumentParser(
        description='Copyrator - copy operator.',
        prog='copyrator'
    )
    parser.add_argument(
        '--namespace',
        type=str,
        default=getenv('NAMESPACE', 'default'),
        help='Operator Namespace (or ${NAMESPACE}), default: default'
    )
    parser.add_argument(
        '--rule-name',
        type=str,
        default=getenv('RULE_NAME', 'main-rule'),
        help='CRD Name (or ${RULE_NAME}), default: main-rule'
    )

    args = parser.parse_args()
    try:
        specs = load_crd(args.namespace, args.rule_name)
        handle(specs)

    except KeyboardInterrupt:
        pass

    except Exception as err:
        raise RuntimeError('Oh no! I am dying...') from err
