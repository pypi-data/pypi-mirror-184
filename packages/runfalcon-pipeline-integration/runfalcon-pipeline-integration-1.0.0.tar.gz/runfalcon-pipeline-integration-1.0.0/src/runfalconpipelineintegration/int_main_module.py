import array
import json
from runfalconpipelineintegration.model_credentials import Credentials
from runfalconpipelineintegration.util_configuration import Configuration
from runfalconpipelineintegration.model_execution_params import ExecutionParams, parse_from_args
from runfalconpipelineintegration.uc_authenticator import Authenticator
from runfalconpipelineintegration.uc_scenario_runner import ScenarioRunner

class ModuleMain:

    __execution_params__:ExecutionParams = None

    def __is_debug_enabled__(self) -> bool:
        return  self.__execution_params__.exists_swtich('--DEBUG') or \
                self.__execution_params__.exists_swtich('-DEBUG') or \
                self.__execution_params__.exists_swtich('DEBUG')

    def __is_quiet__(self) -> bool:
        return  self.__execution_params__.exists_swtich('-q') or \
                self.__execution_params__.exists_swtich('--q')

    def __configure_logger__(self):
        if self.__execution_params__:
            if (self.__is_debug_enabled__()):
                Configuration.instance().set_config_value('LOGGER', 'level', 'DEBUG')
            if (self.__is_quiet__()):
                Configuration.instance().set_config_value('LOGGER', 'quiet', True)

    def __get_credentials__(self) -> Credentials:
        login:str = self.__execution_params__.get_arg('login')
        password:str = self.__execution_params__.get_arg('password')
        if not login:
            raise Exception('Login not received')
        if not password:
            raise Exception('Password not received')
        return Credentials(login, password)

    def __do_authenticate__(self):
        credentials:Credentials = self.__get_credentials__()
        authenticator:Authenticator = Authenticator()
        token:str = authenticator.authenticate(credentials)
        print(token)

    def __job_info_to_string(self, job_info:dict) -> str:
        if not job_info:
            return None
        json_string:str = json.dumps(job_info)
        return json_string

    def __do_run__(self):
        token:str = self.__execution_params__.get_arg('token')
        client:str = self.__execution_params__.get_arg('client')
        application:str = self.__execution_params__.get_arg('application')
        scenario:str = self.__execution_params__.get_arg('scenario')

        if not token:
            raise Exception('Token not received')
        
        if not client:
            raise Exception('Client not received')

        if not application:
            raise Exception('Application not received')

        if not scenario:
            raise Exception('Scenario not received')

        scenario_runner:ScenarioRunner = ScenarioRunner( \
                                                client_name = client, \
                                                application_name = application, \
                                                scenario_code = scenario, \
                                                token = token
                                            )

        job_info:dict = scenario_runner.run_sync()
        print(self.__job_info_to_string(job_info))

    def run(self, args:array):
        self.__execution_params__ = parse_from_args(args)
        self.__configure_logger__()

        if self.__execution_params__.operation == 'authenticate':
            self.__do_authenticate__()
        elif self.__execution_params__.operation == 'run':
            self.__do_run__()
