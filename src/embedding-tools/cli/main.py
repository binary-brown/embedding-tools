import typer
import asyncio
from pathlib import Path

APP_NAME = "embedding_tools"

main_app = typer.Typer(
    name=APP_NAME, help="Tools for embedding documents into postgresql vector store."
)


async def main():
    print("Hello, world!")


@main_app.callback()
async def callback():
    print("Hello, world!")


if __name__ == "__main__":
    asyncio.run(main())
