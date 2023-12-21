"""
ui module
"""
from src.board.board_exception import BoardException
from src.game.game import Game
from src.game.game_exception import GameWonException
from src.ui.ui_exception import UIException


class UI:

    def process_user_command(self, command):
        command = command.strip()
        tokens = command.split(" ", maxsplit=1)
        command = tokens[0]

        if len(tokens) == 1:
            return command, ""

        tokens = tokens[1]
        tokens.strip()

        return command, tokens

    def start(self):

        while True:

            user_input = input(">")
            command, tokens = self.process_user_command(user_input)

            if command == 'play':

                print("     Welcome to Connect Four     ")
                print("---------------------------------")

                game = Game()
                turns = 0
                print(game.board().create_board_as_string())

                while True:

                    if turns % 2 == 0:

                        try:
                            user_input = input(">")
                            command, tokens = self.process_user_command(user_input)

                            if command == 'exit':
                                return
                            else:
                                if command == 'A':
                                    command_col = 0
                                elif command == 'B':
                                    command_col = 1
                                elif command == 'C':
                                    command_col = 2
                                elif command == 'D':
                                    command_col = 3
                                elif command == 'E':
                                    command_col = 4
                                elif command == 'F':
                                    command_col = 5
                                elif command == 'G':
                                    command_col = 6
                                else:
                                    raise UIException("Invalid command!")

                                command_row = int(tokens)
                                if command_row not in [0, 1, 2, 3, 4, 5]:
                                    raise UIException("Invalid command!")

                                game.human_move(command_row, command_col)
                                turns += 1

                        except ValueError as ve:
                            print(str(ve))
                        except BoardException as be:
                            print(be.get_message())
                        except UIException as ue:
                            print(ue.get_message())
                        except GameWonException as ge:
                            print(ge.get_message())
                            print(game.board().create_board_as_string())
                            return

                    elif turns % 2 != 0:
                        try:
                            pos = game.computer_move()
                            turns += 1
                            print(game.board().create_board_as_string())
                            print("Computer move at " + str(pos))
                        except GameWonException as ge:
                            print(str(ge))
                            print(game.board().create_board_as_string())
                            return
                        except ValueError as ve:
                            print(str(ve))
                        except BoardException as be:
                            print(be.get_message())
                        except UIException as ue:
                            print(ue.get_message())

            elif command == 'exit':
                return

            else:
                print("Invalid command!")












