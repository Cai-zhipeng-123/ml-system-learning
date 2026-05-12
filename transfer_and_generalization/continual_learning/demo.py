"""Minimal runnable demo for Continual Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "持续学习",
        "english_name": "Continual Learning",
        "core_idea": "连续学习多个任务并避免遗忘",
        "typical_tasks": "增量学习、终身学习",
        "representative_algorithms": "EWC、Replay",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
