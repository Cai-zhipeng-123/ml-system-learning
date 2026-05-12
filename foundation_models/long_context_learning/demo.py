"""Minimal runnable demo for Long-context Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "长上下文学习",
        "english_name": "Long-context Learning",
        "core_idea": "处理超长序列与记忆",
        "typical_tasks": "长文推理、代码库分析",
        "representative_algorithms": "Transformer-XL、Longformer",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
