from cli_utils.built_in_workers import HelpCliWorker, AbstractCliWorker, ExitCliWorker
from cli_utils.cli_workers_controller import CliWorkersController
from cli_utils.cli_word_processor import WordProcessor
from typing import List


class CliInterface:

    def __init__(
            self,
            cli_workers: List[AbstractCliWorker],
            is_case_sensitiveness_checked: bool=False,
            is_trim_used: bool=True,
            is_hint_used: bool=True,
            welcome_phrase: str="Welcome to the program"
    ):
        self.__word_processor = WordProcessor(
            is_trim_used=is_trim_used,
            is_case_sensitiveness_checked=is_case_sensitiveness_checked
        )
        cli_workers += [ExitCliWorker("exit", ["-e", "--exit"], "it makes you exit from the program")]
        cli_workers += [HelpCliWorker("help", ["-h", "--help"], "it helps you with other worker", cli_workers)]
        self.__cli_workers_controller = CliWorkersController(cli_workers=cli_workers)
        self.__welcome_phrase = welcome_phrase
        self.__is_hint_used = is_hint_used
        self.__arr_available_command = self.__cli_workers_controller.workers_commands
        self.__str_available_command = ", ".join(command for command in self.__arr_available_command)
        self.__command: str  = ""
        self.__command_option: str = ""
        self.__corrected_command: str = ""

    def run(self):
        self.__print_cli_app_header()
        while True:
            readed_input = input("> ").split()
            self.__command = readed_input[0]
            self.__command_option = readed_input[1] if readed_input.__len__() is 2 else ""
            self.__corrected_command = self.__word_processor.correct_command(self.__command)
            if self.__cli_workers_controller.is_command_available(self.__corrected_command):
                self.__manage_worker_job()
            elif self.__is_hint_used:
                self.__print_command_hint()
            else:
                print("incorrect command, press -h or --help for help")

    def __manage_worker_job(self):
        cli_worker = self.__cli_workers_controller.get_cli_worker(self.__command)
        cli_worker.work(self.__command_option)

    def __print_cli_app_header(self):
        print(self.__welcome_phrase)
        print("available commands are: " + self.__str_available_command)

    def __print_command_hint(self):
        similar_command = WordProcessor.get_similar_word(self.__corrected_command, self.__arr_available_command)
        print("incorrect command, maybe you intend " + similar_command)
