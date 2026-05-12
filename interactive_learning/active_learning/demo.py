"""Minimal runnable demo for Active Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "主动学习",
        "english_name": "Active Learning",
        "core_idea": "主动选择最有价值样本进行标注",
        "typical_tasks": "数据标注、人机协同学习",
        "representative_algorithms": "Uncertainty Sampling、QBC",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
