import openai
import json

# VARS
INPUT = "HashiCorp Nomad and Nomad Enterprise 1.4.0 up to 1.5.0 did not correctly enforce deny policies applied to a workload’s variables. Fixed in 1.4.6 and 1.5.1."
# https://platform.openai.com/account/api-keys
openai.api_key = "API_KEY"


def generate_prompt(input: str) -> str:
    return """Obtener productos y versiones en ESPAÑOL en formato JSON. Ejemplos.
    Q: IBM Business Automation Workflow 18.0.0, 18.0.1, 18.0.2, 19.0.1, 19.0.2, 19.0.3, 20.0.1, 20.0.2, 20.0.3, 21.0.1, 21.0.2, 21.0.3 y 22.0.1 es vulnerable a la falsificación de solicitudes entre sitios que podría permitir a un atacante ejecutar acciones maliciosas y no autorizadas transmitidas desde un usuario en el que confía el sitio web.
    A: {{\"product\": \"IBM Business Automation Workflow\", \"version\": \"18.0.0, 18.0.1, 18.0.2, 19.0.1, 19.0.2, 19.0.3, 20.0.1, 20.0.2, 20.0.3, 21.0.1, 21.0.2, 21.0.3 y 22.0.1\"}}
    Q: A double-free was found in the way 389-ds-base handles virtual attributes context in persistent searches.
    A: {{\"product\": \"389-ds-base\", \"version\": \"No se indica.\"}}
    Q: Cross-site Scripting (XSS) - Stored in GitHub repository pimcore/pimcore prior to 10.5.19.
    A: {{\"product\": \"pimcore\", \"version\": \"antes de 10.5.19.\"}}
    Q: A issue has been discovered in GitLab CE/EE affecting all versions from 15.3 prior to 15.7.8, version 15.8 prior to 15.8.4, and version 15.9 prior to 15.9.2 A cross-site scripting vulnerability was found in the title field of work it...
    A: {{\"product\": "GitLab CE/EE", \"version\": \"15.3-15.7.8, 15.8-15.8.4 y 15.9-15.9.2\"}}
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
