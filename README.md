# 🔥 FreeGPT

[![Python](https://img.shields.io/badge/python-3.8-blue.svg)](https://img.shields.io/badge/python-3.8-blue.svg)

_⭐️ Like this repo? please star & consider donating to keep it maintained_

_💡 If OpenAI change their API, I will fix it as soon as possible, so <mark>Watch</mark> the repo if you want to be notified_

_The purpose of this project is not to leak the API, its just mine practice. It's just for educational purposes._

### Features

- [x] Free Open API for everyone
- [x] Change token
- [x] Saves token and conversation
- [x] Reset API's token and conversation when you want
- [x] Open-source, deployed on Vercel, free for all
- [x] No leak of any information (when sending prompt or resetting API's conversation)

I would not add any illegal features to the API like token collection or conversation exporting, since it is not legal to view what someone might ask or their token. Here's what things, if you would contribute, to not add:

- [ ] Token collection/saving
- [ ] Saving prompts and/or responses to file
- [ ] Logging any info

Feel free to test our my project and star it. I reverse engineered ChatGPT API too, so the gpt.py in API directory is written by me. Thanks!

## Usage

Hosted on Vercel. The main route of URL: `https://freegpt-api.vercel.app/`. All API requests should be sent to this URL.

### /

It is not a API at the root, would redirect you back to the github project.

### /api/token

To change the API's token, send a POST request with a token specifying your token at /api/token:

```bash
curl -X POST -d "token=YOUR_ACCESS_TOKEN_HERE" http://localhost:3000/api/token
```

> Server will automatically test your token by sending a test prompt. Rate-limited tokens would give you a key `error`, success will give key `message` with readable messages.

### /api/prompt

After the API is ready with a token, you can ask it prompts. API route: /api/prompt. Include a `prompt` with the request..

```bash
curl -X POST -d "prompt=Hey GPT!" http://localhost:3000/api/prompt
```

When no token was initalized with, the return would be:

```json
{
  "error": "Server-related error, the token could have been rate limited. If you didn't specify a token, please specify it."
}
```

On a success request:

```json
{ "response": "The API response here" }
```

### /api/reset

To reset bot's conversation, send a POST request with no values at /api/reset

```bash
curl -X POST -d http://localhost:3000/api/reset
```

Bot will unspecify the token and the conversation ID, forgiving all you asked it.

### Credits

- [OpenAI](https://openai.com/) for creating the ChatGPT API
- [ashishagarwal2023](https://github.com/ashishagarwal2023) for the API and reverse-engineering
