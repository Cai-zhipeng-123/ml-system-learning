"""Minimal runnable demo for Meta Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "元学习",
        "english_name": "Meta Learning",
        "core_idea": "学习如何快速适应新任务",
        "typical_tasks": "Few-shot Learning、NAS",
        "representative_algorithms": "MAML、ProtoNet",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
