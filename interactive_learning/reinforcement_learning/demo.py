"""Minimal runnable demo for Reinforcement Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "强化学习",
        "english_name": "Reinforcement Learning",
        "core_idea": "与环境交互以最大化长期奖励",
        "typical_tasks": "游戏 AI、机器人、推荐、调度",
        "representative_algorithms": "DQN、PPO、A3C",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
