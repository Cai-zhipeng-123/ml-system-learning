"""Minimal runnable demo for Vision Foundation Model.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "视觉基础模型",
        "english_name": "Vision Foundation Model",
        "core_idea": "大规模视觉预训练",
        "typical_tasks": "图像分类、检测、分割",
        "representative_algorithms": "ViT、SAM",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
