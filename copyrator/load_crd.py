import kubernetes

from copyrator.const import CRD_GROUP, CRD_VERSION, CRD_PLURAL

__all__ = [
    'load_crd',
]


def load_crd(namespace, name):
    """
    Метод для загрузки CRD.
    Используется для получения настроек слежения за сущеностями.
    """
    client = kubernetes.client.ApiClient()
    custom_api = kubernetes.client.CustomObjectsApi(client)

    crd = custom_api.get_namespaced_custom_object(
        CRD_GROUP,
        CRD_VERSION,
        namespace,
        CRD_PLURAL,
        name,
    )
    return {x: crd[x] for x in ('ruleType', 'selector', 'namespace')}
