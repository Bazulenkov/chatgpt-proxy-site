# ChatGPT Proxy

This project is a proxy server that allows you to securely and easily use the OpenAI ChatGPT API from your local machine or network. It provides a simple API that can be used to interact with the ChatGPT API without exposing your credentials to the internet.

## Features

- Securely proxy requests to the OpenAI ChatGPT API
- Supports custom usernames and passwords for authentication
- Supports custom cookie settings for session management
- Supports pre-authorized users for convenience

## Prerequisites

- Python 3.9 or higher
- poetry (optional but recommended)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Bazulenkov/chatgpt-proxy-site.git
   ```

   and enter to the project root folder:

   ```shell
   cd chatgpt-proxy-site/
   ```
2. Install the dependencies:

   ```shell
   pip install .
   ```

3. Copy the sample configuration file:

   ```shell
   cp config.yaml.sample config.yaml
   ```

4. Edit the secrets file to set your API key and other options.

   ```shell
   mkdir -p .streamlit && echo 'OPENAI_API_KEY=<your_key>' >> .streamlit/secrets.toml
   ```

   or 

   ```shell
   EXPORT OPENAI_API_KEY=<your_key>
   ```
   
5. Start the proxy server:

   ```shell
   streamlit run chatgpt_proxy_site/chatbot.py
   ```

## Configuration Options

- `pre-authorized`: This section allows you to define pre-authorized users for convenience.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue. If you would like to contribute code, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.