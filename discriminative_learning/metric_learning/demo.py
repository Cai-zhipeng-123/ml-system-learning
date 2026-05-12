"""Minimal runnable demo for Metric Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "度量学习",
        "english_name": "Metric Learning",
        "core_idea": "学习距离空间中的相似性度量",
        "typical_tasks": "人脸识别、向量检索、商品匹配",
        "representative_algorithms": "Triplet Loss、Siamese Network",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
