"""Minimal runnable demo for RLHF.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "人类反馈学习",
        "english_name": "RLHF",
        "core_idea": "利用人类偏好优化模型行为",
        "typical_tasks": "大模型对齐、Agent",
        "representative_algorithms": "PPO、DPO",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
