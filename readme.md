# Example Telegram bot

## How to run

Run by executing the `main.py` file.

## API Keys

Add your API keys to the api_keys.json file. It will be auto generated when you start the project.

You can modify api_keys.py to accommodate for new keys you have.

## How to add things

### New database entities (Models)

Create new classes for your new database entities inside the `models` package.

The new classes should extend `Base`

```python
class Example(Base):
    pass
```

### New commands

Inside `main.py`, you can add new handlers for commands, using code similar to the one bellow

Where `command_name` is the name of the command, `function_to_execute` is the callback. That is what function should run
when the command is called by the user.

```python application.add_handler(CommandHandler("command_name", function_to_execute))```

