"""Minimal runnable demo for Graph Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "图学习",
        "english_name": "Graph Learning",
        "core_idea": "利用图结构传播节点关系",
        "typical_tasks": "推荐、社交网络、知识图谱",
        "representative_algorithms": "GCN、GAT、GraphSAGE",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
