"""Minimal runnable demo for Contrastive Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "对比学习",
        "english_name": "Contrastive Learning",
        "core_idea": "拉近正样本、拉远负样本以学习表示",
        "typical_tasks": "检索、Embedding 学习、推荐、视觉预训练",
        "representative_algorithms": "SimCLR、MoCo、InfoNCE",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
