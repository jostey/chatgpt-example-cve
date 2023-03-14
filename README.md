# chatgpt-example-cve
In this repository I have created a simple example of a ChatGPT API request to query through a prompt which products and versions of a technology are affected by a vulnerability (CVE) summary.

## Explanation
In this example we need to obtain the product followed by the affected versions and return the result in Spanish. To do this, our prompt in ChatGPT will be to give you several examples of questions and answers we want (inputs and outputs).

```
Q: Cross-site Scripting (XSS) - Stored in GitHub repository pimcore/pimcore prior to 10.5.19.
A: pimcore antes de 10.5.19.
Q: A issue has been discovered in GitLab CE/EE affecting all versions from 15.3 prior to 15.7.8, version 15.8 prior to 15.8.4, and version 15.9 prior to 15.9.2 A cross-site scripting vulnerability was found in the title field of work it...
A: GitLab CE/EE 15.3-15.7.8, 15.8-15.8.4 y 15.9-15.9.2
```

### Installation
We need to use the Python openai library and have a usable OpenAI token.
```
openai.api_key = "API_KEY" # https://platform.openai.com/account/api-keys
```
