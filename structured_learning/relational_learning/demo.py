"""Minimal runnable demo for Relational Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "关系学习",
        "english_name": "Relational Learning",
        "core_idea": "学习实体与关系交互",
        "typical_tasks": "知识图谱推理",
        "representative_algorithms": "TransE、RotatE",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
