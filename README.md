# Flask Spotify Authentication Example

The Flask Spotify Authentication Example project is a practical demonstration of how to authenticate a user in a Spotify application using Flask, one of the most popular Python web frameworks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/AdaiasMagdiel/flask-spotify-authentication-example.git
   ```

2. Navigate to the project directory:

   ```shell
   cd flask-spotify-authentication-example
   ```

3. Create a virtual environment:

   ```shell
   python -m venv .venv
   ```

4. Activate the virtual environment:

   On Windows:

   ```shell
   .venv\Scripts\activate
   ```

   On macOS and Linux:

   ```shell
   source .venv/bin/activate
   ```

5. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Rename `.env.example` to `.env` and save your Spotify Client ID and Client Secret. To generate the Client ID and the Client Secret, see this article from the docs: [Starting with Spotify App](https://developer.spotify.com/documentation/web-api/concepts/apps)

## Usage

Now, just start your application.

```shell
python main.py
```

Your Flask application should now be running locally, and you can access it at `http://localhost:5000`.

## Project Structure

```
flask-spotify-authentication-example/
│
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── site.py
│   ├── __init__.py
│   └── settings.py
├── .env.example
├── main.py
├── README.md
└── requirements.txt
```

The `app` folder contains the core of the application, including routes and config files.

## Dependencies

- Flask
- python-dotenv
- httpx
- yapf
- ruff

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
