from client.commands.Command import Command


class HelloWorld(Command):

    def run(self):
        print("\nHello World ;)")
