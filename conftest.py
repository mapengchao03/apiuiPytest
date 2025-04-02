# import pytest
# import os
# import time
#
# # 清理日志文件夹，保留最近3天的日志文件，其他的删除。
# @pytest.fixture(scope="session", autouse=True)
# def clean_logs():
#     yield
#     if os.path.exists("logs"):
#         # 保留最近3天的日志
#         for f in os.listdir("logs"):
#             file_path = os.path.join("logs", f)
#             if os.stat(file_path).st_mtime < time.time() - 3*86400:
#                 os.remove(file_path)