from pathlib import Path
import shutil
import sys
import os

# 设置 UTF-8 编码，确保 Windows 环境正确处理中文输出
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# 获取项目根目录下的 assets 文件夹路径
assets_dir = Path(__file__).parent.resolve() / "assets"


def configure_ocr_model():
    """配置OCR模型，将默认OCR模型文件复制到项目指定目录"""
    # 源OCR模型所在路径（来自MaaCommonAssets库）
    assets_ocr_dir = assets_dir / "MaaCommonAssets" / "OCR"

    # 检查源OCR模型文件是否存在
    if not assets_ocr_dir.exists():
        print(f"文件未找到: {assets_ocr_dir}")
        sys.exit(1)

    # 目标OCR模型存放路径（项目资源目录）
    ocr_dir = assets_dir / "resource" / "base" / "model" / "ocr"

    # 仅在目标目录不存在时复制默认OCR模型
    # 避免覆盖用户可能已自定义的OCR模型
    if not ocr_dir.exists():
        shutil.copytree(
            # 源路径：使用MaaCommonAssets提供的PPOCR v5中文模型
            assets_ocr_dir / "ppocr_v5" / "zh_cn",
            ocr_dir,  # 目标路径
            dirs_exist_ok=True,  # 允许目录已存在（处理并行执行情况）
        )
        print(f"已成功导入默认OCR模型到: {ocr_dir}")
    else:
        print("发现已存在的OCR目录，跳过默认模型导入。")


if __name__ == "__main__":
    # 执行OCR模型配置
    configure_ocr_model()
    # 提示配置完成（移除重复的 print 语句）
    print("OCR模型配置完成。")
