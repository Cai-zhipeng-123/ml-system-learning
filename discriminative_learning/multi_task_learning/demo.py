"""Minimal runnable demo for Multi-task Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "多任务学习",
        "english_name": "Multi-task Learning",
        "core_idea": "多个相关任务共享表示并联合优化",
        "typical_tasks": "CTR+CVR 预测、多目标推荐、多头预测",
        "representative_algorithms": "Shared-Bottom、MMoE",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
