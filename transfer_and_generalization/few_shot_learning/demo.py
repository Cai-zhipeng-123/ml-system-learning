"""Minimal runnable demo for Few-shot Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "小样本学习",
        "english_name": "Few-shot Learning",
        "core_idea": "用极少样本完成新任务",
        "typical_tasks": "小样本分类、医学 AI",
        "representative_algorithms": "ProtoNet、MatchingNet",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
