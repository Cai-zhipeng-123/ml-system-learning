"""Minimal runnable demo for Imitation Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "模仿学习",
        "english_name": "Imitation Learning",
        "core_idea": "模仿专家行为学习策略",
        "typical_tasks": "自动驾驶、机器人控制",
        "representative_algorithms": "Behavior Cloning、GAIL",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
