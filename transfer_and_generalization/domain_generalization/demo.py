"""Minimal runnable demo for Domain Generalization.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "领域泛化",
        "english_name": "Domain Generalization",
        "core_idea": "学习跨域稳定特征",
        "typical_tasks": "跨设备、跨场景学习",
        "representative_algorithms": "IRM、MetaDG",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
