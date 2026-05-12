"""Minimal runnable demo for Masked Modeling.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "掩码生成学习",
        "english_name": "Masked Modeling",
        "core_idea": "预测被遮蔽部分以恢复原数据",
        "typical_tasks": "NLP 预训练、视觉预训练",
        "representative_algorithms": "BERT、MAE",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
