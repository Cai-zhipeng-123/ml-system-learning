"""Minimal runnable demo for Supervised Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "监督学习",
        "english_name": "Supervised Learning",
        "core_idea": "利用标签数据学习输入到输出映射",
        "typical_tasks": "分类、回归、排序、序列预测、结构化预测",
        "representative_algorithms": "LR、SVM、XGBoost、CNN、Transformer",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
