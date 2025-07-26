# api.py
from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/api/run', methods=['POST'])
def run_main():
    """API 触发端点"""
    try:
        # 执行 main.py 并捕获输出
        result = subprocess.run(
            ['python', 'main.py'],
            capture_output=True,
            text=True,
            env=os.environ  # 继承容器环境变量
        )
        return jsonify({
            "status": "success" if result.returncode == 0 else "error",
            "stdout": result.stdout,
            "stderr": result.stderr
        })
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9020)
