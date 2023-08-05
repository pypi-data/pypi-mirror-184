import array

class ExecutionParams:

    operation:str
    __args__:dict = {}

    def set_arg(self, name:str, value:any = None):
        self.__args__[name] = value if value else name
    
    def get_arg(self, name, default_value:any = None) -> any:
        try:
            return self.__args__[name]
        except Exception as e:
            if str(type(e)) != "<class 'KeyError'>":
                raise e
        return None

    def exists(self, key:str) -> bool:
        value:any = self.get_arg(key)
        return True if value else False

    def exists_swtich(self, switch_key:str) -> bool:
        value:any = self.get_arg(switch_key)
        if not value:
            return False
        return  value == switch_key

def __is_switch__(value:str) -> bool:
    if not value:
        return False
    return value.startswith('--') or value.startswith('-')

def parse_from_args(args:array) -> ExecutionParams:
    if args:
        if len(args) == 0:
            raise Exception('Args not received')

        execution_params:ExecutionParams = ExecutionParams()
        execution_params.operation = args[0]

        key:str = None
        value:str = None
        param_index:int = 1
        while param_index < len(args):
            key = args[param_index]
            if __is_switch__(key):
                execution_params.set_arg(key)
            else:
                param_index += 1
                value = args[param_index]
                execution_params.set_arg(key, value)
            param_index += 1

    return execution_params

