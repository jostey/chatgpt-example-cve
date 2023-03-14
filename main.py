import openai

# VARS
# Source: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27581
INPUT = "github-slug-action is a GitHub Action to expose slug value of GitHub environment variables inside of one's GitHub workflow. Starting in version 4.0.0` and prior to version 4.4.1, this action uses the `github.head_ref` parameter in an insecure way. This vulnerability can be triggered by any user on GitHub on any workflow using the action on pull requests. They just need to create a pull request with a branch name, which can contain the attack payload. This can be used to execute code on the GitHub runners and to exfiltrate any secrets one uses in the CI pipeline. A patched action is available in version 4.4.1. No workaround is available. "
# https://platform.openai.com/account/api-keys
openai.api_key = "API_KEY"


def generate_prompt(input):
    return """Obtener productos y versiones en ESPAÑOL. Ejemplos.
    Q: IBM Business Automation Workflow 18.0.0, 18.0.1, 18.0.2, 19.0.1, 19.0.2, 19.0.3, 20.0.1, 20.0.2, 20.0.3, 21.0.1, 21.0.2, 21.0.3 y 22.0.1 es vulnerable a la falsificación de solicitudes entre sitios que podría permitir a un atacante ejecutar acciones maliciosas y no autorizadas transmitidas desde un usuario en el que confía el sitio web.
    A: IBM Business Automation Workflow 18.0.0, 18.0.1, 18.0.2, 19.0.1, 19.0.2, 19.0.3, 20.0.1, 20.0.2, 20.0.3, 21.0.1, 21.0.2, 21.0.3 y 22.0.1
    Q: A double-free was found in the way 389-ds-base handles virtual attributes context in persistent searches.
    A: No se indica.
    Q: Cross-site Scripting (XSS) - Stored in GitHub repository pimcore/pimcore prior to 10.5.19.
    A: pimcore antes de 10.5.19.
    Q: A issue has been discovered in GitLab CE/EE affecting all versions from 15.3 prior to 15.7.8, version 15.8 prior to 15.8.4, and version 15.9 prior to 15.9.2 A cross-site scripting vulnerability was found in the title field of work it...
    A: GitLab CE/EE 15.3-15.7.8, 15.8-15.8.4 y 15.9-15.9.2
    Q: {}
    A: """.format(input)


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": generate_prompt(INPUT)}]
)

print(completion.choices[0].message.content)
