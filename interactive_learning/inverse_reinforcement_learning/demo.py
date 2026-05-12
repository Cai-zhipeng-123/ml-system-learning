"""Minimal runnable demo for Inverse RL.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "逆强化学习",
        "english_name": "Inverse RL",
        "core_idea": "从行为反推奖励函数",
        "typical_tasks": "自动驾驶、机器人规划",
        "representative_algorithms": "MaxEnt IRL",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
