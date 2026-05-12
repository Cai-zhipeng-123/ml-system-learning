"""Minimal runnable demo for PEFT.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "参数高效迁移",
        "english_name": "PEFT",
        "core_idea": "用少量参数完成模型迁移",
        "typical_tasks": "大模型微调",
        "representative_algorithms": "LoRA、Adapter",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
