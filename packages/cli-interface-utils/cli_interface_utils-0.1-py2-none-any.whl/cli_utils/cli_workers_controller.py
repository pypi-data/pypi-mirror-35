from cli_utils.built_in_workers.abstract_cli_worker import AbstractCliWorker
from typing import List


class CliWorkersController:

    def __init__(self, cli_workers: List[AbstractCliWorker]):
        self.__cli_workers = cli_workers
        self.workers_commands: List[str] = []
        for cli_worker in self.__cli_workers:
            [self.workers_commands.append(command) for command in cli_worker.commands]

    def is_command_available(self, command: str) -> bool:
        return True if command in self.workers_commands else False

    def get_cli_worker(self, command) -> AbstractCliWorker:
        for cli_worker in self.__cli_workers:
            if command in cli_worker.commands:
                return cli_worker
