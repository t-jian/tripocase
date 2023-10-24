# -*- coding: UTF-8 -*-

# from test.test_api import TestApi
# if __name__ == '__main__':
#     TestApi().test_post_token()
#     TestApi().test_creatinvoice1()


# import pytest
# if __name__ == '__main__':
#     pytest.main(["-vs"])
import os
import time

import pytest

# from Tripo.Tripo_Api_Automation.common.yaml_util import read_yaml
# from Tripo.Tripo_Api_Automation.common.yaml_util import write_yaml
# from Tripo.Tripo_Api_Automation.common.yaml_util import clear_yaml

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")

    # data = {"year": "1996年"}
    # write_yaml(data)
    # print(read_yaml("name"))
    # print(read_yaml("year"))
    # clear_yaml()
