"""Minimal runnable demo for Self-supervised Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "自监督学习",
        "english_name": "Self-supervised Learning",
        "core_idea": "从数据自身构造监督信号学习表征",
        "typical_tasks": "预训练、表示学习、跨模态对齐、Embedding 学习",
        "representative_algorithms": "BERT、SimCLR、MAE、MoCo",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
