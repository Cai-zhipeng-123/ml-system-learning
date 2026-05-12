"""Minimal runnable demo for Graph Embedding.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "图表示学习",
        "english_name": "Graph Embedding",
        "core_idea": "学习节点或图的低维表示",
        "typical_tasks": "节点分类、链路预测",
        "representative_algorithms": "DeepWalk、Node2Vec",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
