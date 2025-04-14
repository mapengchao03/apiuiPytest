import os, logging
from config import config
from datetime import datetime
from logging.handlers import RotatingFileHandler

def setup_logging():
    # 创建日志目录
    log_dir = config.log_path

    # 生成时间戳 (格式示例: 20231021_153030)
    timestamp = datetime.now().strftime("%Y-%m-%d")

    # 主日志记录器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # ================= 统一日志格式 =================
    formatter = logging.Formatter(
        "%(asctime)s--%(levelname)s--%(filename)s:%(lineno)d--"
        "[%(module)s:%(funcName)s]--%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # ================= 控制台日志配置 =================
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)  # 控制台默认显示INFO及以上级别

    # ================= 全量日志文件配置 =================
    all_log_path = os.path.join(log_dir , f"{timestamp}_all.log")
    all_file_handler = RotatingFileHandler(
        all_log_path,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
        encoding="utf-8"
    )
    all_file_handler.setFormatter(formatter)
    all_file_handler.setLevel(logging.INFO)  # 记录INFO以上级别

    # ================= 错误日志文件配置 =================
    err_log_path = os.path.join(log_dir , f"{timestamp}_err.log")
    error_file_handler = RotatingFileHandler(
        err_log_path,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
        encoding="utf-8"
    )
    error_file_handler.setFormatter(formatter)
    error_file_handler.setLevel(logging.ERROR)  # 记录ERROR及以上级别

    # 添加所有处理器
    logger.addHandler(console_handler)
    logger.addHandler(all_file_handler)
    logger.addHandler(error_file_handler)

    # 防止日志传播到上级logger
    logger.propagate = False

    # 打印日志路径提示
    print(f"日志文件已创建:\n{all_log_path}\n{err_log_path}")


# 初始化日志配置
setup_logging()
# 获取日志记录器
logger = logging.getLogger(__name__)

# 测试日志输出
if __name__ == "__main__":
    logger.debug("Debug级别信息（仅全量文件可见）")
    logger.info("Info级别信息")
    logger.warning("Warning级别信息")
    logger.error("Error级别信息")
    logger.critical("Critical级别信息")