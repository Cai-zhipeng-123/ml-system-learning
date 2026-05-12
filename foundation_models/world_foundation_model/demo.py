"""Minimal runnable demo for World Foundation Model.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "世界模型",
        "english_name": "World Foundation Model",
        "core_idea": "学习世界动态规律与规划",
        "typical_tasks": "机器人、自动驾驶",
        "representative_algorithms": "MuZero、Dreamer",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
