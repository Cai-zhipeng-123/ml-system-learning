"""Minimal runnable demo for Autoregressive Modeling.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "自回归生成",
        "english_name": "Autoregressive Modeling",
        "core_idea": "按条件概率逐步生成序列",
        "typical_tasks": "文本生成、代码生成、语音生成",
        "representative_algorithms": "GPT、PixelRNN",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
