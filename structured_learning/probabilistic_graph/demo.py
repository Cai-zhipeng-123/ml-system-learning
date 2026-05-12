"""Minimal runnable demo for Probabilistic Graph.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "概率图模型",
        "english_name": "Probabilistic Graph",
        "core_idea": "用图表示随机变量依赖关系",
        "typical_tasks": "推断、诊断、时序建模",
        "representative_algorithms": "Bayesian Network、Markov Random Field",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
