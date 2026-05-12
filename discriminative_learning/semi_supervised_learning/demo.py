"""Minimal runnable demo for Semi-supervised Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "半监督学习",
        "english_name": "Semi-supervised Learning",
        "core_idea": "利用少量标签与大量无标签数据联合训练",
        "typical_tasks": "图像分类、文本分类、目标检测、医学影像",
        "representative_algorithms": "Pseudo-Label、FixMatch、Label Propagation",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
