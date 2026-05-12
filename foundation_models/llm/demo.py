"""Minimal runnable demo for LLM.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "大语言模型",
        "english_name": "LLM",
        "core_idea": "基于海量文本学习通用语言能力",
        "typical_tasks": "对话、推理、代码生成",
        "representative_algorithms": "GPT、Llama、DeepSeek",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
