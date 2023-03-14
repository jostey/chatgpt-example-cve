import openai
import json

# VARS
INPUT = "Apache Log4j2 2.0-beta9 through 2.15.0 (excluding security releases 2.12.2, 2.12.3, and 2.3.1) JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. An attacker who can control log messages or log message parameters can execute arbitrary code loaded from LDAP servers when message lookup substitution is enabled. From log4j 2.15.0, this behavior has been disabled by default. From version 2.16.0 (along with 2.12.2, 2.12.3, and 2.3.1), this functionality has been completely removed. Note that this vulnerability is specific to log4j-core and does not affect log4net, log4cxx, or other Apache Logging Services projects. "
# https://platform.openai.com/account/api-keys
openai.api_key = "API_KEY"


def generate_prompt(input: str) -> str:
    return """Obtener productos y versiones en ESPAÑOL en formato JSON. Ejemplos.
    Q: IBM Business Automation Workflow 18.0.0, 18.0.1, 18.0.2, 19.0.1, 19.0.2, 19.0.3, 20.0.1, 20.0.2, 20.0.3, 21.0.1, 21.0.2, 21.0.3 y 22.0.1 es vulnerable a la falsificación de solicitudes entre sitios que podría permitir a un atacante ejecutar acciones maliciosas y no autorizadas transmitidas desde un usuario en el que confía el sitio web.
    A: [{{"product": "IBM Business Automation Workflow", "versions": "18.0.0, 18.0.1, 18.0.2, 19.0.1, 19.0.2, 19.0.3, 20.0.1, 20.0.2, 20.0.3, 21.0.1, 21.0.2, 21.0.3 y 22.0.1"}}]
    Q: A double-free was found in the way 389-ds-base handles virtual attributes context in persistent searches.
    A: [{{"product": "389-ds-base", "versions": "No se indica."}}]
    Q: Cross-site Scripting (XSS) - Stored in GitHub repository pimcore/pimcore prior to 10.5.19.
    A: [{{"product": "pimcore", "versions": "antes de 10.5.19."}}]
    Q: A issue has been discovered in GitLab CE/EE affecting all versions from 15.3 prior to 15.7.8, version 15.8 prior to 15.8.4, and version 15.9 prior to 15.9.2 A cross-site scripting vulnerability was found in the title field of work it...
    A: [{{"product": "GitLab CE/EE", "versions": "15.3-15.7.8, 15.8-15.8.4 y 15.9-15.9.2"}}]
    Q: Vulnerability in the Oracle Java SE, Oracle GraalVM Enterprise Edition product of Oracle Java SE (component: Serialization). Supported versions that are affected are Oracle Java SE: 7u321, 8u311, 11.0.13, 17.01; Oracle GraalVM Enterprise Edition: 20.3.4 and 21.3.0. Difficult to exploit vulnerability allows unauthenticated attacker with network access via multiple protocols.
    A: [{{"product": "Oracle Java SE", "versions": "7u321, 8u311, 11.0.13 y 17.01"}},{{"product": "Oracle GraalVM Enterprise Edition", "versions": "20.3.4 y 21.3.0"}}]
    Q: {}
    A: """.format(input)


def get_product_and_versions(input: str):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": generate_prompt(input)}]
    )
    print(json.dumps(json.loads(
        completion.choices[0].message.content), indent=2))


if __name__ == "__main__":
    get_product_and_versions(INPUT)
