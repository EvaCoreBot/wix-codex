#!/usr/bin/env python3
"""
Script to generate a static website template via OpenAI's API.

This script uses OpenAI's ChatCompletion (Codex) to generate an HTML
page based on a natural language description. The result is saved
locally as a file. You can then upload this file to Wix or use Wix's CLI
to create a site programmatically. For complete automation of site
creation on Wix, refer to Wix's REST API or CLI documentation.

Usage:
  python generate_site.py --prompt "A sleek portfolio for a designer" --output portfolio.html

Environment variables:
  OPENAI_API_KEY  Your OpenAI API key.

Dependencies:
  - openai (install via pip)

Note: This tool does not directly deploy the site to Wix. It generates
an HTML file that you can import or adapt within Wix. For programmatic
Wix site creation, see https://dev.wix.com/docs/rest/api-reference
"""

import argparse
import os
from typing import Any

import openai


def generate_html(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """Generate HTML content using OpenAI ChatCompletion.

    Args:
        prompt: A description of the website to create.
        model: The OpenAI model to use (default: gpt-3.5-turbo).

    Returns:
        A string containing the generated HTML.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable is not set")

    openai.api_key = api_key

    # Compose messages for ChatCompletion. We set the system prompt to
    # instruct the model to output valid HTML only.
    messages = [
        {
            "role": "system",
            "content": (
                "You are an assistant that generates clean, semantic HTML websites "
                "without any explanation or surrounding text."
            ),
        },
        {"role": "user", "content": f"Create a website: {prompt}"},
    ]

    response: Any = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=2000,
        temperature=0.7,
        n=1,
    )

    html_content = response["choices"][0]["message"]["content"]
    return html_content


def save_html(html: str, output_path: str) -> None:
    """Save HTML content to a file.

    Args:
        html: The HTML content.
        output_path: The path to save the file.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a static HTML file using OpenAI's API"
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Description of the website you want to generate",
    )
    parser.add_argument(
        "--output",
        default="index.html",
        help="Name of the output HTML file (default: index.html)",
    )
    parser.add_argument(
        "--model",
        default="gpt-3.5-turbo",
        help="OpenAI model to use (default: gpt-3.5-turbo)",
    )

    args = parser.parse_args()
    html = generate_html(args.prompt, args.model)
    save_html(html, args.output)
    print(f"Generated {args.output}")


if __name__ == "__main__":
    main()
