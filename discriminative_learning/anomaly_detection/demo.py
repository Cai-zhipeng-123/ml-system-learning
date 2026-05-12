"""Minimal runnable demo for Anomaly Detection.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "异常检测",
        "english_name": "Anomaly Detection",
        "core_idea": "学习正常模式并识别异常样本",
        "typical_tasks": "欺诈检测、设备故障、网络安全",
        "representative_algorithms": "Isolation Forest、One-Class SVM",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
