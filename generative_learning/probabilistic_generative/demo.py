"""Minimal runnable demo for Probabilistic Generative.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "概率生成学习",
        "english_name": "Probabilistic Generative",
        "core_idea": "建模数据概率分布并生成样本",
        "typical_tasks": "密度估计、生成建模",
        "representative_algorithms": "GMM、HMM",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
