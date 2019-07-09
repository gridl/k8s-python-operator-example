k8s-python-operator-example
---------------------------
Kubernetes оператор, реализованный в качестве примера для [статьи на Habr](https://habr.com/ru/company/flant/blog/459320/).


#### Запуск оператора
```bash
usage: copyrator [-h] [--namespace NAMESPACE] [--rule-name RULE_NAME]

Copyrator - copy operator.

optional arguments:
  -h, --help            show this help message and exit
  --namespace NAMESPACE
                        Operator Namespace (or ${NAMESPACE}), default: default
  --rule-name RULE_NAME
                        CRD Name (or ${RULE_NAME}), default: main-rule
``` 
