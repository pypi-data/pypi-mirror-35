## cli_utils - Useful to implementing fastly a cli interface

# how to use it:
- from cli_utils import AbstractCliWorker, CliInterface
- extend AbstarctCLiWorker: 
- override its method work() 
- create an instance of it defining its worker_name, commands, help
- pass all of your worker to new instance of CliInterface
- make CliInterface instance run()

# concrete example:

```python
from cli_utils import AbstractCLiWorker, CliInterface
  
  
class MyWorker(AbstractCliWorker):
          
    def __init__(self, worker_name: str, commands: List[str], command_help: str):
        super().__init__(worker_name, commands, command_help)        
        
    def work(self, input_val: str):
        print("hello", input_val, "i'm a worker")
    
def main():
    
    my_worker = MyWorker(
        worker_name="my worker",
        commands=["--myworker", "-mw"],
        command_help="it simply print hello you!"
    )
    
    cli_interface = CliInterface(
        workers=[my_worker],
        is_case_sensitiveness_checked=False,
        is_trim_used=True,
        is_hint_used=True,
        welcome_phrase="Welcome to the program"                   
    )
    
