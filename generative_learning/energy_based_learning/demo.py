"""Minimal runnable demo for Energy-based Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "能量模型",
        "english_name": "Energy-based Learning",
        "core_idea": "用能量函数刻画数据分布",
        "typical_tasks": "密度估计、联想记忆",
        "representative_algorithms": "RBM、Hopfield Network",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
