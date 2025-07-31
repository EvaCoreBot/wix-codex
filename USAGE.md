# Usage Guide for wix-codex

This project helps you generate a basic HTML template for a Wix site using OpenAI's ChatCompletion (Codex) API. The generated HTML can then be imported into Wix or adapted in the Wix Editor.  

## Prerequisites

- **Python 3.8+** installed on your machine.
- An **OpenAI API key** with access to ChatCompletion models.
- Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Setting up your environment

Export your OpenAI API key so the script can authenticate with the service:

```bash
export OPENAI_API_KEY="sk-..."
```

Replace `sk-...` with your actual key. On Windows use `set` instead of `export`.

## Generating a site template

Run `generate_site.py` with a prompt describing the site you want. For example:

```bash
python generate_site.py --prompt "A personal blog with three sections: about me, blog posts, and contact form" --output my_blog.html
```

This will call OpenAI's API and write the generated HTML to `my_blog.html`. You can open this file in your browser to preview it or import it into Wix.

### Changing the model

By default, the script uses `gpt-3.5-turbo`. You can specify another model with the `--model` flag if you have access:

```bash
python generate_site.py --prompt "Simple one-page portfolio" --model gpt-4 --output portfolio.html
```

## Deploying to Wix

This project does **not** automatically publish the generated site to Wix. To deploy your HTML:

1. Log in to your Wix account.
2. Create a new site and choose **Custom Template** or start from blank.
3. Use the Wix Editor to add a new page and paste your generated HTML into an **Embed** element.
4. Alternatively, explore Wix's [REST API](https://dev.wix.com/docs/rest/api-reference) or CLI if you want to automate deployment. Note that programmatic site creation may require special permissions and is not covered in this repository.

## Contributing & Improvements

Feel free to open issues or pull requests if you find bugs or have ideas for enhancements, such as adding direct Wix API integration or improving the prompt templates for better layouts.

---

This guide complements the inline documentation in `generate_site.py` and should give you a quick start on using OpenAI to draft your Wix site.
