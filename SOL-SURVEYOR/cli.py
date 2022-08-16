import typer
from tx_collect import pull_transactions

app = typer.Typer()

@app.command("print_time")
def do_a_thing():
    pull_transactions()


if __name__ == "__main__": # Code inside this statement will only run if the file is explicitly called and not just imported.
    app()