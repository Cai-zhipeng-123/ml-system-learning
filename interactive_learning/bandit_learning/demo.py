"""Minimal runnable demo for Bandit Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "赌博机学习",
        "english_name": "Bandit Learning",
        "core_idea": "在探索与利用之间动态权衡",
        "typical_tasks": "广告推荐、实验优化",
        "representative_algorithms": "UCB、Thompson Sampling",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
