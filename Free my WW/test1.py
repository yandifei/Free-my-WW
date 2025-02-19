import sys
import platform
import os
import site
import subprocess
from pprint import pprint
try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata  # Python 3.7及以下兼容

def get_python_info():
    """返回当前 Python 环境的完整信息"""
    info = {}

    # 1. 版本信息
    version_info = {
        "python_version": sys.version,
        "version": sys.version_info,
        "implementation": platform.python_implementation(),
        "compiler": platform.python_compiler(),
        "build_info": {
            "build_no": sys.version_info[2],
            "build_date": sys.version_info[3],
            "build_platform": platform.platform()
        }
    }
    info["version"] = version_info

    # 2. 路径信息
    path_info = {
        "executable": sys.executable,
        "prefix": sys.prefix,
        "base_prefix": sys.base_prefix,
        "exec_prefix": sys.exec_prefix,
        "base_exec_prefix": sys.base_exec_prefix,
        "path": sys.path,
        "site_packages": site.getsitepackages(),
        "user_site": site.getusersitepackages()
    }
    info["paths"] = path_info

    # 3. 环境变量
    env_vars = {
        "python_env_vars": {k: v for k, v in os.environ.items() if k.startswith('PYTHON')},
        "path_env": os.environ.get('PATH', '').split(os.pathsep)
    }
    info["environment"] = env_vars

    # 4. 安装的包（需要安装 setuptools）
    try:
        installed_packages = [
            {
                "name": dist.metadata["Name"],
                "version": dist.version,
                "location": dist.locate_file('')
            }
            for dist in metadata.distributions()
        ]
        info["packages"] = installed_packages
    except Exception as e:
        info["packages_error"] = str(e)

    # 5. 系统信息
    system_info = {
        "os": {
            "name": os.name,
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor()
        },
        "user": {
            "login": os.getlogin(),
            "home": os.path.expanduser("~"),
            "uid": os.getuid(),
            "gid": os.getgid()
        }
    }
    info["system"] = system_info

    # 6. 运行时信息
    runtime_info = {
        "byteorder": sys.byteorder,
        "api_version": sys.api_version,
        "maxsize": sys.maxsize,
        "thread_info": sys.thread_info,
        "argv": sys.argv,
        "std_encoding": {
            "stdin": sys.stdin.encoding,
            "stdout": sys.stdout.encoding,
            "stderr": sys.stderr.encoding
        }
    }
    info["runtime"] = runtime_info

    return info

if __name__ == "__main__":
    # 使用示例
    python_info = get_python_info()
    print("Python 完整信息:")
    pprint(python_info)

    # 获取 requirements.txt 格式的包列表
    print("\n安装的包列表:")
    for pkg in python_info.get('packages', []):
        print(f"{pkg['name']}=={pkg['version']}")