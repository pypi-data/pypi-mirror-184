import json
import threading
from logging.config import dictConfig

from flask import Flask, request

from cloud_base_framework.cloud_base_exception import extension_service_illegal_resp, extension_service_not_found, \
    extension_service_biz_error
from cloud_base_framework.cloud_base_log import log_config, log_key

auth_key = 'authId'

dictConfig(log_config)

app = Flask(__name__)


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


@app.route('/base/cloud/spi', methods=['POST'])
def cloud_spi():
    threading.current_thread().__dict__[log_key] = request.headers.get(log_key)
    threading.current_thread().__dict__[auth_key] = request.json.get(auth_key)
    app.logger.info("Spi handler receive request : %s", request.json)
    try:
        method = request.json.get('method')
        # 遍历寻找对应业务类
        for rule in app.url_map.iter_rules():
            if rule.rule != method:
                continue
            # 反序列化 data 值
            request.json['data'] = json.loads(request.json.get('data'), object_hook=JSONObject)
            # 调用业务方法
            func = app.view_functions[rule.endpoint]
            result = func()
            resultJson = json.dumps(result, default=lambda obj: obj.__dict__, ensure_ascii=False)
            app.logger.info("Spi handler response : %s", resultJson)
            # 检查不合法返回值
            if 'code' not in result or 'success' not in result:
                app.logger.error("Spi handler response is invalid! Please use #success_result or #failed_result!")
                return failed_result_with_header(extension_service_illegal_resp.get('code'),
                                                 extension_service_illegal_resp.get('message'))

            return resultJson, 200, [("Content-Type", "application/json")]

        app.logger.error(extension_service_not_found.get('message'))
        return failed_result_with_header(extension_service_not_found.get('code'),
                                         extension_service_not_found.get('message'))
    except Exception as ex:
        app.logger.error("Failed to call biz api! exception: %s", ex)
        return failed_result_with_header(extension_service_biz_error.get('code'),
                                         extension_service_biz_error.get('message'))
    finally:
        # reset
        threading.current_thread().__dict__[log_key] = ""
        threading.current_thread().__dict__[auth_key] = ""


@app.route('/base/health', methods=['GET'])
def health_check():
    return "{\"status\":\"UP\"}"


def success_result(data, code="200"):
    return {
        "success": True,
        "code": code,
        "message": "",
        "data": data
    }


def failed_result(code, message, data=""):
    return {
        "success": False,
        "code": code,
        "message": message,
        "data": data
    }


def failed_result_with_header(code, message, data=""):
    result = failed_result(code, message, data)
    resultJson = json.dumps(result, default=lambda obj: obj.__dict__, ensure_ascii=False)
    return resultJson, 200, [("Content-Type", "application/json")]
