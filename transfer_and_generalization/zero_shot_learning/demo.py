"""Minimal runnable demo for Zero-shot Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "零样本学习",
        "english_name": "Zero-shot Learning",
        "core_idea": "不见样本直接泛化到新类别",
        "typical_tasks": "开集识别、多模态推理",
        "representative_algorithms": "CLIP、Instruction Tuning",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
