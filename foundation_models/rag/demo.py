"""Minimal runnable demo for RAG.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "检索增强学习",
        "english_name": "RAG",
        "core_idea": "结合外部知识增强生成",
        "typical_tasks": "企业知识库、问答系统",
        "representative_algorithms": "DPR、RAG",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
